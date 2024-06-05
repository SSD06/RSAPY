# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *
from PySide2.QtGui import *
from PySide2.QtNetwork import *
from PySide2.QtCore import *
from Crypto import Random  # 导入随机模块
from Crypto.Hash import SHA  # 导入sha加密
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5  # 加密数据和解密数据
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5  # 签名和解签
from Crypto.PublicKey import RSA  # 实现rsa加密
from Crypto.Util.number import long_to_bytes,bytes_to_long
import base64


class Widget:
    def __init__(self):
        self.ui = QUiLoader().load('WidgetForm.ui')
        #self.ui.pushButton.clicked.connect(self.Generatekey)
        self.ui.pushButton.clicked.connect(self.Thrstart)
        self.ui.pushButton_2.clicked.connect(self.SavePrivate_key)
        self.ui.pushButton_3.clicked.connect(self.SavePublic_key)
        self.ui.pushButton_4.clicked.connect(self.LoadPrivate_key)
        self.ui.pushButton_5.clicked.connect(self.LoadPublic_key)
        self.ui.pushButton_6.clicked.connect(self.Public_Encrypt)
        self.ui.pushButton_7.clicked.connect(self.Private_Decrypt)
        self.ui.pushButton_8.clicked.connect(self.GeneratekeyPUB)
        # self.ui.pushButton_8.clicked.connect(self.Private_Encrypt)
        # self.ui.pushButton_9.clicked.connect(self.Public_Decrypt)
        
        self.keyt=KeyThread()
        #self.keyt.num=1024
        self.keyt.key.connect(self.GenKey)
        #self.keyt.start()
        
    def Thrstart(self):
        self.keyt.num=int(self.ui.comboBox.currentText())
        self.keyt.start()
    
    def GenKey(self,key:list):
        
        self.ui.plainTextEdit.setPlainText(key[0].decode())
        self.ui.plainTextEdit_2.setPlainText(key[1].decode())   
        
    def Generatekey(self):
        random_generator = Random.new().read  # 生成随机偏移量
        #print(self.ui.comboBox.currentText())
        if self.ui.comboBox.currentText()=='1024':
            rsa = RSA.generate(1024, random_generator)  # 生成一个私钥
        elif self.ui.comboBox.currentText()=='2048':
            rsa = RSA.generate(2048, random_generator)  # 生成一个私钥
        elif self.ui.comboBox.currentText()=='4096':
            rsa = RSA.generate(4096, random_generator)  # 生成一个私钥
        else :
            rsa = RSA.generate(1024, random_generator)  # 生成一个私钥
        # print(random_generator)
        
        # print(rsa)
        # 生成私钥
        private_key = rsa.exportKey()  # 导出私钥
        # print(private_key.decode())  
        # 生成公钥
        public_key = rsa.publickey().exportKey()  # 生成私钥所对应的公钥
        # print(public_key.decode())
        self.ui.plainTextEdit.setPlainText(private_key.decode())
        self.ui.plainTextEdit_2.setPlainText(public_key.decode())
        
    def GeneratekeyPUB(self):
        if self.ui.plainTextEdit.toPlainText()=='':
            return
        key = RSA.importKey(self.ui.plainTextEdit.toPlainText())
        self.ui.plainTextEdit_2.setPlainText(key.publickey().exportKey().decode())
        
    def SavePrivate_key(self):
        if self.ui.plainTextEdit.toPlainText()=='':
            return
        wind = QMainWindow()
        filename,_= QFileDialog.getSaveFileName(wind, "保存私钥文件","./私钥.pem","*.pem")
        if filename=='':
            return
        with open(filename, 'w')as f:
            f.write(self.ui.plainTextEdit.toPlainText())  # 将私钥内容写入文件中
            
    def SavePublic_key(self):
        if self.ui.plainTextEdit_2.toPlainText()=='':
            return
        wind = QMainWindow()
        filename,_= QFileDialog.getSaveFileName(wind, "保存公钥文件","./公钥.pem","*.pem")
        if filename=='':
            return
        with open(filename, 'w')as f:
            f.write(self.ui.plainTextEdit_2.toPlainText())  # 将公钥内容写入文件中
            
    def LoadPrivate_key(self):
        wind = QMainWindow()
        filename,_= QFileDialog.getOpenFileName(wind, "打开私钥文件","./","*.pem")
        if filename=='':
            return
        with open(filename, 'r')as f:
            self.ui.plainTextEdit.setPlainText(f.read())
            
    def LoadPublic_key(self):
        wind = QMainWindow()
        filename,_= QFileDialog.getOpenFileName(wind, "打开公钥文件","./","*.pem")
        if filename=='':
            return
        with open(filename, 'r')as f:
            self.ui.plainTextEdit_2.setPlainText(f.read())
            
    def Public_Encrypt(self):
        if self.ui.plainTextEdit_2.toPlainText()=='' or self.ui.plainTextEdit_3.toPlainText()=='':
            return
        msg:str = self.ui.plainTextEdit_3.toPlainText()
        try:
            key = RSA.importKey(self.ui.plainTextEdit_2.toPlainText())
        except:
            return
        public_key = key # 读取公钥信息
        cipher = Cipher_pkcs1_v1_5.new(public_key)  # 生成一个加密的类
        msg=msg.encode()
        length = len(msg)
        default_length = public_key.size_in_bytes()-11
        res = []
        for i in range(0, length, default_length):
            res.append(cipher.encrypt(msg[i:i + default_length]))
        encrypt_text = base64.b64encode(b''.join(res))
        #encrypt_text = base64.b64encode(cipher.encrypt(msg.encode()))  # 对数据进行加密
        #encrypt_text = cipher.encrypt(msg.encode()) # 对数据进行加密
        self.ui.plainTextEdit_4.setPlainText(encrypt_text.decode())
    
    
    
    
    def Private_Decrypt(self):
        if self.ui.plainTextEdit.toPlainText()=='' or self.ui.plainTextEdit_4.toPlainText()=='':
            return
        encrypt_msg:str = self.ui.plainTextEdit_4.toPlainText()
        try:
            private_key = RSA.importKey(self.ui.plainTextEdit.toPlainText())
            
        except:
            return
        cipher = Cipher_pkcs1_v1_5.new(private_key)  # 生成一个解密的类
        #print(private_key.size_in_bytes())
        data = base64.b64decode(encrypt_msg)
        length = len(data)
        default_length = private_key.size_in_bytes()
        res = []
        for i in range(0, length, default_length):
            res.append(cipher.decrypt(data[i:i + default_length], 0))
        back_text=b''.join(res)
        #back_text = cipher.decrypt(base64.b64decode(encrypt_msg), 0)  # 进行解密
        self.ui.plainTextEdit_3.setPlainText(back_text.decode())  # 对文本内容进行解码
        
        
    # def Private_Encrypt(self):
    #     if self.ui.plainTextEdit.toPlainText()=='' or self.ui.plainTextEdit_3.toPlainText()=='':
    #         return
    #     msg:str = self.ui.plainTextEdit_3.toPlainText()
    #     try:
    #         key = RSA.importKey(self.ui.plainTextEdit.toPlainText())
    #     except:
    #         return
    #     cipher = Cipher_pkcs1_v1_5.new(key)  # 生成一个加密的类
    #     encrypt_text = base64.b64encode(cipher.encrypt(msg.encode()))  # 对数据进行加密
    #     #encrypt_text = cipher.encrypt(msg.encode()) # 对数据进行加密
    #     self.ui.plainTextEdit_4.setPlainText(encrypt_text.decode())

    
    # def Public_Decrypt(self):
    #     if self.ui.plainTextEdit_2.toPlainText()=='' or self.ui.plainTextEdit_4.toPlainText()=='':
    #         return
    #     encrypt_msg:str = self.ui.plainTextEdit_4.toPlainText()
    #     try:
    #         Public_key = RSA.importKey(self.ui.plainTextEdit_2.toPlainText())
    #     except:
    #         return
    #     cipher = Cipher_pkcs1_v1_5.new(Public_key)  # 生成一个解密的类
    #     back_text = cipher.decrypt(base64.b64decode(encrypt_msg), 0)  # 进行解密
    #     self.ui.plainTextEdit_3.setPlainText(back_text.decode())  # 对文本内容进行解码
        


class KeyThread(QThread):
    key=Signal(list)
    num=int
    
    def __init__(self):
        super().__init__()
    def run(self):
        random_generator = Random.new().read  # 生成随机偏移量
        rsa = RSA.generate(self.num, random_generator)  # 生成一个私钥
        # print(random_generator)
        
        # print(rsa)
        # 生成私钥
        private_key = rsa.exportKey()  # 导出私钥
        # print(private_key.decode())  
        # 生成公钥
        public_key = rsa.publickey().exportKey()  # 生成私钥所对应的公钥
        # print(public_key.decode())
        keys=[private_key,public_key]
        self.key.emit(keys)