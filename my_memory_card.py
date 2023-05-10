from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from random import shuffle, randint


app=QApplication([])
window=QWidget()

btn_OK = QPushButton("Ответить")
lb_question=QLabel("")

layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()
layout_card=QVBoxLayout()

layout_line1.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

RadioGroupBox=QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton()
rbtn_2 = QRadioButton()
rbtn_3 = QRadioButton()
rbtn_4 = QRadioButton()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3=QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
layout_line2.addWidget(RadioGroupBox)

layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
layout_card.setSpacing(5)












class Question():
    def __init__(self, question, right_answer, wrong_1, wrong_2, wrong_3):
        self.right_answer = right_answer
        self.question = question
        self.wrong_answer1 = wrong_1
        self.wrong_answer2 = wrong_2
        self.wrong_answer3 = wrong_3


#Панель результата
AnsGroupBox=QGroupBox('Результат:')
lb_result=QLabel('Правильно/Неправильно')
lb_correct=QLabel('Правильный ответ')

layout_res=QVBoxLayout()
layout_res.addWidget(lb_result)
layout_res.addWidget(lb_correct)

AnsGroupBox.setLayout(layout_res)

layout_line2.addWidget(AnsGroupBox)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Следующий вопрос")


questions=[]
q1 = Question(
    "Какой национальности нет?",
    "Смурфы", 
    "Энцы", "Чулымцы", "Алеуты")
questions.append(q1)
q1 = Question(
    "Какой язык является государственным в Бразилии?",
    "Португальский", 
    "Китайский", "Английский", "Испанский")
questions.append(q1)
q1 = Question(
    "Когда началась вторая мировая война?",
    "1939", 
    "1936", "1941", "1938")
questions.append(q1)
q1 = Question(
    "Когда случилась крупнейшая катастрофа(Без учета событий 11 сентября)?",
    "1977", 
    "2017", "1974", "2001")
questions.append(q1)



def click_ok():
    if btn_OK.text()=='Ответить':
        check_answer()
    elif btn_OK.text()=="Следующий вопрос":
        next_question()


def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)



def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_answer1)
    answers[2].setText(q.wrong_answer2)
    answers[3].setText(q.wrong_answer3)
    lb_correct.setText(q.right_answer)
    lb_question.setText(q.question)
    show_question()

btn_OK.clicked.connect(click_ok)


def show_correct(res):
    lb_result.setText(res)
    show_result()
    
window.total=0
window.right=0
def check_answer():
    if answers[0].isChecked():
        show_correct("Правильный ответ")
        window.right+=1
    elif answers[1].isChecked():
        show_correct("Неправильный ответ")
    elif answers[2].isChecked():
        show_correct("Неправильный ответ")
    elif answers[3].isChecked():
        show_correct("Неправильный ответ")

def next_question():
    window.total+=1
    print('Статистика')
    print('-Всего вопросов:', window.total)
    print('-Правильных ответов:', window.right)
    window.cur_question=randint(0, len(questions)-1)
    q=questions[window.cur_question]
    ask(q)




next_question()
AnsGroupBox.hide()
window.setLayout(layout_card)
window.show()
app.exec()