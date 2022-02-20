# VIDUR SUBAIAH, CONCEPTS OF PROGRAMMING, AUTUMN 2021

from task import Task
from tasks import Tasks
import argparse
import global_variables


task_list = Tasks() # initialize the Tasks object
parser = argparse.ArgumentParser() # set up the parser

# setting up the terms that the parser can recognize, the type of input expected, as well as the help strings
parser.add_argument("--add", type=str, help="the name of the task as a string")
parser.add_argument("--due", type=str, help="the due date of the task as a string in the form MM/DD/YYYY")
parser.add_argument("--priority", type=int, help="the priority of the task as an integer between 1 and 3")
parser.add_argument("--list", action='store_true', help="lists all incomplete tasks, requires no argument")
parser.add_argument('--query', type=str, required=False, nargs="+", help="find tasks based on string search terms")
parser.add_argument("--done", type=int, help="the task id as an integer")
parser.add_argument("--delete", type=int, help="the task id as an integer")
parser.add_argument("--report", action='store_true', help="lists all tasks, no argument required")

arguments = parser.parse_args()

if arguments.add: # runs if adding a task to the task list
    if arguments.priority == None:
        arguments.priority = 1 # sets priority as equal to 1 if nothing given 
    task_item = Task(arguments.add, arguments.due, arguments.priority)
    task_list.add(task_item)
    task_list.pickle_tasks() # updates added tasks 
    print("Created Task " + str(task_item.id))

if arguments.list:
    task_list.list() # lists all tasks yet to be completed

if arguments.query:
    search_string = ""
    for item in arguments.query:
        if arguments.query.index(item) == 0:
            search_string = item
        else:
            search_string = search_string + " " + item # we concatenate all search terms that have been parsed in, into a search string
    task_list.query(search_string)

if arguments.done:
    task_list.done(arguments.done) # passes the id of the task that needs to be marked as complete
    task_list.pickle_tasks() # updates

if arguments.delete:
    task_list.delete(arguments.delete) # passes the id of the task that needs to be deleted
    task_list.pickle_tasks() # updates

if arguments.report:
    task_list.report() # creates a table of all tasks that exist 

