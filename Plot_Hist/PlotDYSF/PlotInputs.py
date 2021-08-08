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
         "DYJets"    : [rt.kYellow, "DY+jets"],
         "OtherBkgs"    : [rt.kBlue, "OtherBkgs"]
         }
