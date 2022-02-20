Command Line Task Manager (Created by Vidur Subaiah) ==>

Fancy task managers with slick user interfaces are slow and cumbersome. With the power of the command line at your disposal, you are able to access all your tasks without having to burden yourself with tedious pointing and clicking. This project designs an object oriented task manager application that will allow you to enter tasks, save them to a file, and retrieve them...all without moving your hands from the keyboard.


Task Class ==>

A task object stores the date they were created and completed. In addition, the task manager allows for different types of tasks: a task with no due date and a task with a due date.


Tasks Class ==>

A tasks object contains all the task objects. This is achieved through a standard list data structure. The list is ordered by creation date. 

All the tasks data are serialized to disk using the Python pickle module. The tasks are brought up/written when the program is entered/exited. An invisivle .todo.pickle file stores this data. 


Running the program ==>

The program is run by downloading the files and then running the todo.py file with python along with the necessary information flags. (Program developed and tested using Python 3.8).

The user should run the program completely from the command line passing in commands and arguments that will alter the behavior of the program. The commands are: --add, --delete, --list, --report, --query, and --done. The argparse package is used to help with parsing of the command line arguments. 


List of example commands ==>

----

Add a new task using the --add command. The task description will have to be enclosed in quotes if there are multiple words. A unique indentifier is returned if the operation is succesful. If the operation is not succesful, the user is informed and the program is ended. The default priority value is 1 and the due date is optional. 

$ python todo.py --add "Walk Dog" --due 4/17/2018 --priority 1 \n
Created task 1

$ python todo.py --add 2 --due 4/17/2018 --priority 1 \n
There was an error in creating your task. Run "todo -h" for usage instructions.

$ python todo.py --add "Study for finals" --due 3/20/2018 --priority 3 \n
Created task 2

$ python todo.py --add "Buy milk and eggs" —due friday --priority 2 \n
Created task 3

$ python todo.py --add "Cook eggs" \n
Created task 4

----

The --list command is used to display a list of the not completed tasks sorted by the due date. If tasks have the same due date, they are sorted by decreasing priority (1 is the highest priority). If tasks have no due date, then they are sorted by decreasing priority.Note that only tasks that are not completed are listed with this command. The Age in the table is the number of days since the task was created

$ python todo.py list

ID   Age  Due Date   Priority   Task
(your tasks here)

----

Search for tasks that match a search term using the --query command. Only tasks that are not completed are included in the results. 

$ python todo.py --query eggs

ID   Age  Due Date   Priority   Task
(your tasks here)

Multiple terms are able to be searched. This is done through 'nargs' in the argparse package. 

$ python todo.py --query eggs dog

ID   Age  Due Date   Priority   Task
(your tasks here)

----

Complete a task by passing the done argument and the unique identifier. The following example complete tasks 1 and 2. Note that you are not deleting a task, you are just marking it as complete. The --list command will no longer print these tasks to the terminal. 

$ python todo.py --done 1 \n
Completed task 1

$ python todo.py --done 2 \n
Completed task 2

$ python todo.py --list

ID   Age  Due Date   Priority   Task
(your tasks here)

----

Delete a task by passing the --delete command and the unique identifier. 

$ python todo.py --delete 3 \n
Deleted task 3

$ python todo.py list

ID   Age  Due Date   Priority   Task
(your tasks here)

----

List all tasks, including complete and incomplete tasks using the --report command. 

$ python todo.py report

ID   Age  Due Date   Priority   Task                Created                       Completed
(your tasks here)

----

Hope you enjoy the program and find it useful!