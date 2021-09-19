# Give Me A Sign

## Hack the North 2021 Project

A touch-free surveying website using computer vision to quickly gather customer feedback. Customers can give a thumbs up, down, or show numbers, to give feedback that is then stored for later analysis

## Inspiration
If you've ever been asked to take a feedback survey while at a restaurant, a hospital, a show, etc, then you know how annoying and time-consuming it can be. Also, If you've ever been given the task of collecting customer feedback via survey, you also know how challenging it can be to convince people to fill out a feedback survey because no one wants to fill those out. We thought of 'GiveMeASign' as a solution to make it extremely fast and convenient for people to give their feedback to a company or service. 'GiveMeASign' would also help business owners collect more feedback because the quickness and simplicity of the feedback collection process makes customers more inclined to give feedback in the first place.

## What it does
'GiveMeASign' allows customers to rapidly fill out a feedback survey in a completely touch-free way, using just hand signs like a thumbs up/down or a 1-5. Anyone looking to gather meaningful feedback can create their own survey and choose what hand signs they want to use for that survey. The survey data/responses can be accessed and analyzed later on by the creator of that survey.

To use 'GiveMeASign' you would choose the type of hand signs that would be used to answer questions in your survey, then you would make the questions of your survey. You can have many or just a single question(s). Then put the app up on a screen (like a tv or a tablet) with a webcam attached and leave it at a convenient place for customers to give their feedback. For example a restaurant could have this setup right before the exit where customers could quickly give a rating out of 1-5 for a certain dish on the menu (if they ordered that dish).

## How we built it
We made this as a web-app to be ran in a web browser. For our database, we used MongoDB to store survey data and survey responses. We basically made a MongoDB cluster and used MongoDB Compass to access the database so that we could all work with the same database remotely. Our main image classification algorithm is written in Python3 using OpenCV. For the backend, we again used Python3 because our main classification algorithm is written in Python3 so it made things a bit easier. We also used the Flask framework to make our Python3 backend. We also made an API using flask for the frontend to interact with the backend so that the frontend can fetch classifications of images and fetch survey data. For the frontend we used HTML, JavaScript, and CSS with Bootstrap. We also used Jinja2 to execute Python3 code in the frontend. 

## Repo Structure
- assets: All files relating to design of the app
- flask-app-older: Older version of the app, not meant for consumer use, only for devs
- flask-app: Main app where all the code is

## Challenges we ran into
- We had plenty of confusion on how to send images from the frontend webcam to the backend where it can be classified
- We had some confusion with using links and routing in the frontend html because when using flask there's a certain way to do page routing and there's a certain way to link external stylesheets or JavaScript scripts.
- We had a lot of problems with the webcam footage not showing up where any issue in the JavaScript would result in the webcam footage not showing and there were a lot of small issues with the JavaScript so the webcam footage would oftentimes not show up

## Accomplishments that we're proud of
- Making an algorithm to quickly and accurately classify various hand signs
- Creating a separate front and back end and connecting them using an API
- Creating a beautiful and elegant design and logo for our web-app that complements our app very well

## What we learned
- How use OpenCV effectively to create a fast image recognition algorithm
- How to use Flask to make a backend for a web-app
- How to use MongoDB to store and retrieve data and how to use MongoDB Compass to use the same database remotely 

## What's next for GiveMeASign
- Right now we only have thumbs up/down and numerical 1-5 hand signs that we can classify but we'd like to add more hand signs that we can classify later on
- We want to continue to improve our classification algorithm to classify images even faster
- We want to improve the user interface and design of the overall web-app to make it easier and more intuitive for users
- We want to spread out to other platforms like IOS, Android, or even make a desktop application to make our app more accessible for everyone regardless of what platform they're on 
- We want to eventually get a domain name and deploy this website for everyone to use 


