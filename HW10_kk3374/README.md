This is the readme for HW10. In HW10, we were to calculate the spatial autocorrelation of Citi Bike ridership by US Census Tract. I counted summer months as June, July, August, and September and winter months as December, January, February, and March. In summer, the Moran's I, which identifies the strength and direction of spatial autocorrelation was .644, and for the winter, it was .662. In both cases, there is a less than .001 probability that either correlation occurred by chance. 

For summer and winter, the spatial autocorrelation broke down as follows: 
Number of summer hotspots: 189
Number of summer coldspots: 243
Number of winter hotspots: 198
Number of summer coldspots: 214

There are 432 autocorrelated CTs in the summer and 412 autocorrelated CTs in the winter . From this data, I can conclude that initializing a Citi Bike trip is  spatially autocorrelated in more Census Tracts in the summertime than the wintertime, I.E., the breadth of autocorrelation for Citi Bike trips is greater when the weather is warm than when it is cold. This makes sense when thinking about the how temperature and general weather patterns would impact ridership. For example, it seems more likely that public spaces such as Central Park, may be used more in the summer. Similarly, there are more tourists in the summer time, and it is also plausible that they might travel to the same popular places in Manhattan: the Chelsea Piers and waterfront, Central Park, and the World Trade Center. In the winter, Citi Bike may be used predominantly by commuters, who travel from all over the boroughs, which could explain the drop in spatial autocorrelation. 

From a prediction standpoint, it seems that this model would be most effective at predicting station popularity in the summer, simply because there is a higer volume of CT autocorrelation than in the winter. 

For this assignment, I wrote the notebook independently and then discussed the implications of differing counts of autocorrelation with Geoff Perrin. 
