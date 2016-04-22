evgenConfig.description = "Pythia e+e-"
evgenConfig.keywords = ["LEP"]
include("MC12JobOptions/Pythia_Base_Fragment.py")
from AthenaCommon.AlgSequence import AlgSequence
topAlg = AlgSequence("TopAlg")

from Pythia_i.Pythia_iConf import Pythia
#topAlg += Pythia()
Pythia = topAlg.Pythia
evgenConfig.minevents = 5000


Pythia.PythiaCommand +=["pyinit use_PYINIT CMS e+ e- 91.2"]

Pythia.PygiveCommand += [ "msel=0",           # Users decay choice.
                          "parj(90)=20000",   # Turn off FSR.
                          "mdcy(15,1)=1",     # Turn ON tau decays.
                          "msub(1)=1",        # Create Z bosons
                          "mdme(174,1)=0", #ddbar
                          "mdme(175,1)=0", #uubar
                          "mdme(176,1)=0", #s
                          "mdme(177,1)=0",  #c
                          "mdme(178,1)=1", #b
                          "mdme(179,1)=0", #t
                          "mdme(182,1)=0",    # Switch for Z->ee.
                          "mdme(183,1)=0",
                          "mdme(184,1)=0",    # Switch for Z->mumu.
                          "mdme(185,1)=0",
                          "mdme(186,1)=0",    # Switch for Z->tautau.
                          "mdme(187,1)=0",
                          "mstj(22)=2"] #ATLAS stable particles convention
                          #mstj 26 0 for no mixing
##
#-------------------------------------------------------------------------------------------------------------
# our pp tuned parameters might as well be worse as defaults ...  
# use no ATLAS parameter settings
#Pythia.Tune_Name="ATLAS_0" : you'll get TestHepMC crashes by doing this only 
# use only recommended ATLAS parameter settings (i.e. the ones necessary for succsfull && consistent simulation within Athena)
#Special tunes for inside pythia??
#Pythia.Tune_Name="PYTUNE_350" # keep ER structure and new PS/MI ... see .log file for exact parameters settings
# use recommended + common (PDF, mass, MI schema etc., but not parameters commonly used for tuning) ATLAS parameter
#Pythia.Tune_Name="ATLAS_-2"
#______________________________________________________________________________________________________________