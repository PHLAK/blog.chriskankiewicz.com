Title: Beginers Guide To Search Engine Optimization
Date: 2009-11-20 00:00
Author: Chris Kankiewicz
Category: Web Dev
Tags: Google, Keywords, robots.txt, Search Engine Optimization, SEO, Sitemaps, Yahoo!
Slug: beginers-guide-to-search-engine-optimization

The following is a quick list of optimizations that, in my years of web
development, I have observed will help increase your sites search engine
ranking. While none of these processes are guaranteed to make your site #1 in
Google overnight, I can promise that by implementing all (or even some) of these
items, in time your site's rank will rise.

The following items are clean, honest ways to optimize your site. I do not
condone, nor solicit, any form of "black hat" search engine optimization and
frown upon it greatly. If that's what you're aiming to implement, I sincerely
hope that Google blacklists your site tomorrow. Please don't send me any emails
asking how to get your sight listed as #1 tomorrow.

Now, onto the list.

## Code to Standards

Whether or not you're aiming for SEO, keeping your code standards compliant will
make your site better all around and help make post-development changes much
simpler. While the effectiveness of coding to standards is still debated in the
SEO community, it's generally believed that a standards compliant page will rank
slightly higher than a non-compliant page with the same content.

Also, by adhering to standards, you'll have a much easier time implementing the
rest of the processes on this list.

## Content is King

The first and foremost rule you'll hear from many SEO "experts" mouth will most
likely be "content is king." Of all the processes detailed on this page, if your
site doesn't contain valuable content to the end user, your page rank will
likely not be very high.

To take this concept one step further, I'm going to add to that saying to create
my own spin off. As opposed to just "content", my saying specifies that "dynamic
content is king." While a site with any content at all is far superior to one
without, I believe that adding something as simple as a twitter feed to your
home page will help convince the search engines that your site is more
important. After all, users (and therefore, probably search engines) love new
content. To expand upon this idea, if it would fit your site, try adding a blog
or a forum to keep that content fresh.

## Separate Content and Style

When a search engine crawls your site, it doesn't see the same thing your end
use sees. The search engine sees the underlying code that is output by your
site. For an example of what the search engine sees, right click your web page
and choose "View Source." This is a much more accurate (though not exact)
representation of what the search engine sees.

If you clutter your code with multitudes of nested tables and lots of in-line
styling properties the search engine may have a hard time finding your content
to index. Instead of nesting table after table, consider using divs. If you
don't know how to use divs, I strongly suggest you learn. Also, instead of
adding the "style" property in line with your (X)HTML, create a separate file
named style.css and add the following code between your pages head tags to call
this file upon page load:

    <link rel="stylesheet" href="style.css" type="text/css"></link>

All you have to do now is add your CSS elements to this style.css file, and give
your (X)HTML element either a class or id. For more on classes and ids, see 
[http://www.w3schools.com/Css/css_syntax.asp](http://www.w3schools.com/Css/css_syntax.asp).

## Use Human Readable URL's

The ability for a user to accurately guess what a page will contain by looking
at a link will not only help your users find what they're looking for, but is
also a good SEO technique. See below for an example of human readable URL's.

Good Examples:

  * www.domain.com/dog-food  
  * www.domain.com/dog/food

Poor Examples:

  * www.domain.com/1337  
  * www.domain.com/index.php?page=1337

## Page Title Format

While it may not seem too important, the title of your page can make a
difference to your page ranking. While a title in the format of "Site Name |
Page Title" is in no way bad, it's generally believed that the best format for a
tile is "Page Title | Site Name." Also, there are many pages out there that list
every directory in their title, this is not necessary and clutters the title so
readers have a tougher time identifying the page.

Good examples:

  * SEO Guide | Web Geek  
  * CK-Gallery • Web Geek  
  * Menu – Taco Bell

Poor examples:

  * Web Geek | SEO Guide  
  * Web Geek > Web Development > SEO Guide  
  * www.web-geek.net | projects | php | ck-gallery

## Header Tag Prioritization

The importance of a title should directly affect which header tag that title
gets (ie `<h1>`. `<h2>`, `<h3>`, etc...).  The more important a title is, the
closer to `<h1>` the title should be with `<h1>` being the page title and
something like a paragraph heading being an `<h2>` or `<h3>` depending on it's
importance.  If one topic is just as important as another, they should have the
same title tag.

## Create a Sitemap

Every website with more than a single page should have a sitemap. You can make a
sitemap in many ways and in many formats, though the most widely accepted by
most search engines is an XML sitemap.

My favorite site for sitemap generation is
[http://www.xml-sitemaps.com/](http://www.xml-sitemaps.com/). This site will
automatically crawl up to 500 pages and generate XML, GZipped, and HTML sitemaps
that you can then upload to your own site. Once you have uploaded your sitemap,
head on over to
[https://www.google.com/webmasters/tools](https://www.google.com/webmasters/tools)
and add your sitemap for Google to index.

**Note:** Even though you can put a sitemap anywhere, the most common location
for a sitemap is in your sites root directory
(`http://www.web-geek.net/sitemap.xml`)

## Use Relevant Keywords

Keywords are a difficult area in SEO. You need to specify keywords relevant to
your site but you don't want to have too many keywords or you'll be hurting your
site more than helping. The generally accepted maximum number of keywords to
include on your page is usually 10, for most sites, and definitely no more than
20 for larger sites. Though major search engines don't take the number of
keywords on your page into consideration when assigning you a page rank, by
having to many keywords, it's harder for a search engine to identify which ones
are more relevant than others.

To include keywords on your page, place the following code between your head
tags.

    <meta name="keywords" content="keyword 1, keyword 2, keyword 3"></meta>

Also, you generally don't want the exact same keywords on any pages unless
they're content matches. Give each page keywords that are relevant to the
content on that page. You also may wish to consider generating your keywords
dynamically.

## Use the "title" Attribute for Links

When creating a link, be sure to include a relevant description of the link
using the title attribute. This adds content for a search engine to pick up and
also, when a user hovers over that link, they will get a popup showing your
description.

Example:

    <a href="http://www.web-geek.net/ck-gallery" title="Dynamic PHP Photo Gallery">CK-Gallery</a>

The above code will create the following link (hover over it to see the title):
[CK-Gallery](http://www.web-geek.net/ck-gallery "Dynamic PHP Photo Gallery")

## Submit your site for indexing

One of the best ways to get your site noticed by a search engine is to manually
submit it for indexing to major search engines. This is especially useful when
your site isn't yet listed in a search engine.

Google: [http://www.google.com/addurl/](http://www.google.com/addurl/)

Yahoo:
[http://siteexplorer.search.yahoo.com/submit](http://siteexplorer.search.yahoo.com/submit)

## Create a robots.txt file

A robots.txt file can be used to limit what directories/files a web robot can
access. This helps prevent a robot from accessing data you do not wish to be
cached by search engines and instead cache only the pages you want to appear. A
good resource on creating and using a robots.txt file can be found at
[http://www.robotstxt.org/robotstxt.html](http://www.robotstxt.org/robotstxt.html).
