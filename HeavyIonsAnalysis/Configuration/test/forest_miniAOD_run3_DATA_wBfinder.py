### HiForest Configuration
# Input: miniAOD
# Type: data

import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')

###############################################################################

# HiForest info
process.load("HeavyIonsAnalysis.EventAnalysis.HiForestInfo_cfi")
process.HiForestInfo.info = cms.vstring("HiForest, miniAOD, 125X, data")

# import subprocess, os
# version = subprocess.check_output(
#     ['git', '-C', os.path.expandvars('$CMSSW_BASE/src'), 'describe', '--tags'])
# if version == '':
#     version = 'no git info'
# process.HiForestInfo.HiForestVersion = cms.string(version)

###############################################################################

# input files
process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    fileNames = cms.untracked.vstring(
        '/store/group/phys_heavyions/mnguyen/HIRun2022A/RecoPatfromRaw_RAW2DIGI_L1Reco_RECO_PAT_inMINIAOD.root',
    ), 
)

# number of events to process, set to -1 to process all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

###############################################################################

# load Global Tag, geometry, etc.
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')


from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '125X_dataRun3_relval_v4', '')
process.HiForestInfo.GlobalTagLabel = process.GlobalTag.globaltag

#centralityTag = "CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1031x02_offline"
#process.HiForestInfo.info.append(centralityTag)
#
#print('\n')
#print('\033[31m~*~ CENTRALITY TABLE FOR 2018 PBPB DATA ~*~\033[0m')
#print('\033[36m~*~ TAG: ' + centralityTag + ' ~*~\033[0m')
#print('\n')
#process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
#process.GlobalTag.toGet.extend([
#    cms.PSet(
#        record = cms.string("HeavyIonRcd"),
#        tag = cms.string(centralityTag),
#        label = cms.untracked.string("HFtowers"),
#        connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
#        ),
#    ])
#
#process.GlobalTag.toGet.extend([
#    cms.PSet(
#        record = cms.string("BTagTrackProbability3DRcd"),
#        tag = cms.string("JPcalib_Data103X_2018PbPb_v1"),
#        connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
#        )
#    ])
#
###############################################################################

# root output
process.TFileService = cms.Service("TFileService",
    fileName = cms.string("HiForestMiniAOD.root"))

# # edm output for debugging purposes
# process.output = cms.OutputModule(
#     "PoolOutputModule",
#     fileName = cms.untracked.string('HiForestEDM.root'),
#     outputCommands = cms.untracked.vstring(
#         'keep *',
#         )
#     )

# process.output_path = cms.EndPath(process.output)

###############################################################################

# event analysis
# process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi')
#process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.skimanalysis_cfi')
#process.load('HeavyIonsAnalysis.EventAnalysis.hltobject_cfi')
#process.load('HeavyIonsAnalysis.EventAnalysis.l1object_cfi')

#from HeavyIonsAnalysis.EventAnalysis.hltobject_cfi import trigger_list_mc
#process.hltobject.triggerNames = trigger_list_mc

