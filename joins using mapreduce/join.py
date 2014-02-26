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
    mr.emit_intermediate(record[1],record)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    # total = 0
    record = []
    for list in list_of_values:
        if list[0] == 'order':
          record = list

    if len(record)>0:
      for list in list_of_values:
        if list[0]  != 'order':
          mr.emit((record+list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
