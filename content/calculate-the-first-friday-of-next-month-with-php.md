Title: Calculate the first Friday of next month with PHP
Date: 2008-10-20 00:00
Author: chris
Category: Code
Tags: Code, First Friday, PHP, PHX2600
Slug: calculate-the-first-friday-of-next-month-with-php

\*\*UPDATE:\*\* This script has been updated, see:
[https://github.com/PHX2600/FirstFriday](https://github.com/PHX2600/FirstFriday)

While developing phx2600.org, I ran into a slight dilemma. The PHX2600
meetings occur once a month on the first Friday of every month, and we
wanted to display that on the site. However, it was becoming a tedious
chore to change the date once a month manually. So, being the automation
addict I am, I thought, why not write a script. So one night I hammered
out the following script that will calculate the first Friday of next
month:

<!--more-->

<?php< p ?>

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
\* FILENAME: first-friday.php \*  
\* AUTHOR: Chris Kankiewicz [PHLAK] \*  
\* WEBSITE: http://www.web-geek.net \*  

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

// START FUNCTIONS

function get\_day(\$describer,\$weekday,\$reference\_date) { //
\$reference\_date format = m-Y

\$d = explode('-',\$reference\_date);

switch (\$describer) {  
case 'first': \$offset = get\_day\_offset(\$reference\_date,\$weekday);
break;  
}

\$r = mktime(0,0,0,\$d[0],1+\$offset,\$d[1]);  
return \$r; //returns timestamp format  
}

function get\_day\_offset(\$anchor,\$target) { //\$anchor format = m-Y

\$ts = explode('-',\$anchor);  
\$ts = mktime(0,0,0,\$ts[0],'01',\$ts[1]);

\$anchor = date("w",\$ts);  
\$target = strtolower(\$target);  
\$days = array(  
'sunday'=\>0,  
'monday'=\>1,  
'tuesday'=\>2,  
'wednesday'=\>3,  
'thursday'=\>4,  
'friday'=\>5,  
'saturday'=\>6  
);

\$offset = \$days[\$target] - \$anchor;

if (\$offset\<0) \$offset+=7;

return \$offset; //returns 0-6 for use in get\_day();  
}

//END FUNCTIONS

\$t = getdate(); //Get today's date

\$today = date('m-Y',\$t[0]); //Display today's date as MM-YYYY

//Calculate Next Month  
if(\$t[mon] == '12'){  
\$nm = '1-'.(\$t[year]+1);  
} elseif(\$t[mday] \<= '7' && \$t[wday] \<= '5') {  
\$nm = (\$t[mon]).'-'.\$t[year];  
} else {  
\$nm = (\$t[mon]+1).'-'.\$t[year];  
}

\$date = get\_day("first", "friday", \$nm);

//Checks if today is after the first friday of the month  
if(\$t[mon] == date('m',\$date)  
&& \$t[mday] \> date('j',\$date)  
&& \$t[mon] == '12') {  
\$nm = '1-'.(\$t[year]+1);  
\$ff = get\_day("first", "friday", \$nm);  
} elseif(\$t[mon] == date('m',\$date)  
&& \$t[mday] \> date('j',\$date) && \$t[mon] != '12') {  
\$nm = (\$t[mon]+1).'-'.\$t[year];  
\$ff = get\_day("first","friday",\$nm);  
} else {  
\$ff = \$date;  
}

// I know this code is crap, deal with it or fix it yourself!

echo date("F j, Y", \$ff);

?\>

I apologies for the crappy code, I was either tired, drunk or both the
night I wrote this.
