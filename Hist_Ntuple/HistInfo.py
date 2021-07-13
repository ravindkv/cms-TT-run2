
#key is the histName in the ntuple, 
#value[0] is the title of x-axis
#value[1] is the number of bins, x-range
#value[2] decide if it is to be drawn for MC or data or both. Default value is for both.
def GetHistogramInfo():
    hDict = { 
             "Muon_pt"              : ["Muon_pt"     , [30,0,1650], True],
             "Muon_eta"             : ["Muon_eta"    , [12,-2.88,2.88], True],
             "Muon_phi"             : ["Muon_phi"    , [20,-5.0,5.0], True],
             "Electron_pt"          : ["Electron_pt"    , [30,0,1500], True],
             "Electron_eta_sc"      : ["Electron_eta_sc" , [12,-2.88,2.88], True],
             "Electron_phi"         : ["Electron_phi"   , [20,-5.0,5.0], True],
             "Photon_et"            : ["Photon_et"    , [30,-20,1180], True],
             "Photon_size"          : ["Photon_size"     , [10,-0.5,9.5], True],
             "Jet_size"             : ["Jet_size"     , [16,-0.5,15.5], True],
             "Jet_b_size"           : ["Jet_b_size"     , [10,-0.5,9.5], True],
             "Jet_pt"               : ["Jet_pt"    , [30,-20,1480], True],
             "Jet_eta"             : ["Jet_eta"    , [12,-2.88,2.88], True],
             "Reco_met"             : ["Reco_met"      , [30,-20,1180], True],
             "Reco_mass_lgamma"     : ["Reco_mass_lgamma", [30,0,3000], True],
             "Reco_mass_t_had"      : ["Reco_mass_t_had", [30,0,3000], True],
             "Reco_mass_t_lep"      : ["Reco_mass_t_lep", [30,0,3000], True],
             "Reco_ht"              : ["Reco_ht"        , [30,0,6000], True],
             "Reco_st"              : ["Reco_st"        , [30,0,6000], True],
             "Reco_mass_T_had"      : ["Reco_mass_T_had", [30,0,6000], True],
             "Reco_mass_T_lep"      : ["Reco_mass_T_lep", [30,0,6000], True],
             "Reco_mass_T"          : ["Reco_mass_T", [30,0,6000], True],
             "Reco_mass_TT"         : ["Reco_mass_TT", [30,0,6000], True],
             "Reco_chi2"            : ["Reco_chi2", [30, 0,1200], True],
             "FatJet_size"             : ["FatJet_size"            , [5,-0.5,4.5], True],
             "FatJet_pt"               : ["FatJet_pt"              , [30,0,3000], True],
             "FatJet_eta"              : ["FatJet_eta"             , [12,-2.88,2.88], True],
             "FatJet_mass"             : ["FatJet_mass"            , [30,0,1200], True],
             "FatJet_msoftdrop"        : ["FatJet_msoftdrop"       , [30,0,1200], True],
             "FatJet_btagDeepB"        : ["FatJet_btagDeepB"       , [20,-0.5,1.5], True],
             "FatJet_deepTagMD_TvsQCD" : ["FatJet_deepTagMD_TvsQCD", [20,-0.5,1.5], True],
             "FatJet_deepTagMD_WvsQCD" : ["FatJet_deepTagMD_WvsQCD", [20,-0.5,1.5], True],
             "FatJet_deepTag_TvsQCD"   : ["FatJet_deepTag_TvsQCD"  , [20,-0.5,1.5], True],
             "FatJet_deepTag_WvsQCD"   : ["FatJet_deepTag_WvsQCD"  , [20,-0.5,1.5], True],
             }
    hDictWeight = { 
             "Weight_lumi"              : ["Weight_lumi"            , [30,0.0,1500000], True],
             "Weight_pu"                : ["Weight_pu"              , [25,0.0,2.0], True],
             "Weight_prefire"           : ["Weight_prefire"         , [30,0.0,1.5], True],
             "Weight_btag"              : ["Weight_btag"            , [25,0.0,2.0], True],
             "Weight_mu"                : ["Weight_mu"              , [30,0.0,1.5], True],
             "Weight_mu_id"             : ["Weight_mu_id"       , [30,0.0,1.5], True],
             "Weight_mu_iso"            : ["Weight_mu_iso"       , [30,0.0,1.5], True],
             "Weight_mu_trig"           : ["Weight_mu_trig"         , [30,0.0,1.5], True],
             "Weight_ele"               : ["Weight_ele"             , [30,0.0,1.5], True],
             "Weight_ele_id"            : ["Weight_ele_id"     , [30,0.0,1.5], True],
             "Weight_ele_reco"          : ["Weight_ele_reco"     , [30,0.0,1.5], True],
             "Weight_ele_trig"          : ["Weight_ele_trig"        , [30,0.0,1.5], True],
             "Weight_pho"               : ["Weight_pho"             , [30,0.0,1.5], True],
             "Weight_pho_id"            : ["Weight_pho_id"          , [30,0.0,1.5], True],
             "Weight_pho_e_veto"        : ["Weight_pho_e_veto"      , [30,0.0,1.5], True],
             "Weight_pu_up"             : ["Weight_pu_up"           , [25,0.0,2.0], True],
             "Weight_pu_down"           : ["Weight_pu_down"         , [25,0.0,2.0], True],
             "Weight_prefire_up"        : ["Weight_prefire_up"      , [30,0.0,1.5], False],
             "Weight_prefire_down"      : ["Weight_prefire_down"     ,[30,0.0,1.5], False],
             "Weight_btag_b_up"         : ["Weight_btag_b_up"       , [25,0.0,2.0], False],
             "Weight_btag_b_down"       : ["Weight_btag_b_down"     , [25,0.0,2.0], False],
             "Weight_btag_l_up"         : ["Weight_btag_l_up"       , [25,0.0,2.0], False],
             "Weight_btag_l_down"       : ["Weight_btag_l_down"     , [25,0.0,2.0], False],
             "Weight_mu_up"             : ["Weight_mu_up"           , [30,0.0,1.5], False],
             "Weight_mu_down"           : ["Weight_mu_down"         , [30,0.0,1.5], False],
             "Weight_mu_id_up"          : ["Weight_mu_id_up"     , [30,0.0,1.5], False],
             "Weight_mu_id_down"        : ["Weight_mu_id_down"     , [30,0.0,1.5], False],
             "Weight_mu_iso_up"         : ["Weight_mu_iso_up"     , [30,0.0,1.5], False],
             "Weight_mu_iso_down"       : ["Weight_mu_iso_down"     , [30,0.0,1.5], False],
             "Weight_mu_trig_up"        : ["Weight_mu_trig_up"      , [30,0.0,1.5], False],
             "Weight_mu_trig_down"      : ["Weight_mu_trig_down"     , [30,0.0,1.5], False],
             "Weight_ele_up"            : ["Weight_ele_up"          , [30,0.0,1.5], False],
             "Weight_ele_down"          : ["Weight_ele_down"        , [30,0.0,1.5], False],
             "Weight_ele_id_up"         : ["Weight_ele_id_up"     , [30,0.0,1.5], False],
             "Weight_ele_id_down"       : ["Weight_ele_id_down"     , [30,0.0,1.5], False],
             "Weight_ele_reco_up"       : ["Weight_ele_reco_up"     , [30,0.0,1.5], False],
             "Weight_ele_reco_down"     : ["Weight_ele_reco_down"     , [30,0.0,1.5], False],
             "Weight_ele_trig_up"       : ["Weight_ele_trig_up"     , [30,0.0,1.5], False],
             "Weight_ele_trig_down"     : ["Weight_ele_trig_down"     , [30,0.0,1.5], False],
             "Weight_pho_up"            : ["Weight_pho_up"          , [30,0.0,1.5], False],
             "Weight_pho_down"          : ["Weight_pho_down"        , [30,0.0,1.5], False],
             "Weight_pho_id_up"         : ["Weight_pho_id_up"       , [30,0.0,1.5], False],
             "Weight_pho_id_down"       : ["Weight_pho_id_down"     , [30,0.0,1.5], False],
             "Weight_pho_e_veto_up"     : ["Weight_pho_e_veto_up"     , [30,0.0,1.5], False],
             "Weight_pho_e_veto_down"   : ["Weight_pho_e_veto_down"     , [30,0.0,1.5], False],
             "Weight_q2"                : ["Weight_q2"              , [30,0.0,1.5], False],
             "Weight_q2_up"             : ["Weight_q2_up"           , [30,0.0,1.5], False],
             "Weight_q2_down"           : ["Weight_q2_down"         , [30,0.0,1.5], False],
             "Weight_gen"               : ["Weight_gen"             , [30,0.0,1.5], False],
             "Weight_pdf"               : ["Weight_pdf"             , [30,0.0,1.5], False],
             "Weight_pdf_up"            : ["Weight_pdf_up"          , [30,0.0,1.5], False],
             "Weight_pdf_down"          : ["Weight_pdf_down"        , [30,0.0,1.5], False],
             "Weight_pdf_syst"          : ["Weight_pdf_syst"        , [30,0.0,1.5], False],
             "Weight_pdf_unc"           : ["Weight_pdf_unc"         , [30,0.0,1.5], False],
             "Weight_isr_up"            : ["Weight_isr_up"          , [30,0.0,1.5], False],
             "Weight_isr_down"          : ["Weight_isr_down"        , [30,0.0,1.5], False],
             "Weight_fsr_up"            : ["Weight_fsr_up"          , [30,0.0,1.5], False],
             "Weight_fsr_down"          : ["Weight_fsr_down"        , [30,0.0,1.5], False],
             }
    hDictTemp = {
             ##"Jet_pt"               : ["Jet_pt"    , [30,-20,1480], True],
             #"Jet_eta"             : ["Jet_eta"    , [12,-2.88,2.88], True],
             ##"Jet_size"             : ["Jet_size"     , [16,-0.5,15.5], True],
             #"Reco_mass_lgamma"     : ["Reco_mass_lgamma", [30,0,3000], True],
             #"Jet_b_size"           : ["Jet_b_size"     , [10,-0.5,9.5], True],
             #"Photon_et"            : ["Photon_et"    , [30,-20,1180], True],
             #"Reco_mass_T"          : ["Reco_mass_T", [30,0,6000], True]
             "Reco_met"             : ["Reco_met"      , [30,-20,1180], True],
             "Reco_ht"              : ["Reco_ht"        , [30,0,6000], True],
             "Muon_pt"              : ["Muon_pt"     , [30,0,1650], True],
             "Muon_eta"             : ["Muon_eta"    , [12,-2.88,2.88], True],
             "Electron_pt"          : ["Electron_pt"    , [30,0,1500], True],
             "Electron_eta_sc"      : ["Electron_eta_sc" , [12,-2.88,2.88], True],
             }
    return hDictTemp
    #return hDict 
    #return hDictWeight 

allHistList = GetHistogramInfo().keys()
allHistList2D = [
["Reco_mass_T"    , "Reco_chi2"],
["Reco_mass_t_had", "Reco_chi2"],
["Reco_mass_t_lep", "Reco_chi2"],
["Reco_mass_T_had", "Reco_chi2"],
["Reco_mass_T_lep", "Reco_chi2"],
["Reco_mass_t_had", "Reco_mass_t_lep"],
["Reco_mass_T_had", "Reco_mass_T_lep"],
]
