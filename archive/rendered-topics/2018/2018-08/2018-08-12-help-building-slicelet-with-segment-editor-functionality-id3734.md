---
topic_id: 3734
title: "Help Building Slicelet With Segment Editor Functionality"
date: 2018-08-12
url: https://discourse.slicer.org/t/3734
---

# Help Building Slicelet with Segment Editor Functionality

**Topic ID**: 3734
**Date**: 2018-08-12
**URL**: https://discourse.slicer.org/t/help-building-slicelet-with-segment-editor-functionality/3734

---

## Post #1 by @bsmarine (2018-08-12 00:37 UTC)

<p>Hi,</p>
<p>I’m working with a group of physicians and graduate students to develop Slicelets as part of a computer vision initiative at my hospital. I’m a long time Slicer user and fan, and am looking for guidance in constructing parts or all of the Segment Editor module within a custom Slicelet.</p>
<p>I’ve been studying the Slicelet Documentation page, and looking for a .py file similar to the Editor.py file to try and build a Slicelet with Segment Editor features within it. But I’m not having any luck finding what seems like the correct files. Does anyone have any suggestions on how to approach this? Perhaps there’s an existing Slicelet that incorporates some or all of the Segment Editor that someone may be willing to share?</p>
<p>Thanks for your help!</p>
<p>Best,</p>
<p>Brett</p>

---

## Post #2 by @lassoan (2018-08-12 00:40 UTC)

<p>Segment Editor module serves as an example how you can use the Segment Editor widget in a scripted module by writing only a few ten lines of code. Copy and paste source code of this module in your slicelet and modify as needed.</p>

---

## Post #3 by @bsmarine (2018-08-12 03:49 UTC)

<p>Sounds very straightforward to implement the Segment Editor widget into a Slicelet.</p>
<p>Is there somewhere specific in Slicer’s source code you recommend I look?</p>

---

## Post #4 by @lassoan (2018-08-12 06:59 UTC)

<p>Segment Editor module source code is available here: <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentEditor/SegmentEditor.py">https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentEditor/SegmentEditor.py</a></p>

---

## Post #5 by @bsmarine (2018-08-12 15:00 UTC)

<p>Awesome! Was able to launch into a Slicelet (along with the impressive additional of features available through your extension). This is really spectacular.</p>
<p>However, one thing I’m missing and struggling to figure out is how to load viewer windows for interacting with images. Currently all I have is the module itself and add data/add scene buttons.</p>
<p>I tried adding the code below as described in Slicelet documentation, but was unsure where to put it. Everywhere I tried (under all the different <strong>init</strong> methods within my Slicelet and also in the .slicerrc.py that’s launched at on start-up) did not end up launching viewers. Any thoughts on what I might be missing?</p>
<p>Thank you!</p>
<pre><code>mainWidget = qt.QWidget()
mainWidget.objectName = "qSlicerAppMainWindow"
vlayout = qt.QVBoxLayout()
mainWidget.setLayout(vlayout)
layoutWidget = slicer.qMRMLLayoutWidget()
layoutManager = slicer.qSlicerLayoutManager()
layoutManager.setMRMLScene(slicer.mrmlScene)
layoutManager.setScriptedDisplayableManagerDirectory(slicer.app.slicerHome + "/bin/Python/mrmlDisplayableManager")
layoutWidget.setLayoutManager(layoutManager)
slicer.app.setLayoutManager(layoutManager)
layoutWidget.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView)
vlayout.addWidget(layoutWidget)</code></pre>

---

## Post #6 by @pieper (2018-08-13 12:42 UTC)

<p>A segment editor Slicelet would be a generally useful tool - <a class="mention" href="/u/bsmarine">@bsmarine</a> maybe you could start a git repository for the project and put your full script there so others could help you debug?</p>

---

## Post #7 by @cpinter (2018-08-13 13:34 UTC)

<p>You can gut this slicelet to only include the panel with the layout selector and the viewers, then add the Segment Editor widget into the panel<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/GelDosimetryAnalysis/blob/master/GelDosimetryAnalysis/GelDosimetryAnalysis.py" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/GelDosimetryAnalysis/blob/master/GelDosimetryAnalysis/GelDosimetryAnalysis.py" target="_blank">SlicerRt/GelDosimetryAnalysis/blob/master/GelDosimetryAnalysis/GelDosimetryAnalysis.py</a></h4>
<pre><code class="lang-py">import os
import unittest
import numpy
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
import GelDosimetryAnalysisLogic
import DataProbeLib
from DICOMLib import DICOMUtils
from slicer.util import VTKObservationMixin

