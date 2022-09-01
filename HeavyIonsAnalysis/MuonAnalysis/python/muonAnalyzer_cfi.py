import FWCore.ParameterSet.Config as cms

muonAnalyzer = cms.EDAnalyzer("MuonAnalyzer",
                           muonSrc = cms.InputTag("unpackedMuons"),
                           vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                           doReco = cms.untracked.bool(True),
                           doGen = cms.bool(False),
                           genparticle = cms.InputTag("packedGenParticles"),
                           simtrack = cms.InputTag("mergedtruth","MergedTrackTruth"),
)

from HeavyIonsAnalysis.TrackAnalysis.unpackedTracksAndVertices_cfi import unpackedTracksAndVertices
from HeavyIonsAnalysis.MuonAnalysis.unpackedMuons_cfi import unpackedMuons

muonSequence = cms.Sequence(unpackedTracksAndVertices + unpackedMuons + muonAnalyzer)