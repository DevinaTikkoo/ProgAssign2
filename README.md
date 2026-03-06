# ProgAssign2
Devina Tikkoo, 61945909

## Project Description 
This program implements the FIFO, LRU, and OPTFF eviction policies for a cache with capacity k and requests m and counts the number of misses per policy. 

## Repository Structure 
```text
ProgAssign2
├── src
│ └── cache_miss_sim.py
│
├── data
│ ├── example1.in
│ ├── example2.in
│ └── example3.in
│
├── tests
│ ├── test1.in
│ └── test2.in
│
└── README.md
```

## Initial Assumptions
The input file will always contain k m in the first line and integer id requests r1 r2 ... rm on the second line. Additionally, k is always >=1 and r is always integers. 

## Running Repository 
Once the repository is cloned, run the program from the root directory with the following command...

python src/cache_miss_sim.py <input_file>

If successful, the output will be written into a .out file with the same name as the input file and echoed into the terminal. Else, a value error will be raised in the terminal. 

Additionally, input files within data are used for the examples in Question 1. To run these, utilize the command... 
python src/cache_miss_sim.py data/<input_file>

The input files in tests are used to ensure accuracy of the cache miss simulator. Additionally, test2.in is used as the example for question 2. It can be run with the command... 
python src/cache_miss_sim.py tests/test2.in

## Question 1
I tested the FIFO, LRU, and OPTFF eviction policies on three input files, utilizing a constant variable of 60 requests each.

| Input File    | k | m  | FIFO | LRU | OPTFF |
|---------------|---|----|------|-----|-------|
| example1.in   | 3 | 60 | 45   | 50  | 31    |
| example2.in   | 3 | 60 | 30   | 32  | 25    |
| example3.in   | 3 | 60 | 60   | 60  | 38    |

### Commentary 
For each input file, OPTFF does result in the fewest misses. It evicts the least needed or never used item in future, making it the optimal offline caching eviction policy. Additionally, FIFO had fewer misses than LRU in the first two input files, but they both resulted in 60 misses in example3.in. 

## Question 2
There does exist a request sequence for when OPTFF strictly has the least misses. Specifically, when k = 3, m = 14, and r is the sequence...
8 9 10 11 8 9 14 8 9 10 11 14 8 9

The sequence is in tests/test2.in and provides the following output. 

### Output/Report
| Policy | Misses |
|--------|--------|
| FIFO   | 11     |
| LRU    | 12     |
| OPTFF  | 8      |

### LRU Computation 
| Request | Cache After | Evicted | Hit/Miss|
|-------  |-------------|---------|---------|
| 8       | 8           |        | Miss    |
| 9       | 8 9         |        | Miss    |
| 10 | 8 9 10 | | Miss |
| 11 | 9 10 11 | 8 | Miss |
| 8 | 10 11 8 | 9 | Miss |
| 9 | 11 8 9 | 10 | Miss |
| 14 | 8 9 14 | 11 | Miss |
| 8 | 8 9 14 |  | Hit |
| 9 | 8 9 14 |  | Hit |
| 10 | 9 14 10 | 8 | Miss |
| 11 | 14 10 11 | 9 | Miss |
| 14 | 14 10 11 |  | Hit |
| 8 | 10 11 8 | 14 | Miss |
| 9 | 11 8 9 | 10 | Miss |

### OPTFF Computation 
| Request | Cache After | Evicted | Hit/Miss |
|--------|-------------|---------|----------|
| 8  | 8         |  | Miss |
| 9  | 8 9       |  | Miss |
| 10 | 8 9 10    |  | Miss |
| 11 | 8 9 11    | 10 | Miss |
| 8  | 8 9 11    |  | Hit |
| 9  | 8 9 11    |  | Hit |
| 14 | 8 9 14    | 11 | Miss |
| 8  | 8 9 14    |   | Hit |
| 9  | 8 9 14    |   | Hit |
| 10 | 8 9 10    | 14 | Miss |
| 11 | 8 9 11    | 10 | Miss |
| 14 | 8 9 14    | 11 | Miss |
| 8  | 8 9 14    |   | Hit |
| 9  | 8 9 14    |  | Hit |

The above computation and algorithm output shows OPTFF has strictly fewer misses than LRU. In this case, LRU made serveral evictions that caused additional misses. It evicts 11 early in the sequence, then 8 when the cache is full since it was the least recently used. However, 8 is requested later, causing another miss. OPTFF looks at future requests for the farthest-in-future use, resulting in less misses. Specifically, it evicts 10 as it's not needed until the end of the algorithm. As such, OPTFF results in 8 misses while LRU results in 12 misses. 

## Question 3

Theorem: OPTFF is an optimal eviction policy and has misses less than or equal to the number of misses for A. 

### Proof

Let A be any offline algorithm. Let S be an optimal reduced schedule to be compared against S_F - schedule produced by OPTFF.

Utilizing induction we can prove the invariant that there exists an optimal reduced schedule S with the same eviction schedule a S_F for the first j steps. 

**Base Case:**
When j = 0 or before the requests occur, the invariant is true. 

**Inductive step:** Assuming, the invariant holds through step `j`. Let i be the item requested at step j + 1. Since S and S_F are the same for the first j steps, their caches will be the same before step j + 1. There are three cases:

1. **i is already in the cache.** Then both schedules get a hit, so S = S, which means the invariant is true. 

2. **i is not in the cache, but S and S_FF evict the same item.** S = S , so the invariant holds.

3. **i is not in the cache, and the S and S_FF evict different items.** 

Let S_F evice item l while S evicts item k, which does not equal l. OPTFF evicts the item whose request is needed furtherst in future. Hence, item l is requested earlier than item k. 

When constructing schedule S that evicts item l at step j+1 and continues to act like S, it becomes apparent that having k in the cache does not increase the number of misses. Specifically, because k is needed furthest in future or after l. As such, S' is still optimal and agrees with the eviction schedule for S_F through j+1. 

Hence the invariant holds for all j, meaning there is a schedule that agrees at each step with OPTFF and that OPTFF has no more misses than nay offline algorithm A. Therefore, misses(OPTFF) <= misses(A) on any fixed sequence. 




