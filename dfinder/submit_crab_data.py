from CRABClient.UserUtilities import config
config = config()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'Run2_DATA_FullParticles_Aggregation_LeadingD' #Nome del task di crab

config.section_('JobType')
config.JobType.psetName = 'forest_miniAOD_run2_DATA_wDfinder.py' #Configuration file che runno con cmsRun
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['HiForestMiniAOD_FullParticles_DATA_Dfinder.root'] #Output file nel file che runno .py
# config.JobType.maxMemoryMB = 2000
config.JobType.maxMemoryMB = 5000

config.section_('Data')
config.Data.inputDataset = '/HIHardProbes/HIRun2018A-PbPb18_MiniAODv1-v1/MINIAOD'
# config.Data.inputBlocks = ['/DiJet_pThat-15_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8/HINPbPbSpring21MiniAOD-FixL1CaloGT_New_Release_112X_upgrade2018_realistic_HI_v9-v1/MINIAODSIM#82022616-3127-422e-a0e0-24ba28e93eab'] 
config.Data.publication = False
# config.Data.runRange = '306773-306793'
# config.Data.totalUnits = -1
# config.Data.splitting = 'FileBased'
# config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.unitsPerJob = 30000
config.Data.splitting = 'EventAwareLumiBased'
config.Data.outLFNDirBase = '/store/user/lfrosina/Run2_dfinder_DATA_FullParticles_aggregation_LeadingD'
# config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/5TeV/ReReco/Cert_306546-306826_5TeV_EOY2017ReReco_Collisions17_JSON.txt'

config.section_('Site')
config.Site.storageSite = 'T2_IT_Rome'
print(config)
