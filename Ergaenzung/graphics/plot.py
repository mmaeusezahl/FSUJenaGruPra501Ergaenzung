import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.preamble'] = r'\usepackage[sfdefault]{roboto}\renewcommand{\familydefault}{\sfdefault}'

fig = plt.figure('501 Sketch', figsize=(3.149,2.5))
plt.clf()
ax  = fig.add_subplot(111) 

a,n =7.6, 2.75

sample_x = np.linspace(50,80)
f = lambda l : np.exp(-a*np.power(l/100,n))

ax.plot(sample_x, f(sample_x), color='black')
ax.set_xlim(50,80)
ax.set_ylim(0,None)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.minorticks_on()
ax.set_xlabel('$\lambda/\mathrm{pm}$')
ax.set_ylabel('$T$', rotation='horizontal')
ax.yaxis.set_label_coords(-0.04,1.02)

l1 = 62
f1 = f(l1)
l2 = 68
f2 = f(l2)

ax.plot([50,l1,l1],[f1,f1,0], color='black', ls='--', lw=1)
ax.plot([50,l2,l2],[f2,f2,0], color='black', ls='--', lw=1)

ax.text(0.30, 0.65,r'$T(\lambda)\approx e^{-7{,}6\left(\frac{\lambda}{100\,\mathrm{\sf pm}}\right)^{2{,}75}}$',
        horizontalalignment='left',verticalalignment='bottom', transform=ax.transAxes)

ax.text((l1+l2)/2, -0.02,r'$\Delta\lambda$',
        horizontalalignment='center',verticalalignment='top', transform=ax.transData)

ax.text(51, f1,r'$T_1$',
        horizontalalignment='left',verticalalignment='center', transform=ax.transData,
        bbox=dict(color='white'))

ax.text(51, f2,r'$T_2$',
        horizontalalignment='left',verticalalignment='center', transform=ax.transData,
        bbox=dict(color='white'))

an = ax.annotate("", xy=(l1, 0.02), xytext=(l2, 0.02), arrowprops=dict(arrowstyle="<->"),
            xycoords='data',
            textcoords='data',)

fig.tight_layout()
fig.savefig('plot.pdf')