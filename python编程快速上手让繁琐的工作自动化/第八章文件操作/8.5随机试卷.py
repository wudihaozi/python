#�ڰ�����Ŀ����������Ĳ����Ծ�
#��һ�������������ݱ�����һ���ֵ���
import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield',
            'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort',
            'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh','North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond',
            'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
# �ڶ��������������ļ�����������˳��
# TODO: Create the quiz and answer key files.
for quizNum in range(35):
    quizFile = open('quiz-%s.txt' % (quizNum+1), 'w')
    answerFile = open('answer-%s.txt'% (quizNum+1), 'w')
    
    # TODO: Write out the header for the quiz.
    quizFile.write('Name: \nDate: \nPeriod: \n')
    quizFile.write(' '*20 +'State Capitals Quiz (Form %s)' % (quizNum+1))
    quizFile.write('\n\n')
    
    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
#��������������ѡ��
# TODO: Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        # TODO: Get wrong and right answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer,3)
        answerOption = wrongAnswer + [correctAnswer]
        random.shuffle(answerOption)
        
        # TODO: Write the question and answer options to the quiz file.
        quizFile.write('%s.What is the capital of %s?\n'%(questionNum+1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s'%('ABCD'[i], answerOption[i]))
        quizFile.write("\n")
        
        # TODO: Write the answer key to a file.
        answerFile.write('%s. %s \n' % (questionNum+1,'ABCD'[answerOption.index(correctAnswer)]))
    quizFile.close()
    answerFile.close()