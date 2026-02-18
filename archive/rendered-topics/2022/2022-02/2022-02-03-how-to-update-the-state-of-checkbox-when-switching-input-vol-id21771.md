# How to update the state of checkbox when switching input volume node

**Topic ID**: 21771
**Date**: 2022-02-03
**URL**: https://discourse.slicer.org/t/how-to-update-the-state-of-checkbox-when-switching-input-volume-node/21771

---

## Post #1 by @PhilipDavis (2022-02-03 05:55 UTC)

<p>Hi there,<br>
I’m new to 3D Slicer and now I’m developing a Python scripted module.<br>
Currently, I’m trying to add a checkbox to control the display of the ROI bounding box in the volume rendering scene, which is actually the same as the ‘Display ROI’ checkbox in the volume rendering module.<br>
Now the ROI bounding box can be shown by clicking the checkbox, but the problem is that when I switch the input volume, the state of the checkbox on the GUI panel is always the same.</p>
<p>As shown in the figure, I first turned on the ROI bounding box for ‘MRHead’, but when I switch the input volume to a new volume(‘CTChest’), the state of the checkbox is also checked, but I haven’t checked it yet:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/352fa8ed9968e7c453f4e7c1bc2c5ca179b363bb.jpeg" data-download-href="/uploads/short-url/7AvpPYg5HUV29WoHcn3x5eTPJBV.jpeg?dl=1" title="figure1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/352fa8ed9968e7c453f4e7c1bc2c5ca179b363bb_2_690x406.jpeg" alt="figure1" data-base62-sha1="7AvpPYg5HUV29WoHcn3x5eTPJBV" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/352fa8ed9968e7c453f4e7c1bc2c5ca179b363bb_2_690x406.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/352fa8ed9968e7c453f4e7c1bc2c5ca179b363bb_2_1035x609.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/352fa8ed9968e7c453f4e7c1bc2c5ca179b363bb.jpeg 2x" data-dominant-color="B5B5C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure1</span><span class="informations">1297×765 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfa595069887520b3f14ba6007d4198881e3e01f.jpeg" data-download-href="/uploads/short-url/rlnXcMhiRDo2Qu0MUiO35MYQn3F.jpeg?dl=1" title="figure2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bfa595069887520b3f14ba6007d4198881e3e01f_2_690x372.jpeg" alt="figure2" data-base62-sha1="rlnXcMhiRDo2Qu0MUiO35MYQn3F" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bfa595069887520b3f14ba6007d4198881e3e01f_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bfa595069887520b3f14ba6007d4198881e3e01f_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfa595069887520b3f14ba6007d4198881e3e01f.jpeg 2x" data-dominant-color="B3B3C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure2</span><span class="informations">1341×724 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there any way to make the state of the checkbox and the input volume correspond one-to-one?</p>
<p>This seems to be because there doesn’t seem to be a connection between the input volume node and the checkbox widget.<br>
However, the checkbox widget derived from CTK:</p>
<pre><code class="lang-auto">self.ROICheckBox = ctk.ctkCheckBox()
</code></pre>
<p>It seems means I can’t connect it to the input volume by something like:</p>
<blockquote>
<p>self.ROICheckBox.setMRMLVolumeNode(VolumeNode)</p>
</blockquote>
<p>I attached my source code below, hoping to get specific guidance on how to fix this bug. Please make sure you turn on the volume rendering for both volumes first to test it.</p>
<p>Thank you very much in advance!</p>
<pre><code class="lang-auto">import logging
import os
import unittest
import vtk, qt, ctk, slicer
import SegmentStatistics
from slicer.ScriptedLoadableModule import *
from slicer.util import TESTING_DATA_URL
from slicer.util import VTKObservationMixin



