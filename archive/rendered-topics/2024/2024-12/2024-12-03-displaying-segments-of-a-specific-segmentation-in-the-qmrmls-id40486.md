---
topic_id: 40486
title: "Displaying Segments Of A Specific Segmentation In The Qmrmls"
date: 2024-12-03
url: https://discourse.slicer.org/t/40486
---

# Displaying Segments of a Specific Segmentation in the qMRMLSegmentsTableView

**Topic ID**: 40486
**Date**: 2024-12-03
**URL**: https://discourse.slicer.org/t/displaying-segments-of-a-specific-segmentation-in-the-qmrmlsegmentstableview/40486

---

## Post #1 by @shahrokh (2024-12-03 07:36 UTC)

<p>Hello Dear Developers and Users,</p>
<p>I used the answers given to a question titled <strong><a href="https://discourse.slicer.org/t/input-segments-in-new-module/5064">Input segments in new module</a></strong> to help me write the following lines of code.</p>
<pre><code class="lang-auto">import os
import unittest
from __main__ import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *

#
# SegmentationSelector
#

class SegmentationSelector(ScriptedLoadableModule):
  
  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "SegmentationSelector" # TODO make this more human readable by adding spaces
    self.parent.categories = ["Examples"]
    self.parent.dependencies = []
    self.parent.contributors = ["John Doe (AnyWare Corp.)"] # replace with "Firstname Lastname (Organization)"

#
# SegmentationSelectorWidget
#

class SegmentationSelectorWidget(ScriptedLoadableModuleWidget):

  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)
    # Instantiate and connect widgets ...

    #
    # Parameters Area
    #
    parametersCollapsibleButton = ctk.ctkCollapsibleButton()
    parametersCollapsibleButton.text = "Parameters"
    self.layout.addWidget(parametersCollapsibleButton)

    # Layout within the dummy collapsible button
    parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)

    ### Start (Segment node selection)
    # Create a qMRMLSegmentSelectorWidget for selecting the Segmentation node
    self.inputSelector1 = slicer.qMRMLSegmentSelectorWidget()
    self.inputSelector1.setMRMLScene(slicer.mrmlScene)
    self.inputSelector1.setToolTip("Pick the input to the algorithm.")
    parametersFormLayout.addRow("Segmentation: ", self.inputSelector1)
    
    # Segment table view setup
    self.inputSelector2 = slicer.qMRMLSegmentsTableView()
    self.inputSelector2.setMRMLScene(slicer.mrmlScene)
    self.inputSelector2.setToolTip("Pick the segments to view.")
    # Add the table view to the layout
    parametersFormLayout.addRow("Segments Table: ", self.inputSelector2)    
    self.inputSelector2.show()
</code></pre>
<p>As you can see in the image below,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b4ee729d2aeff683b65b235ec4fae0617d9e3f1.jpeg" data-download-href="/uploads/short-url/6b7zXRjstIt8lV0RPPCtvjziwRr.jpeg?dl=1" title="Screenshot 2024-12-03 11:01:18" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b4ee729d2aeff683b65b235ec4fae0617d9e3f1_2_690x388.jpeg" alt="Screenshot 2024-12-03 11:01:18" data-base62-sha1="6b7zXRjstIt8lV0RPPCtvjziwRr" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b4ee729d2aeff683b65b235ec4fae0617d9e3f1_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b4ee729d2aeff683b65b235ec4fae0617d9e3f1_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b4ee729d2aeff683b65b235ec4fae0617d9e3f1_2_1380x776.jpeg 2x" data-dominant-color="A3A49B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-12-03 11:01:18</span><span class="informations">1920×1080 328 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>after selecting my desired Segmentation, in the <em>Segment</em> list I can see the list of Segments that are in the Segmentation node, but the <em>Segments Table</em> is empty.<br>
How can I create this connection? It seems like there should be a connection between the <strong>qMRMLSegmentSelectorWidget</strong> and <strong>qMRMLSegmentsTableView</strong>.</p>
<p>Please guide me.<br>
Best regards.<br>
Shahrokh</p>

---

## Post #2 by @shahrokh (2024-12-03 08:32 UTC)

<p>Sorry… my problem is solved. The lines I added are these:</p>
<pre><code class="lang-auto">    # Segment table view setup
...
    self.inputSelector2.setSegmentationNode(self.inputSelector1.currentNode())
    self.inputSelector2.show()
    ...
