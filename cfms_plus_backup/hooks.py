app_name = "cfms_plus"
app_title = "Cfms Plus"
app_publisher = "Abigael Lemba"
app_description = "An Enhanced Church Finance and ERP System"
app_email = "abigaellemba2@gmail.com"
app_license = "MIT"

# --------------------------------------
# Hooks on document methods and events
# --------------------------------------

doc_events = {
    "Church Branch": {
        "after_insert": "cfms_plus.cfms_plus.doctype.church_branch.church_branch.create_coa",
    },
    "Church Members": {
        "after_insert": "cfms_plus.cfms_plus.doctype.church_members.church_members.generate_member_id",
    },
    "Church Events and Programs": {
        "after_insert": [
            "cfms_plus.cfms_plus.doctype.church_events_and_programs.church_events_and_programs.send_informative_notice",
            "cfms_plus.cfms_plus.doctype.church_events_and_programs.church_events_and_programs.update_event_status"
        ],
        "on_update": "cfms_plus.cfms_plus.doctype.church_events_and_programs.church_events_and_programs.handle_workflow_update",
        "on_submit": "cfms_plus.cfms_plus.doctype.church_events_and_programs.church_events_and_programs.handle_final_approval"
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
    }
    # "Event or Program Attendance TOOL": {
    #     "after_insert": "cfms_plus.cfms_plus.doctype.event_or_program_attendance_tool.event_or_program_attendance_tool.mark_event_attendance",
    # }
}

# --------------------------------------
# Scheduled background tasks
# --------------------------------------

scheduler_events = {
    "daily": [
        "cfms_plus.cfms_plus.doctype.church_events_and_programs.church_events_and_programs.update_event_status"
    ]
}

# --------------------------------------
# Export fixtures (UI-created records)
# --------------------------------------

fixtures = [
    "Custom Field",
    "Property Setter",
    {
        "doctype": "Email Template",
        "filters": [["name", "in", ["Church Members Giving Acknowledgement"]]]
    },
    {
        "doctype": "Client Script",
        "filters": [["name", "in", [
            "Register Member to Group/Ministry",
            "Register in Group/Ministry Doc",
            "Events/Programs Calendar"
        ]]]
    },
    {
        "doctype": "Workflow",
        "filters": [["name", "in", ["Event/Program Workflow"]]]
    },
    {
        "doctype": "Workflow State"
    },
    {
        "doctype": "Workflow Action Master"
    },
    {
        "doctype": "Workspace",
        "filters": [["name", "in", ["CFMS +"]]]
    },
    {
        "doctype": "Role",
        "filters": [["name", "in", ["Pastor"]]]
    }
]

# --------------------------------------
# Post-install script
# --------------------------------------

after_install = "cfms_plus.helpers.install.after_install"

# --------------------------------------
# Custom Calendar JS for DocTypes
# --------------------------------------

calendar_js = {
    "Church Events and Programs": "public/js/church_events_and_programs.js"
}
