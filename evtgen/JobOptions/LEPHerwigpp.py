
## Job options file for Herwig++, LEP1 Z -> qq production

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
set LEPGenerator:EventHandler:LuminosityFunction:Energy 91.2
set LEPGenerator:EventHandler:CascadeHandler:MPIHandler NULL
set /Herwig/Particles/e-:PDF /Herwig/Partons/LeptonPDF
set /Herwig/Particles/e+:PDF /Herwig/Partons/LeptonPDF

# These next lines are put here just to avoid a meaningless error that p and pbar do not have PDF's
##set /Herwig/Particles/p+:PDF /Herwig/Partons/AtlasPDFsetLO
##set /Herwig/Particles/pbar-:PDF /Herwig/Partons/AtlasPDFsetLO

set /Herwig/Generators/LEPGenerator:EventHandler:BeamA /Herwig/Particles/e+
set /Herwig/Generators/LEPGenerator:EventHandler:BeamB /Herwig/Particles/e-

cd /Herwig/MatrixElements
set MEee2gZ2qq:MinimumFlavour 5
set MEee2gZ2qq:MaximumFlavour 5

set /Herwig/Cuts/EECuts:MHatMin 91.199
"""

## Set commands
topAlg.Herwigpp.Commands = cmds.splitlines()
