import jpype
from jpype import java
import asposecells
jpype.startJVM()

from asposecells.api import Workbook, FileFormatType, JsonSaveOptions

try:
    workbook = Workbook("Book.xlsx")
    workbook.save("Book.json")
    jpype.shutdownJVM()
    print(f"Converção bem-sucedida")
except Exception as e:
    print(f"Ocorreu outro erro: {e} ")
