from src.algorithm_one import algorithm_one
from src.algorithm_two import algorithm_two

if __name__ == "__main__":

    list_of_path_and_string_of_files_to_parse = \
    [
        [
            "../exported_csv_files/manual_testing_file_one.csv"
            "manual_testing_file_one"
        ],
        [
            "../exported_csv_files/raw_score_dataframe.csv",
            "yao_file"
        ]
    ]

    num_of_students_who_got_specific_max_score_AKA_P = 3
    specific_max_score_AKA_R = 7
    #path_to_csv_file = "../exported_csv_files/manual_testing_file_one.csv"
    #csv_file_name = "manual_testing_file_one"

    for sub_list in list_of_path_and_string_of_files_to_parse:
        algorithm_one(
            num_of_students_who_got_specific_max_score_AKA_P=num_of_students_who_got_specific_max_score_AKA_P,
            specific_max_score_AKA_R=specific_max_score_AKA_R,
            path_to_csv_file=sub_list[0],
            csv_file_name=sub_list[1],
        )
        algorithm_two(
            num_of_students_who_got_specific_max_score_AKA_P=num_of_students_who_got_specific_max_score_AKA_P,
            specific_max_score_AKA_R=specific_max_score_AKA_R,
            path_to_csv_file=sub_list[0],
            csv_file_name=sub_list[1],
        )