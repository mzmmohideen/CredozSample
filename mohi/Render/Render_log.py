import sys
import os, collections
from PySide import *
from Render import *
import datetime
import qdarkstyle
from peewee import *
from peewee import *
import sys
from PySide import QtGui
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import numpy as NP
from matplotlib import pyplot as PLT
from matplotlib.figure import Figure
from datetime import date, timedelta
import random
import math
import FileDialog

class Form(QtGui.QWidget,Ui_Form):
    def __init__(self): 
        super(Form,self).__init__()
        self.setupUi(self)
        self.show()
        self.home()
    def home(self):
        self.mode="global"
        
        
        self.treeWidget_2.hideColumn(0)
        self.global_rb.clicked.connect(self.status)
        self.show_rb.clicked.connect(self.status)
        self.start_date_lineEdit.setText(datetime.datetime.today().date().strftime("%d-%m-%Y").__str__())
        self.end_datelineEdit.setText(datetime.datetime.today().date().strftime("%d-%m-%Y").__str__())
        self.start_date_toolButton.clicked.connect(self.showCalWid)
        self.end_date_toolButton.clicked.connect(self.showCalWid2)
        self.render_comboBox.currentIndexChanged.connect(self.task_filter)
        self.node_comboBox.currentIndexChanged.connect(self.task_filter)
        self.assert_comboBox.currentIndexChanged.connect(self.task_filter)
        self.refresh_Button.clicked.connect(self.getting_date)
        self.treeWidget_1.itemSelectionChanged.connect(self.display_treewidget_2)
        self.treeWidget_2.itemSelectionChanged.connect(self.show_detials)
        # self.task_combobox.currentIndexChanged.connect(self.task_filter)
        self.hide_checkbox.stateChanged.connect(self.hide_details)
        self.hide_checkbox.setChecked(QtCore.Qt.Checked)
        self.hide_checkbox.setEnabled (False)
        self.resolution_comboBox.currentIndexChanged.connect(self.task_filter)
        self.all_rb.clicked.connect(self.task_filter)
        self.comp_rb.clicked.connect(self.task_filter)
        self.mm_rb.clicked.connect(self.task_filter)
        self.paint_rb.clicked.connect(self.task_filter)
        self.roto_rb.clicked.connect(self.task_filter)
        self.others_rb.clicked.connect(self.task_filter)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout = QtGui.QVBoxLayout()
        self.ax = self.figure.add_subplot(111)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout.addWidget(self.toolbar)

    def getting_date(self):
        self._t = {}
        self.output = []
        self.db = SqliteDatabase(r"C:\Users\botvfx\Desktop\ramkumar\Render\render_submission_log.db")
        self.db.connect()
        self.a='SELECT * FROM smedgesubmissiondatamodel where date between "%s" and "%s"'%(self.start_date_lineEdit.text(),self.end_datelineEdit.text())
        self.d = self.db.execute_sql(self.a)
        self._keys = ["id", "date", "time", "show_name", "shot_name", "task_name", "render_type", "node_type", "priority", "resolution", "first_frame", "last_frame", "frame_count", "artist_name", "script_path", "script_size", "output_path", "asset_class"]
        
        for i in self.d.fetchall():
            self._t = {}
            for j in range(len(i)):
                self._t.update({self._keys[j]:i[j]})
            self.output.append(self._t)
        self.task_filter()
        
    def task_filter(self):

        if self.comp_rb.isChecked():
            self.task_result=filter(lambda x :x["task_name"].lower()=="comp",self.output)
        elif self.mm_rb.isChecked():
            self.task_result=filter(lambda x :x["task_name"].lower()=="mm",self.output)
        elif self.paint_rb.isChecked():
            self.task_result=filter(lambda x :x["task_name"].lower()=="paint",self.output)
        elif self.roto_rb.isChecked():
            self.task_result=filter(lambda x :x["task_name"].lower()=="roto",self.output)
        elif self.others_rb.isChecked():
            self.task_result=filter(lambda x :x["task_name"].lower()=="",self.output)
        else:
            self.task_result=self.output
        self.render_filter(self.sender())

    def render_filter(self, sender=""):
        if self.render_comboBox.currentText()!="Select Render Type":
            self.render_result=filter(lambda x :x["render_type"].lower()==self.render_comboBox.currentText().lower(),self.task_result)

        else:
            self.render_result=self.task_result
        
        self.node_filter(sender)

    
    def node_filter(self, sender=""):
        if self.node_comboBox.currentText()!="Select Node Type":
            self.node_result=filter(lambda x :x["node_type"].lower()==self.node_comboBox.currentText().lower(),self.render_result)
        else:
            self.node_result=self.render_result
        self.resolution(sender)

    def resolution(self, sender):
        self.resolution_result=self.node_result
        if sender.objectName()=="resolution_comboBox":
            
            if sender.currentText()!="Select Resolution":
                count = int((float(sender.currentText().lower().replace("k", ""))+0.5)*1000)
                self.resolution_result = filter(lambda y: y['resolution'] and (count-1000+1<int(y["resolution"].split("x")[0])<=count), self.node_result)
        self.asset_filter()

    def asset_filter(self):

        if self.assert_comboBox.currentText()!="Select Asset Class":
            self.asset_result=filter(lambda x :x["asset_class"].lower()==self.assert_comboBox.currentText().lower(),self.resolution_result)
        else:
            self.asset_result=self.resolution_result
        self.display_treewidget()

    def display_treewidget(self):
        self.treeWidget_1.clear()
        self.total_file_count=str(len(self.asset_result))
        self._graph_data = self.asset_result
        if self.mode=="global":
            self.artist_name=[x["artist_name"] for x in self.asset_result]
            self.artist_name=set(self.artist_name)
        
        elif self.mode=="show":
            self.show_name=[x["show_name"] for x in self.asset_result]
            self.show_name=set(self.show_name)
        self.total_frame_count=0 
        self.text=""
        self.task_name=list(set([k["task_name"] for k in self.asset_result]))
        if self.mode=="global":
            for y in self.artist_name:
                self.count=str(sum([i["frame_count"] for i in self.asset_result if i["artist_name"].lower()==y.lower()]))  
                self.file_count=str(len([x for x in self.asset_result if x["artist_name"].lower()==y.lower()]))
                QtGui.QTreeWidgetItem(self.treeWidget_1,[y,self.file_count,self.count])
                self.total_frame_count+=int(self.count)
        

        elif self.mode=="show":
            for y in self.show_name:
                self.count=str(sum([i["frame_count"] for i in self.asset_result if i["show_name"].lower()==y.lower()]))  
                self.file_count=str(len([x for x in self.asset_result if x["show_name"].lower()==y.lower()]))
                QtGui.QTreeWidgetItem(self.treeWidget_1,[y,self.file_count,self.count])
                self.total_frame_count+=int(self.count)

        self.text="Total Frame Count : %s \n"%str(self.total_frame_count)
        self.text+="Total file count : %s \n"%str(self.total_file_count)

        for k in reversed(self.task_name):
            if k=="":
                self.count=sum([i["frame_count"] for i in self.asset_result if i["task_name"].lower()==k.lower()])
                self.text+="%s : %s \n"%("OTHERS",str(self.count))
            else:
                self.count=sum([i["frame_count"] for i in self.asset_result if i["task_name"].lower()==k.lower()])
                self.text+="%s : %s \n"%(k.upper(),str(self.count))

        cmd = {}
        for i in range(1, 9):
            count = int((float(i)+0.5)*1000)
            if "%dK"%i not in cmd.keys():
                cmd["%dK"%i] = 0
            cmd["%dK"%i] = sum([x['frame_count'] for x in filter(lambda y: y['resolution'] and (count-1000+1<int(y["resolution"].split("x")[0])<=count), self.asset_result)])
        self.t = ""
        cmd = collections.OrderedDict(sorted(cmd.items()))
        for k, v in cmd.iteritems():
            if v:
                self.t += "%s: %d   |  "%(k, v) 
        self.t = self.t[:-4]
        self.label.setText(self.text+"\n"+"Total Resolution Frame Count: \n"+self.t+"\n")
        self.plot_graph()

    def autolabel(self,rects):
        self.count=0
        for x in rects:
            if rects==self.bar0:
                self.bar0_height.append(x.get_height())
            elif rects==self.bar1:
                self.bar1_height.append(x.get_height()+self.bar0_height[self.count])
                self.count+=1
            elif rects==self.bar2:
                self.bar2_height.append(x.get_height()+self.bar1_height[self.count])
                self.count+=1
            elif rects==self.bar3:
                self.bar3_height.append(x.get_height()+self.bar2_height[self.count])
                self.count+=1
            elif rects==self.bar4:
                self.bar4_height.append(x.get_height()+self.bar3_height[self.count])
                self.count+=1
        self.count_h=0

        for rect in rects:
            if rects==self.bar0:
                height = rect.get_height()
                if int(height)!=0:
                    self.ax.text(rect.get_x() + rect.get_width()/2.,((rect.get_height()/2)),
                            '%d' % int(rect.get_height()),
                            ha='center', va='center',color='white',size=6)
                    self.count_h+=1
            elif rects==self.bar1:
                height=self.bar1_height[self.count_h]
                if int(x.get_height())!=0:
                    self.ax.text(rect.get_x()+rect.get_width()/2.,(self.bar0_height[self.count_h]+(rect.get_height()/2)),
                            '%d'%int(rect.get_height()),
                            ha='center',va='center',color='white',size=6)
                    self.count_h+=1
            elif rects==self.bar2:
                height=self.bar2_height[self.count_h]
                if int(x.get_height())!=0:
                    self.ax.text(rect.get_x()+rect.get_width()/2.,(self.bar1_height[self.count_h]+(rect.get_height()/2)),
                            '%d'%int(rect.get_height()),
                            ha='center',va='center',color='white',size=6)
                    self.count_h+=1
            elif rects==self.bar3:
                height=self.bar3_height[self.count_h]
                if int(x.get_height())!=0:
                    self.ax.text(rect.get_x()+rect.get_width()/2.,(self.bar2_height[self.count_h]+(rect.get_height()/2)),
                            '%d'%int(rect.get_height()),
                            ha='center',va='center',color='white',size=6)
                    self.count_h+=1
            elif rects==self.bar4:
                height=self.bar4_height[self.count_h]
                if int(x.get_height())!=0:
                    self.ax.text(rect.get_x()+rect.get_width()/2.,(self.bar3_height[self.count_h]+(rect.get_height()/2)),
                            '%d'%int(rect.get_height()),
                            ha='center',va='center',color='white',size=6)

                self.ax.text(rect.get_x()+rect.get_width()/2.,(self.bar4_height[self.count_h]+5),
                            '%d'%int(self.bar4_height[self.count_h]),
                            ha='center',va='center',color='black')
                self.count_h+=1

    def onpick(self,event):

        self.selected_date=self.ax.get_xticklabels()[(int(round(event.mouseevent.xdata)))].get_text()
        if len(self.selected_date)==10:
            self.data_g=[x for x in self.asset_result if x["date"]==self.selected_date]
            self.graph_data(self.data_g)
        legline = event.artist
        self.canvas.draw()
     
        

    def graph_data(self,data):
        self._graph_data = data
        self.treeWidget_1.clear()
        self.total_file_count=str(len(data))
        
        if self.mode=="global":
            self.artist_name=[x["artist_name"] for x in data]
            self.artist_name=set(self.artist_name)
        
        elif self.mode=="show":
            self.show_name=[x["show_name"] for x in data]
            self.show_name=set(self.show_name)
        self.total_frame_count=0 
        self.text=""
        self.task_name=list(set([k["task_name"] for k in data]))
        if self.mode=="global":
            for y in self.artist_name:
                self.count=str(sum([i["frame_count"] for i in data if i["artist_name"].lower()==y.lower()]))  
                self.file_count=str(len([x for x in data if x["artist_name"].lower()==y.lower()]))
                QtGui.QTreeWidgetItem(self.treeWidget_1,[y,self.file_count,self.count])
                self.total_frame_count+=int(self.count)
        

        elif self.mode=="show":
            for y in self.show_name:
                self.count=str(sum([i["frame_count"] for i in data if i["show_name"].lower()==y.lower()]))  
                self.file_count=str(len([x for x in data if x["show_name"].lower()==y.lower()]))
                QtGui.QTreeWidgetItem(self.treeWidget_1,[y,self.file_count,self.count])
                self.total_frame_count+=int(self.count)

        self.text="Total Frame Count : %s \n"%str(self.total_frame_count)
        self.text+="Total File Count : %s \n"%str(self.total_file_count)

        for k in reversed(self.task_name):
            if k=="":
                self.count=sum([i["frame_count"] for i in data if i["task_name"].lower()==k.lower()])
                self.text+="%s : %s \n"%("OTHERS",str(self.count))
            else:
                self.count=sum([i["frame_count"] for i in data if i["task_name"].lower()==k.lower()])
                self.text+="%s : %s \n"%(k.upper(),str(self.count))

        cmd = {}
        for i in range(1, 9):
            count = int((float(i)+0.5)*1000)
            if "%dK"%i not in cmd.keys():
                cmd["%dK"%i] = 0
            cmd["%dK"%i] = sum([x['frame_count'] for x in filter(lambda y: y['resolution'] and (count-1000+1<int(y["resolution"].split("x")[0])<=count), data)])
        self.t = ""
        cmd = collections.OrderedDict(sorted(cmd.items()))
        for k, v in cmd.iteritems():
            if v:
                self.t += "%s: %d   |  "%(k, v) 
        self.t = self.t[:-4]
        self.label.setText(self.text+"\n"+"Total Resolution Frame Count: \n"+self.t+"\n")
    def plot_graph(self):  
        self.bar0_height=[]
        self.bar1_height=[]
        self.bar2_height=[]
        self.bar3_height=[]
        self.bar4_height=[]
        self.layout.addWidget(self.canvas)
        self.graph_frame.setLayout(self.layout)
        self.paint_sum=0
        self.comp_sum=0
        self.mm_sum=0
        self.roto_sum=0
        self.other_sum=0
        self.start_date.split("-")
        self.d1 = date(int(self.start_date.split("-")[0]),int(self.start_date.split("-")[1]),int(self.start_date.split("-")[2]))
        self.d2 = date(int(self.end_date.split("-")[0]),int(self.end_date.split("-")[1]),int(self.end_date.split("-")[2]))
        self.delta=self.d2-self.d1
        self.date_list=[]
        
        for y in range(self.delta.days + 1):
            self.date_list.append(str(self.d1 + timedelta(y)))
        self.paint_data=[]
        self.comp_data=[]
        self.mm_data=[]
        self.roto_data=[]
        self.other_data=[]
        
        for k in self.date_list:
            self.paint_sum=0
            self.comp_sum=0
            self.mm_sum=0
            self.roto_sum=0
            self.other_sum=0

            for x in self.asset_result:
                if x["task_name"]=="paint" and x["date"]==str(k):
                    self.paint_sum+=1
                elif x["task_name"]=="mm" and x["date"]==str(k):
                    self.mm_sum+=1
                elif x["task_name"]=="roto" and x["date"]==str(k):
                    self.roto_sum+=1
                elif x["task_name"]=="comp" and x["date"]==str(k):
                    self.comp_sum+=1
                elif x["task_name"]=="" and x["date"]==str(k):
                    self.other_sum+=1
            self.paint_data.append(self.paint_sum)
            self.comp_data.append(self.comp_sum)
            self.mm_data.append(self.mm_sum)
            self.roto_data.append(self.roto_sum)
            self.other_data.append(self.other_sum)

        ind = self.date_list
        width = 0.5     
        self.ax.clear()
        cat=["Paint","Comp","MM","Roto","Others"]
        self.bar0=""
        self.bar1=""
        self.bar2=""
        self.bar3=""
        self.bar4=""
        self.bar0=self.ax.bar(ind, self.paint_data, width,color="#ffaa88",picker=5,label="paint",edgecolor="white")
        self.autolabel(self.bar0)
        self.bar1=self.ax.bar(ind, self.comp_data,width,bottom=self.paint_data,color="#3498db",picker=5,label="comp",edgecolor="white")
        self.autolabel(self.bar1)
        self.bar2=self.ax.bar(ind,self.mm_data,width,bottom=[x+y for x,y in zip(self.paint_data,self.comp_data)],color="#00cc99",picker=5,label="MM",edgecolor="white")
        self.autolabel(self.bar2)
        self.bar3=self.ax.bar(ind,self.roto_data,width,bottom=[x+y+z for x,y,z in zip(self.paint_data,self.comp_data,self.mm_data)],color="#8888ff",picker=5,label="Roto",edgecolor="white")
        self.autolabel(self.bar3)
        self.bar4=self.ax.bar(ind,self.other_data,width,bottom=[x+y+z+j for x,y,z,j in zip(self.paint_data,self.comp_data,self.mm_data,self.roto_data)],color="grey",picker=5,label="Others",edgecolor="white")
        self.autolabel(self.bar4)
        self.leg=self.ax.legend(loc='upper right')
        self.leg.get_frame().set_alpha(0.4)
        if self.comp_rb.isChecked():
            self.autolabel(self.bar1)
        elif self.mm_rb.isChecked():
            self.autolabel(self.bar2)
        elif self.roto_rb.isChecked():
            self.autolabel(self.bar3)
        elif self.others_rb.isChecked():
            self.autolabel(self.bar4)
        self.ax.set_xticks("2", self.ax)
        self.ax.xaxis.set_tick_params(labelsize=6)
        for x in self.ax.get_xticklabels():
            x.set_rotation(45)
        self.lines = [self.bar0,self.bar1,self.bar2,self.bar3,self.bar4]
        self.lined = dict()
        for legline, origline in zip(self.leg.get_lines(), self.lines):
            legline.set_picker(5)  # 5 pts tolerance
            self.lined[legline] = origline
        self.ax.set_xlabel("Date")
        self.ax.set_ylabel("number of renders")
        self.canvas.mpl_connect('pick_event', self.onpick)
        self.canvas.draw()
            
    def display_treewidget_2(self):
        self.treeWidget_2.clear()
        if self.mode=="global":
            if self.treeWidget_1.selectedItems():
                self.treeWidget_2.setCurrentItem(self.treeWidget_2.topLevelItem(0))
                self.artist=self.treeWidget_1.selectedItems()[0].text(0).lower()
                self.work_details=[x for x in self._graph_data if x["artist_name"].lower()==self.artist]
                for y in self.work_details:
                    QtGui.QTreeWidgetItem(self.treeWidget_2,[str(y["id"]),str(y["frame_count"]),y["show_name"],y["shot_name"],y["date"],y["time"]])
        
        elif self.mode=="show":
            if self.treeWidget_1.selectedItems():
                self.treeWidget_2.setCurrentItem(self.treeWidget_2.topLevelItem(0))
                self.show=self.treeWidget_1.selectedItems()[0].text(0).lower()
                self.work_details=[x for x in self._graph_data if x["show_name"].lower()==self.show]
                for y in self.work_details:
                    QtGui.QTreeWidgetItem(self.treeWidget_2,[str(y["id"]),str(y["frame_count"]),y["artist_name"],y["shot_name"],y["date"],y["time"]])



    def hide_details(self):
        if self.hide_checkbox.isChecked():
            self.frame_details.hide()
        else:
            self.frame_details.show()

    def show_detials(self):
        self.hide_checkbox.setEnabled (True)
        self.hide_checkbox.setChecked(QtCore.Qt.Unchecked)
        if self.treeWidget_2.selectedItems():
            self.details=[x for x in self.asset_result if str(x["id"])==str(self.treeWidget_2.selectedItems()[0].text(0))]
            if self.details:
                self.showname_label.setText(self.details[0]["show_name"])
                self.shotnameandtaskname_label.setText(self.details[0]["shot_name"]+"_"+self.details[0]["task_name"])
                self.frame_label.setText(str(self.details[0]["first_frame"])+"-"+str(self.details[0]["last_frame"])+"_"+str(self.details[0]["frame_count"]))
                self.resolution_label.setText(self.details[0]["resolution"])
                self.priority_label.setText(str(self.details[0]["priority"]))
                self.task_name_label.setText(self.details[0]["task_name"])
                self.script_size_label.setText(str(self.details[0]["script_size"]))
                self.asset_class_label.setText(self.details[0]["asset_class"])
                self.outputpath_textbox.setText("OUTPUT PATH: "+self.details[0]["output_path"])
                self.scriptpath_textbox.setText("SCRIPT PATH: "+self.details[0]["script_path"])

    def status(self):
        if self.show_rb.isChecked():
            self.treeWidget_1.setHeaderLabels(["Show Name","File Count","Frame Count"])
            self.mode="show"

        elif self.global_rb.isChecked():
            self.treeWidget_1.setHeaderLabels(["Artist","File Count","Frame Count"])
            self.mode="global"
        
        self.getting_date()

    def showCalWid(self):
        self.calendar = QtGui.QCalendarWidget()
        self.calendar.setMinimumDate(QtCore.QDate(1900, 1, 1))
        self.calendar.setMaximumDate(QtCore.QDate(3000, 1, 1))
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.updateDate)
        self.calendar.setWindowFlags(QtCore.Qt.FramelessWindowHint)     
        self.calendar.setGridVisible(True)
        pos = QtGui.QCursor.pos()
        self.x=pos.x()
        self.y=pos.y()
        self.calendar.setGeometry(pos.x(), pos.y(),300, 200)
        self.calendar.show()

    def showCalWid2(self):

        self.date=self.start_date_lineEdit.text().split("-")
        self.calendar = QtGui.QCalendarWidget()
        self.calendar.setMinimumDate(QtCore.QDate(int(self.date[0]),int(self.date[1]),int(self.date[2])))
        self.calendar.setMaximumDate(QtCore.QDate(3000, 1, 1))
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.updateDate2)
        self.calendar.setWindowFlags(QtCore.Qt.FramelessWindowHint)     
        self.calendar.setGridVisible(True)
        pos = QtGui.QCursor.pos()
        self.calendar.setGeometry(int(self.x),int(self.y),300, 200)
        self.calendar.show()

    def updateDate2(self):
        get_Date = self.calendar.selectedDate().toString()
        getDate=datetime.datetime.strptime(get_Date,"%a %b %d %Y").strftime("%Y-%m-%d")
        self.end_date=str(getDate)
        self.end_datelineEdit.setText(getDate)
        self.calendar.deleteLater()
        self.getting_date()
        

    def updateDate(self):
        get_Date = self.calendar.selectedDate().toString()
        getDate=datetime.datetime.strptime(get_Date,"%a %b %d %Y").strftime("%Y-%m-%d")
        self.start_date=str(getDate)
        self.start_date_lineEdit.setText(getDate)
        self.calendar.deleteLater()
        self.showCalWid2()



app=QtGui.QApplication([])
app.setStyleSheet(qdarkstyle.load_stylesheet())
window=Form()
sys.exit(app.exec_())
