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
apply the step-wise filtering strategy.
For example, you can create a temporary counting
table (Qi, count), use it to create
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
import pandas as pd

path_to_yao_csv_file = "../exported_csv_files/raw_score_dataframe.csv"
yao_csv_file_name_string = "yao_file"
path_to_manual_testing_csv_file = "../exported_csv_files/manual_testing_file.csv"
manual_testing_csv_file_name_string = "manual_testing_file"

from itertools import combinations

def algorithm_two(
        path_to_csv_file,
        num_of_students_who_got_specific_max_score_AKA_P,
        specific_max_score_AKA_R
):

    """

    :param path_to_csv_file:
    :param num_of_students_who_got_specific_max_score_AKA_P:
    :param specific_max_score_AKA_R:
    :return:
    """

    """
      Unnamed: 0  q1  q2  q3  q4  q5   q6   q7
    0   bloopert   0   0  90   0  90  100  100
    1     martin  80  80  90  80  90  100  100
    2   Shmingus  30  30  80  30  80  100  100
    """
    csv_file_variable = pd.read_csv(path_to_csv_file)
    #print(csv_file_variable)

    """
       q1  q2  q3  q4  q5   q6   q7
    0   0   0  90   0  90  100  100
    1  80  80  90  80  90  100  100
    2  30  30  80  30  80  100  100
    """
    quiz_data = csv_file_variable.iloc[:, 1:]
    #print(quiz_data)

    """
          q1     q2    q3     q4    q5    q6    q7
    0  False  False  True  False  True  True  True
    1   True   True  True   True  True  True  True
    2   True   True  True   True  True  True  True
    """
    passing = quiz_data >= specific_max_score_AKA_R
    #print(passing)

    """
    q1    False
    q2    False
    q3     True
    q4    False
    q5     True
    q6     True
    q7     True
    """
    passing = passing.sum() >= num_of_students_who_got_specific_max_score_AKA_P

    """
    q3    True
    q5    True
    q6    True
    q7    True
    """
    # fuck pandas man. wtf is this shit.
    # "nonono you misunderstand it's just a macro because we do it all the time"
    #       if i make you eat your own shit. like what's happening here.
    #       does that make you a better person? no dude. this is nonsense.
    passing = passing[passing]

    print(passing)

if __name__ == "__main__":
    num_of_students_who_got_specific_max_score_AKA_P = 3
    specific_max_score_AKA_R = 10
    algorithm_two(
        num_of_students_who_got_specific_max_score_AKA_P=num_of_students_who_got_specific_max_score_AKA_P,
        specific_max_score_AKA_R=specific_max_score_AKA_R,
        path_to_csv_file=path_to_manual_testing_csv_file
    )