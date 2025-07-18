import frappe
from frappe.model.document import Document

class EventOrProgramAttendanceTOOL(Document):
    def validate(self):
        """Validate ONLY standard Events"""
        if not frappe.db.exists('Event', self.event_program_name):
            frappe.throw(f"Standard Event required: {self.event_program_name} not found")
        
        # Optional branch validation
        if hasattr(self, 'event_branch'):
            event_branch = frappe.db.get_value('Event', self.event_program_name, 'branch')
            if event_branch != self.event_branch:
                frappe.throw(f"Branch mismatch: Event belongs to {event_branch}")
