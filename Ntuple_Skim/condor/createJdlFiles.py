import os
import sys
import itertools
sys.dont_write_bytecode = True

#IMPORT MODULES FROM OTHER DIR
sys.path.insert(0, os.getcwd().replace("condor",""))
sys.path.insert(0, os.getcwd().replace("Ntuple_Skim/condor","Skim_NanoAOD/sample"))
from NtupleInputs import *
from JobsNano_cff import Samples_2016PreVFP, Samples_2016PostVFP,  Samples_2017, Samples_2018 

tmpDir = "tmpSub"
if not os.path.exists("%s/log"%tmpDir):
    os.makedirs("%s/log"%tmpDir)
condorLogDir = "log"
tarFile = "%s/Ntuple_Skim.tar.gz"%tmpDir
if os.path.exists(tarFile):
	os.system("rm %s"%tarFile)
os.system("tar -zcvf %s ../../Ntuple_Skim --exclude condor"%tarFile)
os.system("cp runMakeNtuple.sh %s/"%tmpDir)
common_command = \
'Universe   = vanilla\n\
should_transfer_files = YES\n\
when_to_transfer_output = ON_EXIT\n\
Transfer_Input_Files = Ntuple_Skim.tar.gz, runMakeNtuple.sh\n\
use_x509userproxy = true\n\
Output = %s/log_$(cluster)_$(process).stdout\n\
Error  = %s/log_$(cluster)_$(process).stderr\n\
Log    = %s/log_$(cluster)_$(process).condor\n\n'%(condorLogDir, condorLogDir, condorLogDir)
#----------------------------------------
#Create jdl files
#----------------------------------------
subFile = open('%s/condorSubmit.sh'%tmpDir,'w')
nJobAll = 0
for year in Years:
    nJobYear = 0
    sampleList = eval("Samples_%s"%year)
    jdlName = 'submitJobs_%s.jdl'%(year)
    jdlFile = open('%s/%s'%(tmpDir, jdlName),'w')
    jdlFile.write('Executable =  runMakeNtuple.sh \n')
    jdlFile.write(common_command)
    for decay, syst in itertools.product(Decays, Systs):
        outDir = "%s/%s/%s/%s"%(outNtupleDir, year, decay, syst)
        os.system("eos root://cmseos.fnal.gov mkdir -p %s"%outDir)
        jdlFile.write("X=$(step)+1\n")
        for sampleName, fEvt in sampleList.items():
            if "Data" in sampleName and "_" in syst: continue
            nJob = reducedJob(fEvt[0], sampleName)
            args =  'Arguments  = %s %s %s %s $INT(X) %i %s\n' %(year, decay, syst, sampleName, nJob, outDir)
            args += "Queue %i\n\n"%nJob
            nJobYear += nJob
            nJobAll  += nJob
            jdlFile.write(args)
    #print "condor_submit jdl/%s"%jdlFile
    subFile.write("condor_submit %s\n"%jdlName)
    jdlFile.close() 
    print("All jobs for %s = %s"%(year, nJobYear))
subFile.close()
print("All jobs for all years = %s"%(nJobAll))
print("OutputDir: /eos/uscms/%s"%outNtupleDir)