from random import *
from time   import *
from copy   import copy


def swap(A, i, j):
  temp = A[i]
  A[i] = A[j]
  A[j] = temp


def lomutoPartition(A, lo, hi):
  pivot = A[hi]
  i     = lo
  for j in range(lo, hi):
    if A[j] <= pivot:
      swap(A, i, j)
      i += 1
  swap(A, i, hi)
  return i


def hoarePartition(A, lo, hi):
  pivot = A[lo]
  i     = lo
  j     = hi
  while True:
    while A[i] < pivot:
      i += 1
    while A[j] > pivot:
      j -= 1
    if i < j:
      swap(A, i, j)
    else:
      return j


def quicksort_lomuto(A, lo, hi):
  if lo < hi:
    p = lomutoPartition(A, lo, hi)
    quicksort_lomuto(A, lo,  p-1)
    quicksort_lomuto(A, p+1, hi)


def quicksort_hoare(A, lo, hi):
  if lo < hi:
    p = hoarePartition(A, lo, hi)
    quicksort_hoare(A, lo,  p)
    quicksort_hoare(A, p+1, hi)


def merge(left, right):
  result = []

  while len(left) is not 0 and len(right) is not 0:
    if left[0] <= right[0]:
      result.append(left[0])
      left = left[1:]
    else:
      result.append(right[0])
      right = right[1:]

  while len(left) is not 0:
    result.append(left[0])
    left = left[1:]
  while len(right) is not 0:
    result.append(right[0])
    right = right[1:]

  return result


def mergesort(A):
  if len(A) <= 1:
    return A
  
  left  = []
  right = []
  for i,x in enumerate(A):
    if i <= len(A) / 2 - 1:
      left.append(x)
    else:
      right.append(x)

  left  = mergesort(left)
  right = mergesort(right)

  return merge(left, right)


def testSort(n,k):
  cnt   = 0
  ql_a  = []
  qh_a  = []
  m_a   = []
  while cnt < k:
    x  = range(n)
    x1 = copy(x)
    shuffle(x1)
    x2 = copy(x1)
    x3 = copy(x1)

    t0  = time()
    quicksort_lomuto(x1, 0, n-1)
    tf  = time()
    assert(x1 == x)
    ql_a.append(tf - t0)
    
    t0  = time()
    quicksort_hoare(x2, 0, n-1)
    tf  = time()
    assert(x2 == x)
    qh_a.append(tf - t0)
    
    t0  = time()
    x3  = mergesort(x3)
    tf  = time()
    assert(x3 == x)
    m_a.append(tf - t0)
  
    cnt += 1
  
  ql_avg = sum(ql_a) / float(k)
  qh_avg = sum(qh_a) / float(k)
  m_avg  = sum(m_a)  / float(k)

  return ql_avg, qh_avg, m_avg


class HashTable(object):

  def __init__(self):
    """
    """
    self.table  = {}

  def put(self, data):
    """
    """
    hashvalue = self.hashFunction(data)

    if self.table.has_key(hashvalue):
      if self.table[hashvalue] == data:
        print "the data '%s' is already in the hash table." % str(data)
      else:
        if type(self.table[hashvalue]) is not list:
          newData = [self.table[hashvalue]]
        newData.append(data)
    else:
      self.table[hashvalue] = data

  def get(self, data):
    """
    """
    hashvalue = self.hashFunction(data)

    if self.table.has_key(hashvalue):
      if self.table[hashvalue] == data:
        return self.table[hashvalue]
      else:
        if type(self.table[hashvalue]) is list:
          for d in self.table[hashvalue]:
            if d == data:
              return data
    print "the data '%s' is not in the hash table." % str(data)
    return None

  def hashFunction(self, data):
    """
    """
    return hash(data)

  def __getitem__(self, data):
    return self.get(data)


n = 10
k = 10000

#out = testSort(n,k)
#print out



