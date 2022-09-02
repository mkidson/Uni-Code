import pandas as pd
import uproot


df = pd.read_csv('data.GamGam.csv')


df.head

"""
print("N events raw = " + str(len(df.index)))

cut0 = df[(df.trigP == True )]

print("N events cut 0 = " + str(len(cut0.index)))

cut1 = cut0[(cut0.photon_trigMatched[0] == True) & (cut0.photon_trigMatched[1] == True ) ]

print("N events cut 1 = " + str(len(cut1.index)))

cut2 = cut1[(cut1.photon_isTightID[0] == True) & (cut1.photon_isTightID[1] == True)]

print("N events cut 2 = " + str(len(cut2.index)))

cut3 = cuts2[((cuts2.photon_etcone20[0]/cuts2.photon_pt[0] ) < 0.065) & ( (cuts2.photon_etcone20[1]/cuts2.photon_pt[1] ) < 0.065) ]

print("N events cut 3 = " + str(len(cut3.index)))

cut4 = cuts3[( (cuts3.photon_ptcone30[0]/cuts3.photon_pt[0] ) < 0.065) & (  (cuts3.photon_ptcone30[1]/cuts3.photon_pt[1] ) < 0.065) ]

print("N events cut 4 = " + str(len(cut4.index)))
"""
