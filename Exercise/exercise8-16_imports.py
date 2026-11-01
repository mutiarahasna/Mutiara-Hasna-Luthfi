# 1. import module_name
import module16
module16.say_hello("Mutiara")

# 2. from module_name import function_name
from module16 import say_hello
say_hello("Mutiara")

# 3. from module_name import function_name as fn (menggunakan alias fungsi)
from module16 import say_hello as sh
sh("Mutiara")

# 4. import module_name as mn (menggunakan alias modul)
import module16 as mm
mm.say_hello("Mutiara")

# 5. from module_name import * (mengimpor semua fungsi sekaligus)
from module16 import *
say_hello("Mutiara")