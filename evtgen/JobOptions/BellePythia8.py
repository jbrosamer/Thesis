evgenConfig.description = "e+e- with the AU2 CTEQ6L1 tune"
evgenConfig.generators+=["Pythia8"]


include("MC12JobOptions/Pythia8_AU2_CT10_Common.py")
evgenConfig.minevents = 5000
topAlg.Pythia8.Commands += \
["Beams:idA = 11",
"Beams:idB = -11",
"Beams:eCM = 10.53",
"Beams:frameType = 1.",
"PDF:lepton = on",
"WeakSingleBoson:ffbar2gmZ = on",
"23:onMode = off",
"23:onIfAny = 4",
"PDF:lepton ON",
"PhaseSpace:mHatMin=4.0"
]

topAlg.Pythia8.Beam1 = "ELECTRON"
topAlg.Pythia8.Beam2 = "POSITRON"
