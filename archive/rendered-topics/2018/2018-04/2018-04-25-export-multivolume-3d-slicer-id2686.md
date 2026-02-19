---
topic_id: 2686
title: "Export Multivolume 3D Slicer"
date: 2018-04-25
url: https://discourse.slicer.org/t/2686
---

# Export multivolume 3D Slicer.

**Topic ID**: 2686
**Date**: 2018-04-25
**URL**: https://discourse.slicer.org/t/export-multivolume-3d-slicer/2686

---

## Post #1 by @ANDREY_FELIPE_ARANGO (2018-04-25 14:51 UTC)

<p>Hi I’m a newbie in 3D Slicer. I’d like to know how to export a multivolume from a module after importing it. I’m not sure about how cleared up is my question but I’ll be pleased about your help.</p>

---

## Post #2 by @lassoan (2018-04-25 20:36 UTC)

<p>What file format would you like to export to? To a single file or to one volume per file?</p>

---

## Post #3 by @ANDREY_FELIPE_ARANGO (2018-04-25 20:56 UTC)

<p>I’d like to export in DICOM format and to one volume per file.</p>

---

## Post #4 by @fedorov (2018-04-26 03:53 UTC)

<p>This cannot be done with Slicer.</p>

---

## Post #5 by @lassoan (2018-04-26 17:16 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="4" data-topic="2686" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>This cannot be done with Slicer.</p>
</blockquote>
</aside>
<p>It is very rare to find something that actually cannot be done in Slicer. The question is mostly about how easy it is to do it, and if it makes sense to do it in Slicer.</p>
<p>Specifically, about how to exporting individual sequence items to DICOM files - it is certainly feasible, but it takes a few steps:</p>
<ul>
<li><a href="https://discourse.slicer.org/t/how-to-split-4d-volumes-to-individual-3d-volumes/2707">split the sequence to individual volume nodes</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export">export each volume to DICOM</a></li>
</ul>
<p>If you need to export a large number of volumes, then you can write a short Python script that performs these steps automatically.</p>

---

## Post #6 by @fedorov (2018-04-26 17:30 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> if I understood the question correctly, the user wants to export individual components of a multivolume, with individual components stored as a single DICOM file (quoting the user: “one volume per file”).</p>
<p>In most cases, multivolume components are 3d volumes, which implies that the individual multivolumes would need to be saved as enhanced or legacy enhanced multiframe storage DICOM objects (which ideally should correspond to the modality from which the multivolume was loaded, and have the attributes propagated from the source DICOM dataset).</p>
<p>To the best of my knowledge, there is no reliable, easy to use tool that would generate such a DICOM object as output. There is <em>definitely</em> no such tool in Slicer.</p>
<p>Indeed, I agree - it can definitely be done. It is “just” DICOM standard, after all. I would love if someone just wrote that converter. We started that work, and we invested significant resources into it, but we do not have a ready to use tool, not even touching its integration with Slicer.</p>

---

## Post #7 by @lassoan (2018-04-26 18:59 UTC)

<p>It’s true that export to multiframe format would be much more work. However, multiframe is still so rare and sparsely supported that I doubt that <a class="mention" href="/u/andrey_felipe_arango">@ANDREY_FELIPE_ARANGO</a> would actually need that format.</p>
<p><a class="mention" href="/u/andrey_felipe_arango">@ANDREY_FELIPE_ARANGO</a> could you describe your workflow? What do you plan to do with the exported DICOM series (what software will load them, what operations you’ll perform on them)?</p>

---

## Post #8 by @ANDREY_FELIPE_ARANGO (2018-05-02 23:03 UTC)

<p>Hi again.</p>
<p>Sorry, I didn’t have enough time to answer quickly. Generally, we are building a module where someone can import a volume file in order to be sliced into individual image files which will be stored with all the data. Then, when we want to export them again, all the individual image files are exported but we want to compact them again in order to export the whole volume previosuly imported.</p>
<p>Please ask me whether you need the code.</p>
<p>Thanks for you help.</p>

---

## Post #9 by @lassoan (2018-05-03 13:14 UTC)

<p>What software will read the exported data?</p>

---

## Post #10 by @ANDREY_FELIPE_ARANGO (2018-05-09 02:11 UTC)

<p>No software. The exported data (volume)  will be just in a folder in DICOM format.</p>
<p>I attach the code that we have until now</p>
<pre><code># -*- coding: cp1252 -*-
##import vtk, qt, ctk, slicer
#
from __future__ import print_function
import sys, re, os, dicom

