import glob


def task_test():
    return {'actions': ['py.test'],
            'file_dep': glob.glob('*.p'),
            }
