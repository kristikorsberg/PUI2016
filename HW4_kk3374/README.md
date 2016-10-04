This is the README.md file for PUI HW4

1. I completed the reading entitled 'Estimating the Reproducibility of Social Sciences"

2. I reviewed Hrafnkell Hjorleifsson's Citi Bike repo, and determined that he should use a one-tailed t-test to evaluate 
the difference in means between weekday ridership and weekend day ridership. I emailed Federica to ensure that I understood
the one-tailed and two-tailed t-test so that I could provide him with the most accurate recommendation. My CitibikeReview_kk3374.md file can be found in his HW4 PUI repository. 

3. I chose to evaluate a chi squared study and a linear regression study, which were representative of both types of statistical tests that identify a difference in means and assess the relationship between independent and dependent variables. The tables are at the bottom of this README.md.

4. For the third assignment, I worked independently to learn about the z test and the chi squared test. In order to find the z and chi squared statistics, I followed Federica's skeleton notebook, read "Introduction to Statistics", and watched several videos through Khan Academy. I met with Laura Gladson, Nonie Mathur, and Santiago Carrillo on Monday, October 3 and they clarified some points for me. First, I learned that I was using the wrong value for the 'area' variable. I used the .998 value from class when I should have looked at the z score table for the .846 value, stored in variable 'z_2y'. We also conferred with each other about the chi squared contingency table. 

5. For the fourth assignment, I followed Federica's skeleton notebook to create a Citi Bike dataframe for one month of data. I conducted the initial dataframe modifications, adding columns for male and female riders, and binning them into different age groups. Then I created the reducted dataframe by pulling every 200th row. I ran the KS statistic for the entire dataframe and the reducted dataframe. In order to complete the Pearson and Spearman tests, I worked with Laura Gladson, Nonie Mathur, and Santiago Carrillo. Specifically, we worked through sorting and grouping the male and female bikers. My dataset had more male than female riders, so I reduced the male dataset and attempted to preserve the variance and spread of the data. I thought the best way to do that would be to take the middle set of numbers in the list that was equal to the number of the entire range of female riders. With this modified dataset, I conducted the Pearson and Spearman tests. For each test, the null hypothesis was rejected. A brief summary of the use case for each test is listed either in markdown cells or is commented out in codd cells.

| *Statistical Analyses	|  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var | Control Var type  | Question to be answered | _H0_ | alpha | link to paper **| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
Chi Squared	| 1, month of birth | categorical | 1, risk of mortality | discrete | 2, age and education | categorical | 	is there a relation between month of birth and mortality risk? | risk of mortality is the same regardless of birth month | 0.001 | [Birth Year as Predictor of Age at Death](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0056425) |
  |||||||||

| *Statistical Analyses	|  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var | Control Var type  | Question to be answered | _H0_ | alpha | link to paper **| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
multiple regression	| 5, age, obesity, alcoholism, family history of hypertension, diabetes | discrete, categorical, categorical, categorical, categorical | 1, hypertension | discrete | unknown | unknown | is there a relation between month of birth and mortality risk? | socio-demographic and clinical attributes do not affect the prevalence of hypertension amont adults in the indigenous village of Jaguapiru, Brazil | 0.001 | [Socio-economic and Clinical Factors that Affect Prevalence of Hypertension, Jaguapiru, Brazil](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0086278) |
  |||||||||

