# AutoEmailApplier
Tired of constantly sending the same emails to different companies to apply for them? Seeing how they use automation to filter us, I say we do the same with this, The AutoEmailApplier, just save a template into the source code, and fill up the blanks in the form and send. You can also attach pdfs such as your resume or cover letter, or both :D

The main idea of this is simple, we make a script in Python that helps us automate the tediousness of constantly rewriting the same thing over and over and over again for different companies. This ReadMe will be split into afew sections, how the code works, screenshots and how to change stuff so you can add and remove stuff.

# How the code works
First up is the template. The code has the template I personally use to reach out to companies and get a conversation going between me and the company.
![image](https://github.com/user-attachments/assets/db59a480-004a-4221-9056-74f7f1f0ebe7)

You can see parts like such as {your_name} or {company_name}. Those are the parts you will fill up in the form. The template can be changed according to your liking, just make sure that the formattings for the parts you have to fill up are using the curly brackets {}.

Next up is the formatting. This is the part of the code that will specify what you have to fill up when you get the form later on. By default the program will ask you to fill up a number of things, these are tailored to my needs for an internship but you can change them as you please. This includes the following:
- Company Name
- Your Name
- Your Course
- Your University Name
- Your Phone Number
- Your Email Address

![image](https://github.com/user-attachments/assets/a71f97f2-4701-4643-860d-626450669dab)

Adding more formattings will increase the complexity but make the email more detailed and tailored to you.

From there we have the subject, will grab the first line of the template and remove the word 'Subject' as to avoid duplication. So the default subject of any email you send with this program will "Subject: Internship Application – IT/Cybersecurity Position at {company_name}".

![image](https://github.com/user-attachments/assets/f06dc64d-f8f2-4bf9-9b65-1ac4e3d6e3ef)

Following this is the structure. This includes the subject of the email, your email, the company's email (which you will also input later on) and the main email itself.

![image](https://github.com/user-attachments/assets/f72dcac1-8633-4f77-be49-89c2032fdbc2)

Next up is the attachments. This is where you can edit the attachments such as pdfs or word documents. These can be added by adding the file paths into the specified section. If you wish to add more just continue on so.

![image](https://github.com/user-attachments/assets/4ee6ef27-fab4-43eb-94e5-2fffe6dc2873)

If there is something wrong with one of the files the program will automatically skip them.
