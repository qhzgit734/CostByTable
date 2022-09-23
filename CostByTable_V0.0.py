# 导入内置库
import sys
import os
# 导入第三方库
from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QWidget, QStyleFactory
from PySide2.QtGui import QIcon, QDesktopServices
import pandas as pd
import datacompy
# 导入.py文件
from qt.uic import win_main_uic, win_h_uic

# 设置全局变量
# 公共
columns_data = []
index_key = []
# 数据库
path_data = ''
sheet_data = ''
nan_key = []
ex_key = []
# 目标文件
path_target = ''
sheet_target = ''
orwt = bool
n4 = int()
# 清单对比
path_cpr = ''
path_cpr_new = ''
sheet_cpr1 = ''
sheet_cpr2 = ''
cpr_key = []
rpt = ''
cpr_info = ''

# 类-process
class PandasPro:
    
    def __init__(self):
        # 设置对齐
        pd.set_option('display.unicode.ambiguous_as_wide', True)
        pd.set_option('display.unicode.east_asian_width', True)
        
    def process(self):
        global n4
        # 读取excel 
        df1 = pd.read_excel(path_data, sheet_name=sheet_data, header=0)
        df2 = pd.read_excel(path_target, sheet_name=sheet_target, header=0)
        # 数据处理
        # 当为多个依据的list时，dropna只要有一个依据空就删整行，drop_duplicates多个依据组合在一起重复才会删除整行
        df1.dropna(subset=index_key, inplace=True)
        df1.drop_duplicates(subset=index_key, inplace=True)
        pro_df1 = df1.set_index(index_key, drop=False)
        
        pro_df2 = df2.set_index(index_key, drop=False)
        pro_df2.update(pro_df1, overwrite=orwt, filter_func=None)

        # 数据匹配数量统计
        or_df1 = pro_df1.copy().fillna('NAN')
        or_df2 = df2.copy().set_index(index_key, drop=False)
        or_df3 = df2.copy().set_index(index_key, drop=False)
        or_df2.update(or_df1, overwrite=orwt, filter_func=None)
        new_df2 = or_df2.copy()
        c = new_df2.compare(or_df3)
        n4 = len(c.index)
        print('匹配数:' + str(n4))
        # 保存excel
        path_target1 = os.path.join(os.path.dirname(path_target), '匹配结果.xlsx')
        if os.path.isfile(path_target1):
            with pd.ExcelWriter(path_target1, mode='a', if_sheet_exists='replace') as writer:
                pro_df2.to_excel(writer, sheet_name=sheet_target, index=False)
        else:
            pro_df2.to_excel(path_target1, sheet_name=sheet_target, index=False)
            
    def export(self):
        # 读取excel
        ex_df1 = pd.read_excel(path_data, sheet_name=sheet_data, header=0)
        # 数据处理
        # ex_df1.columns = columns_data
        # ex_df1.set_index(index_key, drop=True, inplace=True)
        ex_df1.dropna(subset=nan_key, inplace=True)
        ex_df1.drop_duplicates(subset=ex_key, inplace=True)
        # 保存excel
        path_data1 = os.path.join(os.path.dirname(path_data), '数据库.xlsx')
        with pd.ExcelWriter(path_data1) as writer:
            ex_df1.to_excel(writer, sheet_name=sheet_data, index=False)
        
    def cpr(self):
        global rpt, cpr_info
        # 读取excel
        df1 = pd.read_excel(path_cpr, sheet_name=sheet_cpr1, header=0)
        df2 = pd.read_excel(path_cpr_new, sheet_name=sheet_cpr2, header=0)
        # 对比excel
        c = datacompy.Compare(df1=df1, df2=df2, join_columns=cpr_key, ignore_spaces=True)
        df_intst = c.intersect_rows
        df_mis = c.all_mismatch()
        df1_unq_rows = c.df1_unq_rows
        df2_unq_rows = c.df2_unq_rows
        rpt = c.report()

        x1 = len(df_intst.index)
        x2 = len(df1.index)
        x3 = len(df2.index)
        y1 = len(df_mis.index)
        y2 = len(df1_unq_rows.index)
        y3 = len(df2_unq_rows.index)
        cpr_info = '对比概况:' + '\n' + \
                   '共用清单项数据变化量:' + str(y1) + '/' + str(x1) + '\n' + \
                   '旧清单减少:' + str(y2) + '/' + str(x2) + '\n' + \
                   '新清单增加:' + str(y3) + '/' + str(x3) + '\n' + \
                   '详见源目录:对比结果.xlsx'
        # 保存文件
        path_ex = os.path.join(os.path.dirname(path_cpr_new), '对比结果.xlsx')
        with pd.ExcelWriter(path_ex) as writer:
            df_mis.to_excel(writer, sheet_name='共用清单项数据变化')
            df1_unq_rows.to_excel(writer, sheet_name='旧清单减少')
            df2_unq_rows.to_excel(writer, sheet_name='新清单增加')
