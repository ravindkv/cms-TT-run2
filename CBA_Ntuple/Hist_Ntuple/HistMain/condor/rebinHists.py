import os
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.getcwd().replace("condor", ""))
import numpy
import itertools
from HistInputs import *
from optparse import OptionParser
from HistInfo import GetHistogramInfo
from ROOT import TFile, TH1F, gDirectory

#----------------------------------------
#INPUT Command Line Arguments 
#----------------------------------------
parser = OptionParser()
parser.add_option("--isCheck","--isCheck", dest="isCheck",action="store_true",default=False, help="Merge for combined years and channels")
parser.add_option("--isSep","--isSep", dest="isSep",action="store_true",default=False, help="Merge for separate years and channels")
parser.add_option("--isComb","--isComb", dest="isMerge",action="store_true",default=False, help="Merge for combined years and channels")
(options, args) = parser.parse_args()
isCheck = options.isCheck
isSep = options.isSep
isComb = options.isMerge

if isCheck:
    isSep  = True
    isComb = False
    Years  = [Years[0]]
    Decays = [Decays[0]]
    Channels = [Channels[0]]
    Samples = [Samples[0]]
if isSep: 
    isComb = False
if isComb:
    isSep = False
    Years = Years_
    Channels = Channels_
if not isCheck and not isSep and not isComb:
    print("Add either --isCheck or --isSep or --isComb in the command line")
    exit()

hists = GetHistogramInfo()
dictRebin = {}
dictRebin["Reco_mass_T"] = numpy.array([0,200,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1800.,2500.,6000.])
dictRebin["Photon_et"]   = numpy.array([0,100,200,300,400,500,600,700,900,1200,2000.])
dictRebin["Reco_ht"]     = numpy.array([0,500,700,900,1100,1300,1500,1700,1900,2200,2500,3000,5000,9000.])
dictRebin["Reco_st"]     = numpy.array([0,500,700,900,1100,1300,1500,1700,1900,2200,2500,3000,5000,9000.])

#-----------------------------------------
#Functions to read/write histograms
#----------------------------------------
def addHist(histList, name):
    if len(histList) ==0:
        print "Hist list | %s, %s | is empty"%(histList, name)
        sys.exit()
    else:
        hist = histList[0].Clone(name)
        hist.Reset()
        for h in histList:
            hist.Add(h)
        return hist

def getHistDir(sample, CR, sysType):
    histDir = "%s/%s/%s"%(sample, CR, sysType)
    return histDir

def writeHist(sample, CR, sysType, hist_, outputFile):
    outHistDir = getHistDir(sample, CR, sysType)
    if not outputFile.GetDirectory(outHistDir):
        outputFile.mkdir(outHistDir)
    #print gDirectory.ls()
    outputFile.cd(outHistDir)
    hName = hist_.GetName()
    gDirectory.Delete("%s;*"%(hName))
    #print "%10s :/%s/%s/%s/%s"%(round(hist_.Integral(), 1), sample, CR, sysType, hist_.GetName()) 
    if hName in dictRebin.keys():
        hNew = hist_.Rebin(len(dictRebin[hName])-1, hist_.GetName(), dictRebin[hName]) 
        hNew.Write()
    else:
        hist_.Write()
    outputFile.cd()

#-----------------------------------------
# Collect all syst 
#----------------------------------------
allSysType = []
for syst, level in itertools.product(Systematics, SystLevels):
    sysType = "%s_%s"%(syst, level)
    if syst in ["Weight_lumi", "1"] and level in ["up", "down"]:
        continue
    allSysType.append(sysType)

#-----------------------------------------
# Do the rebining here
#----------------------------------------
for year, decay, channel in itertools.product(Years, Decays, Channels):
    inDir = "%s/Merged/%s/%s/%s"%(outHistDir, year, decay, channel)
    inFile = TFile.Open("root://cmseos.fnal.gov/%s/AllInc.root"%inDir, "read")
    outDir = inDir.replace("Merged", "Rebin")
    os.system("eos root://cmseos.fnal.gov mkdir -p %s"%outDir)
    outputFile = TFile("/eos/uscms/%s/AllInc.root"%outDir,"update")
    print("==> %s, %s, %s"%(year, decay, channel))
    for s, r, sys, h in itertools.product(Samples, Regions.keys(), allSysType, hists.keys()):
        if isCheck:
            print("%s, %s, %s, %s"%(s, r, sys, h))
        histDir = getHistDir(s, r, sys)
        h4 = inFile.Get("%s/%s"%(histDir, h))
        writeHist(s, r, sys, h4, outputFile)
    outputFile.Close()
    print "/eos/uscms/%s/AllInc.root\n"%outDir
