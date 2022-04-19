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
    scramv1 project CMSSW CMSSW_10_2_14
    cd CMSSW_10_2_14/src
    eval `scramv1 runtime -sh`
	cd ../..
	tar --strip-components=1 -zxvf HistSF.tar.gz
fi

#Run for Base, Signal region
echo "All arguements: "$@
echo "Number of arguements: "$#
python runMakeHists.py -y $1 -d $2 -c $3 -s $4 --syst $5 --level $6 
printf "Done Histogramming at ";/bin/date

#---------------------------------------------
#Copy the ouput root files
#---------------------------------------------
printf "Copying output files ..."
condorOutDir=/store/user/rverma/Output/cms-TT-run2/CBA_Ntuple/Hist_Ntuple/HistSF/Raw
xrdcp -rf hists/$1/$2/$3/*.root root://cmseos.fnal.gov/$condorOutDir/$1/$2/$3/ 
printf "Done ";/bin/date