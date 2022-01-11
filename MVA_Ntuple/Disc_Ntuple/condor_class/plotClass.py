import os
import sys
import itertools
import collections
sys.path.insert(0, os.getcwd().replace("condor_class", ""))
from DiscInputs import *
from VarInfo import GetVarInfo
from optparse import OptionParser
import numpy as np

#-----------------------------------------
#INPUT command-line arguments 
#----------------------------------------
parser = OptionParser()
parser.add_option("--isMerge","--isMerge", dest="isMerge",action="store_true",default=False,
                     help="merge plots from inclusive and photon categories" )
parser.add_option("--isRun2","--isRun2", dest="isRun2",action="store_true",default=False,
                     help="plot/table for full Run2" )
parser.add_option("--isMake","--isMake", dest="isMake",action="store_true",default=False,
                     help="plot/table for full Run2" )
parser.add_option("--forRebin","--forRebin", dest="forRebin",action="store_true",default=False,
                     help="plot/table for full Run2" )
parser.add_option("--forMain","--forMain", dest="forMain",action="store_true",default=False,
                     help="plot/table for full Run2" )
(options, args) = parser.parse_args()
isMerge         = options.isMerge
isRun2          = options.isRun2
isMake          = options.isMake
forRebin          = options.forRebin
forMain          = options.forMain

merge = [""]
if forRebin:
    merge = ["Rebin"]
if forMain:
    merge = ["forMain"]
if forRebin and forMain:
    merge = ["Rebin", "forMain"]

ext = merge[0]
Year_ = Years

if isRun2:
    Year_ = ["Run2"]
    ext += "Run2"
    if isMerge:
        ext += "Merged"

if isMerge:
    merge = ["", "Cat"]
    ext += "Merged"
os.system("mkdir -p tex")
texFile = open("tex/plotClass%s.tex"%ext, "w")

#texFile.write("\documentclass{article}\n")
#texFile.write("\usepackage{graphicx}\n")
#texFile.write("\usepackage{subfigure}\n")
#texFile.write("\\begin{document}\n")
allPlotPath = []
allPlotName = []
histList = GetVarInfo().keys()
for r, d, c, y, method in itertools.product(Regions.keys(), Decays, Channels, Year_, methodDict.keys()):
    plotDir  = "/eos/uscms/%s/Classification/%s/%s/%s/CombMass/%s/%s/plots"%(condorOutDir, y, d, c, method, r)
    nVarPlots = len(histList)/6 + len(histList)%6
    '''
    for i in range(nVarPlots):
        allPlotPath.append("%s/variables_id_c%s.png"%(plotDir, i+1))
    allPlotPath.append("%s/mva_%s.png"%(plotDir, method))
    allPlotPath.append("%s/rejBvsS.png"%(plotDir))
    allPlotPath.append("%s/CorrelationMatrixB.png"%(plotDir))
    '''
    allPlotPath.append("%s/overtrain_%s.png"%(plotDir, method))
    allPlotName.append("%s, %s, %s, %s"%(y, c, r.replace("_", "\_"), method))

figWidth = 0.38
showPerFig = 12
if isRun2:
    figWidth=0.24
    showPerFig = 24
nPage = len(allPlotPath)/showPerFig
remainder = len(allPlotPath)%showPerFig
if remainder != 0:
    nPage = nPage +1
for page in np.arange(nPage):
    texFile.write("\\begin{figure}\n")
    texFile.write("\centering\n")
    showPerPage = showPerFig
    if remainder != 0:
        if page == nPage -1:
            showPerPage = remainder
    #Plots
    for n in np.arange(showPerPage):
        plotPath = allPlotPath[showPerFig*page + n]
        if showPerPage==2:
            figWidth = 0.45
        if showPerPage==1:
            figWidth = 0.95
        texFile.write("\includegraphics[width=%s\linewidth]{%s}\n"%(figWidth, plotPath))
    plotNames = "PLOT" 
    texFile.write("\caption{Distribution for: $%s$}\n"%allPlotName[page])
    texFile.write("\end{figure}\n")
    texFile.write("\n")
#texFile.write("\end{document}")