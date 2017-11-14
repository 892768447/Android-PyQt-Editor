#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2017年11月9日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: MainWindow
@description: 
"""
import sys

from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QLabel,\
    QSwipeGesture, QGestureRecognizer
import chardet

from library import Lexers
from library.EditorWidget import EditorWidget
from library.QStandardGestures import QSwipeGestureRecognizer


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2017 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)
        self.editorWidget = EditorWidget(self)
        layout.addWidget(self.editorWidget)

        file = 'MainWindow.py'
        print(file)
        lexer = Lexers.get_lexer_by_ext(file)
        self.editorWidget.setLexer(lexer())
        with open(file, 'rb') as fp:
            text = fp.read()
            encoding = chardet.detect(text)
            self.editorWidget.setText(text.decode(
                encoding.get('encoding', 'utf-8')))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
