#!/usr/bin/python
# -*- coding: utf8 -*-

from math import cos,sin

class Rot:
	"""Clase que define movimiento rotacional de dos
	cuerpos alrededor de un punto en movimiento
	"""
	
	def __init__(self,l1,l2,w=2):
		"""
		l1 Distancia del cuerpo de rotacion al objeto 1
		l2 Distancia del cuerpo de rotacion al objeto 2
		w  Velocidad angular de rotacion
		"""
		self.l1=l1
		self.l2=l2
		self.w=w
		
	def pos1(self,t):
		"""Posicion del cuerpo 1 en funcion del tiempo
		
		retorna una tupla x,y con las coordenadas del cuerpo para el tiempo t
		"""
		c=self.c_pos(t)
		x=c[0]+self.l1*cos(self.w*t)
		y=c[1]+self.l1*sin(self.w*t)
		return x,y

	def pos2(self,t):
		"""Posicion del cuerpo 2 en funcion del tiempo
		
		retorna una tupla x,y con las coordenadas del cuerpo para el tiempo t
		"""

		c=self.c_pos(t)
		x=c[0]-self.l2*cos(self.w*t)
		y=c[1]-self.l2*sin(self.w*t)
		return x,y
	
	def c_pos(self,t):
		"""Metodo que debe ser sobrecargado y retornar la posicion del 
		centro de rotacion
		"""
		return (0,0)
		
if __name__=="__main__":
	import pylab as pl
	
	
	def f(self,t):
		return(.5*t,.3*t**2)
	
	Rot.c_pos=f
	 
	r=Rot(1,.5,4)
	
	
	
	
	p1x,p1y,p2x,p2y=[],[],[],[]
    
	for t in range(100):
		t1=t/10.
		x1,y1=r.pos1(t1)
		x2,y2=r.pos2(t1)
		p1x.append(x1)
		p2x.append(x2)
		p1y.append(y1)
		p2y.append(y2)
		
		
	pl.figure()
	pl.axis("equal")
	pl.plot(p1x,p1y,"*")
	pl.plot(p2x,p2y,"o")
	
	pl.show()
