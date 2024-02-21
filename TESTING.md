# Portfolio Project 4 - PIZZATHEACTION
## Full Stack Frameworks with Django Milestone Project
## Testing
---

### Introduction
---
Due to the scale of the project it would be evident that a robust set of testing would be required to ensure all aspects of the site were tested. To do this I created the User Stories to test each feature and function of the site. I have also conducted validation testing of each aspect of the projects code.

### Validation Testing
---

#### HTML Validation
Each section of the site was tested using the [W3C HTML Validator](https://validator.w3.org/#validate_by_uri) using the text area of the direct input. Here are the results:

|Feature|Expected Outcome|Test Performed|Result|Pass/Fail|
|---|---|---|---|---|
|Home|Pass with no errors|HTML passed through W3C HTML Validator|No Errors|Pass|
|Products|Pass with no errors|HTML passed through W3C HTML Validator|No Errors|Pass|
|View Product|Pass with no errors|HTML passed through W3C HTML Validator|No Errors|Pass|
|Add Product|Pass with no errors|HTML passed through W3C HTML Validator|Duplicate ID error - Resolved|Pass|
|Edit Product|Pass with no errors|HTML passed through W3C HTML Validator|Duplicate ID error - Resolved|Pass|
|View Brands|Pass with no errors|HTML passed through W3C HTML Validator|href error on Accordion - Resolved|Pass|
|View Categories|Pass with no errors|HTML passed through W3C HTML Validator|href error on Accordion - Resolved|Pass|
|Profile|Pass with no errors|HTML passed through W3C HTML Validator|No Errors|Pass|
|Blog|Pass with no errors|HTML passed through W3C HTML Validator|No Errors|Pass|
|Add Post|Pass with no errors|HTML passed through W3C HTML Validator|No Errors|Pass|
|Edit Post|Pass with no errors|HTML passed through W3C HTML Validator|No Errors|Pass|
|Delete Post|Pass with no errors|HTML passed through W3C HTML Validator|No Errors|Pass|
|Add Comment|Pass with no errors|HTML passed through W3C HTML Validator|No Errors|Pass|
|Basket|Pass with no errors|HTML passed through W3C HTML Validator|No Errors|Pass|
|Checkout|Pass with no errors|HTML passed through W3C HTML Validator|No Errors|Pass|
|Checkout Success|Pass with no errors|HTML passed through W3C HTML Validator|No Errors|Pass|
|Allauth Templates|Pass with no errors|HTML passed through W3C HTML Validator|No Errors|Pass|
|400|Pass with no errors|HTML passed through W3C HTML Validator|No Errors|Pass|
|403|Pass with no errors|HTML passed through W3C HTML Validator|No Errors|Pass|
|404|Pass with no errors|HTML passed through W3C HTML Validator|No Errors|Pass|
|500|Pass with no errors|HTML passed through W3C HTML Validator|No Errors|Pass|

#### HTML Issues Identified and resolved

- The Add Product and Edit Product both suffered from an issue with duplicate ID's appearing on the image selection. This was the same error experienced by Emma Hewson and her [Island Bees](https://github.com/emmahewson/island-bees) project. Follwoing her solution of changing the JavaScript to get an element using a class name rather than ID and removing the class resolved the issue. Thank you Emma!
- The View Brands and View Categories accordions supplied through bootstrap were causing an error that 'href' wasn't present on the 'a' tag. reviewing the code and comparing it to the code provided by [Bootstrap](https://getbootstrap.com/docs/5.3/components/accordion/) I had incorrectly changed the 'button' tag to an 'a' tag instead. Changin this back and adjustong the CSS to target the correct tag resolved this issue.

#### CSS Validation

There are 4 separate CSS files contained within the application that I run through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/):

|CSS File|Expected Outcome|Test Performed|Result|Pass/Fail|
|---|---|---|---|---|
|base.css|Pass with no errors|CSS passed through W3C CSS Validator|No Errors|Pass|
|blog.css|Pass with no errors|CSS passed through W3C CSS Validator|No Errors|Pass|
|checkout.css|Pass with no errors|CSS passed through W3C CSS Validator|No Errors|Pass|
|profiles.css|Pass with no errors|CSS passed through W3C CSS Validator|No Errors|Pass|

#### JavaScript Linting

The JavaScript in this project is split between small scripts at the bottom of most templates or in the case of the checkout in a standalone .js file. Apart from a few missing semi-colons there were no evident errors in the code.

|Feature|Expected Outcome|Test Performed|Result|Pass/Fail|
|---|---|---|---|---|
|Basket|Pass with no errors|JavaScript passed through JSHint|No Errors|Pass|
|Add Post|Pass with no errors|JavaScript passed through JSHint|No Errors|Pass|
|Blog|Pass with no errors|JavaScript passed through JSHint|No Errors|Pass|
|View Post|Pass with no errors|JavaScript passed through JSHint|No Errors|Pass|
|Checkout|Pass with no errors|JavaScript passed through JSHint|No Errors|Pass|
|Edit Product|Pass with no errors|JavaScript passed through JSHint|No Errors|Pass|
|All Products|Pass with no errors|JavaScript passed through JSHint|No Errors|Pass|

