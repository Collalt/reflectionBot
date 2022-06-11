from model import model

tasks = model.db['tasks']

async def add_task(text = None):
    if text is None:
      raise ValueError("task text is not provided")

    task_id = tasks.insert_one({"text": text})

    return tasks.find_one({"_id": task_id})

async def edit_task(task_id, text = None):
    if task_id is None:
      raise ValueError("task id is not provided")

    if text is None:
      raise ValueError("task text is not provided")
    
    tasks.update_one({"_id": task_id}, {"$set": {"text": text}})

    return tasks.find_one({"_id": task_id})

async def get_task(task_id):
    if task_id is None:
      raise ValueError("task id is not provided")

    return tasks.find_one({"_id": task_id})