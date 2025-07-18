import frappe
from frappe.utils import getdate
from datetime import datetime, timedelta, time
import calendar

def execute():
    """Main function to be called from bench"""
    try:
        print("\n=== Starting service creation ===")
        
        # Direct SQL query to avoid any model dependencies
        templates = frappe.db.sql("""
            SELECT name, service_name, service_type, 
                   start_time, duration, weekday, notes
            FROM `tabRecurring Church Service`
            WHERE active = 1
        """, as_dict=True)
        
        if not templates:
            print("⚠️ No active templates found")
            return

        created = 0
        for template in templates:
            print(f"\nProcessing: {template['name']}")
            print(f"Start time: {template['start_time']} ({type(template['start_time'])})")
            
            try:
                # Handle time conversion
                if isinstance(template['start_time'], timedelta):
                    seconds = template['start_time'].total_seconds()
                    start_time = time(
                        hour=int(seconds // 3600),
                        minute=int((seconds % 3600) // 60),
                        second=int(seconds % 60)
                    )
                else:
                    # Handle string time
                    time_str = str(template['start_time']).split(' ')[-1].split('.')[0]
                    if time_str.count(':') == 2:
                        h, m, s = time_str.split(':')
                        if len(h) == 1:
                            time_str = f"0{time_str}"
                        start_time = datetime.strptime(time_str, "%H:%M:%S").time()
                    else:
                        print("⏭️ Invalid time format")
                        continue

                # Calculate next date
                weekdays = ["Monday", "Tuesday", "Wednesday",
                           "Thursday", "Friday", "Saturday", "Sunday"]
                try:
                    target_day = weekdays.index(template['weekday'].title())
                    today = getdate().weekday()
                    days_diff = (target_day - today) % 7
                    next_date = getdate() + timedelta(days=days_diff or 7)
                except ValueError:
                    print(f"⏭️ Invalid weekday: {template['weekday']}")
                    continue

                print(f"Next date: {next_date}")

                # Check if service exists
                exists = frappe.db.exists("Church Services Attendance", {
                    "service_type": template['service_type'],
                    "service_date": next_date
                })
                
                if exists:
                    print("⏭️ Service exists")
                    continue

                # Create service document
                end_time = (datetime.combine(getdate(), start_time) + 
                          timedelta(minutes=template['duration'])).time()
                
                doc = {
                    "doctype": "Church Services Attendance",
                    "service_name": f"{template['service_name']} - {next_date.strftime('%b %d')}",
                    "service_type": template['service_type'],
                    "service_date": next_date,
                    "start_time": start_time,
                    "end_time": end_time,
                    "recurring_source": template['name'],
                    "notes": template['notes'] or ""
                }
                
                frappe.get_doc(doc).insert(ignore_permissions=True)
                created += 1
                print("✨ Created successfully")

            except Exception as e:
                print(f"❌ Error: {str(e)}")
                continue

        print(f"\n=== Created {created} services ===")
        frappe.db.commit()

    except Exception as e:
        frappe.db.rollback()
        print(f"🔥 Critical error: {str(e)}")
        raise
