import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *

akCs2PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("slimmedJets"),
    rParam = 0.2,
    fillGenJets = False,
    isMC = False,
    jetName = cms.untracked.string("akCs2PF"),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    )

akFlowPuCs2PFJetAnalyzer = akCs2PFJetAnalyzer.clone()
