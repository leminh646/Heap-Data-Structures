# Extended priority queue with additional utility methods

class Task:
    def __init__(self, task_id, priority, arrival_time, deadline=None):
        self.task_id      = task_id
        self.priority     = priority
        self.arrival_time = arrival_time
        self.deadline     = deadline

    def __repr__(self):
        return f"Task(id={self.task_id}, prio={self.priority})"
    
class MaxHeap:
    def __init__(self, tasks=None):
        """
        Initialize an empty max-heap or build from an existing list of Task instances.
        Building from a list runs in O(n) time.
        """
        self._data = []                # array of Task
        self._pos  = {}                # task_id -> index in _data
        if tasks:
            for task in tasks:
                self._data.append(task)
            # Initialize position map
            for i, task in enumerate(self._data):
                self._pos[task.task_id] = i
            # Build heap in-place
            for i in range(len(self._data)//2 - 1, -1, -1):
                self._sift_down(i)

    def __len__(self):
        return len(self._data)

    def __bool__(self):
        return bool(self._data)

    def is_empty(self):
        """O(1) check if the heap is empty."""
        return not self._data

    def peek(self):
        """O(1) return the max task without removing it."""
        return self._data[0] if self._data else None

    def insert(self, task):
        """O(log n) insert a new task."""
        i = len(self._data)
        self._data.append(task)
        self._pos[task.task_id] = i
        self._sift_up(i)

    def extract_max(self):
        """O(log n) remove and return the max task."""
        if self.is_empty():
            return None
        max_task = self._data[0]
        last      = self._data.pop()
        del self._pos[max_task.task_id]
        if self._data:
            self._data[0] = last
            self._pos[last.task_id] = 0
            self._sift_down(0)
        return max_task

    def change_priority(self, task_id, new_priority):
        """
        O(log n) change a task's priority (increase or decrease).
        Automatically chooses sift direction.
        """
        i = self._pos.get(task_id)
        if i is None:
            raise KeyError(f"Task {task_id} not found")
        old_prio = self._data[i].priority
        self._data[i].priority = new_priority
        if new_priority > old_prio:
            self._sift_up(i)
        elif new_priority < old_prio:
            self._sift_down(i)

    def remove(self, task_id):
        """
        O(log n) remove a task by its ID.
        Swaps with last element, pops, then restores heap.
        """
        i = self._pos.get(task_id)
        if i is None:
            return None
        remove_task = self._data[i]
        last = self._data.pop()
        del self._pos[task_id]
        if i < len(self._data):
            self._data[i] = last
            self._pos[last.task_id] = i
            # Determine sift direction by comparing priorities
            if last.priority > remove_task.priority:
                self._sift_up(i)
            else:
                self._sift_down(i)
        return remove_task

    #─── Helpers ────────────────────────────────────────────

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self._data[i].priority <= self._data[parent].priority:
                break
            self._swap(i, parent)
            i = parent

    def _sift_down(self, i):
        n = len(self._data)
        while True:
            left, right = 2*i + 1, 2*i + 2
            largest = i
            if left < n and self._data[left].priority > self._data[largest].priority:
                largest = left
            if right < n and self._data[right].priority > self._data[largest].priority:
                largest = right
            if largest == i:
                break
            self._swap(i, largest)
            i = largest


    def _swap(self, i, j):
        """Swap elements at indices i and j, updating position map."""
        self._data[i], self._data[j] = self._data[j], self._data[i]
        self._pos[self._data[i].task_id] = i
        self._pos[self._data[j].task_id] = j

# Example usage
if __name__ == "__main__":
    tasks = [Task(i, priority=i%5, arrival_time=i) for i in range(10)]
    pq = MaxHeap(tasks)
    print("Initial heap:", pq._data)
    print("Peek max:", pq.peek())
    t = pq.extract_max()
    print("Extracted:", t)
    print("After extraction:", pq._data)
    pq.insert(Task(99, priority=7, arrival_time=100))
    print("After insert:", pq._data)
    pq.change_priority(2, new_priority=10)
    print("After priority change:", pq._data)
    removed = pq.remove(5)
    print("Removed:", removed)
    print("Final heap:", pq._data)
