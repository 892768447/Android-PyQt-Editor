#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017年11月9日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: library.widgets.ScintillaWidget
@description: 
"""
from PyQt5.Qsci import QsciScintilla, QsciLexerPython
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QFont, QColor, QFontMetrics
import chardet

from library import Settings


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2017 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class ScintillaWidget(QsciScintilla):

    def __init__(self, *args, **kwargs):
        super(ScintillaWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_InputMethodEnabled, False)  # for android
        self._lexer = QsciLexerPython(self)
        self.setLexer(self._lexer)
        self.init()
        self.initStyle()

    def init(self):
        # 折叠前后颜色?
        #         self.setFoldMarginColors(fore, back)
        # 设置提示显示方式,参考http://pyqt.sourceforge.net/Docs/QScintilla2/classQsciScintilla.html#a3793111b6e2a86351c798c68deda7d0c
        self.setAnnotationDisplay(self.AnnotationBoxed)
        # 自动提示-不区分大小写
        self.setAutoCompletionCaseSensitivity(False)
        # 自动提示-填充字符
#         self.setAutoCompletionFillups(fillups)
        # 自动提示-启用填充字符?
#         self.setAutoCompletionFillupsEnabled(False)
        # 自动提示-删除当前字符右侧的其它单词
#         self.setAutoCompletionReplaceWord(False)
        # 自动提示-single=true列表只有一个时,不显示,被setAutoCompletionUseSingle代替
#         self.setAutoCompletionShowSingle(False)
        # 参考http://pyqt.sourceforge.net/Docs/QScintilla2/classQsciScintilla.html#ac466f32c3d7e51790b6b25c864783179
        self.setAutoCompletionSource(self.AcsAll)
        # 自动提示-输入一个单词就触发提示
        self.setAutoCompletionThreshold(1)
        # 参考http://pyqt.sourceforge.net/Docs/QScintilla2/classQsciScintilla.html#ae628d46489efa3db3b0c42336a1bf8d3
#         self.setAutoCompletionUseSingle(self.AcusNever)
        # 自动提示-单词分隔符,如果设置了lexer则忽略此设置
#         self.setAutoCompletionWordSeparators(separators)
        # 自动缩进
        self.setAutoIndent(True)
        # 当一行没有其它字符时删除前面的缩进
        self.setBackspaceUnindents(True)
        # 括号匹配,参考http://pyqt.sourceforge.net/Docs/QScintilla2/classQsciScintilla.html#ae8277ccb3a2af0ae9a1495d8f8ea0523
        self.setBraceMatching(self.StrictBraceMatch)  # 严格模式
        # 设置提示背景颜色
        self.setCallTipsBackgroundColor(Qt.white)
        # 设置提示前景颜色
        self.setCallTipsForegroundColor(Qt.darkGray)
        # 设置提示高亮颜色
        self.setCallTipsHighlightColor(Qt.darkBlue)
        # 设置提示位置,参考http://pyqt.sourceforge.net/Docs/QScintilla2/classQsciScintilla.html#aef97a9061de95a09b57d527f6410881d
        self.setCallTipsPosition(self.CallTipsBelowText)  # 文字下方
        # 设置提示样式
        self.setCallTipsStyle(self.CallTipsNoContext)
        # 设置插入字符前景颜色
#         self.setCaretForegroundColor()
        # 设置插入线背景颜色
#         self.setCaretLineBackgroundColor()
        # 设置是否显示插入线
#         self.setCaretLineVisible(True)
        # 设置插入字符宽度
#         self.setCaretWidth(1)
        # 设置很多颜色
#         self.setColor()
        #
#         self.setContractedFolds(    const QList< int > &     folds)
        #
#         self.setEdgeColor()
        #
#         self.setEdgeColumn()
        # 参考http://pyqt.sourceforge.net/Docs/QScintilla2/classQsciScintilla.html#a40b8ec37e068b12d9c83ee497929a00e
#         self.setEdgeMode()
        # 设置换行模式?参考http://pyqt.sourceforge.net/Docs/QScintilla2/classQsciScintilla.html#ab4b6b4286a74e173a86de0a7f55241d5
        # 默认为和系统相关
#         self.setEolMode()
        #
#         self.setEolVisibility(True)
        # Sets the extra space added to the height of a line above the baseline of the text to extra.
#         self.setExtraAscent()
        # Sets the extra space added to the height of a line below the baseline of the text to extra.
#         self.setExtraDescent()
        # Set the number of the first visible line to linenr.
#         self.setFirstVisibleLine()
        # 设置折叠边距的折叠样式,参考http://pyqt.sourceforge.net/Docs/QScintilla2/classQsciScintilla.html#ae478a896ae32a30e8a375049a3d477e0
        self.setFolding(self.CircledTreeFoldStyle, 2)  # 圆形正负号
        # The fold margin may be drawn as a one pixel sized checkerboard
        # pattern of two colours, fore and back.
        self.setFoldMarginColors(Qt.red, Qt.yellow)
        # Sets the background colour of an active hotspot area to col.
#         self.setHotspotBackgroundColor()
        # Sets the foreground colour of an active hotspot area to col.
#         self.setHotspotForegroundColor()
        # 启用活动热点区域的下划线
        self.setHotspotUnderline(True)
        # Enables or disables, according to enable, the wrapping of a hotspot
        # area to following lines. The default is true.
        self.setHotspotWrap(True)
        # Sets the indentation of line line to indentation characters.
#         self.setIndentation(int line, int indentation)
        # 缩进指南?Enables or disables, according to enable, this display of
        # indentation guides.
        self.setIndentationGuides(True)
        # 缩进指南背景颜色Set the background colour of indentation guides to col.
#         self.setIndentationGuidesBackgroundColor()
        # 缩进指南前景颜色Set the foreground colour of indentation guides to col.
#         self.setIndentationGuidesForegroundColor()
        # 不使用tab
        self.setIndentationsUseTabs(False)
        # 缩进空格数量
        self.setIndentationWidth(4)
        # Enables or disables, according to under, if the indicator indicatorNumber is drawn under or over the text (i.e. in the background or foreground). If indicatorNumber is -1 then the state of all indicators is set.
#         self.setIndicatorDrawUnder(bool under, int indicatorNumber = -1)
        # Set the foreground colour of indicator indicatorNumber to col. If indicatorNumber is -1 then the colour of all indicators is set.
#         self.setIndicatorForegroundColor(QColor col, int indicatorNumber = -1)
        # Set the foreground colour of indicator indicatorNumber to col when the mouse is over it or the caret moved into it. If indicatorNumber is -1 then the colour of all indicators is set.
        # self.setIndicatorHoverForegroundColor(col, indicatorNumber =-1)
        # Set the style of indicator indicatorNumber to style when the mouse is over it or the caret moved into it. If indicatorNumber is -1 then the style of all indicators is set.
        # 参考http://pyqt.sourceforge.net/Docs/QScintilla2/classQsciScintilla.html#a3333f3a47163153c1bd7db1a362b8974
#         self.setIndicatorHoverStyle(style, indicatorNumber=-1)
        # Set the outline colour of indicator indicatorNumber to col. If indicatorNumber is -1 then the colour of all indicators is set. At the moment only the alpha value of the colour has any affect.
#         self.setIndicatorOutlineColor(col, indicatorNumber=-1)
        # 页边空白背景色
#         self.setMarginBackgroundColor(int margin,col)
        # Enables or disables, according to lnrs, the display of line numbers in margin margin.
#         self.setMarginLineNumbers(int margin, bool lnrs)
        # Sets the marker mask of margin margin to mask. Only those markers whose bit is set in the mask are displayed in the margin.
#         self.setMarginMarkerMask(int margin, int mask)
        # 设置边距选项
#         self.setMarginOptions(int options)
        # Set the number of margins to margins.设置边距
#         self.setMargins(int margins)
        # 设置边距背景颜色
        self.setMarginsBackgroundColor(Qt.gray)
        #
#         self.setMarginSensitivity(int margin, bool sens)
        # 设置边距字体
#         self.setMarginsFont(font)
        # 设置边距前景颜色
        self.setMarginsForegroundColor(Qt.black)
        # Set the margin text of line line with the text text using the style number style.
#         self.setMarginText(int line, const QString &text, int style)
        # Set the margin text of line line with the text text using the style style.
#         self.setMarginText(int line, const QString &text, const QsciStyle &style)
        #
#         self.setMarginText(int line, const QsciStyledText &text)
        # Set the margin text of line line with the list of styled text text.
#         self.setMarginText(int line, const QList< QsciStyledText > &text)
        # 设置边距类型,参考http://pyqt.sourceforge.net/Docs/QScintilla2/classQsciScintilla.html#aedab060e87e0533083ea8f1398302090
#         self.setMarginType(int maring, MarginType type)
        # 设置边框宽度
#         self.setMarginWidth(int margin, int width)
#         self.setMarginWidth(int margin, QString s)
        # Set the background colour, including the alpha component, of marker markerNumber to col. If markerNumber is -1 then the colour of all markers is set. The default is white.
#         self.setMarkerBackgroundColor(Qt.white,-1)
        # Set the foreground colour of marker markerNumber to col. If
        # markerNumber is -1 then the colour of all markers is set. The default
        # is black.
#         self.setMarkerForegroundColor(Qt.black)

        # 设置默认utf8编码
        self.setUtf8(True)

    def i(self):
        #         self.SendScintilla(self.SCI_SETCODEPAGE, self.SC_CP_UTF8)
        # BRACE MATCHING
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        # CURRENT LINE
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor('#2D2D2D'))
        self.setCaretForegroundColor(QColor('white'))
        # TABS
        self.setIndentationsUseTabs(False)
        self.setIndentationWidth(4)
        self.setTabIndents(True)
        self.setAutoIndent(True)
        self.setBackspaceUnindents(True)
        self.setTabWidth(4)
        # INDENTATION GUIDES
        self.setIndentationGuides(True)
        # FOLDING MARGIN
        self.setFolding(QsciScintilla.PlainFoldStyle)
        self.setMarginWidth(2, 8)  # (2,14)
        # FOLDING MARKERS
        self.markerDefine('-', QsciScintilla.SC_MARKNUM_FOLDEROPEN)
        self.markerDefine('+', QsciScintilla.SC_MARKNUM_FOLDER)
        self.markerDefine('-', QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
        self.markerDefine('+', QsciScintilla.SC_MARKNUM_FOLDEREND)
        # FOLDING LINE DISABLE
        self.SendScintilla(QsciScintilla.SCI_SETFOLDFLAGS, 0)
        # WHITESPACE
        self.setWhitespaceVisibility(QsciScintilla.WsVisible)
        self.setWhitespaceSize(1)
        # DISABLE HORIZONTAL SCROLLBAR
        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)

    def initStyle(self):
        # FONT
        font = self.font() or QFont()
        font.setFamily(Settings.FONT_FAMILY)
        font.setFixedPitch(True)
        font.setPointSize(13)
        self.setFont(font)
        self.setMarginsFont(font)

        # DEFAULT BACKGROUND AND FOREGROUND
        self.setPaper(QColor(Settings.BACKGROUND_COLOR))
        self.setColor(QColor(Settings.FOREGROUND_COLOR))

        # MARGIN LINE NUMBERS
        fontmetrics = QFontMetrics(font)
        self.setMarginsFont(font)
        self.setMarginWidth(0, fontmetrics.width('00000') + 4)
        self.setMarginLineNumbers(0, True)

        # MARGIN BACKGROUND AND FOREGROUND
        self.setMarginsBackgroundColor(QColor(Settings.MARGIN_BACKGROUND))
        self.setMarginsForegroundColor(QColor(Settings.MARGIN_FOREGROUND))

        # EDGE LINE
        # self.setEdgeMode(QsciScintilla.EdgeLine)
        # self.setEdgeColumn(150)
        # self.setEdgeColor(QColor(EDGE_COLOR))

        # SELECTION BACKGROUND AND FOREGROUND
        self.setSelectionBackgroundColor(QColor(Settings.SEL_BACKGROUND))
        self.setSelectionForegroundColor(QColor(Settings.SEL_FOREGROUND))

        # TABS BACKGROUND AND FOREGROUND
        self.setIndentationGuidesBackgroundColor(
            QColor(Settings.IND_BACKGROUND))
        self.setIndentationGuidesForegroundColor(
            QColor(Settings.IND_FOREGROUND))

        # FOLDING MARKERS BACKGROUND AND FOREGROUND
        self.setMarkerBackgroundColor(QColor(Settings.MARKER_BACKGROUND))
        self.setMarkerForegroundColor(QColor(Settings.MARGIN_FOREGROUND))
        self.setFoldMarginColors(QColor(Settings.FOLD_MARGIN_BACKGROUND), QColor(
            Settings.FOLD_MARGIN_BACKGROUND))

        # set lexer style
        self._lexer.setFont(self.font())
        self._lexer.setPaper(QColor(Settings.BACKGROUND_COLOR))
        for key, value in Settings.TEMPORARY.items():
            try:
                self._lexer.setColor(QColor(value), getattr(self._lexer, key))
            except Exception as e:
                print('Warning: ', e)

    def event(self, event):
        if(event.type() == QEvent.Gesture):
            return self.gestureEvent(event)
        return super(ScintillaWidget, self).event(event)

    def gestureEvent(self, event):
        '''gesture event'''
        event = event.gesture(Qt.TapAndHoldGesture)
        if event:  # mouse long click
            # show popup widget
            pos = event.position()
            if pos and not pos.isNull():
                self.toolPopupWidget.show(pos.toPoint())
        return True


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = ScintillaWidget()
    w.show()
    file = 'ScintillaWidget.py'
    with open(file, 'rb') as fp:
        text = fp.read()
        encoding = chardet.detect(text)
        print('encoding: ', encoding)
        w.setText(text.decode(encoding['encoding']))
    sys.exit(app.exec_())
