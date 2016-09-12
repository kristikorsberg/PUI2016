# PUI2016

The tasks associated with Homework One are itemized below. I describe what I did to personally
contribute, and explain who I worked with.

1. I submitted my github account name on NYUClasses and read 'What is the Question?'
2. The lab from class introduced me to github, and the repository sharing that can be achieved
between my local machine, my remote profile on Compute, my github online repository, and my
classmates' online repositories. 
3. In class, I created a repo in Compute called 'gittest_kkorsberg' and added 'myfirstfile.txt'.
I pushed this to github online, which didn't work initially because I didn't have an online respository
created. After making PUI2016_kk3374, I pushed the existing repository from the command line. Inside 
Compute I added the git origin <https://github.com/kristikorsberg/gittest_kkorsberg>. I then made changes 
to the file from my Compute profile committed and pushed them to the online repo. I practiced the process 
of editing 'myfirstfile.txt' on the Compute machine and the online repo several different times, which 
can be seen in lines 3-11.
*Please note that my gittest repository is not saved in my PUI2016_kk3374 repo, it is saved in its own
repo called 'gittest_kkorsberg'. 
4. I attended Sabreen's Office Hours on Thursday, September 8. Initially I was there to review environmental
variables (more on that below), but I ended up working with Danny, Victor, and Yuan on github forking. I
forked Danny's gittest file. On September 9, I also forked Shay's 'myfirstfile.txt' file inside her
gittest repository. Both Shay and Danny successfully merged my edits to her file. 
I sought help from Sabreen with forking. She assisted me in identifying which file paths to copy into the 
'git clone' command. 
5. On September 9, I received a pull request from Shay because she made edits to my 'myfirstfile.txt' file.
I merged these edits with my master file, which can be seen on line 12 in my gittest_kkorsberg 'myfirstfile.txt'. 
Later in the week, Victor forked my 'myfirstfile.txt', and I accepted his changes, which are reflected
on line 13. I also received a fork request from Patrick, which I accepted on September 12. I forked his first
file as well. 
6. On September 8, I read Ryan Chadwick's bash tutorial in order to set environment variables. I created
two variables in my .bash_profile to test the process, however I did not complete the task because I wasn't 
sure where to save the alias. I also didn't know I had to 'source .bash_profile' to make the system 
acknowledge the new lines inside the file. The following day, at Sabreen's office hours, I got some 
guidance about what to do. Himanshu arrived and explained to the group (Victor, Yuan, Danny, and 
myself) what environment variables are and why they are saved inside the .bash_profile on Macs. With that information, 
we created new variables and an alias inside our .bash_profile files. Himanshu then told us that to complete
the process we had to 'source /.bash_profile' in the terminal. I created the variable and alias for pui2016 
on my local machine. 
7. On September 9, using the process that Himanshu explained the day prior, I created environment 
variables on Compute. I learned how to create screenshots by reading github tutorials online. 
8. I started the extra credit independently and successfully wrote np.random.seed() and created 50 2x10 arrays
with normal Gaussian distributions across a new mean and new standard deviation. However, I was unable to plot 
the distributions without assistance. I did not know how to call the (X,Y) variables inside the array. Aaron 
assisted with this and explained his line of code "pl.plot(reprRandAll[i][0], reprRandAll[i][1])". This line
iterates through the 50 arrays (with i), calling the zero-ith and first elements inside each array for plotting. 
Aaron's plot has many extra features (like his color label variable, for example), which I didn't include in mine. 
For the challenge part of the extra credit, I made the mean random by calling np.random.randn().

Screenshots are here:

Screenshots from Compute

![alt tag](https://cloud.githubusercontent.com/assets/22032802/18398300/33dbab2e-769a-11e6-96da-50d3c25f6ad6.png)
![alt tag](https://cloud.githubusercontent.com/assets/22032802/18398304/3606e44a-769a-11e6-8182-d6d960972a69.png)
Screenshots from local machine

![alt tag](https://cloud.githubusercontent.com/assets/22032802/18439326/dd1a17f4-78d2-11e6-88ff-f87b5a0da3e0.png)
![alt tag](https://cloud.githubusercontent.com/assets/22032802/18439419/43aca7ca-78d3-11e6-9e4b-ca9c40a4e1c1.png)
