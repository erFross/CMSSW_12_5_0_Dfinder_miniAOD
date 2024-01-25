// -*- C++ -*-
//
// Package:    PFCandCompositeProducer
// Class:      PFCandCompositeProducer
// 
/**\class PFCandCompositeProducer PFCandCompositeProducer RecoHI/PFCandCompositeProducer/src/PFCandCompositeProducer

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Yetkin Yilmaz,32 4-A08,+41227673039,
//         Created:  Thu Jan 20 19:53:58 CET 2011
//
//


// system include files
#include <memory>


// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/Framework/interface/ESHandle.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "RecoHI/HiJetAlgos/plugins/PFCandCompositeProducer.h"

#include "DataFormats/HcalDetId/interface/HcalDetId.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/GenericParticle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

#include "TMath.h"

#include "DataFormats/Candidate/interface/ShallowCloneCandidate.h"

#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"


//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
PFCandCompositeProducer::PFCandCompositeProducer(const edm::ParameterSet& iConfig)
{
  //register your products  
  pfCandToken_ = consumes<pat::PackedCandidateCollection>(iConfig.getParameter<edm::InputTag>("pfCandTag"));
  compositeToken_ = consumes<pat::CompositeCandidateCollection>(iConfig.getParameter<edm::InputTag>("compositeTag"));
  jpsiTriggFilter_ = iConfig.getParameter<std::string>("jpsiTrigFilter");
  isHI_ = iConfig.getParameter<bool>("isHI");
  removeJMM_ = iConfig.getParameter<bool>("removeJMM");
  removeDKPi_ = iConfig.getParameter<bool>("removeDKPi");
  
  produces<pat::PackedCandidateCollection>();

  if(!removeJMM_ && !removeDKPi_) std::cout<<" PFCandCompositeProducer ain't doing jack "<<std::endl;
  if(removeJMM_ && removeDKPi_) std::cout<<" removing multiple species not yet supported "<<std::endl;

}


PFCandCompositeProducer::~PFCandCompositeProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
PFCandCompositeProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;

    edm::Handle<pat::CompositeCandidateCollection> composites;
    iEvent.getByToken(compositeToken_, composites);

    if (not composites.isValid()) {
        std::cout << "Warning: no composite candidates ..." << std::endl;
        return;
    }

    auto nComp = composites->size();  
    std::vector<pat::CompositeCandidate> selComposites;
    auto prod = std::make_unique<pat::PackedCandidateCollection>();


    if(nComp>0){
 
        //edm::Handle<reco::PFCandidateCollection> pfCands;
        edm::Handle<pat::PackedCandidateCollection> pfCands;
        iEvent.getByToken(pfCandToken_, pfCands);

        prod->reserve(pfCands->size());
        //first pass over composite candidates, apply selections and check for presence in PF candidates 

        //std::cout<<"Prima della selezione -cand- "<<std::endl;

        for (std::vector<pat::CompositeCandidate>::const_iterator it=composites->begin(); it!=composites->end(); ++it) {

            const pat::CompositeCandidate cand = *it;

            //std::cout<<" pt = "<<cand.pt()<<" mass = "<<cand.mass()<<std::endl;

            if(removeDKPi_){  // only selection is pt > 3 GeV for now
              
	            if( seld0Cand(cand) ){	 
	                bool isDup = false;
	                for(unsigned i=0;i<selComposites.size();i++){
	                    if(checkDupTrack(cand,selComposites[i])) isDup = true;
	                }                

	                if(isDup) continue;
	   
	                selComposites.push_back(cand);
                    double candE = sqrt(cand.p()*cand.p() + 1.86484*1.86484);

                    pat::PackedCandidate::LorentzVector p4(cand.px(),cand.py(),cand.pz(),candE);
   	                //reco::PFCandidate newPFCand(0,p4,reco::PFCandidate::ParticleType::h_HF);
   	                pat::PackedCandidate::Point v(0.01, 0.02, 0.);
   	                pat::PackedCandidate newPFCand (p4, v, 1., 1., 1., 11, reco::VertexRefProd(), reco::VertexRef().key()); //check
	                
                    prod->push_back(newPFCand);   
	            }
            }
       
        }
        /*std::cout<<"Dopo la selezione -selComposites- "<<std::endl;
        for (size_t i=0; i<selComposites.size(); i++) {
            std::cout<<" pt = "<<selComposites[i].pt()<<" mass = "<<selComposites[i].mass()<<std::endl;
        }*/
        
     
        int replacedCands = 0;
      
        // now loop over PF candidates and remove ones that are part of composites
        //for(reco::PFCandidateCollection::const_iterator ci  = pfCands->begin(); ci!=pfCands->end(); ++ci)  {
        for(pat::PackedCandidateCollection::const_iterator ci  = pfCands->begin(); ci!=pfCands->end(); ++ci)  {

            //std::cout<<"pfcand.mass() = "<< (*ci).mass()<<std::endl;

            const pat::PackedCandidate& particle = *ci;
       
            //reco::PFCandidate pfOut = *particle.clone();
      
            bool writeCand = true;

            //if(particle.trackRef().isNonnull()){
            if (particle.hasTrackDetails()) {
                const reco::Track pfTrack = particle.pseudoTrack();	 
	           //reco::TrackRef pfTrack = particle.trackRef();
	 
                double pfPt = pfTrack.pt();
                double pfEta = pfTrack.eta();
                double pfPhi = pfTrack.phi();
	 
	 
                for(std::vector<pat::CompositeCandidate>::const_iterator it=selComposites.begin(); it!=selComposites.end(); ++it) {	   
	   
                    const pat::CompositeCandidate cand = *it;
                    double eps = 0.0001;                                                                                                                                                   
                    if(removeDKPi_){
	     
                        double dau1Pt = cand.daughter("track1")->pt();
                        double dau1Eta = cand.daughter("track1")->eta();
                        double dau1Phi = cand.daughter("track1")->phi();
	     
                        double dau2Pt = cand.daughter("track2")->pt();
                        double dau2Eta = cand.daughter("track2")->eta();
                        double dau2Phi = cand.daughter("track2")->phi();

                        if((fabs(dau1Pt-pfPt) < eps && fabs(dau1Eta-pfEta) < eps  && fabs(dau1Phi-pfPhi) < eps) ||
                            (fabs(dau2Pt-pfPt) < eps && fabs(dau2Eta-pfEta) < eps  && fabs(dau2Phi-pfPhi) < eps)) {
	                        writeCand= false;
                            replacedCands++;                                                                                                                                                 
                        }
    	            }
	            }

            }

            if(writeCand) prod->push_back(*ci);
        }
    }

    iEvent.put(std::move(prod));

   
}

