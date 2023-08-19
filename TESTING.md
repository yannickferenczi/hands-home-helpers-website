<div align=center>

# Hands Home Helpers

***- TESTING DOCUMENTATION -***

</div>

## 1.1. Table of content

- [Hands Home Helpers](#hands-home-helpers)
  - [1.1. Table of content](#11-table-of-content)
  - [1.2. Code Validation](#12-code-validation)
    - [1.2.1. HTML](#121-html)
    - [1.2.2. CSS ](#122-css-)
    - [1.2.3. JavaScript](#123-javascript)
      - [1.2.3.1. The result for the script.js file shows three errors:](#1231-the-result-for-the-scriptjs-file-shows-three-errors)
    - [1.2.4. Python](#124-python)
  - [1.3. Lighthouse](#13-lighthouse)
    - [1.3.1. The home page](#131-the-home-page)
    - [1.3.2. The dashboard](#132-the-dashboard)
    - [1.3.3. The offers page](#133-the-offers-page)
    - [1.3.4. The about page](#134-the-about-page)
    - [1.3.5. The contact page](#135-the-contact-page)
    - [1.3.6. The calendar page](#136-the-calendar-page)
  - [1.4. Manual Testing](#14-manual-testing)
    - [1.4.1. User Stories Testing](#141-user-stories-testing)
    - [1.4.2. Features Testing](#142-features-testing)
  - [1.5. Automated testing](#15-automated-testing)
    - [1.5.1. Appointments app](#151-appointments-app)
    - [1.5.2. Config app](#152-config-app)
    - [1.5.3. Contact app](#153-contact-app)
    - [1.5.4. Offers app](#154-offers-app)
    - [1.5.5. Reviews app](#155-reviews-app)
    - [1.5.6. Tasks app](#156-tasks-app)
  - [1.6. Bugs](#16-bugs)


## 1.2. Code Validation

### 1.2.1. HTML

- w3c markup validator results for the landing page:

![w3c markup validator results for the landing page](documentation/w3c_markup_validator_results_landing-page.png)

- w3c markup validator results for the About page:

![w3c markup validator results for the about page](documentation/w3c_markup_validator_results_about-page.png)

- w3c markup validator results for the personal dashboard:

![w3c markup validator results for the personal dashboard](documentation/w3c_markup_validator_results_dashboard.png)

- w3c markup validator results for the contact page:

![w3c markup validator results for the contact page](documentation/w3c_markup_validator_results_contact-page.png)

- w3c markup validator results for the offers:

![w3c markup validator results for the offers](documentation/w3c_markup_validator_results_offers.png)

- w3c markup validator results for the calendar:

![w3c markup validator results for the calendar](documentation/w3c_markup_validator_results_calendar.png)

- w3c markup validator results for the daily calendar:

![w3c markup validator results for the dailycalendar](documentation/w3c_markup_validator_results_daily_calendar.png)

### 1.2.2. CSS <a href="http://jigsaw.w3.org/css-validator/check/referer"><img style="border:0;width:88px;height:31px" src="http://jigsaw.w3.org/css-validator/images/vcss" alt="Valid CSS!" /></a></p>

![w3c css validator results](documentation/w3c_css_validator_results.png)

### 1.2.3. JavaScript

There are two javascript files for this project. As the sendEmail function using EmailJS API does not work properly, I have decided to keep it in a different file so it does not disturb the execution of the rest of the JaviScript functionalities.

Both files were checked with JSHint.

#### 1.2.3.1. The result for the script.js file shows three errors:

- One undefined variable: bootstrap

    bootstrap has been integrated to the project using the minified bootstrap.js (in the base.html template). Therefore there is no need to explicitly import bootstrap in the script.js file.

- Two unused variables: plusSlides and currentSlides

    Those two functions are defined in the script.js file but called in the index.html template.

![jshint results of the script.js file](documentation/jshint_results_script.png)

The result for the script.js file shows three errors:

- One undefined variable: emailjs

    there is no need to define emailjs in the sendEmail.js file as the init method is defined in the base.html file.

- One unused variable: sendEmail

    This function is defined in the sendEmail.js file but called in the base.html template.

![jshint results of the sendEmail.js file](documentation/jshint_results_sendEmail.png)


### 1.2.4. Python

Every Python file has been ran through the [CI Python Linter](https://pep8ci.herokuapp.com/) and for all of them the result was:
> All clear, no errors found

## 1.3. Lighthouse

The main pages of the website have been tested with the Lighthouse validator from Google Chrome.

The results are shown below.

### 1.3.1. The home page

<details>
    <summary>Desktop</summary>
    <img src="documentation/lighthouse_home_desktop.png" alt="Lighthouse results of the home page on desktop">
</details>

<details>
    <summary>Mobile</summary>
    <img src="documentation/lighthouse_home_mobile.png" alt="Lighthouse results of the home page on mobile">
</details>

### 1.3.2. The dashboard

<details>
    <summary>Desktop</summary>
    <img src="documentation/lighthouse_dashboard_desktop.png" alt="Lighthouse results of the dashboard on desktop">
</details>

<details>
    <summary>Mobile</summary>
    <img src="documentation/lighthouse_dashboard_mobile.png" alt="Lighthouse results of the dashboard on mobile">
</details>

### 1.3.3. The offers page

<details>
    <summary>Desktop</summary>
    <img src="documentation/lighthouse_offers_desktop.png" alt="Lighthouse results of the offers page on desktop">
</details>

<details>
    <summary>Mobile</summary>
    <img src="documentation/lighthouse_offers_mobile.png" alt="Lighthouse results of the offers page on mobile">
</details>

### 1.3.4. The about page

<details>
    <summary>Desktop</summary>
    <img src="documentation/lighthouse_about_desktop.png" alt="Lighthouse results of the about page on desktop">
</details>

<details>
    <summary>Mobile</summary>
    <img src="documentation/lighthouse_about_mobile.png" alt="Lighthouse results of the about page on mobile">
</details>

### 1.3.5. The contact page

<details>
    <summary>Desktop</summary>
    <img src="documentation/lighthouse_contact_desktop.png" alt="Lighthouse results of the contact page on desktop">
</details>

<details>
    <summary>Mobile</summary>
    <img src="documentation/lighthouse_contact_mobile.png" alt="Lighthouse results of the contact page on mobile">
</details>

### 1.3.6. The calendar page

<details>
    <summary>Desktop</summary>
    <img src="documentation/lighthouse_calendar_desktop.png" alt="Lighthouse results of the calendar page on desktop">
</details>

<details>
    <summary>Mobile</summary>
    <img src="documentation/lighthouse_calendar_mobile.png" alt="Lighthouse results of the calendar page on mobile">
</details>

## 1.4. Manual Testing

### 1.4.1. User Stories Testing

<details>
<summary style="background-color: #005500;">User Story 9: As a Site User, I can register so that I can access restricted features.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| there is a link to the registration form | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the registration form is properly displayed | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Errors are displayed if the form is not valid | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the database is updated when a valid form is submitted | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| users are redirected to their personal account when registered successfully | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| a unique username is required | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| a password is required | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| a password confirmation is required | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| an email address is optional | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">User Story 10: As a Site User, I can log into my personal account so that I can access personal settings and data.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| there is a link to the login form | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the login form is properly displayed | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Errors are displayed if the form is not valid | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| users are redirected to their personal account when successfully logged in | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| a username is required | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| a password is required | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">User Story 11: As a Logged in Site User, I can log out so that my personal data are safe.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| there is a button to logout | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| users are asked to confirm to logout | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| users are redirected to the home page when successfully logged out | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| users cannot access their personal account anymore | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #bb0000;">User Story 12: As a Registered Site User, I can create a new task so that I can add it to my list of tasks.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| there is a button to create a task | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the form to create a task is properly displayed | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Errors are displayed if the form is not valid | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| There is a field for the name of the task | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| There is an option to repeat the task | <img src="https://img.shields.io/static/v1?label=&message=FAIL&color=bb0000&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=FAIL&color=bb0000&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=FAIL&color=bb0000&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=FAIL&color=bb0000&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=FAIL&color=bb0000&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=FAIL&color=bb0000&style=plastic" alt="test status"> |
| There is a multiple choice field to select the category | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| There is a button to validate the form | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| users are redirected to their personal account when the task has been successfully created | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the database is updated when a valid form is submitted | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">User Story 13: As a Registered Site User, I can access my tasks so that I can list them.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| tasks are listed on the personal account | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| when clicking on a details button, I am redirected to a task detail page | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| tasks are properly displayed | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #bb0000;">User Story 14: As a Registered Site User, I can modify my personal tasks so that I can update their information.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| there is a button to modify a task | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the form to modify a task is properly displayed | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Errors are displayed if the form is not valid | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| There is a field for the name of the task | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| There is an option to repeat the task | <img src="https://img.shields.io/static/v1?label=&message=FAIL&color=bb0000&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=FAIL&color=bb0000&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=FAIL&color=bb0000&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=FAIL&color=bb0000&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=FAIL&color=bb0000&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=FAIL&color=bb0000&style=plastic" alt="test status"> |
| There is a multiple choice field to select the category | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| All field are prepopulated with the information from the selected task | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| There is a button to validate the form | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| There is a button to cancel the modification and go back to the personal account | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| users are redirected to their personal account when the task has been successfully created | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the database is updated when a valid form is submitted | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">User Story 15: As a Registered Site User, I can delete my personal tasks so that I can get rid of them.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| there is a button to delete a task | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| users are asked to confirm when clicking the delete button | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| There is a button to confirm the deletion | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| There is a button to cancel the deletion and go back to the personal account | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| users are redirected to their personal account when the task has been successfully deleted | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the database is updated when a task has been successfully deleted | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">EPIC 4: As a Site User, I can get notified of my actions so that I know if they were successful or not.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| User gets notified when signing up | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| User gets notified when signing in | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| User gets notified when login out | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| User gets notified when creating a task | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| User is asked to confirm before deleting a task | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| User gets notified when deleting a task | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| User gets notified when modifying a task | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| User gets notified when creating an appointment | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| User is asked to confirm before deleting an appointment | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| User gets notified when deleting an appointment | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| User gets notified when modifying an appointment | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| User gets notified when creating a review | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| User is asked to confirm before deleting a review | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| User gets notified when deleting a review | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| User gets notified when modifying a review | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">User Story 33: As a Site User, I can land on a home page explaining the purpose of the website so that I know if it is answering my request.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| the landing page displays properly | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| every link is leading to the relevant page / section | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| there is a Call To Action | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page lists activities of the company | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page shows the logo and the name of the company | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page has a navigation menu | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page has a footer | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page shows a Hero-image | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">User Story 41: As a Site User, I can open an about page so that I can find more information about the company.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| the about page displays properly | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| every link is leading to the relevant page / section | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page has an about us section | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page has a Meet the Team section | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page has a FAQ section | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page shows the logo and the name of the company | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page has a navigation menu | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page has a footer | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">User Story 42: As a Site User, I am redirected to a custom 404-page when using the wrong URLs so that I know I am still on the website and I have a way to go back to a working page.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| the 404-error page displays properly | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| every link is leading to the relevant page / section | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page describes the error | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page has a way to go back to the main area of the website | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page shows the logo and the name of the company | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page has a navigation menu | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page has a footer | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">User Story 43: As a Site User, I am redirected to a custom 500-page when the server cannot handle my request so that I know what is the issue.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| the 500-error page displays properly | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| every link is leading to the relevant page / section | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page describes the error | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page has a way to the contact form | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page shows the logo and the name of the company | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page has a navigation menu | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page has a footer | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">User Story 56: As a Site Owner, I can redirect users to a custom 400-page when their request is suspicious so that the website is less exposed to security matters.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| the 400-error page displays properly | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| every link is leading to the relevant page / section | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page describes the error | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page has a way to go back to the main area of the website | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page shows the logo and the name of the company | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page has a navigation menu | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page has a footer | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #bb0000;">User Story 44: As a Site User, I can use a contact form so that I can contact the company in a way that I am sure will get my request.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| the contact page displays properly | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| every link is leading to the relevant page / section | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page displays a form to submit a request | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the form has a first_name field | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the form has a last_name field | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the form has a email_address field | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the form has a subject field | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the form has a message textarea field | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page shows the logo and the name of the company | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page has a navigation menu | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page has a footer | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the page displays error when submitting a non valid form | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| the request is saved in the database when successfully submitted | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| an email is sent to the company when the form is successfully submitted | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=FAIL&color=bb0000&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=FAIL&color=bb0000&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=FAIL&color=bb0000&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=FAIL&color=bb0000&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=FAIL&color=bb0000&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">EPIC 61: As a Site User, I can handle my appointments directly online so I am more flexible.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Users can create an appointment | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Users can delete their appointment | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Users can modify their appointment | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Users can read a detail of their appointment | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Users get notified when creating, modifying or deleting an appointment | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Users cannot overlap appointments | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Users cannot book less than 1 hour appointment | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">User Story 60: As a Site Administrator, I can manage offers of the company to customers so that I can adapt them to the market.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Admins can create new offers via django admin panel | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Admins can modify offers via django admin panel | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Admins can delete offers via django admin panel | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| offers are properly displayed on the website | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

### 1.4.2. Features Testing

<details>
<summary style="background-color: #005500;">A branding with a logo, a name, and the colors of the company.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| The logo is properly displayed | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Clicking on the logo lead back to the landing page | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| The branding appears on every page | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">A navigation menu.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| The navigation menu is properly displayed | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Each link leads to the relevant page / section | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Links to restricted pages only appear for authorized users | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">Greetings.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Personal greetings are displayed when logged in | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">A call to action (CTA) on a Hero-image.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| The Hero-image is properly displayed | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| The call to action is obvious | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| The call to action leads to the registration page | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">Caroussels to present the company's activities.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Carroussels are properly displayed | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Caroussels show the relevant images | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">A footer with links to social media and extra resources.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| The footer is properly displayed | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| The social media links open in a new tab and lead to the relevant platform | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| The extra resources lead to the relevant page / section | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">A copyright.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| The copyright is properly displayed | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| The copyright shows the current year | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| The link to GitHub open in a new tab and lead to the relevant page | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

---

<details>
<summary style="background-color: #005500;">A personal dashboard.</summary>

- Browser compatibility and responsiveness testing:

|  | chrome-desktop | chrome-mobile | safari-desktop | safari-mobile | firefox-desktop | firefox-mobile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| The content is properly displayed | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Each link leads to the relevant content | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Each button acts as expected | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
| Only content related to the user is displayed | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> | <img src="https://img.shields.io/static/v1?label=&message=PASS&color=success&style=plastic" alt="test status"> |
</details>

## 1.5. Automated testing

![Total coverage of the project](documentation/total_coverage.png)

Some automated tests have been implemented using unittest.

The coverage library has been used to get a visual report of automated testing.

### 1.5.1. Appointments app

![Appointments app coverage](documentation/appointments_coverage_highlighted.png)

### 1.5.2. Config app

![Config app coverage](documentation/config_coverage_highlighted.png)

### 1.5.3. Contact app

![Contact app coverage](documentation/contact_coverage_highlighted.png)

### 1.5.4. Offers app

![Appointments app coverage](documentation/offers_coverage_highlighted.png)

### 1.5.5. Reviews app

![Reviews app coverage](documentation/reviews_coverage_highlighted.png)

### 1.5.6. Tasks app

![Tasks app coverage](documentation/tasks_coverage_highlighted.png)


## 1.6. Bugs

- Deployment not working - ![bug status](https://img.shields.io/static/v1?label=fixed&message=Yes&color=success&style=plastic)

  The deployment did not work at first. I have created 3 setting files. One for development, one for production, and one common to both. Therefore, I needed to modify the manage.py and the wsgi.py files. However, I only had modified the manage.py file so the deployment work fine but the application was not working. I fixed this issue by modifying the wsgi.py file.

- Hero image was not displayed - ![bug status](https://img.shields.io/static/v1?label=fixed&message=Yes&color=success&style=plastic)
  
  On the deployed version, the Hero image on the landing page would not show up. It was a background image of a div element. So the file path to the image was used within the CSS file. I had the background-image property to the style attribute of the div within the HTML file using the static tag. This fixed the problem.

- Emailjs does not work - ![bug status](https://img.shields.io/static/v1?label=fixed&message=Yes&color=success&style=plastic)

  On the deployed version, the EmailJS API would not send emails. I realized that I called my file and my function with the same name. I changed it to give them different names and the problem was solved.

- EmailJS only works when using the Chrome browser - ![bug status](https://img.shields.io/static/v1?label=fixed&message=No&color=bb0000&style=plastic)

  For some reasons that could not be identified, EmailJS does not send emails when using Firefox or Safari browsers. As the issue has not been identified, the bug could not be resolved.

- Reviews stay online after modification - ![bug status](https://img.shields.io/static/v1?label=fixed&message=No&color=bb0000&style=plastic)

    By default, reviews are not directly online. They must be approved by an administrator to be published on the website. However, when a review is approved and then modified by the author of the given review, it stays online without the enhancements having been approved. This bug was not resolved because it was not a priority and time was missing.

- Tasks booked and unbooked keep their due date - ![bug status](https://img.shields.io/static/v1?label=fixed&message=No&color=bb0000&style=plastic)

    When a task is created, its due date value is None. Then when a task is assigned to an appointment, the date of the appointment becomes the due date of the task. However, if the task would be unassigned or the appointment is deleted, the task keeps its due date. This is not only problematic because it has a wrong due date, but also because the task would not be displayed in the options when creating a new appointment. So the task can never be assigned again. An easy and quick fix could be to change the on_delete argument in the model to delete the task when the appointment would be deleted. But it would only solve half of the problem. In fact, if the task would be unassigned, it would still keep its due date. Time is missing and this issue might remain unresolved.

- No way to access the full content of a review when longer than 50 characters - ![bug status](https://img.shields.io/static/v1?label=fixed&message=Yes&color=success&style=plastic)

  The first idea was to display only the beginning of reviews if they would be too long. But somehow, in the implementation, I lost focus and thought that there was no need for a review detailed view. The direct consequence is that there was no way to read the full reviews for the ones being truncated. A quick fix was to take off the truncate filter from the template.

- User should not be able to book an appointment on Sundays - ![bug status](https://img.shields.io/static/v1?label=fixed&message=Yes&color=success&style=plastic)

  The monthly calendar has been implemented with links for every single day to lead to a daily view of the selected day. With if statements, past days and Sundays would not offer that link anymore so users could not select those days to book an appointment.
  Nevertheless, from the daily calendar of a valid day, users could navigate with the next or previous button until a Sunday and create an appointment from there. This problem has been solved with an if statement within the Django template to add two days to the selected day instead of one if the selected day is a Saturday when clicking the next button and the same logic inverse to Mondays when clicking the previous button.

- User should not be able to book an appointment on past days - ![bug status](https://img.shields.io/static/v1?label=fixed&message=Yes&color=success&style=plastic)

    While I was writing the previous bug, I realized that there was a similar issue in the past days. This issue has been fixed by adding a variable called upcoming day to the booking view in the appointments app and an if statement in the template to only display the link to the previous day if that day is still in the future.

- Success notifications not displayed on deletion - ![bug status](https://img.shields.io/static/v1?label=fixed&message=Yes&color=success&style=plastic)

  With the Django mixins, it was quite simple to display a notification to users when they create, update, login, log out, or register. But it was not the case for the class-based delete view. I had to override the delete method of that view so that the notification would be displayed.

Return to the [README.md](README.md) file
