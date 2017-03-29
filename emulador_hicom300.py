#!/usr/bin/python
#
#
# Este script emula las escrituras de la central telefonica hicom300 sobre
# el pueto serie.
#
# las configuraciones del puerto se leen desde serial_conf

import serial_conf
import serial
import random
import math
import sys
import time

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
    
  #def read(self):


# clase para generar una fecha aleatoria
class randomDate:
  def __repr__(self):
    return "%02d/%02d/%d" % (random.randrange(1,31),
                             random.randrange(1,13),
                             random.randrange(12,14))

class randomTime:
  def __repr__(self):
    return "%02d:%02d:%02d" % (random.randrange(0,24),
                               random.randrange(0,60),
                               random.randrange(0,60))


class randomDuration(randomTime):
  def __repr__(self):
    return "%02d:%02d:%02d" % (random.randrange(0,2),
                               random.randrange(0,60),
                               random.randrange(0,60))

class randomTelephoneNumber(randomTime):
  def __repr__(self):
    return "%-30.30s" % (random.randrange(1000,int(math.exp(40))))


class central:
  #rd = fecha al azar
  #rt = hora de la llamada al azar
  #rdur = duracion de la llamada al azar
  #internal = interno al azar
  #rn = numero telefonico al azar 
  def __init__(self,sp):
    self.rd = None
    self.rt = None
    self.rdur = None
    self.internal = None
    self.rn = None
    self.serialPort = sp

  def pickupLine(self):
    self.rd = randomDate()
    self.rt = randomTime()
    self.internal = random.randrange(100,160)

  def dialUp(self):
    self.rn = randomTelephoneNumber()

  def talk(self):
    self.rdur = randomDuration()

  def hangLine(self):
    data = str(self.rd)+str(self.rt)+str(self.rdur)+" "+\
           str(self.internal)+"  "+str(self.rn)+"00000"
    print "Enviando[%s]" % data
    self.serialPort.write(data+"\n")

  def makeCall(self):
    self.pickupLine()
    self.dialUp()
    self.talk()
    self.hangLine()

  def run(self):
    print "ctrl+c para terminar"
    #TODO: Hacer que se corte al pulsar una tecla y no cortar con ctrl+c
    try:
      while 1:
        self.makeCall()
        time.sleep(random.randrange(1,5))
    except KeyboardInterrupt, e:
      pass
      



# Codigo principal
s = serialPort()
c = central(s)
c.run()



