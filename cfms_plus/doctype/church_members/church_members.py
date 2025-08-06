from frappe.model.document import Document
from frappe import _
import frappe

class ChurchMembers(Document):
    def autoname(self):
        """
        Generate name in format: [ABBR]-[FullName] or [FullName] if no abbreviation
        """
        try:
            # Clean the member name
            full_name = (self.full_name or "").strip()
            if not full_name:
                frappe.throw(_("Full Name is required"))
            
            # If no branch specified, use just the name
            if not self.member_branch:
                self.name = full_name
                return
            
            # Get company abbreviation
            company_abbr = frappe.db.get_value(
                "Company", 
                self.member_branch, 
                "abbr"
            ) or ""
            company_abbr = company_abbr.strip().upper()
            
            # Format the final name
            if company_abbr:
                self.name = f"{company_abbr}-{full_name}"
            else:
                self.name = full_name
                
        except Exception as e:
            frappe.log_error(
                title="Church Members Autoname Error",
                message=f"Error in autoname for {self.full_name}: {str(e)}"
            )
            # Fallback to just the name if anything fails
            self.name = (self.full_name or "").strip()