from __main__ import vtk, qt, ctk, slicer
try:
  NUMPY_AVAILABLE = True
  import vtk.util.numpy_support
except:
  NUMPY_AVAILABLE = False
from MultiVolumeImporterLib.Helper import Helper

#
# MultiVolumeImporter
#

class DataImportExport1:
  def __init__(self, parent):
    parent.title = "DICOM" 
    parent.categories = ["Data Import/Export"]
    parent.dependencies = []
    parent.contributors = ["Andrey Arango, Katerine Muñoz, Robinson Quintero (UdeA)"] # replace with "Firstname Lastname (Organization)"
    parent.helpText = """
        """
    parent.acknowledgementText = """
Mateo Ramirez, John Fredy Ochoa (Asesores)
""" 
    self.parent=parent
    Diccionario={}
    self.Diccionario=Diccionario
class DataImportExport1Widget:
  
  def __init__(self, parent = None):
    if not parent:
      self.parent = slicer.qMRMLWidget()
      self.parent.setLayout(qt.QVBoxLayout())
      self.parent.setMRMLScene(slicer.mrmlScene)
    else:
      self.parent = parent
    self.layout = self.parent.layout()
    if not parent:
      self.setup()
      self.parent.show()

  def setup(self):

    w = qt.QWidget();
    layout = qt.QGridLayout();
    w.setLayout(layout);
    self.layout.addWidget(w);
    w.show();
    self.layout = layout;

####################IMPORTAR VOLUMEN 4D#################################################3

### Se crea la sección para importar
    importDataCollapsibleButton = ctk.ctkCollapsibleButton()
    importDataCollapsibleButton.text = "Import DICOM"
    self.layout.addWidget(importDataCollapsibleButton)
    importDataFormLayout = qt.QFormLayout(importDataCollapsibleButton)
#### Crear desplegable para seleccionar dirección del volumen
    self.__fDialog = ctk.ctkDirectoryButton()
    self.__fDialog.caption = 'Input directory'
    importDataFormLayout.addRow('Input directory:', self.__fDialog)
#### Crear desplegable para seleccionar dirección del volumen
    self.inputSelector = slicer.qMRMLNodeComboBox()
    self.inputSelector.nodeTypes = ['vtkMRMLMultiVolumeNode']
    self.inputSelector.addEnabled = True  # Se habilita la posibildad al usuario de crear un nuevo nodo con este widget
    self.inputSelector.removeEnabled = True  # Se le quita al usuario la posibilidad de eliminar el nodo seleccionado en ese momento
    self.inputSelector.setMRMLScene(slicer.mrmlScene)
    importDataFormLayout.addRow("Input node:", self.inputSelector)
    self.parent.connect('mrmlSceneChanged(vtkMRMLScene*)', self.inputSelector, 'setMRMLScene(vtkMRMLScene*)')

    self.__nameFrame = qt.QLineEdit()
    self.__nameFrame.text = 'NA'
    importDataFormLayout.addRow('Volume Name', self.__nameFrame)

        # Botón de importar
    self.buttonImport = qt.QPushButton("Import")
    self.buttonImport.toolTip = "Run the algorithm."
    importDataFormLayout.addRow("", self.buttonImport)
    self.buttonImport.connect('clicked(bool)', self.importFunction)
### Se crea la sección para exportar
    exportDataCollapsibleButton = ctk.ctkCollapsibleButton()
    exportDataCollapsibleButton.text = "Export DICOM"
    self.layout.addWidget(exportDataCollapsibleButton)
    exportDataFormLayout = qt.QFormLayout(exportDataCollapsibleButton)    
     ###Selector de volumen donde se guardara el volumen de la direccion
    self.outputSelector = slicer.qMRMLNodeComboBox()
    self.outputSelector.nodeTypes = ['vtkMRMLMultiVolumeNode']
    self.outputSelector.addEnabled = False  # Se habilita la posibildad al usuario de crear un nuevo nodo con este widget
    self.outputSelector.removeEnabled = False  # Se le quita al usuario la posibilidad de eliminar el nodo seleccionado en ese momento
    self.outputSelector.setMRMLScene(slicer.mrmlScene)
    exportDataFormLayout.addRow("Volumen to export:", self.outputSelector)
    self.parent.connect('mrmlSceneChanged(vtkMRMLScene*)', self.outputSelector, 'setMRMLScene(vtkMRMLScene*)')                             
  #### Crear desplegable para seleccionar direccion del volumen
    self.__fDialogOutput = ctk.ctkDirectoryButton()
    self.__fDialogOutput.caption = 'DICOM directory'
    exportDataFormLayout.addRow('DiCOM directory:', self.__fDialogOutput)
            # Botón de exportar
    self.buttonExport = qt.QPushButton("Export")
    self.buttonExport.toolTip = "Run the algorithm."
    exportDataFormLayout.addRow("", self.buttonExport)
    self.buttonExport.connect('clicked(bool)', self.ExportFunction)


