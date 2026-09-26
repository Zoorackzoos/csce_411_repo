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
import datetime
import time

import pandas as pd

path_to_yao_csv_file = "../exported_csv_files/raw_score_dataframe.csv"
yao_csv_file_name_string = "yao_file"
path_to_manual_testing_csv_file = "../exported_csv_files/manual_testing_file_one.csv"
manual_testing_csv_file_name_string = "manual_testing_file"

from itertools import combinations

def algorithm_two(
        num_of_students_who_got_specific_max_score_AKA_P,
        specific_max_score_AKA_R,
        path_to_csv_file=path_to_yao_csv_file,
        csv_file_name=yao_csv_file_name_string,
):
    start_time = time.perf_counter()
    print("algorithm_two")
    master_string = ""
    master_string += f"algorithm_two\n"

    """
      Unnamed: 0  q1  q2  q3  q4  q5   q6   q7
    0   bloopert   0   0  90   0  90  100  100
    1     martin  80  80  90  80  90  100  100
    2   Shmingus  30  30  80  30  80  100  100
    """
    csv_file_variable = pd.read_csv(path_to_csv_file)
    master_string += str(csv_file_variable) + "\n"

    """
       q1  q2  q3  q4  q5   q6   q7
    0   0   0  90   0  90  100  100
    1  80  80  90  80  90  100  100
    2  30  30  80  30  80  100  100
    """
    quiz_data = csv_file_variable.iloc[:, 1:]
    master_string += str(quiz_data) + "\n"

    """
          q1     q2    q3     q4    q5    q6    q7
    0  False  False  True  False  True  True  True
    1   True   True  True   True  True  True  True
    2   True   True  True   True  True  True  True
    """
    try:
        passing = quiz_data >= specific_max_score_AKA_R
    except:
        print(specific_max_score_AKA_R)

    master_string += str(passing) + "\n"

    # "For example, you can create a temporary counting table (Qi, count)..."
    #       this is that
    passing_students = {}

    for quiz in quiz_data.columns:
        students = set(
            csv_file_variable.loc[
                passing[quiz],
                csv_file_variable.columns[0]
            ]
        )

        if len(students) >= num_of_students_who_got_specific_max_score_AKA_P:
            passing_students[quiz] = students

    """
    {
        'q3': 
        {'bloopert', 'Shmingus', 'martin'}, 
        'q5': 
        {'bloopert', 'Shmingus', 'martin'},
        'q6': 
        {'bloopert', 'Shmingus', 'martin'},
        'q7':
        {'bloopert', 'Shmingus', 'martin'}
    }
    """
    master_string += str(passing_students) + "\n"

    # "use it to create (Qi,Qj,count)"
    #       this is that
    pairs = {}

    for quiz1, quiz2 in combinations(passing_students, 2):

        students = (
            passing_students[quiz1]
            & passing_students[quiz2]
        )

        if len(students) >= num_of_students_who_got_specific_max_score_AKA_P:
            pairs[(quiz1, quiz2)] = students

    """
    {
        ('q3', 'q5'):
        {'Shmingus', 'bloopert', 'martin'},
        ('q3', 'q6'):
        {'Shmingus', 'bloopert', 'martin'},
        ('q3', 'q7'):
        {'Shmingus', 'bloopert', 'martin'},
        ('q5', 'q6'):
        {'Shmingus', 'bloopert', 'martin'},
        ('q5', 'q7'):
        {'Shmingus', 'bloopert', 'martin'},
        ('q6', 'q7'):
        {'Shmingus', 'bloopert', 'martin'}
    }
    """
    master_string += str(pairs) + "\n"

    quiz_order = list(passing_students.keys())

    triples = {}
    for (q1, q2), students in pairs.items():
        start = quiz_order.index(q2) + 1
        for quiz in quiz_order[start:]:
            new_students = students & passing_students[quiz]
            if len(new_students) >= num_of_students_who_got_specific_max_score_AKA_P:
                triples[(q1, q2, quiz)] = new_students

    quadruples = []
    for quizzes, students in triples.items():
        start = quiz_order.index(quizzes[-1]) + 1
        for quiz in quiz_order[start:]:
            new_students = students & passing_students[quiz]
            if len(new_students) >= num_of_students_who_got_specific_max_score_AKA_P:
                quadruples.append((*quizzes, quiz, len(new_students)))

    master_string += f"[\n"
    for result in quadruples:
        master_string += f"\t{result}\n"
    master_string += f"]\n"

    end_time = time.perf_counter()
    master_string += f"time taken for algorithm_two = {end_time - start_time}\n"

    print(master_string)

    export_directory_path = "../export_log_files"
    current_time_var = str(datetime.datetime.now())[0:10] + "_"
    file_name_var = "algorithm_two" + "_on_" + csv_file_name + "_output"
    full_directory_path = export_directory_path + "/" + current_time_var + file_name_var + ".log"

    with open(full_directory_path, "w") as file:
        file.write(master_string)

    return quadruples

if __name__ == "__main__":
    num_of_students_who_got_specific_max_score_AKA_P = 3
    specific_max_score_AKA_R = 7
    algorithm_two(
        num_of_students_who_got_specific_max_score_AKA_P=num_of_students_who_got_specific_max_score_AKA_P,
        specific_max_score_AKA_R=specific_max_score_AKA_R,
        csv_file_name=yao_csv_file_name_string,
        path_to_csv_file=path_to_yao_csv_file
    )