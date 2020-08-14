# Pizza ordering app

In this project, a pizza ordering application was created.
1. Register and login
Two templates were used for resiter and login. The registration form was customized by form.py

When the user logged in, a list of categorized items were on the page with a link allow the user to take further 
actions.

2. Tables Category, Size, Topping, Extra were created in model.py.
Itemfororder table used foreignkey of category and size.
the extras were displayed as boolean variable in the table.

To load the order history into admin page, another table of Orderhistory was also created.

3. When a user logged in, a list of itemfororder are there for selecting.
The user could click a link under certain category he/she interested.
If the item has toppings, a dropdown menu is available for selection. (This function is not complete due to time limit).
If the item has extra, the check box beside the extra items is available for check. The price change upon the checkbox is handled by JavaScript code included in the page of item.html.

By clicking the button addtocart, the selected item will be added to the cart. All the selected items will be displayed in a table. And the total price is beside for confirmation. (remove selected item, and increase the number of certain items have been figured out using Javascript. But I don't have time to redo this part using django)
I used lists names and prices to save the item records in the cart.

In cart.html and checkout.html, a link returning to item list was added. The user could go back to add more items at any time he/she wants.

4. In the checkout route, the values stored in the lists names and prices will be emptyed. And an email will be sent to the user.
After checkout, the cart then is emptied too.

5. All the urls have been updated to urls.py

6. All the relevant tables have been included in the admin.py

7. settings.py has been revised to send email

8. All the templates have been reformated by Visual Studio Code

9. All the python files have been reformated by pycharm

Thanks

