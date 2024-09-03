import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

from matplotlib import font_manager

fontP = font_manager.FontProperties()
fontP.set_family('SimHei')
fontP.set_size(34)

ETK_file = pd.ExcelFile('Chinese.xlsx')
df = ETK_file.parse('Sheet1')

ETK_chr = [ ]
ETK_pin = [ ]
ETK_def = [ ]
ETK_lesC = [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ],
            [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ],
            [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]]
ETK_lesP = [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ],
            [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ],
            [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]]
ETK_lesD = [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ],
            [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ],
            [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]]

less_no = 0
for char_, piny_, defi_ in zip(df.iloc[:,0], df.iloc[:,1], df.iloc[:,2]):
    if isinstance(char_, str) and char_ != 'Characters' and 'HSK' not in char_ and less_no < 10:
        ETK_chr.append(char_)
        ETK_pin.append(piny_)
        ETK_def.append(defi_)
        ETK_lesC[less_no].append(char_)
        ETK_lesP[less_no].append(piny_)
        ETK_lesD[less_no].append(defi_)
    if char_ == 'Characters':
        less_no += 1
        
rnd_ints = [ ]
definition = True
pinyin = False

all_words = False
test = 0

if (all_words):
    print("Testing all characters")
else:
    print("Testing lesson")
print(ETK_lesD[1])

if (all_words):
    while test <= len(ETK_chr):
        rnd = random.randint(0,len(ETK_chr)-1)
        if rnd not in rnd_ints and len(ETK_chr[rnd]) <= 4: 
            rnd_ints.append(rnd)
            if (definition):
                print("Word #", test, '/', len(ETK_chr))
                print("Write translation of ", ETK_def[rnd])
                input("Press keyboard when done: ")
                print("Pinyin:    ", ETK_pin[rnd])
                print("Character: ", ETK_chr[rnd])
                print("=========================")
                fig, ax = plt.subplots()
                ax.text(0.5, 0.5, ETK_chr[rnd], 
                        horizontalalignment='center',
                        verticalalignment='center',
                        fontproperties=fontP)
                plt.show()
            elif (pinyin):
                print("Write the character of ", ETK_pin[rnd])
                input("Press keyboard when done: ")
                print("Translation:  ", ETK_def[rnd])
                print("Character:    ", ETK_chr[rnd])
                print("============================")
            else:
                print("What does ", ETK_chr[rnd], " mean?")
                input("Press keyboard when done: ")
                print("Pinyin:       ", ETK_pin[rnd])
                print("Translation:  ", ETK_def[rnd])
                print("============================")
            test += 1

else:
    less_no = int(input("What lesson are you testing? "))
    while test <= np.shape(ETK_lesD[less_no])[0]:
        rnd = random.randint(0,np.shape(ETK_lesD[less_no])[0]-1)
        if rnd not in rnd_ints and len(ETK_lesC[less_no][rnd]) <= 4:
            print("Word #", test)
            rnd_ints.append(rnd)
            if (definition):
                print("Write translation of ", ETK_lesD[less_no][rnd])
                input("Press keyboard when done: ")
                print("Pinyin:    ", ETK_lesP[less_no][rnd])
                print("Character: ", ETK_lesC[less_no][rnd])
                fig, ax = plt.subplots()
                ax.text(0.5, 0.5, ETK_lesC[less_no][rnd], 
                        horizontalalignment='center',
                        verticalalignment='center',
                        fontproperties=fontP)
                plt.show()
                print("=========================")

            elif (pinyin):
                print("Write the character of ", ETK_lesP[less_no][rnd])
                input("Press keyboard when done: ")
                print("Translation:  ", ETK_lesD[less_no][rnd])
                print("Character:    ", ETK_lesC[less_no][rnd])
                print("============================")
            else:
                print("What does ", ETK_lesC[less_no][rnd], " mean?")
                input("Press keyboard when done: ")
                print("Pinyin:       ", ETK_lesP[less_no][rnd])
                print("Translation:  ", ETK_lesD[less_no][rnd])
                print("============================")
            test += 1
