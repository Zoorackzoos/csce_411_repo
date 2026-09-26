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

Algorithms 1:
enumerate all possible combinations of (Qi, Qj, Qk, Ql) (i,j,k,l from
any one of the  N columns) to check if there are at least P students
who can get scores equal or better than R  across all of these four quizzes.

Output Data:
Print out a file that containing all possible combinations and
the students counts that passing  your testing criteria.
Qi,Qj,Qk,Ql,count
Q1,Q2,Q3,Q4,5
Q2,Q4,Q5,Q7,18

M = rows as students
N = columns as quizzes
P = number of students getting the specific maximum score
R = the specific maximum score
"""
import datetime
import time

import pandas

path_to_yao_csv_file = "../exported_csv_files/raw_score_dataframe.csv"
yao_csv_file_name_string = "yao_file"
path_to_manual_testing_csv_file = "../exported_csv_files/manual_testing_file_one.csv"
manual_testing_csv_file_name_string = "manual_testing_file"

from itertools import combinations

def algorithm_one(
        num_of_students_who_got_specific_max_score_AKA_P,
        specific_max_score_AKA_R,
        path_to_csv_file=path_to_yao_csv_file,
        csv_file_name=yao_csv_file_name_string,
        tab_amount=""
):
    #when started
    start_time = time.perf_counter()
    print("algorithm_one")
    master_string = ""
    master_string += f"{tab_amount}algorithm_one\n"
    tab_amount += "\t"

    # getting the pandas array of the CSV file.
    #       df = data frame
    df = pandas.read_csv(path_to_csv_file)
    master_string += f"{df}\n"

    # skip student-name column
    quiz_columns = df.columns[1:]
    master_string += f"{quiz_columns}\n"

    # boolean matrix, same shape as scores
    scores = df[quiz_columns] >= specific_max_score_AKA_R
    master_string += f"{scores}\n"

    # this is what is present in the sample output.
    # list of quizzes, and at the end is the amount of students that got value P or above.
    results = []

    for combo in combinations(quiz_columns, 4):
        # a student "passes" this combo if they cleared R on ALL 4 quizzes in it
        # bool matrix --> bool matrix with one column --> sum of them, integer
        passing_count = scores[list(combo)].all(axis=1).sum()

        # if that was greater than the max students needing to "pass"
        # then add it and teh student count which is len(passing_count)
        if passing_count >= num_of_students_who_got_specific_max_score_AKA_P:
            results.append((*combo, int(passing_count)))

    end_time = time.perf_counter()
    master_string += f"time taken for algorithm_one = {end_time - start_time}\n"
    master_string += f"[\n"
    for result in results:
        master_string += f"\t{result}\n"
    master_string += f"]\n"

    print(master_string)

    export_directory_path = "../exported_combonation_of_quiz_files"
    current_time_var = str(datetime.datetime.now())[0:10] + "_"
    file_name_var = "algorithm_one" + "_on_" + csv_file_name + "_output"
    full_directory_path = export_directory_path + "/" + current_time_var + file_name_var + ".log"

    with open(full_directory_path, "w") as file:
        file.write(master_string)

    return results

if __name__ == "__main__":
    num_of_students_who_got_specific_max_score_AKA_P = 3
    specific_max_score_AKA_R = 7
    results = algorithm_one(
        num_of_students_who_got_specific_max_score_AKA_P=num_of_students_who_got_specific_max_score_AKA_P,
        specific_max_score_AKA_R=specific_max_score_AKA_R,
        csv_file_name=yao_csv_file_name_string,
        path_to_csv_file=path_to_yao_csv_file
    )
    print(results)