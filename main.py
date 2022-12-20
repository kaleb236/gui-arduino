import sys
import serial
from PyQt5.QtWidgets import QApplication
from final_project import Ui_MainWindow

from PyQt5.QtWidgets import *

arduino = serial.Serial('COM3', baudrate=9600)

class ui_windows(QMainWindow):
    def __init__(self):
        super(ui_windows, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.rgb_bool = True

        self.ui.pushButton_mesafetara.clicked.connect(self.mesafe)
        self.ui.pushButton_ldrdeger.clicked.connect(self.ldr)
        self.ui.rgb.clicked.connect(self.rgb)  
        self.ui.pushButton_servorun.clicked.connect(self.servo)
        self.ui.pushButton_servostop.clicked.connect(self.servo_stop)
        self.ui.pushButton_dcrun.clicked.connect(self.dcrun)
    
    def mesafe(self):
        mes = arduino.readline().decode("ascii")
        self.ui.label_2.setText(f"{mes.split(',')[0]} cm")

    def rgb(self):
        if self.rgb_bool:
            arduino.write(b'r')
            self.rgb_bool = False
        else:
            arduino.write(b'o')
            self.rgb_bool = True
    
    def ldr(self):
        mes = arduino.readline().decode("ascii")
        self.ui.label.setText(mes.split(',')[1])
    
    def servo(self):
        arduino.write(b's')
    
    def servo_stop(self):
        arduino.write(b't')

    def dcrun(slef):
        arduino.write(b'm')
    
    def dcstop(self):
        arduino.write(b'd')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ui_windows()

    win.show()
    sys.exit(app.exec_())