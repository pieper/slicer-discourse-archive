---
topic_id: 19650
title: "Qmrmlnodecombobox Not Initializing With Scene Information"
date: 2021-09-13
url: https://discourse.slicer.org/t/19650
---

# qMRMLNodeComboBox not initializing with scene information

**Topic ID**: 19650
**Date**: 2021-09-13
**URL**: https://discourse.slicer.org/t/qmrmlnodecombobox-not-initializing-with-scene-information/19650

---

## Post #1 by @tsims (2021-09-13 19:51 UTC)

<p>Hi everyone, I have been working on setting up a slicer module in python and am having an issue where my qMRMLNodeComboBox UI element isn’t initializing. I have copied the default scripted module as near as I can tell but still the ComboBox stays diabled and empty as the scene loads. Is there a setting that I am missing</p>
<p>The code for my module:</p>
<pre><code class="lang-auto">import os
import unittest
import logging
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin

#
# CranioMaxilloFacial
#

class CranioMaxilloFacial(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "CranioMaxilloFacial"  # TODO: make this more human readable by adding spaces
    self.parent.categories = ["VSP"]  # TODO: set categories (folders where the module shows up in the module selector)
    self.parent.dependencies = []  # TODO: add here list of module names that this module requires
    self.parent.contributors = ["Tres Sims (Digital Anatomy Simulations for Healthcare)"]  # TODO: replace with "Firstname Lastname (Organization)"
    # TODO: update with short description of the module and a link to online module documentation
    self.parent.helpText = """
        This is an example of scripted loadable module bundled in an extension.
        See more information in &lt;a href="https://github.com/organization/projectname#CranioMaxilloFacial"&gt;module documentation&lt;/a&gt;.
        """
    # TODO: replace with organization, grant and thanks
    self.parent.acknowledgementText = """
        This file was originally developed by Tres Sims and Fluvio Lobo at Digital Anatomy Simulations for Healthcare, LLC
        """

#
# CranioMaxilloFacialWidget
#

class CranioMaxilloFacialWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent=None):
    """
    Called when the user opens the module the first time and the widget is initialized.
    """
    ScriptedLoadableModuleWidget.__init__(self, parent)
    VTKObservationMixin.__init__(self)  # needed for parameter node observation
    self.logic = None
    self._parameterNode = None
    self._updatingGUIFromParameterNode = False

  def setup(self):
    """
    Called when the user opens the module the first time and the widget is initialized.
    """
    ScriptedLoadableModuleWidget.setup(self)

    # Load widget from .ui file (created by Qt Designer).
    # Additional widgets can be instantiated manually and added to self.layout.
    uiWidget = slicer.util.loadUI(self.resourcePath('UI/CranioMaxilloFacial.ui'))
    self.layout.addWidget(uiWidget)
    self.ui = slicer.util.childWidgetVariables(uiWidget)

    # Set scene in MRML widgets. Make sure that in Qt designer the top-level qMRMLWidget's
    # "mrmlSceneChanged(vtkMRMLScene*)" signal in is connected to each MRML widget's.
    # "setMRMLScene(vtkMRMLScene*)" slot.
    uiWidget.setMRMLScene(slicer.mrmlScene)

    # Create logic class. Logic implements all computations that should be possible to run
    # in batch mode, without a graphical user interface.
    self.logic = CranioMaxilloFacialLogic()

    # Connections

    # These connections ensure that we update parameter node when scene is closed
    self.addObserver(slicer.mrmlScene, slicer.mrmlScene.StartCloseEvent, self.onSceneStartClose)
    self.addObserver(slicer.mrmlScene, slicer.mrmlScene.EndCloseEvent, self.onSceneEndClose)

    # These connections ensure that whenever user changes some settings on the GUI, that is saved in the MRML scene
    # (in the selected parameter node).
    self.ui.fiducialListSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.updateParameterNodeFromGUI)

    # Buttons
    self.ui.alignButton.connect('clicked(bool)', self.onApplyButton)

    # Make sure parameter node is initialized (needed for module reload)
    self.initializeParameterNode()

  def cleanup(self):
    """
    Called when the application closes and the module widget is destroyed.
    """
    self.removeObservers()

  def enter(self):
    """
    Called each time the user opens this module.
    """
    # Make sure parameter node exists and observed
    self.initializeParameterNode()

  def exit(self):
    """
    Called each time the user opens a different module.
    """
    # Do not react to parameter node changes (GUI wlil be updated when the user enters into the module)
    self.removeObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)

  def onSceneStartClose(self, caller, event):
    """
    Called just before the scene is closed.
    """
    # Parameter node will be reset, do not use it anymore
    self.setParameterNode(None)

  def onSceneEndClose(self, caller, event):
    """
    Called just after the scene is closed.
    """
    # If this module is shown while the scene is closed then recreate a new parameter node immediately
    if self.parent.isEntered:
      self.initializeParameterNode()

  def initializeParameterNode(self):
    """
    Ensure parameter node exists and observed.
    """

    print("initialize parameter node")
    # Parameter node stores all user choices in parameter values, node selections, etc.
    # so that when the scene is saved and reloaded, these settings are restored.

    self.setParameterNode(self.logic.getParameterNode())

    # Select default input nodes if nothing is selected yet to save a few clicks for the user
    if not self._parameterNode.GetNodeReference("InputFiducials"):
      firstVolumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
      if firstVolumeNode:
        self._parameterNode.SetNodeReferenceID("InputFiducials", firstVolumeNode.GetID())
        print("initialization success")

  def setParameterNode(self, inputParameterNode):
    """
    Set and observe parameter node.
    Observation is needed because when the parameter node is changed then the GUI must be updated immediately.
    """

    print("set parameter node")

    if inputParameterNode:
      self.logic.setDefaultParameters(inputParameterNode)

    # Unobserve previously selected parameter node and add an observer to the newly selected.
    # Changes of parameter node are observed so that whenever parameters are changed by a script or any other module
    # those are reflected immediately in the GUI.
    if self._parameterNode is not None:
      self.removeObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)
    self._parameterNode = inputParameterNode
    if self._parameterNode is not None:
      self.addObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)
 
    # Initial GUI update
    self.updateGUIFromParameterNode()

  def updateGUIFromParameterNode(self, caller=None, event=None):
    """
    This method is called whenever parameter node is changed.
    The module GUI is updated to show the current state of the parameter node.
    """

    if self._parameterNode is None or self._updatingGUIFromParameterNode:
      return

    # Make sure GUI changes do not call updateParameterNodeFromGUI (it could cause infinite loop)
    self._updatingGUIFromParameterNode = True

    # Update node selectors and sliders
    self.ui.fiducialListSelector.setCurrentNode(self._parameterNode.GetNodeReference("InputFiducials"))

    # Update buttons states and tooltips
    if self._parameterNode.GetNodeReference("InputFiducials"):
      self.ui.alignButton.toolTip = "Align and center skull based off of fiducial landmarks"
      self.ui.alignButton.enabled = True
    else:
      self.ui.alignButton.toolTip = "Select necessary components for alignment"
      self.ui.alignButton.enabled = False

    # All the GUI updates are done
    self._updatingGUIFromParameterNode = False

  def updateParameterNodeFromGUI(self, caller=None, event=None):
    """
    This method is called when the user makes any change in the GUI.
    The changes are saved into the parameter node (so that they are restored when the scene is saved and loaded).
    """

    if self._parameterNode is None or self._updatingGUIFromParameterNode:
      return

    wasModified = self._parameterNode.StartModify()  # Modify all properties in a single batch

    self._parameterNode.SetNodeReferenceID("InputFiducials", self.ui.fiducialListSelector.currentNodeID)

    self._parameterNode.EndModify(wasModified)

  def onApplyButton(self):
    """
    Run processing when user clicks "Apply" button.
    """
    pass


