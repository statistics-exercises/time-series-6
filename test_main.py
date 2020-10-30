import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_percentiles(self) : 
        self.assertTrue( percentile25 == np.percentile(samples,25), "you have calculated the 25th percentile wrongly" )
        self.assertTrue( median == np.percentile(samples,50), "you have calculated the median wrongly" )
        self.assertTrue( percentile75 == np.percentile(samples,75), "you have calculated the 75th percentile wrongly" )
        
    def test_samplemean(self) : 
        mean=0
        for i in range(100) : mean = mean + samplemean(20,4,5)
        mean = mean / 100

        pp = 4 / (4+5)
        bar = np.sqrt(pp*(1-pp)/20/100)*st.norm.ppf( (0.99 + 1) / 2 )
        self.assertTrue( np.fabs( mean - pp )<bar, "your function for computing the sample mean does not appear to be working" )
        
    def test_firstevent(self) : 
        mean=0
        for i in range(100) : mean = mean + firstevent(4,5)
        mean = mean / 100

        pp = 4 / (4+5)
        bar = np.sqrt(pp*(1-pp)/100)*st.norm.ppf( (0.99 + 1) / 2 )
        self.assertTrue( np.fabs( mean - pp )<bar, "your function firstevent does not appear to be working" )
        
    def test_exponential(self) : 
        lam,mean=2,0
        for i in range(100) : mean = mean + exponential(lam)
        mean = mean / 100

        bar = np.sqrt(1/(lam*lam)/100)*st.norm.ppf( (0.99 + 1) / 2 )
        self.assertTrue( np.fabs( mean - 1/lam )<bar, "your function for generating exponential random variables does not appear to be working" )
