[![Build Status](https://travis-ci.com/Winternight9/Arbitrator.svg?branch=develop)](https://travis-ci.com/Winternight9/Arbitrator)
# **Arbitrator** 
## **Project Description:**

<p> This application provides a customizable web-based evaluation form with data summarization and status reporting.  Event organizers can create a custom form for their event containing a list of entrants (contestants, projects, presentors, performers, etc) and a set of criteria that they are to be rated on. Criteria may also include guidance (help) on ratings.  There may optionally be space for entering comments. </p>
<p>The event organizers control who can view and submit an evaluation, and the time interval during which submission is allowed.  The organizers can elect to allow self-registration for open events. </p>

---
## **Prerequisite**
- `Python (ver.3.6 or newer)` [download site](https://www.python.org/downloads/)
- `Python modules listed in ` [requirement file](requirements.txt)

---
## **Installation**

First create .env file containing these following configs:
```
DEBUG =True
SECRET_KEY =YOURSECRETKEY
SOCIAL_AUTH_POSTGRES_JSONFIELD =True
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY =YOURGOOLEAPIKEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET =YOURGOOLEAPISECRETKEY
TIME_ZONE =YOURTIMEZONE
```

Second create and activate virtual environment (optional):
```
virtualenv venv
source venv/bin/activate
```

Next install required packages using the following command:
```
pip install -r requirements.txt 
```

Create the migration file using the following command:
```
python manage.py makemigrations
```

Create the database using the following command:
```
python manage.py migrate
```

Collects static files from each of your applications
```
python manage.py collectstatic
```

## **Runing Locally**

Use the following command to run the app locally:

p.s. default port is 8000

```
python manage.py runserver
```

---
## **Team Member**
| Name/Github | ID 
|:--|:--
|[Kasidit Wongpaiboon](https://github.com/BenZacs) |6110545422 
|[Supakorn Tangpremsri](https://github.com/Winternight9) |6110545651
|[Siwat Ponpued](https://github.com/KornSiwat) |6110546640 

---
## **Project Documentation**

- [Project proposal](https://docs.google.com/document/d/1kTY7dEEr1uGpcEcjVZOhP0TgsJtu_pWC3rOKDfO9P_s/edit?usp=sharing)
- Task Board on [Trello](https://trello.com/b/VRIh1G2A/arbitrator)
- [Iteration plan](https://docs.google.com/document/d/1fXLNDfrdQ5OEX7WIRAhF1MOurH1jjK2mBHLmrH1Qhdc/edit?usp=sharing)
- [Iteration script](https://docs.google.com/document/d/1SIVhFa8ENOlhmjqFwTwIH4pjj2gcpML4t7fsYj02RDk/edit?usp=sharing)
- [Code review script & checklist](https://docs.google.com/document/d/1yKp1QEeML1Y40vKWtDQXcF1b86ywMhAMUPt1jFsnZ90/edit?usp=sharing)
- [Github issue tracker](https://github.com/Winternight9/Arbitrator/issues)
