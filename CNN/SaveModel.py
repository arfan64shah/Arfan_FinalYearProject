
import pickle
# # How to use the saved model

with open ('DT_Classifier','rb') as f:
      mod= pickle.load(f)

y_pred= mod.predict([[19,18000]])

# y_pred= mod.predict( [[Mean1, Variance1, Skewness1, Kurtosis1,entropy1, Cont1,Energ1, Homo1, Corre1, Mean2, Variance2, Skewness2, Kurtosis2, entropy2, Cont2, Energ2, Homo2, Corre2, Mean3, Variance3, Skewness3, Kurtosis3, entropy3, Cont3, Energ3, Homo3, Corre3 ]])

print ('Output Class =',y_pred)

# y_pred= mod.predict([[	0.870655, 0.870655, -0.582299,	0.285894,	0.231365,	-0.579999,	-1.02436,	0.664007,	0.986286,	1.19648,	-0.904533,	-1.13354,	1.08772	1.25481,	-1.17386,	-0.929994,	1.02572,	1.10411,	1.02446,	0.61185,	0.995131,	-0.435454,	-0.200913,	-1.10796,	-1.08801,	0.838777]])

# print (y_pred)
# # Load the pickled model 
# y_pred= mod.predict([[16,20000]])
# print (y_pred)

# import PIL
# from PIL import Image

# image = PIL.Image.open("cat.1.jpg")
# image.show()

# import cv2

# width, height = image.size
# print(width, height)

# import pickle
# # How to use the saved model

# with open ('classifier_pickle','rb') as f:
#      mod= pickle.load(f)

# # Load the pickled model 
# y_pred= mod.predict([[	0.870655, 0.870655, -0.582299,	0.285894,	0.231365,	-0.579999,	-1.02436,	0.664007,	0.986286,	1.19648,	-0.904533,	-1.13354,	1.08772	1.25481,	-1.17386,	-0.929994,	1.02572,	1.10411,	1.02446,	0.61185,	0.995131,	-0.435454,	-0.200913,	-1.10796,	-1.08801,	0.838777]])
# print (y_pred)
  
# Use the loaded pickled model to make predictions 