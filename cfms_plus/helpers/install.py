# Document to include custom fields in the User doctype.

import frappe
from frappe import _


def after_install():
    """
    Function to create custom fields in the User doctype after app installation.
    """
    custom_fields = [
        # {
        #     "fieldname": "church_branch",
        #     "label": "Church Branch",
        #     "fieldtype": "Link",
        #     "options": "Church Branch",
        #     "insert_after": "full_name",
        #     "description": "CHURCH BRANCH FOR USER."
        # },
     [
  {
    "doctype": "Custom Field",
    "dt": "User",
    "fieldname": "church_branch",
    "label": "Church Branch",
    "fieldtype": "Link",
    "insert_after": "full_name",
    "options": "Church Branch",
    "description": "CHURCH BRANCH FOR USER"
  }
]

        # {
        #     "fieldname": "address",
        #     "label": "Address",
        #     "fieldtype": "Text",
        #     "insert_after": "state"
        # },
        # {
        #     "fieldname": "zipcode",
        #     "label": "Zipcode",
        #     "fieldtype": "Data",
        #     "insert_after": "interests"
        # },
        # {
        #     "fieldname": "currency",
        #     "label": "Currency",
        #     "fieldtype": "Data",
        #     # "options": "Currency", //Might need changes in UI.
        #     "insert_after": "zipcode"
        # }
    ]

    for field in custom_fields:
        create_custom_field("User", field)

    frappe.msgprint(_("Custom fields added to User doctype successfully."))


def create_custom_field(doctype, field_data):
    """
    Creates a custom field in the specified doctype if it doesn't already exist.
    
    Args:
        doctype (str): The name of the doctype to which the field will be added.
        field_data (dict): A dictionary containing field properties.
    """
    # Check if the custom fields exists
    if not frappe.db.exists("Custom Field", {"dt": doctype, "fieldname": field_data["fieldname"]}):
        custom_field = frappe.get_doc({
            "doctype": "Custom Field",
            "dt": doctype,
            "fieldname": field_data["fieldname"],
            "label": field_data["label"],
            "fieldtype": field_data["fieldtype"],
            "insert_after": field_data.get("insert_after"),
            "description": field_data.get("description"),
            "reqd": field_data.get("reqd", 0),
            "unique": field_data.get("unique", 0),
            "length": field_data.get("length", None)
        })
        custom_field.insert()
        frappe.db.commit()
        frappe.logger().info(f"Custom field '{field_data['fieldname']}' added to '{doctype}' doctype.")
    else:
        frappe.logger().info(f"Custom field '{field_data['fieldname']}' already exists in '{doctype}' doctype.")
