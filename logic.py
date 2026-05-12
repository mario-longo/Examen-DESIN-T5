class TodoLogic:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_text):
        if task_text.strip():
            task = {"text": task_text, "completed": False}
            self.tasks.append(task)
            return task
        return None

    def clear_completed(self):
        self.tasks = [t for t in self.tasks if not t["completed"]]