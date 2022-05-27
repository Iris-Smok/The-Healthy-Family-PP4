
<h1 align="center">The Healthy Family</h1>

                Image

This is a full-stack framework project built using Django, Python, HTML, CSS and JavaScript. My goal is to create a functioning and responsive website, that allows users to post, comment and like or unlike recipes. This project has been built for educational purposes.

# About
The Healthy Family is a website where users can comment, like and view recipes and also share their own recipes with other users.
This page is intended for all parents and others who are looking for inspiration in preparing meals for their children. 

# Table of Contents 
1. [UX](#ux)
    - [User Stories](#user-stories)

2. [Scope](#scope)
    - [Features](#features)
    - [Future Features](#future-features)

3. [Structure](#structure)

4. [Wireframes](#wireframes)

5. [Database schema](#database-schema)

6. [Surface](#surface)

7. [Technologies Used](#technologies-used)

8. [Testing](#testing)

9. [Validating](#validating)

10. [Final Product](#final-product)

11. [Deployment](#deployment)

12. [Credits](#credits)

#
# UX
Using the core UX principles I first started with Strategy, thinking about the target audience & the features they would benefit from.

The target audience for 'The Healthy Family' are:

- all age groups but mostly females, mothers
- everyone who is looking for inspiration in preparing healthy meals for their children
- people who like to share their kitchen creations with others
- people who are not experts in cooking


These users will be looking for:
- An informative website, with information that is easy-to-find & concise
- A website that offers healthy and easy prepared meals
- Ability to make a user account in order to interact with the site content
- Ability to save liked recipes for later use
- Ability to post, comment and like recipes

This website will offer all of these things whilst also allowing for intuitive navigation and conformability of use.

## User Stories 

**Epic: Admin**
- As a site Admin I can create, edit and delete recipes and comments so that I can manage the site content
- As a site Admin I can access the admin panel so that I can manage recipes and comments
- As a site Admin I can log out of the admin panel so that I can disconnect from the website

**Epic: User Interaction**
- As a logged-in User I can write comments on recipes so that I can leave my feedback
- As a logged-in User I can like and unlike recipes so that I can mark which recipes I like
- As a User I can view the number of likes on recipes so that I can see which recipes are the most popular
- As a User I can view comments on recipes so that I can read other users opinions

**Epic: User Recipes**
- As a logged-in User I can post a recipes so that other users can see them
- As a User I can delete my recipes so that I can remove any unwanted recipes that I have made
- As a User I can edit recipes so that I can update any changes or mistakes to my recipes
- As a logged-in User I can upload an image along with my recipe so that other users can see what the dish looks like

**Epic: Login/Register**
- As a User I can register for an account so that I can interact with the site content
- As a User I can log in/out off my account if I wish so that I can connect or disconnect from the website
- As a User I can easily see if I'm logged-in or logged-out so that I can be sure what my status is

**Epic: Navigation**
- As a User I can easily navigate through the site so that I can view desired content
- As a User I can search the desirable recipe by keyword so that I can find the recipe I want faster
- As a User I can see the most loved recipes so that I can quickly find inspiration and see which recipes are most famous
- As a User I can see the most recent recipes so that I can keep up to date with the latest recipes


#
# Scope 

## **Features**

### **Home Page**
*Navigation bar:* 
- The navigation bar appears on every page so users can easily navigate through the site
- Navigation bar has links for 'Home', 'Recipes' and 'Contact us' more links will be shown to logged in users
- If the user is logged in then the left side of the menu shows links for pages that only authorized users can visit and use, they are: 'Favorite Recipes', 'Your Recipes' and  'Logout'. Otherwise, the user will be given the option to 'Register' or 'Login'
- The user name will also appear on the bar, indicating which user is logged in
- A search bar is nested in the navbar to find recipes quickly
- The navbar is fully responsive, collapsing into a hamburger menu for medium and small screen size

*Hero Image:*
- The hero image welcomes the user with a short message advertising what the website is about
- The Login / Register button will take users to the login page, if users do not have an account there is a link to the registration page

*Recently added recipes:*
- Recently Added section shows the latest published recipes so users can quickly see recently published recipes
- The Recently Added section is fully responsive, showing 4 recipe cards
- Each recipe takes the user to the recipe details page
- Users can also see title, image, author, date posted, short description and number of likes

*Most Loved Recipes:*
- The Most Loved Recipes section displays the top 5 recipes with the most likes
- Each recipe takes the user to the recipe details page
- At the bottom of the list there is a link to the Recipes page that takes users to the page with all the recipes

*Contact Us:*
- The Contact Us section allows users to contact the administrator if they have any suggestions or questions

*Footer:*
- Appears on every page snd contains social links
- Links are opened in a new tab to avoid dragging users from our site

### **Recipes Page**
- The Recipes page shows all the published recipes, recipes are shown in order from newest to oldest
- The site will paginate all recipe cards to display 6 to a page
- Each recipe card will display an image, authors name, date posted, short description and number of likes
- Each recipe card takes users to the recipe details page 

### **Login/Register**
- The Login / Register button takes users to the login page where they can also find a link to the Register page where they can create an account

### **Favorite Recipes Page**
- Only logged in users can see Favorite Recipes Page
- The Favorite Recipes page shows all the recipes that the user liked

### **Your Recipes Page**
- The Your Recipes page displays all the recipes that user has created
- At the top there is an Add Recipe button which takes user to the add recipe page
- Each recipe has two buttons, Edit and Delete
- Edit button takes user to the edit page
- Clicking the Delete button will display the message asking the users if they are sure they want to delete that particular recipe

### **Recipes Details Page**
- The Recipes Details Page displays all the information about the selected recipes
- At the top of the page, the recipe card will display Recipes name, author name, date posted and image
- The main body of the page contains short description of the recipe, ingredients and preparation steps
- Number of likes and comments are displayed after the preparation steps
- Commenting section is located at the end of the page, only logged in users can leave a comment

### **Add Recipe Page**
- On the Add Recipe page users can add their recipes to the website
- The user must fill in all the fields in order for the recipe to be published
- If the user doesn't fill in one of the fields the error message appears
- If the user doesn't provide their image, the default image is displayed
- The Add Recipe button is located at the end of the page


### Future Features
- Categories
- Users settings
- Preparation time
- Notification for likes and comments
- Search bar 


#
# Structure
 
Since our target audience is mostly moms, but also everyone else who is looking for inspiration in preparing meals for children the structure idea
for The Healthy Family was to keep it simple. Simplicity helps users to quickly and easily access the app and navigate within the app.

The website is made from one app:
- recipes


# Wireframes
All wireframes were created used [Balsamiq](https://balsamiq.com/)

Wireframes for each device are linked here:
- [Desktop](assets/documents/wireframes-desktop.pdf)
- [Tablet](assets/documents/wireframes-tablet.pdf)
- [Mobile](assets/documents/wireframes-mobile.pdf)


# Database schema

<p align="center">
<img src="assets/documents/database-schema.png" width="900" height="100%">
</p>

# Surface

## Design 

## Chosen Color 

 

## Font 



## Media



# Technologies Used

## Languages 


## Frameworks, Libraries & Programs Used


# Testing


# Validating 


## User Story Testing

### **Testing Users Stories form (UX) Section**



### **HTML Validator** 




### **CSS Validator** 


# Final Product 


# Deployment



# Credits

## Content


## Media


## Acknowledgements





