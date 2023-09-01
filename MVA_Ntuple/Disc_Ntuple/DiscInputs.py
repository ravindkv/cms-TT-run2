import ROOT
import itertools
#-----------------------------------------------------------------
#dirNtuple = "/store/user/rverma/Output/cms-TT-run2/Ntuple_Skim"
dirNtuple = "/store/user/lpctop/Output/cms-TT-run2/Ntuple_Skim"
dirMVA    = "/store/user/rverma/Output/cms-TT-run2/MVA_Ntuple/"
dirClass  = "%s/Disc_Ntuple/DiscMain"%dirMVA
dirRead   = "%s/Disc_Ntuple/DiscMain"%dirMVA
nMulti    = 5
#-----------------------------------------------------------------
#Years 	      =	["2016Pre", "2016Post", "2017", "2018"]
Years 	      =	["2016Pre", "2016Post", "2017"]
#Years 	      =	["2018"]
Channels 	  =	["Mu", "Ele"]
#Channels 	  =	["Mu"]
Decays 	      =	["Semilep"]
#Mass          = ["800", "1600"]
Mass      = ["700", "800", "900", "1100", "1200", "1300", "1500", "2750"]

#Years and channels to be combined
Years_         = ["2016Pre__2016Post__2017__2018"]
Channels_      = ["Mu", "Ele", "Mu__Ele"]
#Channels_      = ["Mu__Ele"]

S1 = []
#S1.append("SignalSpin32_M700")
S1.append("SignalSpin32_M800")
#S1.append("SignalSpin32_M900")
#S1.append("SignalSpin32_M1100")
#S1.append("SignalSpin32_M1200")
#S1.append("SignalSpin32_M1300")
#S1.append("SignalSpin32_M1500")
#S1.append("SignalSpin32_M2750")
S1.append("TTGamma")
S1.append("WJets")
S1.append("DYJets")
S1.append("WGamma")
S1.append("ZGamma")
S1.append("Others")
S1.append("QCD")

S2 = []
S2.append("TTbar")
S3 = []
S3.append("data_obs")

Samples  = S1+S2+S3

SampDict = {}
SampDict["S1"] = S1
SampDict["S2"] = S2
SampDict["S3"] = S3

Systematics   =	[]
Systematics.append("Weight_pu")
Systematics.append("Weight_mu")
Systematics.append("Weight_pho")
Systematics.append("Weight_ele")
Systematics.append("Weight_btag_b")
Systematics.append("Weight_btag_l")
Systematics.append("Weight_ttag")
Systematics.append("Weight_prefire")
Systematics.append("Weight_q2")
Systematics.append("Weight_pdf")
Systematics.append("Weight_isr")
Systematics.append("Weight_fsr")

systVar = []
levels  = ["Up", "Down"]
for s, l in itertools.product(Systematics, levels):
    systVar.append("%s%s"%(s, l))

JMEs    = ["JEC_Total", "JEC_SubTotalPileUp", "JEC_SubTotalRelative", "JEC_SubTotalAbsolute", "JEC_FlavorQCD", "JEC_TimePtEta", "JER"]
levels_  = ["_up", "_down"]
for s, l in itertools.product(JMEs, levels_):
    systVar.append("%s%s"%(s, l))

SystLevels = []
SystLevels.append("Up")
SystLevels.append("Down")

systToNorm = []
systToNorm.append("Weight_q2Up")
systToNorm.append("Weight_q2Down")
systToNorm.append("Weight_pdfUp")
systToNorm.append("Weight_pdfDown")
systToNorm.append("Weight_isrUp")
systToNorm.append("Weight_isrDown")
systToNorm.append("Weight_fsrUp")
systToNorm.append("Weight_fsrDown")
#----------------------------------------------
#Bkg scale factors: DY, MisID, ZGamma, WGamma
#----------------------------------------------
dictSFs = {}
dictSFs['2016Pre']  = [1.34, 1.79, 1.11, 1.20]
dictSFs['2016Post'] = [1.47, 2.22, 0.54, 1.64]
dictSFs['2017']        = [1.38, 1.01, 1.17, 1.01]
dictSFs['2018']        = [1.38, 1.42, 0.66, 1.23]
dictSFs['2016Pre__2016Post__2017__2018'] = [1.38, 1.40, 0.96, 1.22]

#--------------------------------
#tt+gamma+gluon control regions
#--------------------------------
Regions = {}
Regions['ttyg_Enriched_SR_Resolved'] = "e.Jet_size >=5 && e.Jet_b_size >=1 && e.Photon_size==1 && e.Photon_et[0]>100 && e.FatJet_size ==0"
##Regions['ttyg_Enriched_CR_Resolved'] = "e.Jet_size >=5 && e.Jet_b_size >=1 && e.Photon_size==1 && e.Photon_et[0]<75  && e.FatJet_size ==0"
#Regions['ttyg_Enriched_CRb_Resolved']= "e.Jet_size >=5 && e.Jet_b_size <1  && e.Photon_size==1 && e.Photon_et[0]>0   && e.FatJet_size ==0"

Regions['ttyg_Enriched_SR_Boosted']  = "e.Jet_size >=2 && e.Jet_b_size >=1 && e.Photon_size==1 && e.Photon_et[0]>100 && e.FatJet_size >=1"
##Regions['ttyg_Enriched_CR_Boosted']  = "e.Jet_size >=2 && e.Jet_b_size >=1 && e.Photon_size==1 && e.Photon_et[0]<75  && e.FatJet_size >=1"
#Regions['ttyg_Enriched_CRb_Boosted'] = "e.Jet_size >=2 && e.Jet_b_size <1  && e.Photon_size==1 && e.Photon_et[0]>0   && e.FatJet_size >=1"

