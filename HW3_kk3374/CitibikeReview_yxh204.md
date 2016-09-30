Hey Kristi,

I really like your ideas about the CitiBike dataset. I will say that for both ideas, the null and alternative hypotheses have been formulated correctly. For next time, it will be even better if you provided mathematical formulae for your null and alternative hypotheses. For example, in idea 1, you could’ve wrote the following:

Let $\mu_wd$ and $\mu_we$ denote the population means of ridership on weekdays and weekends respectively,

Then, 

$H_0: \mu_wd - \mu_we \leq 0$

$H_1: \mu_wd - \mu_we > 0$

As for cleaning the original dataset and arriving at something useful for your analysis, I recommend using the `pd.DataFrame` method .groupby() chained with .apply(). It will make tallying the total counts much easier.
If you are testing for differences in the population mean in both cases, I would recommend the use of the t-test for mean instead of the Z-test. This is because we don’t know the population variance (or standard deviation) of either average number of trips during weekdays or weekends, or average trip duration during the weekdays or weekends.