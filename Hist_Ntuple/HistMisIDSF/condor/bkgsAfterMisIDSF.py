from ROOT import TFile, TH1F, gDirectory
import os
import sys
sys.path.insert(0, os.getcwd().replace("condor", ""))
from HistInputs import *
import numpy
import itertools
import json
from optparse import OptionParser

#-----------------------------------------
#INPUT command-line arguments 
#----------------------------------------
parser = OptionParser()
parser.add_option("-y", "--year", dest="year", default="2016",type='str',
                     help="Specify the year of the data taking" )
parser.add_option("-d", "--decayMode", dest="decayMode", default="Semilep",type='str',
                     help="Specify which decayMode moded of ttbar Semilep or ? default is Semilep")
parser.add_option("-c", "--channel", dest="channel", default="Ele",type='str',
		  help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("--hist", "--hist", dest="inHistName", default="Reco_mass_lgamma",type='str',
		  help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("--cr", "--CR", dest="CR", default="MisID_Enriched_a2j_e0b_e1y",type='str', 
                     help="which control selection and region")
(options, args) = parser.parse_args()
year            = options.year
decayMode       = options.decayMode
channel         = options.channel
inHistName      = options.inHistName
CR              = options.CR

#-----------------------------------------
#Path of the I/O histograms/datacards
#----------------------------------------
inDir = "%s/%s/%s/%s/Merged"%(condorHistDir, year, decayMode, channel)
inFile = TFile.Open("%s/AllInc.root"%inDir, "read")
outDir = inDir.replace("Raw", "afterMisIDSF")
if not os.path.exists(outDir):
    os.system("mkdir -p %s"%outDir)
outputFile = TFile("%s/AllInc.root"%outDir,"update")
print inFile
#-----------------------------------------
#Functions to read/write histograms
#----------------------------------------
if "le" in channel:
    newBins = numpy.array([0,80,84,88,92,96,100,180.])
else:
    newBins = numpy.array([0,90,180.])
dySF   = 1.2 

path = "/uscms_data/d3/rverma/codes/CMSSW_10_2_13/src/TopRunII/cms-TT-run2/Fit_Hist/FitMisIDSF/"
with open ("%s/RateParams.json"%path) as jsonFile:
    jsonData = json.load(jsonFile)

def getRateParam(name, proc):
    paramDicts   = jsonData[name]
    rateParam = 1.0
    for paramDict in paramDicts:
        for key, val in paramDict.iteritems():
            if proc==key:
                rateParam = val
    return rateParam
name  = "RP_%s_%s_%s_%s_%s"%(year, decayMode, channel, CR, inHistName)
misIDSF   = getRateParam(name,"r")
print misIDSF

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

def getHistDir(sample, sysType, CR):
    histDir = "%s/%s/%s"%(sample, CR, sysType)
    return histDir

def writeHist(hist, procDir, histNewName, outputFile):
    outHistDir = getHistDir(procDir, inHistName, CR)
    if not outputFile.GetDirectory(outHistDir):
        outputFile.mkdir(outHistDir)
    outputFile.cd(outHistDir)
    gDirectory.Delete("%s;*"%(hist.GetName()))
    print "%20s, %15s, %10s, %10s"%(inHistName, procDir, histNewName, round(hist.Integral()))
    hNew = hist.Rebin(len(newBins)-1, histNewName, newBins) 
    hNew.Write()
    #hist.Write()

def getHistData(inHistName, procDir, sysType):
    histDir = getHistDir(procDir, sysType, CR)
    #print "Hist: %s/%s"%(histDir, inHistName)
    hist = inFile.Get("%s/%s"%(histDir, inHistName)).Clone(sysType)
    return hist, procDir, sysType

#-----------------------------------------
#Functions for misID 
#----------------------------------------
def getHistMisID(inHistName, procDir, sysType):
    hList = []
    sysType_ = sysType
    for sample in Samples:
        if "TT_tytg" not in sample and "Data" not in sample:
            if "QCD" in sample:
                sample = "QCD"
            histDir = getHistDir(sample, sysType, CR)
            h = inFile.Get("%s/%s_misid_ele"%(histDir, inHistName))
            if "DYJets" in sample:
                h.Scale(dySF)
            h.Scale(misIDSF)
            hList.append(h)
    return addHist(hList, sysType), procDir, sysType_


def getHistOther(inHistName, procDir, sysType):
    hList = []
    sysType_ = sysType
    for sample in Samples:
        if "TT_tytg" not in sample and "Data" not in sample:
            if "QCD" in sample:
                sample = "QCD"
            histDir = getHistDir(sample, sysType, CR)
            h1 = inFile.Get("%s/%s_genuine"%(histDir, inHistName))
            h2 = inFile.Get("%s/%s_hadronic_photon"%(histDir, inHistName))
            h3 = inFile.Get("%s/%s_hadronic_fake"%(histDir, inHistName))
            if "DYJets" in sample:
                h1.Scale(dySF)
                h2.Scale(dySF)
                h3.Scale(dySF)
            hList.append(h1)
            hList.append(h2)
            hList.append(h3)
    return addHist(hList, sysType), procDir, sysType_

#-----------------------------------------
#Categorise hists here
#----------------------------------------
allSysType = []
allSysType.append("Base")
for syst, level in itertools.product(Systematics, SystLevels):
    sysType = "%s%s"%(syst, level)
    allSysType.append(sysType)
writeList = []
for sysType in allSysType:
#for sysType in ["Base"]: 
    writeList.append(getHistData(inHistName, "data_obs", "Base"))
    writeList.append(getHistMisID(inHistName,  "MisIDEle",  sysType))
    writeList.append(getHistOther(inHistName, "OtherPhotons", sysType))
    # signal sample for plotting purpose
    writeList.append(getHistData(inHistName,  "TT_tytg_M800",   sysType))
    writeList.append(getHistData(inHistName,  "TT_tytg_M1200",  sysType))
    writeList.append(getHistData(inHistName,  "TT_tytg_M1600",  sysType))
for write in writeList:
    writeHist(write[0], write[1], write[2], outputFile)
outputFile.Close()
print outDir
