import operator
import os
import pickle
import sys
import zipfile
from functools import reduce
from os import path
from urllib.request import urlretrieve

stats_dir = path.join(os.path.dirname(os.path.dirname(__file__)), 'stats')


def parse_stats(name, sep='\t', ngram_sep='_'):
    """
    Read key,value pairs from file.
    """
    print("reading ngrams", name)
    d = {}
    with open(name, "r", encoding="utf-8") as f:
        for line in f:
            values = line.split(sep)
            if len(values) > 2:
                d[ngram_sep.join(values[:-1])] = int(values[-1])
            else:
                d[values[0]] = int(values[1])

    return d


def read_stats(corpus, ngram):
    check_stats_files()
    print("Reading " + "{} - {}grams".format(corpus, ngram))
    text = path.join(*[stats_dir, corpus, "counts_{}grams.txt".format(ngram)])
    pickled = path.join(*[stats_dir, corpus, "counts_{}grams.pickle".format(ngram)])

    if os.path.isfile(pickled):
        with open(pickled, "rb") as f:
            stats = pickle.load(f)
            return stats
    elif os.path.isfile(text):
        print("generating binary file for faster loading...")
        stats = parse_stats(text)
        with open(pickled, "wb") as f:
            pickle.dump(stats, f)
        return stats
    else:
        print("stats file not available!")
        sys.exit(1)


def check_stats_files():
    """
    Check
    :return:
    """
    if not os.path.exists(stats_dir):
        print("Word statistics files not found!\nDownloading...", end=" ")
        url = "https://www.dropbox.com/s/a84otqrg6u1c5je/stats.zip?dl=1"
        urlretrieve(url, "stats.zip")
        print("done!")

        print("Unpacking...", end=" ")
        with zipfile.ZipFile("stats.zip", "r") as zip_ref:
            zip_ref.extractall(stats_dir)

        os.remove("stats.zip")
        print("done!")


def product(nums):
    """
    Return the product of a sequence of numbers.
    """
    return reduce(operator.mul, nums, 1)


check_stats_files()