####################EXPORTAR MANUALMENTE#################################################


### Se crea la sección para importar
    exportManualDataCollapsibleButton = ctk.ctkCollapsibleButton()
    exportManualDataCollapsibleButton.text = "Exportar manualmente"
    self.layout.addWidget(exportManualDataCollapsibleButton)
    exportManualDataFormLayout = qt.QFormLayout(exportManualDataCollapsibleButton)
    
###Selector de volumen donde se guardara el volumen de la direccion
    self.outputManualySelector = slicer.qMRMLNodeComboBox()
    self.outputManualySelector.nodeTypes = ['vtkMRMLMultiVolumeNode']
    self.outputManualySelector.addEnabled = False  # Se habilita la posibildad al usuario de crear un nuevo nodo con este widget
    self.outputManualySelector.removeEnabled = False  # Se le quita al usuario la posibilidad de eliminar el nodo seleccionado en ese momento
    self.outputManualySelector.setMRMLScene(slicer.mrmlScene)
    exportManualDataFormLayout.addRow("Volumen to export manually:", self.outputManualySelector)
    self.parent.connect('mrmlSceneChanged(vtkMRMLScene*)', self.outputManualySelector, 'setMRMLScene(vtkMRMLScene*)')

    
    self.__dicomID = qt.QLineEdit()
    self.__dicomID.text = 'NA'
    exportManualDataFormLayout.addRow('Patient ID:', self.__dicomID)

    self.__dicomName = qt.QLineEdit()
    self.__dicomName.text = 'NA'
    exportManualDataFormLayout.addRow('Patient Name:', self.__dicomName)

    self.__dicomstudyID = qt.QLineEdit()
    self.__dicomstudyID.text = 'NA'
    exportManualDataFormLayout.addRow('Study ID:', self.__dicomstudyID)

    self.__dicomstudyComments = qt.QLineEdit()
    self.__dicomstudyComments.text = 'NA'
    exportManualDataFormLayout.addRow('Study Comments:', self.__dicomstudyComments)

    self.__dicomstudyDescription = qt.QLineEdit()
    self.__dicomstudyDescription.text = 'NA'
    exportManualDataFormLayout.addRow('study Description:', self.__dicomstudyDescription)

    self.__dicommodality = qt.QLineEdit()
    self.__dicommodality.text = 'NA'
    exportManualDataFormLayout.addRow('modality:', self.__dicommodality)

    self.__dicommanufacturer = qt.QLineEdit()
    self.__dicommanufacturer.text = 'NA'
    exportManualDataFormLayout.addRow('manufacturer:', self.__dicommanufacturer)

    self.__dicomseriesNumber = qt.QLineEdit()
    self.__dicomseriesNumber.text = 'NA'
    exportManualDataFormLayout.addRow('series Number:', self.__dicomseriesNumber)

    self.__dicomseriesDescription = qt.QLineEdit()
    self.__dicomseriesDescription.text = 'NA'
    exportManualDataFormLayout.addRow('series Description:', self.__dicomseriesDescription)

    self.__dicomPrefix = qt.QLineEdit()
    self.__dicomPrefix.text = 'IMG'
    exportManualDataFormLayout.addRow('dicomPrefix:', self.__dicomPrefix)
    
    self.__dicomNumberFormat = qt.QLineEdit()
    self.__dicomNumberFormat.text = '%04d'
    exportManualDataFormLayout.addRow('series Description:', self.__dicomNumberFormat)

    #### Crear desplegable para seleccionar direccion del volumen
    self.__fDialogManualOutput = ctk.ctkDirectoryButton()
    self.__fDialogManualOutput.caption = 'DICOM directory'
    exportManualDataFormLayout.addRow('DiCOM directory:', self.__fDialogManualOutput)
            # Botón de exportar
    self.buttonManualExport = qt.QPushButton("Export")
    self.buttonManualExport.toolTip = "Run the algorithm."
    exportManualDataFormLayout.addRow("", self.buttonManualExport)
    self.buttonManualExport.connect('clicked(bool)', self.ExportManualFunction)

  def humanSort(self,l):
    """ Sort the given list in the way that humans expect. 
        Conributed by Yanling Liu
    """ 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    l.sort( key=alphanum_key )

  def ExportManualFunction(self):
    escena = slicer.mrmlScene;
    outputVolume= self.outputManualySelector.currentNode()
    

    volumen4D = outputVolume.GetImageData()
    numero_imagenes = outputVolume.GetNumberOfFrames()
    extract1 = vtk.vtkImageExtractComponents()
    extract1.SetInputData(volumen4D)
    
    ras2ijk = vtk.vtkMatrix4x4()
    ijk2ras = vtk.vtkMatrix4x4()

    outputVolume.GetRASToIJKMatrix(ras2ijk)
    outputVolume.GetIJKToRASMatrix(ijk2ras)
    for i in range(numero_imagenes):

      extract1.SetComponents(i) #Seleccionar un volumen lejano
      extract1.Update()

      ScalarVolume = slicer.vtkMRMLScalarVolumeNode();
      ScalarVolume.SetRASToIJKMatrix(ras2ijk)
      ScalarVolume.SetIJKToRASMatrix(ijk2ras)
      ScalarVolume.SetAndObserveImageData(extract1.GetOutput())
      ScalarVolume.SetName(str('Manual')+str(i+1))
      escena.AddNode(ScalarVolume)
      Parameters={}
      Parameters ['patientID']=self.__dicomID.text
  ##        Parameters ['patientComments']=
      Parameters ['patientName']  = self.__dicomName.text
      Parameters ['studyID']=self.__dicomstudyID.text
