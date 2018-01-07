import datetime
import random
import logging

logging.basicConfig(filename='quiz.log',level=logging.INFO)


class Quiz:
    questions = [
'When was tennis player, Martina Hingis, born?','When was tennis player, Martina Hingis, born?','When was tennis player, Martina Hingis, born?','When was tennis player, Martina Hingis, born?','What numbers appear on Donald Duck’s car plate?','What numbers appear on Donald Duck’s car plate?','What numbers appear on Donald Duck’s car plate?','What numbers appear on Donald Duck’s car plate?']
    answers = ['1980','1980','1980','1980','313','313','313','313']

    def __init__(self):
        # generate 10 random questions with numbers from 1 to 10
        randint = random.randint(3, len(self.questions))
        # add these questions into self.questions
        self.questions = self.questions[0:randint]
        self.answers = self.answers[0:randint]
        self.starttime = datetime.datetime.now()
        self.score = 0
        self.roud = 0

    def take_quiz(self):
        # log the start time
        logging.info('Round '+str(self.roud)+'- Questions rendered at: '+str(datetime.datetime.now()))
        # ask all of the questions
        for number in range(len(self.questions)):
            print(str(number) + ' ' + self.questions[number])

        ans = input('Choose your question number \n')
        qnumbers = [n for n in range(len(self.questions))]
        # log if they got the question right
        if int(ans) in qnumbers:
            userans = self.ask(ans)
            if userans:
                self.score += 1
                print('Great! Your answer is correct\n')
                print('Your score is: '+str(self.score))
            else:
                print('Sorry your answer is wrong\n')
        else:
            print('Wrong question number')

        cont = input('Would you like to continue? (y/n) \n')

        # log the end time
        if cont == 'y':
            self.roud += 1
            self.take_quiz()
        elif cont == 'n':
            self.summary()
            logging.info('Quiz end at: '+str(datetime.datetime.now()))
            exit()
        # show a summary

    def ask(self, question):
        # log the start time
        logging.info('Question rendered at: '+str(datetime.datetime.now()))
        # capture the answer
        userans = input('Your answer: ')
        rightans = self.answers[int(question)]
        # check the answer
        logging.info('User answered at: '+str(datetime.datetime.now()))
        if userans.lower() == rightans.lower():
            return True
        else:
            return False
        # log the end time
        # if the answer's right, send back True
        # otherwise, send back False
        # send back the elapsed time, too

    def summary(self):
        # print how many you got right and the total # of questions. 5/10
        print('Your total number of points is: '+str(self.score)+'\n')
        print('Your take rounds: '+str(self.roud)+'\n')
        # print the total time for the quiz: 30 seconds!
        time = datetime.datetime.now() - self.starttime
        print('Your quiz time is: '+ str(round(time.total_seconds()))+' seconds\n')
        if round(time.total_seconds()) <  30 and self.score > 2:
            print('Great you over game in less than 30s and you have {} points!!'.format(self.score))

newgame = Quiz()
newgame.take_quiz()
