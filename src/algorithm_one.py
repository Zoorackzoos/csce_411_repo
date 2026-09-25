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
import pandas

from src.craft_file_containing_all_possible_combinations import craft_file_containing_all_possible_combinations

path_to_yao_csv_file = "../exported_csv_files/raw_score_dataframe.csv"
yao_csv_file_name_string = "yao_file"
path_to_manual_testing_csv_file = "../exported_csv_files/manual_testing_file.csv"
manual_testing_csv_file_name_string = "manual_testing_file"

from itertools import combinations

def algorithm_one(
        P,
        R,
        path_to_csv_file,
        csv_file_name,
        tab_amount=""
):
    df = pandas.read_csv(path_to_csv_file)
    quiz_columns = df.columns[1:]  # skip student-name column
    scores = df[quiz_columns] >= R  # boolean matrix, same shape as scores

    results = []
    for combo in combinations(quiz_columns, 4):
        # a student "passes" this combo if they cleared R on ALL 4 quizzes in it
        passing_count = scores[list(combo)].all(axis=1).sum()
        if passing_count >= P:
            results.append((*combo, passing_count))

    return results

if __name__ == "__main__":
    num_of_students_who_got_specific_max_score_AKA_P = 3
    specific_max_score_AKA_R = 10
    results = algorithm_one(
        P=num_of_students_who_got_specific_max_score_AKA_P,
        R=specific_max_score_AKA_R,
        csv_file_name=manual_testing_csv_file_name_string,
        path_to_csv_file=path_to_manual_testing_csv_file
    )
    print(results)