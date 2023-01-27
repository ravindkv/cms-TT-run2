import os
import sys
sys.dont_write_bytecode = True
import itertools
from optparse import OptionParser
from DiscInputs import SampDict 

#-----------------------------------------
#INPUT Command Line Arguments 
#----------------------------------------
parser = OptionParser()
parser.add_option("-y", "--year", dest="year", default="2016PreVFP",type='str',
                     help="Specifyi the year of the data taking" )
parser.add_option("-d", "--decay", dest="decay", default="Semilep",type='str',
                     help="Specify which decay moded of ttbar Semilep or Dilep? default is Semilep")
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
                     help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("-s", "--sample", dest="sample", default="S1",type='str',
                             help="Specify which sample to run on" )
parser.add_option("-r", "--region", dest="region", default="ttyg_Enriched_SR_Resolved",type='str', 
                     help="which control selection and region"), 
parser.add_option("--syst", "--systematic", dest="systematic", default="Base",type='str',
                     help="Specify which systematic to run on")
parser.add_option("--method", "--method", dest="method", default="BDTA",type='str', 
                     help="Which MVA method to be used")
(options, args) = parser.parse_args()
year    = options.year
decay   = options.decay
channel = options.channel
sample  = options.sample
method  = options.method
region  = options.region
syst    = options.systematic

for s in SampDict[sample]: 
    args = "-y %s -d %s -c %s -s %s --method %s -r %s --syst %s "%(year, decay, channel, s, method, region, syst)
    os.system("python3 reader.py %s"%args)
    print(args)

