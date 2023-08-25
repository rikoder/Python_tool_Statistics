import tkinter as tk
import random
import matplotlib.pyplot as plt
import numpy as np
import statistics
import scipy
from scipy.stats import gaussian_kde

class DistributionGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Distribution Generator")
        self.geometry("300x500")
               
        # Distribution selection
        self.distribution_var = tk.StringVar()
        self.distribution_options = ["Uniform(sample size)", "Normal(mean, stddev, sample size)", "Exponential(Lambda, sample size)", "Log Normal(mean, stddev, sample size)", "Weibull(Scale, Shape, sample size)", "GEV(Location, Scale, Shape, sample size)"]
        self.distribution_var.set(self.distribution_options[0])
        self.distribution_menu = tk.OptionMenu(self, self.distribution_var, *self.distribution_options)
        self.distribution_menu.pack(pady=10)

        
        # Select button
        self.select_button = tk.Button(self, text="Select", command=self.select_parameters)
        self.select_button.pack(pady=10)


    def select_parameters(self):      
        # distribution = self.distribution_var.get()
        # Parameter inputs
        try:
            self.parameters_frame.destroy()
            self.outputs_frame.destroy()
        except:
            pass

        self.parameters_frame = tk.Frame(self)
        self.parameters_frame.pack()
        if self.distribution_var.get() == "Uniform(sample size)":
            self.a_label = tk.Label(self.parameters_frame, text="Lower Bound:")
            self.a_label.grid(row=0, column=0, padx=5, pady=5)
            self.a_entry = tk.Entry(self.parameters_frame)
            self.a_entry.grid(row=0, column=1, padx=5, pady=5)

            self.b_label = tk.Label(self.parameters_frame, text="Upper Bound:")
            self.b_label.grid(row=1, column=0, padx=5, pady=5)
            self.b_entry = tk.Entry(self.parameters_frame)
            self.b_entry.grid(row=1, column=1, padx=5, pady=5)

            self.sample_size_label = tk.Label(self.parameters_frame, text="Sample Size:")
            self.sample_size_label.grid(row=2, column=0, padx=5, pady=5)
            self.sample_size_entry = tk.Entry(self.parameters_frame)
            self.sample_size_entry.grid(row=2, column=1, padx=5, pady=5)     

            
        elif self.distribution_var.get() == "Normal(mean, stddev, sample size)":
            self.mean_label = tk.Label(self.parameters_frame, text="Mean:")
            self.mean_label.grid(row=0, column=0, padx=5, pady=5)
            self.mean_entry = tk.Entry(self.parameters_frame)
            self.mean_entry.grid(row=0, column=1, padx=5, pady=5)

            self.stddev_label = tk.Label(self.parameters_frame, text="Std Dev:")
            self.stddev_label.grid(row=1, column=0, padx=5, pady=5)
            self.stddev_entry = tk.Entry(self.parameters_frame)
            self.stddev_entry.grid(row=1, column=1, padx=5, pady=5)

            self.sample_size_label = tk.Label(self.parameters_frame, text="Sample Size:")
            self.sample_size_label.grid(row=2, column=0, padx=5, pady=5)
            self.sample_size_entry = tk.Entry(self.parameters_frame)
            self.sample_size_entry.grid(row=2, column=1, padx=5, pady=5)     


        elif self.distribution_var.get() == "Exponential(Lambda, sample size)":
            self.lambda_label = tk.Label(self.parameters_frame, text="Lambda:")
            self.lambda_label.grid(row=0, column=0, padx=5, pady=5)
            self.lambda_entry = tk.Entry(self.parameters_frame)
            self.lambda_entry.grid(row=0, column=1, padx=5, pady=5)

            self.sample_size_label = tk.Label(self.parameters_frame, text="Sample Size:")
            self.sample_size_label.grid(row=1, column=0, padx=5, pady=5)
            self.sample_size_entry = tk.Entry(self.parameters_frame)
            self.sample_size_entry.grid(row=1, column=1, padx=5, pady=5)     

            
        elif self.distribution_var.get() == "Log Normal(mean, stddev, sample size)":
            self.mean_label = tk.Label(self.parameters_frame, text="Mean:")
            self.mean_label.grid(row=0, column=0, padx=5, pady=5)
            self.mean_entry = tk.Entry(self.parameters_frame)
            self.mean_entry.grid(row=0, column=1, padx=5, pady=5)

            self.stddev_label = tk.Label(self.parameters_frame, text="Std Dev:")
            self.stddev_label.grid(row=1, column=0, padx=5, pady=5)
            self.stddev_entry = tk.Entry(self.parameters_frame)
            self.stddev_entry.grid(row=1, column=1, padx=5, pady=5)

            self.sample_size_label = tk.Label(self.parameters_frame, text="Sample Size:")
            self.sample_size_label.grid(row=2, column=0, padx=5, pady=5)
            self.sample_size_entry = tk.Entry(self.parameters_frame)
            self.sample_size_entry.grid(row=2, column=1, padx=5, pady=5)     

        elif self.distribution_var.get() == "Weibull(Scale, Shape, sample size)":
            self.c_label = tk.Label(self.parameters_frame, text="Scale(c/s):")
            self.c_label.grid(row=0, column=0, padx=5, pady=5)
            self.c_entry = tk.Entry(self.parameters_frame)
            self.c_entry.grid(row=0, column=1, padx=5, pady=5)

            self.k_label = tk.Label(self.parameters_frame, text="Shape(k):")
            self.k_label.grid(row=1, column=0, padx=5, pady=5)
            self.k_entry = tk.Entry(self.parameters_frame)
            self.k_entry.grid(row=1, column=1, padx=5, pady=5)

            self.sample_size_label = tk.Label(self.parameters_frame, text="Sample Size:")
            self.sample_size_label.grid(row=2, column=0, padx=5, pady=5)
            self.sample_size_entry = tk.Entry(self.parameters_frame)
            self.sample_size_entry.grid(row=2, column=1, padx=5, pady=5)     

        elif self.distribution_var.get() == "GEV(Location, Scale, Shape, sample size)":
            self.c_label = tk.Label(self.parameters_frame, text="Scale(c/s):")
            self.c_label.grid(row=0, column=0, padx=5, pady=5)
            self.c_entry = tk.Entry(self.parameters_frame)
            self.c_entry.grid(row=0, column=1, padx=5, pady=5)

            self.k_label = tk.Label(self.parameters_frame, text="Shape(k):")
            self.k_label.grid(row=1, column=0, padx=5, pady=5)
            self.k_entry = tk.Entry(self.parameters_frame)
            self.k_entry.grid(row=1, column=1, padx=5, pady=5)

            self.m_label = tk.Label(self.parameters_frame, text="Location(m):")
            self.m_label.grid(row=2, column=0, padx=5, pady=5)
            self.m_entry = tk.Entry(self.parameters_frame)
            self.m_entry.grid(row=2, column=1, padx=5, pady=5)


            # Sample size input
            self.sample_size_label = tk.Label(self.parameters_frame, text="Sample Size:")
            self.sample_size_label.grid(row=3, column=0, padx=5, pady=5)
            self.sample_size_entry = tk.Entry(self.parameters_frame)
            self.sample_size_entry.grid(row=3, column=1, padx=5, pady=5)

            
        #File name input to save generated sample
        self.file_name_label = tk.Label(self.parameters_frame, text="File name:")
        self.file_name_label.grid(row=4, column=0, padx=5, pady=5)
        self.file_name_entry = tk.Entry(self.parameters_frame)
        self.file_name_entry.grid(row=4, column=1, padx=5, pady=5)
            
        # Generate button
        self.generate_button = tk.Button(self.parameters_frame, text="Save sample and Generate", command=self.generate_distribution)
        self.generate_button.grid(row = 5, column = 1, padx = 5, pady=5)

        #self.reset_button = tk.Button(self.parameters_frame, text="Reset", command=self.parameters_frame.destroy)
        #self.reset_button.pack(pady=10)
        #self.reset_button.grid(row = 4, column = 1, padx = 5, pady=5)

    def generate_distribution(self):
        
        try:
            self.outputs_frame.destroy()
        except:
            pass
        
        distribution = self.distribution_var.get()

        if distribution == "Uniform(sample size)":
            self.plot_uniform()
        elif distribution == "Normal(mean, stddev, sample size)":
            self.plot_normal()
        elif distribution == "Exponential(Lambda, sample size)":
            self.plot_exponential()
        elif distribution == "Log Normal(mean, stddev, sample size)":
            self.plot_log_normal()
        elif distribution == "Weibull(Scale, Shape, sample size)":
            self.plot_weibull()
        elif distribution == "GEV(Location, Scale, Shape, sample size)":
            self.plot_gev()

    def output(self, sample_array):
        np_sample = np.array(sample_array)
        np_sample.tofile(str(self.file_name_entry.get()) + '.csv', sep = ',')
        self.outputs_frame = tk.Frame(self)
        self.outputs_frame.pack()
        self.mean_label = tk.Label(self.outputs_frame, text="Mean: " + str(np.mean(sample_array)))
        self.mean_label.grid(row=5, column=0, padx=5, pady=5)
        self.mean_label = tk.Label(self.outputs_frame, text="Standard Deviation: " + str(statistics.stdev(sample_array)))
        self.mean_label.grid(row=6, column=0, padx=5, pady=5)
        self.mean_label = tk.Label(self.outputs_frame, text="Skewness: " + str(scipy.stats.skew(sample_array)))
        self.mean_label.grid(row=7, column=0, padx=5, pady=5)
        self.mean_label = tk.Label(self.outputs_frame, text="Kurtosis: " + str(scipy.stats.kurtosis(sample_array)))
        self.mean_label.grid(row=8, column=0, padx=5, pady=5)

    def Plot(self, sample, title):
        #fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        plt.figure(figsize = (8,6))
        sorted_sample = np.sort(sample)
        '''
        kde = gaussian_kde(sample)
        x = np.linspace(min(sample), max(sample), 1000)
        y = kde(x)

        # Plot PDF
        plt.plot(x, y)'''
        plt.hist(sample, bins = min(50, len(sample)), alpha = 0.5, label = 'Uniform', edgecolor = 'black')
        plt.xlabel('Value')
        plt.ylabel('Probability Density')
        plt.title(title)

        # Plot cumulative distribution function
        y_vals = np.arange(len(sorted_sample)) / float(len(sorted_sample) - 1)
        ax2 = plt.twinx()
        ax2.plot(sorted_sample, y_vals, color = 'red')
        ax2.set_xlabel('Value')
        ax2.set_ylabel('Cumulative Probability')

        plt.tight_layout()
        plt.show()

    def plot_uniform(self):
        def Uniform_Distribution_Sample_Generator(a,b):
            return a + (b-a)*random.random()
        a = float(self.a_entry.get())
        b = float(self.b_entry.get())
        sample_size = int(self.sample_size_entry.get())
        uniform_sample = []
        for i in range(sample_size):
            uniform_sample.append(Uniform_Distribution_Sample_Generator(a,b))
            
        self.output(uniform_sample)

        self.Plot(uniform_sample, 'Uniform Distribution')

    def plot_normal(self):
        mean = float(self.mean_entry.get())
        stddev = float(self.stddev_entry.get())
        sample_size = int(self.sample_size_entry.get())
        def Normal_Distribution_Sample_Generator(mean, stddev):
            u1 = random.random()
            u2 = random.random()
            z1 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2) 
            z2 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)
            z1 = z1 * stddev + mean
            z2 = z2 * stddev + mean
            return z1, z2
        Normal_sample = []
        for i in range(sample_size):
          z1,z2 = Normal_Distribution_Sample_Generator(mean, stddev)
          Normal_sample.append(z1)
          Normal_sample.append(z2)

        self.output(Normal_sample)
        self.Plot(Normal_sample, 'Normal Distribution')

    def plot_exponential(self):
        lambda_ = float(self.lambda_entry.get())
        sample_size = int(self.sample_size_entry.get())

        def Exponential_Distribution_Sample_Generator(lambda_):
          return (-1/lambda_) * np.log(random.random())

        Exponential_sample = []

        for i in range(sample_size):
          Exponential_sample.append(Exponential_Distribution_Sample_Generator(lambda_))

        self.output(Exponential_sample)
        self.Plot(Exponential_sample, 'Exponential Distribution')

    def plot_log_normal(self):
        mean = float(self.mean_entry.get())
        stddev = float(self.stddev_entry.get())
        sample_size = int(self.sample_size_entry.get())
        def Normal_Distribution_Sample_Generator(mean, stddev):
            u1 = random.random()
            u2 = random.random()
            z1 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2) 
            z2 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)
            z1 = z1 * stddev + mean
            z2 = z2 * stddev + mean
            return z1, z2

        def Log_Normal_Distribution_Sample_Generator(mean, stddev):
          z1,z2 = Normal_Distribution_Sample_Generator(mean, stddev)
          return np.exp(z1), np.exp(z2)

        Log_Normal_sample = []

        for i in range(sample_size):
          z1,z2 = Log_Normal_Distribution_Sample_Generator(mean, stddev)
          Log_Normal_sample.append(z1)
          Log_Normal_sample.append(z2)

        self.output(Log_Normal_sample)
        self.Plot(Log_Normal_sample, 'Log Normal Distribution')

    def plot_weibull(self):
        c = float(self.c_entry.get()) #Scale parameter
        k = float(self.k_entry.get()) #Shape parameter
        sample_size = int(self.sample_size_entry.get())

        def Weibull_Distribution_Sample_Generator(c,k):
          return c*((-1 * np.log(random.random()))**(1/k))

        Weibull_sample = []

        for i in range(sample_size):
          Weibull_sample.append(Weibull_Distribution_Sample_Generator(c,k))

        self.output(Weibull_sample)
        self.Plot(Weibull_sample, 'Weibull Distribution')

    def plot_gev(self):
        m = float(self.m_entry.get()) #Location parameter
        s = float(self.c_entry.get()) # Scale parameter
        k = float(self.k_entry.get()) #Shape parameter
        sample_size = int(self.sample_size_entry.get())
        def GEV_Distribution_Sample_Generator(m,s,k):
          if k != 0:
            return (m - s/k) + (s/k)*(-1*np.log(random.random()))**(-1*k)
          else:
            return m - s*np.log(random.random())

        GEV_sample = []  

        for i in range(sample_size):
          GEV_sample.append(GEV_Distribution_Sample_Generator(m,s,k))

        self.output(GEV_sample)
        self.Plot(GEV_sample, 'Generalized Extreme Value Distribution')

if __name__ == "__main__":
    app = DistributionGUI()
    app.mainloop()
