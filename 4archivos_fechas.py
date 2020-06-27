import os
from datetime import datetime

files=os.listdir()
for f in files:
    last_update_at=os.path.getmtime(f)
    
    print(f'{f}   {last_update_at}')
