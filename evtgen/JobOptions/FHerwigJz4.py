evgenConfig.description = "Dijet truth jet slice JZ4, with the AU2 CTEQ10 tune"
evgenConfig.keywords = ["QCD", "jets"]
# ... Main generator : Herwig
include( "MC12JobOptions/Jimmy_AUET2_CT10_Common.py" )

topAlg.Herwig.HerwigCommand += [ "iproc 11500",
                          "ptmin 250.",
                          "ptmax 8000."]

include("MC12JobOptions/JetFilter_JZ4.py")
evgenConfig.minevents = 5000


