import ROOT as rt
#-----------------------------------------------------------------
dirCBA  = "/eos/uscms/store/user/rverma/Output/cms-TT-run2/CBA_Ntuple"
dirHist = "%s/Hist_Ntuple/HistMisIDSF"%dirCBA
dirPlot = "%s/Plot_Hist/PlotMisIDSF"%dirCBA
dirTwiki= "/eos/uscms/store/user/rverma/Output/cms-TT-run2/Twiki"
#-----------------------------------------------------------------
Years 	      =	["2016Pre", "2016Post", "2017", "2018"]
#Year 	      =	["2017"]
Channels 	  =	["Mu", "Ele"]
#Channel 	  =	["Ele"]
Decays 	      =	["Semilep"]

#Years and channels to be commbined
Years_         = ["2016Pre__2016Post__2017__2018"]
Channels_      = ["Mu", "Ele", "Mu__Ele"]
#Channels_      = ["Mu__Ele"]

SampleSignal = {
         "SignalSpin32_M800"    : [rt.kMagenta,  "m_{T} = 800"],
         "SignalSpin32_M1200"   : [rt.kCyan,     "m_{T} = 1200"],
         "SignalSpin32_M1500"   : [rt.kPink,     "m_{T} = 1500"],
         }
SampleData = {
         "data_obs"   : [rt.kBlack, "Data"]
         }
SampleBkg = {
         "MisIDEle"    : [rt.kRed, "MisIDEle"],
         "OtherPhotons"    : [rt.kGreen, "OtherPhotons"],
         "ZGamma"    : [rt.kBlue, "ZGamma"],
         "WGamma"    : [rt.kOrange, "WGamma"],
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
Systematics.append("Weight_pdf")
Systematics.append("Weight_pho")
Systematics.append("Weight_isr")
Systematics.append("Weight_fsr")
Systematics.append("Weight_jes")
Systematics.append("Weight_jer")
