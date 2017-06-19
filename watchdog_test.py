import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

watch_dirs = ['.']

def handle_event(event):
    print(str(event) + " modified\n")
    
def _handle(event):
    handle_event(event.src_path)
    
def _loop_darwin(loop_callback):
    observer = Observer()
    handler = _handle

    class EventHandler(FileSystemEventHandler):
        def dispatch(self, event):
            if event.event_type == 'modified':
                handler(event)

    event_handler = EventHandler()
    files = ['data/w1.txt', 'data/w2.txt', 'data/w3.txt']    
    for watch_this in files:
        observer.schedule(event_handler, 'data', recursive=False)

    observer.start()

    fd = open(files[0], 'w')
    fd.write("hi")
    fd.close()
    # write in non-watched file
    fd = open(files[2], 'w')
    fd.write("hi")
    fd.close()
    # write in another watched file
    fd = open(files[1], 'w')
    fd.write("hi")
    fd.close()

    try:
        while True:
            raise KeyboardInterrupt
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    
if __name__ == "__main__":
    _loop_darwin(None)
    ## logging.basicConfig(level=logging.INFO,
    ##                     format='%(asctime)s - %(message)s',
    ##                     datefmt='%Y-%m-%d %H:%M:%S')
    ## path = sys.argv[1] if len(sys.argv) > 1 else '.'
    ## event_handler = LoggingEventHandler()
    ## observer = Observer()
    ## observer.schedule(event_handler, path, recursive=True)
    ## observer.start()
    ## try:
    ##     while True:
    ##         time.sleep(1)
    ## except KeyboardInterrupt:
    ##     observer.stop()
    ## observer.join()
