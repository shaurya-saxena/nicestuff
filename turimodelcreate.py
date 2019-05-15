import turicreate as tc

tasteprofile = tc.SFrame.read_csv("TasteProfile.csv")

m1 = tc.ranking_factorization_recommender.create(tasteprofile, 'user', 'pid', target='status')
m1.save('recommendermodel')