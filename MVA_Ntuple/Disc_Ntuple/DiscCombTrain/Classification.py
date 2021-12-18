import ROOT

import os
import sys
sys.path.insert(0, "%s/%s"%(os.getcwd(), "sample"))
from SampleInfo import getSamples
from DiscInputs import *
from VarInfo import GetVarInfo

#-----------------------------------------
#INPUT Command Line Arguments 
#----------------------------------------
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-y", "--year", dest="year", default="2016",type='str',
                     help="Specifyi the year of the data taking" )
parser.add_option("-d", "--decay", dest="decayMode", default="Semilep",type='str',
                     help="Specify which decay moded of ttbar Semilep or Dilep? default is Semilep")
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
                     help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("-r", "--region", dest="region", default="ttyg_Enriched_SR",type='str', 
                     help="which control selection and region"), 
parser.add_option("--level", "--level", dest="level", default="",type='str',
                     help="Specify up/down of systematic")
parser.add_option("--syst", "--systematic", dest="systematic", default="JetBase",type='str',
                     help="Specify which systematic to run on")
parser.add_option("--method", "--method", dest="methodMVA", default="BDTP",type='str', 
                     help="Which MVA method to be used")
parser.add_option("--isCheck", "--isCheck", dest="isCheck", action="store_true", default=False, help="")
(options, args) = parser.parse_args()
year = options.year
decayMode = options.decayMode
channel = options.channel
region = options.region
syst = options.systematic
level =options.level
method = options.methodMVA
isCheck = options.isCheck
print parser.parse_args()

#-----------------------------------------
#INPUT AnalysisNtuples Directory
#----------------------------------------
package = "TMVA"
dirNtuple = "root://cmseos.fnal.gov//store/user/rverma/Output/cms-TT-run2/Ntuple_Skim/"
dirFile = "%s/%s/%s"%(year, decayMode, syst) 
allSamples = getSamples(year, decayMode, syst)

sigList = []
bkgList = []
for s in allSamples.keys():
    if 'TT_tytg' in s:
        sigs = allSamples[s]
        for sigF in sigs:
            sigList.append(sigF)
    else:
        if "Data" not in s:
            bkgs = allSamples[s]
            print("%s, files: %s"%(s, len(bkgs)))
            for bkgF in bkgs:
                bkgList.append(bkgF)
if isCheck:
    bkgList = ["Semilep_JetBase__TTGamma_SingleLept_2016_Ntuple.root"]

sig = ROOT.TChain("AnalysisTree")
for s in sigList:
    sig.Add("%s/%s/%s"%(dirNtuple, dirFile, s))
bkg = ROOT.TChain("AnalysisTree")
for b in bkgList:
    bkg.Add("%s/%s/%s"%(dirNtuple, dirFile, b))
print(sigList)
print("Total files from all bkgs = %s, Entries = %s "%(len(bkgList), bkg.GetEntries()))
print("Total files from all sigs = %s, Entries = %s "%(len(sigList), sig.GetEntries()))


loader = ROOT.TMVA.DataLoader("dataset")
os.system("mkdir -p dataset/plots")
sigWeight = 1.0
bkgWeight = 1.0
loader.AddSignalTree(sig, sigWeight)
loader.AddBackgroundTree(bkg, bkgWeight)

varDict = GetVarInfo()
print("\nTotal vars = %s \n"%len(varDict.keys()))
for var in varDict.keys():
    print(varDict[var][0])
    loader.AddVariable(varDict[var][0], 'F')

loader.SetSignalWeightExpression("Weight_lumi")
loader.SetBackgroundWeightExpression("Weight_lumi")

#evtSel = ROOT.TCut("pt_j1 > 50")
if "u" in channel: 
    evtSel = ROOT.TCut("Event_pass_presel_mu && %s"%Regions[region])
else:
    evtSel = ROOT.TCut("Event_pass_presel_ele && %s"%Regions[region])
loader.PrepareTrainingAndTestTree(evtSel,"SplitMode=Random:!V")

m = method
print("Method: %s"%m)
ROOT.TMVA.Tools.Instance()
## For PYMVA methods
ROOT.TMVA.PyMethodBase.PyInitialize()
outputFile = ROOT.TFile.Open("%s_Classification.root"%(package), "RECREATE")
factory = ROOT.TMVA.Factory("%s_Classification"%(package), outputFile,
                      "!V:ROC:!Silent:Color:!DrawProgressBar:AnalysisType=Classification" )
factory.BookMethod(loader, methodList[m][0], m, methodList[m][1])
factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()

ROOT.gROOT.SetBatch(True)
roc = factory.GetROCCurve(loader)
roc.Write()
auc = factory.GetROCIntegral(loader, m)
auc_ = "Year = %s\nDecay = %s\nChannel = %s\nRegion = %s\nMethod = %s\nAUC = %s"%(year, decayMode, channel, region, m, auc)
print("RESULT:%s,%s,%s,%s,%s,%s"%(year, decayMode, channel, region, m, auc))
aucFile = open("AUC.txt", "w")
aucFile.write(auc_)
aucFile.close()
outputFile.Close()
