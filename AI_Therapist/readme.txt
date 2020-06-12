# AI Therapist


This is a AI Therapist website using Python framework Django and sqlite3.
Their are 2 views of the website :
1> User View

  In this you can register and login into this site, see more info about the possible advanced version of site with help of 'about' view, 
  chat with the bot through 'chat' view,
  see the list of doctors linked to our site through 'doctorlist' view, 
  user can see all it's chat timeline which is the most exciting part about the site through 'calendarlist' view
  and can logout from the site.
  So,register and and relax yourself using this site.
  
  
  
 2> Admin View
    This view is protected by authentication and is available only for superuser
    
    username: Yatharth
    password: 12345678
    
   Since,most of the things are done through our User View,there is one feature which is implemented through admin view :
    
    1.Create, edit and delete doctors:Doctors will link to the admin through mobile number of admin mentioned in user's site.
                                      Then,admin will add,edit and delete doctor's info from the user site accordingly after talking
                                      with doctor. 