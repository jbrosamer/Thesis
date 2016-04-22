include("GeneratorUtils/StdEvgenSetup.py")
evgenConfig.description = "Herwigpp e+e-"

evgenConfig.generators += ["Herwigpp"]

include("MC12JobOptions/Herwigpp_Base_Fragment.py")

## Construct command set

from Herwigpp_i import config as hw

cmds = hw.energy_cmds(runArgs.ecmEnergy) + hw.base_cmds() + hw.lo_pdf_cmds("cteq6ll.LHpdf")

topAlg.Herwigpp.Commands = cmds.splitlines()
evgenConfig.minevents = 5000

## Add to commands
cmds += """
cd /Herwig/MatrixElements
insert SimpleEE:MatrixElements 0 MEee2gZ2qq
cd /Herwig/Generators
set LEPGenerator:EventHandler:LuminosityFunction:Energy 10.53
set LEPGenerator:EventHandler:CascadeHandler:MPIHandler NULL
set /Herwig/Particles/e-:PDF /Herwig/Partons/LeptonPDF
set /Herwig/Particles/e+:PDF /Herwig/Partons/LeptonPDF

set /Herwig/Generators/LEPGenerator:EventHandler:BeamA /Herwig/Particles/e+
set /Herwig/Generators/LEPGenerator:EventHandler:BeamB /Herwig/Particles/e-

cd /Herwig/MatrixElements
set MEee2gZ2qq:MinimumFlavour 4
set MEee2gZ2qq:MaximumFlavour 4

set /Herwig/Cuts/EECuts:MHatMin 4.0

"""

topAlg.Herwigpp.Commands = cmds.splitlines()

