import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import pickle

# Load the data we'd like to plot
pickle_filename = '../pickles/1e6_results.pickle'
pickle_file = open(pickle_filename, 'rb')
data = pickle.load(pickle_file)
pickle_file.close()

# Fit the data to a gamma distribution
fit_alpha_gamma, fit_loc_gamma, fit_scale_gamma = \
    stats.gamma.fit(data)
fit_shape_invgauss, fit_loc_invgauss, fit_scale_invguass = \
    stats.invgauss.fit(data)

# Graphical parameters
method = "Exclude Indeterminates"
color1 = "#8D99AE"
color2 = "#6320EE"
color3 = "#CA1551"

# Create the visualization
sns.histplot(
    data=data,
    stat="density",
    binwidth=25,
    color=color1
    )

base = range(2500)
gamma_model = [stats.gamma.pdf(x,
                               fit_alpha_gamma,
                               fit_loc_gamma,
                               fit_scale_gamma) for x in base]
plt.plot(base,
         gamma_model,
         lw=2,
         ls='--',
         color=color2,
         label="Gamma Distribution")

invgauss_model = [stats.invgauss.pdf(x,
                                     fit_shape_invgauss,
                                     fit_loc_invgauss,
                                     fit_scale_invguass) for x in base]
plt.plot(base,
         invgauss_model,
         lw=2,
         ls='--',
         color=color3,
         label="Inverse Gauss Distribution")

fontsize = 16
plt.xlim(0,2500)
plt.xlabel("Number of Flips", size=fontsize)
plt.ylabel("Probability", size=fontsize)
plt.title("Method: {method}".format(method=method))
plt.legend(loc="upper right",
           prop={'size': fontsize-2},
           frameon=False)
plt.yticks([])
plt.tight_layout()

# Show or save the visualization
#plt.show()
plt.savefig("{method}.png".format(method=method).replace(" ","_"),
            dpi=250)