process.load('HeavyIonsAnalysis.EventAnalysis.particleFlowAnalyser_cfi')
################################
# electrons, photons, muons
process.load('HeavyIonsAnalysis.EGMAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.doMuons = cms.bool(False)
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
################################
# jet reco sequence
process.load('HeavyIonsAnalysis.JetAnalysis.akCs4PFJetSequence_pponPbPb_data_cff')
################################
# tracks
process.load("HeavyIonsAnalysis.TrackAnalysis.TrackAnalyzers_cff")
# muons (FTW)
process.load("HeavyIonsAnalysis.MuonAnalysis.unpackedMuons_cfi")
process.load("HeavyIonsAnalysis.MuonAnalysis.muonAnalyzer_cfi")
###############################################################################



###############################################################################
# main forest sequence
process.forest = cms.Path(
    process.HiForestInfo + 
    # process.hltanalysis +
    process.trackSequencePbPb +
    process.particleFlowAnalyser +
    process.hiEvtAnalyzer +
    #process.ggHiNtuplizer +
    process.akCs4PFJetAnalyzer +
    process.unpackedMuons +
    process.muonAnalyzer
    )

#customisation



#########################
# Event Selection -> add the needed filters here
#########################

process.load('HeavyIonsAnalysis.EventAnalysis.collisionEventSelection_cff')
process.pclusterCompatibilityFilter = cms.Path(process.clusterCompatibilityFilter)
process.pprimaryVertexFilter = cms.Path(process.primaryVertexFilter)
process.pAna = cms.EndPath(process.skimanalysis)

from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel
process.hltfilter = hltHighLevel.clone(
    HLTPaths = [
        #"HLT_HIZeroBias_v4",                                                     
        "HLT_HIMinimumBias_v2",
    ]
)
process.filterSequence = cms.Sequence(
    process.hltfilter
)

process.superFilterPath = cms.Path(process.filterSequence)
process.skimanalysis.superFilters = cms.vstring("superFilterPath")

for path in process.paths:
    getattr(process, path)._seq = process.filterSequence * getattr(process,path)._seq


#################### D/B finder #################
AddCaloMuon = False
runOnMC = False ## !!
HIFormat = False
UseGenPlusSim = False
# VtxLabel = "unpackedTracksAndVertices"
VtxLabel = "offlineSlimmedPrimaryVerticesRecovery"
TrkLabel = "packedPFCandidates"
GenLabel = "prunedGenParticles"
useL1Stage2 = True
HLTProName = "HLT"
from Bfinder.finderMaker.finderMaker_75X_cff import finderMaker_75X
finderMaker_75X(process, AddCaloMuon, runOnMC, HIFormat, UseGenPlusSim, VtxLabel, TrkLabel, GenLabel, useL1Stage2, HLTProName)

process.Bfinder.MVAMapLabel = cms.InputTag(TrkLabel,"MVAValues")
process.Bfinder.makeBntuple = cms.bool(True)
process.Bfinder.tkPtCut = cms.double(0.8) # before fit
process.Bfinder.tkEtaCut = cms.double(2.4) # before fit
process.Bfinder.jpsiPtCut = cms.double(0.0) # before fit
process.Bfinder.bPtCut = cms.vdouble(3.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0) # before fit
process.Bfinder.Bchannel = cms.vint32(1, 0, 0, 1, 1, 1, 1)
process.Bfinder.VtxChiProbCut = cms.vdouble(0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10)
process.Bfinder.svpvDistanceCut = cms.vdouble(2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 0.0)
process.Bfinder.doTkPreCut = cms.bool(True)
process.Bfinder.doMuPreCut = cms.bool(True)
process.Bfinder.MuonTriggerMatchingPath = cms.vstring(
    "HLT_HIL3Mu0NHitQ10_L2Mu0_MAXdR3p5_M1to5_v1")
process.Bfinder.MuonTriggerMatchingFilter = cms.vstring(
    "hltL3f0L3Mu0L2Mu0DR3p5FilteredNHitQ10M1to5")
process.p = cms.Path(process.BfinderSequence)



###############################
import FWCore.ParameterSet.VarParsing as VarParsing
ivars = VarParsing.VarParsing('analysis')

ivars.maxEvents = -1
ivars.outputFile='HiForestMINIAOD.root'
ivars.inputFiles='file:/afs/cern.ch/work/w/wangj/public/Pythia8_DzeroToKPi_prompt_Pthat15_TuneCP5_5020GeV_Drum5F/step3_reco.root'
ivars.parseArguments() # get and parse the command line arguments

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(ivars.inputFiles),
    # eventsToProcess = cms.untracked.VEventRange('1:236:29748033-1:236:29748033')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(ivars.maxEvents)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(ivars.outputFile))

