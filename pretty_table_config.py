from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY, PLAIN_COLUMNS, MARKDOWN, ORGMODE, DOUBLE_BORDER
FILE_IN = '../datain.txt'

def get_table(cols = []):
    tb = PrettyTable(cols)
    # tb.set_style(DOUBLE_BORDER)
    # tb.padding_width = 10
    # tb.padding_width = 2
    # tb.header = False
    # tb.border=False
    # tb.vertical_char = '+'
    # tb.horizontal_align_char = ''
    # tb.horizontal_char = "+"
    tb.align = 'l'
    # tb.hrules = 1
    return tb
