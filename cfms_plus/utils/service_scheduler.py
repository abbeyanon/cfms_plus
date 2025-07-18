# This file is located at ~/Documents/frappe-bench/apps/cfms_plus/cfms_plus/utils/service_scheduler.py

import frappe
from datetime import datetime, timedelta, time

@frappe.whitelist() # This decorator is good practice for scheduled functions
def create_weekly_services():
    """
    Logic to create church services based on recurring templates.
    This function will be called automatically by the Frappe scheduler.
    """
    print("\n=== Frappe Scheduler: Starting service creation ===") # This will show in scheduler logs

    try:
        # Direct SQL query to get recurring service templates
        templates = frappe.db.sql("""
            SELECT name, service_name, service_type,
                   start_time, duration, weekday, notes
            FROM `tabRecurring Church Service`
            WHERE active = 1
        """, as_dict=True)

        if not templates:
            print("⚠️ No active templates found by scheduler")
            frappe.log_by_ajax("⚠️ No active templates found by scheduler") # Log to Frappe UI
            return

        created = 0
        for template in templates:
            print(f"\nProcessing: {template['name']}")
            frappe.log_by_ajax(f"Processing: {template['name']}") # Log to Frappe UI
            print(f"Start time: {template['start_time']}")
            frappe.log_by_ajax(f"Start time: {template['start_time']}")

            try:
                # Handle time conversion (same logic as your working script)
                if isinstance(template['start_time'], timedelta):
                    seconds = template['start_time'].total_seconds()
                    start_time = time(
                        hour=int(seconds // 3600),
                        minute=int((seconds % 3600) // 60),
                        second=int(seconds % 60)
                    )
                else:
                    time_str = str(template['start_time']).split(' ')[-1].split('.')[0]
                    if time_str.count(':') == 2:
                        h, m, s = time_str.split(':')[:3]
                        if len(h) == 1:
                            time_str = f"0{h}:{m}:{s}"
                        start_time = datetime.strptime(time_str, "%H:%M:%S").time()
                    else:
                        print(f"⏭️ Invalid time format for {template['name']}")
                        frappe.log_by_ajax(f"⏭️ Invalid time format for {template['name']}")
                        continue

                # Calculate next date (same logic as your working script)
                weekdays = ["Monday", "Tuesday", "Wednesday",
                           "Thursday", "Friday", "Saturday", "Sunday"]
                try:
                    target_day = weekdays.index(template['weekday'].title())
                    today = datetime.now().weekday()
                    days_diff = (target_day - today) % 7
                    if days_diff == 0 and datetime.now().time() > start_time:
                         days_diff = 7 # Schedule for next week if today is the day but time has passed
                    elif days_diff == 0 and datetime.now().time() <= start_time:
                         days_diff = 0 # Schedule for today if it's the day and time is still future
                    elif days_diff < 0: # Target day already passed this week
                         days_diff += 7 # Schedule for next week

                    next_date = (datetime.now() + timedelta(days=days_diff)).date()
                except ValueError:
                    print(f"⏭️ Invalid weekday: {template['weekday']} for {template['name']}")
                    frappe.log_by_ajax(f"⏭️ Invalid weekday: {template['weekday']} for {template['name']}")
                    continue

                print(f"Next date: {next_date}")
                frappe.log_by_ajax(f"Next date: {next_date}")


                # Check if service exists for the calculated next_date
                exists = frappe.db.sql("""
                    SELECT name FROM `tabChurch Services Attendance`
                    WHERE service_type = %s AND service_date = %s
                """, (template['service_type'], next_date))

                if exists:
                    print(f"⏭️ Service of type {template['service_type']} already exists for {next_date}")
                    frappe.log_by_ajax(f"⏭️ Service of type {template['service_type']} already exists for {next_date}")
                    continue

                # Create service document (same logic as your working script)
                end_time = (datetime.combine(datetime.now(), start_time) +
                          timedelta(minutes=template['duration'])).time()

                doc = {
                    "doctype": "Church Services Attendance",
                    "service_name": f"{template['service_name']} - {next_date.strftime('%b %d')}",
                    "service_type": template['service_type'],
                    "service_date": next_date,
                    "start_time": start_time,
                    "end_time": end_time,
                    "recurring_source": template['name'],
                    "notes": template['notes'] or "",
                    "church_branch": "JCC THIKA RD"
                }

                frappe.get_doc(doc).insert(ignore_permissions=True)
                created += 1
                print("✨ Created successfully")
                frappe.log_by_ajax("✨ Created successfully")


            except Exception as e:
                print(f"❌ Error for {template['name']}: {str(e)}")
                frappe.log_by_ajax(f"❌ Error for {template['name']}: {str(e)}")
                frappe.db.rollback() # Rollback if one creation fails
                continue # Continue to next template if one fails

        frappe.db.commit() # Commit all changes at the end
        print(f"\n=== Frappe Scheduler: Created {created} services ===")
        frappe.log_by_ajax(f"\n=== Frappe Scheduler: Created {created} services ===")


    except Exception as e:
        print(f"❌ Global Error in scheduler: {str(e)}")
        frappe.log_by_ajax(f"❌ Global Error in scheduler: {str(e)}")
        frappe.db.rollback()