class ScriptedLoadableModuleTemplate(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "TestCheckbox" # TODO make this more human readable by adding spaces
    self.parent.categories = ["Examples"]
    self.parent.dependencies = []
    self.parent.contributors = ["John Doe (AnyWare Corp.)"] # replace with "Firstname Lastname (Organization)"
    self.parent.helpText = """
    The Help text for this scripted module.
"""


    self.parent.helpText += self.getDefaultModuleDocumentationLink()

    self.parent.acknowledgementText = """
   The acknowledgementText
"""



#
# ScriptedLoadableModuleTemplateWidget
#

class ScriptedLoadableModuleTemplateWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):
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
    ScriptedLoadableModuleWidget.setup(self)

    # Instantiate and connect widgets ...


    #
    # Parameters Area
    #
    parametersCollapsibleButton = ctk.ctkCollapsibleButton()
    parametersCollapsibleButton.text = "ROI"
    self.layout.addWidget(parametersCollapsibleButton)
    parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)

    self.logic = ScriptedLoadableModuleTemplateLogic()


    #
    # input volume selector
    #
    self.inputSelector = slicer.qMRMLNodeComboBox()
    self.inputSelector.nodeTypes = ["vtkMRMLScalarVolumeNode"]
    self.inputSelector.selectNodeUponCreation = True
    self.inputSelector.addEnabled = False
    self.inputSelector.removeEnabled = False
    self.inputSelector.noneEnabled = False
    self.inputSelector.showHidden = False
    self.inputSelector.showChildNodeTypes = False
    self.inputSelector.setMRMLScene(slicer.mrmlScene)
    self.inputSelector.setToolTip( "Pick the input to the algorithm." )
    parametersFormLayout.addRow("Input Volume: ", self.inputSelector)


    #
    # ROI checkbox
    #
    self.ROICheckBox =  ctk.ctkCheckBox()
    self.ROICheckBox.enabled = True
    self.ROICheckBox.checked = False
    parametersFormLayout.addRow("ROI:", self.ROICheckBox)
    # self.ROICheckBox.setMRMLVolumeNode(volNode)


    self.addObserver(slicer.mrmlScene, slicer.mrmlScene.StartCloseEvent, self.onSceneStartClose)
    self.addObserver(slicer.mrmlScene, slicer.mrmlScene.EndCloseEvent, self.onSceneEndClose)

    # connections
    self.inputSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.updateParameterNodeFromGUI)
    self.ROICheckBox.connect('clicked(bool)', self.onCheckBox)


    self.initializeParameterNode()

    # Add vertical spacer
    self.layout.addStretch(1)


  def onCheckBox(self):
    VolumeNode = self._parameterNode.GetNodeReference('InputVolume')
    if VolumeNode:
      self.logic.updateROIOnVolume(VolumeNode, self.ROICheckBox.checked)



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
    # Parameter node stores all user choices in parameter values, node selections, etc.
    # so that when the scene is saved and reloaded, these settings are restored.

    self.setParameterNode(self.logic.getParameterNode())

    # Select default input nodes if nothing is selected yet to save a few clicks for the user
    if not self._parameterNode.GetNodeReference("InputVolume"):
      firstVolumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
      if firstVolumeNode:
        self._parameterNode.SetNodeReferenceID("InputVolume", firstVolumeNode.GetID())


  def setParameterNode(self, inputParameterNode):
    """
    Set and observe parameter node.
    Observation is needed because when the parameter node is changed then the GUI must be updated immediately.
    """
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
    self.inputSelector.setCurrentNode(self._parameterNode.GetNodeReference("InputVolume"))
    self.ROICheckBox.checked = (self._parameterNode.GetParameter("ROI") == "true")

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

    self._parameterNode.SetNodeReferenceID("InputVolume", self.inputSelector.currentNodeID)
    self._parameterNode.SetParameter("ROI", "true" if self.ROICheckBox.checked else "false")

    self._parameterNode.EndModify(wasModified)


#
# ScriptedLoadableModuleTemplateLogic
#

class ScriptedLoadableModuleTemplateLogic(ScriptedLoadableModuleLogic):
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



  def updateROIOnVolume(self, VolumeNode, ROIchecked=False):
    VolumeLogic = slicer.modules.volumerendering.logic()
    displayNode = VolumeLogic.GetFirstVolumeRenderingDisplayNode(VolumeNode)
    displayNode.UnRegister(slicer.mrmlScene)
    slicer.mrmlScene.AddNode(displayNode)
    VolumeNode.AddAndObserveDisplayNodeID(displayNode.GetID())
    VolumeLogic.UpdateDisplayNodeFromVolumeNode(displayNode, VolumeNode)
    if ROIchecked == True:
      displayNode.GetROINode().SetDisplayVisibility(True)
      displayNode.SetCroppingEnabled(True)
    else:
      displayNode.GetROINode().SetDisplayVisibility(False)




</code></pre>

---

## Post #2 by @PhilipDavis (2022-02-03 21:52 UTC)

<p>Hello <a class="mention" href="/u/mikebind">@mikebind</a> ,<br>
Could you please take a look at my code and point out how to address it?<br>
Thank you!</p>

---

## Post #3 by @mikebind (2022-02-03 22:08 UTC)

