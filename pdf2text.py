from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
from io import StringIO
import os.path

dir = os.path.dirname(__file__)
pdf = os.path.join(dir, "3001.pdf")
ifp = open(pdf, 'rb')
ofp = StringIO()

rmgr = PDFResourceManager()
lprm = LAParams()
device = TextConverter(rmgr, ofp, codec='utf-8', laparams=lprm)
pintr = PDFPageInterpreter(rmgr, device)

for page in PDFPage.get_pages(ifp):
    pintr.process_page(page)

text = ofp.getvalue()

ofp.close()
device.close()
ifp.close()

print(text)