# 类-主窗口
class CreatRoot(QMainWindow):
    
    def __init__(self, Ui_file):
        super().__init__()
        # 创建主窗口
        self.win = QMainWindow()
        # 创建Ui_MainWindow的实例
        self.win_ui = Ui_file.Ui_MainWindow()
        # 调用setupUi在指定窗口(主窗口)中添加控件
        self.win_ui.setupUi(self.win)
        self.win_ui.pushButton.clicked.connect(self.import_file)
        self.win_ui.pushButton_2.clicked.connect(self.import_file)
        self.win_ui.pushButton_3.clicked.connect(self.repeat)
        self.win_ui.pushButton_4.clicked.connect(self.expt)
        self.win_ui.actionhelp.triggered.connect(lambda: self.open_win(window_help))
        self.win_ui.pushButton_5.clicked.connect(self.import_file)
        self.win_ui.pushButton_6.clicked.connect(self.import_file)
        self.win_ui.pushButton_7.clicked.connect(self.compr)
        self.win_ui.pushButton_8.clicked.connect(self.ex)
        self.win_ui.pushButton_9.clicked.connect(self.ex)
        self.win_ui.pushButton_10.clicked.connect(self.ex)
        self.win_ui.pushButton_11.clicked.connect(self.ex)
        self.win_ui.comboBox.currentIndexChanged.connect(self.cbx)
        self.win_ui.comboBox_2.currentIndexChanged.connect(self.cbx)
        self.win_ui.comboBox_3.currentIndexChanged.connect(self.cbx)
        self.win_ui.comboBox_4.currentIndexChanged.connect(self.cbx)
        
    def cbx(self):
        global sheet_data, sheet_target, sheet_cpr1, sheet_cpr2

        if self.sender().objectName() == 'comboBox':
            sheet_data = self.win_ui.comboBox.currentText()

        elif self.sender().objectName() == 'comboBox_2':
            sheet_target = self.win_ui.comboBox_2.currentText()

        elif self.sender().objectName() == 'comboBox_3':
            sheet_cpr1 = self.win_ui.comboBox_3.currentText()

        elif self.sender().objectName() == 'comboBox_4':
            sheet_cpr2 = self.win_ui.comboBox_4.currentText()
        else:
            pass
        
    def ex(self):
        global nan_key, ex_key, index_key, cpr_key
        text_list = self.win_ui.listWidget.selectedItems()
        text = [i.text() for i in list(text_list)]
        
        if self.sender().objectName() == 'pushButton_8':
            nan_key = text
            self.win_ui.label_13.setText('去空值依据:' + str(nan_key))
        elif self.sender().objectName() == 'pushButton_9':
            ex_key = text
            self.win_ui.label_14.setText('去重复项依据:' + str(ex_key))
        elif self.sender().objectName() == 'pushButton_10':
            index_key = text
            self.win_ui.label_2.setText('匹配依据:' + str(index_key))
        elif self.sender().objectName() == 'pushButton_11':
            text_list = self.win_ui.listWidget_2.selectedItems()
            text = [i.text() for i in list(text_list)]
            cpr_key = text
            self.win_ui.label_4.setText('对比依据:' + str(cpr_key))    
        else:
            pass
            
    def import_file(self):
        global path_data, path_target, path_cpr, path_cpr_new, sheet_data, sheet_target, columns_data,\
            sheet_cpr1, sheet_cpr2
            
        filepath, _ = QFileDialog.getOpenFileName(self.win, '选择文件', '.\\', '文件类型 (*.xlsx *.xls)')

        if self.sender().text() == '导入数据库文件':
            path_data = filepath
            self.win_ui.label_9.setText('文件地址:' + filepath)
            try:
                df1 = pd.read_excel(path_data, sheet_name=None, header=0)
                self.win_ui.comboBox.clear()
                self.win_ui.listWidget.clear()
                list_sheet1 = list(df1)
                self.win_ui.comboBox.addItems(list_sheet1)
                sheet_data = self.win_ui.comboBox.currentText()
                columns_data = df1[sheet_data].columns 
                self.win_ui.listWidget.addItems(columns_data)
            except FileNotFoundError:
                self.win_ui.comboBox.clear()
        elif self.sender().text() == '导入目标文件':
            path_target = filepath
            self.win_ui.label_10.setText('文件地址:' + filepath)
            try:
                df2 = pd.read_excel(path_target, sheet_name=None, header=0)
                self.win_ui.comboBox_2.clear()
                self.win_ui.listWidget.clear()
                list_sheet2 = list(df2)
                self.win_ui.comboBox_2.addItems(list_sheet2)
                sheet_target = self.win_ui.comboBox_2.currentText()
                columns_data = df2[sheet_target].columns 
                self.win_ui.listWidget.addItems(columns_data)
            except FileNotFoundError:
                self.win_ui.comboBox_2.clear()
        elif self.sender().text() == '导入旧清单文件':
            path_cpr = filepath
            self.win_ui.label_15.setText('文件地址:' + filepath)
            try:
                df3 = pd.read_excel(path_cpr, sheet_name=None, header=0)
                self.win_ui.comboBox_3.clear()
                self.win_ui.listWidget_2.clear()
                list_sheet3 = list(df3)
                self.win_ui.comboBox_3.addItems(list_sheet3)
                sheet_cpr1 = self.win_ui.comboBox_3.currentText()
                columns_data = df3[sheet_cpr1].columns
                self.win_ui.listWidget_2.addItems(columns_data) 
            except FileNotFoundError:
                self.win_ui.comboBox_3.clear()
        elif self.sender().text() == '导入新清单文件':
            path_cpr_new = filepath
            self.win_ui.label_18.setText('文件地址:' + filepath)
            try:
                df4 = pd.read_excel(path_cpr_new, sheet_name=None, header=0)
                self.win_ui.comboBox_4.clear()
                self.win_ui.listWidget_2.clear()
                list_sheet4 = list(df4)
                self.win_ui.comboBox_4.addItems(list_sheet4)
                sheet_cpr2 = self.win_ui.comboBox_4.currentText()
                columns_data = df4[sheet_cpr2].columns
                self.win_ui.listWidget_2.addItems(columns_data)  
            except FileNotFoundError:
                self.win_ui.comboBox_4.clear()
        else:
            pass

    def open_win(self, widget_o):
        widget_o.win.show()
        
    def repeat(self):
        global orwt
        
        if self.win_ui.label_9.text() != '文件地址:' and self.win_ui.label_10.text() != '文件地址:':
            pp = PandasPro()
            
            try:   
                # 通用功能
                # index_key = self.win_ui.listWidget.currentItem().text()
                orwt = self.win_ui.checkBox.isChecked()
                pp.process()
                QMessageBox.information(window_main, '提示', 
                                        '匹配数:' + str(n4) + '\n' + 
                                        '详见源目录:匹配结果.xlsx！')
            except:
                QMessageBox.information(window_main, '提示', 
                                        '请检查所选excel文件的:' + '\n' + 
                                        '1、请确认依据正确选择!')
        else:
            QMessageBox.information(window_main, '提示', 
                                        '请确认已选择excel文件')
            
    def expt(self):
        
        if self.win_ui.label_9.text() != '文件地址:':
            pp = PandasPro()
            
            try:
                pp.export()
                QMessageBox.information(window_main, '提示', '详见源目录:数据库.xlsx！')
            except:
                QMessageBox.information(window_main, '提示', 
                                        '请检查所选excel文件的:' + '\n' + 
                                        '1、请确认依据正确选择!')
        else:
            QMessageBox.information(window_main, '提示', 
                                        '请确认已选择excel文件')
            
    def compr(self):
        
        if self.win_ui.label_15.text() != '文件地址:' and self.win_ui.label_18.text() != '文件地址:': 
            pp = PandasPro()
            
            try:
                pp.cpr()
                self.win_ui.textBrowser.setPlainText(rpt)
                QMessageBox.information(window_main, '提示', cpr_info)
            except:
                QMessageBox.information(window_main, '提示', 
                                        '请检查所选excel文件的:' + '\n' + 
                                        '1、请确认依据正确选择!')
                raise
        else:
            QMessageBox.information(window_main, '提示', 
                                        '请确认已选择excel文件')
# 类-菜单窗口-关于
class CreatWinAbout(QWidget):
    
    def __init__(self, Ui_file):
        super().__init__()
        self.win = QWidget()
        self.win_ui = Ui_file.Ui_Form()
        self.win_ui.setupUi(self.win)
        self.win_ui.commandLinkButton.clicked.connect(self.open_git)
    
    def open_git(self):
        QDesktopServices.openUrl(QUrl("https://github.com/qhzgit734?tab=repositories"))
# 类-主程序 
if __name__ == "__main__":
    # 类实例
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))

    window_main = CreatRoot(win_main_uic)
    window_help = CreatWinAbout(win_h_uic)
    # 窗口显示
    window_main.win.show()
    app.setWindowIcon(QIcon('logo.ico'))
    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())

# pyinstaller -F CostByTable_V0.0.py -i 'logo.ico'
# pyinstaller -F -w CostByTable_V0.0.py -i 'logo.ico'
'''
pyinstaller打包datacompy运行错误，在pyinstaller\\hooks文件夹中新建hook-datacompy.py文件，文件内容如下：
from PyInstaller.utils.hooks import collect_data_files
datas = collect_data_files("datacompy")
'''