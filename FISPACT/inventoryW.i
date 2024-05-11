<< -----set initial switches and get nuclear data----- >>
CLOBBER
GETXS 0
GETDECAY 0
FISPACT
* FNS 1000 days pure Tungsten
DENSITY 19.3
MASS 1.0E-3 1
W 100
MIND 1E3
GRAPH 1 2 1 3
UNCERTAINTY 2
HALF
HAZARDS
<< -----irradiation phase----- >>
FLUX 1.04E+15
ATOMS
TIME 1.0 DAYS
ATOMS
TIME 10.0 DAYS
ATOMS
TIME 100.0 DAYS
ATOMS
TIME 1000.0 DAYS
ATOMS
<< -----cooling phase----- >>
FLUX 0.
ZERO
TIME    36 ATOMS
TIME    15 ATOMS
TIME    16 ATOM
END
* END
/*