<p>There is no direct linkage between the checkbox, the ROI node, and the volume rendering which would mean that a change in the checkbox or in the volume would lead to a change in which ROI is shown. Your module code needs to handle that process.  Here is what I think you want to happen (correct me if I am wrong!):</p>
<p>Changing to a different input volume in the “Input volume” combobox should</p>
<ol>
<li>Make the ROI from the prior image volume invisible, regardless of the ROI checkbox state, and</li>
<li>Make the ROI from the new image volume visible, only if the ROI checkbox state is checked.</li>
</ol>
<p>Independently, toggling the ROI checkbox should make the ROI associated with the current input volume visible when checked and invisible when unchecked.</p>
<p>Is that correct?</p>

---

## Post #4 by @PhilipDavis (2022-02-03 22:47 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="3" data-topic="21771">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Independently, toggling the ROI checkbox should make the ROI associated with the current input volume visible when checked and invisible when unchecked.</p>
</blockquote>
</aside>
<p>Hello <a class="mention" href="/u/mikebind">@mikebind</a>, Yes, you are correct, you mentioned above is what exactly I want. However, about the first thing you mentioned:</p>
<blockquote>
<p>Make the ROI from the prior image volume invisible, regardless of the ROI checkbox state.</p>
</blockquote>
<p>I think when user change the input volume in the combobox, the ROI from the prior image volume can still be visible only if he did just turn on its checkbox.</p>
<p>Could you make some change based on the code I just post to address it? Thank you very much!</p>
<p>And what I’d like to achieve is actually same as the ‘Display ROI’ checkbox in the volume rendering module:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b8ffbd3ba08922af31b470e0bb942afa7826879.jpeg" data-download-href="/uploads/short-url/mcautBB3kuLKUWTZKehmUBtHxxv.jpeg?dl=1" title="figure1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b8ffbd3ba08922af31b470e0bb942afa7826879_2_517x281.jpeg" alt="figure1" data-base62-sha1="mcautBB3kuLKUWTZKehmUBtHxxv" width="517" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b8ffbd3ba08922af31b470e0bb942afa7826879_2_517x281.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b8ffbd3ba08922af31b470e0bb942afa7826879_2_775x421.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b8ffbd3ba08922af31b470e0bb942afa7826879_2_1034x562.jpeg 2x" data-dominant-color="B8B6C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure1</span><span class="informations">1387×754 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/510e72b72458a6af28cb550b4046e73c0b081236.jpeg" data-download-href="/uploads/short-url/bz3D3QtZjNgdBmKg7nozTfs104C.jpeg?dl=1" title="figure2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/510e72b72458a6af28cb550b4046e73c0b081236_2_517x290.jpeg" alt="figure2" data-base62-sha1="bz3D3QtZjNgdBmKg7nozTfs104C" width="517" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/510e72b72458a6af28cb550b4046e73c0b081236_2_517x290.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/510e72b72458a6af28cb550b4046e73c0b081236_2_775x435.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/510e72b72458a6af28cb550b4046e73c0b081236_2_1034x580.jpeg 2x" data-dominant-color="B9B8C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure2</span><span class="informations">1306×734 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @mikebind (2022-02-03 22:56 UTC)

