### HiForest Configuration
# Input: miniAOD
# Type: data

import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Run2_2018_pp_on_AA_cff import Run2_2018_pp_on_AA
from Configuration.ProcessModifiers.run2_miniAOD_pp_on_AA_103X_cff import run2_miniAOD_pp_on_AA_103X
process = cms.Process('HiForest', Run2_2018_pp_on_AA,run2_miniAOD_pp_on_AA_103X)

###############################################################################

# HiForest info
process.load("HeavyIonsAnalysis.EventAnalysis.HiForestInfo_cfi")
process.HiForestInfo.info = cms.vstring("HiForest, miniAOD, 125X, data")

###############################################################################

# input files
process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    fileNames = cms.untracked.vstring(
        "/store/hidata/HIRun2018A/HIHardProbes/MINIAOD/PbPb18_MiniAODv1-v1/00000/034807c1-0ae5-4540-bb81-80ab2f3bc01d.root"
        #"/store/hidata/HIRun2018A/HISingleMuon/MINIAOD/PbPb18_MiniAODv1-v1/00000/00345f79-641f-4002-baf1-19ae8e83c48b.root"
    ),
)

# number of events to process, set to -1 to process all events
numEvents = 50
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(numEvents)
    )

###############################################################################

# load Global Tag, geometry, etc.
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')


from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data_promptlike_hi', '')
process.HiForestInfo.GlobalTagLabel = process.GlobalTag.globaltag

# This is the default centrality tag built-in in the miniAOD forest.
# The tag is given here for reference. Changing it has no effect on your analysis.
centralityTag = "CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1033p1x01_offline"
process.HiForestInfo.info.append(centralityTag)

print('\n')
print('\033[31m~*~ CENTRALITY TABLE FOR 2018 PBPB DATA ~*~\033[0m')
print('\033[36m~*~ TAG: ' + centralityTag + ' ~*~\033[0m')
print('\n')
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")

process.GlobalTag.toGet.extend([
    cms.PSet(
        record = cms.string("BTagTrackProbability3DRcd"),
        tag = cms.string("JPcalib_Data103X_2018PbPb_v1"),
        connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
        )
    ])

###############################################################################

# root output
process.TFileService = cms.Service("TFileService",
    
    # per tests locali, cosi distinguo numero di eventi
    #fileName = cms.string("HiForestMiniAOD_OnlyCharged_DATA_Dfinder_numEvents"+str(numEvents)+".root"))
    
    # per task di crab
    fileName = cms.string("HiForestMiniAOD_OnlyCharged_DATA_Dfinder.root"))

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
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.skimanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hltobject_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.l1object_cfi')

from HeavyIonsAnalysis.EventAnalysis.hltobject_cfi import trigger_list_data
process.hltobject.triggerNames = trigger_list_data

process.load('HeavyIonsAnalysis.EventAnalysis.particleFlowAnalyser_cfi')
################################
# electrons, photons, muons
SSHIRun2018A = "HeavyIonsAnalysis/EGMAnalysis/data/SSHIRun2018A.dat"
process.load('HeavyIonsAnalysis.EGMAnalysis.correctedElectronProducer_cfi')
process.correctedElectrons.correctionFile = SSHIRun2018A

