---
topic_id: 40369
title: "Understanding Ui Editing And Python File Generation In 3Dsli"
date: 2024-11-25
url: https://discourse.slicer.org/t/40369
---

# Understanding UI Editing and Python File Generation in 3DSlicer with Qt Designer

**Topic ID**: 40369
**Date**: 2024-11-25
**URL**: https://discourse.slicer.org/t/understanding-ui-editing-and-python-file-generation-in-3dslicer-with-qt-designer/40369

---

## Post #1 by @shahrokh (2024-11-25 16:45 UTC)

<p>Hello Dear Developers and Users,</p>
<p>In the implementation of the module, I am using the <strong>Extension Wizard</strong> module. This module utilizes a fixed template, the result of which ultimately creates a <strong>.ui</strong> file and its corresponding Python file. For example, let’s assume that the name of this module is <em>developModuleTry01</em>. After switching to the <em>developModuleTry01</em> module, I can run the <strong>Qt Designer</strong>  within 3DSlicer and add or remove the module’s widgets. After saving and exiting <strong>Qt Designer</strong>, I click on <strong>Reload and Test</strong> to apply the changes. However, I noticed that the Python file does not change when I edit the UI file. I also checked other options of the <em>developModuleTry01</em> module, including <strong>Reload</strong> and <strong>Restart Slicer</strong>, but I observed that the Python file still doesn’t change when I edit the module’s UI.</p>
<p>Is it a correct and reasonable expectation that the Python file should also change when I edit the UI through <strong>Qt Designer</strong>?</p>
<p>I know that, in general, to generate Python code from a UI file created with <strong>Qt Designer</strong>, tools like or <strong>pyuic</strong> or <strong>pyuic5</strong> should be used. Similarly, in 3DSlicer, a tool similar to <strong>pyuic5</strong> should be used, and it is expected that when using <strong>Edit UI</strong> and clicking on <strong>Reload and Test</strong>, two things should happen:<br>
one, the graphical environment of the module is reloaded, and<br>
two, a tool like <strong>pyuic5</strong> is executed to regenerate the Python file.</p>
<p>Is my assumption incorrect?<br>
Please guide me.<br>
Best regards.<br>
Shahrokh</p>

---

## Post #2 by @pieper (2024-11-25 19:44 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="40369">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>I can run the <strong>Qt Designer</strong> within 3DSlicer and add or remove the module’s widgets. After saving and exiting <strong>Qt Designer</strong>, I click on <strong>Reload and Test</strong> to apply the changes. However, I noticed that the Python file does not change when I edit the UI file.</p>
</blockquote>
</aside>
<p>This is expected.  The UI file is an xml file in the Resources/UI subdirectory that is used to build the widgets for the module GUI.  The default python module script from the template reads this file with a line like <code>uiWidget = slicer.util.loadUI(self.resourcePath("UI&lt;module&gt;.ui"))</code> so the python code doesn’t need to change with you edit the ui file.</p>

---

## Post #3 by @shahrokh (2024-11-26 05:15 UTC)

<p>Thank you very much for your response, but perhaps I should explain the reason for asking this question so that, if possible, you may guide me further.</p>
<p>Perhaps you have already read the question I raised in my previous message with the title of <a href="https://discourse.slicer.org/t/implementing-widgets-for-selecting-nodes-of-type-segment-and-beam/40359">Implementing Widgets for Selecting Nodes of Type Segment and Beam</a>. In general, I want to familiarize myself with the process of developing modules in 3DSlicer. Therefore, I want to learn how I can develop the functionality of widgets so that I can select specific nodes from the Data module and process them. For example, with one widget, I should be able to select only nodes of type <strong>Segment</strong>, with another widget, only nodes of type <strong>Model</strong>, and with yet another widget, only nodes of type <strong>Beam</strong>.</p>
<p>Based on this, the roadmap I set for myself was to first create a UI that contains a widget of type <strong>qMRMLSegmentSelectorWidget</strong> to select only nodes of type <strong>Segment</strong>. The reason I chose this node is that I found out this widget is part of the <strong>Slicer [MRML Widgets]</strong> in Widget Box of Qt Designer, and it seems to have been specifically added to Qt Designer by the 3D Slicer development team for module implementation. (At this point, I also had a problem, as I couldn’t find other widgets in the list that, based on their names, I could guess might be useful for selecting nodes of specific types.)</p>
<p>By selecting this particular widget, I expected that the related Python file would be much shorter so I could analyze and understand its components, and ultimately develop its function so that it would select only nodes of type <strong>Segment</strong> from the Data module. As I mentioned in my message, the Python file that was generated was default and contains 403 lines.</p>
<p>Best regards.<br>
Shahrokh</p>

---

## Post #4 by @pieper (2024-11-26 20:01 UTC)

<p>It sounds like what you are looking for is a <a href="https://apidocs.slicer.org/master/classqMRMLNodeComboBox.html">qMRMLNodeComboBox</a>.  You can use the <code>nodeTypes</code> property and other api options to control what gets displayed.  These are used all over Slicer, so looking at the code will give you ideas how to use it.</p>

---

## Post #5 by @shahrokh (2024-11-27 08:23 UTC)

