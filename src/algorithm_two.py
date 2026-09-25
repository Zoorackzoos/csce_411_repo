"""
Input Data:
The original input data set is a 2-D table with student-quiz relationship,
 and the elements in the  2-D table are the scores for a certain student
 in a certain quiz. (M rows as students, and N  columns as quizzes).

Application:
A teacher wants to pick four quizzes (to be re-used) according
to this 2-D table  which shows the historical students’ performance.
Specifically, the teacher wants to pick four quizzes that having at
least (>=) P students getting scores equal or more than (>=) R in
these four quizzes. What can be the possible choices? The application
program is expected to print out all  the possible combinations that
meet this request for the teacher. (P and R values are thresholds
representing a query criterion.)

Algorithm 2:
apply the step-wise filtering strategy. For example, you can
create a temporary  counting table (Qi, count), use it to create
(Qi,Qj,count), and finally create (Qi, Qj, Qk, Ql,  count).
You may need some data structure to store studentID list for
temporary purpose. These  step-wise tables or data structure
can be in the memory except the final result needs to be printed
 out to a file.

Output Data:
Print out a file that containing all possible combinations and
the students counts that passing  your testing criteria.
Qi,Qj,Qk,Ql,count
Q1,Q2,Q3,Q4,5
Q2,Q4,Q5,Q7,18

"""

