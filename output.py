from model_1 import *
from model_2 import *

if model_1_score>model_2_score:
   print("model_1 is better ")
   print("model_1 score is")
   print(model_1_score)
elif model_1_score < model_2_score:
    print("model_2 is better ")
    print("model_2 score is")
    print(model_2_score)
else:
    print("Both model have equal accuracy")