#
# CranioMaxilloFacialLogic
#

class CranioMaxilloFacialLogic(ScriptedLoadableModuleLogic):
  """This class should implement all the actual
  computation done by your module.  The interface
  should be such that other python code can import
  this class and make use of the functionality without
  requiring an instance of the Widget.
  Uses ScriptedLoadableModuleLogic base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self):
    """
    Called when the logic class is instantiated. Can be used for initializing member variables.
    """
    ScriptedLoadableModuleLogic.__init__(self)

  def setDefaultParameters(self, parameterNode):
    """
    Initialize parameter node with default settings.
    """
    pass

  def process(self, inputVolume, outputVolume, imageThreshold, invert=False, showResult=True):
    """
    Run the processing algorithm.
    Can be used without GUI widget.
    :param inputVolume: volume to be thresholded
    :param outputVolume: thresholding result
    :param imageThreshold: values above/below this threshold will be set to 0
    :param invert: if True then values above the threshold will be set to 0, otherwise values below are set to 0
    :param showResult: show output volume in slice viewers
    """

    pass
</code></pre>
<p>The UI File code:</p>
<pre><code class="lang-auto">&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;ui version="4.0"&gt;
 &lt;class&gt;CranioMaxilloFacial&lt;/class&gt;
 &lt;widget class="qMRMLWidget" name="CranioMaxilloFacial"&gt;
  &lt;property name="geometry"&gt;
   &lt;rect&gt;
    &lt;x&gt;0&lt;/x&gt;
    &lt;y&gt;0&lt;/y&gt;
    &lt;width&gt;279&lt;/width&gt;
    &lt;height&gt;484&lt;/height&gt;
   &lt;/rect&gt;
  &lt;/property&gt;
  &lt;layout class="QVBoxLayout" name="verticalLayout"&gt;
   &lt;item&gt;
    &lt;widget class="QLabel" name="fiducialListLabel"&gt;
     &lt;property name="text"&gt;
      &lt;string&gt;Fiducial List&lt;/string&gt;
     &lt;/property&gt;
    &lt;/widget&gt;
   &lt;/item&gt;
   &lt;item&gt;
    &lt;widget class="qMRMLNodeComboBox" name="fiducialListSelector"&gt;
     &lt;property name="toolTip"&gt;
      &lt;string&gt;Pick a fiducial list for alignment&lt;/string&gt;
     &lt;/property&gt;
     &lt;property name="nodeTypes"&gt;
      &lt;stringlist&gt;
       &lt;string&gt;vtkMRMLScalarVolumeNode&lt;/string&gt;
      &lt;/stringlist&gt;
     &lt;/property&gt;
     &lt;property name="showChildNodeTypes"&gt;
      &lt;bool&gt;false&lt;/bool&gt;
     &lt;/property&gt;
     &lt;property name="addEnabled"&gt;
      &lt;bool&gt;false&lt;/bool&gt;
     &lt;/property&gt;
     &lt;property name="removeEnabled"&gt;
      &lt;bool&gt;false&lt;/bool&gt;
     &lt;/property&gt;
    &lt;/widget&gt;
   &lt;/item&gt;
   &lt;item&gt;
    &lt;widget class="QPushButton" name="alignButton"&gt;
     &lt;property name="enabled"&gt;
      &lt;bool&gt;false&lt;/bool&gt;
     &lt;/property&gt;
     &lt;property name="toolTip"&gt;
      &lt;string&gt;Run the algorithm.&lt;/string&gt;
     &lt;/property&gt;
     &lt;property name="text"&gt;
      &lt;string&gt;Align&lt;/string&gt;
     &lt;/property&gt;
    &lt;/widget&gt;
   &lt;/item&gt;
   &lt;item&gt;
    &lt;spacer name="verticalSpacer"&gt;
     &lt;property name="orientation"&gt;
      &lt;enum&gt;Qt::Vertical&lt;/enum&gt;
     &lt;/property&gt;
     &lt;property name="sizeHint" stdset="0"&gt;
      &lt;size&gt;
       &lt;width&gt;20&lt;/width&gt;
       &lt;height&gt;40&lt;/height&gt;
      &lt;/size&gt;
     &lt;/property&gt;
    &lt;/spacer&gt;
   &lt;/item&gt;
  &lt;/layout&gt;
 &lt;/widget&gt;
 &lt;customwidgets&gt;
  &lt;customwidget&gt;
   &lt;class&gt;qMRMLNodeComboBox&lt;/class&gt;
   &lt;extends&gt;QWidget&lt;/extends&gt;
   &lt;header&gt;qMRMLNodeComboBox.h&lt;/header&gt;
  &lt;/customwidget&gt;
  &lt;customwidget&gt;
   &lt;class&gt;qMRMLWidget&lt;/class&gt;
   &lt;extends&gt;QWidget&lt;/extends&gt;
   &lt;header&gt;qMRMLWidget.h&lt;/header&gt;
   &lt;container&gt;1&lt;/container&gt;
  &lt;/customwidget&gt;
 &lt;/customwidgets&gt;
 &lt;resources/&gt;
 &lt;connections/&gt;
&lt;/ui&gt;
</code></pre>

---

## Post #2 by @tsims (2021-09-14 13:03 UTC)

<p>I was able to solve my own problem! The issue was that I had not configured the signals appropriately in the .ui file. After doing that everything worked as intended.</p>

---
