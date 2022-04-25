#include "../interface/EventPick_Skim.h"
#include <iostream> 
#include <iomanip>

EventPick::EventPick(std::string titleIn){
    title = titleIn;
    year = "2016";
}

EventPick::~EventPick(){
}

void EventPick::process_event(EventTree* tree){
    passSkim = false;
    bool passTrigMu  = false;
    bool passTrigEle = false;
    //Check muon and electron triggers
    //https://twiki.cern.ch/twiki/bin/viewauth/CMS/EgHLTRunIISummary
    //https://twiki.cern.ch/twiki/bin/view/CMS/MuonHLT2016
    if (year.find("2016")!=std::string::npos){
        passTrigMu = 
            tree->HLT_Mu50_ || 
            tree->HLT_TkMu50_;                 
        passTrigEle = 
            tree->HLT_Ele27_WPTight_Gsf_ ||
            tree->HLT_Ele115_CaloIdVT_GsfTrkIdT_||
            tree->HLT_Photon175_ ;
    }                                                                           
    //https://twiki.cern.ch/twiki/bin/view/CMS/MuonHLT2017
    if (year=="2017"){                                                          
        passTrigMu = 
            tree->HLT_Mu50_ || 
            tree->HLT_OldMu100_||
            tree->HLT_TkMu100_ ; 
        passTrigEle = 
            tree->HLT_Ele35_WPTight_Gsf_ ||
            tree->HLT_Ele115_CaloIdVT_GsfTrkIdT_||
            tree->HLT_Photon200_;
    }                                                                           
    //https://twiki.cern.ch/twiki/bin/view/CMS/MuonHLT2018
    if (year=="2018"){                                                          
        passTrigMu = 
            tree->HLT_Mu50_ || 
            tree->HLT_OldMu100_||
            tree->HLT_TkMu100_;
        passTrigEle = 
            tree->HLT_Ele32_WPTight_Gsf_ ||
            tree->HLT_Ele115_CaloIdVT_GsfTrkIdT_||
            tree->HLT_Photon200_ ;
    }
    //Check MET filters    
    //https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2
    bool filters = 
            (tree->Flag_goodVertices_ &&
		    tree->Flag_globalSuperTightHalo2016Filter_ &&
		    tree->Flag_HBHENoiseFilter_ &&
		    tree->Flag_HBHENoiseIsoFilter_ && 
		    tree->Flag_EcalDeadCellTriggerPrimitiveFilter_ &&
		    tree->Flag_BadPFMuonFilter_ &&
		    tree->Flag_eeBadScFilter_ );
    if (year=="2017" || year=="2018"){ 
        filters = filters && tree->Flag_ecalBadCalibFilter_ ;
    }
    //To reject events where neither muon nor electron is present
    bool zeroLep = (tree->nMu_ == 0) && (tree->nEle_ ==0);
    
    //Apply above selections along with additional cuts on PV, nJet, and MET
    passSkim = 
        (passTrigEle || passTrigMu) && 
        filters && 
        !zeroLep && 
        tree->nGoodVtx_>0 &&
        tree->nJet_>0 &&
        tree->MET_pt_>15;
}

