evgenConfig.description = "Dijet truth jet slice JZ4, with Pythia 6 AUET2B"
evgenConfig.keywords = ["QCD", "jets"]

include("MC12JobOptions/Pythia_Perugia2011C_Common.py")


topAlg.Pythia.PythiaCommand += [
                                  "pysubs msel 0",
                                  "pysubs ckin 3 250.",
                                  "pysubs msub 11 1",
                                  "pysubs msub 12 1",
                                  "pysubs msub 13 1",
                                  "pysubs msub 68 1",
                                  "pysubs msub 28 1",
                                  "pysubs msub 53 1"]


include("MC12JobOptions/JetFilter_JZ4.py")
evgenConfig.minevents = 2000




