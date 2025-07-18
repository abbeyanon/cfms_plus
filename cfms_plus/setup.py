# ~/Documents/frappe-bench/apps/cfms_plus/cfms_plus/setup.py
def install():
    """Run on app install"""
    import frappe
    frappe.msgprint("Church Management app installed successfully")

def uninstall():
    """Run on app uninstall"""
    import frappe
    frappe.msgprint("Church Management app uninstalled")
