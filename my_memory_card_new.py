#создай приложение для запоминания информации
#Подключаем модули
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint, shuffle
#создаем класс вопрос (сам вопрос, правельный ответ, не правельные ответы)
class Question():
    def __init__(self,question,Right_answer,wrong1,wrong2,wrong3):
        self.question = question 
        self.Right_answer = Right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
#создаем список вопросами 
questions = []
questions.append(Question('Сколько будет 2+2','четыре','двацать два','шесть','бесконечность'))
questions.append(Question('Кто крестил Русь','В.К. Солнышко','Петр I','Цезарь','Гогаль'))
questions.append(Question('Кто такой плохой человек','Плохой человек','Хороший человек','Грустный человек','Веселый человек'))
#создаем приложение и его окно
app = QApplication([])
at = QWidget()
at.resize(400,200)
#название окна
at.setWindowTitle('Memory card')
#созадем виджет текста
quetion = QLabel('Какой нацинальности не существует?')
#создаем виджет кнопки
lamda = QPushButton('Ответить')
#создаем виджет группбокс вопроса
radiogroup =QGroupBox('Варианты ответа')
#создаем виджет группбокс ответа
ans_radiogroup =QGroupBox('результат теста')
Result = QLabel(' ')
Right_ans = QLabel('Правильный ответ')
v_layout3 = QVBoxLayout()
v_layout3.addWidget(Result,alignment= Qt.AlignTop| Qt.AlignLeft)
v_layout3.addWidget(Right_ans,alignment= Qt.AlignCenter)
ans_radiogroup.setLayout(v_layout3)
#создаем варианты ответов
rbt1 = QRadioButton('Энцы')
rbt2 = QRadioButton('Смурфы')
rbt3 = QRadioButton('Чульманцы')
rbt4 = QRadioButton('Алеуды')

radiogroup_box = QButtonGroup()
radiogroup_box.addButton(rbt1)
radiogroup_box.addButton(rbt2)
radiogroup_box.addButton(rbt3)
radiogroup_box.addButton(rbt4)
#задаем линии для размещения вариантов ответов
v_layout1 = QVBoxLayout()
v_layout2 = QVBoxLayout()
h_layout1 = QHBoxLayout()
#размещаем варианты ответа на линиях
v_layout1.addWidget(rbt1)
v_layout1.addWidget(rbt2)
v_layout2.addWidget(rbt3)
v_layout2.addWidget(rbt4)
#устанавливаем вертикальные линии на горизонтальную
h_layout1.addLayout(v_layout1)
h_layout1.addLayout(v_layout2)
#устонавливаем горизонтальную линию в группбокс
radiogroup.setLayout(h_layout1)
#создаем главную вертикальную линию
layout = QVBoxLayout()
#размищаем на вертикальные виджеты
layout.addWidget(quetion,alignment = Qt.AlignCenter)
layout.addWidget(radiogroup,alignment = Qt.AlignCenter)
layout.addWidget(ans_radiogroup,alignment = Qt.AlignCenter)
ans_radiogroup.hide()
layout.addWidget(lamda,alignment = Qt.AlignCenter)
at.setLayout(layout)
#функция показывающая результат
def show_result():
    radiogroup.hide()
    ans_radiogroup.show()
    lamda.setText('Следующий вопрос')
#функция которая показыает вопрос
def show_question():
    radiogroup.show()
    ans_radiogroup.hide()
    lamda.setText('Ответить')
    radiogroup_box.setExclusive(False)
    rbt1.setChecked(False)
    rbt2.setChecked(False)
    rbt3.setChecked(False)
    rbt4.setChecked(False)
    radiogroup_box.setExclusive(True)
answers = [rbt1,rbt2,rbt3,rbt4]
#функция записывает значенение вопроса и ответов в соотвествующие виджеты 
# при этом варианты ответов распроделяются случайным образом 
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.Right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    quetion.setText(q.question)
    Right_ans.setText(q.Right_answer)
    show_question()
#показать результат
def show_corect(res):
    Result.setText(res)
    show_result()
#проверка выброного варианта ответа
def cheak_answer():
    if answers[0].isChecked():
        show_corect('Правильно!')
        at.score +=1
        print('Статистика \n- Всего вопросов: ', at.total,'\n- Правильных ответов: ', at.score)
        print('Рейтинг', (at.score/at.total*100),'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_corect('Неверно!')
            print('Рейтинг', (at.score/at.total*100),'%')
#задаем случайный вопрос из списка
def next_quetion():
    at.total+=1 
    print('Статистика \n- Всего вопросов: ', at.total,'\n- Правильных ответов: ', at.score)
    random_quetion = randint(0,len(questions)-1)
    q = questions[random_quetion]
    ask(q)
#определяем надоли показать другой вопрос или проверить ответ на этот
def cleek_Ok(): 
    if lamda.text()=='Ответить':
        cheak_answer()
    else:
        next_quetion()
lamda.clicked.connect(cleek_Ok)#при нажатии на кнопку выбераем что конкретно происходит
#финал
at.score = 0
at.total = 0
next_quetion()
at.show()
app.exec_()
