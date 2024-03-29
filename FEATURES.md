# Portfolio Project 4 - PIZZATHEACTION
## Full Stack Frameworks with Django Milestone Project
## Features
---

### Home Page
The home page is made up of the base template, which is visible on all pages, and a dynamic home template that hides the images on smaller devices. The blog section is only available to users that are registered and logged in. Once logged in there is a button similar to the 'Start Shopping'. Examples of both are below.

![Home page logged out image](media/documentation/features/home_page_logged_out.png)
![Home page logged in image](media/documentation/features/home_page_logged_in.png)

### Nav bar
The Navigation bar displays the links to the user and the search function. On smaller devices it is a collapsable Navbar courtsey of Bootstrap. On larger devices each item appears in a single line to the user, with sub-menus available on click. The Blog function is not visible to users that are not registered and logged in.

![Nav Bar Logged Out image](media/documentation/features/nav_bar_logged_out.png)
![Nav Bar Logged In image](media/documentation/features/nav_bar_logged_in.png)

### Footer
The footer is fixed to the bottom of each page and advises user that the site is for educational purposes only.

![Footer image](media/documentation/features/footer.png)

### Sign Up Page
The Sign Up page is an allauth template and responsive depending on screen size. The email is required to be input twice to ensure accuracy. There is a link to guide you to the sign in page if you have already registered.

![Sign Up page image](media/documentation/features/sign_up_page.png)

### Sign In Page
Similar to the register page, the sign in page is also an allauth template and responsive depending on screen size. There are links to the sign up and forgor password page.

![Sign In page image](media/documentation/features/sign_in_page.png)

### Password Reset Page
The password reset page provides the user the opportunity to reset their password if they have forgotten it. This is another allauth template.

![Password Reset page image](media/documentation/features/password_reset_page.png)

### Sign Out Page
The sign out page is another all auth template which provides the user the opportunity to sign out or to stay signed in, returning them to the home page.

![Sign Out page image](media/documentation/features/sign_out_page.png)

### Profile Page
The profile page is where the users order history is retained with a link to each order to review previous orders in detail. There is also the default delivery information which can be updated inside of the profile page, including first and last name.

![Profile page image](media/documentation/features/profile_page.png)

### All Products Page
The All Products Page displays a list off all products availble to registered and un-registered users. The page is responsive depending on screen size limiting the items to a single column on small displays up to 4 columns on larger displays.

In the products drop down menu is the ability to filter all products by price and rating. This filters the items by either price (low to high) or Rating (high to low). A filter dropdown is available in the top right of the screen with reverser functions to those above and more.

![All Products page image](media/documentation/features/all_products_page.png)

### Products by Brand Page
The Products by Brand page provide an accordion for each product in the database. This is dynamically generated so if a product is added or removed a it will be reflected here. Upon selecting a brand a summary of that brand is provided with a link to the all products page where it is filtered to the slected brand.

![Products by Brand page image](media/documentation/features/products_by_brand.png)

### Products by Category Page
Similar to the Products by Brand page, the Products by Category page takes each category and dynamically generates an accordion item for each. A new categroy added or removed will adjust the numbers generated.

![Products by Category page image](media/documentation/features/products_by_category.png)

### View Single Product Page
The view single product page displays all of the details of a single product. Another responsive display depending on screen size, here we have the product image, name, brand, category, description and associate fields and the ability to add a quantity to the basket or return to the product page. The brand name and category are links to the all products page filtering all items by either brand name or category.

![View Single Product page image](media/documentation/features/single_product_page.png)

### Edit Product Page
The edit product page allows a super user to edit all aspects of the selected product. However, if the user does not have the correct privileges they are advised so and redirected to the sign in page. If they sign in with a user without the correct privileges they are redirected home and a message displayed advising them so.

![Edit Product page with permissions image](media/documentation/features/edit_product_permission.png)
![Edit Product page without permissions image](media/documentation/features/edit_product_no_permission.png)

### View Basket Page
The view basket page has two views, one with items and one without. If items are present information about the product including the image, name, SKU and price are displayed. Along side this are the quantity and subtotal with the options to adjust the quantity or remove the item all together. It also provides a basket total, Delivery amount and then the Grand Total. A message is displyed to advise the user that they could get free delivery by spending an extra amount, which is generated dynamically.

