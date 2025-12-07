# DChu's Problem Generator
This is a website where the user can input a command and be given a problem to solve on paper. There is a help section that lists the syntax for the commands and  arguments. 

## Current list of problems
| Problem Name | Description |
| :------------| :-----------|
| Binary Search Tree Problem | Generates an array of unique random numbers, and asks the user to draw a Binary Search Tree when each of the numbers are inserted in order. |
| Matrix System Problem | Generates an augmented matrix and prompts the user to solve the system on paper. |
| Arithmetic Problem | Generates a certain number of arithmetic problems (addition, subtraction, multiplication, division). 
| Heap Problem | Generates a minimum binary heap that is represented using an array of integers. This problem asks the user to insert numbers to the heap but also remove numbers from the heap and prompts the user to trace and write down the results on paper. |
| Array Sorting Problem | Generates a array of random numbers, and asks the user to trace sorting algorithms on paper. |

## Installation
This codebase is written in Python 3.12.3.  
Activate the virtual environment using the command:
```
source .venv/bin/activate
```
And install the Flask and markdown libraries using the command below: 
```
pip install -r requirements.txt
```

Run the Flask framework using the command below:  
```
flask --app app.py run
```

## Contact
Email: chudaniel400@gmail.com  
Use this email to give me feedback on this project. This is still ongoing and I plan to add more problems as I pursue my CS degree. Anyhing is appreciated!