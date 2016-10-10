This is the README for PUI HW 5:

I independently read the '10 Simple Rules for the Care and Feeding of Scientific Data'.

Assignment One asked us to use two different statistical tests to test the goodness of
fit for the age of Citi Bike users against two different random distributions. I chose
to use the KS and the AD tests in the normal and Poisson distributions. In order to 
complete the assignment, I consulted with Santiago Carillo. He told me that, in order
to run the scipy.stats.ks() function accurately, I had to include some information about
significant moments in the Citi Bike age dataset - namely, standard deviation and mean. 
After calculating those variables and passing them into the function, the KS test worked
and I was rejected the null hypothesis. All other tests were conducted in a similar
fashion, by identifying the parameters that needed to be passed through the scipy.stats
function, and printing the results.

Assignment Two asked us to analyze the income parity between men and women. According to 
my regression model, a man's salary is about 1.5 times a woman's salary. I completed
most of this work independently, and shared my code with Laura Gladson and Santiago
Carillo.

Assignment Three asked us to write null and alternative hypotheses for several different
types of statistical analyses. I was unsure how to set up the experiment in the first
example, so I consulted with Laura Gladson, who provided guidance about what to do. 
