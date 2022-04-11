import sys
from redminelib import Redmine


redmine =  Redmine(
    'https://redesgas-homolog.ufrn.br' , 
    key='ecd2aac8b0c5ddf6b3c690f847e8a37c7a7f9ed1', 
    requests={'verify': False})

redmine.issue.create(
    project_id=146,
    tracker_id=201,
    assigned_to_id=3382,
    subject='O host ' + sys.argv[1] + ' encontra-se com uma vulnerabilidade de nivel ' + sys.argv[2])