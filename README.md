# Apriori
Data mining apriori algorithm in python

# usage 
Launch apriori.py from any ide and specify or commande line using this command : 
__python apriori.py__ 

arguemnts :
 
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
                
# Example 
python apriori.py --verbose "True" --dataset "dataset.txt" --epsilon "3"             