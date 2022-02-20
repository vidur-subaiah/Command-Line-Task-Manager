import pickle
import os
from datetime import date, datetime, timezone
import global_variables

class Tasks:
    "A list of Task Objects"

    def __init__(self):
        "Opens up the pickled file if already created"
        if os.path.exists("./.todo.pickle"):
            with open('./.todo.pickle', 'rb') as f: #loads the pickled file which contains the task list
                self.tasks = pickle.load(f)
                global_variables.task_list_length = len(self.tasks)
        else:
            self.tasks = [] # creates the task list if running the program for the first time
    
    def pickle_tasks(self):
        """Picles the task list to the file"""
        with open('./.todo.pickle', 'wb') as f: # writes all the updates to the pickled file 
            pickle.dump(self.tasks,f)
    
    def list(self):
        """Displays an ordered table of incomplete tasks"""
        global_variables.report_flag = 0
        incomplete_tasks = []
        for item in self.tasks:
            if item.completed == None: # only adds incomplete tasks
                incomplete_tasks.append(item)
        list_tasks = sorted(incomplete_tasks) # sorts the list based on the custom sort defined in the task class
        print(f"{'ID':20} {'Age':20} {'Due Date':20} {'Priority':20} {'Task':20}\n{'--':20} {'---':20} {'--------':20} {'--------':20} {'----':20}")
        for item in list_tasks:
            print(item)    

    def report(self):
        """Prints an ordered table of all tasks in the task list"""
        global_variables.report_flag = 1 # report flag set to 1 to obtain a more detailed output when printing 
        list_tasks = sorted(self.tasks)
        print(f"{'ID':20} {'Age':20} {'Due Date':20} {'Priority':20} {'Task':20} {'Created':50} {'Completed':50}\n{'--':20} {'---':20} {'--------':20} {'--------':20} {'----':20} {'-------':50} {'---------':50}")
        for item in list_tasks:
            print(item)

    def done(self, task_id):
        "Marks a task as complete from the list of tasks"
        for item in self.tasks:
            if str(task_id) == str(item.id):
                item.completed = datetime.now(timezone.utc).strftime("%A %B %d, %H:%M:%S %Z %Y") # a task is marked as complete by assigning a string date to its completed attribute
                return print("Completed task " + str(item.id))
        print("The task ID you entered does not exist in the list of tasks. Please try again.")
    
    def delete(self, task_id):
        """Deletes a task from the list of tasks"""
        for item in self.tasks:
            if str(task_id) == str(item.id):
                self.tasks.remove(item) # a task is deleted by removing it from the task list
                return print("Deleted task " + str(item.id))
        print("The task ID you entered does not exist in the list of tasks. Please try again.")

    def query(self,search_term):
        """Displays a list of tasks that match a particular search term"""
        global_variables.report_flag = 0
        list_of_search_terms = search_term.split(" ") # splits the search string into its respective terms by splitting on space characters
        query_results = []
        for search in list_of_search_terms:
            for item in self.tasks:
                if (search.lower() in item.name.lower()) and (item not in query_results) : #checks for match in terms of the name of the task and ensures no duplicates
                    query_results.append(item)
        if len(query_results) == 0:
            print("No tasks matched your search query. Please try again.")
        else:
            query_results = sorted(query_results)
            print(f"{'ID':20} {'Age':20} {'Due Date':20} {'Priority':20} {'Task':20}\n{'--':20} {'---':20} {'--------':20} {'--------':20} {'----':20}")
            for item in query_results:
                print(item)
                
    def add(self,task):
        """Adds a task to the list of tasks"""
        self.tasks.append(task) 
        global_variables.task_list_length = len(self.tasks)