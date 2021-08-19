import ROOT as rt
#-----------------------------------------------------------------
condorHistDir  = "/eos/uscms/store/user/rverma/Output/cms-TT-run2"
#-----------------------------------------------------------------
Year 	      =	["2016", "2017", "2018"]
#Year 	      =	["2017", "2018"]
Channel 	  =	["Mu", "Ele"]
#Channel 	  =	["Mu"]
Decay 	  =	["Dilep"]
SampleSignal = {
         "TT_tytg_M800"    : [rt.kMagenta,  "m_{T} = 800"],
         "TT_tytg_M1200"   : [rt.kCyan,     "m_{T} = 1200"],
         "TT_tytg_M1600"   : [rt.kPink,     "m_{T} = 1600"],
         }
SampleData = {
         "Data"   : [rt.kBlack, "Data"]
         }
SampleBkg = {
         "DYJets"    : [rt.kOrange, "DY+jets"],
         "OtherBkgs"    : [rt.kGreen, "OtherBkgs"]
         }
Samples = SampleBkg
SampleSyst = SampleBkg

Systematics   =	[]
Systematics.append("Weight_pu")
Systematics.append("Weight_mu")
Systematics.append("Weight_ele")
Systematics.append("Weight_btag_b")
Systematics.append("Weight_btag_l")
Systematics.append("Weight_prefire")
#Systematics.append("Weight_q2")
#Systematics.append("Weight_pdf")
Systematics.append("Weight_isr")
Systematics.append("Weight_fsr")
Systematics.append("Weight_jes")
Systematics.append("Weight_jer")
