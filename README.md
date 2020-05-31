# Havard Medical School Challenge

## The Challenge
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

## Installation and Setup
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

## Tests
To run the test suite for this project, use the following command:

```
> python manage.py test
```
