# Priority Queue (Max‐Heap) with Task Management

This module provides an array‐backed max‐heap implementation specialized for scheduling “tasks” with priorities, arrival times, and optional deadlines. It supports fast insertion, extraction of the highest‐priority task, priority changes, and removal of arbitrary tasks by ID—all in logarithmic time.

## Features

- **O(n)** heap construction from an existing list of `Task` objects  
- **O(log n)** insertion (`insert`)  
- **O(log n)** extraction of the max‐priority task (`extract_max`)  
- **O(log n)** priority change (`change_priority`)  
- **O(log n)** removal of any task by its ID (`remove`)  
- **O(1)** peek at the current max (`peek`)  
- **O(1)** emptiness check (`is_empty`)  
- Python‐friendly: supports `len(pq)` and truth testing (`if pq:`)

## File Structure

- `pq.py`  
  - `Task` class: encapsulates `task_id`, `priority`, `arrival_time`, and optional `deadline`  
  - `MaxHeap` class: priority queue implementation  

## Installation

No external dependencies are required beyond the Python standard library. Simply copy `pq.py` into your project or install via your favorite package manager if you bundle it.

## Usage

```python
from pq import Task, MaxHeap
```

### 1. Create some tasks
```
tasks = [
    Task(task_id=1, priority=5, arrival_time= 0),
    Task(task_id=2, priority=2, arrival_time=10),
    Task(task_id=3, priority=7, arrival_time=20, deadline=100),
]
```

### 2. Build a heap in O(n) time
```
pq = MaxHeap(tasks)
```
### 3. Inspect the highest‐priority task without removing it
```
print("Top task:", pq.peek())  
→ Task(id=3, prio=7)
```

### 4. Extract tasks in priority order
```
while not pq.is_empty():
    task = pq.extract_max()
    print("Dispatching:", task)
```

### 5. Dynamic operations
```
pq.insert(Task(task_id=4, priority=4, arrival_time=30))
pq.change_priority(task_id=2, new_priority=8)
removed = pq.remove(task_id=1)
print("Removed task:", removed)
```

## Performance
All core operations (`insert`, `extract_max`, `change_priority`, `remove`) run in O(log n) time due to sifting operations over the heap’s height. The peek and emptiness checks are constant time. Building from an initial list of n tasks takes O(n) time via bottom‐up heapify.