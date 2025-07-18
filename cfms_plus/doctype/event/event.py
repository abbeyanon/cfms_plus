from __future__ import unicode_literals
import frappe

def send_informative_notice(doc, method):
    frappe.msgprint("Sending notice for new event")

def update_event_status(doc, method):
    doc.status = "Open"
    doc.save()

def handle_workflow_update(doc, method):
    frappe.msgprint(f"Workflow updated to {doc.workflow_state}")

def handle_final_approval(doc, method):
    frappe.msgprint("Event finally approved")
