from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY, PLAIN_COLUMNS,MARKDOWN,ORGMODE,DOUBLE_BORDER
tb = PrettyTable(["test", "test1", "test2"])
# tb.set_style(DOUBLE_BORDER)
# tb.padding_width = 10
tb.padding_width = 2
# tb.header = False
# tb.border=False
tb.vertical_char = '+'
# tb.horizontal_align_char = ''
# tb.horizontal_char = "+"
tb.align = 'l'
tb.add_row(["asdasd", "ashbasd\nahsdbhabsdaksnjansdjnasndj\nasjdnajsd\najdjasbd", "asjkads\najsnjad\nsadjajsd"])
tb.add_row(["asdasd",'',''])
print(tb)
b=[2,4,5]
print([1,2,3,*b,4])