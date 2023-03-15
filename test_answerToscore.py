# studentanswer_dic : 학생의 응답 저장 딕셔너리
# studentox_dic : 학생의 문항 정답 딕셔너리
# studentscore_dic : 학생의 점수 저장 딕셔너리

# answer_list : 과목 당 정답 리스트
# answerscore_list : 문항 당 점수 리스트

# q_num : 시험 문항 수

import os.path

def ScoreResult(studentox_dic, answerscore_list, key, q_num):
    resultscore = 0

    for i in range(q_num):
        if (list(studentox_dic[key])[i] == 'O'):
            resultscore += answerscore_list[i]
    
    print("finish check student score result")

    return resultscore

def Check_StudentScore(studentanswer_dic, studentox_dic, studentscore_dic, answer_list, answerscore_list, q_num):
    scorelist = []

    for key in studentanswer_dic:
        for i in range(q_num):
            if (list(studentanswer_dic[key])[i] == answer_list[i]):
                scorelist[i] = 'O'
            else:
                scorelist[i] = 'X'

        studentox_dic[key] = scorelist
        studentscore_dic[key] = ScoreResult(studentox_dic, answerscore_list, key, q_num)
    
    print("finish check student list")


def main():
    studentanswer_dic = {}

    q_num = 0
    repeat = 1

    while(repeat == 1):
        if os.path.isfile("Answer.txt"):
            print("Answer List is exist.")
            print("What kind of class test? (input english)")
            class_name = input(">> ")

            answer_list = Find_ClassTestAnswer(class_name)

            if os.path.isfile("Student.txt"):
                print("Student List is exist.")
                print("Student Name?")
                student_name = input(">> ")

                studentanswer_dic[student_name] = Find_ClassStudentAnswer(class_name, student_name)

                Print_StudentInfo(studentanswer_dic)
            
            else:
                print("Student List is not exist.")
                print("You need to make student data.")
                



        