#
# Gel dosimetry analysis slicelet
#
# Streamlined workflow end-user application based on 3D Slicer and SlicerRT to support
# 3D gel-based radiation dosimetry.
#
# The all-caps terms correspond to data objects in the gel dosimetry data flow diagram
# https://subversion.assembla.com/svn/slicerrt/trunk/GelDosimetryAnalysis/doc/GelDosimetryAnalysis_DataFlow.png
#
</code></pre>

  This file has been truncated. <a href="https://github.com/SlicerRt/GelDosimetryAnalysis/blob/master/GelDosimetryAnalysis/GelDosimetryAnalysis.py" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #8 by @bsmarine (2018-08-15 13:52 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> thank you so much for sharing! This code is extensive, easy to follow and a great learning resource on how to add useful Slicelet functionality. Currently going through it with a colleague and will let you know how it works out.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> I just uploaded to a git repo, specifically, the SegmentEditor.py code <a href="https://github.com/bsmarine/SinaiSlicelets/blob/master/SegmentEditor.py" rel="nofollow noopener">here</a>.</p>
<p>Struggling to understand how to build viewers and module widgets in the same layout. I’m a novice with computer programming and still trying to wrap my head around how parent and child classes syntax work, which seems essential in building Slicelets.</p>
<p>Specifically, I’m trying to launch a SegmentEditor module within a viewer but may be making many mistakes around line 212 to 229. Any suggestions would be greatly appreciated!</p>

---

## Post #9 by @bsmarine (2018-08-28 23:49 UTC)

<p>Hi All,</p>
<p>Can anyone provide suggestions or advice on how to get SegmentEditor to work as a Slicelet using <a href="https://github.com/bsmarine/SinaiSlicelets/blob/master/SegmentEditor.py" rel="noopener nofollow ugc">the code I have loaded up on github</a>?</p>
<p>Specifically, I think that I’m not calling the viewer layout correctly in the Slicelet class (line 198) before it’s passed to the SegmentEditorSlicelet class (line 244).</p>
<blockquote>
<p>/Applications/Slicer.app/Contents/MacOS/Slicer --no-main-window --python-code SegmentEditor.py</p>
</blockquote>
<blockquote>
<p>Loading Slicer RC file [/Users/brettmarinelli/.slicerrc.py]<br>
Traceback (most recent call last):<br>
File “&lt;string&gt;”, line 1, in &lt;module&gt;<br>
NameError: name ‘SegmentEditor’ is not defined</p>
</blockquote>
<p>Any help is greatly appreciated!</p>

---

## Post #10 by @lassoan (2018-08-29 04:01 UTC)

<p>There are a couple of small issues:</p>
<ul>
<li>Starting the slicelet: if you want to specify a file name then you need to use <code>--python-script</code> argument. See details <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets">here</a>. For example, this worked for me: <code>"c:\Program Files\Slicer 4.9.0-2018-08-25\Slicer.exe" --python-script c:\\D\\SinaiSlicelets\\SegmentEditor.py</code>
</li>
<li>SegmentEditor module name is already taken by a Slicer core module. Choose a different one.</li>
<li>There is a syntax error in your code at line 225. To fix it, replace <code>self.parent.vlayout</code> by <code>self.parent.layout()</code>.</li>
</ul>

---

## Post #11 by @bsmarine (2018-11-05 14:14 UTC)

<p>Hi Andras, thanks for your guidance on this. I was able to pull into a Slicelet successfully.</p>
<p>Had to put this project down for a bit and am starting it back up. While the SegmentEditor shows up in my Slicelet, it does not seem to recognize any loaded volumes. Is there a way to generally establish connection with SegmentEditor and any present volumeNodes?</p>
<p>I have posted code <a href="https://github.com/bsmarine/SinaiSlicelets/blob/master/seg_widget.py" rel="nofollow noopener">here</a> on GitHub. Lines 10, 278 and 937 refer to SegmentEditor relevant portions.</p>
<p>Thank you for your help!</p>
<p>Best,</p>
<p>Brett</p>

---

## Post #12 by @lassoan (2018-11-05 17:25 UTC)

<p>You create a segment editor widget <a href="https://github.com/bsmarine/SinaiSlicelets/blob/master/seg_widget.py#L286">here</a> but then you would need to call <code>setMRMLScene</code> and <code>setMRMLSegmentEditorNode</code> to be able to use the widget. To make your widget truly and independent widget, do not reuse the same singleton node as Slicer’s built-in segment editor module: change <code>"SegmentEditor"</code> singleton tag to something like <code>"SinaiSegmentEditor"</code>.</p>

