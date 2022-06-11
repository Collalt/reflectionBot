tasks = db['tasks']

async def add_task(text = None):
    if text is None:
      raise ValueError("task text is not provided")

    return tasks.insert_one({"text": text})

async def edit_task(task_id, text = None):
    if task_id is None:
      raise ValueError("task id is not provided")

    if text is None:
      raise ValueError("task text is not provided")
    
    return tasks.update_one({"_id": task_id}, {"$set": {"text": text}})

async def get_task(task_id):
    if task_id is None:
      raise ValueError("task id is not provided")

    return tasks.find_one({"_id": task_id})