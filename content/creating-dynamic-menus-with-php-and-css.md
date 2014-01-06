Title: Creating Dynamic Menus with PHP and CSS
Date: 2008-10-05 00:00
Author: chris
Category: Code
Tags: CSS, Dynamic Menus, HTML, PHP
Slug: creating-dynamic-menus-with-php-and-css

Want to pep up your web page with some dynamic menus? Here’s a simple
solution that only requires a few lines of PHP and CSS.

\*\*UPDATE (11/1/08):\*\* Simplified the header code and edited the
syntax of the list element echo code.

<!--more-->

\#\# The PHP

Add the following to the top of your page (before the DOCTYPE or HTML
tag).

<?php<br ?> // Get current page file name  
\$page = basename(\$\_SERVER["PHP\_SELF"]);  
?\>

Then add the following to your menu item where you want the class
designation to show up.

Each link should have this piece of code in it. Make sure you replace
“index.php” with the appropriate file name for the page. Example:

<div id="navigation">
-   [\>Home][]
-   [\>Resume][]
-   [\>Photography][]
-   [\>About][]
-   [\>Contact][]

</div>
\*\*Note:\*\* the 2 chevrons “\>\>” at the end are on purpose. One
closes the PHP tag the other closes the ‘a’ tag.

\#\# The CSS

Lastly, add the following element to your style sheet and style it as
you please.

\#navigation ul li a.current {  
background-color: \#FFF;  
border-bottom: 1px solid \#FFF;  
}

This process will result in the following:

![Tabs with
HTML/CSS/PHP](https://lh4.googleusercontent.com/\_7VR99N\_W06c/TZJfibqsQZI/AAAAAAAAAR8/hiz3tP9DuG0/s640/ck-menu-tabs.png)

  [\>Home]: index.php
  [\>Resume]: resume.php
  [\>Photography]: photography.php
  [\>About]: about.php
  [\>Contact]: contact.php
