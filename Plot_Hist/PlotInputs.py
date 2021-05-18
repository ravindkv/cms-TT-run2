import ROOT as rt
#-----------------------------------------------------------------
condorHistDir  = "/eos/uscms/store/user/rverma/Output/cms-TT-run2"
#-----------------------------------------------------------------
#Year 	      =	["2016", "2017", "2018"]
Year 	      =	["2016"]
#Channel 	  =	["Mu", "Ele"]
Channel 	  =	["Mu"]
Decay 	  =	["Semilep"]
Systematics   =	[]
Systematics.append("Weight_pu")
Systematics.append("Weight_mu")
Systematics.append("Weight_pho")
Systematics.append("Weight_ele")
Systematics.append("Weight_btag_b")
Systematics.append("Weight_btag_l")
Systematics.append("Weight_prefire")
Systematics.append("Weight_q2")
Systematics.append("Weight_pdf")
Systematics.append("Weight_isr")
Systematics.append("Weight_fsr")

SystLevels = []
SystLevels.append("Up")
SystLevels.append("Down")

SampleSignal = {
         "TT_tytg_M800"    : [rt.kMagenta,  "m_{T} = 800"],
         "TT_tytg_M1200"   : [rt.kCyan,     "m_{T} = 1200"],
         "TT_tytg_M1600"   : [rt.kPink,     "m_{T} = 1600"],
         }

SampleBkg = {
         "TTGamma"   : [rt.kGreen, "t#bar{t}#gamma"],
         "TTbar"     : [rt.kRed, "t#bar{t}"],
         "SingleTop" : [rt.kOrange, "t"],
         #"QCD"       : [rt.kPink, "QCD"],
         "Others"    : [rt.kBlue, "Others"]
         }
SampleData = {
         "Data"   : [rt.kBlack, "Data"]
         }
SampleWeight = ["TTGamma", "TTbar", "TT_tytg_M800"]
SampleLumi = SampleBkg
#SampleLumi.update(SampleSignal)
SampleSyst = SampleBkg.keys()
Samples = SampleSignal.keys() + SampleBkg.keys() + SampleData.keys()
plotList = ["Muon_pt"]
