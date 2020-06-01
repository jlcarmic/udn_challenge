# Havard Medical School Challenge

## Code Challenge
A key project managed by DBMI is the UDN, Undiagnosed Diseases Network. The UDN
platform is a Django Python app that collects information about participants and allows hospitals
and medical centers to review participant information.

For this test we would like you to create a small Django app to show us how you approach
coding problems and demonstrate some knowledge of the Python ecosystem.

For the project you need to create two views, a form that gathers information on a participant
and a list of all participants with their data in a table.

The form should have character input fields for
* Participant Name
* Participant Age
* Does Participant have any siblings?
* Known environmental exposures
* Known genetic mutations

After submitting information you should be redirected to the list view where each participant and
the values they entered are present. In addition a dropdown box should be present for each
participant that would have 3 values (Not Reviewed, Reviewed - Accepted, Reviewed - Not
Accepted). Changing of this dropdown should save this field alongside the participant data.

### Installation and Setup
This project was written using Python 3.7.3 you will need a virtual environment setup with this version.

All requirements are listed in the `requirements.txt` file. They can be installed using the following command:

```
> pip install -r requirements.txt
```

This project makes use of a SQLite database. You can create the initial database setup using the following command:

```
> python manage.py migrate
```

Once the requirments are installed and database setup, you can start the server using the following command:

```
> python manage.py runserver
```

### Tests
To run the test suite for this project, use the following command:

```
> python manage.py test
```

## Part Two

### What are some measures we could take to secure this application? Not everyone should be able to see the information entered by participants.

Role based access control (RBAC) paired with the principle of least privilege would great improve the security of this application.

RBAC is a mechanism for determining the information an individual has access to via a role they are assigned. This system could create various roles for participants, clinicians, and researchers, all of whom would need different levels of access. Of course an RBAC strategy is not effective if the permissioning for roles is overly permissive. The priniciple of least privilege states that access to information should only be granted to a role when that information is required for the fulfillment of that role's job function. For example, a research may need access to environmental exposure data when reviewing systems but is unlikely to need a person's name or other PII and therefore should not be given access to it.

With the principle of least privilege as a guide, an RBAC system could be designed that secures the dissemination of the information captured by this application to appropriate parties in a way that minimizes data access while facilitating the job functions of all in the program.

### What are some ways in which the above mentioned workflow could be made more dynamic from a UI/UX perspective?

A system like this one is likely to need to capture large amounts of data, however, the entering of that data can quickly become tedious for the user. There are a few things that can help ease that congintive burden.

1) A multipage approach can be used to break up types of information entered. For example, a page for basic demographics separate from a page for genetic mutations. These smaller forms are less overwhelming when first approaching the application and reduce the friction of getting started.

2) A progress bar can help keep a user engaged. While the a multi-page approach can reduce friction, it does not reduce the overall effort required to enter the information. It can also provide its own friction as a user is rewarded with completing a form with yet another form. Progress indicators allow the user to expect more questions and also see that they are proceeding toward a known end.

3) While demographic information like name and age are easy to enter, information like genetic mutations is likely more tedious and error prone. A UI that has a comprehensive list of mutations that can either be selected or auto-completed as the user works on entering this information would greatly reduce user fatigue as well as potential for error. Even if the form is being filled in by a clinician with knowledge of these mutations, manual entry is always tedious and error prone.

These are a few of the UI/UX improvements that could help make this application more approachable.
