# DChu's Problem Generator
This is a personal project where the user can input a command and be given basic computer science / math problems to solve on paper. I built this originally to help me practice and study course material over the fall semester.  
There is a help section that lists the syntax for the commands and arguments. 

## Current list of problems
| Problem Name | Description |
| :------------| :-----------|
| Binary Search Tree Problem | Generates an array of unique random numbers, and asks the user to draw a Binary Search Tree when each of the numbers are inserted in order. |
| Matrix System Problem | Generates an augmented matrix and prompts the user to solve the system on paper. |
| Arithmetic Problem | Generates a certain number of arithmetic problems (addition, subtraction, multiplication, division). 
| Heap Problem | Generates a minimum binary heap that is represented using an array of integers. This problem asks the user to insert numbers to the heap but also remove numbers from the heap and prompts the user to trace and write down the results on paper. |
| Array Sorting Problem | Generates a array of random numbers, and asks the user to trace sorting algorithms on paper. |
| 2x2 Linear Planar System Problem | Generates a 2x2 matrix, and asks the user to find the eigenvalues and eigenvectors of it, and in the context of differential equations, write the general solution to the linear planar system. |
| Binary Problem | Three cases: (1) Generates a list of five 8-bit binary numbers and prompts the user to write down those numbers in decimal form. (2) Generates a list of five unsigned decimal integers (0-255) and prompts the user to write down those numbers in binary form. (3) Generates a list of five hexadecimal integers (00-ff) and prompts the user to write down those numbers in decimal form. |  

## Development process
I started out working with the Flask framework in order to carry out this web application. I set up the `app.py` and `index.html` files as I slowly learned how Flask functions and decorators work. The html file started out very simple. I learned about `meta` tags in the head portion of file, and I put a simple form that contained a field of text and a submit button.  

The first tricky part was getting the `app.py` file to be able to read what the user entered. I had to learn a bit about POST requests which turned out to be the best approach for displaying the output to the user.  

Once I was able to get the form up and running, I began working on generating some problems. I made a `problems/` directory as a custom Python package that contained all of the future Python files for the Problems. I made a Problem module that served as a base abstract class for child problems to derive from. Durign this process, I had a bit of trouble working out how Python packaging works, but things worked out in the end.  

I first made the `BSTProblem` class that extends as a child from the `Problem` class, which was the easiest to implement at the time. I simply made it generate an array of random numbers that don't repeat themselves and tell the user to draw it on paper. Then I wrote the `MatrixLinearSystemProblem` and `HeapProblem` classes later on. The `MatrixLinearSystemProblem` class gave a bit of trouble because I wanted to display the matrices as square and as fixed of a shape as possible; I had to learn about number formatting in Python in order to make this work.

Then came the `ArithmeticProblem`, `ArraySortingProblem` and `LinearPlanarSystemProblem` classes. The planar system one also took me a long time to figure out how to implement it because it required generating a matrix from just eigenvalues and eigenvectors, but *also* making sure the final result contained just integers. I worked around this mathematically by using some form of diagonalization from linear algebra, though I haven't taken a class on that subject and instead am taking differential equations. This was when I started using the `numpy` library for the first time, as I used it for implementing matrix multiplication and inverting matrices.

For styling, I took great interest in learning how to use raw `css`, especially through learning about style selectors and which styling rules take priortiy. I also learned more about margins vs. padding, as well as learning about block vs. inline layouts.

## Installation
This codebase is written in Python 3.12.3.  
The following commands are from a Linux Ubuntu context. For anyone interesting in giving this a try, clone the repository and activate the virtual environment using the command:
```
source .venv/bin/activate
```
And install the Flask and markdown libraries using the command below: 
```
pip install -r requirements.txt
```

Finally, run the Flask framework using the command below:  
```
flask --app app.py run
```
The terminal should respond by giving a url to the local website. Click on it to see the application!

## Contact
Email: chudaniel400@gmail.com  
Use this email to give me feedback on this project. This is still ongoing and I plan to add more problems as I pursue my CS degree.  Anything is appreciated, especially ideas for new problems!