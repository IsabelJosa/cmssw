
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras

# creating quadruplet SeedingLayerSets for the merger;
PixelSeedMergerQuadruplets = cms.PSet(
  appendToDataLabel = cms.string( "" ),

  # this simply describes all possible layer/disk combinations
  # on which quadruplets are expected to appear
  layerList = cms.vstring(
    ## straightforward combinations:
    'BPix1+BPix2+BPix3+BPix4',
    'BPix1+BPix2+BPix3+FPix1_pos',
    'BPix1+BPix2+BPix3+FPix1_neg',
    'BPix1+BPix2+FPix1_pos+FPix2_pos',
    'BPix1+BPix2+FPix1_neg+FPix2_neg',
    'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
    'BPix1+FPix1_neg+FPix2_neg+FPix3_neg'
#    ## "gap" combinations:
#    'BPix2+FPix1_pos+FPix2_pos+FPix3_pos',
#    'BPix2+FPix1_neg+FPix2_neg+FPix3_neg',
#    'BPix1+BPix2+FPix2_pos+FPix3_pos',
#    'BPix1+BPix2+FPix2_neg+FPix3_neg',
#    'BPix1+BPix2+FPix1_pos+FPix3_pos',
#    'BPix1+BPix2+FPix1_neg+FPix3_neg'
  ),

  BPix = cms.PSet( 
    TTRHBuilder = cms.string( "PixelTTRHBuilderWithoutAngle" ),
    HitProducer = cms.string( "siPixelRecHits" ),
  ),
  FPix = cms.PSet( 
    TTRHBuilder = cms.string( "PixelTTRHBuilderWithoutAngle" ),
    HitProducer = cms.string( "siPixelRecHits" ),
  ),
  TEC = cms.PSet(  )
)

_layerListForPhase2 = ['BPix1+BPix2+BPix3+BPix4',
                       'BPix1+BPix2+BPix3+FPix1_pos','BPix1+BPix2+BPix3+FPix1_neg',
                       'BPix1+BPix2+FPix1_pos+FPix2_pos', 'BPix1+BPix2+FPix1_neg+FPix2_neg',
                       'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 'BPix1+FPix1_neg+FPix2_neg+FPix3_neg',
                       'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg',
                       'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg',
                       'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_pos',
                       'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg',
                       'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg',
                       'FPix5_pos+FPix6_pos+FPix7_pos+FPix9_pos', 'FPix5_neg+FPix6_neg+FPix7_neg+FPix9_neg',
                       'FPix6_pos+FPix7_pos+FPix8_pos+FPix9_pos', 'FPix6_neg+FPix7_neg+FPix8_neg+FPix9_neg']

# Needed to have pixelTracks to not to look like depending
# siPixelRecHits (that is inserted in reco sequences in
# InitialStepPreSplitting). The quadruplet merger does not use these
# hit collections (it uses the hits of the triplets), so this is only
# to make framework's circular dependency checker happy.
_forPhase1 = dict(
    BPix = dict(HitProducer = "siPixelRecHitsPreSplitting"),
    FPix = dict(HitProducer = "siPixelRecHitsPreSplitting"),
)
eras.trackingPhase1.toModify(PixelSeedMergerQuadruplets, **_forPhase1)
eras.trackingPhase1PU70.toModify(PixelSeedMergerQuadruplets, **_forPhase1)
eras.trackingPhase2PU140.toModify(PixelSeedMergerQuadruplets, layerList = _layerListForPhase2)
