#include "CondCore/PopCon/interface/PopConAnalyzer.h"
#include "CondTools/Ecal/interface/EcalTPGOddWeightGroupHandler.h"
#include "FWCore/Framework/interface/MakerMacros.h"

typedef popcon::PopConAnalyzer<popcon::EcalTPGOddWeightGroupHandler> ExTestEcalTPGOddWeightGroupAnalyzer;

//define this as a plug-in
DEFINE_FWK_MODULE(ExTestEcalTPGOddWeightGroupAnalyzer);
