import MapReduce
import sys

"""
Inverted Index 
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      if w in mr.intermediate:
        if mr.intermediate[w].count(key) < 1:
          mr.emit_intermediate(w, key)
      else:
        mr.emit_intermediate(w, key)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    # total = 0

    #for v in list_of_values:
      #total += v
    mr.emit((key, list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
