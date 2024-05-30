import csv
from random import randint
import pandas as pd

jokenpo_file = pd.read_csv('C:\\Users\\raide\\Documents\\Introdução a Programação\\MachineLearning\\Jokenpo\\jokenpo.csv')
res = input('responda, 0 para pedra, 1 para papel ou 2 para tesoura')
if jokenpo_file.shape[0] < 10:
    machine_res = randint(0, 2)
else:
    min_value = jokenpo_file['jokenpo'][0].value_counts()
    min_count = min_value.min()
    min_repeat = min_value[min_value == min_count].index.tolist()
    print(min_repeat)









#with open('jokenpo.csv', 'w', newline='') as csvfile:
 #   campos_head=['jokenpo', 'resultado']
 #   writer = csv.DictWriter(csvfile, fieldnames=campos_head)

  #  writer.writeheader()
 #   write.writerow({'jokenpo':'teste'})

