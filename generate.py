#!/usr/bin/env python3

from subprocess import call


people = {
          'tapira': {
                  'title': 'Prof.',
                  'firstname': 'Manuella',
                  'lastname': 'de Tapir',
                  'street': '135th Random ave.',
                  'zip': '04199',
                  'city': 'Nowhere',
                  'state': 'Alaska'
                  },
          'tom': {
                  'title': '',
                  'firstname': 'Tom',
                  'lastname': 'Bond',
                  'street': '12th fake street',
                  'zip': '12202',
                  'city': 'Albany',
                  'state': 'New-York'
                  },
          'danny': {
                  'title': 'Dr.',
                  'firstname': 'Danny',
                  'lastname': 'Mendel',
                  'street': '1st 1337 way',
                  'zip': '12345',
                  'city': 'Springfield',
                  'state': 'Washington'
                  },
          }


for filename, person in people.items():
    define = '"'
    for key, val in person.items():
        define += '\\def\\{}{{{}}}'.format(key, val)
    define += '\input{letter}"'
    cmd = ['pdflatex', '--shell-escape', '-jobname={}'.format(filename), define]
    print(' '.join(cmd))
    call(cmd)
