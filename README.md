# Cfms Plus

**Cfms Plus** is an Enhanced Church Finance and ERP System built on the [Frappe Framework](https://frappeframework.com/). It is tailored for churches to help manage finances, services, members, and ministry operations effectively.

---

## ✅ Key Features

- 🔹 **Church Branch Management** – Auto-setup of Chart of Accounts when branches are created  
- 🔹 **Member Registration** – Auto-generated Member ID on creation  
- 🔹 **Church Services & Events** – Manage events and programs with workflow approvals  
- 🔹 **Attendance Tracking** – Church service and event attendance tracking by member  
- 🔹 **Member Giving** – Linked contributions with automatic journal entries  
- 🔹 **Background Schedulers** – Auto-update event statuses daily  
- 🔹 **Custom Workflows, Roles & Email Templates** – Predefined for church use cases  
- 🔹 **Client Scripts & Custom Fields** – Enhanced UX with tailored customizations

---

## 📦 Requirements

- [Frappe Framework](https://github.com/frappe/frappe)
- [ERPNext](https://github.com/frappe/erpnext) (for core accounting)

---

## ⚙️ Installation

Make sure you have a running Frappe site with ERPNext installed.

### Step-by-step:

```bash
# Clone the app into your bench's apps directory
cd ~/frappe-bench/apps
git clone https://github.com/abbeyanon/cfms_plus.git
# Install the app on your site
cd ~/frappe-bench
bench --site your_site_name install-app cfms_plus
# Apply database migrations
bench --site your_site_name migrate


📬 Acknowledgement
This project is developed and maintained by Abigael Lemba.

📧 For inquiries or contributions, contact: mbitheabigail20@gmail.com

This project is licensed under the MIT License.