</code></pre>
<p>As seen in the image below, I can observe the list of Segments in the Segmentation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05dc147a236a99c2978adb2c25bf55c3dd08335a.jpeg" data-download-href="/uploads/short-url/PPUcN3hCTbhqLcxVLfU8rjoekW.jpeg?dl=1" title="Screenshot from 2024-12-03 11-58-32" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05dc147a236a99c2978adb2c25bf55c3dd08335a_2_690x388.jpeg" alt="Screenshot from 2024-12-03 11-58-32" data-base62-sha1="PPUcN3hCTbhqLcxVLfU8rjoekW" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05dc147a236a99c2978adb2c25bf55c3dd08335a_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05dc147a236a99c2978adb2c25bf55c3dd08335a_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05dc147a236a99c2978adb2c25bf55c3dd08335a_2_1380x776.jpeg 2x" data-dominant-color="A1A2A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-12-03 11-58-32</span><span class="informations">1920×1080 318 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Next, I want to select one of these Segments from the table to perform some further processing on it.</p>
<p>Shahrokh</p>

---

## Post #3 by @shahrokh (2024-12-03 12:42 UTC)

<p>As shown in the image above, I can now see the table containing the Segments in a Segmentation within a module called <em>SegmentationSelector</em>.</p>
<p>Next, I was able to select one of the Segments from the visible table and retrieve its ID using the <code>selectedSegmentIDs</code> function for further processing. I was able to accomplish this in the 3D Slicer Python Interactor with the following commands.</p>
<pre><code class="lang-auto">seg=slicer.qMRMLSegmentSelectorWidget()
seg.setMRMLScene(slicer.mrmlScene)
seg.setToolTip("Pick the input to the algorithm.")
table=slicer.qMRMLSegmentsTableView()
table.setMRMLScene(slicer.mrmlScene)
table.setToolTip("Pick the segments to view.")
table.setSegmentationNode(seg.currentNode())
table.show()
table.selectedSegmentIDs()
</code></pre>
<p>Screenshot of the result of the above commands:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8146a87c5dec66f4910d120f99907453943bc428.png" data-download-href="/uploads/short-url/irCYDHKh07RlsqeaLsJVO8pS0Gs.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8146a87c5dec66f4910d120f99907453943bc428_2_690x273.png" alt="1" data-base62-sha1="irCYDHKh07RlsqeaLsJVO8pS0Gs" width="690" height="273" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8146a87c5dec66f4910d120f99907453943bc428_2_690x273.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8146a87c5dec66f4910d120f99907453943bc428_2_1035x409.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8146a87c5dec66f4910d120f99907453943bc428_2_1380x546.png 2x" data-dominant-color="C6C7C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1843×730 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now, I would like to have the same functionality in my module, <em>SegmentationSelector</em>. In other words, as shown in the image below, I want to select one of the segments from the Segments Table. Can you guide me on how to do this?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2cffc012c9a027cd13da8d11f3a21b41a87bbac.jpeg" data-download-href="/uploads/short-url/pvQAQhCb0egWdIguFhAm44D3syE.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2cffc012c9a027cd13da8d11f3a21b41a87bbac_2_690x388.jpeg" alt="2" data-base62-sha1="pvQAQhCb0egWdIguFhAm44D3syE" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2cffc012c9a027cd13da8d11f3a21b41a87bbac_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2cffc012c9a027cd13da8d11f3a21b41a87bbac_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2cffc012c9a027cd13da8d11f3a21b41a87bbac_2_1380x776.jpeg 2x" data-dominant-color="63645F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1920×1080 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please guide me.<br>
Best regards.<br>
Shahrokh.</p>

---

## Post #4 by @shahrokh (2024-12-03 13:23 UTC)

<p>I saw something similar to what I want in the <strong>Segment Comparison</strong> module. Perhaps there is no need for <code>qMRMLSegmentsTableView</code>. But how can I be sure that when selecting one of the segments from the <em>Segment Table</em>, that segment is actually selected? I modified my module’s code as follows:</p>
<pre><code class="lang-auto">    ### Start (Segment node selection)
    # Create a qMRMLSegmentSelectorWidget for selecting the Segmentation node
    self.inputSelector1 = slicer.qMRMLSegmentSelectorWidget()
    #self.inputSelector1.nodeTypes = (("vtkSegmentation"), "")
    #self.inputSelector1.selectNodeUponCreation = True
    #self.inputSelector1.addEnabled = False
    #self.inputSelector1.removeEnabled = False
    #self.inputSelector1.noneEnabled = False
    #self.inputSelector1.showHidden = False
    #self.inputSelector1.showChildNodeTypes = False
    self.inputSelector1.setMRMLScene(slicer.mrmlScene)
    self.inputSelector1.setToolTip("Pick the input to the algorithm.")
    parametersFormLayout.addRow("Segmentation: ", self.inputSelector1)
    # Print sement selected
    self.inputSelector1.selectedSegmentIDs()
    print("Segment selected: ", self.inputSelector1.selectedSegmentIDs())
