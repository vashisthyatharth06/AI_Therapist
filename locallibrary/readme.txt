# Local Library

The purpose of the website is to provide an online catalog for a small local library, 
where users can browse available books and manage their accounts.
This is developed using Python framework Django and html,css,bootstrap.
Their are 2 views of the website :
1> User View:-

  1.In this you can register and login into this site.
  2.One can see the list of all authors and books in the library without doing login through
    'All Books' and 'All authors' views.
  3.After doing login,one can see the list of borrowed books by him/her through 'My borrowed' view.
  Important:-
  Staff member can also login into this site havig permission to see the list of all borrowed books of
  library through "All borrowed" view and only staff members can see this on site due to special permission given
  to them by admin.They can also renew the book through this site.Special permission given to them by admin is "can_mark_returned".
  One of the normal users of the site:-
  username:Vishal
  password: bcs2018063


 2> Admin View
    This view is protected by authentication and is available only for superuser
    
    username: Yatharth
    password: bcs2018065
    
   Since,most of the things are done through our User View,there is one feature which is implemented through admin view :
    
    1.Create, edit and delete authors.
    2.Create, edit and delete books.
    3.Create, edit, renew(by changing status of book instances from "on loan" to "available" or changing "due_back" date)
      and delete book instances.
    4.Create and delete genres.
    5.Can assign special permission to those users which are staff members so that they can renew books throughn the user view itself.