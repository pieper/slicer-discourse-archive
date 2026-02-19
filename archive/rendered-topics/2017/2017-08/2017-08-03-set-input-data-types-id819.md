---
topic_id: 819
title: "Set Input Data Types"
date: 2017-08-03
url: https://discourse.slicer.org/t/819
---

# Set input data types

**Topic ID**: 819
**Date**: 2017-08-03
**URL**: https://discourse.slicer.org/t/set-input-data-types/819

---

## Post #1 by @Alba_Garcia_de_la_Ca (2017-08-03 19:38 UTC)

<p>Operating system: ubuntu 16.04 / iOS<br>
Slicer version: 4.6<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Good evening,</p>
<p>I guess my question is an easy or basic issue. I have been working with inputvolumes which are usually .nii extension so far. If I want to create the entry for the layout I am doing it this way:</p>
<pre><code>the volume selectors
self.inputFrame1 = qt.QFrame(self.tfgCollapsibleButton)
self.inputFrame1.setLayout(qt.QHBoxLayout())
self.tfgFormLayout.addWidget(self.inputFrame1)
self.inputSelector1 = qt.QLabel("Input Volume: ", self.inputFrame1)
self.inputFrame1.layout().addWidget(self.inputSelector1)
self.inputSelector1 = slicer.qMRMLNodeComboBox(self.inputFrame1)
self.inputSelector1.nodeTypes = ( ("vtkMRMLScalarVolumeNode"), "" )
self.inputSelector1.addEnabled = False
self.inputSelector1.removeEnabled = False
self.inputSelector1.setMRMLScene( slicer.mrmlScene )
self.inputFrame1.layout().addWidget(self.inputSelector1)
</code></pre>
<p>Now I need to set input values as integer, float…I have seen that fields in several modules and extensions (as in the image)<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d769068cce9ed2aff896961e4535a237748fbb5.png" alt="different_values" data-base62-sha1="1V6eeiDlI2YfzfWH0h2I7EZJOQJ" width="689" height="248"><br>
but I have not found the code, neither how to set that fields so after introducing the value I could work with it in my python code. Would you show me where could I find this information or how to set that layout fields?</p>
<p>Thanks in advance!<br>
Regards,<br>
Alba</p>

---

## Post #2 by @Fernando (2017-08-03 20:03 UTC)

<p>Hi Alba,</p>
<p>What do you need exactly? Have you taken a look at <a href="http://doc.qt.io/qt-4.8/qradiobutton.html" rel="nofollow noopener"><code>QRadioButton Class</code></a>?</p>

---

## Post #3 by @Alba_Garcia_de_la_Ca (2017-08-05 15:58 UTC)

<p>Hi Fernando,</p>
<p>I need an integer input (it can be a float) as this one:  <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68aea4a9f0113ded63e721268f6beb93b210eead.png" data-download-href="/uploads/short-url/eW3PlY3BaIhCMKcH3jDboFp7dA9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/68aea4a9f0113ded63e721268f6beb93b210eead_2_690x32.png" alt="image" data-base62-sha1="eW3PlY3BaIhCMKcH3jDboFp7dA9" width="690" height="32" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/68aea4a9f0113ded63e721268f6beb93b210eead_2_690x32.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68aea4a9f0113ded63e721268f6beb93b210eead.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68aea4a9f0113ded63e721268f6beb93b210eead.png 2x" data-dominant-color="F4F4F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">699×33 2.52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> so I can use this value in my code after user has introduced it. Is there any other Qt class which allow me to do that?<br>
Sorry I was not clear enough, but I am saving that information too because it can be helpful in the future : )</p>
<p>Thank you!<br>
Regards,<br>
Alba</p>

---

## Post #4 by @lassoan (2017-08-05 17:40 UTC)

<p>There are Qt and CTK widgets for this (spinbox or slider). Check out source existing Python modules in Slicer or read Qt and CTK documentation.</p>

---

## Post #5 by @Alba_Garcia_de_la_Ca (2017-08-08 20:17 UTC)

<p>Good evening,</p>
<p>Thanks! I am working with them : )</p>
<p>Regards!<br>
Alba</p>

---

## Post #6 by @Saima (2020-12-01 06:55 UTC)

<p>Hi Andras,<br>
Just a simple question but I am stuck and I am unable to identify whats wrong.</p>
<p>Why I am unable to load any volume in the input combo box.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac0de7cbcd296607df04765570dd860f74df327c.png" alt="image" data-base62-sha1="oy3URLM40Ux8MI9vs7YR11FTY0k" width="660" height="31"></p>
<p>I am using designers script for the pyhton module.</p>
<p>I did following in updateGUIFromParameterNode</p>
<pre><code class="lang-python">wasBlocked = self.ui.brainVolume.blockSignals(True)
self.ui.brainVolume.setCurrentNode(self._parameterNode.GetNodeReference("inputbrainVolume"))
self.ui.brainVolume.blockSignals(wasBlocked)

if self._parameterNode.GetNodeReference("inputbrainVolume"):
      self.ui.rasButton.toolTip = "Compute RAS Coordinates from MRI and convert electrode coordinates to RAS coordinates"
      self.ui.rasButton.enabled = True
    else:
      self.ui.rasButton.toolTip = "Select brain volume node"
      self.ui.rasButton.enabled = False
</code></pre>
<p>In <code>updateParameterNodeFromGUI(self, caller=None, event=None)</code> I did:</p>
<pre><code class="lang-python">    self._parameterNode.SetNodeReferenceID("inputbrainVolume", self.ui.brainVolume.currentNodeID)
</code></pre>
<p>in setup(self):</p>
<pre><code class="lang-python">self.ui.brainVolume.connect("currentNodeChanged(vtkMRMLNode*)", self.updateParameterNodeFromGUI)
</code></pre>
<p>What am I missing?</p>
<p>I also set the nodetype in QT designer view to vtkMRMLScalarVolumeNode</p>

---

## Post #7 by @lassoan (2020-12-01 07:01 UTC)

<p>You have forgot to set the MRML scene for the node selector widget. To fix this, in Qt designer’s Signal/Slot editor you can add a connection from the top-level qMRMLWidget’s <code>mrmlSceneChanged(vtkMRMLScene*)</code> signal to the node selector’s <code>setMRMLScene(vtkMRMLScene*)</code> slot.</p>

---

## Post #8 by @Saima (2020-12-01 07:45 UTC)

<p>Its fixed. Thanks a lot.</p>
<p>How to do in script this thing.</p>
<p>Regards,<br>
Saima Safdar</p>

---
