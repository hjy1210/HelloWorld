import numpy as np
from matplotlib import pyplot as plt

# Complete the following to make the plot
if __name__ == "__main__":
    data = np.load('sdss_galaxy_colors.npy')
    # Get a colour map
    cmap = plt.get_cmap('YlOrRd')

    # Define our colour indexes u-g and r-i
    ug=data['u']-data['g']
    ri=data['r']-data['i']
    # Make a redshift array
    redshift=data['redshift']
    # Create the plot with plt.scatter and plt.colorbar
    plt.scatter(ug,ri,lw=0.01,s=1,c=redshift,cmap=cmap)
    plt.colorbar().set_label('Redshift')
    # Define your axis labels and plot title
    plt.xlabel('Colour index u-g')
    plt.ylabel('Colour index r-i')
    #plt.clabel('Redshift')
    plt.title('Redshift (colour) u-g versus r-i')
    # Set any axis limits
    plt.xlim(-0.5,2.5)
    plt.ylim(-0.5,1)
    plt.show()