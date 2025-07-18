# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cfms_plus.utils.attendance import validate_attendance

app_name = "cfms_plus"
app_title = "Cfms Plus"
app_publisher = "Abigael Lemba"
app_description = "An Enhanced Church Finance and ERP System"
app_email = "mbitheabigail20@gmail.com"
app_license = "mit"

# ------------------
# Document Events
# ------------------
doc_events = {
    "Company": {},
    "Church Members": {
        "after_insert": "cfms_plus.cfms_plus.doctype.church_members.church_members.generate_member_id",
    },
    "Questionnaire for Events and Programs": {
        "after_insert": "cfms_plus.cfms_plus.doctype.questionnaire_for_events_and_programs.questionnaire_for_events_and_programs.save_attendance",
    },
    "Church Services Attendance": {
        "on_submit": "cfms_plus.cfms_plus.doctype.church_services_attendance.church_services_attendance.update_member_attendance",
    },
    "Church Collections": {
        "after_insert": "cfms_plus.cfms_plus.doctype.church_collections.church_collections.update_member",
        "on_submit": "cfms_plus.cfms_plus.doctype.church_collections.church_collections.create_journal_entry"
    },
    "Event or Program Attendance TOOL": {
        "validate": "cfms_plus.cfms_plus.doctype.event_or_program_attendance_tool.event_or_program_attendance_tool.validate"
    }
}

# ------------------
# Scheduled Tasks
# ------------------
scheduler_events = {
    "daily": [
        "cfms_plus.utils.service_scheduler.create_weekly_services", 
        "cfms_plus.utils.events.update_event_statuses"
    ]
}

# ------------------
# App Setup Hooks
# ------------------
def on_app_install():
    """Run when app is installed"""
    pass

def on_app_uninstall():
    """Run when app is uninstalled"""
    pass

# ------------------
# Include JS/CSS
# ------------------
app_include_css = "/assets/cfms_plus/css/church.css"
app_include_js = "/assets/cfms_plus/js/church.js"

# ------------------
# DocType Class Overrides
# ------------------
override_doctype_class = {
    "Church Services Attendance": "cfms_plus.overrides.church_attendance.CustomChurchAttendance"
}

# ------------------
# Fixtures
# ------------------
fixtures = [
    "Custom Field",
    "Property Setter",
   # "Custom Script",
    "Client Script",
    "Print Format",
    "Email Template",
    "Workflow",
    "Workflow State",
    "Workflow Action Master",
    "Role",
    "Workspace",
    "Translation",
    "Report"
]

# ------------------
# Calendar JS
# ------------------
calendar_js = {
    "Event": "public/js/event.js"
}