<p>This gist starts from your code (first revision) and then has all the changes to make the behavior I described in the post above (<a href="https://discourse.slicer.org/t/how-to-update-the-state-of-checkbox-when-switching-input-volume-node/21771/3" class="inline-onebox">How to update the state of checkbox when switching input volume node - #3 by mikebind</a>) (see the second revision).</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/mikebind/a3a4ee96076ab23d0e0339a47d02adfb">
  <header class="source">

      <a href="https://gist.github.com/mikebind/a3a4ee96076ab23d0e0339a47d02adfb" target="_blank" rel="noopener">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/mikebind/a3a4ee96076ab23d0e0339a47d02adfb" target="_blank" rel="noopener">https://gist.github.com/mikebind/a3a4ee96076ab23d0e0339a47d02adfb</a></h4>

  <h5>ScriptedLoadableModuleTemplate.py</h5>
  <pre><code class="Python">import logging
import os
import unittest
import vtk, qt, ctk, slicer
import SegmentStatistics
from slicer.ScriptedLoadableModule import *
from slicer.util import TESTING_DATA_URL
from slicer.util import VTKObservationMixin

</code></pre>
    This file has been truncated. <a href="https://gist.github.com/mikebind/a3a4ee96076ab23d0e0339a47d02adfb" target="_blank" rel="noopener">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>See if you can use that to get the behavior you want.  If I understand correctly, you should be able to get that behavior just by removing the code which hides the prior volume ROI.</p>

---

## Post #6 by @PhilipDavis (2022-02-03 23:31 UTC)

<p>Hello <a class="mention" href="/u/mikebind">@mikebind</a>,<br>
Thank you for your kind reply!<br>
I tested the code you just provided. However, I found that the ROI Checkbox doesn’t work for the second input volume, as you can see, when I uncheck it, the ROI checkbox is still there:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1af82a6fa453a85d923ac9d52a4675a89741f43.png" data-download-href="/uploads/short-url/yu36aPlygOFF4Dd8mnYyyT2GnqH.png?dl=1" title="figure2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1af82a6fa453a85d923ac9d52a4675a89741f43_2_517x213.png" alt="figure2" data-base62-sha1="yu36aPlygOFF4Dd8mnYyyT2GnqH" width="517" height="213" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1af82a6fa453a85d923ac9d52a4675a89741f43_2_517x213.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1af82a6fa453a85d923ac9d52a4675a89741f43_2_775x319.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1af82a6fa453a85d923ac9d52a4675a89741f43_2_1034x426.png 2x" data-dominant-color="C6C7DB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure2</span><span class="informations">1267×524 82.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/516a8fbc4f7374ff55501e522c65f421d1ee9962.png" data-download-href="/uploads/short-url/bCeYSNkjJxbvzLtDoiZiaLHMDoC.png?dl=1" title="figure1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/516a8fbc4f7374ff55501e522c65f421d1ee9962_2_517x225.png" alt="figure1" data-base62-sha1="bCeYSNkjJxbvzLtDoiZiaLHMDoC" width="517" height="225" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/516a8fbc4f7374ff55501e522c65f421d1ee9962_2_517x225.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/516a8fbc4f7374ff55501e522c65f421d1ee9962_2_775x337.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/516a8fbc4f7374ff55501e522c65f421d1ee9962_2_1034x450.png 2x" data-dominant-color="C9CADC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure1</span><span class="informations">1219×533 81.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you take a look at my previous/last post and figures:</p>
<blockquote>
<p>However, about the first thing you mentioned: Make the ROI from the prior image volume invisible, regardless of the ROI checkbox state. I think when user change the input volume in the combobox, the ROI from the prior image volume can still be visible only if he did just turn on its checkbox. And what I’d like to achieve is actually same as the ‘Display ROI’ checkbox in the volume rendering module.</p>
</blockquote>
<p>, and see if you can totally get what I describe? Thank you so much!</p>

---

## Post #7 by @mikebind (2022-02-03 23:48 UTC)

<p>On my machine the ROI visibility follows the checkbox with that code.  Can you check to see if an error was generated on yours?  There is an indicator in the lower right of the window which turns into a red X if there has been an error, and if you click on it you can see the log.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a918197bdd96e6d37bececf0a0f59be04bba1a2.png" alt="image" data-base62-sha1="jLPDsX2N4TTpiTgQVN24KuvJsNc" width="224" height="148"></p>
<p>Note that I changed the name of the .py file to <code>TestDebug2.py</code> and made the corresponding changes to all the python class names (e.g.  <code>ScriptedLoadableModuleTemplateLogic</code> became <code>TestDebug2Logic</code>).  So, you would need to add the path to <code>TestDebug2.py</code> in your “Additional Module Paths” in the application settings (or, maybe simpler, change the class names back to what you had earlier; they have to match the file name or the module will not load).</p>
<aside class="quote no-group" data-username="PhilipDavis" data-post="4" data-topic="21771">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/philipdavis/48/14142_2.png" class="avatar"> PhilipDavis:</div>
<blockquote>
<p>what I’d like to achieve is actually same as the ‘Display ROI’ checkbox in the volume rendering module</p>
</blockquote>
</aside>
<p>OK, so you want the ROI checkbox to just reflect the visibility state of the ROI associated with the chosen node?  So, if a user changes the input volume, the ROI checkbox should show whether or not the ROI for the new volume is already visible.  And then when the user toggles the checkbox, that should also toggle the ROI visibility for the current input volume?</p>

---

## Post #8 by @mikebind (2022-02-03 23:59 UTC)

<p>I updated the gist to behave like the toggle in the Volume Rendering module.  Same link: <a href="https://gist.github.com/mikebind/a3a4ee96076ab23d0e0339a47d02adfb">https://gist.github.com/mikebind/a3a4ee96076ab23d0e0339a47d02adfb</a></p>

---

## Post #9 by @PhilipDavis (2022-02-04 00:21 UTC)

<p>Hello <a class="mention" href="/u/mikebind">@mikebind</a> ,<br>
Thank you so much for your kindness and patience! Now everything working smoothly! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #10 by @Saima (2022-03-14 13:55 UTC)

<p>I am trying to add a checkbox to update the model display. How can I do this?</p>
<p>I am running into error</p>
<p>object has no attribute</p>

---
