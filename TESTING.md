# HBCS BARBER's - Testing Documentation

![HBCS BARBER's](static/images/f-homepage.png)

Link to live site - [HBCS BARBER's](https://hbcs-a03727698283.herokuapp.com/)

---

Testing was ongoing throughout the entire build. We utilised Chrome developer tools whilst building to pinpoint and troubleshoot any issues as we went along.

The page has been inspected using google chrome developer tools & Firefox inspector tool to ensure that the page is fully responsive on a variety of different screen sizes and devices. I have also physically tested the responsiveness of the site on a number of different devices.

---

## CONTENTS

* [AUTOMATED TESTING](#AUTOMATED-TESTING)
  * [W3C Validator](#W3C-Validator)
  * [Python pep8 validation](#python-testing)

* [MANUAL TESTING](#MANUAL-TESTING)
  * [Full Testing](#Full-Testing)

---

## AUTOMATED TESTING


### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. It was also used to validate the CSS.

* [Index Page W3C HTML Validation](https://validator.w3.org/nu/#textarea) - Pass

* [style.css CSS Validation](https://jigsaw.w3.org/css-validator/validator) - Pass

* [script.js JS Validation](https://jshint.com/) - Pass


## Python Testing

Python pep8 validation was done via [Code Institute's Python Linter](https://pep8ci.herokuapp.com/)

The only errors recieved here were where some lines of text exceeded the limit of characters a couple of times, but these have now been rectified.

Python Files Tested:

- models
- forms
- views
- urls

___

## ADMIN

| TEST | Expected Outcome | PASS/FAIL|
| --- | --- | --- |
| Create a review | Review successfully created and displayed | Pass |
| Edit a review | The review editing was successfull and displayed | Pass |
| Toggle cancel | When the edit button is toggeled and cancel button clicked successfully toggeles back | Pass |
| Delete a review | The review was deleted and successfull removed | Pass |
| Create 7 Test reviews to check latest_reviews view because set the default to show only 6 reviews | Successfully shown 6 reviews  | Pass |
| Create a booking | Booking successfully created and displayed in profile page | Pass |
| Cancel a booking | Booking successfully canceled and successfully removed from profile page and database | Pass |

--- 

## User

| TEST | Expected Outcome | PASS/FAIL|
| --- | --- | --- |
| Create Account | Created successfully | Pass |
| Login | Login Successful | Pass |
| Logout | Logout Successful | Pass |
| Create a review | Review successfully created and displayed | Pass |
| Edit a review | The review editing was successfull and displayed | Pass |
| Delete a review | The review was deleted and successfull removed | Pass |
| Create a booking | Booking successfully created and displayed in profile page | Pass |
| Cancel a booking | Booking successfully canceled and successfully removed from profile page and database | Pass |
| Sweetalert 2 | When a message is displayed it is displayed by using Sweetalert 2 | Pass |

Back to [README.md](README.md)