// ------------ method called once each job just before starting event loop  ------------
void 
PFCandCompositeProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PFCandCompositeProducer::endJob() {
}


bool
PFCandCompositeProducer::seld0Cand(const pat::CompositeCandidate d0Cand){
  if(d0Cand.pt() < 3.) return false;
  return true;
}

bool
PFCandCompositeProducer::selJpsiCand(const pat::CompositeCandidate jpsiCand){
  //std::cout<<" jpsi cand pt "<<jpsiCand.pt()<<" mass "<<jpsiCand.mass()<< " eta "<<jpsiCand.eta()<< " phi "<< jpsiCand.phi()<<std::endl;
  if(jpsiCand.pt() < 3.) return false;
  if(jpsiCand.mass() < 2.6) return false;
  if(jpsiCand.mass() > 3.5) return false;
  if(jpsiCand.userFloat("vProb") < 0.01) return false; 
  if(fabs(jpsiCand.rapidity()) > 2.4) return false;
  if(fabs(jpsiCand.rapidity()) < 1.6 && jpsiCand.pt() < 6.) return false;

  const pat::Muon *muon1 = dynamic_cast< const pat::Muon* >(jpsiCand.daughter("muon1") );
  const pat::Muon* muon2 = dynamic_cast< const pat::Muon* >(jpsiCand.daughter("muon2") );
  
  if(muon1->charge() == muon2->charge()) return false;

  //std::cout<<" selected Jpsi "<<std::endl;

  return true;
}