##      Parameters ['studyDate']=metadato1.StudyDate
      Parameters ['studyComments']=self.__dicomstudyComments.text
      Parameters ['studyDescription']=self.__dicomstudyDescription
      Parameters ['modality']=self.__dicommodality.text
      Parameters ['manufacturer']=self.__dicommanufacturer.text
  ##        Parameters ['model']=
      Parameters ['seriesNumber']=self.__dicomseriesNumber.text
      Parameters ['seriesDescription']=self.__dicomseriesDescription.text
  ##        Parameters ['rescaleIntercept']=metadato.Rescaleintercept
  ##  Parameter (3/1): rescaleSlope (Rescale slope)
      Parameters ['inputVolume']=ScalarVolume
      Parameters ['dicomDirectory']=self.__fDialogManualOutput.directory
      Parameters ['dicomPrefix']=self.__dicomPrefix.text
      Parameters ['dicomNumberFormat']=self.__dicomNumberFormat.text + str(i+1)
      cliNode = slicer.cli.run( slicer.modules.createdicomseries,None,Parameters,wait_for_completion=True)
    
  def importFunction(self):
    
    self.__dicomTag = 'NA'
    self.__veLabel = 'na'
    self.__veInitial = 0
    self.__veStep = 1
    self.__te = 1
    self.__tr = 1
    self.__fa = 1
    nameFrame = self.__nameFrame.text
    
    
    # check if the output container exists
    mvNode = self.inputSelector.currentNode()
##    if mvNode == None:
##      self.__status.text = 'Status: Select output node!'
##      return



    fileNames = []    # file names on disk
    frameList = []    # frames as MRMLScalarVolumeNode's
    frameFolder = ""
    volumeLabels = vtk.vtkDoubleArray()
    frameLabelsAttr = ''
    frameFileListAttr = ''
    dicomTagNameAttr = self.__dicomTag
    dicomTagUnitsAttr = self.__veLabel
    teAttr = self.__te
    trAttr = self.__tr
    faAttr = self.__fa

    # each frame is saved as a separate volume
    # first filter valid file names and sort alphabetically
    frames = []
    frame0 = None
    inputDir = self.__fDialog.directory
    
    metadatos=[]
    metadato='na'
    print('hola'+str(len(os.listdir(inputDir))))
    for f in os.listdir(inputDir):
    
      if not f.startswith('.'):
        fileName = inputDir+'/'+f
        fileName1 = str(inputDir+'/'+f)
        longitudFilneName=len(fileName1)
        formato=fileName1[(longitudFilneName-3):longitudFilneName]
        if formato=='dcm':
          metadato=dicom.read_file(fileName1)
          metadatos.append(metadato)
        fileNames.append(fileName)
        
        
        
    
      self.humanSort(fileNames)
      n=0

    for fileName in fileNames:
#f: información de cada scalar volume de cada corte
      (s,f) = self.readFrame(fileName)
      
      if s:
        if not frame0:
