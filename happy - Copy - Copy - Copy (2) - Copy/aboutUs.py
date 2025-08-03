from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class AboutUsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()

        title = QLabel("<h2>Team Members</h2>")
        title.setAlignment(Qt.AlignCenter)

        members_info = """
        <b>Shristi Tamang</b><br>
        Email: <a href='mailto:leoshristi29@gmail.com'>leoshristi29@gmail.com</a><br><br>

        <b>Namrata Suwal</b><br>
       Email: <a href='mailto:suwalnamrata732@gmail.com'>suwalnamrata732@gmail.com</a><br><br>

        <b>Nimika K.C</b><br>
        Email: <a href='mailto:nimikakc@gmail.com'>nimikakc@gmail.com</a><br><br>


        <b>Muskan Shrestha</b><br>
        Email: <a href='mailto:muskan.sth17@gmail.com'>muskan.sth17@gmail.com</a>
        """

        members_label = QLabel(members_info)
        members_label.setOpenExternalLinks(True)
        members_label.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(members_label)
        layout.addStretch()

        self.setLayout(layout)