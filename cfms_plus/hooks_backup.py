# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cfms_plus.utils.attendance import validate_attendance

app_name = "cfms_plus"
app_title = "Cfms Plus"
app_publisher = "Abigael Lemba"
app_description = "An ENhanced Church Finance and ERP System"
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
        "cfms_plus.utils.events.update_event_statuses"
    ]
    "daily": [
        "cfms_plus.cfms_plus.doctype.recurring_church_service.recurring_church_service.create_weekly_services"
    ]
}

# ------------------
# Fixtures (COMPLETELY FIXED)
# ------------------
fixtures = [
    {"doctype": "DocType", "filters": [["name", "in", ["User"]]]},
    {"doctype": "Email Template", "filters": [["name", "in", ["Church Members Giving Acknowledgement"]]]},
    {"doctype": "Client Script", "filters": [["name", "in", ["Register Member to Group/Ministry", "Register in Group/Ministry Doc", "Events/Programs Calendar"]]]},
    {"doctype": "Workflow", "filters": [["name", "in", ["Event/Program Workflow"]]]},
    {"doctype": "Workflow State"},
    {"doctype": "Workflow Action Master"},
    {"doctype": "Workspace", "filters": [["name", "in", ["CFMS +"]]]},
    {"doctype": "Role", "filters": [["name", "in", ["Pastor"]]]}
]

# ------------------
# Calendar JS
# ------------------
calendar_js = {
    "Event": "public/js/event.js"
}
