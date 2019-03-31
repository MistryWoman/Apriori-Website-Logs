# AprioriWebsiteLogs
Analyzing anonymized microsoft website user logs to predict user behavior and preferences.

Performing Assosciation Rule Learning on 38,000 anonymous Microsoft website users.
For each user, the data lists all the areas of the web site (Vroots) that user visited in a one week timeframe.

For each user, there is a case line followed by zero or more vote lines.

For example:

C,"10164",10164

V,1123,1

V,1009,1

V,1052,1

Where:
 C  marks this as a case line,
 
'10164' is the case ID number of a user,

'V' marks the vote lines for this case,

'1123', 1009', 1052' are the attributes ID's of Vroots that a user visited.

'1' may be ignored.



--------------------------------------------------------------------------------------------------------------------

The user defined functions used :

extract(): To extract the location of every case and it’s position in dataframe.

makearray():  Makes a list from the positional array passed into function and extracts the votes associated with a specific case.

finaldict():  Iterates through each Case field and calls makearray to generate a dictionary.


Using the TranscationEncoder() method we can transform the input(i.e. List of lists into a matrix data frame)
