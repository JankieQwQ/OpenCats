
import server
import _thread

_thread.start_new_thread(server.run(),())

while True:pass