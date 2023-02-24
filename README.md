# django-fundamentals
"<i>Django Fundamentals</i>" course on <i>PluralSight</i> (by Reindert-Jan Ekker).</br>
This repository holds the development process of a web application where the users can play tictactoe, following the course's guidelines.

You can find the instructor's code for this project on the [course's page on PluralSight](https://www.pluralsight.com/courses/django-fundamentals-update).

## Getting Started

Follow all the steps below if you want to get this project up and running on your computer.
> **Note**
> The 'css', 'js', 'fonts' directories within the 'static' directory are copied from the course resources available on the course's page
on PluralSight. I did not downloaded the up-to-date versions in order to have the same code as in the course working.

### Prerequisites

* [Python 3.8.0](https://www.python.org/downloads/release/python-380/)
* [Git](https://git-scm.com/downloads)

### Setup steps (on Windows operating system)

1. Open cmd
2. Go to the directory you want to clone this repository using <i>cd</i> command
3. Clone this GitHub repository on your computer by using either SSH or HTTPS option:</br>
`git clone git@github.com:AnaMaria2019/django-fundamentals.git` (SSH)
4. Change directory to the directory just cloned, <i>django-fundamentals</i>
5. Create a python virtual environment and activate it:</br>
`python -m venv <name_of_the_venv>`</br>
`<name_of_the_venv>\Scripts\activate` - this works only for Windows
6. Install the necessary packages mentioned in the <i>requirements.txt</i> file;</br> in this case: <i>Django</i>, <i>django-crispy-forms</i> - helps with the
styling of the pages that contain forms
`pip install -r requirements.txt`
7. Migrate the migrations that are already present in the project:</br>
`python manage.py migrate`
8. Run the Django server :)</br>
`python manage.py runserver`
