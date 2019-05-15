import turicreate as tc 

tasteprofile = tc.SFrame.read_csv("TasteProfile.csv")

m1 = tc.load_model('recommendermodel')

results = m1.recommend()

#print(results)

results.export_csv('recommendations.csv')