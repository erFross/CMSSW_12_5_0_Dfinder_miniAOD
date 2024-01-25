from CRABClient.UserUtilities import config
config = config()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'Run2_MC_SD_FullParticles_REAL_ParticlePtCut1Gev_wDFinder'

config.section_('JobType')
config.JobType.psetName = 'forest_miniAOD_run2_MC_wDfinder.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['HiForestMiniAOD_FullParticles_embedded_SD_ParticleJetCut1Gev.root']
# config.JobType.maxMemoryMB = 2000
config.JobType.maxMemoryMB = 5000


config.section_('Data')
config.Data.inputDataset = '/DiJet_pThat-15_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8/HINPbPbSpring21MiniAOD-FixL1CaloGT_New_Release_112X_upgrade2018_realistic_HI_v9-v1/MINIAODSIM'
# config.Data.inputDataset = '/MinBias_Hydjet_Drum5F_2018_5p02TeV/HINPbPbSpring21MiniAOD-NoPUmva98_112X_upgrade2018_realistic_HI_v9-v1/MINIAODSIM' 
config.Data.publication = False
# config.Data.runRange = '306773-306793'
# config.Data.totalUnits = -1
# config.Data.splitting = 'FileBased'
# config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.unitsPerJob = 30000
config.Data.splitting = 'EventAwareLumiBased'
config.Data.outLFNDirBase = '/store/user/lfrosina/Run2_Dfinder_embedded_SD_FullParticles_REAL_ParticlePtCut1Gev'
# config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/5TeV/ReReco/Cert_306546-306826_5TeV_EOY2017ReReco_Collisions17_JSON.txt'

config.section_('Site')
config.Site.storageSite = 'T2_IT_Rome'
print(config)
