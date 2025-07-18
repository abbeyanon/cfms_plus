from frappe.model.document import Document
from datetime import datetime, time
import frappe

class RecurringChurchService(Document):
    def validate(self):
        """Validate document before saving"""
        
        # 1. Validate required fields for active templates
        if not self.disabled:  # If template is enabled
            if not self.day_of_week:
                frappe.throw("Day of Week is required for active templates")
            
            if not self.church_service_type:
                frappe.throw("Church Service Type is required")
        
        # 2. Standardize and validate start_time
        if self.start_time:
            if isinstance(self.start_time, str):
                try:
                    # Handle both "HH:MM:SS" and "HH:MM" formats
                    time_str = self.start_time.split(' ')[-1].split('.')[0]
                    if len(time_str.split(':')) == 2:  # HH:MM format
                        self.start_time = datetime.strptime(time_str, "%H:%M").time()
                    else:  # HH:MM:SS format
                        self.start_time = datetime.strptime(time_str, "%H:%M:%S").time()
                except ValueError:
                    frappe.throw("Start Time must be in HH:MM or HH:MM:SS format")
            
            # Final validation
            if not isinstance(self.start_time, time):
                frappe.throw("Invalid Start Time format")
        
        # 3. Validate duration
        if not isinstance(self.duration, (int, float)) or self.duration <= 0:
            frappe.throw("Duration must be a positive number (minutes)")
        
        # 4. Validate frequency (if field exists)
        if hasattr(self, 'frequency') and self.frequency != "Weekly":
            frappe.throw("This template only supports Weekly frequency")

    def before_save(self):
        """Format fields before saving"""
        # Ensure day_of_week is properly capitalized
        if self.day_of_week:
            self.day_of_week = self.day_of_week.title()