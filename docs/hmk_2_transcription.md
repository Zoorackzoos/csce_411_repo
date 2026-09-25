CSCE 411/811 Data Modeling for Sys Dev 
Fall 2026, 3 credits 
Homework #2 (100 points in total) 
Due date: Tuesday 09/29 11:59pm CST 
[*This assignment contains some coding work*] 
Please remember to add your (and your teammates) Full Name and Email on the project report. Topic: Construct varied temporary tables for use in real-time combinatorial query 
Please do not use any external database systems (e.g., MySQL) for this work. The “tables” mentioned here refer to column-based data structure (like csv format), not actual SQL tables.  You may use Java, Python, or Jupyter Notebook to complete this task, but you do not need to  implement or manage tables inside a real SQL database. 
Canvas submission: 
You should upload two things: 
(1) PDF report for this task. Please follow the steps below. 
(2)  codes zipped into one file (multiple *.py, *.ipynb, *.java etc).
 Please don’t upload any data set or  data files since we will grade using a separate data set. 
Input Data:  
The original input data set is a 2-D table with student-quiz relationship, and the elements in the  2-D table are the scores for a certain student in a certain quiz. (M rows as students, and N  columns as quizzes). 
Application: A teacher wants to pick four quizzes (to be re-used) according to this 2-D table  which shows the historical students’ performance. Specifically, the teacher wants to pick four quizzes that having at least (>=) P students getting scores equal or more than (>=) R in these four quizzes. What can be the possible choices? The application program is expected to print out all  the possible combinations that meet this request for the teacher. (P and R values are thresholds  representing a query criterion.) 

Algorithms 1: 
enumerate all possible combinations of (Qi, Qj, Qk, Ql) (i,j,k,l from any one of the N columns) to check if there are at least P students who can get scores equal or better than R across all of these four quizzes. 
Algorithm 2: 
apply the step-wise filtering strategy. For example, you can create a temporary counting table (Qi, count), use it to create (Qi,Qj,count), and finally create (Qi, Qj, Qk, Ql,  count). You may need some data structure to store studentID list for temporary purpose. These  step-wise tables or data structure can be in the memory except the final result needs to be printed  out to a file. 

Output Data: 
Print out a file that containing all possible combinations and the students counts that passing your testing criteria. 
Qi,Qj,Qk,Ql,count
Q1,Q2,Q3,Q4,5 
Q2,Q4,Q5,Q7,18 
….. 
Please don’t print redundant combinations. For example (Q1,Q2,Q3,Q4) and (Q2,Q1,Q3,Q4) are  redundant combinations, and only one of them should be in the final result. Your algorithms should also print out the running time after it finishes in order to compare the  algorithms/methods. 
***For grading, we will generate a random 2-D matrix (M x N) and use it as the input data in  your algorithms. Please make M,N,P,R general parameters in your programs. We will create a  testing case by a set of threshold (P,R), and check the correctness in your output file, as well as  check whether the running time is consistent with the ones in your report or not.*** 

Implementation Steps 
(when writing a report, please follow these steps as well): 
Step 1: Generating (Simulating) a random dataset. 
Please use the following python codes or write similar codes to generate your own testing data  with 30 rows and 30 columns with studentID and quizID, with scores from 0 to 10. Save this code to a “data_generate.py”. Please include a screen shot of the finally generated data frame. [To be flexible for testing purpose, it doesn’t have to be 30 by 30.] 
import numpy as np 
import pandas as pd 
# Generate a random dataframe with 30 columns and 30 rows num_rows = 30 
num_columns = 30 
# Generate random values between 0 and 10 
random_values = np.random.randint(0, 11, size=(num_rows, num_columns)) 
# Create a dataframe 
df = pd.DataFrame(random_values) 
# Add column names 
column_names = ['Q{}'.format(i) for i in range(1, num_columns+1)] df.columns = column_names 
# Add row names 
row_names = ['S{}'.format(i) for i in range(1, num_rows+1)] df.index = row_names 
df.to_csv('raw_score_dataframe.csv', sep=",", index=True, header=True)



i have a special plugin to view csv and tsv files like this.
for fun i had the path save to a .tsv file, but to no affect. it was not tab separated.
	in my personal project i made codex create a csv to tsv function, so i was justifying that function.



Step 2. Implementing algorithm 1 and algorithm 2. 
Both algorithms should read an arbitrary “csv” file (generated in above step), and print out the  output file, as well as print out the running time (either in the first row in your output file, or in  command line shell). 
(M, N, P, R) should not be hard coded in your algorithm since they can be dynamically changed by the user. Therefore, your algorithms should treat (P,R) as input parameters/variables; (M,N)  can be obtained from the matrix size when you read your “csv” data. 
You can only hard code the combination number for quizzes (which is 4) (CSCE823 students  may need to make it flexible) because we are looking for 4 quizzes among all possible N quizzes. But you can also treat this combination number as an input parameter to make your program  more general. 
You should wrap up separate functions or “.py” files for algorithm 1 and algorithm 2. 

Sir you meant 811.
