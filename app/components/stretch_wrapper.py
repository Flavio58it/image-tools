from PyQt5.QtWidgets import (QHBoxLayout, QFrame)


class NoStretch(QFrame):
	def __init__(self, widget):
		super().__init__()
		layout = QHBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		layout.addWidget(widget)
		layout.addStretch(1)
		self.setLayout(layout)