</code></pre>
<p>However, as shown in the following figure, the output of the print statement is empty.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/179be26ae7235e52772132123db0ab2b9a799b0b.png" data-download-href="/uploads/short-url/3mQXGCwzCKKSA7cQKHKTs7lxfwD.png?dl=1" title="4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/179be26ae7235e52772132123db0ab2b9a799b0b_2_690x293.png" alt="4" data-base62-sha1="3mQXGCwzCKKSA7cQKHKTs7lxfwD" width="690" height="293" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/179be26ae7235e52772132123db0ab2b9a799b0b_2_690x293.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/179be26ae7235e52772132123db0ab2b9a799b0b_2_1035x439.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/179be26ae7235e52772132123db0ab2b9a799b0b_2_1380x586.png 2x" data-dominant-color="D1D1D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4</span><span class="informations">1843×783 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I expected the output of the print statement to be PTV1. In other words, when I select a segment from the list, for example PTV1, I want to use its ID for subsequent processing in the next widgets.<br>
Please guide me.<br>
Best regards.<br>
Shahrokh</p>

---

## Post #5 by @shahrokh (2024-12-04 14:50 UTC)

<p>I must apologize for asking my question again. I tried to select one of the <em>Segments</em> available in a node of the type <em>Segmentation</em>. It is like the <strong>Segment Comparison</strong> module, but unfortunately, I couldn’t succeed. The code I have written so far includes the following lines:</p>
<pre><code class="lang-auto">import os
import unittest
from __main__ import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging

#
# SegmentationSelector
#

class SegmentationSelector(ScriptedLoadableModule):
  
  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "SegmentationSelector" # TODO make this more human readable by adding spaces
    self.parent.categories = ["Examples"]
    self.parent.dependencies = []
    self.parent.contributors = ["John Doe (AnyWare Corp.)"] # replace with "Firstname Lastname (Organization)"

#
# SegmentationSelectorWidget
#

class SegmentationSelectorWidget(ScriptedLoadableModuleWidget):

  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)
    # Instantiate and connect widgets ...

    #
    # Parameters Area
    #
    parametersCollapsibleButton = ctk.ctkCollapsibleButton()
    parametersCollapsibleButton.text = "Parameters"
    self.layout.addWidget(parametersCollapsibleButton)

    # Layout within the dummy collapsible button
    parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)

    #
    # input volume selector
    #
    self.inputSelector0 = slicer.qMRMLNodeComboBox()
    self.inputSelector0.nodeTypes = ["vtkMRMLScalarVolumeNode"]
    self.inputSelector0.selectNodeUponCreation = True
    self.inputSelector0.addEnabled = False
    self.inputSelector0.removeEnabled = False
    self.inputSelector0.noneEnabled = False
    self.inputSelector0.showHidden = False
    self.inputSelector0.showChildNodeTypes = False
    self.inputSelector0.setMRMLScene( slicer.mrmlScene )
    self.inputSelector0.setToolTip( "Pick the input to the algorithm." )
    parametersFormLayout.addRow("Input Volume: ", self.inputSelector0)

    #
    # Select Segment node
    #
    self.inputSelector1 = slicer.qMRMLSegmentSelectorWidget()
    self.inputSelector1.setMRMLScene(slicer.mrmlScene)
    self.inputSelector1.setToolTip("Pick the input to the algorithm.")
    parametersFormLayout.addRow("Segmentation: ", self.inputSelector1)
    self.inputSelector1.selectedSegmentIDs()
    
    #
    # Apply Button
    #
    self.applyButton = qt.QPushButton("Apply")
    self.applyButton.toolTip = "Run the algorithm."
    self.applyButton.enabled = True
    parametersFormLayout.addRow(self.applyButton)

    # connections
    self.applyButton.connect('clicked(bool)', self.onApplyButton)
    self.inputSelector1.connect("currentNodeChanged(vtkMRMLNode*)", self.onSelect)

    # Refresh Apply button state
    self.onSelect()

  def cleanup(self):
    pass

  def onSelect(self):
    self.applyButton.enabled = self.inputSelector1.currentNode()

  def onApplyButton(self):
    logic = SegmentationSelectorLogic()
    logic.run(self.inputSelector1.currentNode())

