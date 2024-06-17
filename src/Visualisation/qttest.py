import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QFrame
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 with Matplotlib and Video Stream")
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # self.figure, self.ax = plt.subplots()
        # self.canvas = FigureCanvas(self.figure)
        # self.main_layout.addWidget(self.canvas)
        
        self.video_frame = QFrame()
        self.video_frame.setFrameShape(QFrame.Box)
        self.video_frame.setFrameShadow(QFrame.Raised)
        self.video_frame.setLineWidth(12)
        self.main_layout.addWidget(self.video_frame)

        # Use a layout inside the video_frame to manage the video_label
        self.video_layout = QVBoxLayout(self.video_frame)
        self.video_label = QLabel(self.video_frame)
        self.video_layout.addWidget(self.video_label)



        # self.plot_example()
        


        self.capture = cv2.VideoCapture(0)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update frame every 30ms

        # self.plot_example()

    def plot_example(self):
        self.ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
        self.canvas.draw()

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            step = channel * width
            qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
            self.video_label.setPixmap(QPixmap.fromImage(qImg))

    def closeEvent(self, event):
        self.capture.release()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())