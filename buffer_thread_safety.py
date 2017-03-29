#!/usr/bin/python
#  $Id: buffer_thread_safety.py,v 1.3 2012-02-14 00:06:12 sshevtsov Exp $
#
#  Implementacion del buffer circular para usos con multiples threads
#

import threading

class bufferException(Exception):
  pass


class bufferTS:
  def __init__(self,amount = 1000):
    self.data = [];
    self.first = self.last = -1
    self.internalCounter = 0
    self.amount = amount
    for i in range(0,amount):
      self.data.append('')
    """
    semaforo para dormir si el buffer se vacia
    """  
    self.sIsEmpty = threading.Semaphore(1)
    self.sIsEmpty.acquire()
    """
    semaforo para dormir si el buffer se llena
    """  
    self.sIsFull = threading.Semaphore(1)
    """
    semaforo para proteger region critica
    """
    self.sMutex = threading.Semaphore(1)

  def isEmpty(self):
    return self.internalCounter == 0

  def isFull(self):
    return self.internalCounter == self.amount

  """
  retorno el siguiente valor circularmente de value basado en amount
  """
  def __incValue__(self,value):
    return (value + 1) % self.amount
  
  """
  Metodo para el comsumidor.
  Intento obtener el semaforo de vacio, si esta vacio el buffer me duermo,
  sere despertado por el productor. Seguido de esto empieza region critica
  protegida por semaforo mutex. En la region me fijo si estoy lleno, por si 
  tengo que avisar que estoy por sacar un elemento asi puede seguir produciendo.
  Finalmente libero el semaforo de vacio si no quede vacio, y libero el mutex
  (region critica)


  obtener(sVacio)
  obtener(sMutex)
  si lleno -> liberar(sLleno) despierto al productor
  saco
  si no vacio -> liberar(sVacio)
  liberar(sMutex)
  """
  def get(self):
    # me duermo aca si el buffer esta vacio
    self.sIsEmpty.acquire()
    # si llegue hasta aca es porque no estoy vacio me desperto el productor
    # region critica
    self.sMutex.acquire()
    # si estaba lleno despierto al productor porque sacare un elemento
    if self.isFull():
      self.sIsFull.release()
    value = self.data[self.first]
    self.first = self.__incValue__(self.first) 
    self.internalCounter -= 1
    #self.__state__("get")
    if not self.isEmpty(): self.sIsEmpty.release()
    # esto NUCA deberia pasar
    if self.internalCounter < 0:
      raise bufferException('internalCounter less than 0, is a bug')
    self.sMutex.release()
    return value;


  """
  Metodo para el productor.
  Intento obtener el semaforo de buffer lleno, si esta lleno me duermo hasta
  que me despierta el consumidor. Sigue la region critica serializada por 
  el semaforo sMutex, ahi me fijo si estoy vacio libero el semaforo de vacio
  para despertar el consumidor ya que depositare un valor en el buffer.
  Almaceno el dato y libero el semaforo de buffer lleno (sIsFull) si no estoy 
  lleno, caso contrario me dormire en la siguiente llamada por esta lleno.


  obtener(sLleno)
  obtener(sMutex)
  si vacio -> liberar(sVacio) despierto al consumidor
  alamaceno
  si no lleno -> liberar(sLleno)
  liberar(sMutex)
  """
  def put(self, value):
    self.sIsFull.acquire()
    self.sMutex.acquire()
    if self.isEmpty():
      self.sIsEmpty.release()
    self.last = self.__incValue__(self.last)
    self.internalCounter += 1
    self.data[self.last] = value
    if self.first < 0:
      self.first=0;
    #self.__state__("put")
    if not self.isFull():
      self.sIsFull.release()
    # el internalCounter no puede pasar el amount, NUNCA
    if self.internalCounter > self.amount:
      raise bufferException('internalCounter greater than amount, is a bug') 
    self.sMutex.release()


  def __state__(self, msq):
    print "-= "+msq+" =-"
    print "IC: "+str(self.internalCounter)
    print str(self.data)
    print "first="+str(self.first)
    print "last="+str(self.last)




