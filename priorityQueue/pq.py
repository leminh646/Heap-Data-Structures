class Task:
    def __init__(self, task_id, priority, arrival_time, deadline=None):
        self.task_id      = task_id
        self.priority     = priority
        self.arrival_time = arrival_time
        self.deadline     = deadline

    def __repr__(self):
        return f"Task(id={self.task_id}, prio={self.priority})"

class MaxHeap:
    def __init__(self):
        self._data = []                # array of Task
        self._pos  = {}                # task_id -> index in _data

    def is_empty(self):
        return len(self._data) == 0

    def insert(self, task):
        """Append and sift up.  O(log n)."""
        i = len(self._data)
        self._data.append(task)
        self._pos[task.task_id] = i
        self._sift_up(i)

    def extract_max(self):
        """Swap root with last, pop it, sift down.  O(log n)."""
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

    def increase_key(self, task_id, new_priority):
        """Raise a task’s priority and sift up.  O(log n)."""
        i = self._pos.get(task_id)
        if i is None:
            raise KeyError("Task not found")
        if new_priority < self._data[i].priority:
            raise ValueError("New priority is lower than current")
        self._data[i].priority = new_priority
        self._sift_up(i)

    def decrease_key(self, task_id, new_priority):
        """Lower a task’s priority and sift down.  O(log n)."""
        i = self._pos.get(task_id)
        if i is None:
            raise KeyError("Task not found")
        if new_priority > self._data[i].priority:
            raise ValueError("New priority is higher than current")
        self._data[i].priority = new_priority
        self._sift_down(i)

    #─── Helpers ────────────────────────────────────────────────────────────────

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self._data[i].priority <= self._data[parent].priority:
                break
            # swap
            self._data[i], self._data[parent] = self._data[parent], self._data[i]
            self._pos[self._data[i].task_id] = i
            self._pos[self._data[parent].task_id] = parent
            i = parent

    def _sift_down(self, i):
        n = len(self._data)
        while True:
            left  = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < n and self._data[left].priority > self._data[largest].priority:
                largest = left
            if right < n and self._data[right].priority > self._data[largest].priority:
                largest = right
            if largest == i:
                break
            # swap
            self._data[i], self._data[largest] = self._data[largest], self._data[i]
            self._pos[self._data[i].task_id]     = i
            self._pos[self._data[largest].task_id] = largest
            i = largest
