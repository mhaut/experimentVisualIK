import sys, os, Ice, traceback, math, random, copy
import numpy as np
import commands
import time
import subprocess
from PySide import *
from PyQt4 import QtGui
from PyQt4.QtGui import QApplication, QDialog
from ui_MainWindow import *


ROBOCOMP = ''
try:
	ROBOCOMP = os.environ['ROBOCOMP']
except:
	print '$ROBOCOMP environment variable not set, using the default value /opt/robocomp'
	ROBOCOMP = '/opt/robocomp'
if len(ROBOCOMP)<1:
	print '|| ROBOCOMP environment variable not set! Exiting.'
	sys.exit()


preStr = "-I"+ROBOCOMP+"/interfaces/ --all "+ROBOCOMP+"/interfaces/"
Ice.loadSlice(preStr+"InverseKinematics.ice")
from RoboCompInverseKinematics import *

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

ic = None




##configCJoint = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefSim/ursusCommon.conf"
##configAprilT = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefSim/apriltags.conf"
################################              OLD CONFIG
###configIK     = "/home/robocomp/robocomp/components/robocomp-ursus-rockin/etc/ficheros_Test_VisualBIK/ikSim.conf"
###configIKG    = "/home/robocomp/robocomp/components/robocomp-ursus-rockin/etc/ficheros_Test_VisualBIK/ikgSim.conf"
###configVIK    = "/home/robocomp/robocomp/components/robocomp-ursus-rockin/etc/ficheros_Test_VisualBIK/vikSim.conf"

##configIK     = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefSim/inversekinematics.conf"
##configIKG    = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefSim/ikg.conf"
##configVIK    = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefSim/vikSim.conf"



###############CONFIG DEFINITIVOS VISUAL EXPERIMENT SIMULATION.
###configCJoint = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefSim/ursusCommon.conf"
###configAprilT = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefSim/apriltags.conf"
###configIK     = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefSim/inversekinematics.conf"
###configIKG    = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefSim/ikg.conf"
###configVIK    = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefSim/vik.conf"
################################################################

##############CONFIG DEFINITIVOS VISUAL EXPERIMENT REMOTE. NOT WORK. The process in the script are in local. I recommended use rcremote
##configCJoint = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefReal/ursusCommon.conf"
##configAprilT = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefReal/apriltags.conf"
##configIK     = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefReal/inversekinematics.conf"
##configIKG    = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefReal/ikg.conf"
##configVIK    = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefReal/vik.conf"
###############################################################

############CONFIG DEFINITIVOS VISUAL EXPERIMENT SIMULATION.
#configCJoint = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefSim/ursusCommon.conf"
#configAprilT = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefSim/apriltags.conf"
#configIK     = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefSim/inversekinematics.conf"
#configIKG    = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefSim/ikg.conf"
#configVIK    = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefSim/vik.conf"
#############################################################
############CONFIG DEFINITIVOS VISUAL EXPERIMENT SIMULATION.
configCJoint = "/home/robocomp/robocomp/components/robocomp-ursus/etc/ursusCommon.conf"
configAprilT = "/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefSim/apriltags.conf" #"/home/robocomp/robocomp/components/robocomp-ursus/etc/apriltags.conf"
configIK     = "/home/robocomp/robocomp/components/robocomp-ursus/etc/inversekinematics.conf"
configIKG    = "/home/robocomp/robocomp/components/robocomp-ursus/etc/ikg.conf"
configVIK    = "/home/robocomp/robocomp/components/robocomp-ursus/etc/vik.conf"
#############################################################






numTargets = 10
nohupIK      = True
nohupGIK      = True
nohupVIK      = True

