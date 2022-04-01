#
# plot file creation
#

import matplotlib.pyplot as plt

plt.plot(range(10))
plt.show()

plt.savefig('pgn_plot.png')
plt.savefig('pdf_plot.pdf')
plt.savefig('jpg_plot.jpg')
plt.savefig('eps_plot.eps')
