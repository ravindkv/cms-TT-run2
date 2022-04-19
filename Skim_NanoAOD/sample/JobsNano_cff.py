import sys
sys.dont_write_bytecode = True

Samples_2016PreVFP = {'TTWtoQQ': [1, '271.5K'], 'Signal_M700': [1, '35.0K'], 'W1jets': [16, '47.9M'], 'Signal_M800': [1, '35.0K'], 'DYjetsM50': [13, '95.2M'], 'ZGamma': [5, '23.3M'], 'TGJets': [3, '988.0K'], 'WW': [4, '15.9M'], 'QCD_Pt30To50_Mu': [9, '28.7M'], 'QCD_Pt80To120_Mu': [11, '22.0M'], 'QCD_Pt300toInf_Ele': [3, '1.1M'], 'QCD_Pt50to80_Ele': [1, '5.4M'], 'QCD_Pt30to50_Ele': [4, '4.4M'], 'DYjetsM10to50': [4, '25.8M'], 'QCD_Pt50To80_Mu': [6, '19.7M'], 'Data_SingleMu_b1_preVFP': [1, '2.8M'], 'WZ': [2, '7.9M'], 'TTZtoLL': [3, '5.8M'], 'QCD_Pt170To300_Mu': [12, '37.1M'], 'ST_t_channel': [10, '56.0M'], 'Data_SingleMu_b2_preVFP': [14, '158.1M'], 'Signal_M1500': [1, '35.0K'], 'QCD_Pt1000ToInf_Mu': [8, '13.7M'], 'TTGamma_SingleLept': [3, '8.3M'], 'Signal_M1600': [1, '35.0K'], 'W4jets': [11, '4.6M'], 'ST_s_channel': [2, '5.5M'], 'Data_SingleMu_d_preVFP': [8, '98.0M'], 'TTZtoQQ': [3, '6.3M'], 'TTGamma_Dilepton': [2, '4.3M'], 'Data_SingleMu_e_preVFP': [9, '91.0M'], 'QCD_Pt800To1000_Mu': [16, '38.9M'], 'QCD_Pt470To600_Mu': [9, '19.7M'], 'QCD_Pt120to170_Ele': [2, '4.9M'], 'QCD_Pt120To170_Mu': [6, '19.1M'], 'WGamma': [4, '9.7M'], 'Data_SingleEle_d_preVFP': [13, '148.2M'], 'QCD_Pt80to120_Ele': [2, '4.8M'], 'Data_SingleEle_c_preVFP': [10, '97.3M'], 'TTGamma_Hadronic': [5, '4.1M'], 'ST_tbarW_channel': [1, '2.3M'], 'Data_SingleEle_f_preVFP': [8, '61.7M'], 'GJets_HT200To400': [5, '19.3M'], 'ZZ': [1, '1.3M'], 'TTbarPowheg_Semilept': [23, '132.2M'], 'GJets_HT400To600': [2, '4.8M'], 'ST_tW_channel': [1, '2.3M'], 'Signal_M1000': [1, '35.0K'], 'Data_SingleMu_f_preVFP': [8, '57.5M'], 'Data_SingleMu_c_preVFP': [5, '67.4M'], 'QCD_Pt600To800_Mu': [12, '19.6M'], 'QCD_Pt170to300_Ele': [1, '1.9M'], 'Data_SingleEle_b2_preVFP': [21, '246.4M'], 'GJets_HT600ToInf': [2, '4.9M'], 'Signal_M1200': [1, '35.0K'], 'TTbarPowheg_Hadronic': [16, '97.3M'], 'QCD_Pt300To470_Mu': [9, '28.5M'], 'Data_SingleEle_e_preVFP': [14, '117.3M'], 'Data_SingleEle_b1_preVFP': [1, '1.4M'], 'Signal_M1300': [1, '35.0K'], 'W2jets': [8, '26.9M'], 'ST_tbar_channel': [9, '31.0M'], 'TTWtoLNu': [5, '2.9M'], 'TTbarPowheg_Dilepton': [6, '37.5M'], 'W3jets': [9, '16.5M'], 'Signal_M900': [1, '35.0K'], 'Signal_M1400': [1, '35.0K']} 
AllJobs_2016PreVFP = 411 
Samples_2016PostVFP = {'TTWtoQQ': [1, '309.0K'], 'Signal_M700': [1, '35.0K'], 'W1jets': [12, '42.0M'], 'Signal_M800': [1, '35.0K'], 'DYjetsM50': [12, '82.4M'], 'ZGamma': [5, '31.6M'], 'TGJets': [2, '789.0K'], 'WW': [8, '15.8M'], 'QCD_Pt30To50_Mu': [5, '35.5M'], 'QCD_Pt80To120_Mu': [8, '22.0M'], 'QCD_Pt300toInf_Ele': [2, '1.1M'], 'QCD_Pt50to80_Ele': [4, '5.4M'], 'QCD_Pt30to50_Ele': [1, '4.4M'], 'DYjetsM10to50': [7, '22.4M'], 'Data_SingleEle_g_postVFP': [14, '153.4M'], 'WZ': [3, '7.6M'], 'TTZtoLL': [8, '6.0M'], 'Data_SingleEle_f_postVFP': [1, '8.9M'], 'QCD_Pt170To300_Mu': [14, '34.2M'], 'ST_t_channel': [17, '63.1M'], 'Signal_M1500': [1, '35.0K'], 'QCD_Pt1000ToInf_Mu': [4, '13.9M'], 'TTGamma_SingleLept': [3, '9.7M'], 'Signal_M1600': [1, '35.0K'], 'W4jets': [9, '4.8M'], 'ST_s_channel': [4, '5.5M'], 'Data_SingleMu_h_postVFP': [16, '174.0M'], 'TTZtoQQ': [4, '5.4M'], 'TTGamma_Dilepton': [3, '4.7M'], 'QCD_Pt800To1000_Mu': [16, '38.9M'], 'QCD_Pt470To600_Mu': [4, '19.8M'], 'QCD_Pt120to170_Ele': [1, '5.0M'], 'WGamma': [1, '3.4M'], 'Data_SingleMu_f_postVFP': [1, '8.0M'], 'QCD_Pt80to120_Ele': [2, '4.8M'], 'TTGamma_Hadronic': [3, '4.8M'], 'Data_SingleMu_g_postVFP': [14, '149.9M'], 'ST_tbarW_channel': [4, '2.6M'], 'GJets_HT200To400': [3, '20.0M'], 'ZZ': [3, '1.2M'], 'TTbarPowheg_Semilept': [27, '144.7M'], 'GJets_HT400To600': [2, '5.0M'], 'ST_tW_channel': [5, '2.5M'], 'Signal_M1000': [1, '35.0K'], 'QCD_Pt120To170_Mu': [6, '19.8M'], 'QCD_Pt600To800_Mu': [11, '18.2M'], 'QCD_Pt170to300_Ele': [1, '1.9M'], 'GJets_HT600ToInf': [2, '4.7M'], 'Signal_M1200': [1, '35.0K'], 'TTbarPowheg_Hadronic': [29, '107.1M'], 'QCD_Pt300To470_Mu': [6, '29.8M'], 'QCD_Pt50To80_Mu': [6, '21.5M'], 'Signal_M1300': [1, '35.0K'], 'W2jets': [7, '24.5M'], 'ST_tbar_channel': [7, '30.6M'], 'TTWtoLNu': [2, '3.3M'], 'TTbarPowheg_Dilepton': [10, '43.5M'], 'W3jets': [4, '17.8M'], 'Data_SingleEle_h_postVFP': [16, '129.0M'], 'Signal_M900': [1, '35.0K'], 'Signal_M1400': [1, '35.0K']} 
AllJobs_2016PostVFP = 369 
Samples_2017 = {'TTWtoQQ': [2, '655.0K'], 'Signal_M700': [1, '200.0K'], 'W1jets': [12, '46.8M'], 'Signal_M800': [1, '200.0K'], 'DYjetsM50': [15, '102.9M'], 'ZGamma': [9, '29.9M'], 'W4jets': [11, '9.6M'], 'TGJets': [5, '2.0M'], 'WW': [3, '15.6M'], 'QCD_Pt30To50_Mu': [22, '58.6M'], 'QCD_Pt80To120_Mu': [12, '46.0M'], 'QCD_Pt300toInf_Ele': [1, '2.2M'], 'QCD_Pt50to80_Ele': [1, '10.2M'], 'QCD_Pt30to50_Ele': [1, '8.8M'], 'DYjetsM10to50': [15, '68.5M'], 'Data_SingleEle_b': [6, '60.5M'], 'Data_SingleEle_c': [12, '136.6M'], 'Data_SingleEle_d': [7, '51.5M'], 'WZ': [4, '7.9M'], 'TTZtoLL': [4, '14.0M'], 'Data_SingleMu_c': [23, '165.7M'], 'Data_SingleMu_b': [16, '136.3M'], 'QCD_Pt170To300_Mu': [19, '73.1M'], 'ST_t_channel': [39, '129.9M'], 'Data_SingleMu_f': [23, '242.1M'], 'Signal_M1500': [1, '197.7K'], 'Data_SingleMu_d': [9, '70.4M'], 'TTGamma_SingleLept': [4, '18.9M'], 'Signal_M1600': [1, '200.0K'], 'Data_SingleEle_e': [10, '102.1M'], 'ST_s_channel': [3, '13.6M'], 'Data_SingleEle_f': [13, '128.5M'], 'TTZtoQQ': [7, '13.8M'], 'TTGamma_Dilepton': [2, '10.0M'], 'QCD_Pt800To1000_Mu': [20, '78.2M'], 'QCD_Pt470To600_Mu': [8, '39.5M'], 'QCD_Pt120to170_Ele': [7, '9.9M'], 'WGamma': [5, '10.3M'], 'QCD_Pt80to120_Ele': [4, '9.6M'], 'TTGamma_Hadronic': [4, '10.5M'], 'ST_tbarW_channel': [9, '5.7M'], 'GJets_HT200To400': [3, '16.5M'], 'ZZ': [1, '2.7M'], 'TTbarPowheg_Semilept': [59, '346.1M'], 'GJets_HT400To600': [1, '4.0M'], 'ST_tW_channel': [8, '5.6M'], 'Signal_M1000': [1, '200.0K'], 'QCD_Pt120To170_Mu': [15, '39.4M'], 'QCD_Pt600To800_Mu': [11, '39.3M'], 'Data_SingleMu_e': [15, '154.6M'], 'QCD_Pt170to300_Ele': [1, '3.7M'], 'GJets_HT600ToInf': [2, '4.2M'], 'Signal_M1200': [1, '200.0K'], 'TTbarPowheg_Hadronic': [40, '233.0M'], 'QCD_Pt300To470_Mu': [13, '58.7M'], 'QCD_Pt50To80_Mu': [9, '40.3M'], 'Signal_M1300': [1, '200.0K'], 'W2jets': [7, '26.6M'], 'ST_tbar_channel': [12, '69.8M'], 'TTWtoLNu': [2, '7.1M'], 'QCD_Pt1000ToInf_Mu': [8, '27.5M'], 'TTbarPowheg_Dilepton': [20, '106.7M'], 'W3jets': [6, '17.9M'], 'Signal_M900': [1, '200.0K'], 'Signal_M1400': [1, '194.0K']} 
AllJobs_2017 = 609 
Samples_2018 = {'TTWtoQQ': [1, '970.2K'], 'Signal_M700': [1, '200.0K'], 'W1jets': [12, '47.9M'], 'Signal_M800': [1, '200.0K'], 'DYjetsM50': [14, '96.2M'], 'ZGamma': [11, '29.9M'], 'TGJets': [6, '2.0M'], 'WW': [6, '15.7M'], 'QCD_Pt30To50_Mu': [13, '58.7M'], 'QCD_Pt80To120_Mu': [12, '45.5M'], 'QCD_Pt300toInf_Ele': [1, '2.2M'], 'QCD_Pt50to80_Ele': [1, '10.5M'], 'QCD_Pt30to50_Ele': [5, '8.6M'], 'DYjetsM10to50': [17, '94.5M'], 'Data_SingleEle_a': [45, '339.0M'], 'Data_SingleEle_b': [15, '153.8M'], 'Data_SingleEle_c': [16, '147.8M'], 'Data_SingleEle_d': [71, '752.5M'], 'WZ': [3, '7.9M'], 'TTZtoLL': [4, '19.6M'], 'Data_SingleMu_c': [11, '110.0M'], 'Data_SingleMu_b': [10, '119.9M'], 'Data_SingleMu_a': [18, '241.6M'], 'QCD_Pt170To300_Mu': [13, '71.9M'], 'ST_t_channel': [30, '178.3M'], 'Signal_M1500': [1, '200.0K'], 'Data_SingleMu_d': [39, '513.9M'], 'TTGamma_SingleLept': [6, '27.7M'], 'Signal_M1600': [1, '199.0K'], 'W4jets': [10, '9.1M'], 'ST_s_channel': [4, '19.4M'], 'TTZtoQQ': [4, '19.8M'], 'TTGamma_Dilepton': [3, '14.7M'], 'QCD_Pt800To1000_Mu': [19, '78.9M'], 'QCD_Pt470To600_Mu': [17, '38.5M'], 'QCD_Pt120to170_Ele': [3, '9.7M'], 'WGamma': [3, '9.9M'], 'QCD_Pt80to120_Ele': [2, '9.5M'], 'TTGamma_Hadronic': [5, '14.8M'], 'ST_tbarW_channel': [4, '7.7M'], 'GJets_HT200To400': [4, '19.4M'], 'ZZ': [1, '3.5M'], 'TTbarPowheg_Semilept': [78, '476.4M'], 'GJets_HT400To600': [1, '4.6M'], 'ST_tW_channel': [10, '8.0M'], 'Signal_M1000': [1, '200.0K'], 'QCD_Pt120To170_Mu': [13, '38.0M'], 'QCD_Pt600To800_Mu': [21, '37.2M'], 'QCD_Pt170to300_Ele': [1, '3.7M'], 'GJets_HT600ToInf': [2, '4.7M'], 'Signal_M1200': [1, '200.0K'], 'TTbarPowheg_Hadronic': [68, '334.2M'], 'QCD_Pt300To470_Mu': [14, '58.9M'], 'QCD_Pt50To80_Mu': [7, '40.0M'], 'Signal_M1300': [1, '200.0K'], 'W2jets': [9, '27.4M'], 'ST_tbar_channel': [26, '95.6M'], 'TTWtoLNu': [2, '10.4M'], 'QCD_Pt1000ToInf_Mu': [6, '27.4M'], 'TTbarPowheg_Dilepton': [31, '145.0M'], 'W3jets': [7, '18.3M'], 'Signal_M900': [1, '191.0K'], 'Signal_M1400': [1, '194.3K']} 
AllJobs_2018 = 764 
AllJobs_AllYears = 2153 
