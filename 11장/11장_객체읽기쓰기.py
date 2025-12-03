import pickle

gameOption = {
"Sound": 8, "VideoQuality": "HIGH", "Money": 100000,
 "WeaponList": ["gun", "missile", "knife" ]
}

pickle.dump( gameOption, open( "save.p", "wb" ))

myMovie = pickle.load( open( "save.p", "rb" ))
print(myMovie)