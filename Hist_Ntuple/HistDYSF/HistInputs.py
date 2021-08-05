#-----------------------------------------------------------------
condorHistDir = "/eos/uscms/store/user/rverma/Output/cms-TT-run2/Hist_Ntuple/HistDYSF/Raw"
#-----------------------------------------------------------------
#Years 	      =	["2016", "2017", "2018"]
Years 	      =	["2016"]
#Channels 	  =	["Mu", "Ele"]
Channels 	  =	["Ele"]
Decays 	      =	["Dilep"]

Samples = []
#bkg and data
Samples.append("TT_tytg_M800")
Samples.append("TT_tytg_M1200")
Samples.append("TT_tytg_M1600")
Samples.append("TTbar")
Samples.append("TTGamma")
Samples.append("WJets")
Samples.append("DYJets")
Samples.append("WGamma")
Samples.append("ZGamma")
Samples.append("Others")
Samples.append("QCDEle")
Samples.append("QCDMu")
Samples.append("DataMu")
Samples.append("DataEle")

Systematics   =	[]
Systematics.append("Weight_pu")
Systematics.append("Weight_mu")
Systematics.append("Weight_ele")
Systematics.append("Weight_btag_b")
Systematics.append("Weight_btag_l")
Systematics.append("Weight_prefire")
Systematics.append("Weight_q2")
Systematics.append("Weight_pdf")
Systematics.append("Weight_isr")
Systematics.append("Weight_fsr")
Systematics.append("Weight_jes")
Systematics.append("Weight_jer")
#Systematics   =	[]

SystLevels = []
SystLevels.append("Up")
SystLevels.append("Down")

Regions = {}
Regions['DY_Enriched_a2j_e0b_e0y']              = "Jet_size>=2 && Jet_b_size==0 && Photon_size==0" 
Regions['DY_Enriched_e3j_e0b_e0y']              = "Jet_size==3 && Jet_b_size==0 && Photon_size==0" 
Regions['DY_Enriched_a3j_e0b_e0y']              = "Jet_size>=3 && Jet_b_size==0 && Photon_size==0" 
Regions['DY_Enriched_a4j_e0b_e0y']              = "Jet_size>=4 && Jet_b_size==0 && Photon_size==0" 
