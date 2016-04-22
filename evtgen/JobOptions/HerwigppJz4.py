include("MC12JobOptions/Herwigpp_UEEE4_MRSTMCal_CT10ME_Common.py")

evgenConfig.description = "QCD dijet production JZ4 with EE4 tune"
evgenConfig.keywords = ["QCD", "jets"]

cmds = """\
insert /Herwig/MatrixElements/SimpleQCD:MatrixElements[0] /Herwig/MatrixElements/MEQCD2to2
set /Herwig/UnderlyingEvent/MPIHandler:IdenticalToUE 0
set /Herwig/Cuts/JetKtCut:MinKT 250*GeV
"""
topAlg.Herwigpp.Commands += cmds.splitlines()

include("MC12JobOptions/JetFilter_JZ4.py")
evgenConfig.minevents = 5000
