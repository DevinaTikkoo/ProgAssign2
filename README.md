# ProgAssign2
Devina Tikkoo, 61945909

##Project Description 

##Repository Structure 

##Initial Assumptions

##Running Repository 

##Question 1

I tested the FIFO, LRU, and OPTFF eviction policies on three input files containing 60 requests each.

| Input File    | k | m  | FIFO | LRU | OPTFF |
|---------------|---|----|------|-----|-------|
| example1.in   | 3 | 60 | 45   | 50  | 31    |
| example2.in   | 3 | 60 | 30   | 32  | 25    |
| example3.in   | 3 | 60 | 60   | 60  | 38    |

###Commentary 
For each input file, OPTFF does result in the fewest misses. It evicts the least needed or never used item in future, making it the optimal offline caching eviction policy. Additionally, FIFO had fewer misses than LRU in the first two input files, but they both resulted in 60 misses in example3.in. 

##Question 2
There does exist a request sequence for when OPTFF strictly has the least misses. Specifically, when k = 3, m = 14, and r is the sequence...
8 9 10 11 8 9 14 8 9 10 11 14 8 9

The sequence is in tests/test2.in and provides the following output. 

| Policy | Misses |
|--------|--------|
| FIFO   | 11     |
| LRU    | 12     |
| OPTFF  | 8      |

###LRU Computation 
| Request | Cache After | Evicted | Hit/Miss|
|-------  |-------------|---------|---------|
| 8       | 8           | –       | Miss    |
| 9       | 8 9         | –       | Miss    |
| 10 | 8 9 10 | – | Miss |
| 11 | 9 10 11 | 8 | Miss |
| 8 | 10 11 8 | 9 | Miss |
| 9 | 11 8 9 | 10 | Miss |
| 14 | 8 9 14 | 11 | Miss |
| 8 | 8 9 14 | – | Hit |
| 9 | 8 9 14 | – | Hit |
| 10 | 9 14 10 | 8 | Miss |
| 11 | 14 10 11 | 9 | Miss |
| 14 | 14 10 11 | – | Hit |
| 8 | 10 11 8 | 14 | Miss |
| 9 | 11 8 9 | 10 | Miss |

##OPTFF Computation 
| Request | Cache After | Evicted | Hit/Miss |
|--------|-------------|---------|----------|
| 8  | 8         | –  | Miss |
| 9  | 8 9       | –  | Miss |
| 10 | 8 9 10    | –  | Miss |
| 11 | 8 9 11    | 10 | Miss |
| 8  | 8 9 11    | –  | Hit |
| 9  | 8 9 11    | –  | Hit |
| 14 | 8 9 14    | 11 | Miss |
| 8  | 8 9 14    | –  | Hit |
| 9  | 8 9 14    | –  | Hit |
| 10 | 8 9 10    | 14 | Miss |
| 11 | 8 9 11    | 10 | Miss |
| 14 | 8 9 14    | 11 | Miss |
| 8  | 8 9 14    | –  | Hit |
| 9  | 8 9 14    | –  | Hit |

The above computation and algorithm output shows OPTFF has strictly fewer misses than LRU. In this case, LRU made serveral evictions that caused additional misses. It evicts '11' early in the sequence, then 8 when the cache is full since it was the least recently used. However, 8 is requested later, causing another miss. OPTFF looks at future requests for the farthest-in-future use, resulting in less misses. Specifically, it evicts 10 as it's not needed until the end of the algorithm. As such, OPTFF results in 8 misses while LRU results in 12 misses. 




