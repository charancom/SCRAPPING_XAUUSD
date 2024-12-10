There are two parts to the assignment:
1. scraping Hourly and 15 mins intervals of XAUUSD.
2. Scraping the News from Forex Factory.

scraping hourly and 15 mins intervals of XAUUSD:
So basically the approach chosen was to use basic requests documentation, and interact with an api.
the api of tingo was reffered during this process.
And it was just a matter of lines of code to extract the data and the features needed in a click.


Scraping the News from Forex Factory
So basically here I have Used the framework selenium to basically the automate the whole process of scraping it from the web.
So Regarding the approach that was used, the elements of the were correctly extracted.
the category the impact belongs was extracted from the webpage.
the format of index for the first entry of every day is different from the format indexes for the rest of the entries in the table on a particular day.
this index case was taken care of.
then after that the required features have been extracted for a single page.

Now I have written a program to basically copy this code 30 times, with 30 different dates for the month october.
And then all the 30 were ran at once.
And 30 csv files were extracted, and another file was used to merge them sequentially in an order, and all the data is aggregated into a single file.
