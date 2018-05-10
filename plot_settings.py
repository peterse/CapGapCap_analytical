import matplotlib as mpl


# see https://matplotlib.org/users/customizing.html
mpl.rcParams["lines.linewidth"] = 3

# Fontsizes
mpl.rcParams["axes.labelsize"] = 28
mpl.rcParams["xtick.labelsize"] = 24
mpl.rcParams["ytick.labelsize"] = 24
mpl.rcParams["axes.titlesize"] =  28
mpl.rcParams["legend.fontsize"] = 28

# Grid settings
mpl.rcParams['grid.color'] = 'k'
mpl.rcParams['grid.linestyle'] = '-'
mpl.rcParams['grid.linewidth'] = 0.5

# automatic figure resizing
#mpl.rcParams['figure.autolayout'] = True

# Enable LaTeX
mpl.rcParams['text.usetex'] = True

FIG_DIR = "C:\\Users\\e6peters\\Dropbox\\DQM_Projects\\QIP_research\\Qubit_research\\CapCap\\CapGapCap_writeup\\DQMLab_Articles_CapGapCap\\Figures\\"