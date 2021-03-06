#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-

from random import shuffle
import pickle


class Answer:
    """
    Has a text (a_str), can be either correct or not
    (the variable "type" holds that info).
    """
    def __init__(self, a_str='', type=False):
        self.a_str = a_str
        self.type = type

    """
    If with_sol is true and the answer is correct,
    prints the answer in bold type. Otherwise prints the
    answer normally.
    """
    def print(self, with_sol=False):
        if with_sol and self.type == True:
            return '\\textbf{{{}}}'.format(self.a_str)
        else:
            return self.a_str


class Question:
    """
    Has a text (q_str), and number of points.
    Holds a list of answers (defauly empty).
    """
    def __init__(self, q_str='', num_points=1):
        self.q_str = q_str
        self.answers = []
        self.num_points = num_points

    def add_answer(self, answer):
        """
        Adds answer to list of answers of the question.
        """
        self.answers.append(answer)

    def randomize_answers(self):
        """
        Randomizes the order of the answers.
        """
        shuffle(self.answers)

    def print_latex(self, with_sol=False):
        """
        Prints the question + answers in LaTeX format.
        """
        out_str = '''
        (\\textbf{{{} points)}} {}

        \\begin{{enumerate}}
        {}
        \\end{{enumerate}}
        '''.format(
                    self.num_points,
                    self.q_str,
                    ' '.join(['\\item {}\n'.format(answer.print(with_sol))
                              for answer in self.answers]),
                )
        print(out_str)


if __name__ == '__main__':
    q1 = Question(q_str='Which of the following statements is not correct regarding cathode rays?',
                  num_points=3)
    q1.add_answer(Answer('The rays carry negative charge', False))
    q1.add_answer(Answer('The charge/mass of these rays is considerably smaller than for positive rays', False))
    q1.add_answer(Answer('The rays produce mechanical effect', False))
    q1.add_answer(Answer('The charge/mass ratio is independent of the nature of the gas taken in the discharge tube', True))

    q2 = Question(q_str='The nucleides X and Y are isotonic to each other with mass numbers 70 and 72 respectively. If the atomic number of X is 34, then that of Y would be:',
                  num_points=5,
                  )
    q2.add_answer(Answer('32', False))
    q2.add_answer(Answer('34', False))
    q2.add_answer(Answer('36', True))
    q2.add_answer(Answer('38', False))

    q3 = Question(q_str='Isobars have same number of:',
                  num_points=2,
                  )
    q3.add_answer(Answer('Protons', False))
    q3.add_answer(Answer('Electrons', False))
    q3.add_answer(Answer('Neutrons', True))
    q3.add_answer(Answer('Nucleons', False))
    
    q4 = Question(q_str='Which of the following elements are halogens? (choose all correct answers)',
                  num_points=2,
                  )
    q4.add_answer(Answer('He', False))
    q4.add_answer(Answer('Li', False))
    q4.add_answer(Answer('Cl', True))
    q4.add_answer(Answer('N', False))
    q4.add_answer(Answer('Br', True))
    q4.add_answer(Answer('Na', False))

    questions = [q1, q2, q3, q4]
    pickle.dump(questions, open('questions.p', 'wb'))
