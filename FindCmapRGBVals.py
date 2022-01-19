# CreditL https://stackoverflow.com/questions/33596491/extract-matplotlib-colormap-in-hex-format#:~:text=You%20can%20get%20a%20tuple%20of%20rgba%20values,wrote%20in%20the%20comments%2C%20you%20can%20use%20matplotlib.colors.rgb2hex.

from pylab import *

cmap_name = 'Blues'

cmap = cm.get_cmap(cmap_name, 5)    # PiYG

for i in range(cmap.N):
    rgba = cmap(i)
    # rgb2hex accepts rgb or rgba
    print(matplotlib.colors.rgb2hex(rgba))
