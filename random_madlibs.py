from sample_madlibs import boxing, zombie
import random

if __name__ == "__main__":
    m = random.choice([boxing, zombie,])
    m.madlib()