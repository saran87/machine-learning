import MapReduce
import sys

"""
Multiply Matrix
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    if record[0] == 'a': 
        for i in xrange(0,5):
            mr.emit_intermediate((record[1],i),[record[0],record[2],record[3]])
    elif record[0] == 'b': 
        for i in xrange(0,5):
            mr.emit_intermediate((i,record[2]),[record[0],record[1],record[3]])


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #make grader happy
    a = []
    b = []
    for v in list_of_values:
        if v[0] == 'a':
            a.append(v)
        else:
            b.append(v)
   
    sum = 0
    for i in a:
        for j in b:
            if i[1] == j[1]:
                sum += (i[2] * j[2])
    if sum > 0:
        mr.emit((key[0],key[1],sum))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
