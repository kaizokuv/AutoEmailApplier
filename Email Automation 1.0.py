import smtplib
import ssl
from email.message import EmailMessage
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Email Template
TEMPLATE = """Subject: Internship Application – IT/Cybersecurity Position at {company_name}

Dear HR Department of {company_name},

I hope this message finds you well. My name is {your_name}, and I am currently pursuing a degree in {your_course} at {your_university}. I am reaching out to express my interest in an internship opportunity at {company_name}, possibly a role in any IT related departments. I am passionate about technology and security, and I have developed hands-on experience through both academic projects and personal learning. I am confident that an internship with your organization would be an incredible opportunity to grow and contribute meaningfully to your team.

I would be grateful for the opportunity to further discuss how I can contribute to {company_name}.

Thank you for your time and consideration. I look forward to your response.

You can find a copy of my resume, cover letter, and university support letter attached if necessary.

Sincerely,  
{your_name}  
{your_phone_number}  
{your_email_address}
"""

# Email Sending Function
def send_email(data):
    msg = EmailMessage()

    filled_template = TEMPLATE.format(
        company_name=data["company_name"],
        your_name=data["your_name"],
        your_course=data["your_course"],
        your_university=data["your_university"],
        your_phone_number=data["your_phone_number"],
        your_email_address=data["your_email_address"]
    )

    subject = filled_template.splitlines()[0].replace("Subject: ", "")
    body = "\n".join(filled_template.splitlines()[1:])

    msg['Subject'] = subject
    msg['From'] = data["your_email_address"]
    msg['To'] = data["company_email_address"]
    msg.set_content(body)

    # Attach PDFs
    attachments = [
        "Add File Paths Here"
    ]

    for filepath in attachments:
        try:
            filename = filepath.split("/")[-1]
            with open(filepath, "rb") as f:
                file_data = f.read()
                msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=filename)
        except FileNotFoundError:
            messagebox.showwarning("File Missing", f"File not found: {filepath} (skipped)")

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(data["your_email_address"], data["your_email_password"])
            server.send_message(msg)
            messagebox.showinfo("Success", f"Email sent to {data['company_email_address']}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email:\n{e}")

# GUI Entry Points
def launch_gui():
    def on_submit():
        data = {
            "your_email_address": email_entry.get().strip(),
            "your_email_password": password_entry.get().strip(),
            "your_name": name_entry.get().strip(),
            "your_course": course_entry.get().strip(),
            "your_university": university_entry.get().strip(),
            "your_phone_number": phone_entry.get().strip(),
            "company_name": company_entry.get().strip(),
            "company_email_address": company_email_entry.get().strip()
        }

        if all(data.values()):
            send_email(data)
        else:
            messagebox.showwarning("Missing Data", "Please fill in all fields.")

    # Build Window
    root = tk.Tk()
    root.title("Automated Email Sender")

    fields = [
        ("Your Gmail Address:", "email_entry"),
        ("Your Gmail App Password:", "password_entry"),
        ("Your Full Name:", "name_entry"),
        ("Your Course Name:", "course_entry"),
        ("Your University:", "university_entry"),
        ("Your Phone Number:", "phone_entry"),
        ("Company Name:", "company_entry"),
        ("Company Email Address:", "company_email_entry")
    ]

    # Info label (App Password)
    AppPass_label = tk.Label(root, text="Don't have an App Password? Click here", fg="blue", cursor="hand2")
    AppPass_label.grid(row=len(fields), columnspan=2, pady=(0, 5))

    # Make it clickable (App Password)
    def AppPass_link(event):
        import webbrowser
        webbrowser.open("https://myaccount.google.com/apppasswords")
    AppPass_label.bind("<Button-1>", AppPass_link)

    # Info label (GitHUb)
    GitHub_label = tk.Label(root, text="Fancy this project? Come check out my others at GitHub :D", fg="blue", cursor="hand2")
    GitHub_label.grid(row=len(fields) + 1, columnspan=2, pady=(0, 5))

    # Make it clickable (GitHub)
    def GitHub_link(event):
        import webbrowser
        webbrowser.open("https://github.com/kaizokuv")
    GitHub_label.bind("<Button-1>", GitHub_link)

    entries = {}
    for i, (label_text, var_name) in enumerate(fields):
        tk.Label(root, text=label_text).grid(row=i, column=0, sticky="w", padx=10, pady=5)
        if "password" in var_name:
            entry = tk.Entry(root, show="*", width=40)
        else:
            entry = tk.Entry(root, width=40)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[var_name] = entry

    # Assign entries to global names
    email_entry = entries["email_entry"]
    password_entry = entries["password_entry"]
    name_entry = entries["name_entry"]
    course_entry = entries["course_entry"]
    university_entry = entries["university_entry"]
    phone_entry = entries["phone_entry"]
    company_entry = entries["company_entry"]
    company_email_entry = entries["company_email_entry"]

    submit_btn = ttk.Button(root, text="Send Email", command=on_submit)
    submit_btn.grid(row=len(fields) + 2, columnspan=2, pady=15)

    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    launch_gui()
