btagWeightCategory = ["1","(1-btagWeight[0])","(btagWeight[2])","(btagWeight[1])"]
def GetHistogramInfo(extraCuts="(passPresel_Mu && nJet>=4 && nBJet>=2)*", nBJets=1):

    histogramInfo = { 
                      "Njet"                           : ["nJet"      , "Njet"     ,        [16,-0.5,15.5], extraCuts      , "", True],
                      "Nbjet"                          : ["nBJet"     , "Nbjet"    ,        [10,0,10], extraCuts      , "", True],
                      "jetPt"                           : ["jetPt"      , "jetPt"     ,      [50,30,1000], extraCuts      , "", True],
                      "muPt"                           : ["muPt"      , "muPt"     ,      [50,30,1000], extraCuts      , "", True],
                      "phoPt"                           : ["phoEt"      , "phoPt"     ,      [50,20,1000], extraCuts      , "", True],
                      "muEta"                          : ["muEta"     , "muEta"    ,   [20,-2.4,2.4], extraCuts      , "", True],
                      "muPhi"                          : ["muPhi"     , "muPhi"    , [20,-3.15,3.15], extraCuts      , "", True],
                      "elePt"                          : ["elePt"     , "elePt"    ,      [20,30,1000], extraCuts      , "", True],
                      "eleSCEta"                       : ["eleSCEta"  , "eleSCEta" ,   [20,-2.4,2.4], extraCuts      , "", True],
                      "elePhi"                         : ["elePhi"    , "elePhi"   , [20,-3.15,3.15], extraCuts      , "", True],
                      "M3"                             : ["M3"        , "M3"       ,     [150,0,1500], extraCuts      , "", True],
                      "MET"                            : ["pfMET"     , "MET"      ,      [20,0,1000], extraCuts      , "", True],
                      "nVtx"                           : ["nVtx"      , "nVtx"     ,        [50,0,50], extraCuts      , "", True],
                      "WtransMass"                     : ["WtransMass","WtransMass",      [20,0,1000], extraCuts      , "", True],
                      "HT"                             : ["HT"        ,"HT"        ,   [20,0,1000], extraCuts      , "", True],
                      "TopHad_mass"                    : ["TopHad_mass"        ,"TopHad_mass"        ,   [30,0,3000], extraCuts      , "", True],
                      "TopLep_mass"                    : ["TopLep_mass"        ,"TopLep_mass"        ,   [30,0,3000], extraCuts      , "", True],
                      "TopTop_mass"                    : ["TopTop_mass"        ,"TopTop_mass"        ,   [30,0,3000], extraCuts      , "", True],
                      "TopStarHad_mass"                    : ["TopStarHad_mass"        ,"TopStarHad_mass"        ,   [30,0,3000], extraCuts      , "", True],
                      "TopStarLep_mass"                    : ["TopStarLep_mass"        ,"TopStarLep_mass"        ,   [30,0,3000], extraCuts      , "", True],
                      "TopStar_mass"                    : ["TopStar_mass"        ,"TopStar_mass"        ,   [30,0,3000], extraCuts      , "", True],
                      "tgtg_mass"                    : ["tgtg_mass"        ,"tgtg_mass"        ,   [30,0,6000], extraCuts      , "", True],
                      "chi2"                           : ["chi2"        ,"chi2"        ,   [50, 0,1000], extraCuts      , "", True],
                      "jetRes"                         : ["jetRes"        ,"jetRes"        ,   [50,0,1.5], extraCuts      , "", True]
                      }
    return histogramInfo

allPlotList = [
#"TopHad_mass",
#"TopLep_mass",
"TopStarHad_mass",
"TopStarLep_mass",
"TopStar_mass",
"chi2",
#"tgtg_mass",
"Njet",      
"muPt",      
"jetPt",      
"phoPt",      
"muEta",     
"MET",       
"Nbjet",     
]

'''
allPlotList = [
"TopHad_mass",
"TopTop_mass",
"TopLep_mass",
"chi2",
"M3"]      

allPlotList = [
"Njet",      
"Nbjet",     
"muPt",      
"muEta",     
"muPhi",     
"elePt",     
"eleSCEta",  
"elePhi",    
"M3",        
"MET",       
"nVtx",      
"WtransMass",
"HT"]      
'''
allPlotList2D = [
#["M3", "chi2"],        
["TopHad_mass", "chi2"],
["TopLep_mass", "chi2"],
["TopStarHad_mass", "chi2"],
["TopStarLep_mass", "chi2"],
["TopStar_mass", "chi2"],
["TopHad_mass", "TopLep_mass"],
["TopStarHad_mass", "TopStarLep_mass"],
]