<p>Thank you very much for the guidance you provided. I will definitely implement the point you mentioned in my module.</p>
<p>The plans I have in mind are to implement modules with names such as VolumeSelector, ModelSelector, BeamSelector, etc., separately, in order to expand my experience in module development.</p>
<p>However, if you pay attention to the following figure, you will notice that the parent class used is of type <strong>qMRMLWidget</strong>. Interestingly, the <strong>qMRMLSegmentSelectorWidget</strong> widget does not have the <strong>nodeType</strong> property.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79341869bfc1442f52602dbb904bca27fa07b245.png" data-download-href="/uploads/short-url/hido2pZ4r3dXg48MXlIRqbTi2YR.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79341869bfc1442f52602dbb904bca27fa07b245_2_690x388.png" alt="1" data-base62-sha1="hido2pZ4r3dXg48MXlIRqbTi2YR" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79341869bfc1442f52602dbb904bca27fa07b245_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79341869bfc1442f52602dbb904bca27fa07b245_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79341869bfc1442f52602dbb904bca27fa07b245_2_1380x776.png 2x" data-dominant-color="CFD1D1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1920×1080 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But as mentioned you, if a widget of type <strong>qMRMLNodeComboBox</strong> is selected, it does have the <strong>nodeType</strong> property, and I think I should set it to <strong>vtkMRMLScalarVolumeNode</strong> or <strong>vtkMRMLSegmentationNode</strong> in python code.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43251733a8241963b01c9fda03cdd9b40ed582b3.png" data-download-href="/uploads/short-url/9zZsk3ZODUxoRCIqWnDrK1rhbXR.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43251733a8241963b01c9fda03cdd9b40ed582b3_2_690x388.png" alt="2" data-base62-sha1="9zZsk3ZODUxoRCIqWnDrK1rhbXR" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43251733a8241963b01c9fda03cdd9b40ed582b3_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43251733a8241963b01c9fda03cdd9b40ed582b3_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43251733a8241963b01c9fda03cdd9b40ed582b3_2_1380x776.png 2x" data-dominant-color="CCCFCE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1920×1080 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best regards.<br>
Shahrokh</p>

---

## Post #6 by @shahrokh (2024-11-30 07:44 UTC)

<p>Thank you very much for the helpful guidance regarding the property <code>nodeTypes</code>. Based on your response and the answer that Csaba Pinter provided to the question raised by Thomas Dutrey titled <a href="https://discourse.slicer.org/t/input-segments-in-new-module/5064">Input segments in new module</a>, I was able to implement two separate modules named <strong>VolumeSelector</strong>, <strong>SegmentSelector</strong> and <strong>RTBeamSelector</strong>.</p>
<p>As mentioned in the response, the key lines in the corresponding Python code files, <strong>VolumeSelector.py</strong>, <strong>SegmentSelector.py</strong> and <strong>RTBeamSelector.py</strong>, are the following lines, which determine the type of node in the Selector:</p>
<p>In the <strong>VolumeSelector.py</strong> file:</p>
<pre><code class="lang-auto">    # input volume selector
    #
    self.inputSelector = slicer.qMRMLNodeComboBox()
    self.inputSelector.nodeTypes = ( ("vtkMRMLScalarVolumeNode"), "" )
    #self.inputSelector.addAttribute( "vtkMRMLScalarVolumeNode", "LabelMap", 0 )
    self.inputSelector.selectNodeUponCreation = True
    self.inputSelector.addEnabled = False
    self.inputSelector.removeEnabled = False
    self.inputSelector.noneEnabled = False
    self.inputSelector.showHidden = False
    self.inputSelector.showChildNodeTypes = False
    self.inputSelector.setMRMLScene( slicer.mrmlScene )
    self.inputSelector.setToolTip( "Pick the input to the algorithm." )
    parametersFormLayout.addRow("Input Volume: ", self.inputSelector)
</code></pre>
<p>In the <strong>SegmentSelector.py</strong> file:</p>
<pre><code class="lang-auto">    # input segment selector
    #
    self.inputSelector = slicer.qMRMLNodeComboBox()
    self.inputSelector.nodeTypes = ( ("vtkMRMLSegmentationNode"), "" )
    #self.inputSelector.addAttribute( "vtkMRMLSegmentationNode", "Segment", 0 )
    self.inputSelector.selectNodeUponCreation = True
    self.inputSelector.addEnabled = False
    self.inputSelector.removeEnabled = False
    self.inputSelector.noneEnabled = False
    self.inputSelector.showHidden = False
    self.inputSelector.showChildNodeTypes = False
    self.inputSelector.setMRMLScene( slicer.mrmlScene )
    self.inputSelector.setToolTip( "Pick the input to the algorithm." )
    parametersFormLayout.addRow("Segment: ", self.inputSelector)
</code></pre>
<p>In the <strong>RTBeamSelector.py</strong> file:</p>
<pre><code class="lang-auto">    # input RT beam selector
    #
    self.inputSelector = slicer.qMRMLNodeComboBox()
    self.inputSelector.nodeTypes = ( ("vtkMRMLRTBeamNode"), "" )
    #self.inputSelector.addAttribute( "vtkMRMLRTBeamNode", "RTBeam", 0 )
    self.inputSelector.selectNodeUponCreation = True
    self.inputSelector.addEnabled = False
    self.inputSelector.removeEnabled = False
    self.inputSelector.noneEnabled = False
    self.inputSelector.showHidden = False
    self.inputSelector.showChildNodeTypes = False
    self.inputSelector.setMRMLScene( slicer.mrmlScene )
    self.inputSelector.setToolTip( "Pick the input to the algorithm." )
    parametersFormLayout.addRow("Beam: ", self.inputSelector)
</code></pre>
<p>Best regards.<br>
Shahrokh</p>

---