##          print("valor de f: "+ str(f));
          frame0 = f
##          print("frame0: "+str(frame0));
          frame0Image = frame0.GetImageData()
          frame0Extent = frame0Image.GetExtent()
##          print("frame0Extent: " + str(frame0Extent));
        else:
##          print("valor de f1: "+ str(f))      
          frameImage = f.GetImageData()
##          print("frameImage: "+str(frameImage))
          frameExtent = frameImage.GetExtent()
##          print("frameExtent: " + str(frameExtent));
          if frameExtent[1]!=frame0Extent[1] or frameExtent[3]!=frame0Extent[3] or frameExtent[5]!=frame0Extent[5]:
            continue
##          n=n+1
##          print("for: "+str(n))
        frames.append(f)
        

  

    nFrames = len(frames)
##    print("nFrames: "+str(nFrames))
    print('Successfully read '+str(nFrames)+' frames')

    if nFrames == 1:
      print('Single frame dataset - not reading as multivolume!')
      return

    # convert seconds data to milliseconds, which is expected by pkModeling.cxx line 81
    if dicomTagUnitsAttr == 's':
      frameIdMultiplier = 1000.0
      dicomTagUnitsAttr = 'ms'
    else:
      frameIdMultiplier = 1.0
##    print("volumeLabelsAntes: "+ str(volumeLabels))
    volumeLabels.SetNumberOfTuples(nFrames)
##    print("volumeLabelsIntermedio: "+ str(volumeLabels))
    volumeLabels.SetNumberOfComponents(1)
##    print("volumeLabelsDespues: "+ str(volumeLabels))
    volumeLabels.Allocate(nFrames)
##    print("volumeLabelsTotal: "+ str(volumeLabels))

### Después de los 3 pasos el único cambio es size, en vez de 0 pasa a ser nFrames
    for i in range(nFrames):
      frameId = frameIdMultiplier*(self.__veInitial+self.__veStep*i)
##      print("frameId: "+str(frameId))
      volumeLabels.SetComponent(i, 0, frameId) ##no hay necesidad
####      print("volumeLabelsTotal: "+ str(volumeLabels))##Aparentemente no hay cambio en volumeLabels
      frameLabelsAttr += str(frameId)+','
##      print("frameLabelsAttr: "+str(frameLabelsAttr))
    frameLabelsAttr = frameLabelsAttr[:-1] ##No hay cambio
##    print("frameLabelsAttrTOTAL: "+str(frameLabelsAttr))

    # allocate multivolume
    mvImage = vtk.vtkImageData()
##    print("mvImage: "+str(mvImage))
    mvImage.SetExtent(frame0Extent)
##    print("mvImageExtent: "+str(mvImage))
##    print("vtk.VTK_MAJOR_VERSION: "+str(vtk.VTK_MAJOR_VERSION))
    if vtk.VTK_MAJOR_VERSION &lt;= 5: ##Versión 7
      mvImage.SetNumberOfScalarComponents(nFrames)
      print("mvImageSC: "+str(mvImage))
      mvImage.SetScalarType(frame0.GetImageData().GetScalarType())
      print("mvImageST: "+str(mvImage))
      mvImage.AllocateScalars()
      print("mvImageAllocate: "+str(mvImage))
    else:
      mvImage.AllocateScalars(frame0.GetImageData().GetScalarType(), nFrames)
##      print("mvImageElse: "+str(mvImage))
      
    extent = frame0.GetImageData().GetExtent()
    numPixels = float(extent[1]+1)*(extent[3]+1)*(extent[5]+1)*nFrames
    scalarType = frame0.GetImageData().GetScalarType()
    print('Will now try to allocate memory for '+str(numPixels)+' pixels of VTK scalar type'+str(scalarType))
    print('Memory allocated successfully')
    mvImageArray = vtk.util.numpy_support.vtk_to_numpy(mvImage.GetPointData().GetScalars())
##    print("mvImageEArray: "+str(mvImageArray))
##    print("mvImage.GetPointData().GetScalars(): " + str(mvImage.GetPointData().GetScalars()));
##    print("ID mvImagearray " + str(id(mvImageArray)));
##    print("ID 2: " + str(mvImage.GetPointData().GetScalars()));
##    print("Que es frame0: " + str(frame0));


    ##EMPIEZA A FORMARCE EL VOLUMEN###############

    mat = vtk.vtkMatrix4x4()
    frame0.GetRASToIJKMatrix(mat)
    mvNode.SetRASToIJKMatrix(mat)
    frame0.GetIJKToRASMatrix(mat)
    mvNode.SetIJKToRASMatrix(mat)
    print("frameId: "+str(frameId))
    print("# imag: "+str(nFrames))
