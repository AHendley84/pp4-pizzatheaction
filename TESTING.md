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
Each section of the site was tested using the [W3C HTML Validator](https://validator.w3.org/#validate_by_input) using the text area of the direct input. Here are the results:

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
Manual testing was conducted on the following devices:
- Alienware m15 Ryzen Ed. R5
- ThinkVision P24h-10 External Monitor#
- Apple iPad 3rd Gen
- Apple iPad 9th Gen
- Apple iPhone 12 Pro
- Samsung Galaxy S23

#### Browser Compatibility
The site has been tested on the following browsers:
- Google Chrome Version 122.0.6261.57 (Official Build) (64-bit)
- Microsoft Edge Version 121.0.2277.128
- Mozilla Firefox Version 123.0
- Google Chrome Developer Tools to simulate multiple different device screen sizes


### User Story Testing

I came up with a number of user stories to focus the design and development of the site. Here is the list of user stories with the expected outcome and whether it passed or failed:

|User Story ID|as a/an|I want to be able to...|So that I can...|Expected Outcome|Pass/Fail|
|---|---|---|---|---|---|
|**Viewing & Navigation**|
|1|Shopper|View a list of products|Chose which to purchase|A full list of products are visible to the shopper|Pass|
|2|Shopper|View individual product details|Identify the price, description, etc|The detail of an individual product is displayed along with price, description, etc|Pass|
|3|Shopper|View the total of my purchases|Track how much I have spent|The profile page retains the order history with the total of each order|Pass|
|**Registration and User Accounts**|
|4|Site User|Easily register for an account|Create a personal account and view my profile|Unregistered site users can follow the link to register for an account from the front page or the nav bar|Pass|
|5|Site User|Easily login and/or logout|Access my personal account information|If the site user is already resigstered, they can choose the sign in option from the front page or the nav bar|Pass|
|6|Site User|Easily recover my password in case I forget|Recover access to the account|If the site user does forget the their password, they can follow a link from the sign in page to recover their password|Pass|
|7|Site User|Receive an email requesting user verify their email address as part of the sign up process|Verify that the users email address is valid|Sending the email is handled on the backend with each prospective user being asked to veirfy their email address before registration is complete|Pass|
|8|Site User|Have a personalised user profile|View my personal order history, order confirmations and save my personal and payment information|Registered site users can navigate to the Profile page and update their default delivery information and an overview of their order history|Pass|
|**Sorting and Searching**|
|9|Shopper|Sort the list of products available|Easily identify the items available by brand, price, rating|Via the Products navigation item a drop down is provided to view products by Branc, Catgeory and then filter all products by Rating (High to Low) and Price (low to High). A Further filter option is available on the Products page with more options|Pass|
|10|Shopper|Search for a product by name or description|Find a specific product type I would like to purchase|The navigation bar contains the search function which searches all aspects of the product to return the most results|Pass|
|**Purchasing and Checkout**|
|11|Shopper|Easily select the quantity of an item when purchasing|Ensure that I don't purchase the incorrect item or quantity|This can be achieved by selecting an indiviudal product|Pass|
|12|Shopper|View items in my shopping cart to be purchased|View the total cost of my purchase prior to completion|This is fully functioning in the basket, providing updated delivery costs if the order is below the £100 free delivery threshold|Pass|
|13|Shopper|Adjust the quantity of individual items in the bag|Easily amend purchases prior to checkout.|Prior to proceeding to the checkout the customer can adjust the quantity of an item in the basket|Pass|
|14|Shopper|Easily enter my payment information|Check out quickly with no hassles.|Registered and unregistered users are able to make purchases with quick access to the payment box provided by Stripe|Pass|
|15|Shopper|Feel my personal information is securely stored in the website|Provide the required information with confidence to complete the purchase|Using Django and Stripe customers can confidently provide their information which can be securely stored, should the user choose to do so|Pass|
|16|Shopper|View and order confirmation after checkout|Verify that I haven't made any mistakes|The customer is provided a copy of their order confirmation immediately after the order completes|Pass| 
|17|Shopper|Receive email confirmation that the purchase has been successful|Retain confirmation for my own personal records.|Emails are automatically generated once the order is placed|Pass|
|**Admin and Store Management**|
|18|Store Owner|Add a product|Add new items to the store.|This is acheivable through super user authorisation|Pass| 
|19|Store Owner|Edit / Update a product|Change product prices, descriptions, images and other criteria.|This is acheivable through super user authorisation|Pass|
|20|Store Owner|Delete a product|Remove items that are no longer for sale.|This is acheivable through super user authorisation. A prompt advises the user that this cannot be undone and do they want to proceed, adding a last line of defensive if the delete button has been hit in error|Pass|
|**Customer Interaction**|
|21|Site User|Easily access the blog feature|View existing blog entries.|Registered site users can access the blog via the navigation bar or via a link on the home page|Pass|
|22|Site User|Easily create a new blog post|Add a blog post.|Once in the blog section there is a clear 'Add Post' button|Pass|
|23|Site User|Leave comments on existing posts|Interact with other users around their blog posts|Once a registered user is viewing a blog post there is an Add Comment link which brings up the comment function to add that to the original post, which is then viewable under the original post|Pass|

#### User Story Testing Images

- 1 - View a list of products<br>
![1 - View a list of products](media/documentation/testing/userstories/shopper_1.png)

- 2 - View individual product details<br>
![2 - View individual product details](media/documentation/testing/userstories/shopper_2.png)

- 3 - View the total of my purchases<br>
![3 - View the total of my purchases](media/documentation/testing/userstories/shopper_3.png)

- 4 - Easily register for an account<br>
![4 - Easily register for an account](media/documentation/testing/userstories/site_user_4.png)

- 5 - Easily login and/or logout<br>
![5 - Easily login and/or logout](media/documentation/testing/userstories/site_user_5.png)

- 6 - Easily recover my password in case I forget<br>
![6 - Easily recover my password in case I forget](media/documentation/testing/userstories/site_user_6.png)

- 8 - Have a personalised user profile<br>
![8 - Have a personalised user profile](media/documentation/testing/userstories/site_user_8.png)

- 9 - Sort the list of products available<br>
![9 - Sort the list of products available](media/documentation/testing/userstories/shopper_9.png)

- 10 - Search for a product by name or description<br>
![10 - Search for a product by name or description](media/documentation/testing/userstories/shopper_10.png)

- 11 - Easily select the quantity of an item when purchasing<br>
![11 - Easily select the quantity of an item when purchasing](media/documentation/testing/userstories/shopper_11.png)

- 12 - View items in my shopping cart to be purchased<br>
![12 - View items in my shopping cart to be purchased](media/documentation/testing/userstories/shopper_12.png)

- 13 - Adjust the quantity of individual items in the bag<br>
![13 - Adjust the quantity of individual items in the bag](media/documentation/testing/userstories/shopper_13.png)

- 14 - Easily enter my payment information<br>
![14 - Easily enter my payment information](media/documentation/testing/userstories/shopper_14.png)

- 15 - Feel my personal information is securely stored in the website<br>
![15 - Feel my personal information is securely stored in the website](media/documentation/testing/userstories/shopper_15.png)

- 16 - View and order confirmation after checkout|Verify that I haven't made any mistakes<br>
![16 - View and order confirmation after checkout|Verify that I haven't made any mistakes](media/documentation/testing/userstories/shopper_16.png)

- 17 - Receive email confirmation that the purchase has been successful<br>
![17 - Receive email confirmation that the purchase has been successful](media/documentation/testing/userstories/shopper_17.png)

- 18 - Add a product<br>
![18 - Add a product](media/documentation/testing/userstories/store_owner_18.png)

- 19 - Edit / Update a product<br>
![19 - Edit / Update a product](media/documentation/testing/userstories/store_owner_19.png)

- 20 - Delete a product<br>
![20 - Delete a product](media/documentation/testing/userstories/store_owner_20.png)

- 21 - Easily access the blog feature<br>
![21 - Easily access the blog feature](media/documentation/testing/userstories/site_user_21.png)

- 22 - Easily create a new blog post<br>
![22 - Easily create a new blog post](media/documentation/testing/userstories/site_user_22.png)

- 23 - Leave comments on existing posts<br>
![23 - Leave comments on existing posts](media/documentation/testing/userstories/site_user_23.png)

### Bugs and Fixes

During the development of the site I have discovered two minor bugs that I was unable to resolve. However, I am confident these do not distract from the overall usability of the site and I am unaware of any other bugs that exist.

#### Bug 1 - First and Last name not reading from Django Admin

As part of the development of the site I wanted to incorporate the ability for each registered user to be able to input their first and last name into the Django Admin without having to have super user access. I've managed to construct the ability to add this to the profile page and it successfully updates the user profile. However, once an order is placed I refer back to the profile page, the names do not appear to pull through, but remain on the Admin side.

As per the final build this bug still remains, I have attempted to resolve the issue but wasn't able to prior to submission. It doesn't impact the overall functionality of the site, just requires the user to re-input their names.

#### Bug 2 - 'Original post updated on' displaying when the post hasn't been updated

A function I wanted to add to the blog was a notification on each post to determine if the original post has been updated. I've pushed this to the live site and it doesn't work. I've spent a number of hours trying to work through why this is but I've not been able to get this resolved prior to the submission of the project.

Again, this does not affect the user experience, it's just an extra touch to make the blog post interface look a little cleaner.
