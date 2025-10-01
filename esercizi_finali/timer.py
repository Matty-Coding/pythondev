# TIMER CON NOTIFICA DESKTOP

# crea un timer
# manda una notifica desktop (modulo plyer)
# bonus: aggiungi suono (modulo playsound)

import time
from plyer import notification

time.sleep(3)
notification.notify(title="Timer", message="HALOOOO", timeout=5)