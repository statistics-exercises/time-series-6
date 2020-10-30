# Averaging for Alice and Bob

Now that we can simulate which of the the two events occurs first we can now use what we have learned to simulate the problem; namely:

_Bob is waiting to catch a bus at the bus stop.  Alice, meanwhile, is in the library.  If the time Alice spends in the library is an exponentially distributed random variable with parameter 5 and the time it takes a bus to arrive is an exponentially distributed random variable with parameter 4 what is the probability that Alice meets Bob at the bus stop._

To answer this problem by simulation we simply generate multiple samples from the statistical distribution that is described in the question and compute an average.  Furthermore, this is what we do whenever we solve a problem by statistical simulation.  We simply sample from the same distribution multiple times and compute a sample mean.  The distributions we are sampling from get more complicated but the algorithm that we are using doesn't get much more complicated than the process of repeated sampling and calculating a sample mean that we have now done countless times during this course. 

With that in mind you therefore need to do the following to complete this exercise:

1. Write a function called `exponential` that takes a parameter called `lam`.  This function should return an exponential random variable from a distribution with the parameter equal to `lam`.
2. Write a second function called `firstevent` that generates two exponential random variables that give the arrival time of Alice and the Bus.  Your function should return a 1 if Alice meets Bob at the bus stop and a zero otherwise.  The function arguments `lam1` and `lam2` are the parameters for the two exponential random variables that appear in this problem.
3. Write a function called `samplemean` that takes in three parameters.  `n` is the number of samples to take when computing the sample mean, `lam1` is the parameter of the exponential random variable that determines Alice's arrival time and `lam2` is the parameter of the exponential random variable that determines thus busses arrival time.  The function called `samplemean` should return a sample mean that is computed by calling the function called `firstevent` `n` times.
4. Resample the distribution for the random variable computed by the function `samplemean` 20 times and store the 20 values for this random variable that you obtain in a list called `samples`.
5. Calculate the `median`, the 25th and 75th percentile of the data in the list called `samples` and store the values of these quantities in the variables called `median`, `percentile25` and `percentile75` respectively. 

Notice that the random variable sampled by the function `firstevent` is a random variable that takes a value of 1 with a certain fixed probability p.  In other words, we can think of this function as one that is just sampling a Bernoulli random variable.
 
