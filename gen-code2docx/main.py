from docxtpl import DocxTemplate
import glob
from util import get_data

data = {'row_c':get_data()}

doc = DocxTemplate("tpl.docx") # ดึงไฟล์ Template เข้ามา
doc.render(data) # เพิ่มข้อมูลลงไฟล์
doc.save("generated_doc.docx") # ส่งออกข้อมูลในไฟล์ใหม่ชื่อ generated_doc.docx