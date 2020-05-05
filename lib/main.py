from peewee import *
from random import randint

db = PostgresqlDatabase('question', user='postgres',
                        password='', host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Question(BaseModel):
    front = CharField()
    back = CharField()


db.drop_tables([Question])
db.create_tables([Question])

first = Question(front='It became widely known as the UNIX operating system''s development language.', back='C')
first.save()

second = Question(front='A general-purpose, concurrent, class-based, object-oriented computer programming language', back='Java')
second.save()

third = Question(front='Open-source, closs platform object orientated, Ruby on rails', back='Ruby')
third.save()

fourth = Question(front='A high-level programming language that emphasizes code readability.', back='Python')
fourth.save()

fifth = Question(front='It is the most widely used scripting language and used  to add programmability to web pages.', back='JavaScript')
fifth.save()

sixth = Question(front='A scripting languages to be embedded into an HTML source document rather than calling an external file to process data.', back='PHP')
sixth.save()

seventh = Question(front='It is the second-oldest high-level programming language (FORTRAN is the oldest).', back='COBOL')
seventh.save()

eigth = Question(front='The oldest high-level programming language.', back='FORTRAN')
eigth.save()

ninth = Question(front='A high-level, general-purpose, interpreted language to make  Unix scripting report processing easier.', back='perl')
ninth.save()

tenth = Question(front='It provides a number of features that "spruce up" the C language, but provides capabilities for OOP.', back='C++')
tenth.save()

def menu():
    print("Will you like to Play, Create a card or Review")
    choice = input('Type: P to Play \tC to Create \tR to Review\n')
    if choice == 'C' or choice == 'c':
        create()
    elif choice == 'R' or choice == 'r': 
        read()
    elif choice == 'P' or choice == 'p': 
        play_game()
    else: 
        print('Invalid input: P to Play \tC to Create or \tR to Review\n')
        menu()

def create():
    q = input("Enter a question you would like to add \n")
    a = input("Enter the answer \n")
    new = Question(front=q, back=a)
    new.save()
    print(f"Here is your new card: \nfront:{new.front} and back:{new.back}")
    menu()

def read():
    for card in Question.select(): 
        print(f"\nQuestion: {card.front} \nAnswer: {card.back}")
    menu()

def play_game():
    correct = 0
    i = int(input("How many cards would you like to study? "))
    total = i

# rand = Question.select().where(Question.id == randint(1,10))
# print([card.front for card in rand])


    for card in Question.select():
        if i > 0:
            i -= 1
            if input(f"{card.front}\n") == card.back:
                print(f"The answer is {card.back}")
                correct += 1
                print(f"Score: {correct}/{total}")

            else:
                print(f"The answer is {card.back}")
                print(f"Score: {correct}/{total}")

    percent = (correct/total)*100
    print(f"{percent}%")           
    play_again = str(input("Press Y to play again?  "))
    if play_again == 'Y' or play_again == 'y':
        play_game()
    else:
            menu()

menu()