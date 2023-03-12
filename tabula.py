import tabula as tb
import pandas as pd
import re


file = 'CAPR-III_6207-1.pdf'
data = tb.read_pdf(file, area = (214.583,39.398,640.688,581.018), pages = '1')

print(data)