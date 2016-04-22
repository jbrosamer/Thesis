evgenConfig.description = "FHerwig e+e-"
evgenConfig.keywords = ["QCD", "jets", "EvtGen"]
from AthenaServices.AthenaServicesConf import AtRndmGenSvc
ServiceMgr += AtRndmGenSvc()
#ServiceMgr.AtRndmGenSvc.Seeds = ["JIMMY 390020611 821000366", "JIMMY_INIT 820021 2347532"]
from Herwig_i.Herwig_iConf import Herwig
topAlg += Herwig()
evgenConfig.generators += ["Herwig"]
evgenConfig.minevents = 5000

include("MC12JobOptions/Jimmy_AUET2_CT10_Common.py")

topAlg.Herwig.HerwigCommand += [ "iproc 105",
                                "beam1type E+",
                                "beam2type E-",
                                "beam1energy "+str(runArgs.ecmEnergy/2.),
                                "beam2energy "+str(runArgs.ecmEnergy/2.),
                                "pltcut 0.0000000000333",
                                 "msflag 0",
                                 "nflav 5"]
from TruthExamples.TruthExamplesConf import TestHepMC
TestHepMC.DumpEvent  = True
TestHepMC.EnergyDifference = 10000000*GeV  # To disable this test
