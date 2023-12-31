<div align=center>

# Hands Home Helpers

![last update](https://img.shields.io/badge/Last_update:-19.08.2023-9d3f3f)

![deployment](https://img.shields.io/static/v1?label=deployed&message=Yes&color=success&style=plastic)
![deployment platform](https://img.shields.io/static/v1?label=plateform&message=Heroku&color=634987&style=plastic)
![coverage](https://img.shields.io/static/v1?label=coverage&message=85%&color=success&style=plastic)

This project aims to create a website for the Hands Home Helpers company, based in NRW, GERMANY, so they can have an online presence to promote their activity and reach new customers. The website also aims to provide a user-friendly interface to make contact between the company and its customers easier.

Hands Home Helpers is a premium housekeeping company with a wide range of services. They offer to take care of your house and garden duties as well as maintain your swimming pool and fix small issues or do small renovations. Finally, they also provide a home care service to assist you in your everyday life.

![Mockup responsive](documentation/amiresponsive_home.png)

**- by Yannick Ferenczi -**

**[Live site](https://hands-home-helpers-website-a2058240b625.herokuapp.com/) | [Repository](https://github.com/yannickferenczi/hands-home-helpers-website)**

-- built with --
<p style="background-color: white; padding: 5px; display: inline-block; margin: 0 auto;">

<img src="https://www.vectorlogo.zone/logos/w3_html5/w3_html5-icon.svg" alt="html5" width="40" height="40"/>
<img src="https://www.vectorlogo.zone/logos/w3_css/w3_css-icon.svg" alt="css3" width="40" height="40"/>
<img src="https://www.vectorlogo.zone/logos/javascript/javascript-icon.svg" alt="javascript" width="40" height="40"/>
<img src="https://www.vectorlogo.zone/logos/getbootstrap/getbootstrap-icon.svg" alt="bootstrap" width="40" height="40"/>
<img src="https://www.vectorlogo.zone/logos/python/python-icon.svg" alt="python" width="40" height="40"/>
<img src="https://www.vectorlogo.zone/logos/postgresql/postgresql-icon.svg" alt="postgresql" width="40" height="40"/>
<img src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" alt="heroku" width="40" height="40"/>
<img src="https://www.vectorlogo.zone/logos/markdown-here/markdown-here-icon.svg" alt="markdown" width="40" height="40"/>

</p>

</div>

---

<div align="center">

## 1. Table of Content

</div>

  - [1. Table of Content](#1-table-of-content)
  - [2. UX Design](#2-ux-design)
    - [2.1. Strategy Plane](#21-strategy-plane)
      - [2.1.1. Business Plan](#211-business-plan)
      - [2.1.2. Goals and objectives](#212-goals-and-objectives)
      - [2.1.3. Target Audience](#213-target-audience)
        - [2.1.3.1. User Research](#2131-user-research)
        - [2.1.3.2. Buyer Personas](#2132-buyer-personas)
    - [2.2. Scope Plane](#22-scope-plane)
      - [2.2.1. Define Must-Have Features](#221-define-must-have-features)
      - [2.2.2. Define Information to provide (content requirements)](#222-define-information-to-provide-content-requirements)
    - [2.3. Structure Plane](#23-structure-plane)
      - [2.3.1. Interaction Design (IXD)](#231-interaction-design-ixd)
        - [2.3.1.1. Define Pages](#2311-define-pages)
        - [2.3.1.2. Handle errors](#2312-handle-errors)
        - [2.3.1.3. Flow Chart](#2313-flow-chart)
      - [2.3.2. Information Architecture (IA)](#232-information-architecture-ia)
    - [2.4. Skeleton Plane](#24-skeleton-plane)
      - [2.4.1. Wireframes](#241-wireframes)
    - [2.5. Surface Plane](#25-surface-plane)
      - [2.5.1. Color Palette](#251-color-palette)
      - [2.5.2. Font Choices](#252-font-choices)
    - [2.6. Database Schema](#26-database-schema)
  - [3. Agile Development](#3-agile-development)
    - [3.1. The workflow](#31-the-workflow)
    -   3.2. Labels](#32-labels)
    - [3.3. The views of the project manager](#33-the-views-of-the-project-manager)
    - [3.4. The story points](#34-the-story-points)
    - [3.5. The sprints](#35-the-sprints)
  - [4. Features](#4-features)
    - [4.1. Features currently available](#41-features-currently-available)
    - [4.2. More features to implement](#42-more-features-to-implement)
  - [5. Technology Used](#5-technology-used)
  - [6. Testing](#6-testing)
  - [7. Deployment](#7-deployment)
    - [7.1. Project Creation](#71-project-creation)
    - [7.2. Deployment to Heroku](#72-deployment-to-heroku)
    - [7.3. Local Development](#73-local-development)
  - [8. Credits](#8-credits)
  - [9. Acknowledgements](#9-acknowledgements)


---

<div align="center">

## 2. UX Design

</div>

### 2.1. Strategy Plane

#### 2.1.1. Business Plan

What problem will the business solve?

> Todos at home take a huge amount of time lessing less time for people to enjoy their hobby/family

What will the business provide to solve that problem?

> Provide a team of qualified workers to take care of their most complicated or annoying tasks and to provide assistance.

How will the business make money?

> The business makes money by providing really high-quality work and an 'all-in-one' solution to the housekeeping matter.

Who will purchase our products or services?

> The potential customers of the business can be:
> - retired people in need of assistance for some particular tasks (they have time to take care of most of their duties but need help with the heavy ones)
> - High-standing people with big properties, including facilities such as a swimming pool for instance, which are nice to have when well maintained but mean too much care.

How will our target customers learn about our business?

> Promotion on social media, in Gardening shops, and with an online presence.

What will the business do better than the competitors?

> The business will bring efficiency (with the all-in-one concept), high-quality results, and flexibility.

How much money do you

- need to start?
- spend every month?
- earn every month?

  > To be able to run fully featured, the business needs two employees (one competent in gardening, swimming pool caring, and doing small repairs/installation and one competent in cleaning)
  > To start: 7 000 € | every month: + 8 712 € / - 5 200 €
  > This brings a 40% margin to the business which should be spread like below:
  > - 10% employee training
  > - 10% company equipment
  > - 10% marketing
  > - 10% profit

How much money do you need to start and operate the business?

> 0, the business owner will start with their own funds.

#### 2.1.2. Goals and objectives

Objectives for the website are:

- An easy-to-navigate website with a clear purpose
- Allow users to create a personal account
- To provide users with insights or tips on how to take good care of their home and garden.

The goals for the site owner are:

- have an online presence
- promote their business
- reduce customer solicitations by providing them an online booking system and a FAQs page

The goals for the site user are:

- discover the purpose of the business
- discover the offers of the business
- get insights and tips on how they could improve the quality of their housekeeping
- list their home tasks

#### 2.1.3. Target Audience

Hands Home Helpers is a B2C company.

##### 2.1.3.1. User Research

A user research has been ran on 85 persons.

Important information out of it is as below:

- nearly 100% of households with an income higher than 7 000 € per month use housekeeping services

- what they value most is personal growth, time with their friends and family, health and wellness

- the household average constitution for people using housekeeping services is as below:

  - 5 persons
  - 5 bedrooms
  - 3 bathrooms

- important for them when choosing a vendor:

  1. good customer review average
  2. physical presence nearby
  3. easy-to-use services

- important when choosing a housekeeping provider:

  1. trustworthy (qualified workers and clear insurance policy)
  2. reliability
  3. flexibility

- average frequency is once or twice per week

- most common required services are

  1. house cleaning
  2. gardening
  3. swimming pool caring
  4. fixing or installing things at home
  5. garden patch caring (70% would appreciate having their own vegetables but do not have time to take care of their garden patch)

- specific areas with special attention:

  1. high-standing kitchen
  2. bathroom with marble

- three budget classes could be identified:

  1. full help required => 21 hours per week (3 days x 7 hours) => 2 745 € per month (30 € per hour)
  2. smaller full help required => 12 hours per week (2 days x 6 hours) => 1 673 € per month (32 € per hour)
  3. minimum help required => 5 hours per week (on 1 day) => 762.5 € per month (35 € per hour)

- the preferred payment method for housekeeping services is the subscription for 85% of those service users. They would also mostly appreciate keeping the benefit of unused hours for the following month.

- the preferred booking method is online booking with 68% and then calling with 25%

- the preferred communication method is online chat and calling with 40% for both

- most reasons they would change their housekeeping services are:
  1. the price
  2. all in one (they could replace their different providers for house cleaning, gardening, and repairs with one single provider)

##### 2.1.3.2. Buyer Personas

Out of the user research, two personas have been created to understand and illustrate in a more concrete representation the ideal customer of Hands Home Helpers.

Persona 1:
![Persona 1](documentation/Persona_1.png)

Persona 2:
![Persona 2](documentation/Persona_2.png)

### 2.2. Scope Plane

In this particular project, there are two kinds of minimum viable products (MVP).

1. The first one, which is educationally oriented, is to provide everything expected for the assessment criteria to pass. So everything will at first be developed regarding this scope.
2. Nevertheless, with the first MVP, the business would not be competitive. So the second MVP, which is more business-oriented, is to provide the website with a real value that could give the business an edge over its competitors. This must be developed too.

#### 2.2.1. Define Must-Have Features

EVERY WEB PROJECT MUST-HAVE FEATURES:

- responsive navigation menu
- logo
- social media links
- error 404 page
- error 500 page
- favicon

NOTIFICATIONS:

To create a positive user experience, notifications will be provided when users are taking actions such as:

- confirmation of registration
- confirmation of login
- confirmation of item created
- confirmation on item successfully edited
- confirmation request when the user wants to delete an item
- confirmation item successfully deleted

AUTHENTICATION SYSTEM:

An authentication system is mandatory and should allow users to

- register
- login
- Logout
- have access to restricted features

TASK MANAGEMENT SYSTEM:

A task management system will help users to communicate with the company on their tasks in an easy way. This system should allow users to

- create new tasks (C)
- list their tasks (R)
- modify their tasks (U)
- delete their tasks (D)

CONTACT FORM

A contact form should be available for users to contact the company in the most convenient way.

#### 2.2.2. Define Information to provide (content requirements)

In the first MVP scope, the needed information is:

- explain the purpose of the website
- indicate users how to use the website by naming links and features with intuitive words

### 2.3. Structure Plane

#### 2.3.1. Interaction Design (IXD)

##### 2.3.1.1. Define Pages

- landing page
- registration page
- login page
- Logout page
- tasks list page
- add task page
- task detail page
- edit the task page
- about page (including meet the team section, FAQ section, and review section)

##### 2.3.1.2. Handle errors

Error-404 and error-500 pages are also to be implemented within the MVP scope.

##### 2.3.1.3. Flow Chart

A flowchart has been design to help stakeholders with the development of the website:

![flowchart for the minimum viable product](documentation/flowchart_mvp.png)

#### 2.3.2. Information Architecture (IA)

information is organized with some known patterns so that users easily find what they are looking for such as:

- navigation menu on the top right
- name and logo on the top left
- social media links in the footer
- company address and contact in the footer

### 2.4. Skeleton Plane

#### 2.4.1. Wireframes

Wireframes have been adapted during the development phase to offer a better user experience.

Landing page:
![Landing page wireframe](documentation/index_wireframe.png)

Registration page:
![Registration page wireframe](documentation/signup_wireframe.png)

Login page:
![Login page wireframe](documentation/login_wireframe.png)

List of tasks page:
![Tasks listing page wireframe](documentation/tasks-list_wireframe.png)

Task detail page:
![Task detail page wireframe](documentation/task-detail_wireframe.png)

Edit task page:
![Edit task page wireframe](documentation/edit-task_wireframe.png)

Error-404 page:
![Error 404 page wireframe](documentation/error-404_wireframe.png)

Error-500 page:
![Error 500 page wireframe](documentation/error-500_wireframe.png)

### 2.5. Surface Plane

#### 2.5.1. Color Palette

Three colors have been chosen on top of black and white.
The first color (#9d3f3f) is the color of the logo: The ant. This logo has been picked to communicate how brave and hardworking are the employees and how efficient will be the working hours. The other colors have been selected using a color calculator to be the best fit for this very first color.

![Color palette of the project](documentation/color_palette.png)

#### 2.5.2. Font Choices

Two fonts have been used within the whole website. They both are sans-serif. Andika has been picked for the titles to give users a feeling of soberness and neatness. And Merriweather Sans has been picked for the standard text as it is a good match for Andika.

### 2.6. Database Schema

The database schema has been modified during the development phase to provide a more powerful tool.

For the minimum viable product:
![Database schema for the minimum viable product](documentation/erd_mvp.png)

The first extension of the erd:
![Database schema with the first extension](documentation/erd_extanded_1.png)

[Back to the Table of Content](#1-table-of-content)

---

<div align="center">

## 3. Agile Development

</div>

The project development has been managed with an agile project manager on GitHub. It is public [here](https://github.com/users/yannickferenczi/projects/15/views/1).

### 3.1. The workflow

The workflow of the project has been broken down into small organized pieces to help realize the amount of work and help spread it over the given period. It organizes a hierarchy as below:


<details>
    <summary>The full project (represented by the project manager)</summary>
    <p>The project manager has been a roadbook, leading the development of this project to its success, handling quite well the stress of such a challenge.</p>
</details>


<details>
    <summary>Milestones</summary>
    <p>4 Milestones were developed for this project, leading the web application to a more and more powerful tool.
    <ul>
    <li>The first Milestone was a guideline toward the minimum viable product. When that was achieved, the project could already be submitted.</li>
    <li>The second and the third Milestones were there to bring more features to the project and implement some automated testing to develop a more robust project.</li>
    <li>Finally, the fourth Milestone is there to help submit a project where attention has been given to details.</li>
    </ul>
    </p>
</details>

<details>
    <summary>EPICS</summary>
    <p>Milestones have been broken into Epics. They correspond to important achievements for the project such as "implementing an authentication system" or "implementing a task management system". They were there to help me concentrate on concrete things to work on while developing the project. It gave some clear direction to take, knowing that they serve the general purpose of the project.</p>
</details>

<details>
    <summary>User Stories</summary>
    <p>User stories were backlog product items that could be done in quite a short time. So they could be contained within a sprint and therefore allow every sprint to have its number of achievements. Some user stories together usually fulfill an EPIC.</p>
</details>

<details>
    <summary>tasks</summary>
    <p>Finally, tasks were defined within the user stories to remind the stakeholder what to develop. They were there to help define the user story, giving more precise things to work on.</p>
</details>

### 3.2. Labels

Labels have been created to quickly visualize the type of backlog product item and its priority. Below is a screenshot of the labels used for the project.

![Labels of the project](documentation/labels.png)

### 3.3. The views of the project manager

The project manager contains 4 views. The three first have been very useful during the development. The fourth one is more of a nice overview of the efforts spread over time.

- The first view: Home

    The first view, called home, has been used during the development phase with the filter `is:open`. It was the first and the last view to look at on a working day. It helped to know what needed to be done, and what needed to be prioritized and help organized the upcoming days.

- The second view: Current sprint

    The second view was just nice to have when tasks were done and the goal of the current sprint was getting closer and closer. It gave a nice feeling of achievement while pushing the backlog product items to the "Ready" column and then to the "Deployed" column when they were respectively done and deployed to the live website.

- The third view: Sprints

    The third view was similar to the second one. Only it gave an overview of the full project and not just of the current sprint. It helped keep the deadline in mind and avoided wasting time on some "nice to have but cool to work on" features so the focus would mostly be on the right tasks.

- The fourth view: Roadmap

    The fourth view is just an overview of the three weeks of work that led to this project. It did not really bring help to the development of the project.

### 3.4. The story points

Story points have been assigned to epics and user stories to be able to submit the project as much developed as possible and, of course, on time. It was clear that the final product would not be done in such a short time, especially because it was my first full stack project and I wanted to go down some unknown part of the Django framework (so far not explained within the code institute course). Nevertheless, I took the challenge to make the first version of this project which could already be used. Now because there were a lot of uncertain abilities to do what I planned to do, it made tricky the story point assignment.

My priority was as expected to develop a minimum viable product (MVP) that corresponds to the expected project from the assessment criteria of Code Institute. This milestone has 182 story points which are 45% of the total amount represented with 400 story points.

### 3.5. The sprints

The project has been developed in 11 Sprints of 2 days.
Each sprint counts a certain amount of story points based on their Epics, User Stories, and tasks. They are as below:

| Sprints | Total Story Points |
| --- | :---: |
| Sprint 1 | 14 |
| Sprint 2 | 24 |
| Sprint 3 | 36 |
| Sprint 4 | 56 |
| Sprint 5 | 44 |
| Sprint 6 | 32 |
| Sprint 7 | 68 |
| Sprint 8 | 14 |
| Sprint 9 | 32 |
| Sprint 10 | 80 |
| Sprint 11 | N/A |

To conclude, it was complicated to evaluate the number of story points depending on how difficult or how long a task would be. This is the reason why the number of points from one sprint to another one can be so different. Another reason is also that some backlog product items were already in development at the end of a sprint already fully accomplished and would count only for the following sprint. It still pretty much looks like the average could be between 30 and 40 points/sprint.

[Back to the Table of Content](#1-table-of-content)

---

<div align="center">

## 4. Features

</div>

This project is a full-stack web application using a cloud-based database (PostgreSQL) to record data.

### 4.1. Features currently available

- A branding with a logo, a name, and the colors of the company

![Hands Home Helpers branding big screens](documentation/hands_home_helpers_branding.png)
![Hands Home Helpers branding small screens](documentation/hands_home_helpers_branding_small.png)

- A navigation menu

![Navigation menu big screens](documentation/navigation_menu.png)
![Navigation menu small screens](documentation/navigation_menu_small.png)

- Greetings

![Greetings](documentation/greetings.png)

- A call to action (CTA) on a Hero-image

![Call to action](documentation/cta_on_hero-image.png)

- Carousels to present the company's activities

![Company's activities](documentation/caroussel_of_activities.png)

- A footer with links to social media and extra resources

![Footer](documentation/footer.png)

- A copyright

![Copyright](documentation/copyright.png)

- A personal dashboard

![Personal dashboard](documentation/personal_dashboard.png)

- A notification system

![Notification system](documentation/notification_system.png)

- A system for the admins to create and display their offers

![Company offers](documentation/offers.png)

- An authentication system

![Authentication system](documentation/authentication_system.png)

- A booking system

The booking system is the highlight of this project. I absolutely wanted to tackle this challenge as I think it is nice to have skills in a professional environment. To be confronted with the problems it can raise was a very interesting and satisfying learning journey.

![Booking system step 1](documentation/booking_system_step_1.png)

![Booking system step 2](documentation/booking_system_step_2.png)

### 4.2. More features to implement

The final goal of the Hands Home Helpers website is to give customers and employees a powerful tool to communicate in the easiest possible way.

Therefore, this web application should implement at least 2 different profiles: 1 customer profile and 1 employee profile, both inheriting from the User model.

To stick to the deadline, this concept could not be implemented to its apogee. So profiles were not within the scope of this project.

That said, I have listed below some features that should be implemented to have a completed and powerful project.

- A customer profile based on the User model, including:
    - the subscription of the customer
    - the remaining working hours for the month
    - the name of their dedicated employee

- An employee profile based on the User model, including:
    - the day they started to work
    - their total amount of working hours (weekly, monthly, yearly)

- Each profile could have access to different dashboards. The customer dashboard has already been partially implemented. The employee dashboard could contain the following:
    - A list of their appointments,
    - Each appointment could lead to a detailed view from which the employee could update info about the tasks that have been done.

- The authentication system could be improved:
    - a backend email could be implemented to allow users to reset their password.
    - a feature could be implemented so users could register with a third party.

- A blog system could be implemented to allow employees to share technical tips on how they do their job. That could help the SEO and carry more visitors to the website.

[Back to the Table of Content](#1-table-of-content)

---

<div align="center">

## 5. Technology Used

</div>

- Languages, Databases, and Frameworks:

  - HTML5
  - CSS3
  - Javascript
  - Bootstrap 5.3.0
  - Python 3.9.17
  - Django 3.2.20
  - PostgreSQL
  - psycopg2 2.9.6
  - django-allauth 0.54.0
  - gunicorn 21.2.0
  - cloudinary 1.33.0
  - coverage 7.3.0
  - Markdown

- Other tools:

  - [Git](https://git-scm.com/) has been used for version control
  - [GitHub](https://github.com/) has been used to store the project code
  - [Code Anywhere](https://codeanywhere.com/) has been used as cloud ide
  - [Google Fonts](https://fonts.google.com/) has been used for the fonts
  - [LucidCharts](https://lucid.app/) has been used to create the erd and the flowchart
  - [Balsamiq](https://balsamiq.com/) has been used to create the wireframes
  - [Font Awesome](https://fontawesome.com/) has been used for the icons
  - [Pexels](https://www.pexels.com/) has been used to find free pictures
  - [Tiny PNG](https://tinypng.com/) has been used to further optimize the images for the site and reduce the file size
  - [EmailJS](https://www.emailjs.com/) has been used to link the contact form to an email address
  - [ElephantSQL](https://customer.elephantsql.com/) has been used to store the database
  - [Heroku](https://www.heroku.com/) has been used to deploy the live website
  - [Google Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools) has been used to debug during the development process
  - Used to inspect page elements, debug issues with the site & test responsiveness on different mockup devices
  - [Markup Validation Service](https://validator.w3.org/) has been used to check the HTML code
  - [CSS Validation Service](https://jigsaw.w3.org/css-validator/) has been used to check the CSS code
  - [CI Python Linter](https://pep8ci.herokuapp.com/) has been used to check the Python code
  - [JSHint](https://jshint.com/) has been used to check the Javascript code
  - [Website Grader](https://website.grader.com/) has been used to create a report on the website performance
  - [PageSpeed Insights](https://pagespeed.web.dev/) has been used to check the speed of the website
  - [Wave](https://wave.webaim.org/) has been used to test the accessibility of the website
  - [Accessibility Checker](https://www.accessibilitychecker.org/) has been used to test the accessibility of the website
  - [Am I responsive](https://ui.dev/amiresponsive) has been used to create a mockup of responsiveness
  - [Shields.io](https://shields.io/) has been used to create badges within the README.md file

[Back to the Table of Content](#1-table-of-content)

---

<div align="center">

## 6. Testing

</div>

Testing details can be found separately in the [TESTING.md](TESTING.md) file

---

<div align="center">

## 7. Deployment

</div>

### 7.1. Project Creation

I have created the project from the [ci-full-template](https://github.com/Code-Institute-Org/ci-full-template) following the steps below:

1. From the link above, click on 'Use this template' and select 'Create a new repository'
2. Enter a name for the new repository
3. Click 'Create Repository'
4. From the new GitHub repository, click on the button '<> Code', then select local and copy the https link of the repository
5. Open Code Anywhere and navigate to the 'workspaces' page
6. Click on 'New Workspace'
7. Paste the GitHub repo URL into the 'Repository URL' box
8. Click 'Create'

### 7.2. Deployment to Heroku

I used Heroku to deploy this project.

To deploy to Heroku:

1. In Code Anywhere CLI from the main directory, to create/update a requirements.txt file containing project dependencies, run

   `pip3 freeze --local > requirements.txt`

2. In Code Anywhere CLI from the main directory, to create a Procfile, run

   `echo web: gunicorn config.wsgi > Procfile`

3. Push the 2 new files to the GitHub repository

4. log in to Heroku, select 'Create New App', create a unique name for the app, and select your nearest region. Click 'Create App'

5. Navigate to 'settings', click reveal config vars, and input the following:

| Key | Value |
| :---: | :---: |
| CLOUDINARY_URL | cloudinary_url |
| PORT | 8000 |
| DATABASE_URL | elephantSQL_url |
| SECRET_KEY | django_secret_key |

1. Navigate to the Deploy tab on the Heroku dashboard and select Github, search for your repository by name, and click 'connect'.
2. Click deploy branch
3. Once the build is complete click on 'Open app' to launch the new app

### 7.3. Local Development

> NB: To run this project locally, you will need to create an env.py file (within the root directory) configuring the above environment variables as these are not included in the GitHub files for security reasons.
> This file should look like this:

```Python
import os

os.environ["DATABASE_URL"] = "elephantSQL_url"
os.environ["SECRET_KEY"] = "django_secret_key"
os.environ["CLOUDINARY_URL"] = "cloudinary_url"
os.environ["DEVELOPMENT"] = "True"
```

To Run Locally:

1. Navigate to the [GitHub Repository](https://github.com/yannickferenczi/hands-home-helpers-website)
2. Click on the button '<> Code', then 'Local' and select 'Download Zip' to download the files locally and open them with an IDE

To Fork the project:

1. Navigate to the [GitHub Repository](https://github.com/yannickferenczi/hands-home-helpers-website)
2. Click on the 'Fork' button at the top right of the page and select 'Create a new fork'
3. This will duplicate the project for you to work on

[Back to the Table of Content](#1-table-of-content)

---

<div align="center">

## 8. Credits

</div>

- The [PP4_masterclass](https://github.com/Code-Institute-Solutions/PP4_masterclass) repository from Code Institute has been used as a reference to implement the minimum viable product.

- To display a message after deleting a task, some code needed to be added. The solution has been taken from [Stackoverflow](https://
- stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown)

- The [Code Institute course](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+BSR102+2021_T1/courseware/5961b57ece7d4ef18749778768a9376e/3b58b5a90e7048c8a4f2344f2401cf4a/) has been used as a guideline to link EmailJS to the contact form and the [sendEmail.js](static/js/sendEmail.js) file has been entirely copied from that course

- The Javascript code to dismiss the notifications has been taken from [Code Institute](https://codeinstitute.net/de/)

- The html calendar has been implemented using an external code found on [Stackoverflow](https://stackoverflow.com/questions/75945489/django-python-calendar-module). It has only been a little been modified to match the expectations of this project.

- The check_overlap function as well as the clean function have been entirely imported from [Alexandre Pinto's website](https://alexpnt.github.io/2017/07/15/django-calendar/). Those functions help validate appointments while being created.

- The star rating system has been implemented using some code from "How to" on [W3schools](https://www.w3schools.com/howto/howto_css_star_rating.asp). It means the HTML, as well as the CSS, have been taken from their website and inserted into my project.

- The slideshow to display reviews of the customers has been taken from [W3schools](https://www.w3schools.com/howto/howto_js_quotes_slideshow.asp). It includes some HTML, CSS, and JavaScript.

[Back to the Table of Content](#1-table-of-content)

---

<div align="center">

## 9. Acknowledgements

</div>

- A huge thanks to my wonderful wife for letting me spend so much time on this project (over 250 hours) even though we have a beautiful 4-month-old daughter who also needs some attention.

- A big thanks also to [Alan Bushell](https://github.com/Alan-Bushell) for all the resources and tips he shared with us during our weekly meetings and for his positive vibes and his support when things went hardcore.

- Thank you to [Code Institute](https://codeinstitute.net/de/) for providing such great content and helping me to implement such a full-stack project in 3 weeks' time after less than 6 months of learning.

- Thank you to [Docstring](https://www.docstring.fr/) and its amazing community for answering many questions as stupid as they possibly are, at any time (day and night).

- And finally thanks to my mentor [Akshat Garg](https://github.com/akshatnitd) who provided me with some resources to assist me in this project.