---

## Post #13 by @bsmarine (2018-11-06 01:50 UTC)

<p>Hi Andras,</p>
<p>I’ve done as you instructed here and sure enough I can now select new Segmentations and set Master Volume!</p>
<p>But a soon as I hit paint brush or eraser the Slicelet closes :\</p>
<p>I cleaned up the <a href="https://github.com/bsmarine/SinaiSlicelets/blob/master/seg_widget.py" rel="nofollow noopener">code on git hub</a>. Relevant lines are at 14, 84 and 97. Do you happen to see what I may have done incorrectly?</p>
<p>Unsure if it’s related, but I receive this error message below on start-up now.</p>
<p>QObject::connect: Cannot connect (null)::layoutChanged(int) to qMRMLSegmentEditorWidget::onLayoutChanged(int)</p>

---

## Post #14 by @lassoan (2018-11-06 02:15 UTC)

<p>Sorry, but I cannot even figure out what would you expect to happen. Please either use the skeleton generated by Extension Wizard (keep all the folders and files that the wizard generates) or follow working examples more closely. Only put a single .py files in the module’s folder (additional Python files are only allowed in subfolders).</p>

---

## Post #15 by @bsmarine (2018-11-06 13:46 UTC)

<p>Hi Andras,</p>
<p>The expectation is to have a SegmentEditor within a Slicelet, using example code that Csaba shared earlier in this chain as a skeleton. This is not meant to be an extension.</p>
<p>I have rearranged the folder structure on <a href="https://github.com/bsmarine/SinaiSlicelets" rel="nofollow noopener">the repo</a> so that now only a single .py appears, with other .py files in subfolders.</p>
<p>With your help I’ve been able to get the data loading portion of this Slicelet to work, meaning it loads specific files from a desired study folder to specific views with axial orientations.</p>
<p>Next, I would like ideally to have a SegmentEditor but am unsure how to add it as Csaba suggested back on this chain August 13th. I have no formal training in object-oriented programming and apologize if my approaches have been confusing to help troubleshoot.</p>
<p>Is it possible to import the SegmentEditorWidget Class directly to line 131 <a href="https://github.com/bsmarine/SinaiSlicelets/blob/master/seg_widget_test.py" rel="nofollow noopener">here</a>? (Btw, I have renamed the singleton tag to “SinaiSegmentEditor” per your suggestion)</p>
<p>Or do I need to include some of the SegmentEditorWidget initialization code directly into the Slicelet initialization code? Apologies if I’m using these terms incorrectly or if it’s confusing.</p>
<p>Thanks for your guidance!</p>
<p>Brett</p>

---

## Post #16 by @lassoan (2018-11-06 14:56 UTC)

<p>There are two main approaches to use Slicer with simple user interface: create slicelet scripts or create regular modules that hide unnecessary user interface elements (toolbar, menu, etc.). It is much more difficult to write correct slicelet scripts, so I would recommend you to follow the latter approach.</p>
<p>First of all, complete <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Programming_Tutorial">Slicer programming tutorial</a>. Then:</p>
<ul>
<li>Create a new extension using the Extension Wizard</li>
<li>Add a new Python scripted module</li>
<li>Replace the new scripted module with a clone of Slicer’s current SegmentEditor module, with renaming the Python filename and all class names inside</li>
<li>Test if simple segment editing features work well</li>
<li>Add all the custom user interface elements to this module (from your current code snippets)</li>
<li>Test if it all works as expected</li>
<li>Ask us how to simplify user interface, start the module from command-line, etc.</li>
</ul>

---

## Post #17 by @Sam_Horvath (2019-07-18 15:38 UTC)

<p>Hi all, I have an update / extension to this question:<br>
<a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>The error Brett reported:</p>
<blockquote>
<p>QObject::connect: Cannot connect (null)::layoutChanged(int) to qMRMLSegmentEditorWidget::onLayoutChanged(int)</p>
</blockquote>
<p>Is due to this line: <a href="https://github.com/Slicer/Slicer/blob/3402898aabbd40761bed8198f89ebc8832594662/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx#L1698">https://github.com/Slicer/Slicer/blob/3402898aabbd40761bed8198f89ebc8832594662/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx#L1698</a></p>
<p>Essentially, the SegmentEditorWidget explicitly links to the main window layout manager, so it cannot function if the main window is hidden.</p>
<p>Is there some we can change this to point the Widget towards a Slicelet layout?</p>

---
