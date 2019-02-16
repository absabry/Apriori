from utils import dataset_from_file,apriori,format_output

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--dataset", help= "dataset to search for occurences within it")
parser.add_argument("--delimeter", help= "Used to parse the dataset file, comma (',') by default")
parser.add_argument("--epsilon", help= "occurences greater than\
                    this value will be kept in the final result", type=int)
parser.add_argument("--verbose", help= "debug purpose only, it will\
                     display each level with its corresponding values\
                     with their counts. Should be one of 'True' or 'False'")
args = parser.parse_args()

delimeter = args.delimeter if args.delimeter is not None else ","
dataset = args.dataset if args.dataset is not None else "datasets/dataset.txt"
T = dataset_from_file(dataset, delimeter)
eps = int(args.epsilon) if args.epsilon is not None else 3
verbose = args.verbose if args.verbose is not None else False

res = apriori(T,eps,verbose)
format_output(res)