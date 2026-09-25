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
import numpy

from src.craft_file_containing_all_possible_combinations import craft_file_containing_all_possible_combinations

path_to_yao_csv_file = "../exported_csv_files/raw_score_dataframe.csv"
yao_csv_file_name_string = "yao_file"
path_to_manual_testing_csv_file = "../exported_csv_files/manual_testing_file.csv"
manual_testing_csv_file_name_string = "manual_testing_file"

def algorithm_one(
        num_of_students_who_got_specific_max_score_AKA_P,
        specific_max_score_AKA_R,
        path_to_csv_file = path_to_yao_csv_file,
        csv_file_name = yao_csv_file_name_string,
        tab_amount = ""
):
    """
    Paraphrasing here...
    look at the columns 1st.
    then check the amount of columns that succeeded
    and if that number matches or is greater than P.
        put that in the list.
    you need 4 quizzes. if 4 quizzes are not able to be put in
        then just settle for what you have :-/

    THIS HAS 2 RETE RUN VALUES
    * qualified_quizess_verbose
    * qualified_quizess_simple

    if i actually gave a damn about this function i would make it more verbose in the ending
    list but honestly.
        I don't care enough for that. you can just look.

    :param num_of_students_who_got_specific_max_score_AKA_P:
    :param specific_max_score_AKA_R:
    :param path_to_csv_file:
    :return:
    """
    print(tab_amount,"algorithm_one")
    tab_amount += "\t"

    csv_file_variable = pandas.read_csv(path_to_csv_file)
    """
    pandas arrays are different than regular arrays.
    you can issue more vague syntax to get faster results than using for loops
    
    as a result. we can do what a double for loop could do...
    ...with this hocus pocus.
            it doesn't show any of the comparisons happening at all but whatever.
    """
    qualified_quizzes_verbose = (
            # compare every score to R.
            # this spits out a bunch of booleans in a list that pass in a pocket pandas array.
            #   this .iloc thing only works because this is a dataframe.
            (csv_file_variable.iloc[:, 1:] >= specific_max_score_AKA_R).sum()
            >=
            # the .sum part is the amount of bools that were TRUE.
            # compare that crap to P.
            num_of_students_who_got_specific_max_score_AKA_P
    )

    # no .iloc used here because this isn't a dataframe. so just do this:
    qualified_quizzes_simple = qualified_quizzes_verbose[
        qualified_quizzes_verbose == True
    ].index.tolist() # make it a list becuase i had pandas arrays.

    if len(qualified_quizzes_simple) <= 0:
        print(tab_amount,"no quiz instances of",num_of_students_who_got_specific_max_score_AKA_P,"getting a score of",specific_max_score_AKA_R,"exist.")
    else:
        print(tab_amount,"there were" , len(qualified_quizzes_simple) ,"quiz instincts of",num_of_students_who_got_specific_max_score_AKA_P,"students who got",specific_max_score_AKA_R,"on the quiz or more.")
        print(tab_amount,"they are the following:")
        for quiz_name in qualified_quizzes_simple:
            print(tab_amount+"\t",quiz_name)

    craft_file_containing_all_possible_combinations(
        list_of_quizzes_that_satisfy_criteria=qualified_quizzes_simple,
        algorithm_name="algorithm_one",
        csv_file_name=yao_csv_file_name_string,
        tab_amount=tab_amount
    )

    return qualified_quizzes_verbose, qualified_quizzes_simple

if __name__ == "__main__":
    num_of_students_who_got_specific_max_score_AKA_P = 3
    specific_max_score_AKA_R = 10
    algorithm_one(
        num_of_students_who_got_specific_max_score_AKA_P=num_of_students_who_got_specific_max_score_AKA_P,
        specific_max_score_AKA_R=specific_max_score_AKA_R,
        csv_file_name=path_to_yao_csv_file,
        path_to_csv_file=path_to_yao_csv_file
    )