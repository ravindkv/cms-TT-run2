import ROOT as rt
#-----------------------------------------------------------------
condorHistDir  = "/eos/uscms/store/user/rverma/Output/cms-TT-run2"
#-----------------------------------------------------------------
Year 	      =	["2016", "2017", "2018"]
#Year 	      =	["2016"]
Channel 	  =	["Mu", "Ele"]
#Channel 	  =	["Ele"]
Decay 	  =	["Semilep"]
SampleSignal = {
         "TT_tytg_M800"    : [rt.kMagenta,  "m_{T} = 800"],
         "TT_tytg_M1200"   : [rt.kCyan,     "m_{T} = 1200"],
         "TT_tytg_M1600"   : [rt.kPink,     "m_{T} = 1600"],
         }
SampleData = {
         "Data"   : [rt.kBlack, "Data"]
         }
SampleBkg = {
         "MisIDEle"    : [rt.kRed, "MisIDEle"],
         "OtherPhotons"    : [rt.kGreen, "OtherPhotons"],
         "ZGamma"    : [rt.kBlue, "ZGamma"],
         "WGamma"    : [rt.kOrange, "WGamma"],
         }
Samples = SampleBkg 


