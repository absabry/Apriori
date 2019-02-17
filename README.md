# Apriori
Data mining apriori algorithm in python

# usage 
Launch apriori.py from any ide  and specify or commande line using this command : 
__python apriori.py__.

You can also use the notebook apriori.ipynb for a more aesthetic plateform. Vizualisation are made from this result. 

arguments :
 
--dataset       Path to the dataset file. 
                Data should be formated as in "dataset.txt" file.
                
--delimeter     Used to parse the dataset file, comma (',') by default 

-- epsilon      value greater than which we'll filter 
                the occurences in the final result

--verbose       debug purpose only, it will display 
                each level with its corresponding 
                values with their counts. 
                Should be one of "True" or "False" 
--help          display help and exit

# output

Using the script apriori.py, values will be printed in console : 

element :               assosicated terms in the dataset

value :                 number of occurences the term is found in the dataset

support:                support of the assosicated term. For instance support(1->2->3)
                        will be __N(1->2->3)/Total__ where __N__ is the number of occurences of a subset
                        and __Total__ is number of lines in the dataset
                        
confidence:             Confidence refers to the likelihood that an item (or subset) B is also bought if item A is bought. 
                        For instance conf(1->2->3) will be the confidence to found 3 with the subset (1->2).
                        
reverse-confidence:     Is the confidence that refers to the likelihood that 
                        an item A is also bought if item (or subset) B is bought.
                        For instance reverse_conf(1->2->3) will be the confidence 
                        to found the subset (1->2) with the number 3.
                        
Lift:                   Lift(A -> B) refers to the increase in the ratio of sale of B when A is sold. 
                        Lift(A –> B) can be calculated by dividing Confidence(A -> B) divided by Support(B). 
                        
reverse-lift:           Same as Lift(A -> B) but divided by Support(A).
   
# Example 
python apriori.py --verbose "True" --dataset "dataset.txt" --epsilon "3"             
