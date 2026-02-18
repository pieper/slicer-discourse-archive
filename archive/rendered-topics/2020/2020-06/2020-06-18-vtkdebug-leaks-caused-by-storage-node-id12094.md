# vtkDebug Leaks caused by storage node

**Topic ID**: 12094
**Date**: 2020-06-18
**URL**: https://discourse.slicer.org/t/vtkdebug-leaks-caused-by-storage-node/12094

---

## Post #1 by @Queen_Rei (2020-06-18 14:04 UTC)

<p>Hello! I am trying to resolve some leaks that are related to the following lines.<br>
This script is meant to run the module 100 ms after start-up and when I remove this snippet the errors go away. Is there a flaw in the way I set this up?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15bb558ab12ddf4d7135720893fac92d6c885a2f.png" alt="image" data-base62-sha1="36fo59ZG0qiyzpEHTmCjtaXDQL5" width="448" height="204"></p>
<pre><code># Loading Dicom into scene
masterLoadedNodeID = loadedNodeIDs[0]
seriesVolumeNode = slicer.util.getNode(masterLoadedNodeID)
storageVolumeNode = seriesVolumeNode.CreateDefaultStorageNode()
seriesVolumeNode.SetAndObserveStorageNodeID(storageVolumeNode.GetID())
</code></pre>
<p>Just for more context these are the lines right before the snippet causing errors.</p>
<pre><code>from DICOMLib import DICOMUtils
loadedNodeIDs = []

with DICOMUtils.TemporaryDICOMDatabase() as db:
  DICOMUtils.importDicom(dicomDataDir, db)
  patientUIDs = db.patients()
  for patientUID in patientUIDs:
    loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
</code></pre>

---

## Post #2 by @pieper (2020-06-18 15:40 UTC)

<p>It would be good if you could post a full script to reproduce the issue.</p>

---

## Post #3 by @lassoan (2020-06-18 16:05 UTC)

<p>Most probably the issue is that your Python variable is created in the global scope and keeps a reference to the node, so the node does not get deleted. You can either create your variables in a local scope (in a function) or set them to None after you don’t need them anymore:</p>
<pre><code class="lang-python">...
seriesVolumeNode = None
storageVolumeNode = None
</code></pre>

---

## Post #4 by @Queen_Rei (2020-06-18 19:39 UTC)

<p>Here is the entire part of the script that is involved with this bug:</p>
<pre><code>import os
import unittest
import logging
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin

class DICOM2OBJ(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "DICOM2OBJ"
    self.parent.categories = ["Modules"]
    self.parent.dependencies = []
    self.parent.contributors = ["Andrew Gonzalez"]
    self.parent.helpText = """
This is an example of scripted loadable module bundled in an extension.
It performs a simple thresholding on the input volume and optionally captures a screenshot.
"""
    self.parent.helpText += self.getDefaultModuleDocumentationLink()
    self.parent.acknowledgementText = "acknowledgementText"
    self.RunOnStartUp()
    
  def RunOnStartUp(self):
    # Run module on startup of slicer
    slicer.app.connect("startupCompleted()", self.LoadSegment)
  
  def LoadSegment(self):
    # Adding delay to allow other slicer modules to be instantiated
    qt.QTimer.singleShot(100, self.ProceduralSegmentation)

  def ProceduralSegmentation(self):
 
    # TODO create text box for input folder
    # Importing Dicom into temporary database
    dicomDataDir = "C:/Users/Public/Pictures"
    from DICOMLib import DICOMUtils
    loadedNodeIDs = []
    
    with DICOMUtils.TemporaryDICOMDatabase() as db:
      DICOMUtils.importDicom(dicomDataDir, db)
      patientUIDs = db.patients()
      for patientUID in patientUIDs:
        loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))

	# Loading Dicom into scene
    seriesVolumeNode = slicer.util.getNode(loadedNodeIDs[0])
    storageVolumeNode = seriesVolumeNode.CreateDefaultStorageNode()
    seriesVolumeNode.SetAndObserveStorageNodeID(storageVolumeNode.GetID())
    storageVolumeNode = None

    # Access segmentation module
    slicer.util.selectModule('Segment Editor')
    segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
    slicer.mrmlScene.AddNode(segmentationNode)
    segmentationNode.CreateDefaultDisplayNodes() # only needed for display
    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(seriesVolumeNode)
    
    # TODO Automate creation of different segments in the future
    # Create spine segment
    segmentTypeID = "Spine"
    newSegment = slicer.vtkSegment()
    newSegment.SetName(segmentTypeID)
    newSegment.SetColor([0.89, 0.85, 0.78])
    segmentationNode.GetSegmentation().AddSegment(newSegment,segmentTypeID)

    # Create segment editor widget to get access to effects
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)

    # Access segment editor node
    segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
    slicer.mrmlScene.AddNode(segmentEditorNode)
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(segmentationNode)
    segmentEditorWidget.setMasterVolumeNode(seriesVolumeNode)
    seriesVolumeNode = None</code></pre>

---

## Post #5 by @Queen_Rei (2020-06-18 19:40 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Per your suggestions I set them to None after they aren’t needed anymore and the error did not go away. To my knowledge they are being created in the ProceduralSegmentation() method. Would having the method in the DICOM2OBJ class be the issue?</p>
<p>I also tried doing it with a method and it just doubled the same leaks, so I’m suspecting the nodes are being declared globally some how.</p>

---

## Post #6 by @lassoan (2020-06-18 19:54 UTC)

<aside class="quote no-group" data-username="Queen_Rei" data-post="4" data-topic="12094">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/queen_rei/48/6348_2.png" class="avatar"> Queen_Rei:</div>
<blockquote>
<p><code>storageVolumeNode = seriesVolumeNode.CreateDefaultStorageNode()</code></p>
</blockquote>
</aside>
<p>The issue is this line. <code>CreateDefaultStorageNode</code> is a factory method: it creates a new object that must be destroyed by the caller using <code>UnRegister</code>. So, you need to add this line to fix the memory leak:</p>
<pre><code>storageVolumeNode.UnRegister()
</code></pre>
<p>See more details here:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MemoryManagement#Python_scripts_and_scripted_modules" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MemoryManagement#Python_scripts_and_scripted_modules</a></p>

---

## Post #7 by @Queen_Rei (2020-06-18 20:08 UTC)

<p>Thanks! That resolved it~</p>

---
