#!/usr/bin/python
#
# $Id: reader_hicom300.py,v 1.6 2012-02-24 20:53:25 sshevtsov Exp $
#
#  Este script es utilizado para levantar los datos del puerto serie
#  al cual esta conectada la central hicom300.
# 
#  La configuracion del pueto esta definida en y explicada en el archivo
#  serial_conf.py
#
#  Las demas configuraciones estan en el archivo reader_hicom300_conf.py
#
from buffer_thread_safety import bufferTS
import logging
from logging.handlers import TimedRotatingFileHandler
from logging import FileHandler
import os
import re
import reader_hicom300_conf
import serial
import serial_conf
import sys
import threading

class serialPort:
  def __init__(self):
    try:
      self.port = serial.Serial(serial_conf.port,
                                serial_conf.baudrate,
                                serial_conf.bytesize,
                                serial_conf.parity,
                                serial_conf.stopbits,
                                serial_conf.timeout)
    except serial.SerialException, e:
      raise Exception, "Error seting up serial port: %s" % e
      sys.exit(1)

    self.port.open()
    self.port.flushInput()
    self.port.flushOutput()

  def __del__(self):
    try:
      self.port.close()
    except AttributeError, e:
      return

  def write(self,data):
    try:
      self.port.write(data)
    except serial.SerialTimeoutException, e:
      raise Exception, "Error writing data to serial port: %s" % e
    
  def read(self):
    try:
      data = self.port.readline()
    except ValueError, e:
      raise Exception, "Error reading data from serial port: %s" % e
      return False
    return data


class serialReader(threading.Thread):
  def __init__(self, sp, buf):
    threading.Thread.__init__(self)
    self.serialPort = sp
    self.bufferTS = buf

  def run(self):
    while True:
      data = self.serialPort.read()
      if data:
        self.bufferTS.put(data)
    
      
class serialLogger(threading.Thread):
  def __init__(self,fileName, buf):
    threading.Thread.__init__(self)
    self.bufferTS = buf
    self.fileName = fileName
    # configuracion del logger.
    # rotacion medida en dias 'D' cuantos? 1, backup = 200 dias.
    # se comenta la rotacion por codigo porque es manejada por el parser
    #logHandler = TimedRotatingFileHandler(self.fileName,'D',1,200)
    logHandler = FileHandler(self.fileName)
    logFormatter =  logging.Formatter("%(levelname)s %(asctime)s|%(message)s","")
    logHandler.setFormatter(logFormatter)
    self.logger = logging.getLogger('LlamadasTelefonicas')
    self.logger.addHandler(logHandler)
    self.logger.setLevel(logging.INFO)

  def isValidLogLine(self,line):
    expr = re.compile("\d{2}/\d{2}/\d{2}\d{2}:\d{2}:\d{2}\d{2}:\d{2}:\d{2}\s+\d{3}\s+\d+\s+0{5}")
    searchRes = expr.search(line)
    if searchRes == None:
      return False
    if len(searchRes.group(0)) <= 0:
      return False
    return True
    

  def run(self):
     while True:
       data = self.bufferTS.get()
       if not self.isValidLogLine(data):
         continue
       callDate = data[0:8]
       callTime = data[8:16]
       callDuration = data[16:24]
       callInternal = data[25:28]
       callOutLine = data[30:32]
       callNumber = data[32:60].strip()
       logLine = ("%s\t%s\t%s\t%s\t%s\t%s" % 
         (callDate, callTime, callDuration, 
          callInternal, callOutLine, callNumber))
       self.logger.info(logLine)

"""
convertiendo a servicio.
hago el fork si soy padre salgo
me adopta el proceso de init
"""
print "Forking."
if os.fork() > 0:
  os._exit(0)

# me hago lider de la sesion
os.setsid()

os.chdir(reader_hicom300_conf.workDir)
# grabo mi pid en el pidfile
pidFile = open(reader_hicom300_conf.pidFileName, 'w')
pidFile.write("%d\n" % os.getpid())
pidFile.close()

s = serialPort()
commonBuffer = bufferTS()
hicom300Reader = serialReader(s,commonBuffer)
hicom300Logger = serialLogger(reader_hicom300_conf.logFileName,commonBuffer)

# a trabajar
hicom300Reader.start()
hicom300Logger.start()
