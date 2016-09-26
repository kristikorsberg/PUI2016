# PUI2016

The tasks associated with Homework Three are itemized below. I describe what I did to personally
contribute, and explain who I worked with.

Our first task was to read "The Earth is Round", by Jacob Cohen. I completed this work 
independently.

Assignment 1 required that we write a Jupyter Notebook that visually depicts the Central
Limit Theorem. Inside the notebook, we had to create 100 random samples of different 
sizes ranging between between 10 and 2000, from 5 different distributions (Normal,
Poisson, Binomial, Chi-Squared, and one of our choice, for which I selected exponential. 
For each sample, we plotted the sample's mean against the sample's size. For each plot,
we were to describe the plot in terms of the law of large numbers. Finally, we were to
plot all of the distributions of all sample means as a histogram. For extra credit,
we could fit a Gaussian distribution to the distribution of means. 

In order to complete this assignment, I looked at the skeleton notebook, however I found
the code from class to be much more helpful. I pushed my Lecture 3 Notes to my HW3 repo
for reference, but after looking at the code from lecture, I was able to write a function
for each distribution, which pulled the mean of a randomly selected sample size. Once I
had the function written to generate mean, I enclosed it in a for loop, which randomly 
generated 100 samples from the range 10-2000. I enclosed the means inside of a list and
plotted the 'IndexOfValues', which was defined as each sample size against the mean of the
sample. While I worked on this independently, I discussed the Central Limit Theorem
extensively with Danny Fay on Wednesday. He and I also wrote code independently for each
distribution and then compared our results after writing the notebook. In order to write
the function, I needed to look up each Numpy command online and determine the parameters
for each distribution. I consulted with Himanshu at the beginning of the assignment as
well, to be sure that I understood the 'Pythonic' code written in class. I had some 
difficulty with the binomial distribution, in that I could not ensure that the scatter
plot would follow the funnel shape, despite the fact that the histogram was accurate.

#NEED TO CHECK BINOMIAL SCATTER DISTRIBUTION. IT IS NOT A FUNNEL. 
#NEED TO FIT GAUSSIAN DISTRIBUTION

For Assignment 2, we made a Jupyter Notebook inside Compute, which sets the foundation for 
a data driven insight about Citi Bike data. We had to create null and alternative 
hypotheses with a confidence level, use Pandas to read the Citi Bike data directly from
its website, display the first few rows of the data in the notebook, create a new data-
frame with the information that we plan to analyze, and plot the data.

In order to complete this assignment, I had to study Pandas. I found Chris Albon's
tutorials extremely useful, and ended up writing a 'Pandas Practice' Jupyter Notebook
to familiarize myself with the commands necessary to manipulate dataframes. I also found
a tutorial, which is cited in the notebook, about how to group data by selected time frames.
This proved extremely helpful when plotting. I worked on this notebook mostly independently
as well, because I wanted to learn Pandas and have a strong foundation for the module
before heading into the rest of the semester. I was interested in analyzing bike riding
patterns as it relates to commuting, so I wrote two pairs of hypotheses and included two
plots and datasets, one for each. I had a difficult time pushing the notebook to github,
so I reached to Sabreen after making several efforts to troubleshoot on my own. 

Assignment 3 required that we complete the lab from lecture. In this lab, we had to write
a null and alternative hypothesis for the bus commute time data; perform a z test; and
interpret the z statistic we generated.

I read about z statistics in the "Statistics in a Nutshell" book, and proceeded to use
the formula provided by Federica in the homework assignment. I had a difficult time
pulling the data from github so I saved the file locally and worked on it from there.


