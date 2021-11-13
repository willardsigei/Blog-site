# Blog~Site

## Description
This is a personal blogging website where you can create and share your blogs and also comment on blogs. For users to do anything with the app, they need to register first. 

## By [Willard Sigei]


## User Stories
Users can do the following with the app:
* View the different blogs.
* See the blogs other people have posted.
* Comment on the different blogs and leave feedback.
* Submit new blogs.
* Delete blogs

## BDD
| Behaviour | Input | Output |
| --------------- | :----------:| --------: |
|Display Blogs | **Click** on Blogs| A page with a list of blogs |
|Add new blog | **Click** New Blog | User Should register/sign in to add new blog |
|View Blogs | **Click** on Blogs | View a blog and comments |
|Comment on a blog | **Click** Comment icon| Registered User displays a form where a user can comment on a certain blog |
|Delete a blog | **Click** delete icon | Blog is deleted|
|Close a blog | **Click** Home(navbar) | Returns to homepage |

## Technologies used
* Python3.8
* Flask framework
* HTML & CSS
* POSTGRESS

## Setup/Installation Requirements
* internet access
* $ git clone 
* $ cd blog-app (project-name)
* $ python3.8 -m venv virtual (install virtual environment)
* $ source virtual/bin/activate
* $ python3.8 -m pip install -r requirements.txt ( to install all the dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
* $ ./start.sh
* The app runs and you can make changes.


# CREDITS

#### Google.com, StackOverflow.com and Miguel Grinberg -author of 'Flask Web Development, 2nd Edition'


# Support and Contacts

In case You have any issues using this code please do no hesitate to get in touch with me through protich12@gmail.com or leave a commit here on github.


## Technologies Used
- Python3.8
- Flask framework
- HTML
- Bootstrap
- PostgreSQL


# Figma Wireframe Design Link.


## License
* [[License: MIT]](LICENSE.md)
* Copyright (c) 2021 **Willard Sigei**