#https://github.com/ViniciusMikuni/ttbb-analysis/blob/5d48e5e03bdd0ca162d3dd058f4ee02ef33a8460/python/MVA_cfg.py
batchs = 64
layoutString = "Layout=RELU|64,RELU|64,RELU|64,SOFTSIGN"
training0 =  "LearningRate=1e-3,Momentum=0.0,Repetitions=1,ConvergenceSteps=20,BatchSize=256,TestRepetitions=10,Regularization=L2,Multithreading=True,DropConfig=0.1,DropRepetitions=1"
#training1 = "LearningRate=1e-2,Momentum=0.0,Repetitions=1,ConvergenceSteps=10,BatchSize=256,TestRepetitions=7,Regularization=L2,Multithreading=True"

trainingStrategyString  = "TrainingStrategy="
trainingStrategyString += training0
#trainingStrategyString += training0 + "|" + training1

nnOptions = "!H:V:ErrorStrategy=CROSSENTROPY:VarTransform=None:WeightInitialization=XAVIERUNIFORM"
nnOptions += ":" + layoutString + ":" +  trainingStrategyString + ":Architecture=CPU"

methodDict = {#"BDTG":[ROOT.TMVA.Types.kBDT,":".join(["!H","!V","NTrees=850","MaxDepth=5","BoostType=Grad","Shrinkage=0.01","UseBaggedBoost","BaggedSampleFraction=0.50","SeparationType=GiniIndex","nCuts=50"])],
              #"BDTCW":[ROOT.TMVA.Types.kBDT,":".join(["!H","!V","NTrees=500","MaxDepth=8","BoostType=Grad","Shrinkage=0.01","UseBaggedBoost","BaggedSampleFraction=0.50","SeparationType=GiniIndex","nCuts=50"])],
              #"BDTFish":[ROOT.TMVA.Types.kBDT,":".join(["!H","!V","NTrees=500","MaxDepth=4","BoostType=Grad","Shrinkage=0.01","UseFisherCuts","MinLinCorrForFisher=0.5","UseBaggedBoost","BaggedSampleFraction=0.50","SeparationType=GiniIndex","nCuts=50"])],
              ##"LH":[ROOT.TMVA.Types.kLikelihood,"H:!V:TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmoothBkg[1]=10:NSmooth=1:NAvEvtPerBin=50"],
              #"Cuts":[ROOT.TMVA.Types.kCuts,"H:!V:PopSize=500:Steps=50"],
              #"MLP": [ROOT.TMVA.Types.kMLP, "H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5:!UseRegulator"],
              ##"SVM": [ROOT.TMVA.Types.kSVM,"VarTransform=Norm"],
              "BDTA": [ROOT.TMVA.Types.kBDT, "!H:!V:NTrees=850:MaxDepth=6:BoostType=AdaBoost:AdaBoostBeta=0.05:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=30"],
              #"DNN": [ROOT.TMVA.Types.kDNN, nnOptions],
              #"PyDNN":[ROOT.TMVA.Types.kPyKeras,":".join(["H","V","NumEpochs=700","TriesEarlyStopping=20","BatchSize="+str(batchs)])],
              #"Fish" : [ROOT.TMVA.Types.kFisher, "H:!V:Fisher:VarTransform=None:CreateMVAPdfs:PDFInterpolMVAPdf=Spline2:NbinsMVAPdf=50:NsmoothMVAPdf=10" ],
              #"FishG" : [ROOT.TMVA.Types.kFisher, "H:!V:Fisher:VarTransform=Gauss:CreateMVAPdfs:PDFInterpolMVAPdf=Spline2:Boost_Num=20:Boost_Transform=log:Boost_Type=AdaBoost:Boost_AdaBoostBeta=0.2:!Boost_DetailedMonitoring" ],

              #"PDEFoam": [ROOT.TMVA.Types.kPDEFoam, "!H:!V::SigBgSeparate=F:MaxDepth=4:UseYesNoCell=T:DTLogic=MisClassificationError:FillFoamWithOrigWeights=F:TailCut=0:nActiveCells=500:nBin=20:Nmin=400:Compress=T"],
              ##"LH":[ROOT.TMVA.Types.kLikelihood,"H:!V:TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmoothBkg[1]=10:NSmooth=1:NAvEvtPerBin=50:VarTransform=Decorrelate"],
              #"PyGTB": [ROOT.TMVA.Types.kPyGTB,"!V:NEstimators=850:NJobs=4"],
              #"PyAda": [ROOT.TMVA.Types.kPyAdaBoost,"!V:NEstimators=1000"],
              #"PyForest": [ROOT.TMVA.Types.kPyRandomForest, "!V:VarTransform=None:NEstimators=850:Criterion=gini:MaxFeatures=auto:MaxDepth=4:MinSamplesLeaf=1:MinWeightFractionLeaf=0:Bootstrap=kTRUE"]
              }
def split_list(lst, n):
    print("sample list (len = %s): %s"%(len(lst), lst))
    if n > len(lst):
        n = len(lst)
    print("nMulti jobs: %s"%n)
    sublist_size = len(lst) // n
    remainder = len(lst) % n
    sublists = []
    start = 0
    for i in range(n):
        sublist_length = sublist_size + (1 if i < remainder else 0)
        sublists.append(lst[start:start+sublist_length])
        start += sublist_length
    print("splitted list = %s"%sublists)
    return sublists
