# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
# THE NEXT TWO LINES IMPORT TWO LIBRARIES. LINE 4 IS IMPORTING A SCRAPER WIKI LIBRARY WHICH IS USED FOR SCRAPING PAGES.
import scraperwiki
import lxml.html
#
print("hello")
# # Read in a page
html = scraperwiki.scrape("http://foo.com")
print(html)
# EXPLANATION: THE ABOVE CODE HAS A VARIABLE WHICH IS HTML, THE FUNCTION .scrape AND THE ("STRING"). 
# SO THE CODE HAS GONE TO THIS SITE AND SCRAPED THE HTML WITHIN THE STRING. WE RAN THIS ON MORPH.IO. 
# NOW, WE WANT TO BE MORE SPECIFIC, IT HAS JUST SCRAPED THE WHOLE PAGE. SO WE ARE GOING TO DRILL DOWN FURTHER.
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
print(root.cssselect("div#footer"))
#ROOT = HAS CREATED A NEW VARIABLE. THE WORD ROOT IS COMPLETELY ARBITUARY, YOU COULD NAME IS ANYTHING.
#LXML.HTML is a library we have imported. It is a library which allows you to convert webpages.
#FROMSTRING - IS A FUNCTION WHICH CONVERTS SOMETHING FROM A STRING OF CHARACTERS IN TO SOMETHING THAT CAN BE DRILLED DOWN IN TO.
#THE STRING FROM LXML.HTML WILL THEN BE MADE IN TO A NEW VARIABLE UNDER ROOT.
#CSSSELECT IS A FUNCTION TO DRILL DOWN IN TO THE CODE ON THE PAGE. THIS LINE OF CODE IS ASKING IT TO MAKE A MATCH TO ANY HTML TAGS WITHIN THE STRING THAT MATCH THAT CRITERIA.
#SO "DIVALIGN-'LEFT'... DIV AND ALIGN LEFT ARE HTML TAGS, ALIGN LEFT IS AN ATTRIBUTE, SO WE'RE ASKING IT TO GRAB ANYTHING THAT MATCHES THESE. 
#WE RAN THIS ON MORPH.IO AND IT CAME BACK WITH EMPTY [ ]. THIS MEANS IT RETURNED NO MATCHES FOR DIVALIGN LEFT. 
listofmatches=root.cssselect("a")
#THIS CODE TURNS THE HTML WE'VE SCRAPED INTO SOMETHING THAT MAKES SENSE.
for match in listofmatches: 
  print(match)
primt(lxml.html.tostring(match))
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
