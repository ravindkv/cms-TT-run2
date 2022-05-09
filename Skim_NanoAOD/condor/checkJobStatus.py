import os
import sys
sys.dont_write_bytecode = True

#IMPORT MODULES FROM OTHER DIR
sys.path.insert(0, os.getcwd().replace("condor",""))
sys.path.insert(0, os.getcwd().replace("condor","sample"))
from SkimInputs import *
from JobsNano_cff import Samples_2016PreVFP, Samples_2016PostVFP,  Samples_2017, Samples_2018 

#-----------------------------------------
#Function to compare two lists
#----------------------------------------
def returnNotMatches(a, b):
    return [[x for x in a if x not in b], [x for x in b if x not in a]]

for year in Years:
    #-----------------------------------------
    #Path of the output histrograms
    #----------------------------------------
    inHistFullDir = "/eos/uscms/%s/%s"%(outSkimDir, year)
    #inHistFullDir = "%s/%s"%(condorHistDir, inHistSubDir)
    condorLogDir = "tmpSub/log"

    #----------------------------------------
    #Get all submitted jobs
    #----------------------------------------
    submittedDict = {}
    #Create for Base, Signal region
    sampleList = eval("Samples_%s"%year)
    for sampleName in sampleList.keys():
        nJob = sampleList[sampleName][0]
        for job in range(nJob):
            rootFile = "%s_Skim_%sof%s.root"%(sampleName, job+1, nJob)
            submittedDict[rootFile] = sampleName
    print "Total submitted jobs: %s"%len(submittedDict.keys())

    #----------------------------------------
    #Get all finished jobs
    #----------------------------------------
    finishedList = os.listdir(inHistFullDir)
    print "Total finished jobs: %s"%len(finishedList)

    #----------------------------------------
    #Get all un-finished jobs
    #----------------------------------------
    print "Unfinished jobs: %s\n"%(len(submittedDict.keys()) - len(finishedList))
    unFinishedList = returnNotMatches(finishedList, submittedDict.keys())   
    print unFinishedList

    #----------------------------------------
    #Get finished but corrupted jobs
    #----------------------------------------
    corruptedList = []
    for finished in finishedList:
        fullPath = "%s/%s"%(inHistFullDir, finished)
        sizeInBytes = os.path.getsize(fullPath)
        if sizeInBytes < 3000:
            corruptedList.append(finished)

    print "\nFinished but corrupted jobs: %s"%len(corruptedList)
    for corrupted in corruptedList:
        print corrupted

    #----------------------------------------
    # Check log fils as well
    #----------------------------------------
    grepName = "grep -rn nan %s -A 6 -B 2 "%condorLogDir
    print "\nNan/Inf is propgrated for the following jobs: \n"
    os.system(grepName)

    #----------------------------------------
    #Create jdl file to be resubmitted
    #----------------------------------------
    condorLogDir = "tmpSub/log"
    common_command = \
    'Universe   = vanilla\n\
    should_transfer_files = YES\n\
    when_to_transfer_output = ON_EXIT\n\
    Transfer_Input_Files = Skim_NanoAOD.tar.gz, runMakeSkims.sh\n\
    use_x509userproxy = true\n\
    Output = %s/log_$(cluster)_$(process).stdout\n\
    Error  = %s/log_$(cluster)_$(process).stderr\n\
    Log    = %s/log_$(cluster)_$(process).condor\n\n'%(condorLogDir, condorLogDir, condorLogDir)


    #----------------------------------------
    #Create jdl files
    #----------------------------------------
    if len(unFinishedList) ==0 and len(corruptedList)==0:
        print "Noting to be resubmitted"
    else:
        jdlFileName = 'tmpSub/resubmitJobs_%s.jdl'%(year)
        jdlFile = open(jdlFileName,'w')
        jdlFile.write('Executable =  runMakeSkims.sh \n')
        jdlFile.write(common_command)
        for unFinished in unFinishedList[1]:
            run_command =  \
            'arguments  = %s %s \n\
    queue 1\n\n' %(submittedDict[unFinished], year)
            jdlFile.write(run_command)
        for corrupted in corruptedList:
            run_command =  \
            'arguments  = %s %s \n\
    queue 1\n\n' %(submittedDict[corrupted], year)
            jdlFile.write(run_command)
        print "condor_submit %s"%jdlFileName
        jdlFile.close() 
    print inHistFullDir
