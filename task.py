from datetime import date, datetime, timezone
import itertools
import global_variables

class Task:
  """This class represents a task and its associated information
    
      Attributes:
              - created - date
              - completed - date
              - name - string
              - unique id - number
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date (optional) 
  """

  created = datetime.now(timezone.utc).strftime("%A %B %d, %H:%M:%S %Z %Y") # the timezone is currently in UTC
  created_datetime_object = datetime.now(timezone.utc) # a datetime object which is used later to calculate the age of a task
  
  def __init__(self, name, due_date = None, priority = 1, completed = None):
    "Runs when a Task Object is being created and checks for incorrect parameters types"
    if type(name) != str: # ensuring that the name of a task is a string 
      raise Exception("""There was an error in creating your task. Run "todo -h" for usage instructions.""")
      quit()
    else:
      self.name = name 

    if due_date != None and type(due_date) != str: # ensuring that the due date is a string or None
      raise Exception("""There was an error in creating your task. Run "todo -h" for usage instructions.""")
      quit()
    elif due_date == None:
      self.due_date = None
    else:
      self.due_date = datetime.strptime(due_date, "%m/%d/%Y") # converting the date string into datetime format
    
    if priority != None and type(priority) == int and (1 <= priority <= 3): # ensuring that the priority is an integer between 1 and 3
      self.priority = priority
    else:
      raise Exception("""There was an error in creating your task. Run "todo -h" for usage instructions.""")
      quit()

    if completed != None and type(completed) != str: # ensuring that completed is a date string or None
      raise Exception("""There was an error in creating your task. Run "todo -h" for usage instructions.""")
      quit()
    else:
      self.completed = completed

    self.id = global_variables.task_list_length + 1 # ensuring that the task id is unique by making it one more than the number of existing tasks

  def __gt__(self, other):
    """Determines ordering of tasks. Compares based on due date and next by priority. Earlier due dates are placed higher. 3 is 
    considered the highest priority. If one of the tasks does not contain a due date then the other task with a due date is placed higher."""
    if self.due_date != None and other.due_date!= None:
      if self.due_date > other.due_date:
        return True
      if self.due_date == other.due_date:
        if self.priority < other.priority:
          return False
        else:
          return True
      return False
    if self.due_date == None and other.due_date == None:
      if self.priority < other.priority:
        return False
      else:
        return True
    if self.due_date != None and other.due_date == None:
      return True
    if self.due_date == None and other.due_date != None:
      return False

  def __lt__(self, other):
    """Determines ordering of tasks. Compares based on due date and next by priority."""
    if self.due_date != None and other.due_date!= None:
      if self.due_date < other.due_date:
        return True
      if self.due_date == other.due_date:
        if self.priority < other.priority:
          return False
        else:
          return True
      return False
    if self.due_date == None and other.due_date == None:
      if self.priority < other.priority:
        return True
      else:
        return False
    if self.due_date != None and other.due_date == None:
      return True
    if self.due_date == None and other.due_date != None:
      return False

  def __eq__(self, other):
    """Determines whether two tasks are equal. Two tasks are equal if they contain the same due date and priority."""
    if (self.due_date == other.due_date) and (self.priority == other.priority):
      return True
    return False

  def __str__(self):
    "Prints out a task and its details. A more detailed output is printed when the report flag is set equal to 1."
    if global_variables.report_flag == 0:
      id = self.id
      age = self.age()
      if self.due_date != None:
        due_date = self.due_date.strftime("%m/%d/%Y")
      else:
        due_date = self.due_date
      priority = self.priority
      task = self.name
      return f"{str(id):20} {str(age) + 'd':20} {str(due_date):20} {str(priority):20} {str(task):20}"
    else:
      id = self.id
      age = self.age()
      if self.due_date != None:
        due_date = self.due_date.strftime("%m/%d/%Y")
      else:
        due_date = self.due_date
      priority = self.priority
      task = self.name
      created = self.created
      completed = self.completed
      return f"{str(id):20} {str(age) + 'd':20} {str(due_date):20} {str(priority):20} {str(task):20} {str(created):50} {str(completed):50}"

  def age(self):
    """Determines the age in days of a task since it was first created"""
    current_date = datetime.now(timezone.utc) # obtains the current date
    difference = current_date - self.created_datetime_object # obtains the difference between when the task was created and the current date
    days = difference.days # obtains the difference in days
    return days