class Auxiliar(QtGui.QDialog,Ice.Application):
	#-------------------------------------------------------------------
	# CONSTRUCTOR: inicializa la clase y levanta la interfaz de usuario
	#-------------------------------------------------------------------
	def __init__(self, params):
		super(Auxiliar, self).__init__()
				
		global ic
	  	#ic = self.communicator()
		ic = Ice.initialize(params)
	  	print "---->",type(ic)
	  	
		self.inversekinematics_proxy_0 = None
		self.inversekinematics_proxy_1 = None
		self.ui = Ui_guiDlg()
		self.ui.setupUi(self)
		self.show()
		
		self.stop = False
		self.ui.stopButton.clicked.connect(self.stopTest)
		self.ui.testButton.clicked.connect(self.runTest)
		
	#------------------------------------------------------------------#
	#                 METODOS AUXILIARES DEL PROGRAMA                  #
	#------------------------------------------------------------------#
	#######################################################
	### SLOTS DE LA CLASE
	#######################################################
	def stopTest(self):
		if self.stop == True:
			self.stop = False
			self.ui.stopButton.setText("Reanude")
		else:
			self.stop = True
			self.ui.stopButton.setText("Stop")

	#### TODO QUITAR COMENTARIOS 
	def runTest(self):
		self.ui.testButton.setEnabled(False)
		self.weights = WeightVector() #vector de pesos
		self.weights.x = 1
		self.weights.y = 1
		self.weights.z = 1
		self.weights.rx = 0.1
		self.weights.ry = 0.1
		self.weights.rz = 0.1
		
		self.axis = Axis() #vector de ejes
		self.axis.x = 0
		self.axis.y = 0
		self.axis.z = 1
			
		#Genero 100 targets aleatorios y los almaceno en un vector:
		self.targets = []
		while len(self.targets)<numTargets:
			pose6D    = Pose6D()
			pose6D.x  = random.randint(240, 300)
			pose6D.y  = random.randint(1000, 1250)
			pose6D.z  = random.randint(380, 470)
			pose6D.rx = 0
			pose6D.ry = -0.80
			pose6D.rz = 0 #-3.1416
			if (pose6D in self.targets) == False:
				self.targets.append(pose6D)
				
		#Eliminamos los ficheros que puedan contener basura:
		os.system("rm /home/robocomp/robocomp/components/robocomp-ursus/components/visualik/data.txt")

		self.i=1
		self.doTest()
	

	#### TODO QUITAR COMENTARIOS	
	def doTest(self):
		################################################
		############################ VIK
		os.system("rm /home/robocomp/robocomp/components/robocomp-ursus/components/visualik/data.txt")
		os.system('killall -9 VisualBIK ikGraphGenerator inversekinematics ursuscommonjointcomp apriltagscomp')

		##LEVANTAMOS EL URSUS COMMON JOINT
		self.ui.textEdit_2.append(str(self.i)+'---> ejecutando ursus common joint\n')
		print '############################# ejecutando ursus common joint'
		os.system('killall -9 ursuscommonjointcomp')
		os.system('nohup /home/robocomp/robocomp/components/robocomp-ursus/components/ursusCommonJoint/bin/ursuscommonjointcomp --Ice.Config='+configCJoint+' > /dev/null &')
		##LEVANTAMOS EL APRIL TAGS
		self.ui.textEdit_2.append(str(self.i)+'---> ejecutando apriltags\n')
		print '############################# ejecutando apriltags'
		os.system('killall -9 apriltagscomp')
		os.system('nohup /home/robocomp/robocomp/components/robocomp-robolab/components/apriltagsComp/bin/apriltagscomp --Ice.Config='+configAprilT+' > /dev/null &')
		#DORMIMOS 5 SEGUNDOS
		time.sleep(5)
		
		##LEVANTAMOS EL INVERSEKINEMATICS
		self.ui.textEdit_2.append(str(self.i)+'--->  ejecutando IK\n')
		print '############################# ejecutando IK'
		os.system('killall -9 inversekinematics')
		command = '/home/robocomp/robocomp/components/robocomp-ursus/components/inversekinematics/bin/inversekinematics --Ice.Config='+configIK
		if nohupIK is True:
                    command = 'nohup '+command+' 2> ikDATA.txt'
		os.system(command+' &')
		#DORMIMOS 5 SEGUNDOS
		time.sleep(10)
		
		##LEVANTAMOS EL INVERSEKINEMATICSGRAPH
		self.ui.textEdit_2.append(str(self.i)+'--->  ejecutando GIK\n')
		print '############################# ejecutando GIK'
		os.system('killall -9 ikGraphGenerator')
		command = '/home/robocomp/robocomp/components/robocomp-ursus/components/ikGraphGenerator/bin/ikGraphGenerator --Ice.Config='+configIKG
		if nohupGIK is True:
                    command = 'nohup '+command+' 2> graphDATA.txt'
		os.system(command+' &')
		#DORMIMOS 5 SEGUNDOS
		time.sleep(10)		
		
		##LEVANTAMOS EL VISUAL INVERSEKINEMATICS
		self.ui.textEdit_2.append(str(self.i)+'--->  ejecutando VIK\n')
		print '############################# ejecutando VIK'
		os.system('killall -9 VisualBIK')
		command = '/home/robocomp/robocomp/components/robocomp-ursus/components/visualik/bin/VisualBIK --Ice.Config='+configVIK
		if nohupVIK is True:
                    command = 'nohup '+command+' 2> visualDATA.txt'
		os.system(command+' &')
		#DORMIMOS 5 SEGUNDOS
		time.sleep(10)
		
		#### CREAR EL PROXY AL INVERSEKINEMATICS
		self.initializeProxy_0()
		##ENVIAMOS LOS TARGETS:
		j=0
		for pose in self.targets:
			#mandamos al home
			try:
				self.inversekinematics_proxy_0.goHome("RIGHTARM")
				time.sleep(7)
			except:
				print "fallo al enviar al home"
			print "\n\nIteracion ("+str(j)+")", "Pose Actual: ["+str(pose.x)+", "+str(pose.y)+", "+str(pose.z)+", "+str(pose.rx)+", "+str(pose.ry)+", "+str(pose.rz)+"]"
			try:
				#Primero a la CABEZA para que mire:
				part = "HEAD"
				self.inversekinematics_proxy_0.setTargetAlignaxis(part, pose, self.axis)
				
				part = "RIGHTARM"
				identificador = self.inversekinematics_proxy_0.setTargetPose6D(part,pose, self.weights)
				
				state = TargetState()
				state = self.inversekinematics_proxy_0.getTargetState("RIGHTARM", identificador)
				while state.finish!=True:
					state = self.inversekinematics_proxy_0.getTargetState("RIGHTARM", identificador)

				#Ya hemos terminado: escribimos el dato
				try:
                                    infile = open ("/home/robocomp/robocomp/components/robocomp-ursus/components/visualik/data.txt" ,"r" )
                                    lines = infile.readlines () 
                                    if len(lines)<=0:
                                            print "FICHERO VACIO"
                                            sys.exit(-1)

                                    infile.close ()
                                    last_line = lines [ len ( lines ) -1 ]
                                    #print last_line
                                    if "\n" != last_line:
                                        print "ultima linea",last_line
                                        self.ui.textEdit.append(last_line+'\n')
                                        #TODO ALERT MERCEDES REVISAR
                                        step1 = last_line.split(":");
                                        step2 = step1[2].split(" ")
                                        
                                        #ANIADIDO POR MARIO
                                        #step2 = last_line.split(" ");
                                        ############################
                                        
                                        error_vt = float(step2[0])
                                        print "Error visual alcanzado: ", error_vt 
                                except IOError as e:
                                    print e
                                    sys.exit(-1)
			except:
				print "EXCEPCION EN SEND POSE 6D"
				traceback.print_exc()
                        j += 1

	
		print 'ITERACION HECHA!'
		#GUARDAMOS LOS DATOS EN OTRO FICHERO
		os.system('mv /home/robocomp/robocomp/components/robocomp-ursus/components/visualik/data.txt /home/robocomp/robocomp/components/experimentVisualIK/files/visualBIKexperiment/output/datosObtenidos_VIK'+str(self.i).zfill(5)+'.txt')

		##############################################################################################
		##############################################################################################
		##############################################################################################
		##############################################################################################
		os.system("rm /home/robocomp/robocomp/components/robocomp-ursus/components/inversekinematics/data.txt")
		os.system('killall -9 VisualBIK ikGraphGenerator inversekinematics ursuscommonjointcomp apriltagscomp')

		
		##LEVANTAMOS EL URSUS COMMON JOINT
		self.ui.textEdit_2.append(str(self.i)+'---> ejecutando ursus common joint\n')
		print '############################# ejecutando ursus common joint'
		os.system('killall -9 ursuscommonjointcomp')
		os.system('nohup /home/robocomp/robocomp/components/robocomp-ursus/components/ursusCommonJoint/bin/ursuscommonjointcomp --Ice.Config='+configCJoint+' > /dev/null &')
		time.sleep(5)
		
		##LEVANTAMOS EL INVERSEKINEMATICS
		self.ui.textEdit_2.append(str(self.i)+'--->  ejecutando IK\n')
		print '############################# ejecutando IK'
		os.system('killall -9 inversekinematics')
		command = '/home/robocomp/robocomp/components/robocomp-ursus/components/inversekinematics/bin/inversekinematics --Ice.Config='+configIK
		if nohupIK is True:
                    command = 'nohup '+command+' 2> ikDATA.txt'
		os.system(command+' &')
		#DORMIMOS 5 SEGUNDOS
		time.sleep(10)

		##LEVANTAMOS EL INVERSEKINEMATICSGRAPH
		self.ui.textEdit_2.append(str(self.i)+'--->  ejecutando GIK\n')
		print '############################# ejecutando GIK'
		os.system('killall -9 ikGraphGenerator')
		command = '/home/robocomp/robocomp/components/robocomp-ursus/components/ikGraphGenerator/bin/ikGraphGenerator --Ice.Config='+configIKG
		if nohupGIK is True:
                    command = 'nohup '+command+' 2> graphDATA.txt'
		os.system(command+' &')
		#DORMIMOS 5 SEGUNDOS
		time.sleep(10)	

		#######
		self.initializeProxy_1()
		##ENVIAMOS LOS TARGETS:
		j=0
		for pose in self.targets:
			#mandamos al home
			try:
				self.inversekinematics_proxy_1.goHome("RIGHTARM")
				time.sleep(7)
			except:
				print "fallo al enviar al home"
			print "\n\nIteracion ("+str(j)+")", "Pose Actual: ["+str(pose.x)+", "+str(pose.y)+", "+str(pose.z)+", "+str(pose.rx)+", "+str(pose.ry)+", "+str(pose.rz)+"]"
			try:
				#Primero a la CABEZA para que mire:
				part = "HEAD"
				self.inversekinematics_proxy_1.setTargetAlignaxis(part, pose, self.axis)
				
				part = "RIGHTARM"
				identificador = self.inversekinematics_proxy_1.setTargetPose6D(part,pose, self.weights)
			
				state = TargetState()
				state = self.inversekinematics_proxy_1.getTargetState("RIGHTARM", identificador)
				while state.finish!=True:
					state = self.inversekinematics_proxy_1.getTargetState("RIGHTARM", identificador)

				#Ya hemos terminado: escribimos el dato
				try:
                                    infile = open ("/home/robocomp/robocomp/components/robocomp-ursus/components/ikGraphGenerator/data.txt" ,"r" )
                                    lines = infile.readlines () 
                                    if len(lines)<=0:
                                            print "FICHERO VACIO"
                                            sys.exit(-1)

                                    infile.close ()
                                    last_line = lines [ len ( lines ) -1 ]
                                    #print last_line
                                    if "\n" != last_line:
                                        print "ultima linea",last_line
                                        self.ui.textEdit.append(last_line+'\n')
                                        #TODO ALERT MERCEDES REVISAR
                                        step1 = last_line.split(":");
                                        step2 = step1[2].split(" ")
                                        
                                        #ANIADIDO POR MARIO
                                        #step2 = last_line.split(" ");
                                        ############################
                                        
                                        error_vt = float(step2[0])
                                        print "Error visual alcanzado: ", error_vt 
                                except IOError as e:
                                    print e
                                    sys.exit(-1)
			except:
				print "EXCEPCION EN SEND POSE 6D"
				traceback.print_exc()
                        j += 1

	
		#print 'ITERACION HECHA!'
		#GUARDAMOS LOS DATOS EN OTRO FICHERO
		os.system('mv /home/robocomp/robocomp/components/robocomp-ursus/components/inversekinematics/data.txt /home/robocomp/robocomp/components/experimentVisualIK/files/visualBIKexperiment/output/datosObtenidos_IK'+str(self.i).zfill(5)+'.txt')
		
				
	#######################################################
	### METODOS PRIVADOS DE LA CLASE
	#######################################################
	#### Inicializa el proxy al visualIK.
	def initializeProxy_0(self):
		print "PROXY_VIK"
		import RoboCompInverseKinematics
		status = 0
		try:
			# Remote object connection for InverseKinematics
			try:
				proxyString = ic.getProperties().getProperty('InverseKinematicsProxy_0')
				print "Proxy VIK ----------------------->" + proxyString
				try:
					basePrx = ic.stringToProxy(proxyString)
					self.inversekinematics_proxy_0 = RoboCompInverseKinematics.InverseKinematicsPrx.checkedCast(basePrx)
				except Ice.Exception:
					print 'Cannot connect to the remote object (InverseKinematics)', proxyString
					status = 1
			except Ice.Exception, e:
				print e
				print 'Cannot get InverseKinematicsProxy_0 property.'
				status = 1
		except:
			traceback.print_exc()
			status = 1

	#### Inicializa el proxy al IK.
	def initializeProxy_1(self):
		print "PROXY_IK"
		import RoboCompInverseKinematics
		status = 0
		try:
			# Remote object connection for InverseKinematics
			try:
				proxyString = ic.getProperties().getProperty('InverseKinematicsProxy_1')
				print "Proxy IK ----------------------->" + proxyString
				try:
					basePrx = ic.stringToProxy(proxyString)
					self.inversekinematics_proxy_1 = RoboCompInverseKinematics.InverseKinematicsPrx.checkedCast(basePrx)
				except Ice.Exception:
					print 'Cannot connect to the remote object (InverseKinematics)', proxyString
					status = 1
			except Ice.Exception, e:
				print e
				print 'Cannot get InverseKinematicsProxy_1 property.'
				status = 1
		except:
			traceback.print_exc()
			status = 1
			
	def generateErrorsXML(self, input_file, output_file, stdDevT, stdDevR, stdDevF):
		fields = dict()
		fields["tx"]    = stdDevT
		fields["ty"]    = stdDevT
		fields["tz"]    = stdDevT
		fields["rx"]    = stdDevR
		fields["ry"]    = stdDevR
		fields["rz"]    = stdDevR
		fields["focal"] = stdDevF

		entrada = open(input_file, "r")
		salida  = open(output_file, "w")

		for line in entrada.readlines():
			lineOut = copy.deepcopy(line)
			if "@error".lower() in line.lower():
				if "<transform" in line:
					lineOut = self.cambiaError(line, fields)
				elif "<translation" in line:
					lineOut = self.cambiaError(line, fields)
				elif "<rotation" in line:
					lineOut = self.cambiaError(line, fields)
				elif "<rgbd" in line:
					lineOut = self.cambiaError(line, fields)
				else:
					print 'whaaaat', line
			salida.write(lineOut)
		entrada.close()
		salida.close()
		
	def cambiaError(self, line, fields):
		ret = ''
		s = line.split('"')
		first = ''
		for i in xrange(len(s)):
			if i%2 == 1:
				done = False
				for field in fields:
					if s[i-1].endswith(field+'='):
						if len(s)>i and "@error".lower() in s[i].lower():
							XXX = s[i]
							base = s[i].lower().split("@error")[0]
							if base == '':
								base = 0
							else:
								base = float(base)
							fl = s[i-1][:-1].strip()
							#print 'field', fl
							err = 0
							if fields[fl] > 0.:
								err = np.random.normal(0., fields[fl], 1)[0]
								while err > 2.*fields[fl]:
									err = np.random.normal(0., fields[fl], 1)[0]
							ret += first + str(base+err)
							first = '"'
							done = True
							break
				if not done:
					ret += first + s[i]
					first = '"'
			else:
				ret += first + s[i]
				first = '"'
		return ret
