#!/bin/bash
#To be run on remote machine
#Take input arguments as an array
myArray=( "$@" )
#Array: Size=$#, an element=$1, all element = $@

printf "Start Running Histogramming at ";/bin/date
printf "Worker node hostname ";/bin/hostname

if [ -z ${_CONDOR_SCRATCH_DIR} ] ; then 
    echo "Running Interactively" ; 
else
    echo "Running In Batch"
    echo ${_CONDOR_SCRATCH_DIR}
    source /cvmfs/cms.cern.ch/cmsset_default.sh
    export SCRAM_ARCH=slc7_amd64_gcc700
    scramv1 project CMSSW CMSSW_12_6_0
    cd CMSSW_12_6_0/src
    eval `scramv1 runtime -sh`
	cd ../..
	tar --strip-components=1 -xvf Disc_Ntuple.tar.gz
fi

#Run for Base, Signal region
echo "All arguements: "$@
echo "Number of arguements: "$#
python3 reader.py -y $1 -d $2 -c $3 -r $4 -s $5 --method BDTA  --syst $6
printf "Done Histogramming at ";/bin/date

#---------------------------------------------
#Copy the ouput root files
#---------------------------------------------
printf "Copying output files ..."
xrdcp -rf discs/Reader root://cmseos.fnal.gov/$7
rm -r discs
rm -r CMSSW*
printf "Done ";/bin/date