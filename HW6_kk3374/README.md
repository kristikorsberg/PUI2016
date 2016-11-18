In HW6, we had two assignments. The first was to follow a skeleton notebook and conduct
several analyses about energy consumption and building data. I downloaded both energy and
building datasets from the NYC Open Data and plotted a scatter matrix of the energy data. 
This matrix identified the columns which had float values, or values able to be converted 
to float. Since 'Site EUI(kBtu/ft2)' and 'Reported Property Floor Area (Building(s)) (ft²)'
were not included in the plot, I knew that I had to conver those values which could not
be converted to float to 'NAN' values. This would be important for numerical analyses
conducted later in the assignment. After passing the 'canconvert' through the np.vectorize()
function, I merged the energy and building datasets. I also created a new column entitled
'Total Energy', which was the total energy usage of each building unit, rather than energy 
consumption by square foot. I made two scatter plots, one with Number of Units as a 
function of Energy Consumption and another with Energy Consumption as a function of
Number of Units. There was no obvious linear relationship, so I transformed the values
in each dataframe series to log base 10 and re-plotted the two graphs. Next, I had to
plot a line of best fit. I ran into some issues, here and reached out to Federica over
the weekend. Initially, I did not cut the energy and units datasets after converting
them to logged units, which broke the Jupyter Notebook kernel. Federica reminded me that
log values have infinity values, so it would be necessary to cut the data. After 
limiting the datasets to ranges of values, I re-ran the regression analysis and successfully
plotted the regression lines. Federica also alerted me that my notebook was using a lot
of memory because I created new dataframe variables every time I manipulated the data. 
For that reason, I renamed several dataframes by overwriting existing variable names.
After plotting the regression lines, I manually calculated the chi squared values. I
also calculated and plotted the second degree polynomial. I concluded that, since the R2
value was higher for the second degree polynomial, that it was a better fit than the 
linear model. 

Ben Miller helped me obtain the units dataset - I did not know that I could copy the link
address from NYC Open Data. After he told me the zip file could be downloaded in that way,
I was able to open the files.

Jonathan Pichot showed me how to concisely write a curl statement, which I used to pull
the energy CSV. 

Danny Fay shared with me the statsmodels syntax for writing a second degree polynomial. 
I wasn't sure how to do that, and had written a regression fit with the numpy polyfit and 
numpy poly1d functions. 

Federica provided feedback about log regression models, how to write Python 2.7 syntax to be 
compatible with Python 3, and with memory saving techniques by renaming variables instead
of creating new ones. 

I shared my workflow with Santiago Carillo. I helped him troubleshoot some issues he
ran into with converting values to either floats or 'NAN's. I also shared my method of
plotting a second degree polynomial with numpy polyfit and poly1d with Nicola Macchitella. 


Assignment two required that we conduct a statistical analysis on the Citi Bike data
that was analyzed for HW3. I ran a t-test and incorporated feedback from both reviewers
in my final notebook. The Authorea link to my post is here: 
https://www.authorea.com/users/106897/articles/133954/_show_article.

# FBB
the analysis is quite good, and the writing is fine. But the report has no figures or tables to show that data. that is essentia in a scientific report
