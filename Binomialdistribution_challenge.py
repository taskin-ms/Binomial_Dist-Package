
import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution


class Binomial(Distribution):
    
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
                
    """
   
   
   
    def __init__(self, prob = 0.5, size = 25 ):
        
        
        
        
        self.p = prob
        self.n = size
        
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
        
        
    def calculate_mean(self):
     
    
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        
        self.mean = self.p*self.n
        return self.mean
        
         

   
    def calculate_stdev(self):
        

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        
        self.stdev = math.sqrt(self.n * self.p * (1-self.p))
        return self.stdev
    
    
    def replace_stats_with_data(self): 


        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """
        self.n = len(self.data)
        positive = []
        for data in self.data:
            if data != 0:
                positive.append(data)
        
        self.p = len(positive) / len(self.data)
        
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        
        return self.p, self.n
        
        
        
    
   
    def plot_bar(self):
        
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        plt.bar(x = ['0', '1'], height = [(1 - self.p) * self.n, self.p * self.n])
        plt.title("Bar Graph Of Data")
        plt.xlabel("Data")
        plt.ylabel("Count")
        
        plt.show()
        
    
    
    def pdf(self, k):
        
        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        return ( math.factorial(self.n) / (math.factorial(k) *( math.factorial(self.n-k)) ) )* (self.p ** k) * ( (1 - self.p) ** (self.n - k) )
        


    def plot_prob_dens(self):
        

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
    
     
        x = []
        y = []
        
        for num in range(0, self.n + 1):
            x.append(num)
            y.append(self.pdf(num))
        
        plt.bar(x, y)
        plt.title("Probablity Distribution of Outcomes")
        plt.xlabel("Outcome")
        plt.ylabel("Probablity")
        
        return x
        return y
                
    
    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
        
        result = Binomial()
        
        result.n = self.n + other.n
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()
        
        
        return result
        
                        
   
    def __repr__(self):
        
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
        
    
        return "mean {}, standard deviation {}, p {}, n {}".format(self.mean, self.stdev, self.p, self.n)
