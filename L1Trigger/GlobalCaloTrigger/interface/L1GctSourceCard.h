#ifndef L1GCTSOURCECARD_H_
#define L1GCTSOURCECARD_H_

#include "L1Trigger/GlobalCaloTrigger/interface/L1GctEmCand.h"
#include "L1Trigger/GlobalCaloTrigger/interface/L1GctRegion.h"
#include "L1Trigger/GlobalCaloTrigger/interface/L1GctFileRW.h"

#include <vector>
#include <bitset>

using std::vector;
using std::bitset;

class L1RctCrate;

/**
  * Represents a GCT Source Card
  * author: Jim Brooke
  * date: 20/2/2006
  * 
  **/

class L1GctSourceCard
{
public:
  L1GctSourceCard(); //(L1RctCrate* rc);
  ~L1GctSourceCard();
  
  ///
  ///

  void process();
  
  vector<L1GctEmCand> getIsoElectrons();
  vector<L1GctEmCand> getNonIsoElectrons();
  vector<L1GctRegion> getRegions();
  bitset<14> getMipBits();
  bitset<14> getQuietBits();

  friend class L1GctFileRW;

private:

	// need a pointer to the RCT crate...
	L1RctCrate* rctCrate;
	
};

#endif /*L1GCTSOURCECARD_H_*/
