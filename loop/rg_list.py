import os

GROUP1 = 'test1'
GROUP2 = 'test2'
GROUP3 = 'test3'

GROUP_NAME_LIST = [
'%s-%s' %(os.environ['USERNAME'], GROUP1),
'%s-%s' %(os.environ['USERNAME'], GROUP2),
'%s-%s' %(os.environ['USERNAME'], GROUP3)
]