If no items are present the user is advised and a button back to the shop is provided.

![View Basket page with items image](media/documentation/features/basket_with_items.png)
![View Basket page without items image](media/documentation/features/empty_basket.png)

### Checkout Page
THe checkout page provides the user the ability to add delivery information to their profile if they are registered and logged in. Below this is the Stripe Payment field that allows them to enter their card details and to proceed with completing the order. There is also an Order Summary with a count of how many items the customer has, the subtotal based on quantity and unit price, and order total, delivery charge if any and grand total.

If a user tries to access the checkout without any items, they are redirected to the all products page and advised they have no items to checkout with.

![Checkout page image](media/documentation/features/checkout.png)

### Checkout Success
Once the order is completed the user is presented with the checkout success screen. It provides their unique order number, date, details of the products ordered, delivery details and the billing information.

THe user is notified in the body of the message and via a success notification to confirm that an email has been sent to confirm the order.

![Checkout Success page image](media/documentation/features/checkout_success.png)

### Blog/Community Page
The Blog/Community page provides an overview of all posts available to registered users. Each entry provides the title, author, category, created on and depending on if the post has been updated, the date and time it was updated. It also advises how many comments each post has had and the number of likes it has recieved. If you are the user that created the post or a super user, you have the ability to edit the post or delete the post and these appear to the right of the comments and likes. There is an add post button located at the top right of the page so a new thread can be started.

Should a user who is not registered attempt to access the blog they are advised they must be registered and logged in to proceed, with a redirection button to the home page.

![Blog/Community page with permissions image](media/documentation/features/blog_page.png)
![Blog/Community page without permissions image](media/documentation/features/blog_page_no_permission.png)

### View Post Page
The view post page allows the user to view a single post and it's associated comments. Registered users can like or unlike the post and add comments. Comments from the posts original author are offset to the right where as all other comments are set to the left to give some visual seperation.

Again, should a user who is not registered attempt to access an indiviudal post they are advised they must be registered and logged in to proceed, with a redirection button to the home page.

![View Post page with permissions image](media/documentation/features/view_post_permission.png)
![View Post page without permissions image](media/documentation/features/view_post_no_permission.png)

### Add Post Page
The Add Post page provides registered users the opportunity to create a new post. They add a title, a category and then the content of their message. Submission is done via the post button at the bottom and there is also a cancel button should they not wish to proceed.

Again, should a user who is not registered attempt to access the add post page they are advised they must be registered and logged in to proceed, with a redirection button to the home page.

![Add Post page with permissions image](media/documentation/features/add_post_permission.png)
![Add Post page without permissions image](media/documentation/features/add_post_no_permission.png)

### Edit Post Page
The Edit Post page provides the original posts author or a user with super user access the ability to edit a post post. Similar to the add post, they can edit the title, category and the content of their message. Submission is done via the update button at the bottom and there is also a cancel button should they not wish to proceed.

Again, should a user who is not registered attempt to access the edit post page they are advised they must be registered and logged in to proceed, with a redirection button to the home page.

![Edit Post page with permissions image](media/documentation/features/edit_post_permission.png)
![Edit Post page without permissions image](media/documentation/features/edit_post_no_permission.png)

### Delete Post Page
The delete post page allows the original posts author or a user with super user access the ability to delete a post. The user is advised that this cannot be undone once completed, with the option to complete the deletion or cancel.

Again, should a user who is not registered attempt to access the delete post page they are advised they do not have permission to access this page, with a redirection button to the home page.

![Delete Post page with permissions image](media/documentation/features/delete_post_permission.png)
![Delete Post page without permissions image](media/documentation/features/delete_post_no_permission.png)

### Add Comment Page
Registered users have the ability to leave comments on posts. Under each individual post is an Add Comment button which directs the user to the Add Comment page. Here a text box is provided for the user to input their response to the original post. It has an add button and a cancel button should the choose not to proceed with the comment.

Again, should a user who is not registered attempt to access the add comment page they are advised they do not have permission to access this page, with a redirection button to the home page.

![Add Comment page with permissions image](media/documentation/features/add_comment_permission.png)
![Add Comment page without permissions image](media/documentation/features/add_comment_no_permission.png)


Back to [README.md](README.md)