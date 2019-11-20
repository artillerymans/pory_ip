
import time


# strTime = time.strftime('%Y%m%d_%H%M%S', time.localtime())
#
# print(strTime)
#
# Utils.del_file()

#测试正则表达式

import re

chekcUrl = 'https://www.kuaidaili.com/free/inha/1/'
strMatch = r'.+www.kuaidaili.com/free/inha/[0-9]/$'
m = re.match(strMatch, chekcUrl)
print(m.group(0))




