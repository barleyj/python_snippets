def task_create_foo():
    return {
        'actions': ['touch foo', 'chmod 750 foo'],
        'targets': ['foo'],
        'verbosity': 2,
        'uptodate': [True]
        }

def task_on_foo_changed():
    # will execute if foo or its metadata is modified
    return {
        'actions': ['python process.py'],
        'file_dep': ['Assignment2.java', 'Card.java', 'Dealer.java', 'Deck.java', 'Hand.java', 'README.TXT', 'asgmt02.html', 'asgmt02.jardesc', 'asgmt02.out.txt', 'package.bluej'],
        'verbosity': 2
        }
