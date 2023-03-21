# Assignment 1 
Version 1.2
Deadline: Sunday, 9th of April. Late submissions lead to reduced points.
Minor details may be added later. The main elements should be the same.


# Assignment description 
• The first assignment is to design a cloud-based system which accepts a vCard file (contact
file), sends it to an API, parses it server-side and adds it to a database. 
• The system should be able to return the contacts from the API as JSON or vCard format.
• The front-end should therefore add an interface for reading the file and posting the contents to the API. 
• The API should accept a post, get the vCard text, parse it on the server and add it to the database.
• In addition, you should deliver a short report (max 2 pages). More on this below.


# Specific requirements 
• Server-side programming language: Python
• Database type: MongoDB
• API design: REST


# API 
• POST to [Railway.app-uri]/contacts/ should accept a JSON structure which
includes the vCard plaintext content, parse it, and add the values to the database. An
integer __id should be added as key.

• GET to [Railway.app-uri]/contacts/ should return a JSON list of all contacts
with information, while [Railway.app-uri]/contacts/<id> should get
contact by key (__id). This should be a regular JSON format.

• GET to [Railway.app-uri]/contacts/vcard and [Railway.appuri]/contacts/<id>/vcard should do the same as above but return as vCard
format. (But inside a JSON structure.)


# Report / Deliverables 
The deliverable is the link to the (public) git repo, or a zip file including the repo. It should
only be delivered by one of the group members (you should be able to use git archive for this).

The repo should include a short report on (preferably) maximum 2 pages, which includes
the following (you can use more, but try not to. Unless you use a lot of charts/diagrams/screenshots and such):

• Name of group members.
• Short explanation of which kind of cloud service would fit the best for this type of system (e.g., SaaS, PaaS, IaaS, etc.).
• Short explanation on how the system works (can include diagrams).
• Short explanation of the choices you made during development as well as why you made them.

The assignment repo and report should be delivered on Blackboard within the deadline. It
can be written in either Norwegian or English.


# Recommendations 
Structure the data in the database similar to how JSON/dict would store it. I.e., contacts
should have all contacts. Each contact should have a set of data values, like name, phone
number, email, etc.

We may build further on this system for assignment 2, so it is advisable to make the system
modular and understandable.


# Regarding the requirements 
If some requirements are not satisfied, you will still be graded, but will receive fewer points.
(Each requirement is not weighted equally.)

Exactly how the elements are connected is up to you. Should the API functions call parser
and add to database, or should we have a separate small module/class/function for this? Up
to you.


# Suggested schedule 
You may work in whichever order you want, and at whichever schedule you want. This is
just a suggestion (assuming 4 weeks).

• Week 1: Plan all the functions needed for both client and server.
• Week 2: Start implementing the functions of the server, as well as the web pages for the client.
• Week 3: Connect MongoDB to the server and do tests that the system works.
• Week 4: Perform the measurements of the system and write the required report.