from frappe.model.document import Document
from frappe import _

class ChurchMembers(Document):
    def autoname(self):
        """
        Ultra-resilient naming for church members
        Uses company abbreviation (abbr) instead of branch_code
        """
        try:
            if not self.member_branch:
                self.name = (self.full_name or "").strip()
                return
            
            # Get company abbreviation directly
            company_abbr = frappe.db.get_value("Company", self.member_branch, "abbr") or ""
            
            # Clean and format
            clean_name = (self.full_name or "").strip()
            clean_abbr = company_abbr.strip()
            
            self.name = f"{clean_name}-{clean_abbr}" if clean_abbr else clean_name
            
        except Exception:
            # Final fallback
            self.name = (self.full_name or "").strip()