##    print("Long frame: "+str(len(frame)))
    for frameId in range(nFrames):
      # TODO: check consistent size and orientation!
      frame = frames[frameId]
      frameImage = frame.GetImageData()
      frameImageArray = vtk.util.numpy_support.vtk_to_numpy(frameImage.GetPointData().GetScalars())
      mvImageArray.T[frameId] = frameImageArray

    mvDisplayNode = slicer.mrmlScene.CreateNodeByClass('vtkMRMLMultiVolumeDisplayNode')
    mvDisplayNode.SetScene(slicer.mrmlScene)
    slicer.mrmlScene.AddNode(mvDisplayNode)
    mvDisplayNode.SetReferenceCount(mvDisplayNode.GetReferenceCount()-1)
    mvDisplayNode.SetDefaultColorMap()

    mvNode.SetAndObserveDisplayNodeID(mvDisplayNode.GetID())
    mvNode.SetAndObserveImageData(mvImage)
    mvNode.SetNumberOfFrames(nFrames)

    mvNode.SetLabelArray(volumeLabels)
    mvNode.SetLabelName(self.__veLabel)

    mvNode.SetAttribute('MultiVolume.FrameLabels',frameLabelsAttr)
    mvNode.SetAttribute('MultiVolume.NumberOfFrames',str(nFrames))
    mvNode.SetAttribute('MultiVolume.FrameIdentifyingDICOMTagName',dicomTagNameAttr)
    mvNode.SetAttribute('MultiVolume.FrameIdentifyingDICOMTagUnits',dicomTagUnitsAttr)

    if dicomTagNameAttr == 'TriggerTime' or dicomTagNameAttr == 'AcquisitionTime':
      if teAttr != '':
        mvNode.SetAttribute('MultiVolume.DICOM.EchoTime',teAttr)
      if trAttr != '':
        mvNode.SetAttribute('MultiVolume.DICOM.RepetitionTime',trAttr)
      if faAttr != '':
        mvNode.SetAttribute('MultiVolume.DICOM.FlipAngle',faAttr)

    mvNode.SetName(nameFrame)
    
    NameFrame=nameFrame
    self.Diccionario={NameFrame:metadato};
    print(self.Diccionario.get(NameFrame))
    Helper.SetBgFgVolumes(mvNode.GetID(),None)
  

  def readFrame(self,file):
    sNode = slicer.vtkMRMLVolumeArchetypeStorageNode()
    sNode.ResetFileNameList()
    sNode.SetFileName(file)
    sNode.SetSingleFile(0)
    frame = slicer.vtkMRMLScalarVolumeNode()
    success = sNode.ReadData(frame)
    return (success,frame)

  # leave no trace of the temporary nodes
  def annihilateScalarNode(self, node):
    dn = node.GetDisplayNode()
    sn = node.GetStorageNode()
    node.SetAndObserveDisplayNodeID(None)
    node.SetAndObserveStorageNodeID(None)
    slicer.mrmlScene.RemoveNode(dn)
    slicer.mrmlScene.RemoveNode(sn)
    slicer.mrmlScene.RemoveNode(node)

  def ExportFunction(self):
    escena = slicer.mrmlScene;
    outputVolume= self.outputSelector.currentNode()
    outputDir=self.__fDialogOutput.directory
    Nombre=outputVolume.GetName()
    metadato1=self.Diccionario.get(Nombre)

    volumen4D = outputVolume.GetImageData()
    numero_imagenes = outputVolume.GetNumberOfFrames()
    extract1 = vtk.vtkImageExtractComponents()
    extract1.SetInputData(volumen4D)
    
    ras2ijk = vtk.vtkMatrix4x4()
    ijk2ras = vtk.vtkMatrix4x4()

    outputVolume.GetRASToIJKMatrix(ras2ijk)
    outputVolume.GetIJKToRASMatrix(ijk2ras)
    print(outputDir)
    
    for i in range(numero_imagenes):

      extract1.SetComponents(i) #Seleccionar un volumen lejano
      extract1.Update()

      ScalarVolume = slicer.vtkMRMLScalarVolumeNode();
      ScalarVolume.SetRASToIJKMatrix(ras2ijk)
      ScalarVolume.SetIJKToRASMatrix(ijk2ras)
      ScalarVolume.SetAndObserveImageData(extract1.GetOutput())
      ScalarVolume.SetName(str(Nombre)+str(i+1))
      escena.AddNode(ScalarVolume)
      Parameters={}
      
      Parameters ['patientID']=metadato1.PatientID