#
# SegmentationSelectorLogic
#

class SegmentationSelectorLogic(ScriptedLoadableModuleLogic):
  def run(self, inputVolume):
    """
    Run the actual algorithm
    """
    print("Segment selected: ", type(inputVolume))
    return True

</code></pre>
<p>I referred to the <a href="https://apidocs.slicer.org/master/classqMRMLSegmentSelectorWidget.html" rel="noopener nofollow ugc">Slicer: qMRMLSegmentSelectorWidget Class Reference</a>, but unfortunately, I couldn’t find a method that allows me to connect a segment selected from the combobox of the <strong>qMRMLSegmentSelectorWidget</strong> to the <strong>Apply</strong> pushbutton. Also, I couldn’t find the Python code for the <strong>Segment Comparison</strong> module, which I could use as a base for my code. I also read the PDF file titled <a href="https://github.com/Slicer/SlicerProgrammingTutorial/releases/download/Slicer-5.6/SlicerProgrammingTutorial.pdf" rel="noopener nofollow ugc">Programming tutorial for 3D Slicer</a>, which was very useful, and I was able to implement the code up to this point. If possible, could you guide me on how I can complete this code?</p>
<p>Please guide me.<br>
Best regards.<br>
Shahrokh</p>

---

## Post #6 by @pieper (2024-12-04 15:03 UTC)

<p>It’s good that you keep working on this and I’m sure you will get it sorted out.</p>
<p>Regarding <code>qMRMLSegmentSelectorWidget</code>, here’s a snippet showing how it’s supposed to work.  If it’s not working this way in your module, then experimenting in the python console like this can help.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; w = slicer.qMRMLSegmentSelectorWidget()
&gt;&gt;&gt; w.setMRMLScene(slicer.mrmlScene)
&gt;&gt;&gt; w.show()
&gt;&gt;&gt; w.currentNode()
&lt;MRMLCorePython.vtkMRMLSegmentationNode(0x7fb7b2b5c660) at 0x1b0dccb80&gt;
&gt;&gt;&gt;w.currentSegmentID()
'Segment_1_3'
</code></pre>
<p>If you run into behavior that doesn’t make sense to you, post small, easy to replicate snippets like this so it’s easy for people to answer without reading through all your code.</p>

---

## Post #7 by @shahrokh (2024-12-07 08:05 UTC)

<p>Thank you very much for your suggestion. I will follow the suggestion you mentioned and post small, easy-to-replicate snippets like this to make it easier to answer without having to read through all of my code.</p>
<p>Thank you so much for your guidance. I realized that my mistake was in the <code>onSelect</code> function. The return value of this function should be of type <code>vtkMRMLSegmentationNode</code>.</p>
<p>Based on this, the corrected code will be as follows:</p>
<blockquote>
<p>…<br>
def onSelect(self):<br>
self.inputSelector1.currentNode()<br>
print("Output onSelect fun: ", type(self.inputSelector1.currentNode()))<br>
…</p>
</blockquote>
<p>By selecting any of the segments from the ComboBox <strong>Segment</strong> list and then clicking <strong>Apply</strong>, I can see the result in the Python Interactor.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a780c1d55f8dc3f02af7208bf31bfa5e99e37e7.png" data-download-href="/uploads/short-url/63HfKe6Xqwh47UK53L7Wt8y2Ikf.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a780c1d55f8dc3f02af7208bf31bfa5e99e37e7_2_690x388.png" alt="1" data-base62-sha1="63HfKe6Xqwh47UK53L7Wt8y2Ikf" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a780c1d55f8dc3f02af7208bf31bfa5e99e37e7_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a780c1d55f8dc3f02af7208bf31bfa5e99e37e7_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a780c1d55f8dc3f02af7208bf31bfa5e99e37e7_2_1380x776.png 2x" data-dominant-color="BCBCB9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1920×1080 262 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>‌Best regards.<br>
Shahrokh</p>

---