#process.load('HeavyIonsAnalysis.MuonAnalysis.unpackedMuons_cfi')
#process.load("HeavyIonsAnalysis.MuonAnalysis.muonAnalyzer_cfi")
process.load('HeavyIonsAnalysis.EGMAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.doMuons = cms.bool(False)
process.ggHiNtuplizer.electronSrc = "correctedElectrons"
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
################################
# jet reco sequence
process.load('HeavyIonsAnalysis.JetAnalysis.akCs4PFJetSequence_pponPbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.akCs2PFJetSequence_pponPbPb_data_cff')#aggiunto io
################################
# tracks
process.load("HeavyIonsAnalysis.TrackAnalysis.TrackAnalyzers_cff")
###############################################################################

# ZDC RecHit Producer
process.load('HeavyIonsAnalysis.ZDCAnalysis.QWZDC2018Producer_cfi')
process.load('HeavyIonsAnalysis.ZDCAnalysis.QWZDC2018RecHit_cfi')

process.load('HeavyIonsAnalysis.ZDCAnalysis.zdcanalyzer_cfi')
process.zdcanalyzer.doZDCRecHit = True
process.zdcanalyzer.doZDCDigi = False
process.zdcanalyzer.zdcRecHitSrc = cms.InputTag("QWzdcreco")
process.zdcanalyzer.calZDCDigi = True
################################


###############################################################################
# main forest sequence
process.forest = cms.Path(
    process.HiForestInfo +
    process.hiEvtAnalyzer +
    process.hltanalysis #+
    #process.hltobject +
    #process.l1object +
    #process.trackSequencePbPb +
    #process.particleFlowAnalyser +
    #process.correctedElectrons +
    #process.ggHiNtuplizer +
    #process.zdcdigi +
    #process.QWzdcreco +
    #process.zdcanalyzer #+
    #process.unpackedMuons +
    #process.muonAnalyzer
    )

#customisation

addR2Jets = True
addR2FlowJets = False

addR3Jets = False
addR3FlowJets = False

addR4Jets = True
addR4FlowJets = False

# this is only for non-reclustered jets
addCandidateTagging = False


if addR2Jets or addR2FlowJets or addR3Jets or addR3FlowJets or addR4Jets or addR4FlowJets :
    process.load("HeavyIonsAnalysis.JetAnalysis.extraJets_cff")
    from HeavyIonsAnalysis.JetAnalysis.clusterJetsFromMiniAOD_cff import setupHeavyIonJets
    process.load("HeavyIonsAnalysis.JetAnalysis.candidateBtaggingMiniAOD_cff")
    process.load("RecoHI.HiJetAlgos.PFCandCompositeProducer_cfi")

    if addR2Jets :
        process.jetsR2 = cms.Sequence()
        setupHeavyIonJets('akCs2PF', process.jetsR2, process, isMC = 0, radius = 0.20, JECTag = 'AK2PF', doFlow = False)
        process.akCs2PFpatJetCorrFactors.levels = ['L2Relative', 'L2L3Residual']
        process.akCs2PFJetAnalyzer.jetTag = 'akCs2PFpatJets'
        process.akCs2PFJetAnalyzer.jetName = 'akCs2PF'
        process.forest += process.extraJetsData * process.jetsR2 * process.akCs2PFJetAnalyzer
        process.pfCandComposites.compositeTag = cms.InputTag('Dfinder')
        process.pfCandComposites.removeDKPi = True
        process.akCs2PFJets.src = 'pfCandComposites'#'packedPFCand'#'compositeTag'#'pfCandTag'#'PFCandCompositeProducer
        process.forest.insert(0,process.pfCandComposites)

    if addR2FlowJets :
        process.jetsR2flow = cms.Sequence()
        setupHeavyIonJets('akCs2PFFlow', process.jetsR2flow, process, isMC = 0, radius = 0.20, JECTag = 'AK2PF', doFlow = True)
        process.akCs2PFFlowpatJetCorrFactors.levels = ['L2Relative', 'L2L3Residual']
        process.akFlowPuCs2PFJetAnalyzer.jetTag = 'akCs2PFFlowpatJets'
        process.akFlowPuCs2PFJetAnalyzer.jetName = 'akCs2PFFlow'
        process.forest += process.extraFlowJetsData * process.jetsR2flow * process.akFlowPuCs2PFJetAnalyzer

    if addR3Jets :
        process.jetsR3 = cms.Sequence()
        setupHeavyIonJets('akCs3PF', process.jetsR3, process, isMC = 0, radius = 0.30, JECTag = 'AK3PF', doFlow = False)
        process.akCs3PFpatJetCorrFactors.levels = ['L2Relative', 'L2L3Residual']
        process.akCs3PFJetAnalyzer = process.akCs4PFJetAnalyzer.clone(jetTag = "akCs3PFpatJets", jetName = 'akCs3PF')
        process.forest += process.extraJetsData * process.jetsR3 * process.akCs3PFJetAnalyzer

    if addR3FlowJets :
        process.jetsR3flow = cms.Sequence()
        setupHeavyIonJets('akCs3PFFlow', process.jetsR3flow, process, isMC = 0, radius = 0.30, JECTag = 'AK3PF', doFlow = True)
        process.akCs3PFFlowpatJetCorrFactors.levels = ['L2Relative', 'L2L3Residual']
        process.akFlowPuCs3PFJetAnalyzer = process.akCs4PFJetAnalyzer.clone(jetTag = "akCs3PFFlowpatJets", jetName = 'akCs3PFFlow')
        process.forest += process.extraFlowJetsData * process.jetsR3flow * process.akFlowPuCs3PFJetAnalyzer 

    if addR4Jets :
        # Recluster using an alias "0" in order not to get mixed up with the default AK4 collections
        process.jetsR4 = cms.Sequence()
        setupHeavyIonJets('akCs0PF', process.jetsR4, process, isMC = 0, radius = 0.40, JECTag = 'AK4PF', doFlow = False)
        process.akCs0PFpatJetCorrFactors.levels = ['L2Relative', 'L2L3Residual']
        process.akCs4PFJetAnalyzer.jetTag = 'akCs0PFpatJets'
        process.akCs4PFJetAnalyzer.jetName = 'akCs0PF'
        process.forest += process.extraJetsData * process.jetsR4 * process.akCs4PFJetAnalyzer
        process.pfCandComposites.compositeTag = cms.InputTag('Dfinder')
        process.pfCandComposites.removeDKPi = True
        process.akCs0PFJets.src = 'pfCandComposites'#'packedPFCand'#'compositeTag'#'pfCandTag'#'PFCandCompositeProducer
        process.forest.insert(0,process.pfCandComposites)

    if addR4FlowJets :
        process.jetsR4flow = cms.Sequence()
        setupHeavyIonJets('akCs4PFFlow', process.jetsR4flow, process, isMC = 0, radius = 0.40, JECTag = 'AK4PF', doFlow = True)
        process.akCs4PFFlowpatJetCorrFactors.levels = ['L2Relative', 'L2L3Residual']
        process.akFlowPuCs4PFJetAnalyzer.jetTag = 'akCs4PFFlowpatJets'
        process.akFlowPuCs4PFJetAnalyzer.jetName = 'akCs4PFFlow'
        process.forest += process.extraFlowJetsData * process.jetsR4flow * process.akFlowPuCs4PFJetAnalyzer


if addCandidateTagging:
    process.load("HeavyIonsAnalysis.JetAnalysis.candidateBtaggingMiniAOD_cff")

    from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
    updateJetCollection(
        process,
        jetSource = cms.InputTag('slimmedJets'),
        jetCorrections = ('AK4PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
        btagDiscriminators = ['pfCombinedSecondaryVertexV2BJetTags', 'pfDeepCSVDiscriminatorsJetTags:BvsAll', 'pfDeepCSVDiscriminatorsJetTags:CvsB', 'pfDeepCSVDiscriminatorsJetTags:CvsL'], ## to add discriminators,
        btagPrefix = 'TEST',
    )

    process.updatedPatJets.addJetCorrFactors = False
    process.updatedPatJets.discriminatorSources = cms.VInputTag(
        cms.InputTag('pfDeepCSVJetTags:probb'),
        cms.InputTag('pfDeepCSVJetTags:probc'),
        cms.InputTag('pfDeepCSVJetTags:probudsg'),
        cms.InputTag('pfDeepCSVJetTags:probbb'),
    )

    process.akCs4PFJetAnalyzer.jetTag = "updatedPatJets"

    process.forest.insert(1,process.candidateBtagging*process.updatedPatJets)


#########################
# Event Selection -> add the needed filters here
#########################

process.load('HeavyIonsAnalysis.EventAnalysis.collisionEventSelection_cff')
process.pclusterCompatibilityFilter = cms.Path(process.clusterCompatibilityFilter)
process.pprimaryVertexFilter = cms.Path(process.primaryVertexFilter)
process.load('HeavyIonsAnalysis.EventAnalysis.hffilter_cfi')
process.pphfCoincFilter2Th4 = cms.Path(process.phfCoincFilter2Th4)
process.pAna = cms.EndPath(process.skimanalysis)

#################### D/B finder ################# 
AddCaloMuon = False 
runOnMC = False ## !!
HIFormat = False 
UseGenPlusSim = False 
# VtxLabel = "unpackedTracksAndVertices"
VtxLabel = "offlineSlimmedPrimaryVerticesRecovery"
TrkLabel = "packedPFCandidates"
GenLabel = "prunedGenParticles"
TrkChi2Label = "packedPFCandidateTrackChi2"
useL1Stage2 = True
HLTProName = "HLT"
from Bfinder.finderMaker.finderMaker_75X_cff import finderMaker_75X 
finderMaker_75X(process, AddCaloMuon, runOnMC, HIFormat, UseGenPlusSim, VtxLabel, TrkLabel, TrkChi2Label, GenLabel, useL1Stage2, HLTProName)
process.Dfinder.MVAMapLabel = cms.InputTag(TrkLabel, "MVAValues")
process.Dfinder.makeDntuple = cms.bool(True)
process.Dfinder.tkPtCut = cms.double(2.0) # before fit
process.Dfinder.tkEtaCut = cms.double(2.4) # before fit
process.Dfinder.dPtCut = cms.vdouble(4.0, 4.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0) # before fit
process.Dfinder.VtxChiProbCut = cms.vdouble(0.05, 0.05, 0.0, 0.0, 0.0, 0.0, 0.05, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.05, 0.05)
process.Dfinder.dCutSeparating_PtVal = cms.vdouble(5., 5., 5., 5., 5., 5., 5., 5., 5., 5., 5., 5., 5., 5., 5., 5.)
process.Dfinder.tktkRes_svpvDistanceCut_lowptD = cms.vdouble(0., 0., 0., 0., 0., 0., 0., 0., 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 0., 0.)
process.Dfinder.tktkRes_svpvDistanceCut_highptD = cms.vdouble(0., 0., 0., 0., 0., 0., 0., 0., 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 0., 0.)
process.Dfinder.svpvDistanceCut_lowptD = cms.vdouble(2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 0., 0., 0., 0., 0., 0., 2.5, 2.5)
process.Dfinder.svpvDistanceCut_highptD = cms.vdouble(2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 0., 0., 0., 0., 0., 0., 2.5, 2.5)
process.Dfinder.Dchannel = cms.vint32(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
process.Dfinder.dropUnusedTracks = cms.bool(True)
process.Dfinder.detailMode = cms.bool(False)

process.dfinder = cms.Path(process.DfinderSequence)


###############################
#import FWCore.ParameterSet.VarParsing as VarParsing
#ivars = VarParsing.VarParsing('analysis')

#ivars.maxEvents = 1000 #-1 #tutti
#ivars.outputFile='HiForestMiniAOD_OnlyCharged_DATA_SD_ParticleJetCut1Gev.root'
#ivars.inputFiles='/store/hidata/HIRun2018A/HIHardProbes/MINIAOD/PbPb18_MiniAODv1-v1/00000/034807c1-0ae5-4540-bb81-80ab2f3bc01d.root'
#ivars.parseArguments() # get and parse the command line arguments

#process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring(ivars.inputFiles),
#    eventsToProcess = cms.untracked.VEventRange('1:236:29748033-1:236:29748033')
#)

#process.maxEvents = cms.untracked.PSet(
#    input = cms.untracked.int32(ivars.maxEvents)
#)

#process.TFileService = cms.Service("TFileService",
#    fileName = cms.string(ivars.outputFile)
#)