##        Parameters ['patientComments']=
      Parameters ['patientName']  = 'Validacion_PIS'
      Parameters ['studyID']=metadato1.StudyID
      Parameters ['studyDate']=metadato1.StudyDate
      Parameters ['studyComments']=metadato1.StudyComments
      Parameters ['studyDescription']=metadato1.StudyDescription
      Parameters ['modality']=metadato1.Modality
      Parameters ['manufacturer']=metadato1.Manufacturer
##        Parameters ['model']=
      Parameters ['seriesNumber']=metadato1.SeriesNumber
      Parameters ['seriesDescription']=metadato1.SeriesDescription
##        Parameters ['rescaleIntercept']=metadato.Rescaleintercept
##  Parameter (3/1): rescaleSlope (Rescale slope)
      Parameters ['inputVolume']=ScalarVolume
      Parameters ['dicomDirectory']=outputDir
      Parameters ['dicomPrefix']='IMG'
      Parameters ['dicomNumberFormat']='%04d' + str(i+1)
      cliNode = slicer.cli.run( slicer.modules.createdicomseries,None,Parameters,wait_for_completion=True)
        
      



    ##        Parameters ['patientName']= 'Katy'
    



  
   
    qt.QMessageBox.information(slicer.util.mainWindow(),'Slicer Python','Multivolume Exportado')
    
##    
##
##cliModule = slicer.modules.createdicomseries
##n=cliModule.cliModuleLogic().CreateNode()
##for groupIndex in xrange(0,n.GetNumberOfParameterGroups()):
##  for parameterIndex in xrange(0,n.GetNumberOfParametersInGroup(groupIndex)):
##    print '  Parameter ({0}/{1}): {2} ({3})'.format(groupIndex, parameterIndex, n.GetParameterName(groupIndex, parameterIndex), n.GetParameterLabel(groupIndex, parameterIndex))
##
.</code></pre>

---

## Post #11 by @lassoan (2018-05-09 03:41 UTC)

<aside class="quote no-group" data-username="ANDREY_FELIPE_ARANGO" data-post="10" data-topic="2686">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/49beb7/48.png" class="avatar"> ANDREY_FELIPE_ARANGO:</div>
<blockquote>
<p>No software. The exported data (volume) will be just in a folder in DICOM format.</p>
</blockquote>
</aside>
<p>DICOM files can be created so many ways (especially 4D volumes), so it is very important to know what software do you plan to use them with. What software will read the data that you save? Are you going to implement that software or is it an existing software? Commercial or in-house developed prototype?</p>

---

## Post #12 by @Robinson_Quintero (2018-05-09 18:52 UTC)

<p>Thanks for your support. We just want to export to 3D Slicer. I mean, we want to export it but like a multi volumen with DICOM format.</p>

---

## Post #13 by @lassoan (2018-05-09 19:00 UTC)

<p>There is no multi-volume DICOM format but there are many ways how you can store 3D+t data sets in DICOM. We can only help if you know exactly what software you need this exported data to be compatible with.</p>
<p>If you only need to make sure Slicer can load the data set, then I would recommend to use nrrd instead of DICOM format.</p>

---

## Post #14 by @ANDREY_FELIPE_ARANGO (2018-05-09 21:08 UTC)

<p>I’m understanding what are you saying but we made a mistake in the explanation of the nature of the exported data. We just want to export the volumes of a sliced multi-volume, i.e. we import a multi-volume data, which is sliced and then we want to export the same volume not the individual images like it’s happening. For example, one multivolume has 60 volumes and each volume has 60 images. When we are exporting them to a folder, 3600 individual images are imported. We are aiming the exporting of 60 volumes.</p>

---

## Post #15 by @lassoan (2018-05-14 03:25 UTC)

<p>OK, then as I wrote above, you can follow the instructions described in this post: <a href="https://discourse.slicer.org/t/how-to-split-4d-volumes-to-individual-3d-volumes/2707">How to split 4D volumes to individual 3D volumes?</a></p>

---

## Post #16 by @Nassir (2018-07-24 04:15 UTC)

