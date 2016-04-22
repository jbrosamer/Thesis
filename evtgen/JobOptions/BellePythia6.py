evgenConfig.description = "Pythia e+e-"
evgenConfig.keywords = ["QCD", "jets", "EvtGen"]
include("MC12JobOptions/Pythia_Base_Fragment.py")
from AthenaCommon.AlgSequence import AlgSequence
topAlg = AlgSequence("TopAlg")

from Pythia_i.Pythia_iConf import Pythia

Pythia = topAlg.Pythia
evgenConfig.minevents = 5000

Pythia.PygiveCommand += [ "msel=0",           # Users decay choice.
                          "parj(90)=20000",   # Turn off FSR.
                          "mdcy(15,1)=1",     # Turn ON tau decays.
                          "msub(1)=1",        # Create Z bosons
                          "mdme(174,1)=0", #ddbar
                          "mdme(175,1)=0", #uubar
                          "mdme(176,1)=0", #s
                          "mdme(177,1)=1",  #c
                          "mdme(178,1)=0", #b
                          "mdme(179,1)=0", #t
                          "mdme(182,1)=0",    # Switch for Z->ee.
                          "mdme(183,1)=0",
                          "mdme(184,1)=0",    # Switch for Z->mumu.
                          "mdme(185,1)=0",
                          "mdme(186,1)=0",    # Switch for Z->tautau.
                          "mdme(187,1)=0",
                          "mstj(22)=2"] #ATLAS stable particles convention

