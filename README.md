# Programming-Query-Blog-Django-3.0
![Optional Text](./main/myFolder/Capture.png)
Blog web app built using dajngo 3.0, HTML5, CSS. The app contains 2 main models which are:

Custom user model (users can register, post new blog posts and comment on every other blog post)

Blog Post model, Comment model (simillar infrastructure for both of these classes)

Comments and Blog Posts can be edited and deleted by their respective authors (and only by them). Each of the objects in these classes has it's own unique slug field identifier which is used to implement the aformentined functionalities.

I used dajngo template tags in order to set the behaviour of most of the web pages and in addition, I implemented a search bar using a search function that is defined inside of the blog model's views file.

The app was designed using bootstrap and custom css.
You can check out the web app in the following address: eliyacobov1.pythonanywhere.com