<p>Sorry to bring this back from the dead but the short python script you described is exactly what I am trying to make. Mostly, it’s the exporting part (with a header tweaking) that I’m trying to automate. Here it is from line 44 onwards (the first 44 lines are because I tried to embed it in a extension (from the tutorial) as I didn’t know how to run the script elsehow). <a href="https://drive.google.com/open?id=1yFAAoAtv7dcTUFfDBQ9ByA4MXMiUdX0F" rel="nofollow noopener">https://drive.google.com/open?id=1yFAAoAtv7dcTUFfDBQ9ByA4MXMiUdX0F</a></p>
<p>I think the code should work, but I keep getting I get the error global name ‘getNode’ is not defined. getNode works if I type it into the interactor, so is there something that I need to import that I have not?</p>
<p>Cheers</p>
<p>P.S: Is there a way for me to figure this out on my own using the interactor, or is it just background that I need to get used to?</p>

---

## Post #17 by @lassoan (2018-07-24 17:47 UTC)

<p><code>getNode</code> is defined in <code>slicer.util</code> package, which is imported into the Python interpreter’s namespace for convenience, but in modules, you would need to use <code>slicer.util.getNode</code>.</p>
<p>However, <code>getNode</code> is developed for testing and interactive use. In modules, it is recommended to use the more explicit get methods in the scene, for example <code>slicer.mrmlScene.GetFirstNodeByName(...)</code>.</p>

---

## Post #18 by @Nassir (2018-08-03 00:45 UTC)

<p>I have one more question about making this pythons script.</p>
<p>Unfortunately, because (1) the data that I am using is high in magnitude and precision and (2) the “create a dicom series” module by default uses the output type “short”, exporting the data using a (quite similar) script results in: dicom images where values that would have been higher  than 16 bit (say 100000 Bqml) become negative values (say -4000 Bqml).</p>
<p>I couldn’t go around route (1), but route (2) offers an easy solution if I manually set the Output Type to “int”. However, this is not a helpful solution for automation. <em>I have been trying to find a way to automatically specify the Output Type, but I can’t figure out how to read the documentation of CLI modules</em>. Another way I’ve been trying to figure this out is using python interactor’s help operation/tab key on <em>slicer.modules.createdicomseries</em>, but my search is fruitless.</p>
<p>TLDR: how does one use python to pass non-dictionary parameters into a CLI module (specifically output type into create a dicom series).</p>

---

## Post #19 by @Nicole_Aucoin (2018-08-03 13:50 UTC)

<p>You can look at the  XML that defines the interface for the module by running the cli with the --xml flag. Or you can look at the source code :<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/CLI/CreateDICOMSeries/CreateDICOMSeries.xml#L179" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/CLI/CreateDICOMSeries/CreateDICOMSeries.xml#L179" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/CLI/CreateDICOMSeries/CreateDICOMSeries.xml#L179</a></h4>
<pre class="onebox"><code class="lang-xml"><ol class="start lines" start="169" style="counter-reset: li-counter 168 ;">
<li>  &lt;longflag&gt;--useCompression&lt;/longflag&gt;</li>
<li>  &lt;description&gt;&lt;![CDATA[Compress the output pixel data.]]&gt;&lt;/description&gt;</li>
<li>  &lt;label&gt;Use Compression&lt;/label&gt;</li>
<li>  &lt;default&gt;false&lt;/default&gt;</li>
<li>&lt;/boolean&gt;</li>
<li>&lt;label&gt;Filter Settings&lt;/label&gt;</li>
<li>&lt;string-enumeration&gt;</li>
<li>  &lt;name&gt;Type&lt;/name&gt;</li>
<li>  &lt;label&gt;Output Type:&lt;/label&gt;</li>
<li>  &lt;description&gt;&lt;![CDATA[Type for the new output volume.]]&gt;&lt;/description&gt;</li>
<li class="selected">  &lt;longflag&gt;--type&lt;/longflag&gt;</li>
<li>  &lt;flag&gt;--t&lt;/flag&gt;</li>
<li>  &lt;default&gt;Short&lt;/default&gt;</li>
<li>  &lt;element&gt;UnsignedChar&lt;/element&gt;</li>
<li>  &lt;element&gt;Char&lt;/element&gt;</li>
<li>  &lt;element&gt;UnsignedChar&lt;/element&gt;</li>
<li>  &lt;element&gt;Short&lt;/element&gt;</li>
<li>  &lt;element&gt;UnsignedShort&lt;/element&gt;</li>
<li>  &lt;element&gt;Int&lt;/element&gt;</li>
<li>  &lt;element&gt;UnsignedInt&lt;/element&gt;</li>
<li>&lt;/string-enumeration&gt;</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
In there it has the output type argument as --type and you can pass it Int</p>

---