#### Python Linting

All Python code was passed through the [CI Python Linter](https://pep8ci.herokuapp.com/) with no major errors. There were a few lines that were ove 80 characters, but these were easily resolved.

|File Name|App|Expected Outcome|Test Performed|Result|Pass/Fail|
|---|---|---|---|---|---|
|apps.py|Basket|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|contexts.py|Basket|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|urls.py|Basket|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|views.py|Basket|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|admin.py|Blog|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|apps.py|Blog|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|forms.py|Blog|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|models.py|Blog|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|urls.py|Blog|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|views.py|Blog|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|admin.py|Checkout|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|apps.py|Checkout|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|forms.py|Checkout|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|models.py|Checkout|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|signals.py|Checkout|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|urls.py|Checkout|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|views.py|Checkout|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|webhook_handler.py|Checkout|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|webhooks.py|Checkout|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|apps.py|Home|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|urls.py|Home|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|views.py|Home|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|asgi.py|Pizzatheaction|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|settings.py|Pizzatheaction|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|urls.py|Pizzatheaction|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|wsgi.py|Pizzatheaction|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|admin.py|Products|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|apps.py|Products|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|forms.py|Products|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|models.py|Products|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|urls.py|Products|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|views.py|Products|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|widgets.py|Products|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|apps.py|Profiles|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|forms.py|Profiles|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|models.py|Profiles|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|urls.py|Profiles|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|
|views.py|Profiles|Pass with no errors|Python code passed through CI Python Linter|No Errors|Pass|

#### Performance Testing

Using the Google Chrome Dev Tools Lighthouse, I checked the performance score of each section of the site. Below is a table with details of the test and the results images. Due to time constraints I lowered my pass rate to 80 and above. With a bit more time I feel I could have brought each of these pages to over 90.

|Feature|Expected Outcome|Test Performed|Outcome/Changes|Pass/Fail|Image|
|---|---|---|---|---|---|
|Home|Score of 80+ with no major errors or issues|Chrome Lighthouse Report for page|90|Pass|![Home](media/documentation/testing/lighthouse/home.png)|
|Products|Score of 80+ with no major errors or issues|Chrome Lighthouse Report for page|87|Pass|![Products](media/documentation/testing/lighthouse/products.png)|
|View Product|Score of 80+ with no major errors or issues|Chrome Lighthouse Report for page|94|Pass|![View Product](media/documentation/testing/lighthouse/view_product.png)|
|Add Product|Score of 80+ with no major errors or issues|Chrome Lighthouse Report for page|89|Pass|![Add Product](media/documentation/testing/lighthouse/add_product.png)|
|Edit Product|Score of 80+ with no major errors or issues|Chrome Lighthouse Report for page|89|Pass|![Edit Product](media/documentation/testing/lighthouse/edit_product.png)|
|View Brands|Score of 80+ with no major errors or issues|Chrome Lighthouse Report for page|89|Pass|![View Brands](media/documentation/testing/lighthouse/view_brands.png)|
|View Categories|Score of 80+ with no major errors or issues|Chrome Lighthouse Report for page|89|Pass|![View Categories](media/documentation/testing/lighthouse/view_categories.png)|
|Profile|Score of 80+ with no major errors or issues|Chrome Lighthouse Report for page|87|Pass|![Profile](media/documentation/testing/lighthouse/profile.png)|
|Blog|Score of 80+ with no major errors or issues|Chrome Lighthouse Report for page|89|Pass|![Blog](media/documentation/testing/lighthouse/blog.png)|
|Add Post|Score of 80+ with no major errors or issues|Chrome Lighthouse Report for page|82|Pass|![Add Post](media/documentation/testing/lighthouse/add_post.png)|
|Edit Post|Score of 80+ with no major errors or issues|Chrome Lighthouse Report for page|81|Pass|![Edit Post](media/documentation/testing/lighthouse/edit_post.png)|
|Delete Post|Score of 80+ with no major errors or issues|Chrome Lighthouse Report for page|90|Pass|![Delete Post](media/documentation/testing/lighthouse/delete_post.png)|
|Add Comment|Score of 80+ with no major errors or issues|Chrome Lighthouse Report for page|82|Pass|![Add Comment](media/documentation/testing/lighthouse/add_comment.png)|
|Basket|Score of 80+ with no major errors or issues|Chrome Lighthouse Report for page|90|Pass|![Basket](media/documentation/testing/lighthouse/basket.png)|
|Checkout|Score of 80+ with no major errors or issues|Chrome Lighthouse Report for page|82|Pass|![Checkout](media/documentation/testing/lighthouse/checkout.png)|
|Checkout Success|Score of 80+ with no major errors or issues|Chrome Lighthouse Report for page|89|Pass|![Checkout Success](media/documentation/testing/lighthouse/checkout_success.png)|

### Device & Browser Testing

#### Responsive Device Testing


#### Browser Compatibility


### User Story Testing


### Bugs and Fixes
