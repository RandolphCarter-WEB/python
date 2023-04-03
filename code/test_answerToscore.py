# studentanswer_dic : 학생의 응답 저장 딕셔너리
# studentox_dic : 학생의 문항 정답 딕셔너리
# studentscore_dic : 학생의 점수 저장 딕셔너리

# answer_list : 과목 당 정답 리스트
# answerscore_list : 문항 당 점수 리스트

# q_num : 시험 문항 수

import os.path

def CheckTxtfile_Answer(answer_dic):
    if os.path.isfile("Answer.txt"):
        print("Answer List is exist.")
 
    else:
        print("Answer List is not exist.")
        print("You need to make answer data.")

        Make_AnswerTxt()
                
    print("What kind of class test? (input english)")
    class_name = input(">> ")

    answer_dic = Find_ClassTestAnswer(class_name)

    return class_name

def CheckTxtfile_Student(studentanswer_dic, class_name):
    if os.path.isfile("Student.txt"):
        print("Student List is exist.")
            
    else:
        print("Student List is not exist.")
        print("You need to make student data.")

        Make_StudentTxt()

    print("Student Name?")
    student_name = input(">> ")

    studentanswer_dic[student_name] = Find_ClassStudentAnswer(class_name, student_name)

    Print_StudentInfo(studentanswer_dic)


def Make_AnswerTxt():
    class_dic = {}
    classanswer_dic = {}

    class_name = input("what kind of class? (input [class_name]-year.month) >>")
    q_num = int(input("how may quetion they have? >>"))

    for i in range(q_num):
        answer = int(input("${i}'s quetion answer >>"))
        score = int(input("${i}'s quetion score >>"))

        classanswer_dic[answer] = score

    class_dic[class_name] = classanswer_dic

    Save_AnswerFile(class_dic)

def Make_StudentTxt():
    student_dic = {}
    student_class = {}
    studentanswer_dic = {}

    student_name = input("Input student name >>")
    class_name = input("Input class name >>")

    for i in range()




def main():
    studentanswer_dic = {}
    answer_dic = {}
        
    class_name = CheckTxtfile_Answer(answer_dic)
    CheckTxtfile_Student(studentanswer_dic, class_name)

        