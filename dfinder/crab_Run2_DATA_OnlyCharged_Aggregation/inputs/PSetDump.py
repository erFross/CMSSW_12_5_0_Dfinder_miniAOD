import FWCore.ParameterSet.Config as cms
from HeterogeneousCore.CUDACore.SwitchProducerCUDA import SwitchProducerCUDA

process = cms.Process("HiForest")

process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    fileNames = cms.untracked.vstring('/store/hidata/HIRun2018A/HIHardProbes/MINIAOD/PbPb18_MiniAODv1-v1/00000/034807c1-0ae5-4540-bb81-80ab2f3bc01d.root')
)
process.CondDB = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionTimeout = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('')
)

process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(
        0.004123, 0.00602, 0.008201, 0.010489, 0.013379,
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807,
        0.058939, 0.125497
    ),
    HFdepthOneParameterB = cms.vdouble(
        -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05,
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107,
        0.000425, 0.000209
    ),
    HFdepthTwoParameterA = cms.vdouble(
        0.002861, 0.004168, 0.0064, 0.008388, 0.011601,
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447,
        0.051579, 0.086593
    ),
    HFdepthTwoParameterB = cms.vdouble(
        -2e-06, -0.0, -7e-06, -6e-06, -2e-06,
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05,
        0.000157, -3e-06
    )
)

process.METSignificanceParams = cms.PSet(
    dRMatch = cms.double(0.4),
    jetThreshold = cms.double(15),
    jeta = cms.vdouble(0.8, 1.3, 1.9, 2.5),
    jpar = cms.vdouble(1.39, 1.26, 1.21, 1.23, 1.28),
    pjpar = cms.vdouble(-0.2586, 0.6173)
)

process.calibratedEgammaPatSettings = cms.PSet(
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Run2018_29Sep2020_RunFineEtaR9Gain'),
    minEtToCalibrate = cms.double(5.0),
    produceCalibratedObjs = cms.bool(True),
    recHitCollectionEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    recHitCollectionEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
    semiDeterministic = cms.bool(True)
)

process.calibratedEgammaSettings = cms.PSet(
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Run2018_29Sep2020_RunFineEtaR9Gain'),
    minEtToCalibrate = cms.double(5.0),
    produceCalibratedObjs = cms.bool(True),
    recHitCollectionEB = cms.InputTag("reducedEcalRecHitsEB"),
    recHitCollectionEE = cms.InputTag("reducedEcalRecHitsEE"),
    semiDeterministic = cms.bool(True)
)

process.combinedSecondaryVertexCommon = cms.PSet(
    SoftLeptonFlip = cms.bool(False),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)

process.ecalTrkCombinationRegression = cms.PSet(
    ecalTrkRegressionConfig = cms.PSet(
        ebHighEtForestName = cms.ESInputTag("","electron_eb_ECALTRK"),
        ebLowEtForestName = cms.ESInputTag("","electron_eb_ECALTRK_lowpt"),
        eeHighEtForestName = cms.ESInputTag("","electron_ee_ECALTRK"),
        eeLowEtForestName = cms.ESInputTag("","electron_ee_ECALTRK_lowpt"),
        forceHighEnergyTrainingIfSaturated = cms.bool(False),
        lowEtHighEtBoundary = cms.double(50.0),
        rangeMaxHighEt = cms.double(3.0),
        rangeMaxLowEt = cms.double(3.0),
        rangeMinHighEt = cms.double(-1.0),
        rangeMinLowEt = cms.double(-1.0)
    ),
    ecalTrkRegressionUncertConfig = cms.PSet(
        ebHighEtForestName = cms.ESInputTag("","electron_eb_ECALTRK_var"),
        ebLowEtForestName = cms.ESInputTag("","electron_eb_ECALTRK_lowpt_var"),
        eeHighEtForestName = cms.ESInputTag("","electron_ee_ECALTRK_var"),
        eeLowEtForestName = cms.ESInputTag("","electron_ee_ECALTRK_lowpt_var"),
        forceHighEnergyTrainingIfSaturated = cms.bool(False),
        lowEtHighEtBoundary = cms.double(50.0),
        rangeMaxHighEt = cms.double(0.5),
        rangeMaxLowEt = cms.double(0.5),
        rangeMinHighEt = cms.double(0.0002),
        rangeMinLowEt = cms.double(0.0002)
    ),
    maxEPDiffInSigmaForComb = cms.double(15.0),
    maxEcalEnergyForComb = cms.double(200.0),
    maxRelTrkMomErrForComb = cms.double(10.0),
    minEOverPForComb = cms.double(0.025)
)

process.egammaHBHERecHit = cms.PSet(
    hbheRecHits = cms.InputTag("hbhereco"),
    maxHcalRecHitSeverity = cms.int32(9),
    recHitEThresholdHB = cms.vdouble(0.1, 0.2, 0.3, 0.3),
    recHitEThresholdHE = cms.vdouble(
        0.1, 0.2, 0.2, 0.2, 0.2,
        0.2, 0.2
    )
)

process.isolationSumsCalculator = cms.PSet(
    ComponentName = cms.string('isolationSumsCalculator'),
    EcalRecHitEtaSliceA_Barrel = cms.double(2.5),
    EcalRecHitEtaSliceA_Endcap = cms.double(2.5),
    EcalRecHitEtaSliceB_Barrel = cms.double(2.5),
    EcalRecHitEtaSliceB_Endcap = cms.double(2.5),
    EcalRecHitInnerRadiusA_Barrel = cms.double(3.5),
    EcalRecHitInnerRadiusA_Endcap = cms.double(3.5),
    EcalRecHitInnerRadiusB_Barrel = cms.double(3.5),
    EcalRecHitInnerRadiusB_Endcap = cms.double(3.5),
    EcalRecHitOuterRadiusA_Barrel = cms.double(0.4),
    EcalRecHitOuterRadiusA_Endcap = cms.double(0.4),
    EcalRecHitOuterRadiusB_Barrel = cms.double(0.3),
    EcalRecHitOuterRadiusB_Endcap = cms.double(0.3),
    EcalRecHitThreshEA_Barrel = cms.double(0.095),
    EcalRecHitThreshEA_Endcap = cms.double(0.0),
    EcalRecHitThreshEB_Barrel = cms.double(0.095),
    EcalRecHitThreshEB_Endcap = cms.double(0.0),
    EcalRecHitThreshEtA_Barrel = cms.double(0.0),
    EcalRecHitThreshEtA_Endcap = cms.double(0.11),
    EcalRecHitThreshEtB_Barrel = cms.double(0.0),
    EcalRecHitThreshEtB_Endcap = cms.double(0.11),
    HBHERecHitCollection = cms.InputTag("hbhereco"),
    HcalRecHitInnerRadiusA_Barrel = cms.vdouble(
        0.15, 0.15, 0.15, 0.15, 0.15,
        0.15, 0.15
    ),
    HcalRecHitInnerRadiusA_Endcap = cms.vdouble(
        0.15, 0.15, 0.15, 0.15, 0.15,
        0.15, 0.15
    ),
    HcalRecHitInnerRadiusB_Barrel = cms.vdouble(
        0.15, 0.15, 0.15, 0.15, 0.15,
        0.15, 0.15
    ),
    HcalRecHitInnerRadiusB_Endcap = cms.vdouble(
        0.15, 0.15, 0.15, 0.15, 0.15,
        0.15, 0.15
    ),
    HcalRecHitOuterRadiusA_Barrel = cms.vdouble(
        0.4, 0.4, 0.4, 0.4, 0.4,
        0.4, 0.4
    ),
    HcalRecHitOuterRadiusA_Endcap = cms.vdouble(
        0.4, 0.4, 0.4, 0.4, 0.4,
        0.4, 0.4
    ),
    HcalRecHitOuterRadiusB_Barrel = cms.vdouble(
        0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3
    ),
    HcalRecHitOuterRadiusB_Endcap = cms.vdouble(
        0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3
    ),
    TrackConeInnerRadiusA_Barrel = cms.double(0.04),
    TrackConeInnerRadiusA_Endcap = cms.double(0.04),
    TrackConeInnerRadiusB_Barrel = cms.double(0.04),
    TrackConeInnerRadiusB_Endcap = cms.double(0.04),
    TrackConeOuterRadiusA_Barrel = cms.double(0.4),
    TrackConeOuterRadiusA_Endcap = cms.double(0.4),
    TrackConeOuterRadiusB_Barrel = cms.double(0.3),
    TrackConeOuterRadiusB_Endcap = cms.double(0.3),
    barrelEcalRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    beamSpotProducer = cms.InputTag("offlineBeamSpot"),
    endcapEcalRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    isolationtrackEtaSliceA_Barrel = cms.double(0.015),
    isolationtrackEtaSliceA_Endcap = cms.double(0.015),
    isolationtrackEtaSliceB_Barrel = cms.double(0.015),
    isolationtrackEtaSliceB_Endcap = cms.double(0.015),
    isolationtrackThresholdA_Barrel = cms.double(0.0),
    isolationtrackThresholdA_Endcap = cms.double(0.0),
    isolationtrackThresholdB_Barrel = cms.double(0.0),
    isolationtrackThresholdB_Endcap = cms.double(0.0),
    longImpactParameterA_Barrel = cms.double(0.2),
    longImpactParameterA_Endcap = cms.double(0.2),
    longImpactParameterB_Barrel = cms.double(0.2),
    longImpactParameterB_Endcap = cms.double(0.2),
    maxHcalRecHitSeverity = cms.int32(9),
    moduleEtaBoundary = cms.vdouble(
        0.0, 0.02, 0.43, 0.46, 0.78,
        0.81, 1.13, 1.15, 1.45, 1.58
    ),
    modulePhiBoundary = cms.double(0.0087),
    recHitEThresholdHB = cms.vdouble(0.1, 0.2, 0.3, 0.3),
    recHitEThresholdHE = cms.vdouble(
        0.1, 0.2, 0.2, 0.2, 0.2,
        0.2, 0.2
    ),
    trackProducer = cms.InputTag("generalTracks"),
    transImpactParameterA_Barrel = cms.double(0.1),
    transImpactParameterA_Endcap = cms.double(0.1),
    transImpactParameterB_Barrel = cms.double(0.1),
    transImpactParameterB_Endcap = cms.double(0.1),
    useNumCrystals = cms.bool(True),
    vetoClustered = cms.bool(False)
)

process.j2tParametersCALO = cms.PSet(
    coneSize = cms.double(0.4),
    extrapolations = cms.InputTag("trackExtrapolator"),
    trackQuality = cms.string('goodIterative'),
    tracks = cms.InputTag("generalTracks")
)

process.j2tParametersVX = cms.PSet(
    coneSize = cms.double(0.4),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(50),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.maxLuminosityBlocks = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.nanoDQMIO_perLSoutput = cms.PSet(
    MEsToSave = cms.untracked.vstring(
        'DT/02-Segments/03-MeanT0/T0MeanAllWheels',
        'EcalBarrel/EBOccupancyTask/EBOT digi occupancy',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +',
        'Muons/MuonRecoAnalyzer/',
        'Muons/MuonIdDQM/GlobalMuons/',
        'PixelPhase1/Phase1_MechanicalView/',
        'PixelPhase1/Tracks/',
        'SiStrip/MechanicalView/',
        'Tracking/PrimaryVertices/highPurityTracks/pt_0to1/offline/',
        'Tracking/TrackParameters/generalTracks/LSanalysis/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/LSanalysis/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/LSanalysis/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/LSanalysis/',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/GeneralProperties/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/GeneralProperties/',
        'Tracking/TrackParameters/generalTracks/HitProperties/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/HitProperties/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/HitProperties/',
        'Tracking/TrackParameters/generalTracks/HitProperties/Pixel/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/Pixel/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/HitProperties/Pixel/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/HitProperties/Pixel/',
        'Tracking/TrackParameters/generalTracks/HitProperties/Strip/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/Strip/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/HitProperties/Strip/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/HitProperties/Strip/'
    )
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

process.trackPseudoSelectionBlock = cms.PSet(
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)

process.trackSelectionBlock = cms.PSet(
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)

process.variableJTAPars = cms.PSet(
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5)
)

process.vertexCutsBlock = cms.PSet(
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    )
)

process.vertexRecoBlock = cms.PSet(
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    )
)

process.vertexSelectionBlock = cms.PSet(
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)

process.vertexTrackSelectionBlock = cms.PSet(
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)

process.ZDC2018Pedestal_0 = cms.VPSet(
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM0'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM1'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM2'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM3'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM4'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM5'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM6'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM7'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM8'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM9'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM10'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM11'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM12'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM13'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM14'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM15'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD0'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD1'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD2'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD3'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD4'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD5'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD6'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD7'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD8'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD9'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD10'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD11'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD12'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD13'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD14'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD15'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM0'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM1'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM2'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM3'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM4'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM5'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM6'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM7'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM8'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM9'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM10'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM11'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM12'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM13'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM14'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM15'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD0'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD1'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD2'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD3'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD4'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD5'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD6'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD7'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD8'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD9'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD10'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD11'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD12'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD13'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD14'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD15'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD0'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD1'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD2'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD3'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD4'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD5'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD6'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD7'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD8'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD9'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD10'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD11'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD12'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD13'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD14'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD15'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD0'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD1'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD2'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD3'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD4'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD5'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD6'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD7'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD8'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD9'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD10'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD11'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD12'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD13'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD14'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ),
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD15'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    )
)

process.gainFill7435 = cms.VPSet(
    cms.PSet(
        calib = cms.untracked.double(0.11),
        object = cms.untracked.string('hZDCP_EM1')
    ),
    cms.PSet(
        calib = cms.untracked.double(0.11),
        object = cms.untracked.string('hZDCP_EM2')
    ),
    cms.PSet(
        calib = cms.untracked.double(0.08),
        object = cms.untracked.string('hZDCP_EM3')
    ),
    cms.PSet(
        calib = cms.untracked.double(0.1),
        object = cms.untracked.string('hZDCP_EM4')
    ),
    cms.PSet(
        calib = cms.untracked.double(0.06),
        object = cms.untracked.string('hZDCP_EM5')
    ),
    cms.PSet(
        calib = cms.untracked.double(1.0),
        object = cms.untracked.string('hZDCP_HAD1')
    ),
    cms.PSet(
        calib = cms.untracked.double(0.61),
        object = cms.untracked.string('hZDCP_HAD2')
    ),
    cms.PSet(
        calib = cms.untracked.double(0.46),
        object = cms.untracked.string('hZDCP_HAD3')
    ),
    cms.PSet(
        calib = cms.untracked.double(0.52),
        object = cms.untracked.string('hZDCP_HAD4')
    ),
    cms.PSet(
        calib = cms.untracked.double(0.12),
        object = cms.untracked.string('hZDCM_EM1')
    ),
    cms.PSet(
        calib = cms.untracked.double(0.12),
        object = cms.untracked.string('hZDCM_EM2')
    ),
    cms.PSet(
        calib = cms.untracked.double(0.08),
        object = cms.untracked.string('hZDCM_EM3')
    ),
    cms.PSet(
        calib = cms.untracked.double(0.1),
        object = cms.untracked.string('hZDCM_EM4')
    ),
    cms.PSet(
        calib = cms.untracked.double(0.11),
        object = cms.untracked.string('hZDCM_EM5')
    ),
    cms.PSet(
        calib = cms.untracked.double(1.0),
        object = cms.untracked.string('hZDCM_HAD1')
    ),
    cms.PSet(
        calib = cms.untracked.double(0.81),
        object = cms.untracked.string('hZDCM_HAD2')
    ),
    cms.PSet(
        calib = cms.untracked.double(0.46),
        object = cms.untracked.string('hZDCM_HAD3')
    ),
    cms.PSet(
        calib = cms.untracked.double(0.58),
        object = cms.untracked.string('hZDCM_HAD4')
    ),
    cms.PSet(
        calib = cms.untracked.double(2.67),
        object = cms.untracked.string('Pscale')
    ),
    cms.PSet(
        calib = cms.untracked.double(4.45),
        object = cms.untracked.string('Mscale')
    )
)

process.heavyIonCSV_vpset = cms.VPSet(
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackSip3dSig_0'),
        taggingVarName = cms.string('trackSip3dSig')
    ),
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackSip3dSig_1'),
        taggingVarName = cms.string('trackSip3dSig')
    ),
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackSip3dSig_2'),
        taggingVarName = cms.string('trackSip3dSig')
    ),
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackSip3dSig_3'),
        taggingVarName = cms.string('trackSip3dSig')
    ),
    cms.PSet(
        default = cms.double(-999),
        name = cms.string('TagVarCSV_trackSip3dSigAboveCharm'),
        taggingVarName = cms.string('trackSip3dSigAboveCharm')
    ),
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackPtRel_0'),
        taggingVarName = cms.string('trackPtRel')
    ),
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackPtRel_1'),
        taggingVarName = cms.string('trackPtRel')
    ),
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackPtRel_2'),
        taggingVarName = cms.string('trackPtRel')
    ),
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackPtRel_3'),
        taggingVarName = cms.string('trackPtRel')
    ),
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackEtaRel_0'),
        taggingVarName = cms.string('trackEtaRel')
    ),
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackEtaRel_1'),
        taggingVarName = cms.string('trackEtaRel')
    ),
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackEtaRel_2'),
        taggingVarName = cms.string('trackEtaRel')
    ),
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackEtaRel_3'),
        taggingVarName = cms.string('trackEtaRel')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackDeltaR_0'),
        taggingVarName = cms.string('trackDeltaR')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackDeltaR_1'),
        taggingVarName = cms.string('trackDeltaR')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackDeltaR_2'),
        taggingVarName = cms.string('trackDeltaR')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackDeltaR_3'),
        taggingVarName = cms.string('trackDeltaR')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackPtRatio_0'),
        taggingVarName = cms.string('trackPtRatio')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackPtRatio_1'),
        taggingVarName = cms.string('trackPtRatio')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackPtRatio_2'),
        taggingVarName = cms.string('trackPtRatio')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackPtRatio_3'),
        taggingVarName = cms.string('trackPtRatio')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackJetDist_0'),
        taggingVarName = cms.string('trackJetDist')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackJetDist_1'),
        taggingVarName = cms.string('trackJetDist')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackJetDist_2'),
        taggingVarName = cms.string('trackJetDist')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackJetDist_3'),
        taggingVarName = cms.string('trackJetDist')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackDecayLenVal_0'),
        taggingVarName = cms.string('trackDecayLenVal')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackDecayLenVal_1'),
        taggingVarName = cms.string('trackDecayLenVal')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackDecayLenVal_2'),
        taggingVarName = cms.string('trackDecayLenVal')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackDecayLenVal_3'),
        taggingVarName = cms.string('trackDecayLenVal')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('TagVarCSV_trackSumJetEtRatio'),
        taggingVarName = cms.string('trackSumJetEtRatio')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('TagVarCSV_trackSumJetDeltaR'),
        taggingVarName = cms.string('trackSumJetDeltaR')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('TagVarCSV_vertexMass'),
        taggingVarName = cms.string('vertexMass')
    ),
    cms.PSet(
        default = cms.double(0),
        name = cms.string('TagVarCSV_vertexNTracks'),
        taggingVarName = cms.string('vertexNTracks')
    ),
    cms.PSet(
        default = cms.double(-10),
        name = cms.string('TagVarCSV_vertexEnergyRatio'),
        taggingVarName = cms.string('vertexEnergyRatio')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('TagVarCSV_vertexJetDeltaR'),
        taggingVarName = cms.string('vertexJetDeltaR')
    ),
    cms.PSet(
        default = cms.double(-1),
        name = cms.string('TagVarCSV_flightDistance2dSig'),
        taggingVarName = cms.string('flightDistance2dSig')
    ),
    cms.PSet(
        default = cms.double(0),
        name = cms.string('TagVarCSV_jetNSecondaryVertices'),
        taggingVarName = cms.string('jetNSecondaryVertices')
    ),
    cms.PSet(
        default = cms.double(0),
        name = cms.string('TagVarCSV_vertexCategory'),
        taggingVarName = cms.string('vertexCategory')
    )
)

process.Bfinder = cms.EDProducer("Bfinder",
    BSLabel = cms.InputTag("offlineBeamSpot"),
    Bchannel = cms.vint32(
        1, 0, 0, 0, 0,
        0, 0
    ),
    GenLabel = cms.InputTag("prunedGenParticles"),
    HLTLabel = cms.InputTag("TriggerResults","","HLT"),
    MaxDocaCut = cms.vdouble(
        999.0, 999.0, 999.0, 999.0, 999.0,
        999.0, 999.0
    ),
    MuonLabel = cms.InputTag("patMuonsWithTrigger"),
    MuonTriggerMatchingFilter = cms.vstring(''),
    MuonTriggerMatchingPath = cms.vstring(''),
    PUInfoLabel = cms.InputTag("addPileupInfo"),
    PVLabel = cms.InputTag("offlineSlimmedPrimaryVerticesRecovery"),
    RunOnMC = cms.bool(False),
    TrackLabel = cms.InputTag("packedPFCandidates"),
    VtxChiProbCut = cms.vdouble(
        0.01, 0.01, 0.01, 0.01, 0.01,
        0.01, 0.01
    ),
    alphaCut = cms.vdouble(
        999.0, 999.0, 999.0, 999.0, 999.0,
        999.0, 999.0
    ),
    bEtaCut = cms.vdouble(
        2.4, 2.4, 2.4, 2.4, 2.4,
        2.4, 2.4
    ),
    bPtCut = cms.vdouble(
        5.0, 5.0, 5.0, 5.0, 5.0,
        5.0, 5.0
    ),
    detailMode = cms.bool(True),
    doBntupleSkim = cms.bool(False),
    doMuPreCut = cms.bool(True),
    doTkPreCut = cms.bool(True),
    dropUnusedTracks = cms.bool(True),
    jpsiPtCut = cms.double(0.0),
    makeBntuple = cms.bool(True),
    printInfo = cms.bool(True),
    svpvDistanceCut = cms.vdouble(
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0
    ),
    tkEtaCut = cms.double(999.0),
    tkPtCut = cms.double(1.0),
    uj_VtxChiProbCut = cms.double(0.01)
)


process.Dfinder = cms.EDProducer("Dfinder",
    BSLabel = cms.InputTag("offlineBeamSpot"),
    Dchannel = cms.vint32(
        1, 1, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0
    ),
    GenLabel = cms.InputTag("prunedGenParticles"),
    HLTLabel = cms.InputTag("TriggerResults","","HLT"),
    MVAMapLabel = cms.InputTag("packedPFCandidates","MVAValues"),
    MaxDocaCut = cms.vdouble(
        999.0, 999.0, 999.0, 999.0, 999.0,
        999.0, 999.0, 999.0, 999.0, 999.0,
        999.0, 999.0, 999.0, 999.0, 999.0,
        999.0
    ),
    PUInfoLabel = cms.InputTag("addPileupInfo"),
    PVLabel = cms.InputTag("offlineSlimmedPrimaryVerticesRecovery"),
    ResToNonRes_PtAsym_max = cms.vdouble(
        1.0, 1.0, 1.0, 1.0, 1.0,
        1.0, 1.0, 1.0, 1.0, 1.0,
        1.0, 1.0, 1.0, 1.0, 1.0,
        1.0
    ),
    ResToNonRes_PtAsym_min = cms.vdouble(
        -1.0, -1.0, -1.0, -1.0, -1.0,
        -1.0, -1.0, -1.0, -1.0, -1.0,
        -1.0, -1.0, -1.0, -1.0, -1.0,
        -1.0
    ),
    RunOnMC = cms.bool(False),
    TrackChi2Label = cms.InputTag("packedPFCandidateTrackChi2"),
    TrackLabel = cms.InputTag("packedPFCandidates"),
    VtxChiProbCut = cms.vdouble(
        0.05, 0.05, 0.0, 0.0, 0.0,
        0.0, 0.05, 0.05, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.05,
        0.05
    ),
    alphaCut = cms.vdouble(
        999.0, 999.0, 999.0, 999.0, 999.0,
        999.0, 999.0, 999.0, 999.0, 999.0,
        999.0, 999.0, 999.0, 999.0, 999.0,
        999.0
    ),
    codeCat = cms.int32(-1),
    dCutSeparating_PtVal = cms.vdouble(
        5.0, 5.0, 5.0, 5.0, 5.0,
        5.0, 5.0, 5.0, 5.0, 5.0,
        5.0, 5.0, 5.0, 5.0, 5.0,
        5.0
    ),
    dEtaCut = cms.vdouble(
        1.5, 1.5, 1.5, 1.5, 1.5,
        1.5, 1.5, 1.5, 1.5, 1.5,
        1.5, 1.5, 1.5, 1.5, 1.5,
        1.5
    ),
    dPtCut = cms.vdouble(
        4.0, 4.0, 1.0, 1.0, 1.0,
        1.0, 2.0, 2.0, 1.0, 1.0,
        1.0, 1.0, 1.0, 1.0, 2.0,
        2.0
    ),
    dRapidityCut = cms.vdouble(
        10.0, 10.0, 10.0, 10.0, 10.0,
        10.0, 10.0, 10.0, 10.0, 10.0,
        10.0, 10.0, 10.0, 10.0, 10.0,
        10.0
    ),
    detailMode = cms.bool(False),
    doDntupleSkim = cms.bool(False),
    doTkPreCut = cms.bool(True),
    dropUnusedTracks = cms.bool(True),
    makeDntuple = cms.bool(True),
    printInfo = cms.bool(True),
    svpvDistanceCut_highptD = cms.vdouble(
        2.5, 2.5, 2.5, 2.5, 2.5,
        2.5, 2.5, 2.5, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 2.5,
        2.5
    ),
    svpvDistanceCut_lowptD = cms.vdouble(
        2.5, 2.5, 2.5, 2.5, 2.5,
        2.5, 2.5, 2.5, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 2.5,
        2.5
    ),
    tkEtaCut = cms.double(2.4),
    tkPtCut = cms.double(2.0),
    tktkRes_VtxChiProbCut = cms.vdouble(
        0.05, 0.05, 0.05, 0.05, 0.05,
        0.05, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0
    ),
    tktkRes_alphaCut = cms.vdouble(
        999.0, 999.0, 999.0, 999.0, 999.0,
        999.0, 999.0, 999.0, 999.0, 999.0,
        999.0, 999.0, 999.0, 999.0, 999.0,
        999.0
    ),
    tktkRes_alphaToSVCut = cms.vdouble(
        999.0, 999.0, 999.0, 999.0, 999.0,
        999.0, 999.0, 999.0, 999.0, 999.0,
        999.0, 999.0, 999.0, 999.0, 999.0,
        999.0
    ),
    tktkRes_dCutSeparating_PtVal = cms.vdouble(
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0
    ),
    tktkRes_dEtaCut = cms.vdouble(
        1.5, 1.5, 1.5, 1.5, 1.5,
        1.5, 1.5, 1.5, 1.5, 1.5,
        1.5, 1.5, 1.5, 1.5, 1.5,
        1.5
    ),
    tktkRes_dPtCut = cms.vdouble(
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0
    ),
    tktkRes_svpvDistanceCut_highptD = cms.vdouble(
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 2.5, 2.5,
        2.5, 2.5, 2.5, 2.5, 0.0,
        0.0
    ),
    tktkRes_svpvDistanceCut_lowptD = cms.vdouble(
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 2.5, 2.5,
        2.5, 2.5, 2.5, 2.5, 0.0,
        0.0
    ),
    tktkRes_svpvDistanceToSVCut_highptD = cms.vdouble(
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0
    ),
    tktkRes_svpvDistanceToSVCut_lowptD = cms.vdouble(
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0
    )
)


process.PackedPFTowers = cms.EDProducer("PackedPFTowers",
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("packedPFCandidates"),
    useHF = cms.bool(True)
)


process.QWzdcreco = cms.EDProducer("QWZDC2018RecHit",
    ZDCCalib = cms.VPSet(
        cms.PSet(
            calib = cms.untracked.double(0.11),
            object = cms.untracked.string('hZDCP_EM1')
        ),
        cms.PSet(
            calib = cms.untracked.double(0.11),
            object = cms.untracked.string('hZDCP_EM2')
        ),
        cms.PSet(
            calib = cms.untracked.double(0.08),
            object = cms.untracked.string('hZDCP_EM3')
        ),
        cms.PSet(
            calib = cms.untracked.double(0.1),
            object = cms.untracked.string('hZDCP_EM4')
        ),
        cms.PSet(
            calib = cms.untracked.double(0.06),
            object = cms.untracked.string('hZDCP_EM5')
        ),
        cms.PSet(
            calib = cms.untracked.double(1.0),
            object = cms.untracked.string('hZDCP_HAD1')
        ),
        cms.PSet(
            calib = cms.untracked.double(0.61),
            object = cms.untracked.string('hZDCP_HAD2')
        ),
        cms.PSet(
            calib = cms.untracked.double(0.46),
            object = cms.untracked.string('hZDCP_HAD3')
        ),
        cms.PSet(
            calib = cms.untracked.double(0.52),
            object = cms.untracked.string('hZDCP_HAD4')
        ),
        cms.PSet(
            calib = cms.untracked.double(0.12),
            object = cms.untracked.string('hZDCM_EM1')
        ),
        cms.PSet(
            calib = cms.untracked.double(0.12),
            object = cms.untracked.string('hZDCM_EM2')
        ),
        cms.PSet(
            calib = cms.untracked.double(0.08),
            object = cms.untracked.string('hZDCM_EM3')
        ),
        cms.PSet(
            calib = cms.untracked.double(0.1),
            object = cms.untracked.string('hZDCM_EM4')
        ),
        cms.PSet(
            calib = cms.untracked.double(0.11),
            object = cms.untracked.string('hZDCM_EM5')
        ),
        cms.PSet(
            calib = cms.untracked.double(1.0),
            object = cms.untracked.string('hZDCM_HAD1')
        ),
        cms.PSet(
            calib = cms.untracked.double(0.81),
            object = cms.untracked.string('hZDCM_HAD2')
        ),
        cms.PSet(
            calib = cms.untracked.double(0.46),
            object = cms.untracked.string('hZDCM_HAD3')
        ),
        cms.PSet(
            calib = cms.untracked.double(0.58),
            object = cms.untracked.string('hZDCM_HAD4')
        ),
        cms.PSet(
            calib = cms.untracked.double(2.67),
            object = cms.untracked.string('Pscale')
        ),
        cms.PSet(
            calib = cms.untracked.double(4.45),
            object = cms.untracked.string('Mscale')
        )
    ),
    srcDetId = cms.untracked.InputTag("zdcdigi","DetId"),
    srcfC = cms.untracked.InputTag("zdcdigi","regularfC")
)


process.ak4CaloL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloL6SLBCorrector")
)


process.ak4CaloL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak4CaloL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4CaloL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloL6SLBCorrector")
)


process.ak4CaloL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2Relative')
)


process.ak4CaloL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L3Absolute')
)


process.ak4CaloL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4CaloJetsSoftMuonTagInfos")
)


process.ak4CaloResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak4HiGenJets = cms.EDProducer("SubEventGenJetProducer",
    Active_Area_Repeats = cms.int32(5),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    Rho_EtaMax = cms.double(4.5),
    applyWeight = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('GenJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("genParticlesForJets"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True)
)


process.ak4HiGenJetsCleaned = cms.EDProducer("HiGenJetCleaner",
    createNewCollection = cms.untracked.bool(True),
    deltaR = cms.double(0.25),
    fillDummyEntries = cms.untracked.bool(True),
    ptCut = cms.double(20),
    src = cms.InputTag("ak4HiGenJets")
)


process.ak4HiSignalGenJets = cms.EDProducer("HiSignalGenJetProducer",
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("ak4HiGenJets")
)


process.ak4JPTL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4L1JPTFastjetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4L1JPTFastjetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2Relative')
)


process.ak4JPTL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L3Absolute')
)


process.ak4JPTResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2L3Residual')
)


process.ak4L1JPTFastjetCorrector = cms.EDProducer("L1JPTOffsetCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.InputTag("ak4CaloL1FastjetCorrector")
)


process.ak4L1JPTOffsetCorrector = cms.EDProducer("L1JPTOffsetCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.InputTag("ak4CaloL1OffsetCorrector")
)


process.ak4PFCHSL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFCHSL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1OffsetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1OffsetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFCHSL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2Relative')
)


process.ak4PFCHSL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L3Absolute')
)


process.ak4PFCHSResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak4PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("pfEmptyCollection"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4PFJetsCHS = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("pfEmptyCollection"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4PFJetsForFlow = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(15.0),
    jetType = cms.string('BasicJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(
        -5, -4, -3, -2, -1,
        0, 1, 2, 3, 4,
        5
    ),
    puPtMin = cms.double(25),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("PackedPFTowers"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4PFL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFL6SLBCorrector")
)


process.ak4PFL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1OffsetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1OffsetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFL6SLBCorrector")
)


process.ak4PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2Relative')
)


process.ak4PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L3Absolute')
)


process.ak4PFL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4PFJetsSoftMuonTagInfos")
)


process.ak4PFPuppiL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1FastjetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1FastjetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFPuppiL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1OffsetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1OffsetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFPuppiL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak4PFPuppiL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak4PFPuppiResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L2L3Residual')
)


process.ak4PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak4TrackL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4TrackL2RelativeCorrector", "ak4TrackL3AbsoluteCorrector")
)


process.ak4TrackL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4TRK'),
    level = cms.string('L2Relative')
)


process.ak4TrackL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4TRK'),
    level = cms.string('L3Absolute')
)


process.ak5JetExtender = cms.EDProducer("JetExtender",
    coneSize = cms.double(0.5),
    jet2TracksAtCALO = cms.InputTag("ak5JetTracksAssociatorAtCaloFace"),
    jet2TracksAtVX = cms.InputTag("ak5JetTracksAssociatorAtVertex"),
    jets = cms.InputTag("ak5CaloJets")
)


process.ak5JetTracksAssociatorAtCaloFace = cms.EDProducer("JetTracksAssociatorAtCaloFace",
    coneSize = cms.double(0.5),
    extrapolations = cms.InputTag("trackExtrapolator"),
    jets = cms.InputTag("ak5CaloJets"),
    trackQuality = cms.string('goodIterative'),
    tracks = cms.InputTag("generalTracks")
)


process.ak5JetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("akCs4PFJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityGeneralTracks"),
    useAssigned = cms.bool(False)
)


process.ak5JetTracksAssociatorAtVertexPF = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("ak5PFJetsCHS"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)


process.ak5JetTracksAssociatorExplicit = cms.EDProducer("JetTracksAssociatorExplicit",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("ak5PFJetsCHS"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)


process.akCs0PFJets = cms.EDProducer("CSJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.005),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    applyWeight = cms.bool(False),
    csAlpha = cms.double(2.0),
    csRParam = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    etaMap = cms.InputTag("hiPuRho","mapEtaEdges"),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('pfParticlesCs'),
    jetPtMin = cms.double(0.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(
        -5, -4, -3, -2, -1,
        0, 1, 2, 3, 4,
        5
    ),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    rho = cms.InputTag("hiPuRho","mapToRho"),
    rhoFlowFitParams = cms.InputTag("hiFJRhoFlowModulation","rhoFlowFitParams"),
    rhom = cms.InputTag("hiPuRho","mapToRhoM"),
    src = cms.InputTag("pfCandComposites"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useModulatedRho = cms.bool(False),
    voronoiRfact = cms.double(-0.9),
    writeJetsWithConst = cms.bool(True)
)


process.akCs0PFpatJetCorrFactors = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L2Relative',
        'L2L3Residual'
    ),
    mightGet = cms.optional.untracked.vstring,
    payload = cms.string('AK4PF'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akCs0PFJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akCs0PFpatJets = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akCs0PFpatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akCs0PFpatJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("akCs0PFpfDeepCSVJetTags","probb"), cms.InputTag("akCs0PFpfDeepCSVJetTags","probc"), cms.InputTag("akCs0PFpfDeepCSVJetTags","probudsg"), cms.InputTag("akCs0PFpfDeepCSVJetTags","probbb"), cms.InputTag("akCs0PFpfJetProbabilityBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedCaloTowers = cms.bool(False),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akCs0PFpatJetGenJetMatch"),
    genPartonMatch = cms.InputTag("akCs0PFpatJetPartonMatch"),
    getJetMCFlavour = cms.bool(True),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag("akCs0PFpatJetCorrFactors"),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("akCs0PFJets"),
    mightGet = cms.optional.untracked.vstring,
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak5JetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.akCs0PFpfDeepCSVJetTags = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepCSV_PhaseI.json'),
    checkSVForDefaults = cms.bool(True),
    meanPadding = cms.bool(True),
    src = cms.InputTag("akCs0PFpfDeepCSVTagInfos"),
    toAdd = cms.PSet(

    )
)


process.akCs0PFpfDeepCSVTagInfos = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("akCs0PFpfSecondaryVertexTagInfos")
)


process.akCs0PFpfImpactParameterTagInfos = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("akCs0PFJets"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVerticesRecovery"),
    useTrackQuality = cms.bool(False)
)


process.akCs0PFpfJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateJetProbabilityComputer'),
    tagInfos = cms.VInputTag("akCs0PFpfImpactParameterTagInfos")
)


process.akCs0PFpfSecondaryVertexTagInfos = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akCs0PFpfImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akCs2PFJets = cms.EDProducer("CSJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.005),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    applyWeight = cms.bool(False),
    csAlpha = cms.double(2.0),
    csRParam = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    etaMap = cms.InputTag("hiPuRho","mapEtaEdges"),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('pfParticlesCs'),
    jetPtMin = cms.double(0.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(
        -5, -4, -3, -2, -1,
        0, 1, 2, 3, 4,
        5
    ),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.2),
    radiusPU = cms.double(0.5),
    rho = cms.InputTag("hiPuRho","mapToRho"),
    rhoFlowFitParams = cms.InputTag("hiFJRhoFlowModulation","rhoFlowFitParams"),
    rhom = cms.InputTag("hiPuRho","mapToRhoM"),
    src = cms.InputTag("pfCandComposites"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useModulatedRho = cms.bool(False),
    voronoiRfact = cms.double(-0.9),
    writeJetsWithConst = cms.bool(True)
)


process.akCs2PFpatJetCorrFactors = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L2Relative',
        'L2L3Residual'
    ),
    mightGet = cms.optional.untracked.vstring,
    payload = cms.string('AK2PF'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akCs2PFJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akCs2PFpatJets = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akCs2PFpatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akCs2PFpatJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("akCs2PFpfDeepCSVJetTags","probb"), cms.InputTag("akCs2PFpfDeepCSVJetTags","probc"), cms.InputTag("akCs2PFpfDeepCSVJetTags","probudsg"), cms.InputTag("akCs2PFpfDeepCSVJetTags","probbb"), cms.InputTag("akCs2PFpfJetProbabilityBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedCaloTowers = cms.bool(False),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akCs2PFpatJetGenJetMatch"),
    genPartonMatch = cms.InputTag("akCs2PFpatJetPartonMatch"),
    getJetMCFlavour = cms.bool(True),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag("akCs2PFpatJetCorrFactors"),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("akCs2PFJets"),
    mightGet = cms.optional.untracked.vstring,
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak5JetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.akCs2PFpfDeepCSVJetTags = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepCSV_PhaseI.json'),
    checkSVForDefaults = cms.bool(True),
    meanPadding = cms.bool(True),
    src = cms.InputTag("akCs2PFpfDeepCSVTagInfos"),
    toAdd = cms.PSet(

    )
)


process.akCs2PFpfDeepCSVTagInfos = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("akCs2PFpfSecondaryVertexTagInfos")
)


process.akCs2PFpfImpactParameterTagInfos = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("akCs2PFJets"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVerticesRecovery"),
    useTrackQuality = cms.bool(False)
)


process.akCs2PFpfJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateJetProbabilityComputer'),
    tagInfos = cms.VInputTag("akCs2PFpfImpactParameterTagInfos")
)


process.akCs2PFpfSecondaryVertexTagInfos = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akCs2PFpfImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akCs4PFJets = cms.EDProducer("CSJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.005),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    applyWeight = cms.bool(False),
    csAlpha = cms.double(2.0),
    csRParam = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    etaMap = cms.InputTag("hiPuRho","mapEtaEdges"),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('pfParticlesCs'),
    jetPtMin = cms.double(0.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(
        -5, -4, -3, -2, -1,
        0, 1, 2, 3, 4,
        5
    ),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    rho = cms.InputTag("hiPuRho","mapToRho"),
    rhoFlowFitParams = cms.InputTag("hiFJRhoFlowModulation","rhoFlowFitParams"),
    rhom = cms.InputTag("hiPuRho","mapToRhoM"),
    src = cms.InputTag("cleanedParticleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useModulatedRho = cms.bool(False),
    voronoiRfact = cms.double(-0.9),
    writeJetsWithConst = cms.bool(True)
)


process.allPartons = cms.EDProducer("PartonSelector",
    src = cms.InputTag("hiSignalGenParticles"),
    withLeptons = cms.bool(False)
)


process.calibratedElectrons = cms.EDProducer("CalibratedElectronProducer",
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Run2018_29Sep2020_RunFineEtaR9Gain'),
    epCombConfig = cms.PSet(
        ecalTrkRegressionConfig = cms.PSet(
            ebHighEtForestName = cms.ESInputTag("","electron_eb_ECALTRK"),
            ebLowEtForestName = cms.ESInputTag("","electron_eb_ECALTRK_lowpt"),
            eeHighEtForestName = cms.ESInputTag("","electron_ee_ECALTRK"),
            eeLowEtForestName = cms.ESInputTag("","electron_ee_ECALTRK_lowpt"),
            forceHighEnergyTrainingIfSaturated = cms.bool(False),
            lowEtHighEtBoundary = cms.double(50.0),
            rangeMaxHighEt = cms.double(3.0),
            rangeMaxLowEt = cms.double(3.0),
            rangeMinHighEt = cms.double(-1.0),
            rangeMinLowEt = cms.double(-1.0)
        ),
        ecalTrkRegressionUncertConfig = cms.PSet(
            ebHighEtForestName = cms.ESInputTag("","electron_eb_ECALTRK_var"),
            ebLowEtForestName = cms.ESInputTag("","electron_eb_ECALTRK_lowpt_var"),
            eeHighEtForestName = cms.ESInputTag("","electron_ee_ECALTRK_var"),
            eeLowEtForestName = cms.ESInputTag("","electron_ee_ECALTRK_lowpt_var"),
            forceHighEnergyTrainingIfSaturated = cms.bool(False),
            lowEtHighEtBoundary = cms.double(50.0),
            rangeMaxHighEt = cms.double(0.5),
            rangeMaxLowEt = cms.double(0.5),
            rangeMinHighEt = cms.double(0.0002),
            rangeMinLowEt = cms.double(0.0002)
        ),
        maxEPDiffInSigmaForComb = cms.double(15.0),
        maxEcalEnergyForComb = cms.double(200.0),
        maxRelTrkMomErrForComb = cms.double(10.0),
        minEOverPForComb = cms.double(0.025)
    ),
    mightGet = cms.optional.untracked.vstring,
    minEtToCalibrate = cms.double(5.0),
    produceCalibratedObjs = cms.bool(True),
    recHitCollectionEB = cms.InputTag("reducedEcalRecHitsEB"),
    recHitCollectionEE = cms.InputTag("reducedEcalRecHitsEE"),
    semiDeterministic = cms.bool(True),
    src = cms.InputTag("gedGsfElectrons"),
    valueMapsStored = cms.vstring(
        'energyScaleStatUp',
        'energyScaleStatDown',
        'energyScaleSystUp',
        'energyScaleSystDown',
        'energyScaleGainUp',
        'energyScaleGainDown',
        'energySigmaRhoUp',
        'energySigmaRhoDown',
        'energySigmaPhiUp',
        'energySigmaPhiDown',
        'energyScaleUp',
        'energyScaleDown',
        'energySigmaUp',
        'energySigmaDown',
        'energyScaleValue',
        'energySigmaValue',
        'energySmearNrSigma',
        'ecalEnergyPreCorr',
        'ecalEnergyErrPreCorr',
        'ecalEnergyPostCorr',
        'ecalEnergyErrPostCorr',
        'ecalTrkEnergyPreCorr',
        'ecalTrkEnergyErrPreCorr',
        'ecalTrkEnergyPostCorr',
        'ecalTrkEnergyErrPostCorr'
    )
)


process.calibratedPatElectrons = cms.EDProducer("CalibratedPatElectronProducer",
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Run2018_29Sep2020_RunFineEtaR9Gain'),
    epCombConfig = cms.PSet(
        ecalTrkRegressionConfig = cms.PSet(
            ebHighEtForestName = cms.ESInputTag("","electron_eb_ECALTRK"),
            ebLowEtForestName = cms.ESInputTag("","electron_eb_ECALTRK_lowpt"),
            eeHighEtForestName = cms.ESInputTag("","electron_ee_ECALTRK"),
            eeLowEtForestName = cms.ESInputTag("","electron_ee_ECALTRK_lowpt"),
            forceHighEnergyTrainingIfSaturated = cms.bool(False),
            lowEtHighEtBoundary = cms.double(50.0),
            rangeMaxHighEt = cms.double(3.0),
            rangeMaxLowEt = cms.double(3.0),
            rangeMinHighEt = cms.double(-1.0),
            rangeMinLowEt = cms.double(-1.0)
        ),
        ecalTrkRegressionUncertConfig = cms.PSet(
            ebHighEtForestName = cms.ESInputTag("","electron_eb_ECALTRK_var"),
            ebLowEtForestName = cms.ESInputTag("","electron_eb_ECALTRK_lowpt_var"),
            eeHighEtForestName = cms.ESInputTag("","electron_ee_ECALTRK_var"),
            eeLowEtForestName = cms.ESInputTag("","electron_ee_ECALTRK_lowpt_var"),
            forceHighEnergyTrainingIfSaturated = cms.bool(False),
            lowEtHighEtBoundary = cms.double(50.0),
            rangeMaxHighEt = cms.double(0.5),
            rangeMaxLowEt = cms.double(0.5),
            rangeMinHighEt = cms.double(0.0002),
            rangeMinLowEt = cms.double(0.0002)
        ),
        maxEPDiffInSigmaForComb = cms.double(15.0),
        maxEcalEnergyForComb = cms.double(200.0),
        maxRelTrkMomErrForComb = cms.double(10.0),
        minEOverPForComb = cms.double(0.025)
    ),
    mightGet = cms.optional.untracked.vstring,
    minEtToCalibrate = cms.double(5.0),
    produceCalibratedObjs = cms.bool(True),
    recHitCollectionEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    recHitCollectionEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
    semiDeterministic = cms.bool(True),
    src = cms.InputTag("slimmedElectrons"),
    valueMapsStored = cms.vstring(
        'energyScaleStatUp',
        'energyScaleStatDown',
        'energyScaleSystUp',
        'energyScaleSystDown',
        'energyScaleGainUp',
        'energyScaleGainDown',
        'energySigmaRhoUp',
        'energySigmaRhoDown',
        'energySigmaPhiUp',
        'energySigmaPhiDown',
        'energyScaleUp',
        'energyScaleDown',
        'energySigmaUp',
        'energySigmaDown',
        'energyScaleValue',
        'energySigmaValue',
        'energySmearNrSigma',
        'ecalEnergyPreCorr',
        'ecalEnergyErrPreCorr',
        'ecalEnergyPostCorr',
        'ecalEnergyErrPostCorr',
        'ecalTrkEnergyPreCorr',
        'ecalTrkEnergyErrPreCorr',
        'ecalTrkEnergyPostCorr',
        'ecalTrkEnergyErrPostCorr'
    )
)


process.calibratedPatPhotons = cms.EDProducer("CalibratedPatPhotonProducer",
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Run2018_29Sep2020_RunFineEtaR9Gain'),
    mightGet = cms.optional.untracked.vstring,
    minEtToCalibrate = cms.double(5.0),
    produceCalibratedObjs = cms.bool(True),
    recHitCollectionEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    recHitCollectionEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
    semiDeterministic = cms.bool(True),
    src = cms.InputTag("slimmedPhotons"),
    valueMapsStored = cms.vstring(
        'energyScaleStatUp',
        'energyScaleStatDown',
        'energyScaleSystUp',
        'energyScaleSystDown',
        'energyScaleGainUp',
        'energyScaleGainDown',
        'energySigmaRhoUp',
        'energySigmaRhoDown',
        'energySigmaPhiUp',
        'energySigmaPhiDown',
        'energyScaleUp',
        'energyScaleDown',
        'energySigmaUp',
        'energySigmaDown',
        'energyScaleValue',
        'energySigmaValue',
        'energySmearNrSigma',
        'ecalEnergyPreCorr',
        'ecalEnergyErrPreCorr',
        'ecalEnergyPostCorr',
        'ecalEnergyErrPostCorr'
    )
)


process.calibratedPhotons = cms.EDProducer("CalibratedPhotonProducer",
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Run2018_29Sep2020_RunFineEtaR9Gain'),
    mightGet = cms.optional.untracked.vstring,
    minEtToCalibrate = cms.double(5.0),
    produceCalibratedObjs = cms.bool(True),
    recHitCollectionEB = cms.InputTag("reducedEcalRecHitsEB"),
    recHitCollectionEE = cms.InputTag("reducedEcalRecHitsEE"),
    semiDeterministic = cms.bool(True),
    src = cms.InputTag("gedPhotons"),
    valueMapsStored = cms.vstring(
        'energyScaleStatUp',
        'energyScaleStatDown',
        'energyScaleSystUp',
        'energyScaleSystDown',
        'energyScaleGainUp',
        'energyScaleGainDown',
        'energySigmaRhoUp',
        'energySigmaRhoDown',
        'energySigmaPhiUp',
        'energySigmaPhiDown',
        'energyScaleUp',
        'energyScaleDown',
        'energySigmaUp',
        'energySigmaDown',
        'energyScaleValue',
        'energySigmaValue',
        'energySmearNrSigma',
        'ecalEnergyPreCorr',
        'ecalEnergyErrPreCorr',
        'ecalEnergyPostCorr',
        'ecalEnergyErrPostCorr'
    )
)


process.caloMetT1 = cms.EDProducer("CorrectedCaloMETProducer",
    src = cms.InputTag("caloMetM"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrCaloMetType1","type1"))
)


process.caloMetT1T2 = cms.EDProducer("CorrectedCaloMETProducer",
    src = cms.InputTag("caloMetM"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrCaloMetType1","type1"), cms.InputTag("corrCaloMetType2"))
)


process.cleanPatElectrons = cms.EDProducer("PATElectronCleaner",
    checkOverlaps = cms.PSet(
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatMuons")
        )
    ),
    finalCut = cms.string(''),
    preselection = cms.string(''),
    src = cms.InputTag("selectedPatElectrons")
)


process.cleanPatJets = cms.EDProducer("PATJetCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        ),
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatMuons")
        ),
        photons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatPhotons")
        ),
        taus = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatTaus")
        ),
        tkIsoElectrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            preselection = cms.string('pt > 10 && trackIso < 3'),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        )
    ),
    finalCut = cms.string(''),
    preselection = cms.string(''),
    src = cms.InputTag("selectedPatJets")
)


process.cleanPatMuons = cms.EDProducer("PATMuonCleaner",
    checkOverlaps = cms.PSet(

    ),
    finalCut = cms.string(''),
    preselection = cms.string(''),
    src = cms.InputTag("selectedPatMuons")
)


process.cleanPatPhotons = cms.EDProducer("PATPhotonCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('bySuperClusterSeed'),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        )
    ),
    finalCut = cms.string(''),
    preselection = cms.string(''),
    src = cms.InputTag("selectedPatPhotons")
)


process.cleanPatTaus = cms.EDProducer("PATTauCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        ),
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatMuons")
        )
    ),
    finalCut = cms.string('pt > 18. & abs(eta) < 2.3'),
    preselection = cms.string('tauID("decayModeFinding") > 0.5 & tauID("byLooseCombinedIsolationDeltaBetaCorr3Hits") > 0.5 & tauID("againstMuonTight3") > 0.5 & tauID("againstElectronVLooseMVA6") > 0.5'),
    src = cms.InputTag("selectedPatTaus")
)


process.cleanedPartons = cms.EDProducer("HiPartonCleaner",
    createNewCollection = cms.untracked.bool(True),
    deltaR = cms.double(0.25),
    fillDummyEntries = cms.untracked.bool(True),
    ptCut = cms.double(20),
    src = cms.InputTag("allPartons")
)


process.combinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('heavyIonCSVComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexTagInfos"))
)


process.corrCaloMetType1 = cms.EDProducer("CaloJetMETcorrInputProducer",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("ak4CaloL2L3Corrector"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    src = cms.InputTag("ak4CaloJets"),
    srcMET = cms.InputTag("caloMetM"),
    type1JetPtThreshold = cms.double(20.0)
)


process.corrCaloMetType2 = cms.EDProducer("Type2CorrectionProducer",
    srcUnclEnergySums = cms.VInputTag(cms.InputTag("corrCaloMetType1","type2"), cms.InputTag("muCaloMetCorr")),
    type2CorrFormula = cms.string('A + B*TMath::Exp(-C*x)'),
    type2CorrParameter = cms.PSet(
        A = cms.double(2.0),
        B = cms.double(1.3),
        C = cms.double(0.1)
    )
)


process.corrPfMetType1 = cms.EDProducer("PFJetMETcorrInputProducer",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
    jetCorrLabelRes = cms.InputTag("ak4PFCHSL1FastL2L3ResidualCorrector"),
    offsetCorrLabel = cms.InputTag("ak4PFCHSL1FastjetCorrector"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("ak4PFJetsCHS"),
    type1JetPtThreshold = cms.double(15.0)
)


process.corrPfMetType2 = cms.EDProducer("Type2CorrectionProducer",
    srcUnclEnergySums = cms.VInputTag(cms.InputTag("corrPfMetType1","type2"), cms.InputTag("corrPfMetType1","offset"), cms.InputTag("pfCandMETcorr")),
    type2CorrFormula = cms.string('A'),
    type2CorrParameter = cms.PSet(
        A = cms.double(1.4)
    )
)


process.correctedElectrons = cms.EDProducer("CorrectedElectronProducer",
    centrality = cms.InputTag("centralityBin","HFtowers"),
    correctionFile = cms.string('HeavyIonsAnalysis/EGMAnalysis/data/SSHIRun2018A.dat'),
    epCombConfig = cms.PSet(
        ecalTrkRegressionConfig = cms.PSet(
            ebHighEtForestName = cms.ESInputTag("","electron_eb_ECALTRK"),
            ebLowEtForestName = cms.ESInputTag("","electron_eb_ECALTRK_lowpt"),
            eeHighEtForestName = cms.ESInputTag("","electron_ee_ECALTRK"),
            eeLowEtForestName = cms.ESInputTag("","electron_ee_ECALTRK_lowpt"),
            forceHighEnergyTrainingIfSaturated = cms.bool(False),
            lowEtHighEtBoundary = cms.double(50.0),
            rangeMaxHighEt = cms.double(3.0),
            rangeMaxLowEt = cms.double(3.0),
            rangeMinHighEt = cms.double(-1.0),
            rangeMinLowEt = cms.double(-1.0)
        ),
        ecalTrkRegressionUncertConfig = cms.PSet(
            ebHighEtForestName = cms.ESInputTag("","electron_eb_ECALTRK_var"),
            ebLowEtForestName = cms.ESInputTag("","electron_eb_ECALTRK_lowpt_var"),
            eeHighEtForestName = cms.ESInputTag("","electron_ee_ECALTRK_var"),
            eeLowEtForestName = cms.ESInputTag("","electron_ee_ECALTRK_lowpt_var"),
            forceHighEnergyTrainingIfSaturated = cms.bool(False),
            lowEtHighEtBoundary = cms.double(50.0),
            rangeMaxHighEt = cms.double(0.5),
            rangeMaxLowEt = cms.double(0.5),
            rangeMinHighEt = cms.double(0.0002),
            rangeMinLowEt = cms.double(0.0002)
        ),
        maxEPDiffInSigmaForComb = cms.double(15.0),
        maxEcalEnergyForComb = cms.double(200.0),
        maxRelTrkMomErrForComb = cms.double(10.0),
        minEOverPForComb = cms.double(0.025)
    ),
    minPt = cms.double(20.0),
    semiDeterministic = cms.bool(True),
    src = cms.InputTag("slimmedElectrons")
)


process.elPFIsoDepositChargedAllPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositChargedPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositGammaPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFCandWithSuperClusterExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        MissHitSCMatch_Veto = cms.bool(True),
        SCMatch_Veto = cms.bool(False),
        inputCandView = cms.InputTag("pfAllPhotonsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositNeutralPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositPUPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoValueCharged03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.electronMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    mcPdgId = cms.vint32(11),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons")
)


process.filteredDisplacedMuons = cms.EDProducer("DisplacedMuonFilterProducer",
    EcalIsoDeposits = cms.InputTag("displacedMuons","ecal"),
    FillDetectorBasedIsolation = cms.bool(False),
    FillTimingInfo = cms.bool(True),
    HcalIsoDeposits = cms.InputTag("displacedMuons","hcal"),
    HoIsoDeposits = cms.InputTag("displacedMuons","ho"),
    JetIsoDeposits = cms.InputTag("displacedMuons","jets"),
    TrackIsoDeposits = cms.InputTag("displacedMuons","tracker"),
    minMatches = cms.double(2),
    minPtSTA = cms.double(3.5),
    minPtTK = cms.double(3.5),
    srcMuons = cms.InputTag("displacedMuons")
)


process.genParticlePlusGEANT = cms.EDProducer("GenPlusSimParticleProducer",
    filter = cms.vstring('pt > 0.0'),
    genParticles = cms.InputTag("genParticles"),
    setStatus = cms.int32(8),
    src = cms.InputTag("g4SimHits")
)


process.genParticlesForJets = cms.EDProducer("InputGenJetsParticleSelector",
    excludeFromResonancePids = cms.vuint32(12, 13, 14, 16),
    excludeResonances = cms.bool(False),
    ignoreParticleIDs = cms.vuint32(
        1000022, 1000012, 1000014, 1000016, 2000012,
        2000014, 2000016, 1000039, 5100039, 4000012,
        4000014, 4000016, 9900012, 9900014, 9900016,
        39
    ),
    partonicFinalState = cms.bool(False),
    src = cms.InputTag("genParticles"),
    tausAsJets = cms.bool(False)
)


process.heavyIonCleanedGenJets = cms.EDProducer("HiGenJetCleaner",
    createNewCollection = cms.untracked.bool(True),
    deltaR = cms.double(0.25),
    fillDummyEntries = cms.untracked.bool(True),
    ptCut = cms.double(20),
    src = cms.InputTag("iterativeCone5HiGenJets")
)


process.hiFJRhoFlowModulation = cms.EDProducer("HiFJRhoFlowModulationProducer",
    EvtPlane = cms.InputTag("hiEvtPlane"),
    doEvtPlane = cms.bool(False),
    doFreePlaneFit = cms.bool(False),
    doJettyExclusion = cms.bool(False),
    evtPlaneLevel = cms.int32(0),
    firstFittedVn = cms.int32(2),
    jetTag = cms.InputTag("ak4PFJetsForFlow"),
    lastFittedVn = cms.int32(3),
    mightGet = cms.optional.untracked.vstring,
    minPfCandidatesPerEvent = cms.int32(100),
    pfCandSource = cms.InputTag("packedPFCandidates"),
    pfCandidateEtaCut = cms.double(1),
    pfCandidateMaxPtCut = cms.double(3),
    pfCandidateMinPtCut = cms.double(0.3)
)


process.hiPartons = cms.EDProducer("HiPartonCleaner",
    createNewCollection = cms.untracked.bool(True),
    deltaR = cms.double(0.25),
    fillDummyEntries = cms.untracked.bool(True),
    ptCut = cms.double(20),
    src = cms.InputTag("genPartons")
)


process.hiPuRho = cms.EDProducer("HiPuRhoProducer",
    dropZeroTowers = cms.bool(True),
    medianWindowWidth = cms.int32(2),
    mightGet = cms.optional.untracked.vstring,
    minimumTowersFraction = cms.double(0.7),
    nSigmaPU = cms.double(1),
    puPtMin = cms.double(15),
    rParam = cms.double(0.3),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("PackedPFTowers"),
    towSigmaCut = cms.double(5)
)


process.hiSignalGenJetProducer = cms.EDProducer("HiSignalGenJetProducer",
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("akHiGenJets")
)


process.hiSignalGenParticles = cms.EDProducer("HiSignalParticleProducer",
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("prunedGenParticles")
)


process.hpsPFTauBasicDiscriminators = cms.EDProducer("PFRecoTauDiscriminationByIsolationContainer",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            IDname = cms.string('ByLooseCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(2.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByMediumCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(1.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByTightCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(0.8, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByLooseChargedIsolation'),
            maximumAbsoluteValues = cms.vdouble(2.5),
            referenceRawIDNames = cms.vstring('ChargedIsoPtSum')
        ),
        cms.PSet(
            IDname = cms.string('ByPhotonPtSumOutsideSignalCone'),
            maximumRelativeValues = cms.vdouble(0.1),
            referenceRawIDNames = cms.vstring('PhotonPtSumOutsideSignalCone')
        )
    ),
    IDdefinitions = cms.VPSet(
        cms.PSet(
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ChargedIsoPtSum'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSum'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSumWeight'),
            UseAllPFCandsForWeights = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('TauFootprintCorrection'),
            storeRawFootprintCorrection = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PhotonPtSumOutsideSignalCone'),
            storeRawPhotonSumPt_outsideSignalCone = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PUcorrPtSum'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawPUsumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ByRawCombinedIsolationDBSumPtCorr3Hits'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        )
    ),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    WeightECALIsolation = cms.double(1),
    applyFootprintCorrection = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.bool(True),
    deltaBetaPUTrackPtCutOverride_val = cms.double(0.5),
    footprintCorrections = cms.VPSet(
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 0')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ),
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ),
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )
    ),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    mightGet = cms.optional.untracked.vstring,
    minTauPtForNoIso = cms.double(-99),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.impactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("ak5JetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.islandPhotonCore = cms.EDProducer("PhotonCoreProducer",
    conversionProducer = cms.InputTag(""),
    endcapOnly = cms.bool(False),
    minSCEt = cms.double(8.0),
    photonCoreCollection = cms.string(''),
    pixelSeedProducer = cms.InputTag("electronMergedSeeds"),
    risolveConversionAmbiguity = cms.bool(True),
    scHybridBarrelProducer = cms.InputTag("correctedIslandBarrelSuperClusters"),
    scIslandEndcapProducer = cms.InputTag("correctedIslandEndcapSuperClusters")
)


process.jetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.jetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.lowPtElectronMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    mcPdgId = cms.vint32(11),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("lowPtGsfElectrons")
)


process.lowPtGsfElectronID = cms.EDProducer("LowPtGsfElectronIDProducer",
    MaxPtThreshold = cms.double(15),
    MinPtThreshold = cms.double(0.5),
    ModelNames = cms.vstring(''),
    ModelThresholds = cms.vdouble(-99),
    ModelWeights = cms.vstring('RecoEgamma/ElectronIdentification/data/LowPtElectrons/LowPtElectrons_ID_2020Nov28.root'),
    PassThrough = cms.bool(False),
    Version = cms.string('V1'),
    electrons = cms.InputTag("lowPtGsfElectrons"),
    gsfToTrack = cms.InputTag("lowPtGsfToTrackLinks"),
    mightGet = cms.optional.untracked.vstring,
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    unbiased = cms.InputTag("lowPtGsfElectronSeedValueMaps","unbiased"),
    useGsfToTrack = cms.bool(False),
    usePAT = cms.bool(False)
)


process.lowPtGsfElectrons = cms.EDProducer("LowPtGsfElectronFinalizer",
    mightGet = cms.optional.untracked.vstring,
    previousGsfElectronsTag = cms.InputTag("lowPtGsfElectronsPreRegression"),
    regressionConfig = cms.PSet(
        eleRegs = cms.PSet(
            ecalOnlyMean = cms.PSet(
                ebHighEtForestName = cms.ESInputTag("","lowPtElectron_eb_ecalOnly_05To50_mean"),
                ebLowEtForestName = cms.ESInputTag("","lowPtElectron_eb_ecalOnly_05To50_mean"),
                eeHighEtForestName = cms.ESInputTag("","lowPtElectron_ee_ecalOnly_05To50_mean"),
                eeLowEtForestName = cms.ESInputTag("","lowPtElectron_ee_ecalOnly_05To50_mean"),
                forceHighEnergyTrainingIfSaturated = cms.bool(True),
                lowEtHighEtBoundary = cms.double(20.0),
                rangeMaxHighEt = cms.double(3.0),
                rangeMaxLowEt = cms.double(2.0),
                rangeMinHighEt = cms.double(-1.0),
                rangeMinLowEt = cms.double(0.2)
            ),
            ecalOnlySigma = cms.PSet(
                ebHighEtForestName = cms.ESInputTag("","lowPtElectron_eb_ecalOnly_05To50_sigma"),
                ebLowEtForestName = cms.ESInputTag("","lowPtElectron_eb_ecalOnly_05To50_sigma"),
                eeHighEtForestName = cms.ESInputTag("","lowPtElectron_ee_ecalOnly_05To50_sigma"),
                eeLowEtForestName = cms.ESInputTag("","lowPtElectron_ee_ecalOnly_05To50_sigma"),
                forceHighEnergyTrainingIfSaturated = cms.bool(True),
                lowEtHighEtBoundary = cms.double(20.0),
                rangeMaxHighEt = cms.double(0.5),
                rangeMaxLowEt = cms.double(0.5),
                rangeMinHighEt = cms.double(0.0002),
                rangeMinLowEt = cms.double(0.0002)
            ),
            epComb = cms.PSet(
                ecalTrkRegressionConfig = cms.PSet(
                    ebHighEtForestName = cms.ESInputTag("","lowPtElectron_eb_ecalTrk_05To50_mean"),
                    ebLowEtForestName = cms.ESInputTag("","lowPtElectron_eb_ecalTrk_05To50_mean"),
                    eeHighEtForestName = cms.ESInputTag("","lowPtElectron_ee_ecalTrk_05To50_mean"),
                    eeLowEtForestName = cms.ESInputTag("","lowPtElectron_ee_ecalTrk_05To50_mean"),
                    forceHighEnergyTrainingIfSaturated = cms.bool(False),
                    lowEtHighEtBoundary = cms.double(20.0),
                    rangeMaxHighEt = cms.double(2.0),
                    rangeMaxLowEt = cms.double(2.0),
                    rangeMinHighEt = cms.double(0.2),
                    rangeMinLowEt = cms.double(0.2)
                ),
                ecalTrkRegressionUncertConfig = cms.PSet(
                    ebHighEtForestName = cms.ESInputTag("","lowPtElectron_eb_ecalTrk_05To50_sigma"),
                    ebLowEtForestName = cms.ESInputTag("","lowPtElectron_eb_ecalTrk_05To50_sigma"),
                    eeHighEtForestName = cms.ESInputTag("","lowPtElectron_ee_ecalTrk_05To50_sigma"),
                    eeLowEtForestName = cms.ESInputTag("","lowPtElectron_ee_ecalTrk_05To50_sigma"),
                    forceHighEnergyTrainingIfSaturated = cms.bool(False),
                    lowEtHighEtBoundary = cms.double(20.0),
                    rangeMaxHighEt = cms.double(0.5),
                    rangeMaxLowEt = cms.double(0.5),
                    rangeMinHighEt = cms.double(0.0002),
                    rangeMinLowEt = cms.double(0.0002)
                ),
                maxEPDiffInSigmaForComb = cms.double(15.0),
                maxEcalEnergyForComb = cms.double(200.0),
                maxRelTrkMomErrForComb = cms.double(10.0),
                minEOverPForComb = cms.double(0.025)
            )
        ),
        maxRawEnergyForLowPtEBSigma = cms.double(-1),
        maxRawEnergyForLowPtEESigma = cms.double(1200.0),
        modifierName = cms.string('EGRegressionModifierV3'),
        phoRegs = cms.PSet(
            ecalOnlyMean = cms.PSet(
                ebHighEtForestName = cms.ESInputTag("","photon_eb_ECALonly"),
                ebLowEtForestName = cms.ESInputTag("","photon_eb_ecalOnly_5To300_0p2To2_mean"),
                eeHighEtForestName = cms.ESInputTag("","photon_ee_ECALonly"),
                eeLowEtForestName = cms.ESInputTag("","photon_ee_ecalOnly_5To300_0p2To2_mean"),
                forceHighEnergyTrainingIfSaturated = cms.bool(True),
                lowEtHighEtBoundary = cms.double(999999.0),
                rangeMaxHighEt = cms.double(3.0),
                rangeMaxLowEt = cms.double(2.0),
                rangeMinHighEt = cms.double(-1.0),
                rangeMinLowEt = cms.double(0.2)
            ),
            ecalOnlySigma = cms.PSet(
                ebHighEtForestName = cms.ESInputTag("","photon_eb_ECALonly_var"),
                ebLowEtForestName = cms.ESInputTag("","photon_eb_ecalOnly_5To300_0p0002To0p5_sigma"),
                eeHighEtForestName = cms.ESInputTag("","photon_ee_ECALonly_var"),
                eeLowEtForestName = cms.ESInputTag("","photon_ee_ecalOnly_5To300_0p0002To0p5_sigma"),
                forceHighEnergyTrainingIfSaturated = cms.bool(True),
                lowEtHighEtBoundary = cms.double(999999.0),
                rangeMaxHighEt = cms.double(0.5),
                rangeMaxLowEt = cms.double(0.5),
                rangeMinHighEt = cms.double(0.0002),
                rangeMinLowEt = cms.double(0.0002)
            )
        ),
        rhoTag = cms.InputTag("fixedGridRhoFastjetAll"),
        useClosestToCentreSeedCrysDef = cms.bool(False)
    )
)


process.muCaloMetCorr = cms.EDProducer("MuonMETcorrInputProducer",
    src = cms.InputTag("muons"),
    srcMuonCorrections = cms.InputTag("muonMETValueMapProducer","muCorrData")
)


process.muPFIsoDepositChargedAllPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositChargedPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositGammaPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllPhotonsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositNeutralPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositPUPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoValueCharged03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueCharged04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueChargedAll03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueChargedAll04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGamma03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGamma04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGammaHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGammaHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutral03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutral04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutralHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutralHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValuePU03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValuePU04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueCharged03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueCharged04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueChargedAll03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueChargedAll04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGamma03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGamma04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGammaHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGammaHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutral03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutral04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutralHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutralHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValuePU03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValuePU04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueCharged03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueCharged04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueChargedAll03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueChargedAll04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGamma03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGamma04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGammaHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGammaHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutral03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutral04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutralHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutralHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValuePU03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValuePU04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muonHLTL1Match = cms.EDProducer("HLTL1MuonMatcher",
    fallbackToME1 = cms.bool(False),
    l1PhiOffset = cms.double(0.02181661564992912),
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltL1extraParticles")'),
    maxDeltaEta = cms.double(99),
    maxDeltaPhi = cms.double(6),
    maxDeltaR = cms.double(0.5),
    resolveAmbiguities = cms.bool(True),
    setPropLabel = cms.string('propagatedToM2'),
    sortBy = cms.string('pt'),
    src = cms.InputTag("muons"),
    useMB2InOverlap = cms.bool(False),
    useSimpleGeometry = cms.bool(True),
    useStage2L1 = cms.bool(False),
    useState = cms.string('atVertex'),
    useTrack = cms.string('tracker'),
    writeExtraInfo = cms.bool(True)
)


process.muonL1Info = cms.EDProducer("L1MuonMatcher",
    fallbackToME1 = cms.bool(True),
    firstBX = cms.int32(0),
    l1PhiOffset = cms.double(0.02181661564992912),
    lastBX = cms.int32(0),
    matched = cms.InputTag("gmtStage2Digis","Muon"),
    maxDeltaEta = cms.double(0.2),
    maxDeltaPhi = cms.double(6),
    maxDeltaR = cms.double(0.3),
    preselection = cms.string(''),
    setL1Label = cms.string('l1'),
    setPropLabel = cms.string('propagated'),
    sortBy = cms.string('pt'),
    src = cms.InputTag("muons"),
    useMB2InOverlap = cms.bool(True),
    useSimpleGeometry = cms.bool(True),
    useStage2L1 = cms.bool(True),
    useState = cms.string('atVertex'),
    useTrack = cms.string('tracker'),
    writeExtraInfo = cms.bool(True)
)


process.muonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    mcPdgId = cms.vint32(13),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("muons")
)


process.muonMatchHLTCtfTrack = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltMuTrackJpsiCtfTrackCands")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(False),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchHLTCtfTrack2 = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltMuTrackJpsiEffCtfTrackCands")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchHLTL1 = cms.EDProducer("HLTL1MuonMatcher",
    fallbackToME1 = cms.bool(True),
    l1PhiOffset = cms.double(0.02181661564992912),
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltGtStage2Digis:Muon")'),
    maxDeltaEta = cms.double(0.2),
    maxDeltaPhi = cms.double(6),
    maxDeltaR = cms.double(0.3),
    preselection = cms.string(''),
    resolveAmbiguities = cms.bool(False),
    setPropLabel = cms.string('propagatedToM2'),
    sortBy = cms.string('pt'),
    src = cms.InputTag("patMuonsWithoutTrigger"),
    useMB2InOverlap = cms.bool(True),
    useSimpleGeometry = cms.bool(True),
    useStage2L1 = cms.bool(True),
    useState = cms.string('atVertex'),
    useTrack = cms.string('tracker'),
    writeExtraInfo = cms.bool(True)
)


process.muonMatchHLTL2 = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltL2MuonCandidatesPPOnAA")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.3),
    resolveAmbiguities = cms.bool(False),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchHLTL3 = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltIterL3MuonCandidatesPPOnAA")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(False),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchHLTL3T = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltGlbTrkMuonCands")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchHLTL3fromL2 = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltIterL3FromL2MuonCandidates")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(False),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchHLTTkMu = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltHighPtTkMuonCands")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(False),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchHLTTrackIt = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltTracksIter")'),
    maxDPtRel = cms.double(1.0),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(False),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchHLTTrackMu = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltMuTkMuJpsiTrackerMuonCands")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(False),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchL1 = cms.EDProducer("HLTL1MuonMatcher",
    fallbackToME1 = cms.bool(False),
    l1PhiOffset = cms.double(0.02181661564992912),
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltL1extraParticles")'),
    maxDeltaEta = cms.double(99),
    maxDeltaPhi = cms.double(6),
    maxDeltaR = cms.double(0.5),
    resolveAmbiguities = cms.bool(True),
    setPropLabel = cms.string('propagatedToM2'),
    sortBy = cms.string('pt'),
    src = cms.InputTag("patMuonsWithoutTrigger"),
    useMB2InOverlap = cms.bool(False),
    useSimpleGeometry = cms.bool(True),
    useStage2L1 = cms.bool(False),
    useState = cms.string('atVertex'),
    useTrack = cms.string('tracker'),
    writeExtraInfo = cms.bool(True)
)


process.muonTriggerMatchHLT = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string(''),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.ootPhotonCore = cms.EDProducer("PhotonCoreProducer",
    conversionProducer = cms.InputTag("conversions"),
    endcapOnly = cms.bool(False),
    minSCEt = cms.double(10.0),
    photonCoreCollection = cms.string(''),
    pixelSeedProducer = cms.InputTag("electronMergedSeeds"),
    risolveConversionAmbiguity = cms.bool(True),
    scHybridBarrelProducer = cms.InputTag("particleFlowSuperClusterOOTECAL","particleFlowSuperClusterOOTECALBarrel"),
    scIslandEndcapProducer = cms.InputTag("particleFlowSuperClusterOOTECAL","particleFlowSuperClusterOOTECALEndcapWithPreshower")
)


process.ootPhotonEcalPFClusterIsolationProducer = cms.EDProducer("PhotonEcalPFClusterIsolationProducer",
    candidateProducer = cms.InputTag("ootPhotonsTmp"),
    drMax = cms.double(0.3),
    drVetoBarrel = cms.double(0),
    drVetoEndcap = cms.double(0),
    energyBarrel = cms.double(0),
    energyEndcap = cms.double(0),
    etaStripBarrel = cms.double(0),
    etaStripEndcap = cms.double(0),
    mightGet = cms.optional.untracked.vstring,
    pfClusterProducer = cms.InputTag("particleFlowClusterOOTECAL")
)


process.ootPhotonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(1.0),
    maxDeltaR = cms.double(0.2),
    mcPdgId = cms.vint32(22),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ootPhotons")
)


process.ootPhotons = cms.EDProducer("GEDPhotonProducer",
    PFIsolationCalculatorSet = cms.PSet(
        ComponentName = cms.string('pfIsolationCalculator'),
        applyDzDxyVeto = cms.bool(True),
        applyMissHitPhVeto = cms.bool(False),
        applyPFPUVeto = cms.bool(True),
        applyVeto = cms.bool(True),
        checkClosestZVertex = cms.bool(True),
        coneDR = cms.double(0.3),
        deltaRVetoBarrel = cms.bool(True),
        deltaRVetoBarrelCharged = cms.double(0.02),
        deltaRVetoBarrelNeutrals = cms.double(-1.0),
        deltaRVetoBarrelPhotons = cms.double(-1.0),
        deltaRVetoEndcap = cms.bool(True),
        deltaRVetoEndcapCharged = cms.double(0.02),
        deltaRVetoEndcapNeutrals = cms.double(-1.0),
        deltaRVetoEndcapPhotons = cms.double(0.07),
        numberOfCrystalEndcapPhotons = cms.double(4.0),
        numberOfRings = cms.int32(1),
        particleType = cms.int32(1),
        rectangleDeltaEtaVetoBarrelCharged = cms.double(-1),
        rectangleDeltaEtaVetoBarrelNeutrals = cms.double(-1),
        rectangleDeltaEtaVetoBarrelPhotons = cms.double(0.015),
        rectangleDeltaEtaVetoEndcapCharged = cms.double(-1),
        rectangleDeltaEtaVetoEndcapNeutrals = cms.double(-1),
        rectangleDeltaEtaVetoEndcapPhotons = cms.double(-1),
        rectangleDeltaPhiVetoBarrelCharged = cms.double(-1),
        rectangleDeltaPhiVetoBarrelNeutrals = cms.double(-1),
        rectangleDeltaPhiVetoBarrelPhotons = cms.double(1.0),
        rectangleDeltaPhiVetoEndcapCharged = cms.double(-1),
        rectangleDeltaPhiVetoEndcapNeutrals = cms.double(-1),
        rectangleDeltaPhiVetoEndcapPhotons = cms.double(-1),
        rectangleVetoBarrel = cms.bool(True),
        rectangleVetoEndcap = cms.bool(False),
        ringSize = cms.double(0.3),
        useCrystalSize = cms.bool(True)
    ),
    PhotonDNNPFid = cms.PSet(
        enabled = cms.bool(False),
        inputTensorName = cms.string('FirstLayer_input'),
        modelsFiles = cms.vstring(
            'RecoEgamma/PhotonIdentification/data/Photon_PFID_dnn/v1/EB/EB_modelDNN.pb',
            'RecoEgamma/PhotonIdentification/data/Photon_PFID_dnn/v1/EE/EE_modelDNN.pb'
        ),
        outputDim = cms.vuint32(1, 1),
        outputTensorName = cms.string('sequential/FinalLayer/Sigmoid'),
        scalersFiles = cms.vstring(
            'RecoEgamma/PhotonIdentification/data/Photon_PFID_dnn/v1/EB/EB_scaler.txt',
            'RecoEgamma/PhotonIdentification/data/Photon_PFID_dnn/v1/EE/EE_scaler.txt'
        ),
        useEBModelInGap = cms.bool(True)
    ),
    RecHitFlagToBeExcludedEB = cms.vstring(
        'kFaultyHardware',
        'kTowerRecovered',
        'kDead'
    ),
    RecHitFlagToBeExcludedEE = cms.vstring(
        'kFaultyHardware',
        'kNeighboursRecovered',
        'kTowerRecovered',
        'kDead',
        'kWeird'
    ),
    RecHitSeverityToBeExcludedEB = cms.vstring(
        'kWeird',
        'kBad',
        'kTime'
    ),
    RecHitSeverityToBeExcludedEE = cms.vstring(
        'kWeird',
        'kBad',
        'kTime'
    ),
    barrelEcalHits = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    candidateP4type = cms.string('fromEcalEnergy'),
    checkHcalStatus = cms.bool(True),
    ecalRecHitSumEtOffsetBarrel = cms.double(999999999),
    ecalRecHitSumEtOffsetEndcap = cms.double(999999999),
    ecalRecHitSumEtSlopeBarrel = cms.double(0.0),
    ecalRecHitSumEtSlopeEndcap = cms.double(0.0),
    endcapEcalHits = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    energyRegressionWeightsDBLocation = cms.string('wgbrph'),
    energyRegressionWeightsFileLocation = cms.string('/afs/cern.ch/user/b/bendavid/cmspublic/regweights/gbrph.root'),
    hOverEConeSize = cms.double(0.15),
    hbheInstance = cms.string(''),
    hbheModule = cms.string('hbhereco'),
    hbheRecHits = cms.InputTag("hbhereco"),
    hcalRecHitSumEtOffsetBarrel = cms.double(999999999),
    hcalRecHitSumEtOffsetEndcap = cms.double(999999999),
    hcalRecHitSumEtSlopeBarrel = cms.double(0.0),
    hcalRecHitSumEtSlopeEndcap = cms.double(0.0),
    hcalRun2EffDepth = cms.bool(False),
    highEt = cms.double(100.0),
    isolationSumsCalculatorSet = cms.PSet(
        ComponentName = cms.string('isolationSumsCalculator'),
        EcalRecHitEtaSliceA_Barrel = cms.double(2.5),
        EcalRecHitEtaSliceA_Endcap = cms.double(2.5),
        EcalRecHitEtaSliceB_Barrel = cms.double(2.5),
        EcalRecHitEtaSliceB_Endcap = cms.double(2.5),
        EcalRecHitInnerRadiusA_Barrel = cms.double(3.5),
        EcalRecHitInnerRadiusA_Endcap = cms.double(3.5),
        EcalRecHitInnerRadiusB_Barrel = cms.double(3.5),
        EcalRecHitInnerRadiusB_Endcap = cms.double(3.5),
        EcalRecHitOuterRadiusA_Barrel = cms.double(0.4),
        EcalRecHitOuterRadiusA_Endcap = cms.double(0.4),
        EcalRecHitOuterRadiusB_Barrel = cms.double(0.3),
        EcalRecHitOuterRadiusB_Endcap = cms.double(0.3),
        EcalRecHitThreshEA_Barrel = cms.double(0.095),
        EcalRecHitThreshEA_Endcap = cms.double(0.0),
        EcalRecHitThreshEB_Barrel = cms.double(0.095),
        EcalRecHitThreshEB_Endcap = cms.double(0.0),
        EcalRecHitThreshEtA_Barrel = cms.double(0.0),
        EcalRecHitThreshEtA_Endcap = cms.double(0.11),
        EcalRecHitThreshEtB_Barrel = cms.double(0.0),
        EcalRecHitThreshEtB_Endcap = cms.double(0.11),
        HBHERecHitCollection = cms.InputTag("hbhereco"),
        HcalRecHitInnerRadiusA_Barrel = cms.vdouble(
            0.15, 0.15, 0.15, 0.15, 0.15,
            0.15, 0.15
        ),
        HcalRecHitInnerRadiusA_Endcap = cms.vdouble(
            0.15, 0.15, 0.15, 0.15, 0.15,
            0.15, 0.15
        ),
        HcalRecHitInnerRadiusB_Barrel = cms.vdouble(
            0.15, 0.15, 0.15, 0.15, 0.15,
            0.15, 0.15
        ),
        HcalRecHitInnerRadiusB_Endcap = cms.vdouble(
            0.15, 0.15, 0.15, 0.15, 0.15,
            0.15, 0.15
        ),
        HcalRecHitOuterRadiusA_Barrel = cms.vdouble(
            0.4, 0.4, 0.4, 0.4, 0.4,
            0.4, 0.4
        ),
        HcalRecHitOuterRadiusA_Endcap = cms.vdouble(
            0.4, 0.4, 0.4, 0.4, 0.4,
            0.4, 0.4
        ),
        HcalRecHitOuterRadiusB_Barrel = cms.vdouble(
            0.3, 0.3, 0.3, 0.3, 0.3,
            0.3, 0.3
        ),
        HcalRecHitOuterRadiusB_Endcap = cms.vdouble(
            0.3, 0.3, 0.3, 0.3, 0.3,
            0.3, 0.3
        ),
        TrackConeInnerRadiusA_Barrel = cms.double(0.04),
        TrackConeInnerRadiusA_Endcap = cms.double(0.04),
        TrackConeInnerRadiusB_Barrel = cms.double(0.04),
        TrackConeInnerRadiusB_Endcap = cms.double(0.04),
        TrackConeOuterRadiusA_Barrel = cms.double(0.4),
        TrackConeOuterRadiusA_Endcap = cms.double(0.4),
        TrackConeOuterRadiusB_Barrel = cms.double(0.3),
        TrackConeOuterRadiusB_Endcap = cms.double(0.3),
        barrelEcalRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        beamSpotProducer = cms.InputTag("offlineBeamSpot"),
        endcapEcalRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        isolationtrackEtaSliceA_Barrel = cms.double(0.015),
        isolationtrackEtaSliceA_Endcap = cms.double(0.015),
        isolationtrackEtaSliceB_Barrel = cms.double(0.015),
        isolationtrackEtaSliceB_Endcap = cms.double(0.015),
        isolationtrackThresholdA_Barrel = cms.double(0.0),
        isolationtrackThresholdA_Endcap = cms.double(0.0),
        isolationtrackThresholdB_Barrel = cms.double(0.0),
        isolationtrackThresholdB_Endcap = cms.double(0.0),
        longImpactParameterA_Barrel = cms.double(0.2),
        longImpactParameterA_Endcap = cms.double(0.2),
        longImpactParameterB_Barrel = cms.double(0.2),
        longImpactParameterB_Endcap = cms.double(0.2),
        maxHcalRecHitSeverity = cms.int32(9),
        moduleEtaBoundary = cms.vdouble(
            0.0, 0.02, 0.43, 0.46, 0.78,
            0.81, 1.13, 1.15, 1.45, 1.58
        ),
        modulePhiBoundary = cms.double(0.0087),
        recHitEThresholdHB = cms.vdouble(0.1, 0.2, 0.3, 0.3),
        recHitEThresholdHE = cms.vdouble(
            0.1, 0.2, 0.2, 0.2, 0.2,
            0.2, 0.2
        ),
        trackProducer = cms.InputTag("generalTracks"),
        transImpactParameterA_Barrel = cms.double(0.1),
        transImpactParameterA_Endcap = cms.double(0.1),
        transImpactParameterB_Barrel = cms.double(0.1),
        transImpactParameterB_Endcap = cms.double(0.1),
        useNumCrystals = cms.bool(True),
        vetoClustered = cms.bool(False)
    ),
    maxHcalRecHitSeverity = cms.int32(9),
    maxHoverEBarrel = cms.double(0.5),
    maxHoverEEndcap = cms.double(0.5),
    minR9Barrel = cms.double(0.94),
    minR9Endcap = cms.double(0.95),
    minSCEtBarrel = cms.double(10.0),
    minSCEtEndcap = cms.double(10.0),
    mipVariableSet = cms.PSet(
        ComponentName = cms.string('mipVariable'),
        HaloDiscThreshold = cms.double(70.0),
        ResidualWidth = cms.double(0.23),
        XRangeFit = cms.double(180.0),
        YRangeFit = cms.double(7.0),
        barrelEcalRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        endcapEcalRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE")
    ),
    multThresEB = cms.double(1.0),
    multThresEE = cms.double(1.25),
    mvaBasedHaloVariableSet = cms.PSet(
        HBHERecHitsCollection = cms.InputTag("hbhereco"),
        barrelEcalRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        endcapEcalRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        esRecHitCollection = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES"),
        noiseThrES = cms.double(0.0),
        recHitEThresholdHB = cms.vdouble(0.1, 0.2, 0.3, 0.3),
        recHitEThresholdHE = cms.vdouble(
            0.1, 0.2, 0.2, 0.2, 0.2,
            0.2, 0.2
        ),
        rhoLabel = cms.InputTag("fixedGridRhoFastjetAllTmp"),
        trainingFileName = cms.FileInPath('RecoEgamma/PhotonIdentification/data/beamHaloTaggerID/xgboostToTMVA_BHtagger.root')
    ),
    nTrackHollowConeBarrel = cms.double(999999999),
    nTrackHollowConeEndcap = cms.double(999999999),
    nTrackSolidConeBarrel = cms.double(999999999),
    nTrackSolidConeEndcap = cms.double(999999999),
    outputPhotonCollection = cms.string(''),
    pfCandidates = cms.InputTag("particleFlowTmp"),
    pfECALClusIsolCfg = cms.PSet(
        drMax = cms.double(0.3),
        drVetoBarrel = cms.double(0),
        drVetoEndcap = cms.double(0),
        energyBarrel = cms.double(0),
        energyEndcap = cms.double(0),
        etaStripBarrel = cms.double(0),
        etaStripEndcap = cms.double(0),
        pfClusterProducer = cms.InputTag("particleFlowClusterECAL")
    ),
    pfECALClusIsolation = cms.InputTag("ootPhotonEcalPFClusterIsolationProducer"),
    pfEgammaCandidates = cms.InputTag(""),
    pfHCALClusIsolCfg = cms.PSet(
        drMax = cms.double(0.3),
        drVetoBarrel = cms.double(0),
        drVetoEndcap = cms.double(0),
        energyBarrel = cms.double(0),
        energyEndcap = cms.double(0),
        etaStripBarrel = cms.double(0),
        etaStripEndcap = cms.double(0),
        pfClusterProducerHCAL = cms.InputTag("particleFlowClusterHCAL"),
        pfClusterProducerHFEM = cms.InputTag(""),
        pfClusterProducerHFHAD = cms.InputTag(""),
        useEt = cms.bool(True),
        useHF = cms.bool(False)
    ),
    pfHCALClusIsolation = cms.InputTag("ootPhotonHcalPFClusterIsolationProducer"),
    pfIsolCfg = cms.PSet(
        chargedHadronIso = cms.InputTag(""),
        chargedHadronPFPVIso = cms.InputTag(""),
        chargedHadronWorstVtxGeomVetoIso = cms.InputTag(""),
        chargedHadronWorstVtxIso = cms.InputTag(""),
        neutralHadronIso = cms.InputTag(""),
        photonIso = cms.InputTag("")
    ),
    photonEcalEnergyCorrFunction = cms.string('EcalClusterEnergyCorrectionObjectSpecific'),
    photonProducer = cms.InputTag("ootPhotonsTmp"),
    posCalcParameters = cms.PSet(
        LogWeighted = cms.bool(True),
        T0_barl = cms.double(7.4),
        T0_endc = cms.double(6.3),
        T0_endcPresh = cms.double(3.6),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89)
    ),
    posCalc_logweight = cms.bool(True),
    posCalc_t0_barl = cms.double(7.7),
    posCalc_t0_endc = cms.double(6.3),
    posCalc_t0_endcPresh = cms.double(3.6),
    posCalc_w0 = cms.double(4.2),
    posCalc_x0 = cms.double(0.89),
    preshowerHits = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES"),
    primaryVertexProducer = cms.InputTag("offlinePrimaryVerticesWithBS"),
    recHitEThresholdHB = cms.vdouble(0.1, 0.2, 0.3, 0.3),
    recHitEThresholdHE = cms.vdouble(
        0.1, 0.2, 0.2, 0.2, 0.2,
        0.2, 0.2
    ),
    reconstructionStep = cms.string('ootfinal'),
    regressionWeightsFromDB = cms.bool(True),
    runMIPTagger = cms.bool(True),
    runMVABasedHaloTagger = cms.bool(True),
    sigmaIetaIetaCutBarrel = cms.double(999999999),
    sigmaIetaIetaCutEndcap = cms.double(999999999),
    superClusterCrackEnergyCorrFunction = cms.string('EcalClusterCrackCorrection'),
    superClusterEnergyCorrFunction = cms.string('EcalClusterEnergyCorrection'),
    superClusterEnergyErrorFunction = cms.string('EcalClusterEnergyUncertainty'),
    trackPtSumHollowConeBarrel = cms.double(999999999),
    trackPtSumHollowConeEndcap = cms.double(999999999),
    trackPtSumSolidConeBarrel = cms.double(999999999),
    trackPtSumSolidConeEndcap = cms.double(999999999),
    usePrimaryVertex = cms.bool(True),
    useRegression = cms.bool(True),
    valueMapPhotons = cms.string('')
)


process.ootPhotonsTmp = cms.EDProducer("GEDPhotonProducer",
    PFIsolationCalculatorSet = cms.PSet(
        ComponentName = cms.string('pfIsolationCalculator'),
        applyDzDxyVeto = cms.bool(True),
        applyMissHitPhVeto = cms.bool(False),
        applyPFPUVeto = cms.bool(True),
        applyVeto = cms.bool(True),
        checkClosestZVertex = cms.bool(True),
        coneDR = cms.double(0.3),
        deltaRVetoBarrel = cms.bool(True),
        deltaRVetoBarrelCharged = cms.double(0.02),
        deltaRVetoBarrelNeutrals = cms.double(-1.0),
        deltaRVetoBarrelPhotons = cms.double(-1.0),
        deltaRVetoEndcap = cms.bool(True),
        deltaRVetoEndcapCharged = cms.double(0.02),
        deltaRVetoEndcapNeutrals = cms.double(-1.0),
        deltaRVetoEndcapPhotons = cms.double(0.07),
        numberOfCrystalEndcapPhotons = cms.double(4.0),
        numberOfRings = cms.int32(1),
        particleType = cms.int32(1),
        rectangleDeltaEtaVetoBarrelCharged = cms.double(-1),
        rectangleDeltaEtaVetoBarrelNeutrals = cms.double(-1),
        rectangleDeltaEtaVetoBarrelPhotons = cms.double(0.015),
        rectangleDeltaEtaVetoEndcapCharged = cms.double(-1),
        rectangleDeltaEtaVetoEndcapNeutrals = cms.double(-1),
        rectangleDeltaEtaVetoEndcapPhotons = cms.double(-1),
        rectangleDeltaPhiVetoBarrelCharged = cms.double(-1),
        rectangleDeltaPhiVetoBarrelNeutrals = cms.double(-1),
        rectangleDeltaPhiVetoBarrelPhotons = cms.double(1.0),
        rectangleDeltaPhiVetoEndcapCharged = cms.double(-1),
        rectangleDeltaPhiVetoEndcapNeutrals = cms.double(-1),
        rectangleDeltaPhiVetoEndcapPhotons = cms.double(-1),
        rectangleVetoBarrel = cms.bool(True),
        rectangleVetoEndcap = cms.bool(False),
        ringSize = cms.double(0.3),
        useCrystalSize = cms.bool(True)
    ),
    PhotonDNNPFid = cms.PSet(
        enabled = cms.bool(False),
        inputTensorName = cms.string('FirstLayer_input'),
        modelsFiles = cms.vstring(
            'RecoEgamma/PhotonIdentification/data/Photon_PFID_dnn/v1/EB/EB_modelDNN.pb',
            'RecoEgamma/PhotonIdentification/data/Photon_PFID_dnn/v1/EE/EE_modelDNN.pb'
        ),
        outputDim = cms.vuint32(1, 1),
        outputTensorName = cms.string('sequential/FinalLayer/Sigmoid'),
        scalersFiles = cms.vstring(
            'RecoEgamma/PhotonIdentification/data/Photon_PFID_dnn/v1/EB/EB_scaler.txt',
            'RecoEgamma/PhotonIdentification/data/Photon_PFID_dnn/v1/EE/EE_scaler.txt'
        ),
        useEBModelInGap = cms.bool(True)
    ),
    RecHitFlagToBeExcludedEB = cms.vstring(
        'kFaultyHardware',
        'kTowerRecovered',
        'kDead'
    ),
    RecHitFlagToBeExcludedEE = cms.vstring(
        'kFaultyHardware',
        'kNeighboursRecovered',
        'kTowerRecovered',
        'kDead',
        'kWeird'
    ),
    RecHitSeverityToBeExcludedEB = cms.vstring(
        'kWeird',
        'kBad',
        'kTime'
    ),
    RecHitSeverityToBeExcludedEE = cms.vstring(
        'kWeird',
        'kBad',
        'kTime'
    ),
    barrelEcalHits = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    candidateP4type = cms.string('fromEcalEnergy'),
    checkHcalStatus = cms.bool(True),
    ecalRecHitSumEtOffsetBarrel = cms.double(999999999),
    ecalRecHitSumEtOffsetEndcap = cms.double(999999999),
    ecalRecHitSumEtSlopeBarrel = cms.double(0.0),
    ecalRecHitSumEtSlopeEndcap = cms.double(0.0),
    endcapEcalHits = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    energyRegressionWeightsDBLocation = cms.string('wgbrph'),
    energyRegressionWeightsFileLocation = cms.string('/afs/cern.ch/user/b/bendavid/cmspublic/regweights/gbrph.root'),
    hOverEConeSize = cms.double(0.15),
    hbheInstance = cms.string(''),
    hbheModule = cms.string('hbhereco'),
    hbheRecHits = cms.InputTag("hbhereco"),
    hcalRecHitSumEtOffsetBarrel = cms.double(999999999),
    hcalRecHitSumEtOffsetEndcap = cms.double(999999999),
    hcalRecHitSumEtSlopeBarrel = cms.double(0.0),
    hcalRecHitSumEtSlopeEndcap = cms.double(0.0),
    hcalRun2EffDepth = cms.bool(False),
    highEt = cms.double(100.0),
    isolationSumsCalculatorSet = cms.PSet(
        ComponentName = cms.string('isolationSumsCalculator'),
        EcalRecHitEtaSliceA_Barrel = cms.double(2.5),
        EcalRecHitEtaSliceA_Endcap = cms.double(2.5),
        EcalRecHitEtaSliceB_Barrel = cms.double(2.5),
        EcalRecHitEtaSliceB_Endcap = cms.double(2.5),
        EcalRecHitInnerRadiusA_Barrel = cms.double(3.5),
        EcalRecHitInnerRadiusA_Endcap = cms.double(3.5),
        EcalRecHitInnerRadiusB_Barrel = cms.double(3.5),
        EcalRecHitInnerRadiusB_Endcap = cms.double(3.5),
        EcalRecHitOuterRadiusA_Barrel = cms.double(0.4),
        EcalRecHitOuterRadiusA_Endcap = cms.double(0.4),
        EcalRecHitOuterRadiusB_Barrel = cms.double(0.3),
        EcalRecHitOuterRadiusB_Endcap = cms.double(0.3),
        EcalRecHitThreshEA_Barrel = cms.double(0.095),
        EcalRecHitThreshEA_Endcap = cms.double(0.0),
        EcalRecHitThreshEB_Barrel = cms.double(0.095),
        EcalRecHitThreshEB_Endcap = cms.double(0.0),
        EcalRecHitThreshEtA_Barrel = cms.double(0.0),
        EcalRecHitThreshEtA_Endcap = cms.double(0.11),
        EcalRecHitThreshEtB_Barrel = cms.double(0.0),
        EcalRecHitThreshEtB_Endcap = cms.double(0.11),
        HBHERecHitCollection = cms.InputTag("hbhereco"),
        HcalRecHitInnerRadiusA_Barrel = cms.vdouble(
            0.15, 0.15, 0.15, 0.15, 0.15,
            0.15, 0.15
        ),
        HcalRecHitInnerRadiusA_Endcap = cms.vdouble(
            0.15, 0.15, 0.15, 0.15, 0.15,
            0.15, 0.15
        ),
        HcalRecHitInnerRadiusB_Barrel = cms.vdouble(
            0.15, 0.15, 0.15, 0.15, 0.15,
            0.15, 0.15
        ),
        HcalRecHitInnerRadiusB_Endcap = cms.vdouble(
            0.15, 0.15, 0.15, 0.15, 0.15,
            0.15, 0.15
        ),
        HcalRecHitOuterRadiusA_Barrel = cms.vdouble(
            0.4, 0.4, 0.4, 0.4, 0.4,
            0.4, 0.4
        ),
        HcalRecHitOuterRadiusA_Endcap = cms.vdouble(
            0.4, 0.4, 0.4, 0.4, 0.4,
            0.4, 0.4
        ),
        HcalRecHitOuterRadiusB_Barrel = cms.vdouble(
            0.3, 0.3, 0.3, 0.3, 0.3,
            0.3, 0.3
        ),
        HcalRecHitOuterRadiusB_Endcap = cms.vdouble(
            0.3, 0.3, 0.3, 0.3, 0.3,
            0.3, 0.3
        ),
        TrackConeInnerRadiusA_Barrel = cms.double(0.04),
        TrackConeInnerRadiusA_Endcap = cms.double(0.04),
        TrackConeInnerRadiusB_Barrel = cms.double(0.04),
        TrackConeInnerRadiusB_Endcap = cms.double(0.04),
        TrackConeOuterRadiusA_Barrel = cms.double(0.4),
        TrackConeOuterRadiusA_Endcap = cms.double(0.4),
        TrackConeOuterRadiusB_Barrel = cms.double(0.3),
        TrackConeOuterRadiusB_Endcap = cms.double(0.3),
        barrelEcalRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        beamSpotProducer = cms.InputTag("offlineBeamSpot"),
        endcapEcalRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        isolationtrackEtaSliceA_Barrel = cms.double(0.015),
        isolationtrackEtaSliceA_Endcap = cms.double(0.015),
        isolationtrackEtaSliceB_Barrel = cms.double(0.015),
        isolationtrackEtaSliceB_Endcap = cms.double(0.015),
        isolationtrackThresholdA_Barrel = cms.double(0.0),
        isolationtrackThresholdA_Endcap = cms.double(0.0),
        isolationtrackThresholdB_Barrel = cms.double(0.0),
        isolationtrackThresholdB_Endcap = cms.double(0.0),
        longImpactParameterA_Barrel = cms.double(0.2),
        longImpactParameterA_Endcap = cms.double(0.2),
        longImpactParameterB_Barrel = cms.double(0.2),
        longImpactParameterB_Endcap = cms.double(0.2),
        maxHcalRecHitSeverity = cms.int32(9),
        moduleEtaBoundary = cms.vdouble(
            0.0, 0.02, 0.43, 0.46, 0.78,
            0.81, 1.13, 1.15, 1.45, 1.58
        ),
        modulePhiBoundary = cms.double(0.0087),
        recHitEThresholdHB = cms.vdouble(0.1, 0.2, 0.3, 0.3),
        recHitEThresholdHE = cms.vdouble(
            0.1, 0.2, 0.2, 0.2, 0.2,
            0.2, 0.2
        ),
        trackProducer = cms.InputTag("generalTracks"),
        transImpactParameterA_Barrel = cms.double(0.1),
        transImpactParameterA_Endcap = cms.double(0.1),
        transImpactParameterB_Barrel = cms.double(0.1),
        transImpactParameterB_Endcap = cms.double(0.1),
        useNumCrystals = cms.bool(True),
        vetoClustered = cms.bool(False)
    ),
    maxHcalRecHitSeverity = cms.int32(9),
    maxHoverEBarrel = cms.double(0.5),
    maxHoverEEndcap = cms.double(0.5),
    minR9Barrel = cms.double(0.94),
    minR9Endcap = cms.double(0.95),
    minSCEtBarrel = cms.double(10.0),
    minSCEtEndcap = cms.double(10.0),
    mipVariableSet = cms.PSet(
        ComponentName = cms.string('mipVariable'),
        HaloDiscThreshold = cms.double(70.0),
        ResidualWidth = cms.double(0.23),
        XRangeFit = cms.double(180.0),
        YRangeFit = cms.double(7.0),
        barrelEcalRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        endcapEcalRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE")
    ),
    multThresEB = cms.double(1.0),
    multThresEE = cms.double(1.25),
    mvaBasedHaloVariableSet = cms.PSet(
        HBHERecHitsCollection = cms.InputTag("hbhereco"),
        barrelEcalRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        endcapEcalRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        esRecHitCollection = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES"),
        noiseThrES = cms.double(0.0),
        recHitEThresholdHB = cms.vdouble(0.1, 0.2, 0.3, 0.3),
        recHitEThresholdHE = cms.vdouble(
            0.1, 0.2, 0.2, 0.2, 0.2,
            0.2, 0.2
        ),
        rhoLabel = cms.InputTag("fixedGridRhoFastjetAllTmp"),
        trainingFileName = cms.FileInPath('RecoEgamma/PhotonIdentification/data/beamHaloTaggerID/xgboostToTMVA_BHtagger.root')
    ),
    nTrackHollowConeBarrel = cms.double(999999999),
    nTrackHollowConeEndcap = cms.double(999999999),
    nTrackSolidConeBarrel = cms.double(999999999),
    nTrackSolidConeEndcap = cms.double(999999999),
    outputPhotonCollection = cms.string(''),
    pfCandidates = cms.InputTag("particleFlowTmp"),
    pfECALClusIsolCfg = cms.PSet(
        drMax = cms.double(0.3),
        drVetoBarrel = cms.double(0),
        drVetoEndcap = cms.double(0),
        energyBarrel = cms.double(0),
        energyEndcap = cms.double(0),
        etaStripBarrel = cms.double(0),
        etaStripEndcap = cms.double(0),
        pfClusterProducer = cms.InputTag("particleFlowClusterECAL")
    ),
    pfEgammaCandidates = cms.InputTag(""),
    pfHCALClusIsolCfg = cms.PSet(
        drMax = cms.double(0.3),
        drVetoBarrel = cms.double(0),
        drVetoEndcap = cms.double(0),
        energyBarrel = cms.double(0),
        energyEndcap = cms.double(0),
        etaStripBarrel = cms.double(0),
        etaStripEndcap = cms.double(0),
        pfClusterProducerHCAL = cms.InputTag("particleFlowClusterHCAL"),
        pfClusterProducerHFEM = cms.InputTag(""),
        pfClusterProducerHFHAD = cms.InputTag(""),
        useEt = cms.bool(True),
        useHF = cms.bool(False)
    ),
    photonEcalEnergyCorrFunction = cms.string('EcalClusterEnergyCorrectionObjectSpecific'),
    photonProducer = cms.InputTag("ootPhotonCore"),
    posCalcParameters = cms.PSet(
        LogWeighted = cms.bool(True),
        T0_barl = cms.double(7.4),
        T0_endc = cms.double(6.3),
        T0_endcPresh = cms.double(3.6),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89)
    ),
    posCalc_logweight = cms.bool(True),
    posCalc_t0_barl = cms.double(7.7),
    posCalc_t0_endc = cms.double(6.3),
    posCalc_t0_endcPresh = cms.double(3.6),
    posCalc_w0 = cms.double(4.2),
    posCalc_x0 = cms.double(0.89),
    preshowerHits = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES"),
    primaryVertexProducer = cms.InputTag("offlinePrimaryVerticesWithBS"),
    recHitEThresholdHB = cms.vdouble(0.1, 0.2, 0.3, 0.3),
    recHitEThresholdHE = cms.vdouble(
        0.1, 0.2, 0.2, 0.2, 0.2,
        0.2, 0.2
    ),
    reconstructionStep = cms.string('oot'),
    regressionWeightsFromDB = cms.bool(True),
    runMIPTagger = cms.bool(True),
    runMVABasedHaloTagger = cms.bool(True),
    sigmaIetaIetaCutBarrel = cms.double(999999999),
    sigmaIetaIetaCutEndcap = cms.double(999999999),
    superClusterCrackEnergyCorrFunction = cms.string('EcalClusterCrackCorrection'),
    superClusterEnergyCorrFunction = cms.string('EcalClusterEnergyCorrection'),
    superClusterEnergyErrorFunction = cms.string('EcalClusterEnergyUncertainty'),
    trackPtSumHollowConeBarrel = cms.double(999999999),
    trackPtSumHollowConeEndcap = cms.double(999999999),
    trackPtSumSolidConeBarrel = cms.double(999999999),
    trackPtSumSolidConeEndcap = cms.double(999999999),
    usePrimaryVertex = cms.bool(True),
    useRegression = cms.bool(True),
    valueMapPhotons = cms.string('')
)


process.particleFlowClusterECAL = cms.EDProducer("CorrectedECALPFClusterProducer",
    energyCorrector = cms.PSet(
        applyCrackCorrections = cms.bool(False),
        applyMVACorrections = cms.bool(True),
        autoDetectBunchSpacing = cms.bool(True),
        bunchSpacing = cms.int32(25),
        ebSrFlagLabel = cms.InputTag("ecalDigis"),
        eeSrFlagLabel = cms.InputTag("ecalDigis"),
        maxPtForMVAEvaluation = cms.double(300.0),
        recHitsEBLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        recHitsEELabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        setEnergyUncertainty = cms.bool(False),
        srfAwareCorrection = cms.bool(True)
    ),
    inputECAL = cms.InputTag("particleFlowClusterECALUncorrected"),
    inputPS = cms.InputTag("particleFlowClusterPS"),
    mightGet = cms.optional.untracked.vstring,
    minimumPSEnergy = cms.double(0),
    skipPS = cms.bool(False)
)


process.particleFlowClusterECALUncorrected = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                gatheringThreshold = cms.double(0.08),
                gatheringThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                gatheringThreshold = cms.double(0.3),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.1088899999982),
                noiseTermLowE = cms.double(1.3188299999994002),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.724899999994),
                noiseTermLowE = cms.double(6.926830000006),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(9),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.1088899999982),
                noiseTermLowE = cms.double(1.3188299999994002),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.724899999994),
                noiseTermLowE = cms.double(6.926830000006),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        positionCalcForConvergence = cms.PSet(
            T0_EB = cms.double(7.4),
            T0_EE = cms.double(3.1),
            T0_ES = cms.double(1.2),
            W0 = cms.double(4.2),
            X0 = cms.double(0.89),
            algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
            minAllowedNormalization = cms.double(0.0),
            minFractionInCalc = cms.double(0.0)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                recHitEnergyNorm = cms.double(0.08)
            ),
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.3)
            )
        ),
        showerSigma = cms.double(1.5),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(
        T0_EB = cms.double(7.4),
        T0_EE = cms.double(3.1),
        T0_ES = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89),
        algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
        minAllowedNormalization = cms.double(0.0),
        minFractionInCalc = cms.double(0.0)
    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("particleFlowRecHitECAL"),
    seedCleaners = cms.VPSet(cms.PSet(
        RecHitFlagsToBeExcluded = cms.vstring(),
        algoName = cms.string('FlagsCleanerECAL')
    )),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(8),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                seedingThreshold = cms.double(0.6),
                seedingThresholdPt = cms.double(0.15)
            ),
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                seedingThreshold = cms.double(0.23),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    )
)


process.particleFlowClusterOOTECAL = cms.EDProducer("CorrectedECALPFClusterProducer",
    energyCorrector = cms.PSet(
        applyCrackCorrections = cms.bool(False),
        applyMVACorrections = cms.bool(True),
        autoDetectBunchSpacing = cms.bool(True),
        bunchSpacing = cms.int32(25),
        ebSrFlagLabel = cms.InputTag("ecalDigis"),
        eeSrFlagLabel = cms.InputTag("ecalDigis"),
        maxPtForMVAEvaluation = cms.double(300.0),
        recHitsEBLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        recHitsEELabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        setEnergyUncertainty = cms.bool(False),
        srfAwareCorrection = cms.bool(True)
    ),
    inputECAL = cms.InputTag("particleFlowClusterOOTECALUncorrected"),
    inputPS = cms.InputTag("particleFlowClusterPS"),
    mightGet = cms.optional.untracked.vstring,
    minimumPSEnergy = cms.double(0),
    skipPS = cms.bool(False)
)


process.particleFlowClusterOOTECALUncorrected = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                gatheringThreshold = cms.double(0.08),
                gatheringThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                gatheringThreshold = cms.double(0.3),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.1088899999982),
                noiseTermLowE = cms.double(1.3188299999994002),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.724899999994),
                noiseTermLowE = cms.double(6.926830000006),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(9),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.1088899999982),
                noiseTermLowE = cms.double(1.3188299999994002),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.724899999994),
                noiseTermLowE = cms.double(6.926830000006),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        positionCalcForConvergence = cms.PSet(
            T0_EB = cms.double(7.4),
            T0_EE = cms.double(3.1),
            T0_ES = cms.double(1.2),
            W0 = cms.double(4.2),
            X0 = cms.double(0.89),
            algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
            minAllowedNormalization = cms.double(0.0),
            minFractionInCalc = cms.double(0.0)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                recHitEnergyNorm = cms.double(0.08)
            ),
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.3)
            )
        ),
        showerSigma = cms.double(1.5),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(
        T0_EB = cms.double(7.4),
        T0_EE = cms.double(3.1),
        T0_ES = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89),
        algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
        minAllowedNormalization = cms.double(0.0),
        minFractionInCalc = cms.double(0.0)
    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("particleFlowRecHitOOTECAL"),
    seedCleaners = cms.VPSet(cms.PSet(
        RecHitFlagsToBeExcluded = cms.vstring(),
        algoName = cms.string('FlagsCleanerECAL')
    )),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(8),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                seedingThreshold = cms.double(0.6),
                seedingThresholdPt = cms.double(0.15)
            ),
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                seedingThreshold = cms.double(0.23),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    )
)


process.particleFlowClusterPS = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(False)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(6e-05),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                recHitEnergyNorm = cms.double(6e-05)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                recHitEnergyNorm = cms.double(6e-05)
            )
        ),
        showerSigma = cms.double(0.3),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("particleFlowRecHitPS"),
    seedCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    )
)


process.particleFlowPtrs = cms.EDProducer("PFCandidateFwdPtrProducer",
    src = cms.InputTag("particleFlow")
)


process.particleFlowRecHitECAL = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        barrel = cms.PSet(

        ),
        endcap = cms.PSet(

        ),
        name = cms.string('PFRecHitECALNavigator')
    ),
    producers = cms.VPSet(
        cms.PSet(
            name = cms.string('PFEBRecHitCreator'),
            qualityTests = cms.VPSet(
                cms.PSet(
                    applySelectionsToAllCrystals = cms.bool(True),
                    name = cms.string('PFRecHitQTestDBThreshold')
                ),
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )
            ),
            srFlags = cms.InputTag(""),
            src = cms.InputTag("ecalRecHit","EcalRecHitsEB")
        ),
        cms.PSet(
            name = cms.string('PFEERecHitCreator'),
            qualityTests = cms.VPSet(
                cms.PSet(
                    applySelectionsToAllCrystals = cms.bool(True),
                    name = cms.string('PFRecHitQTestDBThreshold')
                ),
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )
            ),
            srFlags = cms.InputTag(""),
            src = cms.InputTag("ecalRecHit","EcalRecHitsEE")
        )
    )
)


process.particleFlowRecHitOOTECAL = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        barrel = cms.PSet(

        ),
        endcap = cms.PSet(

        ),
        name = cms.string('PFRecHitECALNavigator')
    ),
    producers = cms.VPSet(
        cms.PSet(
            name = cms.string('PFEBRecHitCreator'),
            qualityTests = cms.VPSet(
                cms.PSet(
                    applySelectionsToAllCrystals = cms.bool(True),
                    name = cms.string('PFRecHitQTestDBThreshold')
                ),
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(False),
                    topologicalCleaning = cms.bool(True)
                )
            ),
            srFlags = cms.InputTag(""),
            src = cms.InputTag("ecalRecHit","EcalRecHitsEB")
        ),
        cms.PSet(
            name = cms.string('PFEERecHitCreator'),
            qualityTests = cms.VPSet(
                cms.PSet(
                    applySelectionsToAllCrystals = cms.bool(True),
                    name = cms.string('PFRecHitQTestDBThreshold')
                ),
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(False),
                    topologicalCleaning = cms.bool(True)
                )
            ),
            srFlags = cms.InputTag(""),
            src = cms.InputTag("ecalRecHit","EcalRecHitsEE")
        )
    )
)


process.particleFlowRecHitPS = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        name = cms.string('PFRecHitPreshowerNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFPSRecHitCreator'),
        qualityTests = cms.VPSet(
            cms.PSet(
                name = cms.string('PFRecHitQTestThreshold'),
                threshold = cms.double(0.0)
            ),
            cms.PSet(
                cleaningThreshold = cms.double(0.0),
                name = cms.string('PFRecHitQTestES'),
                topologicalCleaning = cms.bool(True)
            )
        ),
        src = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES")
    ))
)


process.particleFlowSuperClusterECAL = cms.EDProducer("PFECALSuperClusterProducer",
    BeamSpot = cms.InputTag("offlineBeamSpot"),
    ClusteringType = cms.string('Mustache'),
    ESAssociation = cms.InputTag("particleFlowClusterECAL"),
    EnergyWeight = cms.string('Raw'),
    PFBasicClusterCollectionBarrel = cms.string('particleFlowBasicClusterECALBarrel'),
    PFBasicClusterCollectionEndcap = cms.string('particleFlowBasicClusterECALEndcap'),
    PFBasicClusterCollectionPreshower = cms.string('particleFlowBasicClusterECALPreshower'),
    PFClusters = cms.InputTag("particleFlowClusterECAL"),
    PFSuperClusterCollectionBarrel = cms.string('particleFlowSuperClusterECALBarrel'),
    PFSuperClusterCollectionEndcap = cms.string('particleFlowSuperClusterECALEndcap'),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string('particleFlowSuperClusterECALEndcapWithPreshower'),
    applyCrackCorrections = cms.bool(False),
    barrelRecHits = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    doSatelliteClusterMerge = cms.bool(False),
    dropUnseedable = cms.bool(False),
    endcapRecHits = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    etawidth_SuperClusterBarrel = cms.double(0.04),
    etawidth_SuperClusterEndcap = cms.double(0.04),
    isOOTCollection = cms.bool(False),
    mightGet = cms.optional.untracked.vstring,
    phiwidth_SuperClusterBarrel = cms.double(0.2),
    phiwidth_SuperClusterEndcap = cms.double(0.2),
    regressionConfig = cms.PSet(
        applySigmaIetaIphiBug = cms.bool(False),
        eRecHitThreshold = cms.double(1),
        ecalRecHitsEB = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        ecalRecHitsEE = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        hgcalCylinderR = cms.double(2.799999952316284),
        hgcalRecHits = cms.InputTag(""),
        isHLT = cms.bool(False),
        isPhaseII = cms.bool(False),
        regTrainedWithPS = cms.bool(True),
        regressionKeyEB = cms.string('pfscecal_EBCorrection_offline_v2'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_offline_v2'),
        regressionMaxEB = cms.double(2),
        regressionMaxEE = cms.double(2),
        regressionMinEB = cms.double(0.2),
        regressionMinEE = cms.double(0.2),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_offline_v2'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_offline_v2'),
        uncertaintyMaxEB = cms.double(0.5),
        uncertaintyMaxEE = cms.double(0.5),
        uncertaintyMinEB = cms.double(0.0002),
        uncertaintyMinEE = cms.double(0.0002),
        vertexCollection = cms.InputTag("offlinePrimaryVertices")
    ),
    satelliteClusterSeedThreshold = cms.double(50),
    satelliteMajorityFraction = cms.double(0.5),
    seedThresholdIsET = cms.bool(True),
    thresh_PFClusterBarrel = cms.double(0),
    thresh_PFClusterES = cms.double(0),
    thresh_PFClusterEndcap = cms.double(0),
    thresh_PFClusterSeedBarrel = cms.double(1),
    thresh_PFClusterSeedEndcap = cms.double(1),
    thresh_SCEt = cms.double(4),
    useDynamicDPhiWindow = cms.bool(False),
    useRegression = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.particleFlowSuperClusterOOTECAL = cms.EDProducer("PFECALSuperClusterProducer",
    BeamSpot = cms.InputTag("offlineBeamSpot"),
    ClusteringType = cms.string('Mustache'),
    ESAssociation = cms.InputTag("particleFlowClusterOOTECAL"),
    EnergyWeight = cms.string('Raw'),
    PFBasicClusterCollectionBarrel = cms.string('particleFlowBasicClusterOOTECALBarrel'),
    PFBasicClusterCollectionEndcap = cms.string('particleFlowBasicClusterOOTECALEndcap'),
    PFBasicClusterCollectionPreshower = cms.string('particleFlowBasicClusterOOTECALPreshower'),
    PFClusters = cms.InputTag("particleFlowClusterOOTECAL"),
    PFSuperClusterCollectionBarrel = cms.string('particleFlowSuperClusterOOTECALBarrel'),
    PFSuperClusterCollectionEndcap = cms.string('particleFlowSuperClusterOOTECALEndcap'),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string('particleFlowSuperClusterOOTECALEndcapWithPreshower'),
    applyCrackCorrections = cms.bool(False),
    barrelRecHits = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    doSatelliteClusterMerge = cms.bool(False),
    dropUnseedable = cms.bool(False),
    endcapRecHits = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    etawidth_SuperClusterBarrel = cms.double(0.04),
    etawidth_SuperClusterEndcap = cms.double(0.04),
    isOOTCollection = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    phiwidth_SuperClusterBarrel = cms.double(0.2),
    phiwidth_SuperClusterEndcap = cms.double(0.2),
    regressionConfig = cms.PSet(
        applySigmaIetaIphiBug = cms.bool(False),
        eRecHitThreshold = cms.double(1),
        ecalRecHitsEB = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        ecalRecHitsEE = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        hgcalCylinderR = cms.double(2.799999952316284),
        hgcalRecHits = cms.InputTag(""),
        isHLT = cms.bool(False),
        isPhaseII = cms.bool(False),
        regTrainedWithPS = cms.bool(True),
        regressionKeyEB = cms.string('pfscecal_EBCorrection_offline_v2'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_offline_v2'),
        regressionMaxEB = cms.double(2),
        regressionMaxEE = cms.double(2),
        regressionMinEB = cms.double(0.2),
        regressionMinEE = cms.double(0.2),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_offline_v2'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_offline_v2'),
        uncertaintyMaxEB = cms.double(0.5),
        uncertaintyMaxEE = cms.double(0.5),
        uncertaintyMinEB = cms.double(0.0002),
        uncertaintyMinEE = cms.double(0.0002),
        vertexCollection = cms.InputTag("offlinePrimaryVertices")
    ),
    satelliteClusterSeedThreshold = cms.double(50),
    satelliteMajorityFraction = cms.double(0.5),
    seedThresholdIsET = cms.bool(True),
    thresh_PFClusterBarrel = cms.double(0),
    thresh_PFClusterES = cms.double(0),
    thresh_PFClusterEndcap = cms.double(0),
    thresh_PFClusterSeedBarrel = cms.double(1),
    thresh_PFClusterSeedEndcap = cms.double(1),
    thresh_SCEt = cms.double(4),
    useDynamicDPhiWindow = cms.bool(False),
    useRegression = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.patDisplacedMuons = cms.EDProducer("PATMuonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(False),
    addInverseBeta = cms.bool(True),
    addPuppiIsolation = cms.bool(False),
    addResolutions = cms.bool(False),
    addTriggerMatching = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    caloMETMuonCorrs = cms.InputTag("muonMETValueMapProducer","muCorrData"),
    computeMiniIso = cms.bool(False),
    computeMuonIDMVA = cms.bool(False),
    computeMuonMVA = cms.bool(False),
    computePuppiCombinedIso = cms.bool(False),
    computeSoftMuonMVA = cms.bool(False),
    effectiveAreaVec = cms.vdouble(0.0566, 0.0562, 0.0363, 0.0119, 0.0064),
    efficiencies = cms.PSet(

    ),
    embedCaloMETMuonCorrs = cms.bool(False),
    embedCombinedMuon = cms.bool(True),
    embedDytMuon = cms.bool(False),
    embedGenMatch = cms.bool(False),
    embedHighLevelSelection = cms.bool(True),
    embedMuonBestTrack = cms.bool(True),
    embedPFCandidate = cms.bool(False),
    embedPfEcalEnergy = cms.bool(False),
    embedPickyMuon = cms.bool(False),
    embedStandAloneMuon = cms.bool(True),
    embedTcMETMuonCorrs = cms.bool(False),
    embedTpfmsMuon = cms.bool(False),
    embedTrack = cms.bool(True),
    embedTunePMuonBestTrack = cms.bool(True),
    forceBestTrackEmbedding = cms.bool(False),
    genParticleMatch = cms.InputTag("displacedMuonMatch"),
    hltCollectionFilters = cms.vstring('*'),
    isoDeposits = cms.PSet(

    ),
    isolationValues = cms.PSet(

    ),
    lowPtmvaTrainingFile = cms.FileInPath('RecoMuon/MuonIdentification/data/mu_lowpt_BDTG.weights.xml'),
    miniIsoParams = cms.vdouble(
        0.05, 0.2, 10.0, 0.5, 0.0001,
        0.01, 0.01, 0.01, 0.0
    ),
    muonSimInfo = cms.InputTag("displacedMuonSimClassifier"),
    muonSource = cms.InputTag("filteredDisplacedMuons"),
    mvaDrMax = cms.double(0.4),
    mvaIDTrainingFile = cms.FileInPath('RecoMuon/MuonIdentification/data/mvaID.onnx'),
    mvaJetTag = cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
    mvaL1Corrector = cms.InputTag("ak4PFCHSL1FastjetCorrector"),
    mvaL1L2L3ResCorrector = cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
    mvaTrainingFile = cms.FileInPath('RecoMuon/MuonIdentification/data/mu_2017_BDTG.weights.xml'),
    mvaUseJec = cms.bool(False),
    pfCandsForMiniIso = cms.InputTag("packedPFCandidates"),
    pfMuonSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    recomputeBasicSelectors = cms.bool(False),
    resolutions = cms.PSet(

    ),
    rho = cms.InputTag("fixedGridRhoFastjetCentralNeutral"),
    softMvaTrainingFile = cms.FileInPath('RecoMuon/MuonIdentification/data/TMVA-muonid-bmm4-B-25.weights.xml'),
    sourceMuonTimeExtra = cms.InputTag("filteredDisplacedMuons","combined"),
    tcMETMuonCorrs = cms.InputTag("muonTCMETValueMapProducer","muCorrData"),
    triggerObjects = cms.InputTag("slimmedPatTrigger"),
    triggerResults = cms.InputTag("TriggerResults","","HLT"),
    useParticleFlow = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patElectrons = cms.EDProducer("PATElectronProducer",
    addEfficiencies = cms.bool(False),
    addElectronID = cms.bool(False),
    addGenMatch = cms.bool(True),
    addMVAVariables = cms.bool(True),
    addPFClusterIso = cms.bool(False),
    addPuppiIsolation = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    computeMiniIso = cms.bool(False),
    ecalPFClusterIsoMap = cms.InputTag(""),
    efficiencies = cms.PSet(

    ),
    electronIDSources = cms.PSet(

    ),
    electronSource = cms.InputTag("gedGsfElectrons"),
    embedBasicClusters = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedGsfElectronCore = cms.bool(True),
    embedGsfTrack = cms.bool(False),
    embedHighLevelSelection = cms.bool(True),
    embedPFCandidate = cms.bool(True),
    embedPflowBasicClusters = cms.bool(True),
    embedPflowPreshowerClusters = cms.bool(True),
    embedPflowSuperCluster = cms.bool(True),
    embedPreshowerClusters = cms.bool(True),
    embedRecHits = cms.bool(True),
    embedSeedCluster = cms.bool(True),
    embedSuperCluster = cms.bool(True),
    embedTrack = cms.bool(True),
    genParticleMatch = cms.InputTag("electronMatch"),
    hcalPFClusterIsoMap = cms.InputTag(""),
    isoDeposits = cms.PSet(
        pfChargedAll = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        pfChargedHadrons = cms.InputTag("elPFIsoDepositChargedPAT"),
        pfNeutralHadrons = cms.InputTag("elPFIsoDepositNeutralPAT"),
        pfPUChargedHadrons = cms.InputTag("elPFIsoDepositPUPAT"),
        pfPhotons = cms.InputTag("elPFIsoDepositGammaPAT")
    ),
    isolationValues = cms.PSet(
        pfChargedAll = cms.InputTag("elPFIsoValueChargedAll04PFIdPAT"),
        pfChargedHadrons = cms.InputTag("elPFIsoValueCharged04PFIdPAT"),
        pfNeutralHadrons = cms.InputTag("elPFIsoValueNeutral04PFIdPAT"),
        pfPUChargedHadrons = cms.InputTag("elPFIsoValuePU04PFIdPAT"),
        pfPhotons = cms.InputTag("elPFIsoValueGamma04PFIdPAT")
    ),
    isolationValuesNoPFId = cms.PSet(
        pfChargedAll = cms.InputTag("elPFIsoValueChargedAll04NoPFIdPAT"),
        pfChargedHadrons = cms.InputTag("elPFIsoValueCharged04NoPFIdPAT"),
        pfNeutralHadrons = cms.InputTag("elPFIsoValueNeutral04NoPFIdPAT"),
        pfPUChargedHadrons = cms.InputTag("elPFIsoValuePU04NoPFIdPAT"),
        pfPhotons = cms.InputTag("elPFIsoValueGamma04NoPFIdPAT")
    ),
    mightGet = cms.optional.untracked.vstring,
    miniIsoParamsB = cms.vdouble(
        0.05, 0.2, 10.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0
    ),
    miniIsoParamsE = cms.vdouble(
        0.05, 0.2, 10.0, 0.0, 0.015,
        0.015, 0.08, 0.0, 0.0
    ),
    pfCandidateMap = cms.InputTag("particleFlow","electrons"),
    pfCandsForMiniIso = cms.InputTag("packedPFCandidates"),
    pfElectronSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    resolutions = cms.PSet(

    ),
    useParticleFlow = cms.bool(False),
    usePfCandidateMultiMap = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patHemispheres = cms.EDProducer("PATHemisphereProducer",
    combinationMethod = cms.int32(3),
    maxElectronEta = cms.double(5),
    maxJetEta = cms.double(5),
    maxMuonEta = cms.double(5),
    maxPhotonEta = cms.double(5),
    maxTauEta = cms.double(-1),
    minElectronEt = cms.double(7),
    minJetEt = cms.double(30),
    minMuonEt = cms.double(7),
    minPhotonEt = cms.double(200000),
    minTauEt = cms.double(1000000),
    patElectrons = cms.InputTag("cleanLayer1Electrons"),
    patJets = cms.InputTag("cleanLayer1Jets"),
    patMets = cms.InputTag("layer1METs"),
    patMuons = cms.InputTag("cleanLayer1Muons"),
    patPhotons = cms.InputTag("cleanLayer1Photons"),
    patTaus = cms.InputTag("cleanLayer1Taus"),
    seedMethod = cms.int32(3)
)


process.patJetCharge = cms.EDProducer("JetChargeProducer",
    exp = cms.double(1.0),
    src = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    var = cms.string('Pt')
)


process.patJetCorrFactors = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L2Relative',
        'L3Absolute'
    ),
    mightGet = cms.optional.untracked.vstring,
    payload = cms.string('AK4PF'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akCs4PFJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.patJetFlavourAssociation = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("akCs4PFJets"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","physicsPartons"),
    rParam = cms.double(0.4)
)


process.patJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacy")
)


process.patJetGenJetMatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak4GenJets"),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("akCs4PFJets")
)


process.patJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("akCs4PFJets"),
    partons = cms.InputTag("allPartons")
)


process.patJetPartonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(
        1, 2, 3, 4, 5,
        21
    ),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akCs4PFJets")
)


process.patJetPartons = cms.EDProducer("HadronAndPartonSelector",
    fullChainPhysPartons = cms.bool(True),
    particles = cms.InputTag("hiSignalGenParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.patJetPartonsLegacy = cms.EDProducer("PartonSelector",
    src = cms.InputTag("genParticles"),
    withLeptons = cms.bool(False)
)


process.patJets = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(
        "simpleSecondaryVertexHighEffBJetTags", "simpleSecondaryVertexHighPurBJetTags", "combinedSecondaryVertexV2BJetTags", "jetBProbabilityBJetTags", "jetProbabilityBJetTags",
        "trackCountingHighEffBJetTags", "trackCountingHighPurBJetTags"
    ),
    efficiencies = cms.PSet(

    ),
    embedCaloTowers = cms.bool(False),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatch"),
    genPartonMatch = cms.InputTag("patJetPartonMatch"),
    getJetMCFlavour = cms.bool(True),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag("patJetCorrFactors"),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("akCs4PFJets"),
    mightGet = cms.optional.untracked.vstring,
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak5JetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patLowPtElectrons = cms.EDProducer("PATElectronProducer",
    addEfficiencies = cms.bool(False),
    addElectronID = cms.bool(True),
    addGenMatch = cms.bool(True),
    addMVAVariables = cms.bool(False),
    addPFClusterIso = cms.bool(False),
    addPuppiIsolation = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    computeMiniIso = cms.bool(False),
    ecalPFClusterIsoMap = cms.InputTag(""),
    efficiencies = cms.PSet(

    ),
    electronIDSources = cms.PSet(
        ID = cms.InputTag("lowPtGsfElectronID"),
        ptbiased = cms.InputTag("rekeyLowPtGsfElectronSeedValueMaps","ptbiased"),
        unbiased = cms.InputTag("rekeyLowPtGsfElectronSeedValueMaps","unbiased")
    ),
    electronSource = cms.InputTag("lowPtGsfElectrons"),
    embedBasicClusters = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedGsfElectronCore = cms.bool(True),
    embedGsfTrack = cms.bool(True),
    embedHighLevelSelection = cms.bool(False),
    embedPFCandidate = cms.bool(False),
    embedPflowBasicClusters = cms.bool(False),
    embedPflowPreshowerClusters = cms.bool(False),
    embedPflowSuperCluster = cms.bool(False),
    embedPreshowerClusters = cms.bool(False),
    embedRecHits = cms.bool(False),
    embedSeedCluster = cms.bool(True),
    embedSuperCluster = cms.bool(True),
    embedTrack = cms.bool(True),
    genParticleMatch = cms.InputTag("lowPtElectronMatch"),
    hcalPFClusterIsoMap = cms.InputTag(""),
    isoDeposits = cms.PSet(

    ),
    isolationValues = cms.PSet(

    ),
    isolationValuesNoPFId = cms.PSet(

    ),
    mightGet = cms.optional.untracked.vstring,
    miniIsoParamsB = cms.vdouble(
        0.05, 0.2, 10.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0
    ),
    miniIsoParamsE = cms.vdouble(
        0.05, 0.2, 10.0, 0.0, 0.015,
        0.015, 0.08, 0.0, 0.0
    ),
    pfCandidateMap = cms.InputTag("particleFlow","electrons"),
    pfCandsForMiniIso = cms.InputTag("packedPFCandidates"),
    pfElectronSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    resolutions = cms.PSet(

    ),
    useParticleFlow = cms.bool(False),
    usePfCandidateMultiMap = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patMETs = cms.EDProducer("PATMETProducer",
    addEfficiencies = cms.bool(False),
    addGenMET = cms.bool(True),
    addMuonCorrections = cms.bool(False),
    addResolutions = cms.bool(False),
    computeMETSignificance = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genMETSource = cms.InputTag("genMetTrue"),
    metSource = cms.InputTag("pfMetT1"),
    muonSource = cms.InputTag("muons"),
    parameters = cms.PSet(
        dRMatch = cms.double(0.4),
        jetThreshold = cms.double(15),
        jeta = cms.vdouble(0.8, 1.3, 1.9, 2.5),
        jpar = cms.vdouble(1.39, 1.26, 1.21, 1.23, 1.28),
        pjpar = cms.vdouble(-0.2586, 0.6173)
    ),
    resolutions = cms.PSet(

    ),
    srcJetResPhi = cms.string('AK4PFchs_phi'),
    srcJetResPt = cms.string('AK4PFchs_pt'),
    srcJetSF = cms.string('AK4PFchs'),
    srcJets = cms.InputTag("cleanedPatJets"),
    srcLeptons = cms.VInputTag("selectedPatElectrons", "selectedPatMuons", "selectedPatPhotons"),
    srcPFCands = cms.InputTag("particleFlow"),
    srcRho = cms.InputTag("fixedGridRhoAll"),
    srcWeights = cms.InputTag(""),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patMuons = cms.EDProducer("PATMuonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(True),
    addInverseBeta = cms.bool(True),
    addPuppiIsolation = cms.bool(False),
    addResolutions = cms.bool(False),
    addTriggerMatching = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    caloMETMuonCorrs = cms.InputTag("muonMETValueMapProducer","muCorrData"),
    computeMiniIso = cms.bool(False),
    computeMuonIDMVA = cms.bool(False),
    computeMuonMVA = cms.bool(False),
    computePuppiCombinedIso = cms.bool(False),
    computeSoftMuonMVA = cms.bool(False),
    effectiveAreaVec = cms.vdouble(0.0566, 0.0562, 0.0363, 0.0119, 0.0064),
    efficiencies = cms.PSet(

    ),
    embedCaloMETMuonCorrs = cms.bool(True),
    embedCombinedMuon = cms.bool(True),
    embedDytMuon = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedHighLevelSelection = cms.bool(True),
    embedMuonBestTrack = cms.bool(True),
    embedPFCandidate = cms.bool(True),
    embedPfEcalEnergy = cms.bool(True),
    embedPickyMuon = cms.bool(True),
    embedStandAloneMuon = cms.bool(True),
    embedTcMETMuonCorrs = cms.bool(False),
    embedTpfmsMuon = cms.bool(True),
    embedTrack = cms.bool(False),
    embedTunePMuonBestTrack = cms.bool(True),
    forceBestTrackEmbedding = cms.bool(False),
    genParticleMatch = cms.InputTag("muonMatch"),
    hltCollectionFilters = cms.vstring('*'),
    isoDeposits = cms.PSet(
        pfChargedAll = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        pfChargedHadrons = cms.InputTag("muPFIsoDepositChargedPAT"),
        pfNeutralHadrons = cms.InputTag("muPFIsoDepositNeutralPAT"),
        pfPUChargedHadrons = cms.InputTag("muPFIsoDepositPUPAT"),
        pfPhotons = cms.InputTag("muPFIsoDepositGammaPAT")
    ),
    isolationValues = cms.PSet(
        pfChargedAll = cms.InputTag("muPFIsoValueChargedAll04PAT"),
        pfChargedHadrons = cms.InputTag("muPFIsoValueCharged04PAT"),
        pfNeutralHadrons = cms.InputTag("muPFIsoValueNeutral04PAT"),
        pfPUChargedHadrons = cms.InputTag("muPFIsoValuePU04PAT"),
        pfPhotons = cms.InputTag("muPFIsoValueGamma04PAT")
    ),
    lowPtmvaTrainingFile = cms.FileInPath('RecoMuon/MuonIdentification/data/mu_lowpt_BDTG.weights.xml'),
    miniIsoParams = cms.vdouble(
        0.05, 0.2, 10.0, 0.5, 0.0001,
        0.01, 0.01, 0.01, 0.0
    ),
    muonSimInfo = cms.InputTag("muonSimClassifier"),
    muonSource = cms.InputTag("muons"),
    mvaDrMax = cms.double(0.4),
    mvaIDTrainingFile = cms.FileInPath('RecoMuon/MuonIdentification/data/mvaID.onnx'),
    mvaJetTag = cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
    mvaL1Corrector = cms.InputTag("ak4PFCHSL1FastjetCorrector"),
    mvaL1L2L3ResCorrector = cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
    mvaTrainingFile = cms.FileInPath('RecoMuon/MuonIdentification/data/mu_2017_BDTG.weights.xml'),
    mvaUseJec = cms.bool(True),
    pfCandsForMiniIso = cms.InputTag("packedPFCandidates"),
    pfMuonSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    recomputeBasicSelectors = cms.bool(True),
    resolutions = cms.PSet(

    ),
    rho = cms.InputTag("fixedGridRhoFastjetCentralNeutral"),
    softMvaTrainingFile = cms.FileInPath('RecoMuon/MuonIdentification/data/TMVA-muonid-bmm4-B-25.weights.xml'),
    sourceMuonTimeExtra = cms.InputTag("muons","combined"),
    tcMETMuonCorrs = cms.InputTag("muonTCMETValueMapProducer","muCorrData"),
    triggerObjects = cms.InputTag("slimmedPatTrigger"),
    triggerResults = cms.InputTag("TriggerResults","","HLT"),
    useParticleFlow = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patMuonsWithTrigger = cms.EDProducer("PATTriggerMatchMuonEmbedder",
    matches = cms.VInputTag(
        cms.InputTag("muonMatchHLTL2"), cms.InputTag("muonMatchHLTL3"), cms.InputTag("muonMatchHLTL3T"), cms.InputTag("muonMatchHLTL3fromL2"), cms.InputTag("muonMatchHLTTkMu"),
        cms.InputTag("muonMatchHLTCtfTrack"), cms.InputTag("muonMatchHLTCtfTrack2"), cms.InputTag("muonMatchHLTTrackMu"), cms.InputTag("muonMatchHLTTrackIt"), cms.InputTag("muonMatchHLTL1"),
        cms.InputTag("muonMatchHLTL1","propagatedReco")
    ),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.patMuonsWithoutTrigger = cms.EDProducer("PATMuonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(False),
    addInverseBeta = cms.bool(True),
    addPuppiIsolation = cms.bool(False),
    addResolutions = cms.bool(False),
    addTriggerMatching = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    caloMETMuonCorrs = cms.InputTag("muonMETValueMapProducer","muCorrData"),
    computeMiniIso = cms.bool(False),
    computeMuonIDMVA = cms.bool(False),
    computeMuonMVA = cms.bool(False),
    computePuppiCombinedIso = cms.bool(False),
    computeSoftMuonMVA = cms.bool(False),
    effectiveAreaVec = cms.vdouble(0.0566, 0.0562, 0.0363, 0.0119, 0.0064),
    efficiencies = cms.PSet(

    ),
    embedCaloMETMuonCorrs = cms.bool(False),
    embedCombinedMuon = cms.bool(True),
    embedDytMuon = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedHighLevelSelection = cms.bool(True),
    embedMuonBestTrack = cms.bool(True),
    embedPFCandidate = cms.bool(False),
    embedPfEcalEnergy = cms.bool(False),
    embedPickyMuon = cms.bool(False),
    embedStandAloneMuon = cms.bool(True),
    embedTcMETMuonCorrs = cms.bool(False),
    embedTpfmsMuon = cms.bool(False),
    embedTrack = cms.bool(True),
    embedTunePMuonBestTrack = cms.bool(True),
    forceBestTrackEmbedding = cms.bool(False),
    genParticleMatch = cms.InputTag("muonMatch"),
    hltCollectionFilters = cms.vstring('*'),
    isoDeposits = cms.PSet(

    ),
    isolationValues = cms.PSet(
        pfChargedAll = cms.InputTag("muPFIsoValueChargedAll04PAT"),
        pfChargedHadrons = cms.InputTag("muPFIsoValueCharged04PAT"),
        pfNeutralHadrons = cms.InputTag("muPFIsoValueNeutral04PAT"),
        pfPUChargedHadrons = cms.InputTag("muPFIsoValuePU04PAT"),
        pfPhotons = cms.InputTag("muPFIsoValueGamma04PAT")
    ),
    lowPtmvaTrainingFile = cms.FileInPath('RecoMuon/MuonIdentification/data/mu_lowpt_BDTG.weights.xml'),
    miniIsoParams = cms.vdouble(
        0.05, 0.2, 10.0, 0.5, 0.0001,
        0.01, 0.01, 0.01, 0.0
    ),
    muonSimInfo = cms.InputTag("muonSimClassifier"),
    muonSource = cms.InputTag("muons"),
    mvaDrMax = cms.double(0.4),
    mvaIDTrainingFile = cms.FileInPath('RecoMuon/MuonIdentification/data/mvaID.onnx'),
    mvaJetTag = cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
    mvaL1Corrector = cms.InputTag("ak4PFCHSL1FastjetCorrector"),
    mvaL1L2L3ResCorrector = cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
    mvaTrainingFile = cms.FileInPath('RecoMuon/MuonIdentification/data/mu_2017_BDTG.weights.xml'),
    mvaUseJec = cms.bool(True),
    pfCandsForMiniIso = cms.InputTag("packedPFCandidates"),
    pfMuonSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    recomputeBasicSelectors = cms.bool(True),
    resolutions = cms.PSet(

    ),
    rho = cms.InputTag("fixedGridRhoFastjetCentralNeutral"),
    softMvaTrainingFile = cms.FileInPath('RecoMuon/MuonIdentification/data/TMVA-muonid-bmm4-B-25.weights.xml'),
    sourceMuonTimeExtra = cms.InputTag("muons","combined"),
    tcMETMuonCorrs = cms.InputTag("muonTCMETValueMapProducer","muCorrData"),
    triggerObjects = cms.InputTag("slimmedPatTrigger"),
    triggerResults = cms.InputTag("TriggerResults","","HLT"),
    useParticleFlow = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag(cms.InputTag("muonL1Info"))
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag()
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag(cms.InputTag("muonL1Info","deltaR"), cms.InputTag("muonL1Info","deltaPhi"))
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag(cms.InputTag("muonL1Info","quality"), cms.InputTag("muonL1Info","bx"))
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patOOTPhotons = cms.EDProducer("PATPhotonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(True),
    addPFClusterIso = cms.bool(False),
    addPhotonID = cms.bool(False),
    addPuppiIsolation = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    conversionSource = cms.InputTag("allConversions"),
    ecalPFClusterIsoMap = cms.InputTag(""),
    efficiencies = cms.PSet(

    ),
    electronSource = cms.InputTag("gedGsfElectrons"),
    embedBasicClusters = cms.bool(False),
    embedGenMatch = cms.bool(False),
    embedPreshowerClusters = cms.bool(False),
    embedRecHits = cms.bool(False),
    embedSeedCluster = cms.bool(False),
    embedSuperCluster = cms.bool(False),
    genParticleMatch = cms.InputTag("ootPhotonMatch"),
    hcalPFClusterIsoMap = cms.InputTag(""),
    isoDeposits = cms.PSet(

    ),
    isolationValues = cms.PSet(

    ),
    mightGet = cms.optional.untracked.vstring,
    photonIDSources = cms.PSet(

    ),
    photonSource = cms.InputTag("ootPhotons"),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    resolutions = cms.PSet(

    ),
    saveRegressionData = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patPhotons = cms.EDProducer("PATPhotonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(True),
    addPFClusterIso = cms.bool(False),
    addPhotonID = cms.bool(False),
    addPuppiIsolation = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    conversionSource = cms.InputTag("allConversions"),
    ecalPFClusterIsoMap = cms.InputTag(""),
    efficiencies = cms.PSet(

    ),
    electronSource = cms.InputTag("gedGsfElectrons"),
    embedBasicClusters = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedPreshowerClusters = cms.bool(True),
    embedRecHits = cms.bool(True),
    embedSeedCluster = cms.bool(True),
    embedSuperCluster = cms.bool(True),
    genParticleMatch = cms.InputTag("photonMatch"),
    hcalPFClusterIsoMap = cms.InputTag(""),
    isoDeposits = cms.PSet(
        pfChargedAll = cms.InputTag("phPFIsoDepositChargedAllPAT"),
        pfChargedHadrons = cms.InputTag("phPFIsoDepositChargedPAT"),
        pfNeutralHadrons = cms.InputTag("phPFIsoDepositNeutralPAT"),
        pfPUChargedHadrons = cms.InputTag("phPFIsoDepositPUPAT"),
        pfPhotons = cms.InputTag("phPFIsoDepositGammaPAT")
    ),
    isolationValues = cms.PSet(
        pfChargedAll = cms.InputTag("phPFIsoValueChargedAll04PFIdPAT"),
        pfChargedHadrons = cms.InputTag("phPFIsoValueCharged04PFIdPAT"),
        pfNeutralHadrons = cms.InputTag("phPFIsoValueNeutral04PFIdPAT"),
        pfPUChargedHadrons = cms.InputTag("phPFIsoValuePU04PFIdPAT"),
        pfPhotons = cms.InputTag("phPFIsoValueGamma04PFIdPAT")
    ),
    mightGet = cms.optional.untracked.vstring,
    photonIDSources = cms.PSet(

    ),
    photonSource = cms.InputTag("gedPhotons"),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    resolutions = cms.PSet(

    ),
    saveRegressionData = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patTaus = cms.EDProducer("PATTauProducer",
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenMatch = cms.bool(True),
    addResolutions = cms.bool(False),
    addTauID = cms.bool(True),
    addTauJetCorrFactors = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedIsolationPFCands = cms.bool(False),
    embedIsolationPFChargedHadrCands = cms.bool(False),
    embedIsolationPFGammaCands = cms.bool(False),
    embedIsolationPFNeutralHadrCands = cms.bool(False),
    embedIsolationTracks = cms.bool(False),
    embedLeadPFCand = cms.bool(False),
    embedLeadPFChargedHadrCand = cms.bool(False),
    embedLeadPFNeutralCand = cms.bool(False),
    embedLeadTrack = cms.bool(False),
    embedSignalPFCands = cms.bool(False),
    embedSignalPFChargedHadrCands = cms.bool(False),
    embedSignalPFGammaCands = cms.bool(False),
    embedSignalPFNeutralHadrCands = cms.bool(False),
    embedSignalTracks = cms.bool(False),
    genJetMatch = cms.InputTag("tauGenJetMatch"),
    genParticleMatch = cms.InputTag("tauMatch"),
    isoDeposits = cms.PSet(

    ),
    resolutions = cms.PSet(

    ),
    skipMissingTauID = cms.bool(False),
    tauIDSources = cms.PSet(
        againstElectronDeadECAL = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDeadECALElectronRejection"),
            provenanceConfigLabel = cms.string('')
        ),
        againstMuonLoose3 = cms.PSet(
            idLabel = cms.string('ByLooseMuonRejection3'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByMuonRejection3"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        againstMuonTight3 = cms.PSet(
            idLabel = cms.string('ByTightMuonRejection3'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByMuonRejection3"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byCombinedIsolationDeltaBetaCorrRaw3Hits = cms.PSet(
            idLabel = cms.string('ByRawCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        byLooseCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByLooseCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byMediumCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByMediumCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byPhotonPtSumOutsideSignalCone = cms.PSet(
            idLabel = cms.string('ByPhotonPtSumOutsideSignalCone'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byTightCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByTightCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        chargedIsoPtSum = cms.PSet(
            idLabel = cms.string('ChargedIsoPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        chargedIsoPtSumdR03 = cms.PSet(
            idLabel = cms.string('ChargedIsoPtSumdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        decayModeFinding = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding"),
            provenanceConfigLabel = cms.string('')
        ),
        decayModeFindingNewDMs = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            provenanceConfigLabel = cms.string('')
        ),
        footprintCorrection = cms.PSet(
            idLabel = cms.string('TauFootprintCorrection'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        footprintCorrectiondR03 = cms.PSet(
            idLabel = cms.string('TauFootprintCorrectiondR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSum = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumWeight = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumWeight'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumWeightdR03 = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumWeightdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumdR03 = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        photonPtSumOutsideSignalCone = cms.PSet(
            idLabel = cms.string('PhotonPtSumOutsideSignalCone'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        photonPtSumOutsideSignalConedR03 = cms.PSet(
            idLabel = cms.string('PhotonPtSumOutsideSignalConedR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        puCorrPtSum = cms.PSet(
            idLabel = cms.string('PUcorrPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        )
    ),
    tauJetCorrFactorsSource = cms.VInputTag(cms.InputTag("patTauJetCorrFactors")),
    tauSource = cms.InputTag("hpsPFTauProducer"),
    tauTransverseImpactParameterSource = cms.InputTag("hpsPFTauTransverseImpactParameters"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patTrigger = cms.EDProducer("TriggerObjectFilterByCollection",
    collections = cms.vstring(
        'hltL1extraParticles',
        'hltGmtStage2Digis',
        'hltL2MuonCandidates',
        'hltIterL3MuonCandidates',
        'hltIterL3FromL2MuonCandidates',
        'hltHighPtTkMuonCands',
        'hltGlbTrkMuonCands',
        'hltMuTrackJpsiCtfTrackCands',
        'hltMuTrackJpsiEffCtfTrackCands',
        'hltMuTkMuJpsiTrackerMuonCands',
        'hltTracksIter',
        'hltGtStage2Digis:Muon',
        'hltIterL3MuonCandidatesPPOnAA',
        'hltL2MuonCandidatesPPOnAA'
    ),
    src = cms.InputTag("patTriggerFull")
)


process.patTriggerFull = cms.EDProducer("PATTriggerProducer",
    ReadPrescalesFromFile = cms.bool(False),
    l1GtReadoutRecordInputTag = cms.InputTag("gtDigis","","RECO"),
    l1GtRecordInputTag = cms.InputTag("gtDigis"),
    l1GtTriggerMenuLiteInputTag = cms.InputTag("gtDigis"),
    l1tAlgBlkInputTag = cms.InputTag("gtStage2Digis","","RECO"),
    l1tExtBlkInputTag = cms.InputTag("gtStage2Digis","","RECO"),
    onlyStandAlone = cms.bool(True),
    packTriggerLabels = cms.bool(False),
    processName = cms.string('HLT'),
    stageL1Trigger = cms.uint32(2)
)


process.pfCandComposites = cms.EDProducer("PFCandCompositeProducer",
    compositeTag = cms.InputTag("Dfinder"),
    isHI = cms.bool(False),
    jpsiTrigFilter = cms.string('hltHIDoubleMu0L1Filtered'),
    pfCandTag = cms.InputTag("packedPFCandidates"),
    removeDKPi = cms.bool(True),
    removeJMM = cms.bool(False)
)


process.pfCandMETcorr = cms.EDProducer("PFCandMETcorrInputProducer",
    src = cms.InputTag("pfCandsNotInJetsForMetCorr"),
    srcWeights = cms.InputTag("")
)


process.pfCandsNotInJetsForMetCorr = cms.EDProducer("PFCandidateFromFwdPtrProducer",
    src = cms.InputTag("pfCandsNotInJetsPtrForMetCorr")
)


process.pfCandsNotInJetsPtrForMetCorr = cms.EDProducer("TPPFJetsOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    matchByPtrDirect = cms.bool(False),
    mightGet = cms.optional.untracked.vstring,
    name = cms.untracked.string('noJet'),
    topCollection = cms.InputTag("pfJetsPtrForMetCorr")
)


process.pfDeepCMVADiscriminatorsJetTags = cms.EDProducer("BTagProbabilityToDiscriminator",
    discriminators = cms.VPSet(
        cms.PSet(
            denominator = cms.VInputTag(),
            name = cms.string('BvsAll'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepCMVAJetTags","probb"), cms.InputTag("pfDeepCMVAJetTags","probbb"))
        ),
        cms.PSet(
            denominator = cms.VInputTag(cms.InputTag("pfDeepCMVAJetTags","probc"), cms.InputTag("pfDeepCMVAJetTags","probb"), cms.InputTag("pfDeepCMVAJetTags","probbb")),
            name = cms.string('CvsB'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepCMVAJetTags","probc"))
        ),
        cms.PSet(
            denominator = cms.VInputTag(cms.InputTag("pfDeepCMVAJetTags","probc"), cms.InputTag("pfDeepCMVAJetTags","probudsg")),
            name = cms.string('CvsL'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepCMVAJetTags","probc"))
        )
    )
)


process.pfDeepCMVAJetTags = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/Model_DeepCMVA.json'),
    checkSVForDefaults = cms.bool(False),
    meanPadding = cms.bool(False),
    src = cms.InputTag("pfDeepCMVATagInfos"),
    toAdd = cms.PSet(

    )
)


process.pfDeepCMVANegativeTagInfos = cms.EDProducer("DeepCMVATagInfoProducer",
    cMVAPtThreshold = cms.double(200),
    deepNNTagInfos = cms.InputTag("pfDeepCSVNegativeTagInfos"),
    elInfoSrc = cms.InputTag("softPFElectronsTagInfos"),
    ipInfoSrc = cms.InputTag("pfImpactParameterTagInfos"),
    jpComputerSrc = cms.string('candidateJetProbabilityComputer'),
    jpbComputerSrc = cms.string('candidateJetBProbabilityComputer'),
    muInfoSrc = cms.InputTag("softPFMuonsTagInfos"),
    softelComputerSrc = cms.string('softPFElectronComputer'),
    softmuComputerSrc = cms.string('softPFMuonComputer')
)


process.pfDeepCMVAPositiveTagInfos = cms.EDProducer("DeepCMVATagInfoProducer",
    cMVAPtThreshold = cms.double(200),
    deepNNTagInfos = cms.InputTag("pfDeepCSVPositiveTagInfos"),
    elInfoSrc = cms.InputTag("softPFElectronsTagInfos"),
    ipInfoSrc = cms.InputTag("pfImpactParameterTagInfos"),
    jpComputerSrc = cms.string('candidateJetProbabilityComputer'),
    jpbComputerSrc = cms.string('candidateJetBProbabilityComputer'),
    muInfoSrc = cms.InputTag("softPFMuonsTagInfos"),
    softelComputerSrc = cms.string('softPFElectronComputer'),
    softmuComputerSrc = cms.string('softPFMuonComputer')
)


process.pfDeepCMVATagInfos = cms.EDProducer("DeepCMVATagInfoProducer",
    cMVAPtThreshold = cms.double(200),
    deepNNTagInfos = cms.InputTag("pfDeepCSVTagInfos"),
    elInfoSrc = cms.InputTag("softPFElectronsTagInfos"),
    ipInfoSrc = cms.InputTag("pfImpactParameterTagInfos"),
    jpComputerSrc = cms.string('candidateJetProbabilityComputer'),
    jpbComputerSrc = cms.string('candidateJetBProbabilityComputer'),
    muInfoSrc = cms.InputTag("softPFMuonsTagInfos"),
    softelComputerSrc = cms.string('softPFElectronComputer'),
    softmuComputerSrc = cms.string('softPFMuonComputer')
)


process.pfDeepCSVDiscriminatorsJetTags = cms.EDProducer("BTagProbabilityToDiscriminator",
    discriminators = cms.VPSet(
        cms.PSet(
            denominator = cms.VInputTag(),
            name = cms.string('BvsAll'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTags","probb"), cms.InputTag("pfDeepCSVJetTags","probbb"))
        ),
        cms.PSet(
            denominator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTags","probc"), cms.InputTag("pfDeepCSVJetTags","probb"), cms.InputTag("pfDeepCSVJetTags","probbb")),
            name = cms.string('CvsB'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTags","probc"))
        ),
        cms.PSet(
            denominator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTags","probudsg"), cms.InputTag("pfDeepCSVJetTags","probc")),
            name = cms.string('CvsL'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepCSVJetTags","probc"))
        )
    )
)


process.pfDeepCSVJetTags = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepCSV_PhaseI.json'),
    checkSVForDefaults = cms.bool(True),
    meanPadding = cms.bool(True),
    src = cms.InputTag("pfDeepCSVTagInfos"),
    toAdd = cms.PSet(

    )
)


process.pfDeepCSVNegativeTagInfos = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(True),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(-2.0),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(10.0),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(10.0),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(True)
    ),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderNegativeTagInfos")
)


process.pfDeepCSVPositiveTagInfos = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(0),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(0),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos")
)


process.pfDeepCSVTagInfos = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("pfSecondaryVertexTagInfos")
)


process.pfImpactParameterTagInfos = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("slimmedJets"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVerticesRecovery"),
    useTrackQuality = cms.bool(False)
)


process.pfInclusiveSecondaryVertexFinderTagInfos = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveCandidateSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfJetsPtrForMetCorr = cms.EDProducer("PFJetFwdPtrProducer",
    src = cms.InputTag("ak4PFJets")
)


process.pfMetT1 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1","type1"))
)


process.pfMetT1T2 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetType2"))
)


process.pfNegativeDeepCMVAJetTags = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/Model_DeepCMVA.json'),
    checkSVForDefaults = cms.bool(False),
    meanPadding = cms.bool(False),
    src = cms.InputTag("pfDeepCMVANegativeTagInfos"),
    toAdd = cms.PSet(

    )
)


process.pfNegativeDeepCSVJetTags = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepCSV_PhaseI.json'),
    checkSVForDefaults = cms.bool(True),
    meanPadding = cms.bool(True),
    src = cms.InputTag("pfDeepCSVNegativeTagInfos"),
    toAdd = cms.PSet(

    )
)


process.pfNoPileUpIsoPFBRECO = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    matchByPtrDirect = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpIsoPFBRECO")
)


process.pfNoPileUpJME = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    matchByPtrDirect = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpJME")
)


process.pfNoPileUpPFBRECO = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    matchByPtrDirect = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpPFBRECO")
)


process.pfPileUpIsoPFBRECO = cms.EDProducer("PFPileUp",
    DzCutForChargedFromPUVtxs = cms.double(0.2),
    NumOfPUVtxsForCharged = cms.uint32(0),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("offlinePrimaryVertices"),
    checkClosestZVertex = cms.bool(True),
    enable = cms.bool(False),
    mightGet = cms.optional.untracked.vstring,
    useVertexAssociation = cms.bool(False),
    verbose = cms.untracked.bool(False),
    vertexAssociation = cms.InputTag(""),
    vertexAssociationQuality = cms.int32(0)
)


process.pfPileUpJME = cms.EDProducer("PFPileUp",
    DzCutForChargedFromPUVtxs = cms.double(0.2),
    NumOfPUVtxsForCharged = cms.uint32(2),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("goodOfflinePrimaryVertices"),
    checkClosestZVertex = cms.bool(False),
    enable = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    useVertexAssociation = cms.bool(False),
    verbose = cms.untracked.bool(False),
    vertexAssociation = cms.InputTag(""),
    vertexAssociationQuality = cms.int32(0)
)


process.pfPileUpPFBRECO = cms.EDProducer("PFPileUp",
    DzCutForChargedFromPUVtxs = cms.double(0.2),
    NumOfPUVtxsForCharged = cms.uint32(0),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("offlinePrimaryVertices"),
    checkClosestZVertex = cms.bool(True),
    enable = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    useVertexAssociation = cms.bool(False),
    verbose = cms.untracked.bool(False),
    vertexAssociation = cms.InputTag(""),
    vertexAssociationQuality = cms.int32(0)
)


process.pfPositiveDeepCMVAJetTags = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/Model_DeepCMVA.json'),
    checkSVForDefaults = cms.bool(False),
    meanPadding = cms.bool(False),
    src = cms.InputTag("pfDeepCMVAPositiveTagInfos"),
    toAdd = cms.PSet(

    )
)


process.pfPositiveDeepCSVJetTags = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepCSV_PhaseI.json'),
    checkSVForDefaults = cms.bool(True),
    meanPadding = cms.bool(True),
    src = cms.InputTag("pfDeepCSVPositiveTagInfos"),
    toAdd = cms.PSet(

    )
)


process.pfSecondaryVertexTagInfos = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.phPFIsoDepositChargedAllPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositChargedPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositGammaPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFCandWithSuperClusterExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        MissHitSCMatch_Veto = cms.bool(False),
        SCMatch_Veto = cms.bool(True),
        inputCandView = cms.InputTag("pfAllPhotonsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositNeutralPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositPUPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoValueCharged03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueCharged04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueChargedAll03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueChargedAll04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueGamma03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.05)'),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueGamma04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.05)'),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueNeutral03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueNeutral04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValuePU03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositPUPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValuePU04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositPUPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.photonCore = cms.EDProducer("PhotonCoreProducer",
    conversionProducer = cms.InputTag(""),
    endcapOnly = cms.bool(False),
    minSCEt = cms.double(10.0),
    photonCoreCollection = cms.string(''),
    pixelSeedProducer = cms.InputTag("electronMergedSeeds"),
    risolveConversionAmbiguity = cms.bool(True),
    scHybridBarrelProducer = cms.InputTag("correctedHybridSuperClusters"),
    scIslandEndcapProducer = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower")
)


process.photonCoreHGC = cms.EDProducer("PhotonCoreProducer",
    conversionProducer = cms.InputTag(""),
    endcapOnly = cms.bool(True),
    minSCEt = cms.double(10.0),
    photonCoreCollection = cms.string(''),
    pixelSeedProducer = cms.InputTag("electronMergedSeeds"),
    risolveConversionAmbiguity = cms.bool(True),
    scHybridBarrelProducer = cms.InputTag(""),
    scIslandEndcapProducer = cms.InputTag("particleFlowSuperClusterHGCal")
)


process.photonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(1.0),
    maxDeltaR = cms.double(0.2),
    mcPdgId = cms.vint32(22),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("gedPhotons")
)


process.primaryVertexAssociation = cms.EDProducer("PFCandidatePrimaryVertexSorter",
    assignment = cms.PSet(
        DzCutForChargedFromPUVtxs = cms.double(0.2),
        EtaMinUseDz = cms.double(-1),
        NumOfPUVtxsForCharged = cms.uint32(0),
        OnlyUseFirstDz = cms.bool(False),
        PtMaxCharged = cms.double(-1),
        maxDistanceToJetAxis = cms.double(0.07),
        maxDtSigForPrimaryAssignment = cms.double(3),
        maxDxyForJetAxisAssigment = cms.double(0.1),
        maxDxyForNotReconstructedPrimary = cms.double(0.01),
        maxDxySigForNotReconstructedPrimary = cms.double(2),
        maxDzErrorForPrimaryAssignment = cms.double(0.05),
        maxDzForJetAxisAssigment = cms.double(0.1),
        maxDzForPrimaryAssignment = cms.double(0.1),
        maxDzSigForPrimaryAssignment = cms.double(5),
        maxJetDeltaR = cms.double(0.5),
        minJetPt = cms.double(25),
        preferHighRanked = cms.bool(False),
        useTiming = cms.bool(False),
        useVertexFit = cms.bool(True)
    ),
    jets = cms.InputTag("ak4PFJets"),
    mightGet = cms.optional.untracked.vstring,
    particles = cms.InputTag("cleanedParticleFlow"),
    produceAssociationToOriginalVertices = cms.bool(True),
    produceNoPileUpCollection = cms.bool(False),
    producePileUpCollection = cms.bool(False),
    produceSortedVertices = cms.bool(False),
    qualityForPrimary = cms.int32(2),
    sorting = cms.PSet(

    ),
    usePVMET = cms.bool(True),
    vertices = cms.InputTag("offlinePrimaryVertices")
)


process.primaryVertexAssociationJME = cms.EDProducer("PFCandidatePrimaryVertexSorter",
    assignment = cms.PSet(
        DzCutForChargedFromPUVtxs = cms.double(0.2),
        EtaMinUseDz = cms.double(2.4),
        NumOfPUVtxsForCharged = cms.uint32(2),
        OnlyUseFirstDz = cms.bool(True),
        PtMaxCharged = cms.double(20.0),
        maxDistanceToJetAxis = cms.double(0.07),
        maxDtSigForPrimaryAssignment = cms.double(3),
        maxDxyForJetAxisAssigment = cms.double(0.1),
        maxDxyForNotReconstructedPrimary = cms.double(0.01),
        maxDxySigForNotReconstructedPrimary = cms.double(2),
        maxDzErrorForPrimaryAssignment = cms.double(10000000000.0),
        maxDzForJetAxisAssigment = cms.double(0.1),
        maxDzForPrimaryAssignment = cms.double(0.3),
        maxDzSigForPrimaryAssignment = cms.double(10000000000.0),
        maxJetDeltaR = cms.double(0.5),
        minJetPt = cms.double(25),
        preferHighRanked = cms.bool(False),
        useTiming = cms.bool(False),
        useVertexFit = cms.bool(True)
    ),
    jets = cms.InputTag("ak4PFJets"),
    mightGet = cms.optional.untracked.vstring,
    particles = cms.InputTag("cleanedParticleFlow"),
    produceAssociationToOriginalVertices = cms.bool(True),
    produceNoPileUpCollection = cms.bool(False),
    producePileUpCollection = cms.bool(False),
    produceSortedVertices = cms.bool(False),
    qualityForPrimary = cms.int32(2),
    sorting = cms.PSet(

    ),
    usePVMET = cms.bool(True),
    vertices = cms.InputTag("goodOfflinePrimaryVertices")
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.rekeyLowPtGsfElectronSeedValueMaps = cms.EDProducer("LowPtGsfElectronSeedValueMapsProducer",
    ModelNames = cms.vstring(
        'unbiased',
        'ptbiased'
    ),
    floatValueMaps = cms.VInputTag("lowPtGsfElectronSeedValueMaps:unbiased", "lowPtGsfElectronSeedValueMaps:ptbiased"),
    gsfElectrons = cms.InputTag("lowPtGsfElectrons"),
    gsfTracks = cms.InputTag("lowPtGsfEleGsfTracks"),
    mightGet = cms.optional.untracked.vstring,
    preIdsValueMap = cms.InputTag("lowPtGsfElectronSeeds"),
    rekey = cms.bool(True)
)


process.secondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.siPixelRecHits = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("siPixelClusters")
)


process.siPixelRecHitsPreSplittingCPU = cms.EDProducer("SiPixelRecHitSoAFromLegacy",
    CPE = cms.string('PixelCPEFast'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    convertToLegacy = cms.bool(True),
    isPhase2 = cms.bool(False),
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("siPixelClustersPreSplitting")
)


process.siPixelRecHitsPreSplittingCUDA = cms.EDProducer("SiPixelRecHitCUDA",
    CPE = cms.string('PixelCPEFast'),
    beamSpot = cms.InputTag("offlineBeamSpotToCUDA"),
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("siPixelClustersPreSplittingCUDA")
)


process.simpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfos"))
)


process.simpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfos"))
)


process.tauGenJetMatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("tauGenJetsSelectorAllHadrons"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.1),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer")
)


process.tauGenJets = cms.EDProducer("TauGenJetProducer",
    GenParticles = cms.InputTag("genParticles"),
    includeNeutrinos = cms.bool(False),
    verbose = cms.untracked.bool(False)
)


process.tauIsoDepositPFCandidates = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("particleFlow"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFChargedHadrons = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        candidateSource = cms.InputTag("pfAllChargedHadronsPFBRECO"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFGammas = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("pfAllPhotonsPFBRECO"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFNeutralHadrons = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("pfAllNeutralHadronsPFBRECO"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(999.9),
    maxDeltaR = cms.double(999.9),
    mcPdgId = cms.vint32(15),
    mcStatus = cms.vint32(2),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer")
)


process.trackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.trackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.unpackedTracksAndVertices = cms.EDProducer("TrackAndVertexUnpacker",
    lostTrackNormChi2Map = cms.InputTag("lostTrackChi2"),
    lostTracks = cms.InputTag("lostTracks"),
    mightGet = cms.optional.untracked.vstring,
    packedPFCandidateNormChi2Map = cms.InputTag("packedPFCandidateTrackChi2"),
    packedPFCandidates = cms.InputTag("packedPFCandidates"),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    recoverTracks = cms.bool(False),
    secondaryVertices = cms.InputTag("slimmedSecondaryVertices")
)


process.zdcdigi = cms.EDProducer("QWZDC2018Producer2",
    Debug = cms.untracked.bool(False),
    HardCode = cms.untracked.bool(True),
    Pedestal = cms.VPSet(
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM0'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM1'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM2'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM3'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM4'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM5'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM6'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM7'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM8'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM9'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM10'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM11'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM12'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM13'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM14'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM15'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD0'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD1'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD2'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD3'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD4'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD5'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD6'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD7'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD8'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD9'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD10'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD11'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD12'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD13'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD14'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD15'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM0'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM1'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM2'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM3'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM4'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM5'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM6'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM7'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM8'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM9'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM10'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM11'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM12'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM13'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM14'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM15'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD0'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD1'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD2'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD3'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD4'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD5'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD6'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD7'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD8'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD9'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD10'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD11'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD12'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD13'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD14'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD15'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD0'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD1'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD2'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD3'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD4'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD5'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD6'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD7'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD8'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD9'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD10'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD11'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD12'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD13'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD14'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD15'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD0'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD1'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD2'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD3'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD4'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD5'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD6'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD7'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD8'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD9'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD10'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD11'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD12'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD13'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD14'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ),
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD15'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        )
    ),
    SOI = cms.untracked.int32(4),
    Src = cms.untracked.InputTag("hcalDigis","ZDC")
)


process.siPixelRecHitsPreSplitting = SwitchProducerCUDA(
    cpu = cms.EDProducer("SiPixelRecHitConverter",
        CPE = cms.string('PixelCPEGeneric'),
        VerboseLevel = cms.untracked.int32(0),
        src = cms.InputTag("siPixelClustersPreSplitting")
    )
)


process.siPixelRecHitsPreSplittingSoA = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        siPixelRecHitsPreSplittingCPU = cms.VPSet(
            cms.PSet(
                type = cms.string('cmscudacompatCPUTraitsTrackingRecHit2DHeterogeneous')
            ),
            cms.PSet(
                type = cms.string('uintAsHostProduct')
            )
        )
    )
)


process.clusterCompatibilityFilter = cms.EDFilter("HIClusterCompatibilityFilter",
    cluscomSrc = cms.InputTag("hiClusterCompatibility"),
    clusterPars = cms.vdouble(0.0, 0.0045),
    clusterTrunc = cms.double(2.0),
    maxZ = cms.double(20.05),
    minZ = cms.double(-20.0),
    nhitsTrunc = cms.int32(150)
)


process.countPatElectrons = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    minNumber = cms.uint32(0),
    src = cms.InputTag("cleanPatElectrons")
)


process.countPatJets = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    minNumber = cms.uint32(0),
    src = cms.InputTag("cleanPatJets")
)


process.countPatLeptons = cms.EDFilter("PATLeptonCountFilter",
    countElectrons = cms.bool(True),
    countMuons = cms.bool(True),
    countTaus = cms.bool(False),
    electronSource = cms.InputTag("cleanPatElectrons"),
    maxNumber = cms.uint32(999999),
    minNumber = cms.uint32(0),
    muonSource = cms.InputTag("cleanPatMuons"),
    tauSource = cms.InputTag("cleanPatTaus")
)


process.countPatMuons = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    minNumber = cms.uint32(0),
    src = cms.InputTag("cleanPatMuons")
)


process.countPatPhotons = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    minNumber = cms.uint32(0),
    src = cms.InputTag("cleanPatPhotons")
)


process.countPatTaus = cms.EDFilter("PATCandViewCountFilter",
    maxNumber = cms.uint32(999999),
    minNumber = cms.uint32(0),
    src = cms.InputTag("cleanPatTaus")
)


process.goodOfflinePrimaryVertices = cms.EDFilter("VertexSelector",
    cut = cms.string('!isFake && ndof >= 4.0 && abs(z) <= 24.0 && abs(position.Rho) <= 2.0'),
    filter = cms.bool(False),
    src = cms.InputTag("offlinePrimaryVertices")
)


process.highPurityGeneralTracks = cms.EDFilter("TrackSelector",
    cut = cms.string('quality("highPurity")'),
    src = cms.InputTag("generalTracks")
)


process.hltPixelClusterShapeFilter = cms.EDFilter("HLTPixelClusterShapeFilter",
    clusterPars = cms.vdouble(0, 0.0045),
    clusterTrunc = cms.double(2),
    inputTag = cms.InputTag("siPixelRecHits"),
    maxZ = cms.double(20.05),
    mightGet = cms.optional.untracked.vstring,
    minZ = cms.double(-20),
    nhitsTrunc = cms.int32(150),
    saveTags = cms.bool(True),
    zStep = cms.double(0.2)
)


process.pfAllChargedHadronsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212
    ),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllChargedParticlesPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212, 11, -11, 13,
        -13
    ),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllNeutralHadronsAndPhotonsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22, 111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllNeutralHadronsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllPhotonsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfEmptyCollection = cms.EDFilter("GenericPFCandidateSelector",
    cut = cms.string('pt<0'),
    src = cms.InputTag("particleFlow")
)


process.pfPileUpAllChargedParticlesPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212, 11, -11, 13,
        -13
    ),
    src = cms.InputTag("pfPileUpIsoPFBRECO")
)


process.phfCoincFilter2Th4 = cms.EDFilter("HiHFFilter",
    HFfilters = cms.InputTag("hiHFfilters","hiHFfilters","PAT"),
    minnumtowers = cms.int32(2),
    threshold = cms.int32(4)
)


process.primaryVertexFilter = cms.EDFilter("VertexSelector",
    cut = cms.string('!isFake && abs(z) <= 25 && position.Rho <= 2'),
    filter = cms.bool(True),
    src = cms.InputTag("offlineSlimmedPrimaryVerticesRecovery")
)


process.selectedPatDisplacedMuons = cms.EDFilter("PATMuonSelector",
    cut = cms.string(''),
    src = cms.InputTag("patDisplacedMuons")
)


process.selectedPatElectrons = cms.EDFilter("PATElectronSelector",
    cut = cms.string(''),
    src = cms.InputTag("patElectrons")
)


process.selectedPatJets = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    cutLoose = cms.string(''),
    nLoose = cms.uint32(0),
    src = cms.InputTag("patJets")
)


process.selectedPatLowPtElectrons = cms.EDFilter("PATElectronSelector",
    cut = cms.string("pt > 1. && electronID(\'ID\') > -0.25"),
    src = cms.InputTag("patLowPtElectrons")
)


process.selectedPatMuons = cms.EDFilter("PATMuonSelector",
    cut = cms.string(''),
    src = cms.InputTag("patMuons")
)


process.selectedPatOOTPhotons = cms.EDFilter("PATPhotonSelector",
    cut = cms.string(''),
    src = cms.InputTag("patOOTPhotons")
)


process.selectedPatPhotons = cms.EDFilter("PATPhotonSelector",
    cut = cms.string(''),
    src = cms.InputTag("patPhotons")
)


process.selectedPatTaus = cms.EDFilter("PATTauSelector",
    cut = cms.string(''),
    src = cms.InputTag("patTaus")
)


process.tauGenJetsSelectorAllHadrons = cms.EDFilter("TauGenJetDecayModeSelector",
    filter = cms.bool(False),
    select = cms.vstring(
        'oneProng0Pi0',
        'oneProng1Pi0',
        'oneProng2Pi0',
        'oneProngOther',
        'threeProng0Pi0',
        'threeProng1Pi0',
        'threeProngOther',
        'rare'
    ),
    src = cms.InputTag("tauGenJets")
)


process.HiForestInfo = cms.EDAnalyzer("HiForestInfo",
    GlobalTagLabel = cms.string('124X_dataRun2_PromptLike_HI_v1'),
    HiForestVersion = cms.string(''),
    info = cms.vstring(
        'HiForest, miniAOD, 125X, data',
        'CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1033p1x01_offline'
    )
)


process.PbPbTracks = cms.EDAnalyzer("TrackAnalyzer",
    beamSpotSrc = cms.untracked.InputTag("offlineBeamSpot"),
    chi2Map = cms.InputTag("packedPFCandidateTrackChi2"),
    chi2MapLost = cms.InputTag("lostTrackChi2"),
    doTrack = cms.untracked.bool(True),
    lostTracksSrc = cms.InputTag("lostTracks"),
    packedCandSrc = cms.InputTag("packedPFCandidates"),
    trackPtMin = cms.untracked.double(0.01),
    vertexSrc = cms.InputTag("unpackedTracksAndVertices")
)


process.akCs2PFJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetSubstructure",
    doChargedConstOnly = cms.untracked.bool(True),
    doGenSym = cms.untracked.bool(False),
    doGenTaus = cms.untracked.bool(False),
    doHardestSplitMatching = cms.untracked.bool(False),
    doHiJetID = cms.untracked.bool(True),
    doJetConstituents = cms.untracked.bool(False),
    doLifeTimeTagging = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(False),
    doSubjetPurity = cms.untracked.bool(False),
    doTower = cms.untracked.bool(False),
    doWTARecluster = cms.untracked.bool(False),
    dopthatcut = cms.untracked.bool(False),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genjetTag = cms.InputTag("ak4HiGenJets"),
    groom_combine = cms.double(1),
    groom_type = cms.double(0),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetName = cms.untracked.string('akCs2PF'),
    jetPtMin = cms.double(10.0),
    jetTag = cms.InputTag("akCs2PFpatJets"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("akPu4PFpatJets"),
    mydynktcut = cms.double(1),
    mysdcut1 = cms.double(0.2),
    mysdcut2 = cms.double(0.1),
    pfCandSource = cms.InputTag("packedPFCandidates"),
    rParam = cms.double(0.2),
    towersSrc = cms.InputTag("towerMaker"),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiTracks"),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True),
    useRawPt = cms.untracked.bool(False),
    vtxTag = cms.InputTag("hiSelectedVertex")
)


process.akCs4PFJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetSubstructure",
    doChargedConstOnly = cms.untracked.bool(True),
    doGenSym = cms.untracked.bool(False),
    doGenTaus = cms.untracked.bool(False),
    doHardestSplitMatching = cms.untracked.bool(False),
    doHiJetID = cms.untracked.bool(True),
    doJetConstituents = cms.untracked.bool(False),
    doLifeTimeTagging = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(False),
    doSubjetPurity = cms.untracked.bool(False),
    doTower = cms.untracked.bool(False),
    doWTARecluster = cms.untracked.bool(False),
    dopthatcut = cms.untracked.bool(False),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genjetTag = cms.InputTag("ak4HiGenJets"),
    groom_combine = cms.double(1),
    groom_type = cms.double(0),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetName = cms.untracked.string('akCs0PF'),
    jetPtMin = cms.double(10.0),
    jetTag = cms.InputTag("akCs0PFpatJets"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("akPu4PFpatJets"),
    mydynktcut = cms.double(1),
    mysdcut1 = cms.double(0.2),
    mysdcut2 = cms.double(0.1),
    pfCandSource = cms.InputTag("packedPFCandidates"),
    rParam = cms.double(0.4),
    towersSrc = cms.InputTag("towerMaker"),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiTracks"),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True),
    useRawPt = cms.untracked.bool(False),
    vtxTag = cms.InputTag("hiSelectedVertex")
)


process.akFlowPuCs2PFJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetSubstructure",
    doChargedConstOnly = cms.untracked.bool(True),
    doGenSym = cms.untracked.bool(False),
    doGenTaus = cms.untracked.bool(False),
    doHardestSplitMatching = cms.untracked.bool(False),
    doHiJetID = cms.untracked.bool(True),
    doJetConstituents = cms.untracked.bool(False),
    doLifeTimeTagging = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(False),
    doSubjetPurity = cms.untracked.bool(False),
    doTower = cms.untracked.bool(False),
    doWTARecluster = cms.untracked.bool(False),
    dopthatcut = cms.untracked.bool(False),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genjetTag = cms.InputTag("ak4HiGenJets"),
    groom_combine = cms.double(1),
    groom_type = cms.double(0),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetName = cms.untracked.string('akCs2PF'),
    jetPtMin = cms.double(10.0),
    jetTag = cms.InputTag("slimmedJets"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("akPu4PFpatJets"),
    mydynktcut = cms.double(1),
    mysdcut1 = cms.double(0.2),
    mysdcut2 = cms.double(0.1),
    pfCandSource = cms.InputTag("packedPFCandidates"),
    rParam = cms.double(0.2),
    towersSrc = cms.InputTag("towerMaker"),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiTracks"),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True),
    useRawPt = cms.untracked.bool(False),
    vtxTag = cms.InputTag("hiSelectedVertex")
)


process.akFlowPuCs4PFJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetSubstructure",
    doChargedConstOnly = cms.untracked.bool(True),
    doGenSym = cms.untracked.bool(False),
    doGenTaus = cms.untracked.bool(False),
    doHardestSplitMatching = cms.untracked.bool(False),
    doHiJetID = cms.untracked.bool(True),
    doJetConstituents = cms.untracked.bool(False),
    doLifeTimeTagging = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(False),
    doSubjetPurity = cms.untracked.bool(False),
    doTower = cms.untracked.bool(False),
    doWTARecluster = cms.untracked.bool(False),
    dopthatcut = cms.untracked.bool(False),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genjetTag = cms.InputTag("ak4HiGenJets"),
    groom_combine = cms.double(1),
    groom_type = cms.double(0),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetName = cms.untracked.string('akCs4PF'),
    jetPtMin = cms.double(10.0),
    jetTag = cms.InputTag("slimmedJets"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("akPu4PFpatJets"),
    mydynktcut = cms.double(1),
    mysdcut1 = cms.double(0.2),
    mysdcut2 = cms.double(0.1),
    pfCandSource = cms.InputTag("packedPFCandidates"),
    rParam = cms.double(0.4),
    towersSrc = cms.InputTag("towerMaker"),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiTracks"),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True),
    useRawPt = cms.untracked.bool(False),
    vtxTag = cms.InputTag("hiSelectedVertex")
)


process.cleanPatCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
    candidates = cms.VInputTag(cms.InputTag("cleanPatElectrons"), cms.InputTag("cleanPatMuons"), cms.InputTag("cleanPatTaus"), cms.InputTag("cleanPatPhotons"), cms.InputTag("cleanPatJets")),
    logName = cms.untracked.string('cleanPatCandidates|PATSummaryTables')
)


process.ggHiNtuplizer = cms.EDAnalyzer("ggHiNtuplizer",
    beamSpotSrc = cms.InputTag("offlineBeamSpot"),
    conversionsSrc = cms.InputTag("reducedEgamma","reducedConversions"),
    doEffectiveAreas = cms.bool(True),
    doElectrons = cms.bool(False),
    doGenParticles = cms.bool(False),
    doMuons = cms.bool(False),
    doPackedGenParticle = cms.bool(True),
    doPfIso = cms.bool(True),
    doPhoERegression = cms.bool(True),
    doPhotons = cms.bool(True),
    doRecHitsEB = cms.bool(False),
    doRecHitsEE = cms.bool(False),
    doSuperClusters = cms.bool(False),
    effAreasConfigFile = cms.FileInPath('HeavyIonsAnalysis/EGMAnalysis/data/EffectiveAreas_94X_v0'),
    electronSrc = cms.InputTag("correctedElectrons"),
    genParticleSrc = cms.InputTag("packedGenParticles"),
    isPackedPFCandidate = cms.bool(True),
    isParticleGun = cms.bool(False),
    muonSrc = cms.InputTag("unpackedMuons"),
    particleFlowCollection = cms.InputTag("packedPFCandidates"),
    photonSrc = cms.InputTag("slimmedPhotons"),
    pileupSrc = cms.InputTag("slimmedAddPileupInfo"),
    recHitsEB = cms.untracked.InputTag("reducedEgamma","reducedEBRecHits"),
    recHitsEE = cms.untracked.InputTag("reducedEgamma","reducedEERecHits"),
    rhoSrc = cms.InputTag("fixedGridRhoFastjetAll"),
    signalGenParticleSrc = cms.InputTag("packedGenParticlesSignal"),
    superClusters = cms.InputTag("reducedEgamma","reducedSuperClusters"),
    useValMapIso = cms.bool(True),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.hiEvtAnalyzer = cms.EDAnalyzer("HiEvtAnalyzer",
    CentralityBinSrc = cms.InputTag("centralityBin","HFtowers"),
    CentralitySrc = cms.InputTag("hiCentrality"),
    EvtPlane = cms.InputTag("hiEvtPlane"),
    EvtPlaneFlat = cms.InputTag("hiEvtPlaneFlat"),
    HFfilters = cms.InputTag("hiHFfilters","hiHFfilters"),
    HiMC = cms.InputTag("heavyIon"),
    Vertex = cms.InputTag("offlineSlimmedPrimaryVerticesRecovery"),
    doCentrality = cms.bool(True),
    doEvtPlane = cms.bool(True),
    doEvtPlaneFlat = cms.bool(True),
    doHFfilters = cms.bool(True),
    doHiMC = cms.bool(False),
    doMC = cms.bool(False),
    doVertex = cms.bool(True),
    evtPlaneLevel = cms.int32(0),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    useHepMC = cms.bool(False)
)


process.hltanalysis = cms.EDAnalyzer("TriggerAnalyzer",
    HLTProcessName = cms.string('HLT'),
    hltPSProvCfg = cms.PSet(
        stageL1Trigger = cms.uint32(2)
    ),
    hltdummybranches = cms.vstring( (
        'DST_Physics_v7',
        'AlCa_EcalEtaEBonlyForHI_v1',
        'AlCa_EcalEtaEEonlyForHI_v1',
        'AlCa_EcalPhiSymForHI_v1',
        'AlCa_EcalPi0EBonlyForHI_v1',
        'AlCa_EcalPi0EEonlyForHI_v1',
        'AlCa_RPCMuonNormalisationForHI_v1',
        'HLT_EcalCalibration_v4',
        'HLT_HICastorMinimumBias_part0_v1',
        'HLT_HICastorMinimumBias_part10_v1',
        'HLT_HICastorMinimumBias_part11_v1',
        'HLT_HICastorMinimumBias_part12_v1',
        'HLT_HICastorMinimumBias_part13_v1',
        'HLT_HICastorMinimumBias_part14_v1',
        'HLT_HICastorMinimumBias_part15_v1',
        'HLT_HICastorMinimumBias_part16_v1',
        'HLT_HICastorMinimumBias_part17_v1',
        'HLT_HICastorMinimumBias_part18_v1',
        'HLT_HICastorMinimumBias_part19_v1',
        'HLT_HICastorMinimumBias_part1_v1',
        'HLT_HICastorMinimumBias_part2_v1',
        'HLT_HICastorMinimumBias_part3_v1',
        'HLT_HICastorMinimumBias_part4_v1',
        'HLT_HICastorMinimumBias_part5_v1',
        'HLT_HICastorMinimumBias_part6_v1',
        'HLT_HICastorMinimumBias_part7_v1',
        'HLT_HICastorMinimumBias_part8_v1',
        'HLT_HICastorMinimumBias_part9_v1',
        'HLT_HICastor_HighJet_BptxAND_v1',
        'HLT_HICastor_HighJet_MBHF1AND_BptxAND_v1',
        'HLT_HICastor_HighJet_MBHF1OR_BptxAND_v1',
        'HLT_HICastor_HighJet_MBHF1OR_v1',
        'HLT_HICastor_HighJet_MBHF2AND_BptxAND_v1',
        'HLT_HICastor_HighJet_NotMBHF2AND_v1',
        'HLT_HICastor_HighJet_NotMBHF2OR_v1',
        'HLT_HICastor_HighJet_v1',
        'HLT_HICastor_MediumJet_BptxAND_v1',
        'HLT_HICastor_MediumJet_MBHF1OR_BptxAND_v1',
        'HLT_HICastor_MediumJet_MBHF1OR_v1',
        'HLT_HICastor_MediumJet_NotMBHF2AND_v1',
        'HLT_HICastor_MediumJet_NotMBHF2OR_v1',
        'HLT_HICastor_MediumJet_SingleEG5_MBHF1OR_BptxAND_v1',
        'HLT_HICastor_MediumJet_SingleEG5_MBHF1OR_v1',
        'HLT_HICastor_MediumJet_SingleMu0_MBHF1OR_BptxAND_v1',
        'HLT_HICastor_MediumJet_SingleMu0_MBHF1OR_v1',
        'HLT_HICastor_MediumJet_v1',
        'HLT_HICastor_Muon_BptxAND_v1',
        'HLT_HICastor_Muon_v1',
        'HLT_HICentrality30100_FirstCollisionAfterAbortGap_v1',
        'HLT_HICentralityTag20100_v1',
        'HLT_HICentralityTag30100_v1',
        'HLT_HICentralityTag50100_v1',
        'HLT_HICentralityVeto_Beamspot_v1',
        'HLT_HICentralityVeto_v1',
        'HLT_HICsAK4PFJet100Eta1p5_Beamspot_v1',
        'HLT_HICsAK4PFJet100Eta1p5_Centrality_30_100_v1',
        'HLT_HICsAK4PFJet100Eta1p5_Centrality_50_100_v1',
        'HLT_HICsAK4PFJet100Eta1p5_v1',
        'HLT_HICsAK4PFJet120Eta1p5_v1',
        'HLT_HICsAK4PFJet60Eta1p5_Centrality_30_100_v1',
        'HLT_HICsAK4PFJet60Eta1p5_Centrality_50_100_v1',
        'HLT_HICsAK4PFJet60Eta1p5_v1',
        'HLT_HICsAK4PFJet80Eta1p5_Centrality_30_100_v1',
        'HLT_HICsAK4PFJet80Eta1p5_Centrality_50_100_v1',
        'HLT_HICsAK4PFJet80Eta1p5_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt15_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt20_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt30_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt40_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt50_v1',
        'HLT_HIDmesonPPTrackingGlobal_Dpt60_v1',
        'HLT_HIDoubleEle10GsfMass50_v1',
        'HLT_HIDoubleEle10Gsf_v1',
        'HLT_HIDoubleEle15GsfMass50_v1',
        'HLT_HIDoubleEle15Gsf_v1',
        'HLT_HIDsPPTrackingGlobal_Dpt20_v1',
        'HLT_HIDsPPTrackingGlobal_Dpt30_v1',
        'HLT_HIDsPPTrackingGlobal_Dpt40_v1',
        'HLT_HIDsPPTrackingGlobal_Dpt50_v1',
        'HLT_HIDsPPTrackingGlobal_Dpt60_v1',
        'HLT_HIEle10Gsf_PuAK4CaloJet100Eta2p1_v1',
        'HLT_HIEle10Gsf_PuAK4CaloJet40Eta2p1_v1',
        'HLT_HIEle10Gsf_PuAK4CaloJet60Eta2p1_v1',
        'HLT_HIEle10Gsf_PuAK4CaloJet80Eta2p1_v1',
        'HLT_HIEle10Gsf_v1',
        'HLT_HIEle15Ele10GsfMass50_v1',
        'HLT_HIEle15Ele10Gsf_v1',
        'HLT_HIEle15Gsf_PuAK4CaloJet100Eta2p1_v1',
        'HLT_HIEle15Gsf_PuAK4CaloJet40Eta2p1_v1',
        'HLT_HIEle15Gsf_PuAK4CaloJet60Eta2p1_v1',
        'HLT_HIEle15Gsf_PuAK4CaloJet80Eta2p1_v1',
        'HLT_HIEle15Gsf_v1',
        'HLT_HIEle20Gsf_PuAK4CaloJet100Eta2p1_v1',
        'HLT_HIEle20Gsf_PuAK4CaloJet40Eta2p1_v1',
        'HLT_HIEle20Gsf_PuAK4CaloJet60Eta2p1_v1',
        'HLT_HIEle20Gsf_PuAK4CaloJet80Eta2p1_v1',
        'HLT_HIEle20Gsf_v1',
        'HLT_HIEle30Gsf_v1',
        'HLT_HIEle40Gsf_v1',
        'HLT_HIEle50Gsf_v1',
        'HLT_HIFullTracks2018_HighPt18_v1',
        'HLT_HIFullTracks2018_HighPt24_v1',
        'HLT_HIFullTracks2018_HighPt34_v1',
        'HLT_HIFullTracks2018_HighPt45_v1',
        'HLT_HIFullTracks2018_HighPt56_v1',
        'HLT_HIFullTracks2018_HighPt60_v1',
        'HLT_HIFullTracks_Multiplicity020_HF1AND_v1',
        'HLT_HIFullTracks_Multiplicity020_HF1OR_v1',
        'HLT_HIFullTracks_Multiplicity020_HF2OR_v1',
        'HLT_HIFullTracks_Multiplicity020_v1',
        'HLT_HIFullTracks_Multiplicity2040_HF1AND_v1',
        'HLT_HIFullTracks_Multiplicity2040_HF1OR_v1',
        'HLT_HIFullTracks_Multiplicity2040_HF2OR_v1',
        'HLT_HIFullTracks_Multiplicity2040_v1',
        'HLT_HIFullTracks_Multiplicity335_HF1OR_v1',
        'HLT_HIFullTracks_Multiplicity4060_v1',
        'HLT_HIFullTracks_Multiplicity6080_v1',
        'HLT_HIFullTracks_Multiplicity80100_v1',
        'HLT_HIGEDPhoton10_Cent30_100_v1',
        'HLT_HIGEDPhoton10_Cent50_100_v1',
        'HLT_HIGEDPhoton10_EB_HECut_v1',
        'HLT_HIGEDPhoton10_EB_v1',
        'HLT_HIGEDPhoton10_HECut_v1',
        'HLT_HIGEDPhoton10_v1',
        'HLT_HIGEDPhoton20_Cent30_100_v1',
        'HLT_HIGEDPhoton20_Cent50_100_v1',
        'HLT_HIGEDPhoton20_EB_HECut_v1',
        'HLT_HIGEDPhoton20_EB_v1',
        'HLT_HIGEDPhoton20_HECut_v1',
        'HLT_HIGEDPhoton20_v1',
        'HLT_HIGEDPhoton30_Cent30_100_v1',
        'HLT_HIGEDPhoton30_Cent50_100_v1',
        'HLT_HIGEDPhoton30_EB_HECut_v1',
        'HLT_HIGEDPhoton30_EB_v1',
        'HLT_HIGEDPhoton30_HECut_v1',
        'HLT_HIGEDPhoton30_v1',
        'HLT_HIGEDPhoton40_Cent30_100_v1',
        'HLT_HIGEDPhoton40_Cent50_100_v1',
        'HLT_HIGEDPhoton40_EB_HECut_v1',
        'HLT_HIGEDPhoton40_EB_v1',
        'HLT_HIGEDPhoton40_HECut_v1',
        'HLT_HIGEDPhoton40_v1',
        'HLT_HIGEDPhoton50_EB_HECut_v1',
        'HLT_HIGEDPhoton50_EB_v1',
        'HLT_HIGEDPhoton50_HECut_v1',
        'HLT_HIGEDPhoton50_v1',
        'HLT_HIGEDPhoton60_EB_HECut_v1',
        'HLT_HIGEDPhoton60_EB_v1',
        'HLT_HIGEDPhoton60_HECut_v1',
        'HLT_HIGEDPhoton60_v1',
        'HLT_HIHcalNZS_v1',
        'HLT_HIHcalPhiSym_v1',
        'HLT_HIIslandPhoton10_Eta1p5_v1',
        'HLT_HIIslandPhoton10_Eta2p4_Cent30_100_v1',
        'HLT_HIIslandPhoton10_Eta2p4_Cent50_100_v1',
        'HLT_HIIslandPhoton10_Eta2p4_v1',
        'HLT_HIIslandPhoton10_Eta3p1_Cent30_100_v1',
        'HLT_HIIslandPhoton10_Eta3p1_Cent50_100_v1',
        'HLT_HIIslandPhoton10_Eta3p1_v1',
        'HLT_HIIslandPhoton20_Eta1p5_v1',
        'HLT_HIIslandPhoton20_Eta2p4_Cent30_100_v1',
        'HLT_HIIslandPhoton20_Eta2p4_Cent50_100_v1',
        'HLT_HIIslandPhoton20_Eta2p4_v1',
        'HLT_HIIslandPhoton20_Eta3p1_Cent30_100_v1',
        'HLT_HIIslandPhoton20_Eta3p1_Cent50_100_v1',
        'HLT_HIIslandPhoton20_Eta3p1_v1',
        'HLT_HIIslandPhoton30_Eta1p5_v1',
        'HLT_HIIslandPhoton30_Eta2p4_Cent30_100_v1',
        'HLT_HIIslandPhoton30_Eta2p4_Cent50_100_v1',
        'HLT_HIIslandPhoton30_Eta2p4_v1',
        'HLT_HIIslandPhoton30_Eta3p1_Cent30_100_v1',
        'HLT_HIIslandPhoton30_Eta3p1_Cent50_100_v1',
        'HLT_HIIslandPhoton30_Eta3p1_v1',
        'HLT_HIIslandPhoton40_Eta1p5_v1',
        'HLT_HIIslandPhoton40_Eta2p4_Cent30_100_v1',
        'HLT_HIIslandPhoton40_Eta2p4_Cent50_100_v1',
        'HLT_HIIslandPhoton40_Eta2p4_v1',
        'HLT_HIIslandPhoton40_Eta3p1_Cent30_100_v1',
        'HLT_HIIslandPhoton40_Eta3p1_Cent50_100_v1',
        'HLT_HIIslandPhoton40_Eta3p1_v1',
        'HLT_HIIslandPhoton50_Eta1p5_v1',
        'HLT_HIIslandPhoton50_Eta2p4_v1',
        'HLT_HIIslandPhoton50_Eta3p1_v1',
        'HLT_HIIslandPhoton60_Eta1p5_v1',
        'HLT_HIIslandPhoton60_Eta2p4_v1',
        'HLT_HIIslandPhoton60_Eta3p1_v1',
        'HLT_HIL1DoubleMu0_v1',
        'HLT_HIL1DoubleMu10_v1',
        'HLT_HIL1DoubleMuOpen_Centrality_30_100_v1',
        'HLT_HIL1DoubleMuOpen_Centrality_40_100_v1',
        'HLT_HIL1DoubleMuOpen_Centrality_50_100_v1',
        'HLT_HIL1DoubleMuOpen_MAXdR2p0_v1',
        'HLT_HIL1DoubleMuOpen_MAXdR3p5_v1',
        'HLT_HIL1DoubleMuOpen_OS_Centrality_30_100_v1',
        'HLT_HIL1DoubleMuOpen_OS_Centrality_40_100_v1',
        'HLT_HIL1DoubleMuOpen_OS_MAXdR2p0_v1',
        'HLT_HIL1DoubleMuOpen_OS_er1p6_v1',
        'HLT_HIL1DoubleMuOpen_OS_v1',
        'HLT_HIL1DoubleMuOpen_SS_v1',
        'HLT_HIL1DoubleMuOpen_er1p6_v1',
        'HLT_HIL1DoubleMuOpen_v1',
        'HLT_HIL1Mu3Eta2p5_Ele10Gsf_v1',
        'HLT_HIL1Mu3Eta2p5_Ele15Gsf_v1',
        'HLT_HIL1Mu3Eta2p5_Ele20Gsf_v1',
        'HLT_HIL1Mu3_Centrality_70_100_v1',
        'HLT_HIL1Mu3_Centrality_80_100_v1',
        'HLT_HIL1Mu3_v1',
        'HLT_HIL1Mu5Eta2p5_Ele10Gsf_v1',
        'HLT_HIL1Mu5Eta2p5_Ele15Gsf_v1',
        'HLT_HIL1Mu5Eta2p5_Ele20Gsf_v1',
        'HLT_HIL1Mu5_v1',
        'HLT_HIL1Mu7Eta2p5_Ele10Gsf_v1',
        'HLT_HIL1Mu7Eta2p5_Ele15Gsf_v1',
        'HLT_HIL1Mu7Eta2p5_Ele20Gsf_v1',
        'HLT_HIL1Mu7_v1',
        'HLT_HIL1MuOpen_Centrality_70_100_v1',
        'HLT_HIL1MuOpen_Centrality_80_100_v1',
        'HLT_HIL1NotBptxOR_v1',
        'HLT_HIL1UnpairedBunchBptxMinus_v1',
        'HLT_HIL1UnpairedBunchBptxPlus_v1',
        'HLT_HIL1_ETT10_ETTAsym50_MinimumBiasHF1_OR_BptxAND_v1',
        'HLT_HIL1_ETT60_ETTAsym65_MinimumBiasHF2_OR_PixelTracks10_v1',
        'HLT_HIL1_ETT65_ETTAsym80_MinimumBiasHF2_OR_PixelTracks10_v1',
        'HLT_HIL1_ETT8_ETTAsym50_MinimumBiasHF1_OR_BptxAND_v1',
        'HLT_HIL1_ZDC_AND_OR_MinimumBiasHF1_AND_BptxAND_v1',
        'HLT_HIL1_ZDC_AND_OR_MinimumBiasHF2_AND_BptxAND_v1',
        'HLT_HIL2DoubleMuOpen_v1',
        'HLT_HIL2DoubleMu_L1DoubleMuOpen_OS_MAXdR2p0_v1',
        'HLT_HIL2Mu12_v1',
        'HLT_HIL2Mu15_v1',
        'HLT_HIL2Mu20_v1',
        'HLT_HIL2Mu3_NHitQ10_v1',
        'HLT_HIL2Mu3_NHitQ15_tagging_v1',
        'HLT_HIL2Mu3_NHitQ15_v1',
        'HLT_HIL2Mu3_v1',
        'HLT_HIL2Mu5_NHitQ10_v1',
        'HLT_HIL2Mu5_NHitQ15_tagging_v1',
        'HLT_HIL2Mu5_NHitQ15_v1',
        'HLT_HIL2Mu5_v1',
        'HLT_HIL2Mu7_NHitQ10_v1',
        'HLT_HIL2Mu7_NHitQ15_tagging_v1',
        'HLT_HIL2Mu7_NHitQ15_v1',
        'HLT_HIL2Mu7_v1',
        'HLT_HIL2_L1DoubleMu10_v1',
        'HLT_HIL3DoubleMuOpen_JpsiPsi_v1',
        'HLT_HIL3DoubleMuOpen_M60120_v1',
        'HLT_HIL3DoubleMuOpen_Upsi_v1',
        'HLT_HIL3DoubleMuOpen_v1',
        'HLT_HIL3Mu0NHitQ10_L2Mu0_MAXdR3p5_M1to5_v1',
        'HLT_HIL3Mu0_L2Mu0_v1',
        'HLT_HIL3Mu12_v1',
        'HLT_HIL3Mu15_v1',
        'HLT_HIL3Mu20_v1',
        'HLT_HIL3Mu2p5NHitQ10_L2Mu2_M7toinf_v1',
        'HLT_HIL3Mu2p5NHitQ10_L2Mu2_v1',
        'HLT_HIL3Mu2p5_L1DoubleMu0_v1',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet100Eta2p1_FilterDr_v1',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet100Eta2p1_v1',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet40Eta2p1_FilterDr_v1',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet40Eta2p1_v1',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet60Eta2p1_FilterDr_v1',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet60Eta2p1_v1',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet80Eta2p1_FilterDr_v1',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet80Eta2p1_v1',
        'HLT_HIL3Mu3NHitQ10_L1DoubleMuOpen_v1',
        'HLT_HIL3Mu3_EG10HECut_v1',
        'HLT_HIL3Mu3_EG15HECut_v1',
        'HLT_HIL3Mu3_EG20HECut_v1',
        'HLT_HIL3Mu3_EG30HECut_v1',
        'HLT_HIL3Mu3_L1DoubleMu0_v1',
        'HLT_HIL3Mu3_L1DoubleMuOpen_OS_v1',
        'HLT_HIL3Mu3_L1DoubleMuOpen_v1',
        'HLT_HIL3Mu3_L1TripleMuOpen_v1',
        'HLT_HIL3Mu3_NHitQ10_tagging_v1',
        'HLT_HIL3Mu3_NHitQ10_v1',
        'HLT_HIL3Mu3_v1',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet100Eta2p1_FilterDr_v1',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet100Eta2p1_v1',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet40Eta2p1_FilterDr_v1',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet40Eta2p1_v1',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet60Eta2p1_FilterDr_v1',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet60Eta2p1_v1',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet80Eta2p1_FilterDr_v1',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet80Eta2p1_v1',
        'HLT_HIL3Mu5_EG10HECut_v1',
        'HLT_HIL3Mu5_EG15HECut_v1',
        'HLT_HIL3Mu5_EG20HECut_v1',
        'HLT_HIL3Mu5_EG30HECut_v1',
        'HLT_HIL3Mu5_NHitQ10_tagging_v1',
        'HLT_HIL3Mu5_NHitQ10_v1',
        'HLT_HIL3Mu5_v1',
        'HLT_HIL3Mu7_EG10HECut_v1',
        'HLT_HIL3Mu7_EG15HECut_v1',
        'HLT_HIL3Mu7_EG20HECut_v1',
        'HLT_HIL3Mu7_EG30HECut_v1',
        'HLT_HIL3Mu7_NHitQ10_tagging_v1',
        'HLT_HIL3Mu7_NHitQ10_v1',
        'HLT_HIL3Mu7_v1',
        'HLT_HIL3_L1DoubleMu10_v1',
        'HLT_HILcPPTrackingGlobal_Dpt20_v1',
        'HLT_HILcPPTrackingGlobal_Dpt30_v1',
        'HLT_HILcPPTrackingGlobal_Dpt40_v1',
        'HLT_HILcPPTrackingGlobal_Dpt50_v1',
        'HLT_HILcPPTrackingGlobal_Dpt60_v1',
        'HLT_HIMinimumBiasHFOR_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part0_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part10_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part11_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part12_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part13_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part14_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part15_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part16_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part17_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part18_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part19_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part1_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part20_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part21_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part22_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part23_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part2_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part3_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part4_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part5_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part6_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part7_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part8_v1',
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part9_v1',
        'HLT_HIMinimumBiasRF_part0_v1',
        'HLT_HIMinimumBiasRF_part10_v1',
        'HLT_HIMinimumBiasRF_part11_v1',
        'HLT_HIMinimumBiasRF_part12_v1',
        'HLT_HIMinimumBiasRF_part13_v1',
        'HLT_HIMinimumBiasRF_part14_v1',
        'HLT_HIMinimumBiasRF_part15_v1',
        'HLT_HIMinimumBiasRF_part16_v1',
        'HLT_HIMinimumBiasRF_part17_v1',
        'HLT_HIMinimumBiasRF_part18_v1',
        'HLT_HIMinimumBiasRF_part19_v1',
        'HLT_HIMinimumBiasRF_part1_v1',
        'HLT_HIMinimumBiasRF_part20_v1',
        'HLT_HIMinimumBiasRF_part21_v1',
        'HLT_HIMinimumBiasRF_part22_v1',
        'HLT_HIMinimumBiasRF_part23_v1',
        'HLT_HIMinimumBiasRF_part2_v1',
        'HLT_HIMinimumBiasRF_part3_v1',
        'HLT_HIMinimumBiasRF_part4_v1',
        'HLT_HIMinimumBiasRF_part5_v1',
        'HLT_HIMinimumBiasRF_part6_v1',
        'HLT_HIMinimumBiasRF_part7_v1',
        'HLT_HIMinimumBiasRF_part8_v1',
        'HLT_HIMinimumBiasRF_part9_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part0_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part10_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part11_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part12_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part13_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part14_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part15_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part16_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part17_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part18_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part19_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part1_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part2_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part3_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part4_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part5_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part6_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part7_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part8_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part9_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part0_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part10_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part11_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part12_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part13_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part14_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part15_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part16_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part17_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part18_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part19_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part1_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part2_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part3_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part4_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part5_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part6_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part7_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part8_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part9_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part0_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part10_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part11_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part12_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part13_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part14_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part15_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part16_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part17_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part18_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part19_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part1_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part2_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part3_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part4_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part5_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part6_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part7_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part8_v1',
        'HLT_HIMinimumBias_SinglePixelTrack_part9_v1',
        'HLT_HIMinimumBias_part0_v1',
        'HLT_HIMinimumBias_part10_v1',
        'HLT_HIMinimumBias_part10_v6',
        'HLT_HIMinimumBias_part11_v1',
        'HLT_HIMinimumBias_part11_v6',
        'HLT_HIMinimumBias_part12_v1',
        'HLT_HIMinimumBias_part12_v7',
        'HLT_HIMinimumBias_part13_v1',
        'HLT_HIMinimumBias_part13_v7',
        'HLT_HIMinimumBias_part14_v1',
        'HLT_HIMinimumBias_part14_v8',
        'HLT_HIMinimumBias_part15_v1',
        'HLT_HIMinimumBias_part15_v8',
        'HLT_HIMinimumBias_part16_v1',
        'HLT_HIMinimumBias_part16_v9',
        'HLT_HIMinimumBias_part17_v1',
        'HLT_HIMinimumBias_part17_v9',
        'HLT_HIMinimumBias_part18_v1',
        'HLT_HIMinimumBias_part18_v10',
        'HLT_HIMinimumBias_part18_v11',
        'HLT_HIMinimumBias_part19_v1',
        'HLT_HIMinimumBias_part19_v10',
        'HLT_HIMinimumBias_part19_v11',
        'HLT_HIMinimumBias_part1_v1',
        'HLT_HIMinimumBias_part20_v1',
        'HLT_HIMinimumBias_part21_v1',
        'HLT_HIMinimumBias_part22_v1',
        'HLT_HIMinimumBias_part23_v1',
        'HLT_HIMinimumBias_part24_v1',
        'HLT_HIMinimumBias_part25_v1',
        'HLT_HIMinimumBias_part2_v1',
        'HLT_HIMinimumBias_part2_v2',
        'HLT_HIMinimumBias_part3_v1',
        'HLT_HIMinimumBias_part3_v2',
        'HLT_HIMinimumBias_part4_v1',
        'HLT_HIMinimumBias_part4_v3',
        'HLT_HIMinimumBias_part5_v1',
        'HLT_HIMinimumBias_part5_v3',
        'HLT_HIMinimumBias_part6_v1',
        'HLT_HIMinimumBias_part6_v4',
        'HLT_HIMinimumBias_part7_v1',
        'HLT_HIMinimumBias_part7_v4',
        'HLT_HIMinimumBias_part8_v1',
        'HLT_HIMinimumBias_part8_v5',
        'HLT_HIMinimumBias_part9_v1',
        'HLT_HIMinimumBias_part9_v5',
        'HLT_HIPhysicsForZS_v1',
        'HLT_HIPhysics_v1',
        'HLT_HIPuAK4CaloJet100Eta2p4_CSVv2WP0p75_v1',
        'HLT_HIPuAK4CaloJet100Eta2p4_CSVv2WP0p8_v1',
        'HLT_HIPuAK4CaloJet100Eta2p4_DeepCSV0p4_v1',
        'HLT_HIPuAK4CaloJet100Eta2p4_DeepCSV0p71_v1',
        'HLT_HIPuAK4CaloJet100Eta5p1_Centrality_30_100_v1',
        'HLT_HIPuAK4CaloJet100Eta5p1_Centrality_50_100_v1',
        'HLT_HIPuAK4CaloJet100Eta5p1_v1',
        'HLT_HIPuAK4CaloJet100Fwd_v1',
        'HLT_HIPuAK4CaloJet100_35_Eta0p7_v1',
        'HLT_HIPuAK4CaloJet100_35_Eta1p1_v1',
        'HLT_HIPuAK4CaloJet120Eta5p1_v1',
        'HLT_HIPuAK4CaloJet120Fwd_v1',
        'HLT_HIPuAK4CaloJet40Eta5p1_Centrality_30_100_v1',
        'HLT_HIPuAK4CaloJet40Eta5p1_Centrality_50_100_v1',
        'HLT_HIPuAK4CaloJet40Eta5p1_v1',
        'HLT_HIPuAK4CaloJet40Fwd_v1',
        'HLT_HIPuAK4CaloJet60Eta2p4_CSVv2WP0p75_v1',
        'HLT_HIPuAK4CaloJet60Eta2p4_CSVv2WP0p8_v1',
        'HLT_HIPuAK4CaloJet60Eta2p4_DeepCSV0p4_v1',
        'HLT_HIPuAK4CaloJet60Eta2p4_DeepCSV0p71_v1',
        'HLT_HIPuAK4CaloJet60Eta5p1_Centrality_30_100_v1',
        'HLT_HIPuAK4CaloJet60Eta5p1_Centrality_50_100_v1',
        'HLT_HIPuAK4CaloJet60Eta5p1_v1',
        'HLT_HIPuAK4CaloJet60Fwd_v1',
        'HLT_HIPuAK4CaloJet80Eta2p4_CSVv2WP0p75_v1',
        'HLT_HIPuAK4CaloJet80Eta2p4_CSVv2WP0p8_v1',
        'HLT_HIPuAK4CaloJet80Eta2p4_DeepCSV0p4_v1',
        'HLT_HIPuAK4CaloJet80Eta2p4_DeepCSV0p71_v1',
        'HLT_HIPuAK4CaloJet80Eta5p1_Centrality_30_100_v1',
        'HLT_HIPuAK4CaloJet80Eta5p1_Centrality_50_100_v1',
        'HLT_HIPuAK4CaloJet80Eta5p1_v1',
        'HLT_HIPuAK4CaloJet80Fwd_v1',
        'HLT_HIPuAK4CaloJet80_35_Eta0p7_v1',
        'HLT_HIPuAK4CaloJet80_35_Eta1p1_v1',
        'HLT_HIPuAK4CaloJet80_45_45_Eta2p1_v1',
        'HLT_HIRandom_v1',
        'HLT_HIUPC_DoubleEG2_BptxAND_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleEG2_BptxAND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleEG2_NotMBHF2AND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleEG2_NotMBHF2AND_SinglePixelTrack_v1',
        'HLT_HIUPC_DoubleEG2_NotMBHF2AND_v1',
        'HLT_HIUPC_DoubleEG2_NotMBHF2OR_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleEG2_NotMBHF2OR_SinglePixelTrack_v1',
        'HLT_HIUPC_DoubleEG2_NotMBHF2OR_v1',
        'HLT_HIUPC_DoubleEG5_BptxAND_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleEG5_BptxAND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleEG5_NotMBHF2AND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleEG5_NotMBHF2AND_SinglePixelTrack_v1',
        'HLT_HIUPC_DoubleEG5_NotMBHF2AND_v1',
        'HLT_HIUPC_DoubleEG5_NotMBHF2OR_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleEG5_NotMBHF2OR_SinglePixelTrack_v1',
        'HLT_HIUPC_DoubleEG5_NotMBHF2OR_v1',
        'HLT_HIUPC_DoubleMu0_BptxAND_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleMu0_NotMBHF2AND_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleMu0_NotMBHF2AND_v1',
        'HLT_HIUPC_DoubleMu0_NotMBHF2OR_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleMu0_NotMBHF2OR_v1',
        'HLT_HIUPC_DoubleMuOpen_BptxAND_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleMuOpen_NotMBHF2OR_MaxPixelTrack_v1',
        'HLT_HIUPC_DoubleMuOpen_NotMBHF2OR_v1',
        'HLT_HIUPC_ETT5_Asym50_NotMBHF2OR_SinglePixelTrack_v1',
        'HLT_HIUPC_ETT5_Asym50_NotMBHF2OR_v1',
        'HLT_HIUPC_Mu8_Mu13_MaxPixelTrack_v1',
        'HLT_HIUPC_Mu8_Mu13_v1',
        'HLT_HIUPC_NotMBHF2AND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_NotMBHF2AND_SinglePixelTrack_v1',
        'HLT_HIUPC_NotMBHF2AND_v1',
        'HLT_HIUPC_NotMBHF2OR_BptxAND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_NotMBHF2OR_BptxAND_SinglePixelTrack_v1',
        'HLT_HIUPC_SingleEG3_BptxAND_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleEG3_BptxAND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleEG3_NotMBHF2AND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleEG3_NotMBHF2AND_SinglePixelTrack_v1',
        'HLT_HIUPC_SingleEG3_NotMBHF2AND_v1',
        'HLT_HIUPC_SingleEG3_NotMBHF2OR_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleEG3_NotMBHF2OR_SinglePixelTrack_v1',
        'HLT_HIUPC_SingleEG3_NotMBHF2OR_v1',
        'HLT_HIUPC_SingleEG5_BptxAND_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleEG5_BptxAND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleEG5_NotMBHF2AND_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleEG5_NotMBHF2AND_SinglePixelTrack_v1',
        'HLT_HIUPC_SingleEG5_NotMBHF2AND_v1',
        'HLT_HIUPC_SingleEG5_NotMBHF2OR_SinglePixelTrack_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleEG5_NotMBHF2OR_SinglePixelTrack_v1',
        'HLT_HIUPC_SingleEG5_NotMBHF2OR_v1',
        'HLT_HIUPC_SingleMu0_BptxAND_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleMu0_NotMBHF2AND_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleMu0_NotMBHF2AND_v1',
        'HLT_HIUPC_SingleMu0_NotMBHF2OR_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleMu0_NotMBHF2OR_v1',
        'HLT_HIUPC_SingleMu3_BptxAND_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleMu3_NotMBHF2OR_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleMu3_NotMBHF2OR_v1',
        'HLT_HIUPC_SingleMuOpen_BptxAND_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleMuOpen_NotMBHF2AND_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleMuOpen_NotMBHF2AND_v1',
        'HLT_HIUPC_SingleMuOpen_NotMBHF2OR_MaxPixelTrack_v1',
        'HLT_HIUPC_SingleMuOpen_NotMBHF2OR_v1',
        'HLT_HIUPC_ZeroBias_MaxPixelCluster_v1',
        'HLT_HIUPC_ZeroBias_SinglePixelTrack_v1',
        'HLT_HIZeroBias_FirstCollisionAfterAbortGap_v1',
        'HLT_HIZeroBias_v1',
        'HLT_HI_CastorMuon_v1',
        'HLT_HMinimumBias_part12_v1',
        'HLT_HMinimumBias_part18_v1',
        'HLT_HcalCalibration_v5',
        'HLT_Mu8_Mu13_MaxPixelTrack_v1',
        'HLT_Mu8_Mu13_v1',
        'HLT_ZDCAND_MBHF1AND_BptxAND_v1',
        'HLT_ZDCAND_MBHF1OR_BptxAND_v1',
        'HLT_ZDCAND_MBHF2AND_BptxAND_v1',
        'HLT_ZDCAND_MBHF2OR_BptxAND_v1',
        'HLT_ZDCM_BptxAND_v1',
        'HLT_ZDCM_ZDCP_BptxAND_v1',
        'HLT_ZDCM_ZDCP_MBHF1AND_BptxAND_v1',
        'HLT_ZDCM_v1',
        'HLT_ZDCOR_MBHF1OR_BptxAND_v1',
        'HLT_ZDCOR_MBHF2OR_BptxAND_v1',
        'HLT_ZDCP_BptxAND_v1',
        'HLT_ZDCP_v1'
     ) ),
    hltresults = cms.InputTag("TriggerResults","","HLT"),
    l1dummybranches = cms.vstring( (
        'L1_AlwaysTrue',
        'L1_BPTX_AND_Ref1_VME',
        'L1_BPTX_AND_Ref3_VME',
        'L1_BPTX_AND_Ref4_VME',
        'L1_BPTX_BeamGas_B1_VME',
        'L1_BPTX_BeamGas_B2_VME',
        'L1_BPTX_BeamGas_Ref1_VME',
        'L1_BPTX_BeamGas_Ref2_VME',
        'L1_BPTX_NotOR_VME',
        'L1_BPTX_OR_Ref3_VME',
        'L1_BPTX_OR_Ref4_VME',
        'L1_BPTX_RefAND_VME',
        'L1_BptxMinus',
        'L1_BptxMinus_NotBptxPlus',
        'L1_BptxOR',
        'L1_BptxPlus',
        'L1_BptxPlus_NotBptxMinus',
        'L1_BptxXOR',
        'L1_Castor1',
        'L1_CastorHighJet',
        'L1_CastorHighJet_BptxAND',
        'L1_CastorHighJet_MinimumBiasHF1_OR_BptxAND',
        'L1_CastorHighJet_NotMinimumBiasHF2_AND_BptxAND',
        'L1_CastorHighJet_NotMinimumBiasHF2_OR_BptxAND',
        'L1_CastorHighJet_OR_MinimumBiasHF1_AND_BptxAND',
        'L1_CastorHighJet_OR_MinimumBiasHF2_AND_BptxAND',
        'L1_CastorMediumJet',
        'L1_CastorMediumJet_BptxAND',
        'L1_CastorMediumJet_MinimumBiasHF1_OR_BptxAND',
        'L1_CastorMediumJet_NotMinimumBiasHF2_AND_BptxAND',
        'L1_CastorMediumJet_NotMinimumBiasHF2_OR_BptxAND',
        'L1_CastorMediumJet_SingleEG5_MinimumBiasHF1_OR_BptxAND',
        'L1_CastorMediumJet_SingleMu0_MinimumBiasHF1_OR_BptxAND',
        'L1_CastorMuon',
        'L1_CastorMuon_BptxAND',
        'L1_Centrality_20_100_MinimumBiasHF1_AND_BptxAND',
        'L1_Centrality_30_100',
        'L1_Centrality_30_100_MinimumBiasHF1_AND_BptxAND',
        'L1_Centrality_50_100',
        'L1_Centrality_Saturation',
        'L1_DoubleEG10_BptxAND',
        'L1_DoubleEG2',
        'L1_DoubleEG2_BptxAND',
        'L1_DoubleEG2_NotMinimumBiasHF2_AND_BptxAND',
        'L1_DoubleEG2_NotMinimumBiasHF2_OR_BptxAND',
        'L1_DoubleEG5',
        'L1_DoubleEG5_BptxAND',
        'L1_DoubleEG5_NotMinimumBiasHF2_AND_BptxAND',
        'L1_DoubleEG5_NotMinimumBiasHF2_OR_BptxAND',
        'L1_DoubleEG8_BptxAND',
        'L1_DoubleJet16And12_MidEta2p7_BptxAND',
        'L1_DoubleJet16And12_MidEta2p7_Centrality_30_100_BptxAND',
        'L1_DoubleJet16And12_MidEta2p7_Centrality_50_100_BptxAND',
        'L1_DoubleJet16And8_MidEta2p7_BptxAND',
        'L1_DoubleJet16And8_MidEta2p7_Centrality_30_100_BptxAND',
        'L1_DoubleJet16And8_MidEta2p7_Centrality_50_100_BptxAND',
        'L1_DoubleJet20And12_MidEta2p7_BptxAND',
        'L1_DoubleJet20And12_MidEta2p7_Centrality_30_100_BptxAND',
        'L1_DoubleJet20And12_MidEta2p7_Centrality_50_100_BptxAND',
        'L1_DoubleJet20And8_MidEta2p7_BptxAND',
        'L1_DoubleJet20And8_MidEta2p7_Centrality_30_100_BptxAND',
        'L1_DoubleJet20And8_MidEta2p7_Centrality_50_100_BptxAND',
        'L1_DoubleJet28And16_MidEta2p7_BptxAND',
        'L1_DoubleJet28And16_MidEta2p7_Centrality_30_100_BptxAND',
        'L1_DoubleJet28And16_MidEta2p7_Centrality_50_100_BptxAND',
        'L1_DoubleMu0',
        'L1_DoubleMu0_BptxAND',
        'L1_DoubleMu0_Centrality_10_100_MinimumBiasHF1_AND_BptxAND',
        'L1_DoubleMu0_Centrality_30_100_MinimumBiasHF1_AND_BptxAND',
        'L1_DoubleMu0_Centrality_50_100_MinimumBiasHF1_AND_BptxAND',
        'L1_DoubleMu0_Mass_Min1',
        'L1_DoubleMu0_MinimumBiasHF1_AND_BptxAND',
        'L1_DoubleMu0_NotMinimumBiasHF2_AND_BptxAND',
        'L1_DoubleMu0_NotMinimumBiasHF2_OR_BptxAND',
        'L1_DoubleMu0_SQ',
        'L1_DoubleMu0_SQ_OS',
        'L1_DoubleMu10_BptxAND',
        'L1_DoubleMuOpen',
        'L1_DoubleMuOpen_BptxAND',
        'L1_DoubleMuOpen_Centrality_10_100_BptxAND',
        'L1_DoubleMuOpen_Centrality_30_100_BptxAND',
        'L1_DoubleMuOpen_Centrality_40_100_BptxAND',
        'L1_DoubleMuOpen_Centrality_50_100_BptxAND',
        'L1_DoubleMuOpen_MaxDr2p0_BptxAND',
        'L1_DoubleMuOpen_MaxDr2p0_OS_BptxAND',
        'L1_DoubleMuOpen_MaxDr3p5',
        'L1_DoubleMuOpen_MaxDr3p5_BptxAND',
        'L1_DoubleMuOpen_NotMinimumBiasHF2_AND_BptxAND',
        'L1_DoubleMuOpen_NotMinimumBiasHF2_OR_BptxAND',
        'L1_DoubleMuOpen_OS',
        'L1_DoubleMuOpen_OS_BptxAND',
        'L1_DoubleMuOpen_SS',
        'L1_DoubleMuOpen_SS_BptxAND',
        'L1_ETMHF100',
        'L1_ETMHF100_HTT60er',
        'L1_ETMHF120',
        'L1_ETMHF120_HTT60er',
        'L1_ETT10_ETTAsym50_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT10_ETTAsym55_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT10_ETTAsym60_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT10_ETTAsym65_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT10_ETTAsym70_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT10_ETTAsym80_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT1200',
        'L1_ETT1600',
        'L1_ETT2000',
        'L1_ETT35_NotETT80_BptxAND',
        'L1_ETT40_NotETT95_BptxAND',
        'L1_ETT45_NotETT110_BptxAND',
        'L1_ETT5',
        'L1_ETT50_ETTAsym40_MinimumBiasHF2_OR_BptxAND',
        'L1_ETT50_ETTAsym40_NotMinimumBiasHF2_OR_BptxAND',
        'L1_ETT50_ETTAsym50_MinimumBiasHF2_OR_BptxAND',
        'L1_ETT50_ETTAsym50_NotMinimumBiasHF2_OR_BptxAND',
        'L1_ETT50_ETTAsym55_MinimumBiasHF2_OR_BptxAND',
        'L1_ETT50_ETTAsym60_MinimumBiasHF2_OR_BptxAND',
        'L1_ETT50_ETTAsym60_NotMinimumBiasHF2_OR_BptxAND',
        'L1_ETT50_ETTAsym65_MinimumBiasHF2_OR_BptxAND',
        'L1_ETT50_ETTAsym70_MinimumBiasHF2_OR_BptxAND',
        'L1_ETT50_ETTAsym70_NotMinimumBiasHF2_OR_BptxAND',
        'L1_ETT50_ETTAsym80_MinimumBiasHF2_OR_BptxAND',
        'L1_ETT50_ETTAsym80_NotMinimumBiasHF2_OR_BptxAND',
        'L1_ETT50_NotETT120_BptxAND',
        'L1_ETT55_NotETT130_BptxAND',
        'L1_ETT5_BptxAND',
        'L1_ETT5_ETTAsym40_BptxAND',
        'L1_ETT5_ETTAsym40_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT5_ETTAsym40_NotMinimumBiasHF2_OR_BptxAND',
        'L1_ETT5_ETTAsym50_BptxAND',
        'L1_ETT5_ETTAsym50_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT5_ETTAsym50_NotMinimumBiasHF2_OR_BptxAND',
        'L1_ETT5_ETTAsym55_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT5_ETTAsym60_BptxAND',
        'L1_ETT5_ETTAsym60_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT5_ETTAsym60_NotMinimumBiasHF2_OR_BptxAND',
        'L1_ETT5_ETTAsym65_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT5_ETTAsym70_BptxAND',
        'L1_ETT5_ETTAsym70_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT5_ETTAsym70_NotMinimumBiasHF2_OR_BptxAND',
        'L1_ETT5_ETTAsym80_BptxAND',
        'L1_ETT5_ETTAsym80_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT5_ETTAsym80_NotMinimumBiasHF2_OR_BptxAND',
        'L1_ETT5_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT5_NotETT30_BptxAND',
        'L1_ETT5_NotMinimumBiasHF2_OR',
        'L1_ETT60_ETTAsym60_MinimumBiasHF2_OR_BptxAND',
        'L1_ETT60_ETTAsym65_MinimumBiasHF2_OR_BptxAND',
        'L1_ETT65_ETTAsym70_MinimumBiasHF2_OR_BptxAND',
        'L1_ETT65_ETTAsym80_MinimumBiasHF2_OR_BptxAND',
        'L1_ETT8_ETTAsym50_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT8_ETTAsym55_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT8_ETTAsym60_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT8_ETTAsym65_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT8_ETTAsym70_MinimumBiasHF1_OR_BptxAND',
        'L1_ETT8_ETTAsym80_MinimumBiasHF1_OR_BptxAND',
        'L1_ETTAsym40',
        'L1_ETTAsym40_BptxAND',
        'L1_ETTAsym40_MinimumBiasHF1_OR_BptxAND',
        'L1_ETTAsym40_NotMinimumBiasHF2_OR_BptxAND',
        'L1_ETTAsym50',
        'L1_ETTAsym50_BptxAND',
        'L1_ETTAsym50_MinimumBiasHF1_OR_BptxAND',
        'L1_ETTAsym50_NotMinimumBiasHF2_OR_BptxAND',
        'L1_ETTAsym60',
        'L1_ETTAsym60_BptxAND',
        'L1_ETTAsym60_MinimumBiasHF1_OR_BptxAND',
        'L1_ETTAsym60_NotMinimumBiasHF2_OR_BptxAND',
        'L1_ETTAsym70',
        'L1_ETTAsym70_BptxAND',
        'L1_ETTAsym70_MinimumBiasHF1_OR_BptxAND',
        'L1_ETTAsym70_NotMinimumBiasHF2_OR_BptxAND',
        'L1_ETTAsym80',
        'L1_ETTAsym80_BptxAND',
        'L1_ETTAsym80_MinimumBiasHF1_OR_BptxAND',
        'L1_ETTAsym80_NotMinimumBiasHF2_OR_BptxAND',
        'L1_FirstBunchAfterTrain',
        'L1_FirstBunchBeforeTrain',
        'L1_FirstBunchInTrain',
        'L1_FirstCollisionInOrbit',
        'L1_FirstCollisionInOrbit_Centrality30_100_BptxAND',
        'L1_FirstCollisionInTrain',
        'L1_HCAL_LaserMon_Trig',
        'L1_HCAL_LaserMon_Veto',
        'L1_HTT120er',
        'L1_HTT200er',
        'L1_HTT280er',
        'L1_HTT360er',
        'L1_HTT450er',
        'L1_IsolatedBunch',
        'L1_LastBunchInTrain',
        'L1_LastCollisionInTrain',
        'L1_MinimumBiasHF0_AND_BptxAND',
        'L1_MinimumBiasHF0_OR_BptxAND',
        'L1_MinimumBiasHF1_AND',
        'L1_MinimumBiasHF1_AND_BptxAND',
        'L1_MinimumBiasHF1_AND_OR_ETT10_BptxAND',
        'L1_MinimumBiasHF1_OR',
        'L1_MinimumBiasHF1_OR_BptxAND',
        'L1_MinimumBiasHF1_XOR_BptxAND',
        'L1_MinimumBiasHF2_AND',
        'L1_MinimumBiasHF2_AND_BptxAND',
        'L1_MinimumBiasHF2_OR',
        'L1_MinimumBiasHF2_OR_BptxAND',
        'L1_NotBptxOR',
        'L1_NotETT100_MinimumBiasHF1_AND_BptxAND',
        'L1_NotETT110_MinimumBiasHF1_OR_BptxAND',
        'L1_NotETT110_MinimumBiasHF2_OR_BptxAND',
        'L1_NotETT150_MinimumBiasHF1_AND_BptxAND',
        'L1_NotETT150_MinimumBiasHF1_OR_BptxAND',
        'L1_NotETT150_MinimumBiasHF2_OR_BptxAND',
        'L1_NotETT200_MinimumBiasHF1_AND_BptxAND',
        'L1_NotETT20_MinimumBiasHF1_AND_BptxAND',
        'L1_NotETT20_MinimumBiasHF1_OR_BptxAND',
        'L1_NotETT20_MinimumBiasHF2_OR_BptxAND',
        'L1_NotETT80_MinimumBiasHF1_AND_BptxAND',
        'L1_NotETT80_MinimumBiasHF1_OR_BptxAND',
        'L1_NotETT80_MinimumBiasHF2_OR_BptxAND',
        'L1_NotETT95_MinimumBiasHF1_AND_BptxAND',
        'L1_NotETT95_MinimumBiasHF1_OR_BptxAND',
        'L1_NotETT95_MinimumBiasHF2_OR_BptxAND',
        'L1_NotMinimumBiasHF0_AND_BptxAND',
        'L1_NotMinimumBiasHF0_AND_BptxAND_TOTEM_1',
        'L1_NotMinimumBiasHF0_AND_BptxAND_TOTEM_2',
        'L1_NotMinimumBiasHF0_AND_BptxAND_TOTEM_4',
        'L1_NotMinimumBiasHF0_OR_BptxAND',
        'L1_NotMinimumBiasHF0_OR_BptxAND_TOTEM_1',
        'L1_NotMinimumBiasHF0_OR_BptxAND_TOTEM_2',
        'L1_NotMinimumBiasHF0_OR_BptxAND_TOTEM_4',
        'L1_NotMinimumBiasHF1_AND',
        'L1_NotMinimumBiasHF1_OR',
        'L1_NotMinimumBiasHF1_OR_BptxAND',
        'L1_NotMinimumBiasHF2_AND',
        'L1_NotMinimumBiasHF2_AND_BptxAND',
        'L1_NotMinimumBiasHF2_OR',
        'L1_NotMinimumBiasHF2_OR_BptxAND',
        'L1_SecondBunchInTrain',
        'L1_SecondLastBunchInTrain',
        'L1_SingleEG10er2p5',
        'L1_SingleEG12_BptxAND',
        'L1_SingleEG12_SingleJet28_MidEta2p7_BptxAND',
        'L1_SingleEG12_SingleJet28_MidEta2p7_MinDr0p4_BptxAND',
        'L1_SingleEG12_SingleJet32_MidEta2p7_BptxAND',
        'L1_SingleEG12_SingleJet40_MidEta2p7_BptxAND',
        'L1_SingleEG12_SingleJet44_MidEta2p7_BptxAND',
        'L1_SingleEG12_SingleJet44_MidEta2p7_MinDr0p4_BptxAND',
        'L1_SingleEG12_SingleJet56_MidEta2p7_BptxAND',
        'L1_SingleEG12_SingleJet56_MidEta2p7_MinDr0p4_BptxAND',
        'L1_SingleEG12_SingleJet60_MidEta2p7_BptxAND',
        'L1_SingleEG12_SingleJet60_MidEta2p7_MinDr0p4_BptxAND',
        'L1_SingleEG15_BptxAND',
        'L1_SingleEG15_Centrality_30_100_BptxAND',
        'L1_SingleEG15_Centrality_50_100_BptxAND',
        'L1_SingleEG15_SingleJet28_MidEta2p7_BptxAND',
        'L1_SingleEG15_SingleJet28_MidEta2p7_MinDr0p4_BptxAND',
        'L1_SingleEG15_SingleJet44_MidEta2p7_BptxAND',
        'L1_SingleEG15_SingleJet44_MidEta2p7_MinDr0p4_BptxAND',
        'L1_SingleEG15_SingleJet56_MidEta2p7_BptxAND',
        'L1_SingleEG15_SingleJet56_MidEta2p7_MinDr0p4_BptxAND',
        'L1_SingleEG15_SingleJet60_MidEta2p7_BptxAND',
        'L1_SingleEG15_SingleJet60_MidEta2p7_MinDr0p4_BptxAND',
        'L1_SingleEG15er2p5',
        'L1_SingleEG21_BptxAND',
        'L1_SingleEG21_Centrality_30_100_BptxAND',
        'L1_SingleEG21_Centrality_50_100_BptxAND',
        'L1_SingleEG26er2p5',
        'L1_SingleEG3',
        'L1_SingleEG30_BptxAND',
        'L1_SingleEG3_BptxAND',
        'L1_SingleEG3_Centrality_30_100_BptxAND',
        'L1_SingleEG3_Centrality_50_100_BptxAND',
        'L1_SingleEG3_NotMinimumBiasHF2_AND_BptxAND',
        'L1_SingleEG3_NotMinimumBiasHF2_OR_BptxAND',
        'L1_SingleEG5',
        'L1_SingleEG50',
        'L1_SingleEG5_BptxAND',
        'L1_SingleEG5_NotMinimumBiasHF2_AND_BptxAND',
        'L1_SingleEG5_NotMinimumBiasHF2_OR_BptxAND',
        'L1_SingleEG5_SingleJet28_MidEta2p7_BptxAND',
        'L1_SingleEG5_SingleJet32_MidEta2p7_BptxAND',
        'L1_SingleEG5_SingleJet40_MidEta2p7_BptxAND',
        'L1_SingleEG7_BptxAND',
        'L1_SingleEG7_Centrality_30_100_BptxAND',
        'L1_SingleEG7_Centrality_50_100_BptxAND',
        'L1_SingleEG7_SingleJet28_MidEta2p7_BptxAND',
        'L1_SingleEG7_SingleJet28_MidEta2p7_MinDr0p4_BptxAND',
        'L1_SingleEG7_SingleJet32_MidEta2p7_BptxAND',
        'L1_SingleEG7_SingleJet40_MidEta2p7_BptxAND',
        'L1_SingleEG7_SingleJet44_MidEta2p7_BptxAND',
        'L1_SingleEG7_SingleJet44_MidEta2p7_MinDr0p4_BptxAND',
        'L1_SingleEG7_SingleJet56_MidEta2p7_BptxAND',
        'L1_SingleEG7_SingleJet56_MidEta2p7_MinDr0p4_BptxAND',
        'L1_SingleEG7_SingleJet60_MidEta2p7_BptxAND',
        'L1_SingleEG7_SingleJet60_MidEta2p7_MinDr0p4_BptxAND',
        'L1_SingleEG8er2p5',
        'L1_SingleIsoEG12_BptxAND',
        'L1_SingleIsoEG15_BptxAND',
        'L1_SingleIsoEG21_BptxAND',
        'L1_SingleIsoEG3_BptxAND',
        'L1_SingleIsoEG7_BptxAND',
        'L1_SingleJet120',
        'L1_SingleJet120_FWD3p0',
        'L1_SingleJet120er2p5',
        'L1_SingleJet16_BptxAND',
        'L1_SingleJet16_Centrality_30_100_BptxAND',
        'L1_SingleJet16_Centrality_50_100_BptxAND',
        'L1_SingleJet16_FWD_BptxAND',
        'L1_SingleJet16_FWD_Centrality_30_100_BptxAND',
        'L1_SingleJet16_FWD_Centrality_50_100_BptxAND',
        'L1_SingleJet180er2p5',
        'L1_SingleJet200',
        'L1_SingleJet24_BptxAND',
        'L1_SingleJet24_Centrality_30_100_BptxAND',
        'L1_SingleJet24_Centrality_50_100_BptxAND',
        'L1_SingleJet28_BptxAND',
        'L1_SingleJet28_Centrality_30_100_BptxAND',
        'L1_SingleJet28_Centrality_50_100_BptxAND',
        'L1_SingleJet28_FWD_BptxAND',
        'L1_SingleJet28_FWD_Centrality_30_100_BptxAND',
        'L1_SingleJet28_FWD_Centrality_50_100_BptxAND',
        'L1_SingleJet32_BptxAND',
        'L1_SingleJet32_Centrality_30_100_BptxAND',
        'L1_SingleJet32_Centrality_50_100_BptxAND',
        'L1_SingleJet35',
        'L1_SingleJet35_FWD3p0',
        'L1_SingleJet35er2p5',
        'L1_SingleJet36_BptxAND',
        'L1_SingleJet36_Centrality_30_100_BptxAND',
        'L1_SingleJet36_Centrality_50_100_BptxAND',
        'L1_SingleJet36_FWD_BptxAND',
        'L1_SingleJet36_FWD_Centrality_30_100_BptxAND',
        'L1_SingleJet36_FWD_Centrality_50_100_BptxAND',
        'L1_SingleJet40_BptxAND',
        'L1_SingleJet40_Centrality_30_100_BptxAND',
        'L1_SingleJet40_Centrality_50_100_BptxAND',
        'L1_SingleJet44_BptxAND',
        'L1_SingleJet44_Centrality_30_100_BptxAND',
        'L1_SingleJet44_Centrality_50_100_BptxAND',
        'L1_SingleJet44_FWD_BptxAND',
        'L1_SingleJet44_FWD_Centrality_30_100_BptxAND',
        'L1_SingleJet44_FWD_Centrality_50_100_BptxAND',
        'L1_SingleJet48_BptxAND',
        'L1_SingleJet48_Centrality_30_100_BptxAND',
        'L1_SingleJet48_Centrality_50_100_BptxAND',
        'L1_SingleJet56_BptxAND',
        'L1_SingleJet56_Centrality_30_100_BptxAND',
        'L1_SingleJet56_Centrality_50_100_BptxAND',
        'L1_SingleJet56_FWD_BptxAND',
        'L1_SingleJet56_FWD_Centrality_30_100_BptxAND',
        'L1_SingleJet56_FWD_Centrality_50_100_BptxAND',
        'L1_SingleJet60',
        'L1_SingleJet60_BptxAND',
        'L1_SingleJet60_Centrality_30_100_BptxAND',
        'L1_SingleJet60_Centrality_50_100_BptxAND',
        'L1_SingleJet60_FWD3p0',
        'L1_SingleJet60er2p5',
        'L1_SingleJet64_BptxAND',
        'L1_SingleJet64_Centrality_30_100_BptxAND',
        'L1_SingleJet64_Centrality_50_100_BptxAND',
        'L1_SingleJet64_FWD_BptxAND',
        'L1_SingleJet64_FWD_Centrality_30_100_BptxAND',
        'L1_SingleJet64_FWD_Centrality_50_100_BptxAND',
        'L1_SingleJet72_BptxAND',
        'L1_SingleJet8',
        'L1_SingleJet80_BptxAND',
        'L1_SingleJet8_BptxAND',
        'L1_SingleJet8_Centrality_30_100_BptxAND',
        'L1_SingleJet8_Centrality_50_100_BptxAND',
        'L1_SingleJet8_FWD_BptxAND',
        'L1_SingleJet8_FWD_Centrality_30_100_BptxAND',
        'L1_SingleJet8_FWD_Centrality_50_100_BptxAND',
        'L1_SingleJet90',
        'L1_SingleJet90_FWD3p0',
        'L1_SingleJet90er2p5',
        'L1_SingleMu0',
        'L1_SingleMu0_BMTF',
        'L1_SingleMu0_BptxAND',
        'L1_SingleMu0_DQ',
        'L1_SingleMu0_EMTF',
        'L1_SingleMu0_NotMinimumBiasHF2_AND_BptxAND',
        'L1_SingleMu0_NotMinimumBiasHF2_OR_BptxAND',
        'L1_SingleMu0_OMTF',
        'L1_SingleMu12',
        'L1_SingleMu12_BptxAND',
        'L1_SingleMu12_DQ_BMTF',
        'L1_SingleMu12_DQ_EMTF',
        'L1_SingleMu12_DQ_OMTF',
        'L1_SingleMu12_MinimumBiasHF1_AND_BptxAND',
        'L1_SingleMu12_SingleEG7_BptxAND',
        'L1_SingleMu16',
        'L1_SingleMu16_BptxAND',
        'L1_SingleMu16_MinimumBiasHF1_AND_BptxAND',
        'L1_SingleMu22',
        'L1_SingleMu22_BMTF',
        'L1_SingleMu22_EMTF',
        'L1_SingleMu22_OMTF',
        'L1_SingleMu3',
        'L1_SingleMu3Open_BptxAND',
        'L1_SingleMu3_BptxAND',
        'L1_SingleMu3_Centrality_70_100_BptxAND',
        'L1_SingleMu3_Centrality_80_100_BptxAND',
        'L1_SingleMu3_MinimumBiasHF1_AND_BptxAND',
        'L1_SingleMu3_NotMinimumBiasHF2_OR_BptxAND',
        'L1_SingleMu3_SingleEG12_BptxAND',
        'L1_SingleMu3_SingleEG15_BptxAND',
        'L1_SingleMu3_SingleEG20_BptxAND',
        'L1_SingleMu3_SingleEG30_BptxAND',
        'L1_SingleMu3_SingleJet28_MidEta2p7_BptxAND',
        'L1_SingleMu3_SingleJet32_MidEta2p7_BptxAND',
        'L1_SingleMu3_SingleJet40_MidEta2p7_BptxAND',
        'L1_SingleMu5',
        'L1_SingleMu5_BptxAND',
        'L1_SingleMu5_MinimumBiasHF1_AND_BptxAND',
        'L1_SingleMu5_SingleEG10_BptxAND',
        'L1_SingleMu5_SingleEG12_BptxAND',
        'L1_SingleMu5_SingleEG15_BptxAND',
        'L1_SingleMu5_SingleEG20_BptxAND',
        'L1_SingleMu7',
        'L1_SingleMu7_BptxAND',
        'L1_SingleMu7_DQ',
        'L1_SingleMu7_MinimumBiasHF1_AND_BptxAND',
        'L1_SingleMu7_SingleEG10_BptxAND',
        'L1_SingleMu7_SingleEG12_BptxAND',
        'L1_SingleMu7_SingleEG15_BptxAND',
        'L1_SingleMu7_SingleEG7_BptxAND',
        'L1_SingleMuCosmics',
        'L1_SingleMuCosmics_BMTF',
        'L1_SingleMuCosmics_EMTF',
        'L1_SingleMuCosmics_OMTF',
        'L1_SingleMuOpen',
        'L1_SingleMuOpen_BptxAND',
        'L1_SingleMuOpen_Centrality_70_100_BptxAND',
        'L1_SingleMuOpen_Centrality_70_100_MinimumBiasHF1_AND_BptxAND',
        'L1_SingleMuOpen_Centrality_80_100_BptxAND',
        'L1_SingleMuOpen_Centrality_80_100_MinimumBiasHF1_AND_BptxAND',
        'L1_SingleMuOpen_NotMinimumBiasHF2_AND_BptxAND',
        'L1_SingleMuOpen_NotMinimumBiasHF2_OR_BptxAND',
        'L1_SingleMuOpen_SingleEG15_BptxAND',
        'L1_SingleMuOpen_SingleJet28_MidEta2p7_BptxAND',
        'L1_SingleMuOpen_SingleJet44_MidEta2p7_BptxAND',
        'L1_SingleMuOpen_SingleJet56_MidEta2p7_BptxAND',
        'L1_SingleMuOpen_SingleJet64_MidEta2p7_BptxAND',
        'L1_TOTEM_1',
        'L1_TOTEM_2',
        'L1_TOTEM_3',
        'L1_TOTEM_4',
        'L1_UnpairedBunchBptxMinus',
        'L1_UnpairedBunchBptxPlus',
        'L1_ZDCM',
        'L1_ZDCM_BptxAND',
        'L1_ZDCM_ZDCP_BptxAND',
        'L1_ZDCP',
        'L1_ZDCP_BptxAND',
        'L1_ZDC_AND_OR_MinimumBiasHF1_AND_BptxAND',
        'L1_ZDC_AND_OR_MinimumBiasHF1_OR_BptxAND',
        'L1_ZDC_AND_OR_MinimumBiasHF2_AND_BptxAND',
        'L1_ZDC_AND_OR_MinimumBiasHF2_OR_BptxAND',
        'L1_ZDC_OR_OR_MinimumBiasHF1_OR_BptxAND',
        'L1_ZDC_OR_OR_MinimumBiasHF2_OR_BptxAND',
        'L1_ZeroBias',
        'L1_ZeroBias_copy'
     ) ),
    l1results = cms.InputTag("gtStage2Digis")
)


process.hltobject = cms.EDAnalyzer("TriggerObjectAnalyzer",
    processName = cms.string('HLT'),
    treeName = cms.string('JetTriggers'),
    triggerNames = cms.vstring(
        'HLT_HIL1DoubleMuOpen_v',
        'HLT_HIL1DoubleMuOpen_OS_Centrality_40_100_v',
        'HLT_HIL1DoubleMuOpen_Centrality_50_100_v',
        'HLT_HIL1DoubleMu10_v',
        'HLT_HIL2_L1DoubleMu10_v',
        'HLT_HIL3_L1DoubleMu10_v',
        'HLT_HIL2DoubleMuOpen_v',
        'HLT_HIL3DoubleMuOpen_v',
        'HLT_HIL3DoubleMuOpen_M60120_v',
        'HLT_HIL3DoubleMuOpen_JpsiPsi_v',
        'HLT_HIL3DoubleMuOpen_Upsi_v',
        'HLT_HIL3Mu0_L2Mu0_v',
        'HLT_HIL3Mu0NHitQ10_L2Mu0_MAXdR3p5_M1to5_v',
        'HLT_HIL3Mu2p5NHitQ10_L2Mu2_M7toinf_v',
        'HLT_HIL3Mu3_L1TripleMuOpen_v',
        'HLT_HIL1MuOpen_Centrality_70_100_v',
        'HLT_HIL1MuOpen_Centrality_80_100_v',
        'HLT_HIL2Mu3_NHitQ15_v',
        'HLT_HIL2Mu5_NHitQ15_v',
        'HLT_HIL2Mu7_NHitQ15_v',
        'HLT_HIL3Mu12_v',
        'HLT_HIL3Mu15_v',
        'HLT_HIL3Mu20_v',
        'HLT_HIL3Mu3_NHitQ10_v',
        'HLT_HIL3Mu5_NHitQ10_v',
        'HLT_HIL3Mu7_NHitQ10_v',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet40Eta2p1_v',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet60Eta2p1_v',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet80Eta2p1_v',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet100Eta2p1_v',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet40Eta2p1_v',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet60Eta2p1_v',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet80Eta2p1_v',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet100Eta2p1_v',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet40Eta2p1_FilterDr_v',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet60Eta2p1_FilterDr_v',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet80Eta2p1_FilterDr_v',
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet100Eta2p1_FilterDr_v',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet40Eta2p1_FilterDr_v',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet60Eta2p1_FilterDr_v',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet80Eta2p1_FilterDr_v',
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet100Eta2p1_FilterDr_v',
        'HLT_HIPuAK4CaloJet40Eta5p1_v',
        'HLT_HIPuAK4CaloJet60Eta5p1_v',
        'HLT_HIPuAK4CaloJet80Eta5p1_v',
        'HLT_HIPuAK4CaloJet100Eta5p1_v',
        'HLT_HIPuAK4CaloJet120Eta5p1_v',
        'HLT_HIPuAK4CaloJet40Fwd_v',
        'HLT_HIPuAK4CaloJet60Fwd_v',
        'HLT_HIPuAK4CaloJet80Fwd_v',
        'HLT_HIPuAK4CaloJet100Fwd_v',
        'HLT_HIPuAK4CaloJet120Fwd_v',
        'HLT_HIPuAK4CaloJet80_35_Eta1p1_v',
        'HLT_HIPuAK4CaloJet100_35_Eta1p1_v',
        'HLT_HIPuAK4CaloJet80_35_Eta0p7_v',
        'HLT_HIPuAK4CaloJet100_35_Eta0p7_v',
        'HLT_HIPuAK4CaloJet80_45_45_Eta2p1_v',
        'HLT_HIPuAK4CaloJet60Eta2p4_DeepCSV0p4_v',
        'HLT_HIPuAK4CaloJet80Eta2p4_DeepCSV0p4_v',
        'HLT_HIPuAK4CaloJet100Eta2p4_DeepCSV0p4_v',
        'HLT_HIPuAK4CaloJet60Eta2p4_CSVv2WP0p75_v',
        'HLT_HIPuAK4CaloJet80Eta2p4_CSVv2WP0p75_v',
        'HLT_HIPuAK4CaloJet100Eta2p4_CSVv2WP0p75_v',
        'HLT_HICsAK4PFJet60Eta1p5_v',
        'HLT_HICsAK4PFJet80Eta1p5_v',
        'HLT_HICsAK4PFJet100Eta1p5_v',
        'HLT_HICsAK4PFJet120Eta1p5_v',
        'HLT_HIEle10Gsf_v',
        'HLT_HIEle15Gsf_v',
        'HLT_HIEle20Gsf_v',
        'HLT_HIEle30Gsf_v',
        'HLT_HIEle40Gsf_v',
        'HLT_HIEle50Gsf_v',
        'HLT_HIDoubleEle15Gsf_v',
        'HLT_HIDoubleEle15GsfMass50_v',
        'HLT_HIEle15Ele10Gsf_v',
        'HLT_HIEle15Ele10GsfMass50_v',
        'HLT_HIDoubleEle10Gsf_v',
        'HLT_HIDoubleEle10GsfMass50_v',
        'HLT_HIEle10Gsf_PuAK4CaloJet40Eta2p1_v',
        'HLT_HIEle10Gsf_PuAK4CaloJet60Eta2p1_v',
        'HLT_HIEle10Gsf_PuAK4CaloJet80Eta2p1_v',
        'HLT_HIEle10Gsf_PuAK4CaloJet100Eta2p1_v',
        'HLT_HIEle15Gsf_PuAK4CaloJet40Eta2p1_v',
        'HLT_HIEle15Gsf_PuAK4CaloJet60Eta2p1_v',
        'HLT_HIEle15Gsf_PuAK4CaloJet80Eta2p1_v',
        'HLT_HIEle15Gsf_PuAK4CaloJet100Eta2p1_v',
        'HLT_HIEle20Gsf_PuAK4CaloJet40Eta2p1_v',
        'HLT_HIEle20Gsf_PuAK4CaloJet60Eta2p1_v',
        'HLT_HIEle20Gsf_PuAK4CaloJet80Eta2p1_v',
        'HLT_HIEle20Gsf_PuAK4CaloJet100Eta2p1_v',
        'HLT_HIL1Mu5Eta2p5_Ele20Gsf_v',
        'HLT_HIL1Mu7Eta2p5_Ele20Gsf_v',
        'HLT_HIGEDPhoton10_v',
        'HLT_HIGEDPhoton20_v',
        'HLT_HIGEDPhoton30_v',
        'HLT_HIGEDPhoton40_v',
        'HLT_HIGEDPhoton50_v',
        'HLT_HIGEDPhoton60_v',
        'HLT_HIGEDPhoton10_EB_v',
        'HLT_HIGEDPhoton20_EB_v',
        'HLT_HIGEDPhoton30_EB_v',
        'HLT_HIGEDPhoton40_EB_v',
        'HLT_HIGEDPhoton50_EB_v',
        'HLT_HIGEDPhoton60_EB_v',
        'HLT_HIIslandPhoton10_Eta2p4_v',
        'HLT_HIIslandPhoton20_Eta2p4_v',
        'HLT_HIIslandPhoton30_Eta2p4_v',
        'HLT_HIIslandPhoton40_Eta2p4_v',
        'HLT_HIIslandPhoton50_Eta2p4_v',
        'HLT_HIIslandPhoton60_Eta2p4_v',
        'HLT_HIIslandPhoton10_Eta1p5_v',
        'HLT_HIIslandPhoton20_Eta1p5_v',
        'HLT_HIIslandPhoton30_Eta1p5_v',
        'HLT_HIIslandPhoton40_Eta1p5_v',
        'HLT_HIIslandPhoton50_Eta1p5_v',
        'HLT_HIIslandPhoton60_Eta1p5_v',
        'HLT_HIPuAK4CaloJet40Eta5p1_Centrality_30_100_v',
        'HLT_HIPuAK4CaloJet60Eta5p1_Centrality_30_100_v',
        'HLT_HIPuAK4CaloJet80Eta5p1_Centrality_30_100_v',
        'HLT_HIPuAK4CaloJet100Eta5p1_Centrality_30_100_v',
        'HLT_HIPuAK4CaloJet40Eta5p1_Centrality_50_100_v',
        'HLT_HIPuAK4CaloJet60Eta5p1_Centrality_50_100_v',
        'HLT_HIPuAK4CaloJet80Eta5p1_Centrality_50_100_v',
        'HLT_HIPuAK4CaloJet100Eta5p1_Centrality_50_100_v',
        'HLT_HICsAK4PFJet60Eta1p5_Centrality_30_100_v',
        'HLT_HICsAK4PFJet80Eta1p5_Centrality_30_100_v',
        'HLT_HICsAK4PFJet100Eta1p5_Centrality_30_100_v',
        'HLT_HICsAK4PFJet60Eta1p5_Centrality_50_100_v',
        'HLT_HICsAK4PFJet80Eta1p5_Centrality_50_100_v',
        'HLT_HICsAK4PFJet100Eta1p5_Centrality_50_100_v',
        'HLT_HIGEDPhoton10_Cent30_100_v',
        'HLT_HIGEDPhoton20_Cent30_100_v',
        'HLT_HIGEDPhoton30_Cent30_100_v',
        'HLT_HIGEDPhoton40_Cent30_100_v',
        'HLT_HIIslandPhoton10_Eta2p4_Cent30_100_v',
        'HLT_HIIslandPhoton20_Eta2p4_Cent30_100_v',
        'HLT_HIIslandPhoton30_Eta2p4_Cent30_100_v',
        'HLT_HIIslandPhoton40_Eta2p4_Cent30_100_v',
        'HLT_HIGEDPhoton10_Cent50_100_v',
        'HLT_HIGEDPhoton20_Cent50_100_v',
        'HLT_HIGEDPhoton30_Cent50_100_v',
        'HLT_HIGEDPhoton40_Cent50_100_v',
        'HLT_HIIslandPhoton10_Eta2p4_Cent50_100_v',
        'HLT_HIIslandPhoton20_Eta2p4_Cent50_100_v',
        'HLT_HIIslandPhoton30_Eta2p4_Cent50_100_v',
        'HLT_HIIslandPhoton40_Eta2p4_Cent50_100_v',
        'HLT_HIFullTracks_Multiplicity2040_HF1OR_v',
        'HLT_HIFullTracks_Multiplicity4060_v',
        'HLT_HIFullTracks_Multiplicity6080_v',
        'HLT_HIFullTracks_Multiplicity80100_v',
        'HLT_HIDmesonPPTrackingGlobal_Dpt15_v',
        'HLT_HIDmesonPPTrackingGlobal_Dpt20_v',
        'HLT_HIDmesonPPTrackingGlobal_Dpt40_v',
        'HLT_HIDmesonPPTrackingGlobal_Dpt50_v',
        'HLT_HIDmesonPPTrackingGlobal_Dpt60_v',
        'HLT_HIDsPPTrackingGlobal_Dpt20_v',
        'HLT_HIDsPPTrackingGlobal_Dpt40_v',
        'HLT_HIDsPPTrackingGlobal_Dpt50_v',
        'HLT_HIDsPPTrackingGlobal_Dpt60_v',
        'HLT_HILcPPTrackingGlobal_Dpt20_v',
        'HLT_HILcPPTrackingGlobal_Dpt40_v',
        'HLT_HILcPPTrackingGlobal_Dpt50_v',
        'HLT_HILcPPTrackingGlobal_Dpt60_v',
        'HLT_HIFullTracks2018_HighPt18_v',
        'HLT_HIFullTracks2018_HighPt24_v',
        'HLT_HIFullTracks2018_HighPt34_v',
        'HLT_HIFullTracks2018_HighPt45_v',
        'HLT_HIFullTracks2018_HighPt56_v',
        'HLT_HIFullTracks2018_HighPt60_v',
        'HLT_HIUPC_ZeroBias_SinglePixelTrack_v',
        'HLT_HIUPC_SingleEG5_NotMBHF2AND_SinglePixelTrack_v',
        'HLT_HIUPC_SingleMuOpen_NotMBHF2AND_v',
        'HLT_HICastor_MediumJet_NotMBHF2AND_v'
    ),
    triggerObjects = cms.InputTag("slimmedPatTrigger","","PAT"),
    triggerResults = cms.InputTag("TriggerResults","","HLT")
)


process.inclusiveJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetSubstructure",
    doChargedConstOnly = cms.untracked.bool(True),
    doGenSym = cms.untracked.bool(False),
    doGenTaus = cms.untracked.bool(False),
    doHardestSplitMatching = cms.untracked.bool(False),
    doHiJetID = cms.untracked.bool(True),
    doJetConstituents = cms.untracked.bool(False),
    doLifeTimeTagging = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(False),
    doSubjetPurity = cms.untracked.bool(False),
    doTower = cms.untracked.bool(False),
    doWTARecluster = cms.untracked.bool(False),
    dopthatcut = cms.untracked.bool(False),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genjetTag = cms.InputTag("ak4HiGenJets"),
    groom_combine = cms.double(1),
    groom_type = cms.double(0),
    isMC = cms.untracked.bool(False),
    jetPtMin = cms.double(10.0),
    jetTag = cms.InputTag("ak2PFJets"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("akPu4PFpatJets"),
    mydynktcut = cms.double(1),
    mysdcut1 = cms.double(0.2),
    mysdcut2 = cms.double(0.1),
    pfCandSource = cms.InputTag("packedPFCandidates"),
    rParam = cms.double(0.2),
    towersSrc = cms.InputTag("towerMaker"),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiTracks"),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True),
    useRawPt = cms.untracked.bool(False),
    vtxTag = cms.InputTag("hiSelectedVertex")
)


process.l1object = cms.EDAnalyzer("L1UpgradeFlatTreeProducer",
    doEg = cms.bool(True),
    doJet = cms.bool(True),
    doMuon = cms.bool(True),
    doSum = cms.bool(True),
    doTau = cms.bool(True),
    egToken = cms.untracked.InputTag("caloStage2Digis","EGamma"),
    jetToken = cms.untracked.InputTag("caloStage2Digis","Jet"),
    maxL1Upgrade = cms.uint32(60),
    muonToken = cms.untracked.InputTag("gmtStage2Digis","Muon"),
    sumToken = cms.untracked.InputTag("caloStage2Digis","EtSum"),
    tauTokens = cms.untracked.VInputTag(cms.InputTag("caloStage2Digis","Tau"))
)


process.particleFlowAnalyser = cms.EDAnalyzer("ParticleFlowAnalyser",
    absEtaMax = cms.double(5.0),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    ptMin = cms.double(5.0)
)


process.patCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
    candidates = cms.VInputTag(
        cms.InputTag("patElectrons"), cms.InputTag("patMuons"), cms.InputTag("patTaus"), cms.InputTag("patPhotons"), cms.InputTag("patJets"),
        cms.InputTag("patMETs")
    ),
    logName = cms.untracked.string('patCandidates|PATSummaryTables')
)


process.ppTracks = cms.EDAnalyzer("TrackAnalyzer",
    beamSpotSrc = cms.untracked.InputTag("offlineBeamSpot"),
    chi2Map = cms.InputTag("packedPFCandidateTrackChi2"),
    chi2MapLost = cms.InputTag("lostTrackChi2"),
    doTrack = cms.untracked.bool(True),
    lostTracksSrc = cms.InputTag("lostTracks"),
    packedCandSrc = cms.InputTag("packedPFCandidates"),
    trackPtMin = cms.untracked.double(0.01),
    vertexSrc = cms.InputTag("unpackedTracksAndVertices")
)


process.selectedPatCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
    candidates = cms.VInputTag(cms.InputTag("selectedPatElectrons"), cms.InputTag("selectedPatMuons"), cms.InputTag("selectedPatTaus"), cms.InputTag("selectedPatPhotons"), cms.InputTag("selectedPatJets")),
    logName = cms.untracked.string('selectedPatCanddiates|PATSummaryTables')
)


process.skimanalysis = cms.EDAnalyzer("FilterAnalyzer",
    hltresults = cms.InputTag("TriggerResults","","HiForest"),
    superFilters = cms.vstring('')
)


process.trackAnalyzer = cms.EDAnalyzer("TrackAnalyzer",
    beamSpotSrc = cms.untracked.InputTag("offlineBeamSpot"),
    chi2Map = cms.InputTag("packedPFCandidateTrackChi2"),
    chi2MapLost = cms.InputTag("lostTrackChi2"),
    doTrack = cms.untracked.bool(True),
    lostTracksSrc = cms.InputTag("lostTracks"),
    packedCandSrc = cms.InputTag("packedPFCandidates"),
    trackPtMin = cms.untracked.double(0.01),
    vertexSrc = cms.InputTag("unpackedTracksAndVertices")
)


process.zdcanalyzer = cms.EDAnalyzer("ZDCTreeProducer",
    calZDCDigi = cms.bool(True),
    doZDCDigi = cms.bool(False),
    doZDCRecHit = cms.bool(True),
    nZdcTs = cms.int32(10),
    verbose = cms.bool(True),
    zdcDigiSrc = cms.InputTag("hcalDigis","ZDC"),
    zdcRecHitSrc = cms.InputTag("QWzdcreco")
)


process.DQMStore = cms.Service("DQMStore",
    MEsToSave = cms.untracked.vstring(
        'DT/02-Segments/03-MeanT0/T0MeanAllWheels',
        'EcalBarrel/EBOccupancyTask/EBOT digi occupancy',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +',
        'Muons/MuonRecoAnalyzer/',
        'Muons/MuonIdDQM/GlobalMuons/',
        'PixelPhase1/Phase1_MechanicalView/',
        'PixelPhase1/Tracks/',
        'SiStrip/MechanicalView/',
        'Tracking/PrimaryVertices/highPurityTracks/pt_0to1/offline/',
        'Tracking/TrackParameters/generalTracks/LSanalysis/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/LSanalysis/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/LSanalysis/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/LSanalysis/',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/GeneralProperties/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/GeneralProperties/',
        'Tracking/TrackParameters/generalTracks/HitProperties/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/HitProperties/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/HitProperties/',
        'Tracking/TrackParameters/generalTracks/HitProperties/Pixel/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/Pixel/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/HitProperties/Pixel/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/HitProperties/Pixel/',
        'Tracking/TrackParameters/generalTracks/HitProperties/Strip/',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/Strip/',
        'Tracking/TrackParameters/highPurityTracks/pt_0to1/HitProperties/Strip/',
        'Tracking/TrackParameters/highPurityTracks/dzPV0p1/HitProperties/Strip/'
    ),
    assertLegacySafe = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(True),
    saveByLumi = cms.untracked.bool(False),
    trackME = cms.untracked.string(''),
    verbose = cms.untracked.int32(0)
)


process.MessageLogger = cms.Service("MessageLogger",
    cerr = cms.untracked.PSet(
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        enable = cms.untracked.bool(True),
        enableStatistics = cms.untracked.bool(False),
        lineLength = cms.optional.untracked.int32,
        noLineBreaks = cms.optional.untracked.bool,
        noTimeStamps = cms.untracked.bool(False),
        resetStatistics = cms.untracked.bool(False),
        statisticsThreshold = cms.untracked.string('WARNING'),
        threshold = cms.untracked.string('INFO'),
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    cout = cms.untracked.PSet(
        enable = cms.untracked.bool(False),
        enableStatistics = cms.untracked.bool(False),
        lineLength = cms.optional.untracked.int32,
        noLineBreaks = cms.optional.untracked.bool,
        noTimeStamps = cms.optional.untracked.bool,
        resetStatistics = cms.untracked.bool(False),
        statisticsThreshold = cms.optional.untracked.string,
        threshold = cms.optional.untracked.string,
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    debugModules = cms.untracked.vstring(),
    default = cms.untracked.PSet(
        limit = cms.optional.untracked.int32,
        lineLength = cms.untracked.int32(80),
        noLineBreaks = cms.untracked.bool(False),
        noTimeStamps = cms.untracked.bool(False),
        reportEvery = cms.untracked.int32(1),
        statisticsThreshold = cms.untracked.string('INFO'),
        threshold = cms.untracked.string('INFO'),
        timespan = cms.optional.untracked.int32,
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    files = cms.untracked.PSet(
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            enableStatistics = cms.untracked.bool(False),
            extension = cms.optional.untracked.string,
            filename = cms.optional.untracked.string,
            lineLength = cms.optional.untracked.int32,
            noLineBreaks = cms.optional.untracked.bool,
            noTimeStamps = cms.optional.untracked.bool,
            output = cms.optional.untracked.string,
            resetStatistics = cms.untracked.bool(False),
            statisticsThreshold = cms.optional.untracked.string,
            threshold = cms.optional.untracked.string,
            allowAnyLabel_=cms.optional.untracked.PSetTemplate(
                limit = cms.optional.untracked.int32,
                reportEvery = cms.untracked.int32(1),
                timespan = cms.optional.untracked.int32
            )
        )
    ),
    suppressDebug = cms.untracked.vstring(),
    suppressFwkInfo = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    allowAnyLabel_=cms.optional.untracked.PSetTemplate(
        limit = cms.optional.untracked.int32,
        reportEvery = cms.untracked.int32(1),
        timespan = cms.optional.untracked.int32
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    CTPPSFastRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1357987)
    ),
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(987346)
    ),
    RPSiDetDigitizer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(137137)
    ),
    RPixDetDigitizer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(137137)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(98765432)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6541321)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(654321)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(234567)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    fastSimProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(13579)
    ),
    fastTrackerRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(24680)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(88776655)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6453209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(54525)
    ),
    saveFileName = cms.untracked.string(''),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11223344)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonGEMDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('HiForestMiniAOD_OnlyCharged_DATA_Dfinder.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL',
        'ZDC',
        'CASTOR',
        'EcalBarrel',
        'EcalEndcap',
        'EcalPreshower',
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerConstituentsMapBuilder = cms.ESProducer("CaloTowerConstituentsMapBuilder",
    MapAuto = cms.untracked.bool(False),
    MapFile = cms.untracked.string('Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz'),
    SkipHE = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService",
    maxExtrapolationTimeInSec = cms.uint32(0)
)


process.EcalLaserCorrectionServiceMC = cms.ESProducer("EcalLaserCorrectionServiceMC",
    appendToDataLabel = cms.string('')
)


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GEMGeometryESModule = cms.ESProducer("GEMGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(18268),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    fromDD4hep = cms.untracked.bool(False),
    fromDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.SteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAlong'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.SteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAny'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.SteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorOpposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerAdditionalParametersPerDet = cms.ESProducer("TrackerAdditionalParametersPerDetESModule",
    appendToDataLabel = cms.string('')
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer",
    usePhase2Stacks = cms.bool(False)
)


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(18268)
)


process.XMLFromDBSource = cms.ESProducer("XMLIdealGeometryESProducer",
    label = cms.string('Extended'),
    rootDDName = cms.string('cms:OCMS')
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.ak10PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak10PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFCHSL1Fastjet',
        'ak10PFCHSL2Relative',
        'ak10PFCHSL3Absolute',
        'ak10PFCHSResidual'
    )
)


process.ak10PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFCHSL1Offset',
        'ak10PFCHSL2Relative',
        'ak10PFCHSL3Absolute',
        'ak10PFCHSResidual'
    )
)


process.ak10PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak10PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFCHSL2Relative',
        'ak10PFCHSL3Absolute'
    )
)


process.ak10PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFCHSL2Relative',
        'ak10PFCHSL3Absolute',
        'ak10PFCHSResidual'
    )
)


process.ak10PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L2Relative')
)


process.ak10PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L3Absolute')
)


process.ak10PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak10PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak10PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFL1Fastjet',
        'ak10PFL2Relative',
        'ak10PFL3Absolute',
        'ak10PFResidual'
    )
)


process.ak10PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFL1Offset',
        'ak10PFL2Relative',
        'ak10PFL3Absolute',
        'ak10PFResidual'
    )
)


process.ak10PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak10PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFL2Relative',
        'ak10PFL3Absolute'
    )
)


process.ak10PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFL2Relative',
        'ak10PFL3Absolute',
        'ak10PFResidual'
    )
)


process.ak10PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L2Relative')
)


process.ak10PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L3Absolute')
)


process.ak10PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L2L3Residual')
)


process.ak1PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak1PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFCHSL1Fastjet',
        'ak1PFCHSL2Relative',
        'ak1PFCHSL3Absolute',
        'ak1PFCHSResidual'
    )
)


process.ak1PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFCHSL1Offset',
        'ak1PFCHSL2Relative',
        'ak1PFCHSL3Absolute',
        'ak1PFCHSResidual'
    )
)


process.ak1PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak1PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFCHSL2Relative',
        'ak1PFCHSL3Absolute'
    )
)


process.ak1PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFCHSL2Relative',
        'ak1PFCHSL3Absolute',
        'ak1PFCHSResidual'
    )
)


process.ak1PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L2Relative')
)


process.ak1PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L3Absolute')
)


process.ak1PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak1PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak1PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFL1Fastjet',
        'ak1PFL2Relative',
        'ak1PFL3Absolute',
        'ak1PFResidual'
    )
)


process.ak1PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFL1Offset',
        'ak1PFL2Relative',
        'ak1PFL3Absolute',
        'ak1PFResidual'
    )
)


process.ak1PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak1PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFL2Relative',
        'ak1PFL3Absolute'
    )
)


process.ak1PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFL2Relative',
        'ak1PFL3Absolute',
        'ak1PFResidual'
    )
)


process.ak1PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L2Relative')
)


process.ak1PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L3Absolute')
)


process.ak1PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L2L3Residual')
)


process.ak2PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak2PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFCHSL1Fastjet',
        'ak2PFCHSL2Relative',
        'ak2PFCHSL3Absolute',
        'ak2PFCHSResidual'
    )
)


process.ak2PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFCHSL1Offset',
        'ak2PFCHSL2Relative',
        'ak2PFCHSL3Absolute',
        'ak2PFCHSResidual'
    )
)


process.ak2PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak2PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFCHSL2Relative',
        'ak2PFCHSL3Absolute'
    )
)


process.ak2PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFCHSL2Relative',
        'ak2PFCHSL3Absolute',
        'ak2PFCHSResidual'
    )
)


process.ak2PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L2Relative')
)


process.ak2PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L3Absolute')
)


process.ak2PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak2PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak2PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFL1Fastjet',
        'ak2PFL2Relative',
        'ak2PFL3Absolute',
        'ak2PFResidual'
    )
)


process.ak2PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFL1Offset',
        'ak2PFL2Relative',
        'ak2PFL3Absolute',
        'ak2PFResidual'
    )
)


process.ak2PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak2PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFL2Relative',
        'ak2PFL3Absolute'
    )
)


process.ak2PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFL2Relative',
        'ak2PFL3Absolute',
        'ak2PFResidual'
    )
)


process.ak2PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L2Relative')
)


process.ak2PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L3Absolute')
)


process.ak2PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L2L3Residual')
)


process.ak3PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak3PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFCHSL1Fastjet',
        'ak3PFCHSL2Relative',
        'ak3PFCHSL3Absolute',
        'ak3PFCHSResidual'
    )
)


process.ak3PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFCHSL1Offset',
        'ak3PFCHSL2Relative',
        'ak3PFCHSL3Absolute',
        'ak3PFCHSResidual'
    )
)


process.ak3PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak3PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFCHSL2Relative',
        'ak3PFCHSL3Absolute'
    )
)


process.ak3PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFCHSL2Relative',
        'ak3PFCHSL3Absolute',
        'ak3PFCHSResidual'
    )
)


process.ak3PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L2Relative')
)


process.ak3PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L3Absolute')
)


process.ak3PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak3PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak3PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFL1Fastjet',
        'ak3PFL2Relative',
        'ak3PFL3Absolute',
        'ak3PFResidual'
    )
)


process.ak3PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFL1Offset',
        'ak3PFL2Relative',
        'ak3PFL3Absolute',
        'ak3PFResidual'
    )
)


process.ak3PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak3PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFL2Relative',
        'ak3PFL3Absolute'
    )
)


process.ak3PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFL2Relative',
        'ak3PFL3Absolute',
        'ak3PFResidual'
    )
)


process.ak3PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L2Relative')
)


process.ak3PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L3Absolute')
)


process.ak3PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L2L3Residual')
)


process.ak4CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet',
        'ak4CaloL2Relative',
        'ak4CaloL3Absolute'
    )
)


process.ak4CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet',
        'ak4CaloL2Relative',
        'ak4CaloL3Absolute',
        'ak4CaloL6SLB'
    )
)


process.ak4CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet',
        'ak4CaloL2Relative',
        'ak4CaloL3Absolute',
        'ak4CaloResidual'
    )
)


process.ak4CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak4CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Offset',
        'ak4CaloL2Relative',
        'ak4CaloL3Absolute'
    )
)


process.ak4CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Offset',
        'ak4CaloL2Relative',
        'ak4CaloL3Absolute',
        'ak4CaloResidual'
    )
)


process.ak4CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL2Relative',
        'ak4CaloL3Absolute'
    )
)


process.ak4CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL2Relative',
        'ak4CaloL3Absolute',
        'ak4CaloL6SLB'
    )
)


process.ak4CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL2Relative',
        'ak4CaloL3Absolute',
        'ak4CaloResidual'
    )
)


process.ak4CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2Relative')
)


process.ak4CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L3Absolute')
)


process.ak4CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4CaloJetsSoftMuonTagInfos")
)


process.ak4CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak4JPTL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTFastjet',
        'ak4JPTL2Relative',
        'ak4JPTL3Absolute'
    )
)


process.ak4JPTL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTFastjet',
        'ak4JPTL2Relative',
        'ak4JPTL3Absolute',
        'ak4JPTResidual'
    )
)


process.ak4JPTL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTOffset',
        'ak4JPTL2Relative',
        'ak4JPTL3Absolute'
    )
)


process.ak4JPTL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTOffset',
        'ak4JPTL2Relative',
        'ak4JPTL3Absolute',
        'ak4JPTResidual'
    )
)


process.ak4JPTL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4JPTL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTOffset',
        'ak4JPTL2Relative',
        'ak4JPTL3Absolute'
    )
)


process.ak4JPTL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTOffset',
        'ak4JPTL2Relative',
        'ak4JPTL3Absolute',
        'ak4JPTResidual'
    )
)


process.ak4JPTL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2Relative')
)


process.ak4JPTL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L3Absolute')
)


process.ak4JPTResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2L3Residual')
)


process.ak4L1JPTFastjet = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak4CaloL1Fastjet')
)


process.ak4L1JPTOffset = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak4CaloL1Offset')
)


process.ak4PFCHSL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Fastjet',
        'ak4PFCHSL2Relative',
        'ak4PFCHSL3Absolute'
    )
)


process.ak4PFCHSL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Fastjet',
        'ak4PFCHSL2Relative',
        'ak4PFCHSL3Absolute',
        'ak4PFCHSResidual'
    )
)


process.ak4PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFCHSL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Offset',
        'ak4PFCHSL2Relative',
        'ak4PFCHSL3Absolute'
    )
)


process.ak4PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Offset',
        'ak4PFCHSL2Relative',
        'ak4PFCHSL3Absolute',
        'ak4PFCHSResidual'
    )
)


process.ak4PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL2Relative',
        'ak4PFCHSL3Absolute'
    )
)


process.ak4PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL2Relative',
        'ak4PFCHSL3Absolute',
        'ak4PFCHSResidual'
    )
)


process.ak4PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2Relative')
)


process.ak4PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L3Absolute')
)


process.ak4PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak4PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'ak4PFL2Relative',
        'ak4PFL3Absolute'
    )
)


process.ak4PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'ak4PFL2Relative',
        'ak4PFL3Absolute',
        'ak4PFL6SLB'
    )
)


process.ak4PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'ak4PFL2Relative',
        'ak4PFL3Absolute',
        'ak4PFResidual'
    )
)


process.ak4PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Offset',
        'ak4PFL2Relative',
        'ak4PFL3Absolute'
    )
)


process.ak4PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Offset',
        'ak4PFL2Relative',
        'ak4PFL3Absolute',
        'ak4PFResidual'
    )
)


process.ak4PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL2Relative',
        'ak4PFL3Absolute'
    )
)


process.ak4PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL2Relative',
        'ak4PFL3Absolute',
        'ak4PFL6SLB'
    )
)


process.ak4PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL2Relative',
        'ak4PFL3Absolute',
        'ak4PFResidual'
    )
)


process.ak4PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2Relative')
)


process.ak4PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L3Absolute')
)


process.ak4PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4PFJetsSoftMuonTagInfos")
)


process.ak4PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak4TrackL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet',
        'ak4TrackL2Relative',
        'ak4TrackL3Absolute'
    )
)


process.ak4TrackL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4TrackL2Relative',
        'ak4TrackL3Absolute'
    )
)


process.ak4TrackL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5TRK'),
    level = cms.string('L2Relative')
)


process.ak4TrackL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5TRK'),
    level = cms.string('L3Absolute')
)


process.ak5PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak5PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFCHSL1Fastjet',
        'ak5PFCHSL2Relative',
        'ak5PFCHSL3Absolute',
        'ak5PFCHSResidual'
    )
)


process.ak5PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFCHSL1Offset',
        'ak5PFCHSL2Relative',
        'ak5PFCHSL3Absolute',
        'ak5PFCHSResidual'
    )
)


process.ak5PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak5PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFCHSL2Relative',
        'ak5PFCHSL3Absolute'
    )
)


process.ak5PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFCHSL2Relative',
        'ak5PFCHSL3Absolute',
        'ak5PFCHSResidual'
    )
)


process.ak5PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L2Relative')
)


process.ak5PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L3Absolute')
)


process.ak5PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak5PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak5PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFL1Fastjet',
        'ak5PFL2Relative',
        'ak5PFL3Absolute',
        'ak5PFResidual'
    )
)


process.ak5PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFL1Offset',
        'ak5PFL2Relative',
        'ak5PFL3Absolute',
        'ak5PFResidual'
    )
)


process.ak5PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak5PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFL2Relative',
        'ak5PFL3Absolute'
    )
)


process.ak5PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFL2Relative',
        'ak5PFL3Absolute',
        'ak5PFResidual'
    )
)


process.ak5PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2Relative')
)


process.ak5PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L3Absolute')
)


process.ak5PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.ak6PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak6PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFCHSL1Fastjet',
        'ak6PFCHSL2Relative',
        'ak6PFCHSL3Absolute',
        'ak6PFCHSResidual'
    )
)


process.ak6PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFCHSL1Offset',
        'ak6PFCHSL2Relative',
        'ak6PFCHSL3Absolute',
        'ak6PFCHSResidual'
    )
)


process.ak6PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak6PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFCHSL2Relative',
        'ak6PFCHSL3Absolute'
    )
)


process.ak6PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFCHSL2Relative',
        'ak6PFCHSL3Absolute',
        'ak6PFCHSResidual'
    )
)


process.ak6PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L2Relative')
)


process.ak6PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L3Absolute')
)


process.ak6PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak6PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak6PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFL1Fastjet',
        'ak6PFL2Relative',
        'ak6PFL3Absolute',
        'ak6PFResidual'
    )
)


process.ak6PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFL1Offset',
        'ak6PFL2Relative',
        'ak6PFL3Absolute',
        'ak6PFResidual'
    )
)


process.ak6PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak6PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFL2Relative',
        'ak6PFL3Absolute'
    )
)


process.ak6PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFL2Relative',
        'ak6PFL3Absolute',
        'ak6PFResidual'
    )
)


process.ak6PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L2Relative')
)


process.ak6PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L3Absolute')
)


process.ak6PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L2L3Residual')
)


process.ak7CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet',
        'ak7CaloL2Relative',
        'ak7CaloL3Absolute'
    )
)


process.ak7CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL1Offset',
        'ak7CaloL2Relative',
        'ak7CaloL3Absolute',
        'ak7CaloL6SLB'
    )
)


process.ak7CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL1Fastjet',
        'ak7CaloL2Relative',
        'ak7CaloL3Absolute',
        'ak7CaloResidual'
    )
)


process.ak7CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak7CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL1Offset',
        'ak7CaloL2Relative',
        'ak7CaloL3Absolute'
    )
)


process.ak7CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL1Offset',
        'ak7CaloL2Relative',
        'ak7CaloL3Absolute',
        'ak7CaloResidual'
    )
)


process.ak7CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL2Relative',
        'ak7CaloL3Absolute'
    )
)


process.ak7CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL2Relative',
        'ak7CaloL3Absolute',
        'ak7CaloL6SLB'
    )
)


process.ak7CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL2Relative',
        'ak7CaloL3Absolute',
        'ak7CaloResidual'
    )
)


process.ak7CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L2Relative')
)


process.ak7CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L3Absolute')
)


process.ak7CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak7CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak7CaloJetsSoftMuonTagInfos")
)


process.ak7CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L2L3Residual')
)


process.ak7JPTL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTFastjet',
        'ak7JPTL2Relative',
        'ak7JPTL3Absolute'
    )
)


process.ak7JPTL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTFastjet',
        'ak7JPTL2Relative',
        'ak7JPTL3Absolute',
        'ak7JPTResidual'
    )
)


process.ak7JPTL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTOffset',
        'ak7JPTL2Relative',
        'ak7JPTL3Absolute'
    )
)


process.ak7JPTL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTOffset',
        'ak7JPTL2Relative',
        'ak7JPTL3Absolute',
        'ak7JPTResidual'
    )
)


process.ak7JPTL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTOffset',
        'ak7JPTL2Relative',
        'ak7JPTL3Absolute'
    )
)


process.ak7L1JPTFastjet = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK7JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak7CaloL1Fastjet')
)


process.ak7L1JPTOffset = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK7JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak7CaloL1Offset')
)


process.ak7PFCHSL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Fastjet',
        'ak7PFCHSL2Relative',
        'ak7PFCHSL3Absolute'
    )
)


process.ak7PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak7PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFCHSL1Fastjet',
        'ak7PFCHSL2Relative',
        'ak7PFCHSL3Absolute',
        'ak7PFCHSResidual'
    )
)


process.ak7PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFCHSL1Offset',
        'ak7PFCHSL2Relative',
        'ak7PFCHSL3Absolute',
        'ak7PFCHSResidual'
    )
)


process.ak7PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFCHSL2Relative',
        'ak7PFCHSL3Absolute'
    )
)


process.ak7PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFCHSL2Relative',
        'ak7PFCHSL3Absolute',
        'ak7PFCHSResidual'
    )
)


process.ak7PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L2Relative')
)


process.ak7PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L3Absolute')
)


process.ak7PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak7PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'ak7PFL2Relative',
        'ak7PFL3Absolute'
    )
)


process.ak7PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'ak7PFL2Relative',
        'ak7PFL3Absolute',
        'ak7PFL6SLB'
    )
)


process.ak7PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak7PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL1Fastjet',
        'ak7PFL2Relative',
        'ak7PFL3Absolute',
        'ak7PFResidual'
    )
)


process.ak7PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL1Offset',
        'ak7PFL2Relative',
        'ak7PFL3Absolute'
    )
)


process.ak7PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL1Offset',
        'ak7PFL2Relative',
        'ak7PFL3Absolute',
        'ak7PFResidual'
    )
)


process.ak7PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL2Relative',
        'ak7PFL3Absolute'
    )
)


process.ak7PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL2Relative',
        'ak7PFL3Absolute',
        'ak7PFL6SLB'
    )
)


process.ak7PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL2Relative',
        'ak7PFL3Absolute',
        'ak7PFResidual'
    )
)


process.ak7PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L2Relative')
)


process.ak7PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L3Absolute')
)


process.ak7PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak7PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak7PFJetsSoftMuonTagInfos")
)


process.ak7PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L2L3Residual')
)


process.ak8PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak8PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFCHSL1Fastjet',
        'ak8PFCHSL2Relative',
        'ak8PFCHSL3Absolute',
        'ak8PFCHSResidual'
    )
)


process.ak8PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFCHSL1Offset',
        'ak8PFCHSL2Relative',
        'ak8PFCHSL3Absolute',
        'ak8PFCHSResidual'
    )
)


process.ak8PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak8PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFCHSL2Relative',
        'ak8PFCHSL3Absolute'
    )
)


process.ak8PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFCHSL2Relative',
        'ak8PFCHSL3Absolute',
        'ak8PFCHSResidual'
    )
)


process.ak8PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L2Relative')
)


process.ak8PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L3Absolute')
)


process.ak8PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak8PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak8PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFL1Fastjet',
        'ak8PFL2Relative',
        'ak8PFL3Absolute',
        'ak8PFResidual'
    )
)


process.ak8PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFL1Offset',
        'ak8PFL2Relative',
        'ak8PFL3Absolute',
        'ak8PFResidual'
    )
)


process.ak8PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak8PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFL2Relative',
        'ak8PFL3Absolute'
    )
)


process.ak8PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFL2Relative',
        'ak8PFL3Absolute',
        'ak8PFResidual'
    )
)


process.ak8PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L2Relative')
)


process.ak8PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L3Absolute')
)


process.ak8PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L2L3Residual')
)


process.ak9PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak9PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFCHSL1Fastjet',
        'ak9PFCHSL2Relative',
        'ak9PFCHSL3Absolute',
        'ak9PFCHSResidual'
    )
)


process.ak9PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFCHSL1Offset',
        'ak9PFCHSL2Relative',
        'ak9PFCHSL3Absolute',
        'ak9PFCHSResidual'
    )
)


process.ak9PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak9PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFCHSL2Relative',
        'ak9PFCHSL3Absolute'
    )
)


process.ak9PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFCHSL2Relative',
        'ak9PFCHSL3Absolute',
        'ak9PFCHSResidual'
    )
)


process.ak9PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L2Relative')
)


process.ak9PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L3Absolute')
)


process.ak9PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak9PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak9PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFL1Fastjet',
        'ak9PFL2Relative',
        'ak9PFL3Absolute',
        'ak9PFResidual'
    )
)


process.ak9PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFL1Offset',
        'ak9PFL2Relative',
        'ak9PFL3Absolute',
        'ak9PFResidual'
    )
)


process.ak9PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak9PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFL2Relative',
        'ak9PFL3Absolute'
    )
)


process.ak9PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFL2Relative',
        'ak9PFL3Absolute',
        'ak9PFResidual'
    )
)


process.ak9PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L2Relative')
)


process.ak9PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L3Absolute')
)


process.ak9PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L2L3Residual')
)


process.caloSimulationParameters = cms.ESProducer("CaloSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False)
)


process.candidateJetProbabilityComputer = cms.ESProducer("CandidateJetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.combinedSecondaryVertexV2Computer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex',
        'CombinedSVIVFV2PseudoVertex',
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.ctppsBeamParametersFromLHCInfoESSource = cms.ESProducer("CTPPSBeamParametersFromLHCInfoESSource",
    appendToDataLabel = cms.string(''),
    beamDivX45 = cms.double(0.1),
    beamDivX56 = cms.double(0.1),
    beamDivY45 = cms.double(0.1),
    beamDivY56 = cms.double(0.1),
    lhcInfoLabel = cms.string(''),
    vtxOffsetX45 = cms.double(0.01),
    vtxOffsetX56 = cms.double(0.01),
    vtxOffsetY45 = cms.double(0.01),
    vtxOffsetY56 = cms.double(0.01),
    vtxOffsetZ45 = cms.double(0.01),
    vtxOffsetZ56 = cms.double(0.01),
    vtxStddevX = cms.double(0.02),
    vtxStddevY = cms.double(0.02),
    vtxStddevZ = cms.double(0.02)
)


process.ctppsInterpolatedOpticalFunctionsESSource = cms.ESProducer("CTPPSInterpolatedOpticalFunctionsESSource",
    appendToDataLabel = cms.string(''),
    lhcInfoLabel = cms.string(''),
    opticsLabel = cms.string('')
)


process.ecalSeverityLevel = cms.ESProducer("EcalSeverityLevelESProducer",
    dbstatusMask = cms.PSet(
        kBad = cms.vstring(
            'kNonRespondingIsolated',
            'kDeadVFE',
            'kDeadFE',
            'kNoDataNoTP'
        ),
        kGood = cms.vstring('kOk'),
        kProblematic = cms.vstring(
            'kDAC',
            'kNoLaser',
            'kNoisy',
            'kNNoisy',
            'kNNNoisy',
            'kNNNNoisy',
            'kNNNNNoisy',
            'kFixedG6',
            'kFixedG1',
            'kFixedG0'
        ),
        kRecovered = cms.vstring(),
        kTime = cms.vstring(),
        kWeird = cms.vstring()
    ),
    flagMask = cms.PSet(
        kBad = cms.vstring(
            'kFaultyHardware',
            'kDead',
            'kKilled'
        ),
        kGood = cms.vstring('kGood'),
        kProblematic = cms.vstring(
            'kPoorReco',
            'kPoorCalib',
            'kNoisy',
            'kSaturated'
        ),
        kRecovered = cms.vstring(
            'kLeadingEdgeRecovered',
            'kTowerRecovered'
        ),
        kTime = cms.vstring('kOutOfTime'),
        kWeird = cms.vstring(
            'kWeird',
            'kDiWeird'
        )
    ),
    timeThresh = cms.double(2.0)
)


process.ecalSimulationParametersEB = cms.ESProducer("EcalSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    name = cms.string('EcalHitsEB')
)


process.ecalSimulationParametersEE = cms.ESProducer("EcalSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    name = cms.string('EcalHitsEE')
)


process.ecalSimulationParametersES = cms.ESProducer("EcalSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    name = cms.string('EcalHitsES')
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalSimulationConstants = cms.ESProducer("HcalSimulationConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalSimulationParameters = cms.ESProducer("HcalSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False)
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.heavyIonCSVComputer = cms.ESProducer("HeavyIonCSVESProducer",
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    sv_cfg = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        calibrationRecords = cms.vstring(
            'CombinedSVIVFV2RecoVertex',
            'CombinedSVIVFV2PseudoVertex',
            'CombinedSVIVFV2NoVertex'
        ),
        categoryVariableName = cms.string('vertexCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexFinderTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ),
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ),
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackSip3dSig_2'),
            taggingVarName = cms.string('trackSip3dSig')
        ),
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackSip3dSig_3'),
            taggingVarName = cms.string('trackSip3dSig')
        ),
        cms.PSet(
            default = cms.double(-999),
            name = cms.string('TagVarCSV_trackSip3dSigAboveCharm'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ),
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ),
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ),
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackPtRel_2'),
            taggingVarName = cms.string('trackPtRel')
        ),
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackPtRel_3'),
            taggingVarName = cms.string('trackPtRel')
        ),
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ),
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ),
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackEtaRel_2'),
            taggingVarName = cms.string('trackEtaRel')
        ),
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackEtaRel_3'),
            taggingVarName = cms.string('trackEtaRel')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackDeltaR_2'),
            taggingVarName = cms.string('trackDeltaR')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackDeltaR_3'),
            taggingVarName = cms.string('trackDeltaR')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackPtRatio_2'),
            taggingVarName = cms.string('trackPtRatio')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackPtRatio_3'),
            taggingVarName = cms.string('trackPtRatio')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackJetDist_2'),
            taggingVarName = cms.string('trackJetDist')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackJetDist_3'),
            taggingVarName = cms.string('trackJetDist')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackDecayLenVal_2'),
            taggingVarName = cms.string('trackDecayLenVal')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackDecayLenVal_3'),
            taggingVarName = cms.string('trackDecayLenVal')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('TagVarCSV_trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('TagVarCSV_trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('TagVarCSV_vertexMass'),
            taggingVarName = cms.string('vertexMass')
        ),
        cms.PSet(
            default = cms.double(0),
            name = cms.string('TagVarCSV_vertexNTracks'),
            taggingVarName = cms.string('vertexNTracks')
        ),
        cms.PSet(
            default = cms.double(-10),
            name = cms.string('TagVarCSV_vertexEnergyRatio'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('TagVarCSV_vertexJetDeltaR'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ),
        cms.PSet(
            default = cms.double(-1),
            name = cms.string('TagVarCSV_flightDistance2dSig'),
            taggingVarName = cms.string('flightDistance2dSig')
        ),
        cms.PSet(
            default = cms.double(0),
            name = cms.string('TagVarCSV_jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ),
        cms.PSet(
            default = cms.double(0),
            name = cms.string('TagVarCSV_vertexCategory'),
            taggingVarName = cms.string('vertexCategory')
        )
    ),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/TMVA_Btag_CsJets_PbPb2018_BDTG.weights.xml')
)


process.ic5CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet',
        'ic5CaloL2Relative',
        'ic5CaloL3Absolute'
    )
)


process.ic5CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL1Offset',
        'ic5CaloL2Relative',
        'ic5CaloL3Absolute',
        'ic5CaloL6SLB'
    )
)


process.ic5CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL1Fastjet',
        'ic5CaloL2Relative',
        'ic5CaloL3Absolute',
        'ic5CaloResidual'
    )
)


process.ic5CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ic5CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL1Offset',
        'ic5CaloL2Relative',
        'ic5CaloL3Absolute'
    )
)


process.ic5CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL1Offset',
        'ic5CaloL2Relative',
        'ic5CaloL3Absolute',
        'ic5CaloResidual'
    )
)


process.ic5CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ic5CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL2Relative',
        'ic5CaloL3Absolute'
    )
)


process.ic5CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL2Relative',
        'ic5CaloL3Absolute',
        'ic5CaloL6SLB'
    )
)


process.ic5CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL2Relative',
        'ic5CaloL3Absolute',
        'ic5CaloResidual'
    )
)


process.ic5CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L2Relative')
)


process.ic5CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L3Absolute')
)


process.ic5CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ic5CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ic5CaloJetsSoftMuonTagInfos")
)


process.ic5CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L2L3Residual')
)


process.ic5PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'ic5PFL2Relative',
        'ic5PFL3Absolute'
    )
)


process.ic5PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'ic5PFL2Relative',
        'ic5PFL3Absolute',
        'ic5PFL6SLB'
    )
)


process.ic5PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL1Fastjet',
        'ic5PFL2Relative',
        'ic5PFL3Absolute',
        'ic5PFResidual'
    )
)


process.ic5PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ic5PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL1Offset',
        'ic5PFL2Relative',
        'ic5PFL3Absolute'
    )
)


process.ic5PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL1Offset',
        'ic5PFL2Relative',
        'ic5PFL3Absolute',
        'ic5PFResidual'
    )
)


process.ic5PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ic5PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL2Relative',
        'ic5PFL3Absolute'
    )
)


process.ic5PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL2Relative',
        'ic5PFL3Absolute',
        'ic5PFL6SLB'
    )
)


process.ic5PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL2Relative',
        'ic5PFL3Absolute',
        'ic5PFResidual'
    )
)


process.ic5PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L2Relative')
)


process.ic5PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L3Absolute')
)


process.ic5PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ic5PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ic5PFJetsSoftMuonTagInfos")
)


process.ic5PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L2L3Residual')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.jetBProbabilityComputer = cms.ESProducer("JetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.jetProbabilityComputer = cms.ESProducer("JetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.kt4CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet',
        'kt4CaloL2Relative',
        'kt4CaloL3Absolute'
    )
)


process.kt4CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL1Offset',
        'kt4CaloL2Relative',
        'kt4CaloL3Absolute',
        'kt4CaloL6SLB'
    )
)


process.kt4CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL1Fastjet',
        'kt4CaloL2Relative',
        'kt4CaloL3Absolute',
        'kt4CaloResidual'
    )
)


process.kt4CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.kt4CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL1Offset',
        'kt4CaloL2Relative',
        'kt4CaloL3Absolute'
    )
)


process.kt4CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL1Offset',
        'kt4CaloL2Relative',
        'kt4CaloL3Absolute',
        'kt4CaloResidual'
    )
)


process.kt4CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt4CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL2Relative',
        'kt4CaloL3Absolute'
    )
)


process.kt4CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL2Relative',
        'kt4CaloL3Absolute',
        'kt4CaloL6SLB'
    )
)


process.kt4CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL2Relative',
        'kt4CaloL3Absolute',
        'kt4CaloResidual'
    )
)


process.kt4CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L2Relative')
)


process.kt4CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L3Absolute')
)


process.kt4CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt4CaloJetsSoftMuonTagInfos")
)


process.kt4CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L2L3Residual')
)


process.kt4PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'kt4PFL2Relative',
        'kt4PFL3Absolute'
    )
)


process.kt4PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'kt4PFL2Relative',
        'kt4PFL3Absolute',
        'kt4PFL6SLB'
    )
)


process.kt4PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL1Fastjet',
        'kt4PFL2Relative',
        'kt4PFL3Absolute',
        'kt4PFResidual'
    )
)


process.kt4PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.kt4PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL1Offset',
        'kt4PFL2Relative',
        'kt4PFL3Absolute'
    )
)


process.kt4PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL1Offset',
        'kt4PFL2Relative',
        'kt4PFL3Absolute',
        'kt4PFResidual'
    )
)


process.kt4PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt4PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL2Relative',
        'kt4PFL3Absolute'
    )
)


process.kt4PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL2Relative',
        'kt4PFL3Absolute',
        'kt4PFL6SLB'
    )
)


process.kt4PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL2Relative',
        'kt4PFL3Absolute',
        'kt4PFResidual'
    )
)


process.kt4PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L2Relative')
)


process.kt4PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L3Absolute')
)


process.kt4PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt4PFJetsSoftMuonTagInfos")
)


process.kt4PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L2L3Residual')
)


process.kt6CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet',
        'kt6CaloL2Relative',
        'kt6CaloL3Absolute'
    )
)


process.kt6CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL1Offset',
        'kt6CaloL2Relative',
        'kt6CaloL3Absolute',
        'kt6CaloL6SLB'
    )
)


process.kt6CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL1Fastjet',
        'kt6CaloL2Relative',
        'kt6CaloL3Absolute',
        'kt6CaloResidual'
    )
)


process.kt6CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.kt6CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL1Offset',
        'kt6CaloL2Relative',
        'kt6CaloL3Absolute'
    )
)


process.kt6CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL1Offset',
        'kt6CaloL2Relative',
        'kt6CaloL3Absolute',
        'kt6CaloResidual'
    )
)


process.kt6CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt6CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL2Relative',
        'kt6CaloL3Absolute'
    )
)


process.kt6CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL2Relative',
        'kt6CaloL3Absolute',
        'kt6CaloL6SLB'
    )
)


process.kt6CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL2Relative',
        'kt6CaloL3Absolute',
        'kt6CaloResidual'
    )
)


process.kt6CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L2Relative')
)


process.kt6CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L3Absolute')
)


process.kt6CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt6CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt6CaloJetsSoftMuonTagInfos")
)


process.kt6CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L2L3Residual')
)


process.kt6PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'kt6PFL2Relative',
        'kt6PFL3Absolute'
    )
)


process.kt6PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'kt6PFL2Relative',
        'kt6PFL3Absolute',
        'kt6PFL6SLB'
    )
)


process.kt6PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL1Fastjet',
        'kt6PFL2Relative',
        'kt6PFL3Absolute',
        'kt6PFResidual'
    )
)


process.kt6PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.kt6PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL1Offset',
        'kt6PFL2Relative',
        'kt6PFL3Absolute'
    )
)


process.kt6PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL1Offset',
        'kt6PFL2Relative',
        'kt6PFL3Absolute',
        'kt6PFResidual'
    )
)


process.kt6PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt6PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL2Relative',
        'kt6PFL3Absolute'
    )
)


process.kt6PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL2Relative',
        'kt6PFL3Absolute',
        'kt6PFL6SLB'
    )
)


process.kt6PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL2Relative',
        'kt6PFL3Absolute',
        'kt6PFResidual'
    )
)


process.kt6PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L2Relative')
)


process.kt6PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L3Absolute')
)


process.kt6PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt6PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt6PFJetsSoftMuonTagInfos")
)


process.kt6PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L2L3Residual')
)


process.multipleScatteringParametrisationMakerESProducer = cms.ESProducer("MultipleScatteringParametrisationMakerESProducer",
    appendToDataLabel = cms.string('')
)


process.muonGeometryConstants = cms.ESProducer("MuonGeometryConstantsESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False)
)


process.muonOffsetESProducer = cms.ESProducer("MuonOffsetESProducer",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    names = cms.vstring(
        'MuonCommonNumbering',
        'MuonBarrel',
        'MuonEndcap',
        'MuonBarrelWheels',
        'MuonBarrelStation1',
        'MuonBarrelStation2',
        'MuonBarrelStation3',
        'MuonBarrelStation4',
        'MuonBarrelSuperLayer',
        'MuonBarrelLayer',
        'MuonBarrelWire',
        'MuonRpcPlane1I',
        'MuonRpcPlane1O',
        'MuonRpcPlane2I',
        'MuonRpcPlane2O',
        'MuonRpcPlane3S',
        'MuonRpcPlane4',
        'MuonRpcChamberLeft',
        'MuonRpcChamberMiddle',
        'MuonRpcChamberRight',
        'MuonRpcEndcap1',
        'MuonRpcEndcap2',
        'MuonRpcEndcap3',
        'MuonRpcEndcap4',
        'MuonRpcEndcapSector',
        'MuonRpcEndcapChamberB1',
        'MuonRpcEndcapChamberB2',
        'MuonRpcEndcapChamberB3',
        'MuonRpcEndcapChamberC1',
        'MuonRpcEndcapChamberC2',
        'MuonRpcEndcapChamberC3',
        'MuonRpcEndcapChamberE1',
        'MuonRpcEndcapChamberE2',
        'MuonRpcEndcapChamberE3',
        'MuonRpcEndcapChamberF1',
        'MuonRpcEndcapChamberF2',
        'MuonRpcEndcapChamberF3',
        'MuonEndcapStation1',
        'MuonEndcapStation2',
        'MuonEndcapStation3',
        'MuonEndcapStation4',
        'MuonEndcapSubrings',
        'MuonEndcapSectors',
        'MuonEndcapLayers',
        'MuonEndcapRing1',
        'MuonEndcapRing2',
        'MuonEndcapRing3',
        'MuonEndcapRingA',
        'MuonGEMEndcap',
        'MuonGEMSector',
        'MuonGEMChamber'
    )
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    ),
    siPixelQualityLabel = cms.string('')
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ),
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.simpleSecondaryVertex2TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.simpleSecondaryVertex3TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackCounting3D2ndComputer = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.trackCounting3D3rdComputer = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.BTagRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('JetTagComputerRecord')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionTimeout = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('124X_dataRun2_PromptLike_HI_v1'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    toGet = cms.VPSet(cms.PSet(
        connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
        record = cms.string('BTagTrackProbability3DRcd'),
        tag = cms.string('JPcalib_Data103X_2018PbPb_v1')
    ))
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ),
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ),
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(100.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379,
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807,
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05,
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107,
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601,
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447,
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06,
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05,
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ),
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ),
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ),
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ),
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ),
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ),
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        noiseCorrelation = cms.vdouble(0.0),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        noiseCorrelation = cms.vdouble(0.26, 0.254),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(208),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        noiseCorrelation = cms.vdouble(0.0),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        noiseCorrelation = cms.vdouble(0.26, 0.254),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(208),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        noiseCorrelation = cms.vdouble(0.0),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        noiseCorrelation = cms.vdouble(0.0),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        noiseCorrelation = cms.vdouble(0.0),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(True),
    useHFUpgrade = cms.bool(True),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(False),
    useLayer0Weight = cms.bool(True)
)


process.essourceEcalSev = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalSeverityLevelAlgoRcd')
)


process.prefer("es_hardcode")

process.siPixelRecHitsPreSplittingTask = cms.Task(process.siPixelRecHitsPreSplitting)


process.ak4CaloL1FastL2L3CorrectorTask = cms.Task(process.ak4CaloL1FastL2L3Corrector, process.ak4CaloL1FastjetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector)


process.ak4CaloL1FastL2L3L6CorrectorTask = cms.Task(process.ak4CaloL1FastL2L3L6Corrector, process.ak4CaloL1FastjetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloL6SLBCorrector)


process.ak4CaloL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4CaloL1FastL2L3ResidualCorrector, process.ak4CaloL1FastjetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloResidualCorrector)


process.ak4CaloL1L2L3CorrectorTask = cms.Task(process.ak4CaloL1L2L3Corrector, process.ak4CaloL1OffsetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector)


process.ak4CaloL1L2L3ResidualCorrectorTask = cms.Task(process.ak4CaloL1L2L3ResidualCorrector, process.ak4CaloL1OffsetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloResidualCorrector)


process.ak4CaloL2L3CorrectorTask = cms.Task(process.ak4CaloL2L3Corrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector)


process.ak4CaloL2L3L6CorrectorTask = cms.Task(process.ak4CaloL2L3L6Corrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloL6SLBCorrector)


process.ak4CaloL2L3ResidualCorrectorTask = cms.Task(process.ak4CaloL2L3ResidualCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloResidualCorrector)


process.ak4L1JPTFastjetCorrectorTask = cms.Task(process.ak4CaloL1FastjetCorrector, process.ak4L1JPTFastjetCorrector)


process.ak4L1JPTOffsetCorrectorTask = cms.Task(process.ak4CaloL1OffsetCorrector, process.ak4L1JPTOffsetCorrector)


process.ak4PFCHSL1FastL2L3CorrectorTask = cms.Task(process.ak4PFCHSL1FastL2L3Corrector, process.ak4PFCHSL1FastjetCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector)


process.ak4PFCHSL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4PFCHSL1FastL2L3ResidualCorrector, process.ak4PFCHSL1FastjetCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector, process.ak4PFCHSResidualCorrector)


process.ak4PFCHSL1L2L3CorrectorTask = cms.Task(process.ak4PFCHSL1L2L3Corrector, process.ak4PFCHSL1OffsetCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector)


process.ak4PFCHSL1L2L3ResidualCorrectorTask = cms.Task(process.ak4PFCHSL1L2L3ResidualCorrector, process.ak4PFCHSL1OffsetCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector, process.ak4PFCHSResidualCorrector)


process.ak4PFCHSL2L3CorrectorTask = cms.Task(process.ak4PFCHSL2L3Corrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector)


process.ak4PFCHSL2L3ResidualCorrectorTask = cms.Task(process.ak4PFCHSL2L3ResidualCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector, process.ak4PFCHSResidualCorrector)


process.ak4PFL1FastL2L3CorrectorTask = cms.Task(process.ak4PFL1FastL2L3Corrector, process.ak4PFL1FastjetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector)


process.ak4PFL1FastL2L3L6CorrectorTask = cms.Task(process.ak4PFL1FastL2L3L6Corrector, process.ak4PFL1FastjetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFL6SLBCorrector)


process.ak4PFL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4PFL1FastL2L3ResidualCorrector, process.ak4PFL1FastjetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFResidualCorrector)


process.ak4PFL1L2L3CorrectorTask = cms.Task(process.ak4PFL1L2L3Corrector, process.ak4PFL1OffsetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector)


process.ak4PFL1L2L3ResidualCorrectorTask = cms.Task(process.ak4PFL1L2L3ResidualCorrector, process.ak4PFL1OffsetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFResidualCorrector)


process.ak4PFL2L3CorrectorTask = cms.Task(process.ak4PFL2L3Corrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector)


process.ak4PFL2L3L6CorrectorTask = cms.Task(process.ak4PFL2L3L6Corrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFL6SLBCorrector)


process.ak4PFL2L3ResidualCorrectorTask = cms.Task(process.ak4PFL2L3ResidualCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFResidualCorrector)


process.ak4PFPuppiL1FastL2L3CorrectorTask = cms.Task(process.ak4PFPuppiL1FastL2L3Corrector, process.ak4PFPuppiL1FastjetCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector)


process.ak4PFPuppiL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4PFPuppiL1FastL2L3ResidualCorrector, process.ak4PFPuppiL1FastjetCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector, process.ak4PFPuppiResidualCorrector)


process.ak4PFPuppiL1L2L3CorrectorTask = cms.Task(process.ak4PFPuppiL1L2L3Corrector, process.ak4PFPuppiL1OffsetCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector)


process.ak4PFPuppiL1L2L3ResidualCorrectorTask = cms.Task(process.ak4PFPuppiL1L2L3ResidualCorrector, process.ak4PFPuppiL1OffsetCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector, process.ak4PFPuppiResidualCorrector)


process.ak4PFPuppiL2L3CorrectorTask = cms.Task(process.ak4PFPuppiL2L3Corrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector)


process.ak4PFPuppiL2L3ResidualCorrectorTask = cms.Task(process.ak4PFPuppiL2L3ResidualCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector, process.ak4PFPuppiResidualCorrector)


process.ak4TrackL2L3CorrectorTask = cms.Task(process.ak4TrackL2L3Corrector, process.ak4TrackL2RelativeCorrector, process.ak4TrackL3AbsoluteCorrector)


process.ak5JTAExplicitTask = cms.Task(process.ak5JetTracksAssociatorExplicit)


process.ak5JTATask = cms.Task(process.ak5JetExtender, process.ak5JetTracksAssociatorAtCaloFace, process.ak5JetTracksAssociatorAtVertex, process.ak5JetTracksAssociatorAtVertexPF)


process.cleanPatCandidatesTask = cms.Task(process.cleanPatElectrons, process.cleanPatJets, process.cleanPatMuons, process.cleanPatPhotons, process.cleanPatTaus)


process.correctionTermsCaloMetTask = cms.Task(process.ak4CaloL2L3CorrectorTask, process.ak4CaloL2L3ResidualCorrectorTask, process.corrCaloMetType1, process.corrCaloMetType2, process.muCaloMetCorr)


process.correctionTermsPfMetType1Type2Task = cms.Task(process.ak4PFCHSL1FastL2L3CorrectorTask, process.ak4PFCHSL1FastL2L3ResidualCorrectorTask, process.corrPfMetType1, process.corrPfMetType2, process.particleFlowPtrs, process.pfCandMETcorr, process.pfCandsNotInJetsForMetCorr, process.pfCandsNotInJetsPtrForMetCorr, process.pfJetsPtrForMetCorr)


process.electronPFIsolationDepositsPATTask = cms.Task(process.elPFIsoDepositChargedAllPAT, process.elPFIsoDepositChargedPAT, process.elPFIsoDepositGammaPAT, process.elPFIsoDepositNeutralPAT, process.elPFIsoDepositPUPAT)


process.electronPFIsolationValuesPATTask = cms.Task(process.elPFIsoValueCharged03NoPFIdPAT, process.elPFIsoValueCharged03PFIdPAT, process.elPFIsoValueCharged04NoPFIdPAT, process.elPFIsoValueCharged04PFIdPAT, process.elPFIsoValueChargedAll03NoPFIdPAT, process.elPFIsoValueChargedAll03PFIdPAT, process.elPFIsoValueChargedAll04NoPFIdPAT, process.elPFIsoValueChargedAll04PFIdPAT, process.elPFIsoValueGamma03NoPFIdPAT, process.elPFIsoValueGamma03PFIdPAT, process.elPFIsoValueGamma04NoPFIdPAT, process.elPFIsoValueGamma04PFIdPAT, process.elPFIsoValueNeutral03NoPFIdPAT, process.elPFIsoValueNeutral03PFIdPAT, process.elPFIsoValueNeutral04NoPFIdPAT, process.elPFIsoValueNeutral04PFIdPAT, process.elPFIsoValuePU03NoPFIdPAT, process.elPFIsoValuePU03PFIdPAT, process.elPFIsoValuePU04NoPFIdPAT, process.elPFIsoValuePU04PFIdPAT)


process.filteredDisplacedMuonsTask = cms.Task(process.filteredDisplacedMuons)


process.hiCleanedGenJetsTask_ = cms.Task(process.ak4HiGenJets, process.ak4HiGenJetsCleaned, process.allPartons, process.cleanedPartons, process.genParticlesForJets)


process.hiGenJetsTask = cms.Task(process.ak4HiGenJets, process.ak4HiSignalGenJets, process.allPartons, process.genParticlesForJets, process.hiSignalGenParticles)


process.makePatDisplacedMuonsTask = cms.Task(process.filteredDisplacedMuonsTask, process.patDisplacedMuons)


process.makePatLowPtElectronsTask = cms.Task(process.lowPtElectronMatch, process.patLowPtElectrons)


process.makePatOOTPhotonsTask = cms.Task(process.ootPhotonMatch, process.patOOTPhotons)


process.muonPFIsolationDepositsPATTask = cms.Task(process.muPFIsoDepositChargedAllPAT, process.muPFIsoDepositChargedPAT, process.muPFIsoDepositGammaPAT, process.muPFIsoDepositNeutralPAT, process.muPFIsoDepositPUPAT)


process.muonPFIsolationValuesPATTask = cms.Task(process.muPFIsoValueCharged03PAT, process.muPFIsoValueCharged04PAT, process.muPFIsoValueChargedAll03PAT, process.muPFIsoValueChargedAll04PAT, process.muPFIsoValueGamma03PAT, process.muPFIsoValueGamma04PAT, process.muPFIsoValueGammaHighThreshold03PAT, process.muPFIsoValueGammaHighThreshold04PAT, process.muPFIsoValueNeutral03PAT, process.muPFIsoValueNeutral04PAT, process.muPFIsoValueNeutralHighThreshold03PAT, process.muPFIsoValueNeutralHighThreshold04PAT, process.muPFIsoValuePU03PAT, process.muPFIsoValuePU04PAT, process.muPFMeanDRIsoValueCharged03PAT, process.muPFMeanDRIsoValueCharged04PAT, process.muPFMeanDRIsoValueChargedAll03PAT, process.muPFMeanDRIsoValueChargedAll04PAT, process.muPFMeanDRIsoValueGamma03PAT, process.muPFMeanDRIsoValueGamma04PAT, process.muPFMeanDRIsoValueGammaHighThreshold03PAT, process.muPFMeanDRIsoValueGammaHighThreshold04PAT, process.muPFMeanDRIsoValueNeutral03PAT, process.muPFMeanDRIsoValueNeutral04PAT, process.muPFMeanDRIsoValueNeutralHighThreshold03PAT, process.muPFMeanDRIsoValueNeutralHighThreshold04PAT, process.muPFMeanDRIsoValuePU03PAT, process.muPFMeanDRIsoValuePU04PAT, process.muPFSumDRIsoValueCharged03PAT, process.muPFSumDRIsoValueCharged04PAT, process.muPFSumDRIsoValueChargedAll03PAT, process.muPFSumDRIsoValueChargedAll04PAT, process.muPFSumDRIsoValueGamma03PAT, process.muPFSumDRIsoValueGamma04PAT, process.muPFSumDRIsoValueGammaHighThreshold03PAT, process.muPFSumDRIsoValueGammaHighThreshold04PAT, process.muPFSumDRIsoValueNeutral03PAT, process.muPFSumDRIsoValueNeutral04PAT, process.muPFSumDRIsoValueNeutralHighThreshold03PAT, process.muPFSumDRIsoValueNeutralHighThreshold04PAT, process.muPFSumDRIsoValuePU03PAT, process.muPFSumDRIsoValuePU04PAT)


process.ootPhotonTask = cms.Task(process.ootPhotonCore, process.ootPhotons, process.ootPhotonsTmp, process.particleFlowClusterOOTECAL, process.particleFlowClusterOOTECALUncorrected, process.particleFlowRecHitOOTECAL, process.particleFlowSuperClusterOOTECAL)


process.patJetCorrectionsTask = cms.Task(process.patJetCorrFactors)


process.patJetFlavourIdLegacyTask = cms.Task(process.patJetFlavourAssociationLegacy, process.patJetPartonAssociationLegacy, process.patJetPartonsLegacy)


process.patJetFlavourIdTask = cms.Task(process.patJetFlavourAssociation, process.patJetPartons)


process.patMETCorrectionsTask = cms.Task(process.caloMetT1, process.caloMetT1T2, process.correctionTermsCaloMetTask, process.correctionTermsPfMetType1Type2Task, process.pfMetT1, process.pfMetT1T2)


process.patPFTauIsolationTask = cms.Task(process.tauIsoDepositPFCandidates, process.tauIsoDepositPFChargedHadrons, process.tauIsoDepositPFGammas, process.tauIsoDepositPFNeutralHadrons)


process.pfDeepCSVTask = cms.Task(process.pfDeepCMVAJetTags, process.pfDeepCMVATagInfos, process.pfDeepCSVJetTags, process.pfDeepCSVTagInfos)


process.pfElectronIsolationPATTask = cms.Task(process.electronPFIsolationDepositsPATTask, process.electronPFIsolationValuesPATTask)


process.pfNoPileUpIsoPFBRECOTask = cms.Task(process.pfNoPileUpIsoPFBRECO, process.pfPileUpIsoPFBRECO)


process.pfNoPileUpJMETask = cms.Task(process.goodOfflinePrimaryVertices, process.pfNoPileUpJME, process.pfPileUpJME)


process.pfNoPileUpPFBRECOTask = cms.Task(process.pfNoPileUpPFBRECO, process.pfPileUpPFBRECO)


process.pfSortByTypePFBRECOTask = cms.Task(process.pfAllChargedHadronsPFBRECO, process.pfAllChargedParticlesPFBRECO, process.pfAllNeutralHadronsAndPhotonsPFBRECO, process.pfAllNeutralHadronsPFBRECO, process.pfAllPhotonsPFBRECO, process.pfPileUpAllChargedParticlesPFBRECO)


process.photonPFIsolationDepositsPATTask = cms.Task(process.phPFIsoDepositChargedAllPAT, process.phPFIsoDepositChargedPAT, process.phPFIsoDepositGammaPAT, process.phPFIsoDepositNeutralPAT, process.phPFIsoDepositPUPAT)


process.photonPFIsolationValuesPATTask = cms.Task(process.phPFIsoValueCharged03PFIdPAT, process.phPFIsoValueCharged04PFIdPAT, process.phPFIsoValueChargedAll03PFIdPAT, process.phPFIsoValueChargedAll04PFIdPAT, process.phPFIsoValueGamma03PFIdPAT, process.phPFIsoValueGamma04PFIdPAT, process.phPFIsoValueNeutral03PFIdPAT, process.phPFIsoValueNeutral04PFIdPAT, process.phPFIsoValuePU03PFIdPAT, process.phPFIsoValuePU04PFIdPAT)


process.recoGenJetsHIpostAODTask = cms.Task(process.allPartons, process.hiGenJetsTask)


process.recoPFJetsHIpostAODTask = cms.Task(process.PackedPFTowers, process.ak4PFJets, process.ak4PFJetsCHS, process.ak4PFJetsForFlow, process.ak5JetTracksAssociatorAtVertex, process.akCs4PFJets, process.combinedSecondaryVertexV2BJetTags, process.hiFJRhoFlowModulation, process.hiPuRho, process.highPurityGeneralTracks, process.impactParameterTagInfos, process.jetBProbabilityBJetTags, process.jetProbabilityBJetTags, process.patJetCorrFactors, process.pfEmptyCollection, process.pfNoPileUpJMETask, process.secondaryVertexTagInfos, process.simpleSecondaryVertexHighEffBJetTags, process.simpleSecondaryVertexHighPurBJetTags, process.trackCountingHighEffBJetTags, process.trackCountingHighPurBJetTags)


process.selectedPatCandidatesTask = cms.Task(process.selectedPatElectrons, process.selectedPatJets, process.selectedPatMuons, process.selectedPatPhotons, process.selectedPatTaus)


process.updateHPSPFTausTask = cms.Task(process.hpsPFTauBasicDiscriminators)


process.ak4JPTL1FastL2L3CorrectorTask = cms.Task(process.ak4JPTL1FastL2L3Corrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4L1JPTFastjetCorrectorTask)


process.ak4JPTL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4JPTL1FastL2L3ResidualCorrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4JPTResidualCorrector, process.ak4L1JPTFastjetCorrectorTask)


process.ak4JPTL1L2L3CorrectorTask = cms.Task(process.ak4JPTL1L2L3Corrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4L1JPTOffsetCorrectorTask)


process.ak4JPTL1L2L3ResidualCorrectorTask = cms.Task(process.ak4JPTL1L2L3ResidualCorrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4JPTResidualCorrector, process.ak4L1JPTOffsetCorrectorTask)


process.ak4JPTL2L3CorrectorTask = cms.Task(process.ak4JPTL2L3Corrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4L1JPTOffsetCorrectorTask)


process.ak4JPTL2L3ResidualCorrectorTask = cms.Task(process.ak4JPTL2L3ResidualCorrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4JPTResidualCorrector, process.ak4L1JPTOffsetCorrectorTask)


process.jetCorrectorsTask = cms.Task(process.ak4CaloL1FastL2L3CorrectorTask, process.ak4CaloL1FastL2L3L6CorrectorTask, process.ak4CaloL1FastL2L3ResidualCorrectorTask, process.ak4CaloL1L2L3CorrectorTask, process.ak4CaloL1L2L3ResidualCorrectorTask, process.ak4CaloL2L3CorrectorTask, process.ak4CaloL2L3L6CorrectorTask, process.ak4CaloL2L3ResidualCorrectorTask, process.ak4JPTL1FastL2L3CorrectorTask, process.ak4JPTL1FastL2L3ResidualCorrectorTask, process.ak4JPTL1L2L3CorrectorTask, process.ak4JPTL1L2L3ResidualCorrectorTask, process.ak4JPTL2L3CorrectorTask, process.ak4JPTL2L3ResidualCorrectorTask, process.ak4L1JPTFastjetCorrectorTask, process.ak4L1JPTOffsetCorrectorTask, process.ak4PFCHSL1FastL2L3CorrectorTask, process.ak4PFCHSL1FastL2L3ResidualCorrectorTask, process.ak4PFCHSL1L2L3CorrectorTask, process.ak4PFCHSL1L2L3ResidualCorrectorTask, process.ak4PFCHSL2L3CorrectorTask, process.ak4PFCHSL2L3ResidualCorrectorTask, process.ak4PFL1FastL2L3CorrectorTask, process.ak4PFL1FastL2L3L6CorrectorTask, process.ak4PFL1FastL2L3ResidualCorrectorTask, process.ak4PFL1L2L3CorrectorTask, process.ak4PFL1L2L3ResidualCorrectorTask, process.ak4PFL2L3CorrectorTask, process.ak4PFL2L3L6CorrectorTask, process.ak4PFL2L3ResidualCorrectorTask, process.ak4PFPuppiL1FastL2L3CorrectorTask, process.ak4PFPuppiL1FastL2L3ResidualCorrectorTask, process.ak4PFPuppiL1L2L3CorrectorTask, process.ak4PFPuppiL1L2L3ResidualCorrectorTask, process.ak4PFPuppiL2L3CorrectorTask, process.ak4PFPuppiL2L3ResidualCorrectorTask, process.ak4TrackL2L3CorrectorTask)


process.makePatJetsTask = cms.Task(process.patJetCharge, process.patJetCorrectionsTask, process.patJetFlavourIdLegacyTask, process.patJetFlavourIdTask, process.patJetGenJetMatch, process.patJetPartonMatch, process.patJets, process.recoGenJetsHIpostAODTask, process.recoPFJetsHIpostAODTask)


process.makePatMETsTask = cms.Task(process.patMETCorrectionsTask, process.patMETs)


process.muonPFIsolationPATTask = cms.Task(process.muonPFIsolationDepositsPATTask, process.muonPFIsolationValuesPATTask)


process.patHPSPFTauDiscriminationTask = cms.Task(process.updateHPSPFTausTask)


process.patPFCandidateIsoDepositSelectionTask = cms.Task(process.pfNoPileUpIsoPFBRECOTask, process.pfSortByTypePFBRECOTask)


process.pfParticleSelectionPFBRECOTask = cms.Task(process.pfNoPileUpIsoPFBRECOTask, process.pfNoPileUpPFBRECOTask, process.pfSortByTypePFBRECOTask)


process.pfPhotonIsolationPATTask = cms.Task(process.photonPFIsolationDepositsPATTask, process.photonPFIsolationValuesPATTask)


process.makePatTausTask = cms.Task(process.patPFCandidateIsoDepositSelectionTask, process.patPFTauIsolationTask, process.patTaus, process.tauGenJetMatch, process.tauGenJets, process.tauGenJetsSelectorAllHadrons, process.tauMatch)


process.pfParticleSelectionForIsoTask = cms.Task(process.particleFlowPtrs, process.pfParticleSelectionPFBRECOTask)


process.makePatElectronsTask = cms.Task(process.electronMatch, process.patElectrons, process.pfElectronIsolationPATTask, process.pfParticleSelectionForIsoTask)


process.makePatMuonsTask = cms.Task(process.muonMatch, process.muonPFIsolationPATTask, process.patMuons, process.pfParticleSelectionForIsoTask)


process.makePatPhotonsTask = cms.Task(process.patPhotons, process.pfParticleSelectionForIsoTask, process.pfPhotonIsolationPATTask, process.photonMatch)


process.patCandidatesTask = cms.Task(process.makePatElectronsTask, process.makePatJetsTask, process.makePatMETsTask, process.makePatMuonsTask, process.makePatPhotonsTask, process.makePatTausTask)


process.trackSequencePP = cms.Sequence(process.unpackedTracksAndVertices+process.ppTracks)


process.trackSequencePbPb = cms.Sequence(process.unpackedTracksAndVertices+process.PbPbTracks)


process.extraFlowJetsData = cms.Sequence(process.PackedPFTowers+process.hiPuRho+process.ak4PFJetsForFlow+process.hiFJRhoFlowModulation)


process.extraFlowJetsMC = cms.Sequence(process.PackedPFTowers+process.hiPuRho+process.hiSignalGenParticles+process.allPartons+process.ak4PFJetsForFlow+process.hiFJRhoFlowModulation)


process.extraJetsData = cms.Sequence(process.PackedPFTowers+process.hiPuRho)


process.extraJetsMC = cms.Sequence(process.PackedPFTowers+process.hiPuRho+process.hiSignalGenParticles+process.allPartons)


process.candidateBtagging = cms.Sequence(process.pfImpactParameterTagInfos+process.pfSecondaryVertexTagInfos+process.pfJetProbabilityBJetTags+process.pfDeepCSVTagInfos+process.pfDeepCSVJetTags)


process.jetsR2 = cms.Sequence(process.akCs2PFJets+process.akCs2PFpatJetCorrFactors+process.akCs2PFpfImpactParameterTagInfos+process.akCs2PFpfSecondaryVertexTagInfos+process.akCs2PFpfDeepCSVTagInfos+process.akCs2PFpfDeepCSVJetTags+process.akCs2PFpfJetProbabilityBJetTags+process.akCs2PFpatJets)


process.jetsR4 = cms.Sequence(process.akCs0PFJets+process.akCs0PFpatJetCorrFactors+process.akCs0PFpfImpactParameterTagInfos+process.akCs0PFpfSecondaryVertexTagInfos+process.akCs0PFpfDeepCSVTagInfos+process.akCs0PFpfDeepCSVJetTags+process.akCs0PFpfJetProbabilityBJetTags+process.akCs0PFpatJets)


process.ak4CaloL1FastL2L3CorrectorChain = cms.Sequence(process.ak4CaloL1FastL2L3CorrectorTask)


process.ak4CaloL1FastL2L3L6CorrectorChain = cms.Sequence(process.ak4CaloL1FastL2L3L6CorrectorTask)


process.ak4CaloL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL1FastL2L3ResidualCorrectorTask)


process.ak4CaloL1L2L3CorrectorChain = cms.Sequence(process.ak4CaloL1L2L3CorrectorTask)


process.ak4CaloL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL1L2L3ResidualCorrectorTask)


process.ak4CaloL2L3CorrectorChain = cms.Sequence(process.ak4CaloL2L3CorrectorTask)


process.ak4CaloL2L3L6CorrectorChain = cms.Sequence(process.ak4CaloL2L3L6CorrectorTask)


process.ak4CaloL2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL2L3ResidualCorrectorTask)


process.ak4JPTL1FastL2L3CorrectorChain = cms.Sequence(process.ak4JPTL1FastL2L3CorrectorTask)


process.ak4JPTL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4JPTL1FastL2L3ResidualCorrectorTask)


process.ak4JPTL1L2L3CorrectorChain = cms.Sequence(process.ak4JPTL1L2L3CorrectorTask)


process.ak4JPTL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4JPTL1L2L3ResidualCorrectorTask)


process.ak4JPTL2L3CorrectorChain = cms.Sequence(process.ak4JPTL2L3CorrectorTask)


process.ak4JPTL2L3ResidualCorrectorChain = cms.Sequence(process.ak4JPTL2L3ResidualCorrectorTask)


process.ak4L1JPTFastjetCorrectorChain = cms.Sequence(process.ak4L1JPTFastjetCorrectorTask)


process.ak4L1JPTOffsetCorrectorChain = cms.Sequence(process.ak4L1JPTOffsetCorrectorTask)


process.ak4PFCHSL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL1FastL2L3CorrectorTask)


process.ak4PFCHSL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL1FastL2L3ResidualCorrectorTask)


process.ak4PFCHSL1L2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL1L2L3CorrectorTask)


process.ak4PFCHSL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL1L2L3ResidualCorrectorTask)


process.ak4PFCHSL2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL2L3CorrectorTask)


process.ak4PFCHSL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL2L3ResidualCorrectorTask)


process.ak4PFL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFL1FastL2L3CorrectorTask)


process.ak4PFL1FastL2L3L6CorrectorChain = cms.Sequence(process.ak4PFL1FastL2L3L6CorrectorTask)


process.ak4PFL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL1FastL2L3ResidualCorrectorTask)


process.ak4PFL1L2L3CorrectorChain = cms.Sequence(process.ak4PFL1L2L3CorrectorTask)


process.ak4PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL1L2L3ResidualCorrectorTask)


process.ak4PFL2L3CorrectorChain = cms.Sequence(process.ak4PFL2L3CorrectorTask)


process.ak4PFL2L3L6CorrectorChain = cms.Sequence(process.ak4PFL2L3L6CorrectorTask)


process.ak4PFL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL2L3ResidualCorrectorTask)


process.ak4PFPuppiL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL1FastL2L3CorrectorTask)


process.ak4PFPuppiL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL1FastL2L3ResidualCorrectorTask)


process.ak4PFPuppiL1L2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL1L2L3CorrectorTask)


process.ak4PFPuppiL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL1L2L3ResidualCorrectorTask)


process.ak4PFPuppiL2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL2L3CorrectorTask)


process.ak4PFPuppiL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL2L3ResidualCorrectorTask)


process.ak4TrackL2L3CorrectorChain = cms.Sequence(process.ak4TrackL2L3CorrectorTask)


process.ak5JTA = cms.Sequence(process.ak5JTATask)


process.ak5JTAExplicit = cms.Sequence(process.ak5JTAExplicitTask)


process.cleanPatCandidates = cms.Sequence(process.cleanPatCandidateSummary, process.cleanPatCandidatesTask)


process.correctionTermsCaloMet = cms.Sequence(process.correctionTermsCaloMetTask)


process.correctionTermsPfMetType1Type2 = cms.Sequence(process.correctionTermsPfMetType1Type2Task)


process.countPatCandidates = cms.Sequence(process.countPatElectrons+process.countPatMuons+process.countPatTaus+process.countPatLeptons+process.countPatPhotons+process.countPatJets)


process.electronPFIsolationDepositsPATSequence = cms.Sequence(process.electronPFIsolationDepositsPATTask)


process.electronPFIsolationValuesPATSequence = cms.Sequence(process.electronPFIsolationValuesPATTask)


process.makePatDisplacedMuons = cms.Sequence(process.makePatDisplacedMuonsTask)


process.makePatElectrons = cms.Sequence(process.makePatElectronsTask)


process.makePatJets = cms.Sequence(process.makePatJetsTask)


process.makePatLowPtElectrons = cms.Sequence(process.makePatLowPtElectronsTask)


process.makePatMETs = cms.Sequence(process.makePatMETsTask)


process.makePatMuons = cms.Sequence(process.makePatMuonsTask)


process.makePatOOTPhotons = cms.Sequence(process.makePatOOTPhotonsTask)


process.makePatPhotons = cms.Sequence(process.makePatPhotonsTask)


process.makePatTaus = cms.Sequence(process.makePatTausTask)


process.muonPFIsolationDepositsPATSequence = cms.Sequence(process.muonPFIsolationDepositsPATTask)


process.muonPFIsolationPATSequence = cms.Sequence(process.muonPFIsolationPATTask)


process.muonPFIsolationValuesPATSequence = cms.Sequence(process.muonPFIsolationValuesPATTask)


process.ootPhotonSequence = cms.Sequence(process.ootPhotonTask)


process.patCandidates = cms.Sequence(process.patCandidateSummary, process.patCandidatesTask)


process.patFixedConePFTauDiscrimination = cms.Sequence()


process.patHPSPFTauDiscrimination = cms.Sequence(process.patHPSPFTauDiscriminationTask)


process.patJetCorrections = cms.Sequence(process.patJetCorrectionsTask)


process.patJetFlavourId = cms.Sequence(process.patJetFlavourIdTask)


process.patJetFlavourIdLegacy = cms.Sequence(process.patJetFlavourIdLegacyTask)


process.patMETCorrections = cms.Sequence(process.patMETCorrectionsTask)


process.patPFCandidateIsoDepositSelection = cms.Sequence(process.patPFCandidateIsoDepositSelectionTask)


process.patPFTauIsolation = cms.Sequence(process.patPFTauIsolationTask)


process.patShrinkingConePFTauDiscrimination = cms.Sequence()


process.pfDeepCSV = cms.Sequence(process.pfDeepCSVTask)


process.pfElectronIsolationPATSequence = cms.Sequence(process.pfElectronIsolationPATTask)


process.pfNoPileUpIsoPFBRECOSequence = cms.Sequence(process.pfNoPileUpIsoPFBRECOTask)


process.pfNoPileUpJMESequence = cms.Sequence(process.pfNoPileUpJMETask)


process.pfNoPileUpPFBRECOSequence = cms.Sequence(process.pfNoPileUpPFBRECOTask)


process.pfParticleSelectionForIsoSequence = cms.Sequence(process.pfParticleSelectionForIsoTask)


process.pfParticleSelectionPFBRECOSequence = cms.Sequence(process.pfParticleSelectionPFBRECOTask)


process.pfPhotonIsolationPATSequence = cms.Sequence(process.pfPhotonIsolationPATTask)


process.pfSortByTypePFBRECOSequence = cms.Sequence(process.pfSortByTypePFBRECOTask)


process.photonPFIsolationDepositsPATSequence = cms.Sequence(process.photonPFIsolationDepositsPATTask)


process.photonPFIsolationValuesPATSequence = cms.Sequence(process.photonPFIsolationValuesPATTask)


process.selectedPatCandidates = cms.Sequence(process.selectedPatCandidateSummary, process.selectedPatCandidatesTask)


process.updateHPSPFTaus = cms.Sequence(process.updateHPSPFTausTask)


process.patTriggerMatchers1Mu = cms.Sequence(process.muonMatchHLTL2+process.muonMatchHLTL3+process.muonMatchHLTL3T+process.muonMatchHLTL3fromL2+process.muonMatchHLTTkMu)


process.patTriggerMatchers2Mu = cms.Sequence(process.muonMatchHLTCtfTrack+process.muonMatchHLTCtfTrack2+process.muonMatchHLTTrackMu+process.muonMatchHLTTrackIt)


process.patTriggerMatching = cms.Sequence(process.patTriggerFull+process.patTrigger+process.patTriggerMatchers1Mu+process.patTriggerMatchers2Mu+process.patMuonsWithTrigger)


process.DfinderSequence = cms.Sequence(process.Dfinder)


process.patDefaultSequence = cms.Sequence(process.patCandidates+process.selectedPatCandidates+process.cleanPatCandidates+process.countPatCandidates)


process.patMuonsWithTriggerSequence = cms.Sequence(process.muonL1Info+process.patMuonsWithoutTrigger+process.patTriggerFull+process.patTrigger+process.muonMatchHLTL2+process.muonMatchHLTL1+process.muonMatchHLTL3+process.muonMatchHLTL3T+process.muonMatchHLTL3fromL2+process.muonMatchHLTTkMu+process.patTriggerMatchers2Mu+process.patMuonsWithTrigger)


process.patMuonSequence = cms.Sequence(process.patMuonsWithTriggerSequence)


process.BfinderSequence = cms.Sequence(process.patMuonSequence+process.Bfinder)


process.finderSequence = cms.Sequence(process.patMuonSequence+process.Bfinder+process.Dfinder)


process.forest = cms.Path(process.pfCandComposites+process.pfCandComposites+process.HiForestInfo+process.hiEvtAnalyzer+process.hltanalysis+process.extraJetsData+process.jetsR2+process.akCs2PFJetAnalyzer+process.extraJetsData+process.jetsR4+process.akCs4PFJetAnalyzer)


process.pclusterCompatibilityFilter = cms.Path(process.clusterCompatibilityFilter)


process.pprimaryVertexFilter = cms.Path(process.primaryVertexFilter)


process.pphfCoincFilter2Th4 = cms.Path(process.phfCoincFilter2Th4)


process.dfinder = cms.Path(process.DfinderSequence)


process.pAna = cms.EndPath(process.skimanalysis)


