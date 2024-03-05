/*
Identify sf & lf pairs from free text using multi-stage algorithm
process one line at a time and print out:
line
  sf|lf|P-precision|strategy
*/

#include "AbbrStra.h"
#include "AbbrvE.h"
#include <map>
#include <string>
#include <vector>

using namespace std;
using namespace iret;

namespace iret {

class AbbrOut {
public:
  string sf, lf, strat;
  int sf_offset, lf_offset;
  double prec;

  AbbrOut(void) : sf(""), lf(""), strat(""), prec(0) {}

  void print(ostream &out) { out << "  " << sf << "|" << lf << "|" << prec; }
};

class Ab3P {
public:
  Ab3P(void);
  ~Ab3P(void) { delete wrdData; }

  std::vector<AbbrOut> get_abbrs(char *text);

  /**  Try a potential sf-lf form to find proper lf, strategy used,
       and pseudo-precision of result **/
  void try_pair(const Pot_Abbr &abb, AbbrOut &abbr);

  /**
     psf -- pointer short form
     plf -- pointer long form
  **/
  void try_strats(const char *psf, const char *plf, bool swap, AbbrOut &result);
  void try_strats_pot_abbr(const Pot_Abbr &abb, bool swap, AbbrOut &result);

  AbbrvE ab; // default # pairs = 10,000
  map<string, double> stratPrec;
  StratUtil util;
  WordData *wrdData; // set data needed for AbbrStra
};

} // namespace iret
