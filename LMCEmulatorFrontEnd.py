"""
MIT License

Copyright (c) 2015 Ethan Riley

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from PySide import *
import sys
import os

class window(QtGui.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ofdict={}
        self.initUI()
    def show(self):
        fname, _= QtGui.QFileDialog.getOpenFileName(self, 'Open File',
                '/home')
        self.ofdict[1]=fname
        try:
            af = open(fname, 'r')
            with af:
                data = af.read()
                self.textEdit.setText(data)
        except FileNotFoundError:
            self.delD      
    def font(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)
    def saveas(self):
        sname, _= QtGui.QFileDialog.getSaveFileName(self, 'Save File As',
                '/home')
        try:
            a= open(sname, 'w')
            self.ofdict[1]=sname
            txt=self.textEdit.toPlainText()
            with a:
                a.writelines(txt)
        except FileNotFoundError:
            pass
      
    def save(self):
        key= 1 in self.ofdict
        if key == True:
            try:
                txt=self.textEdit.toPlainText()
                data=self.ofdict[1]
                aof=open(data, 'w')
                with aof:
                    aof.writelines(txt)
            except FileNotFoundError:
                self.saveas()
        else:
            self.saveas()
    def delD(self):
        del(self.ofdict[1])
    def cut(self):
        self.textEdit.cut()
    def copy(self):
        self.textEdit.copy()
    def paste(self):
        self.textEdit.paste()
    def slctA(self):
        self.textEdit.selectAll()
    def print(self):
        self.textEdit.print_(QtGui.QPrinter())
    def undo(self):
        self.textEdit.undo()
    def redo(self):
        self.textEdit.redo()
    def run(self):
        os.system("LMCEmulator.exe")
        raw_input()
    def initUI(self):
        #main widget
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        #ACTS
        #save as
        saveasACT= QtGui.QAction(QtGui.QIcon('saveas.png'),'&Save As', self)
        saveasACT.setShortcut('Ctrl+Shift+S')
        saveasACT.setStatusTip('Save as your document')
        saveasACT.triggered.connect(self.saveas)
        #save
        saveACT= QtGui.QAction(QtGui.QIcon('save.png'),'&Save', self )
        saveACT.setShortcut('Ctrl+S')
        saveACT.setStatusTip('Save your document')
        saveACT.triggered.connect(self.save)
        #print
        printACT= QtGui.QAction(QtGui.QIcon('print.png'),'&Print', self)
        printACT.setShortcut('Ctrl+P')
        printACT.setStatusTip('print your document')
        printACT.triggered.connect(self.print)
        # run
        runAct = QtGui.QAction(QtGui.QIcon('run.png'), '&Run', self)
        runAct.setShortcut('Ctrl+R')
        runAct.setStatusTip('Run')
        runAct.triggered.connect(self.run)
        #exit
        killACT= QtGui.QAction(QtGui.QIcon('exit.png'),'&Exit', self)
        killACT.setShortcut('Ctrl+Q')
        killACT.setStatusTip('Exit')
        killACT.triggered.connect(self.close)
        #satusbar
        self.statusBar()
        #open
        openACT= QtGui.QAction(QtGui.QIcon('open.png'),'&Open', self)
        openACT.setShortcut('Ctrl+O')
        openACT.setStatusTip('open a file')
        openACT.triggered.connect(self.show)
        #cut
        cutACT= QtGui.QAction(QtGui.QIcon('cut.png'),'&Cut', self)
        cutACT.setShortcut('Ctrl+X')
        cutACT.setStatusTip('cut selcted')
        cutACT.triggered.connect(self.cut)
        #copy
        copyACT= QtGui.QAction(QtGui.QIcon('copy.png'),'&Copy', self)
        copyACT.setShortcut('Ctrl+C')
        copyACT.setStatusTip('copy selcted')
        copyACT.triggered.connect(self.copy)
        #paste
        pasteACT= QtGui.QAction(QtGui.QIcon('paste.png'),'&Paste', self)
        pasteACT.setShortcut('Ctrl+V')
        pasteACT.setStatusTip('paste from clipboard')
        pasteACT.triggered.connect(self.paste)
        #select all
        SAACT= QtGui.QAction(QtGui.QIcon('selectall.png'),'&Select All', self)
        SAACT.setShortcut('Ctrl+A')
        SAACT.setStatusTip('Select All')
        SAACT.triggered.connect(self.slctA)
        #font
        fontACT= QtGui.QAction(QtGui.QIcon('font.png'),'&Font', self)
        fontACT.setShortcut('Ctrl+F')
        fontACT.setStatusTip('change font')
        fontACT.triggered.connect(self.fontstuff)
        #undo
        undoACT= QtGui.QAction(QtGui.QIcon('undo.png'),'&Undo', self)
        undoACT.setShortcut('Ctrl+Z')
        undoACT.setStatusTip('undo your last change to your document')
        undoACT.triggered.connect(self.undo)
        #redo
        redoACT= QtGui.QAction(QtGui.QIcon('redo.png'),'&Redo', self)
        redoACT.setShortcut('Ctrl+Shift+Z')
        redoACT.setStatusTip('redo your last change to your document')
        redoACT.triggered.connect(self.redostuff)
        #window
        self.setGeometry(300,300,675,700)
        self.setWindowTitle('LMCEmulator')
        #menubar
        menubar = self.menuBar()
        #init bars
        fileM= menubar.addMenu('&File')
        editM= menubar.addMenu('&Edit')
        runM = menubar.addMenu('&Run')
        #edit actions
        editM.addAction(fontACT)
        editM.addAction(cutACT)
        editM.addAction(copyACT)
        editM.addAction(pasteACT)
        editM.addAction(SAACT)
        editM.addAction(redoACT)
        editM.addAction(undoACT)
        #file actions
        fileM.addAction(killACT)
        fileM.addAction(openACT)
        fileM.addAction(saveasACT)
        fileM.addAction(saveACT)
        fileM.addAction(printACT)
        self.show() 
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
        "Save document and quit?", QtGui.QMessageBox.Yes |
        QtGui.QMessageBox.No|QtGui.QMessageBox.Cancel,QtGui.QMessageBox.Cancel)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
            self.save()
            self.delD()
        elif reply == QtGui.QMessageBox.No:
            event.accept()
            self.delD()
        else:
            event.ignore()

        
def main():
    app= QtGui.QApplication(sys.argv)
    ex = window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
