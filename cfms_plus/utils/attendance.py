import frappe

def validate_attendance(doc, method):
    """
    Custom validation for Event or Program Attendance TOOL
    """
    if not frappe.db.exists({
        'doctype': 'Event',
        'name': doc.event_program_name,
        'branch': doc.event_branch
    }):
        frappe.throw(f"Event {doc.event_program_name} not found in branch {doc.event_branch}")