bool
PFCandCompositeProducer::selMuonCand(const pat::CompositeCandidate jpsiCand, const char* muonName){
  //std::cout<<" muonName "<<muonName<<std::endl;
  const pat::Muon* muon = dynamic_cast<const pat::Muon*>(jpsiCand.daughter(muonName));

  if(!muon::isGoodMuon(*muon, muon::TMOneStationTight)) return false;
  if(!muon->isTrackerMuon()) return false;
  math::XYZPoint RefVtx;
  if (isHI_) RefVtx = (*jpsiCand.userData<reco::Vertex>("PVwithmuons")).position();
  else RefVtx = (*jpsiCand.userData<reco::Vertex>("muonlessPV")).position();
  
  reco::TrackRef iTrack = muon->innerTrack();
  if(fabs(iTrack->dz(RefVtx)) > 20) return false;
  if(fabs(iTrack->dxy(RefVtx)) > 0.3) return false;
  if(iTrack->hitPattern().trackerLayersWithMeasurement() < 6) return false;
  if(iTrack->hitPattern().pixelLayersWithMeasurement() < 1) return false;


  const pat::TriggerObjectStandAloneCollection muHLTMatchesFilter = muon->triggerObjectMatchesByFilter(jpsiTriggFilter_);  
  bool isTriggerMatched = muHLTMatchesFilter.size() > 0;  
  if(!isTriggerMatched) return false;

  bool isGlobalMuon = muon->isGlobalMuon();

  if(!isGlobalMuon) return false;
  double eta = muon->eta();
  double pt = muon->pt();
  bool isMuonInAcc = (fabs(eta) < 2.4 && ((fabs(eta) < 1.2 && pt >= 3.5) ||
                     (1.2 <= fabs(eta) && fabs(eta) < 2.1 && pt >= 5.77-1.89*fabs(eta)) ||
                     (2.1 <= fabs(eta) && pt >= 1.8)));
  
  if(!isMuonInAcc) return false;
  //std::cout<<" selected muon "<<std::endl;
  return true;
}

bool
PFCandCompositeProducer::checkDupTrack(const pat::CompositeCandidate cand1, const pat::CompositeCandidate cand2){
  
  double eps = 0.0001;
  if(fabs(cand1.daughter("track1")->pt() - cand2.daughter("track1")->pt() ) < eps) return true;
  if(fabs(cand1.daughter("track1")->pt() - cand2.daughter("track2")->pt() ) < eps) return true;
  if(fabs(cand1.daughter("track2")->pt() - cand2.daughter("track1")->pt() ) < eps) return true;
  if(fabs(cand1.daughter("track2")->pt() - cand2.daughter("track2")->pt() ) < eps) return true;

  return false;
}


bool
PFCandCompositeProducer::checkDupMuon(const pat::CompositeCandidate cand1, const pat::CompositeCandidate cand2){
  
  double eps = 0.0001;
  if(fabs(cand1.daughter("muon1")->pt() - cand2.daughter("muon1")->pt() ) < eps) return true;
  if(fabs(cand1.daughter("muon1")->pt() - cand2.daughter("muon2")->pt() ) < eps) return true;
  if(fabs(cand1.daughter("muon2")->pt() - cand2.daughter("muon1")->pt() ) < eps) return true;
  if(fabs(cand1.daughter("muon2")->pt() - cand2.daughter("muon2")->pt() ) < eps) return true;

  return false;
}

    //define this as a plug-in
DEFINE_FWK_MODULE(PFCandCompositeProducer);
