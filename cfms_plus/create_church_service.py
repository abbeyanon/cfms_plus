import frappe
from frappe.utils import getdate

def create_service():
    try:
        service = frappe.get_doc({
            "doctype": "Church Services Attendance",
            "service_date": getdate(),
            "start_time": "09:00:00",
            "end_time": "12:00:00"
        }).insert()
        
        frappe.db.commit()
        print(f"Service created: {service.name}")
        return service
        
    except Exception as e:
        frappe.log_error("Service creation failed")
        raise

if __name__ == "__main__":
    create_service()
