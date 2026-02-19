---
topic_id: 31076
title: "Using Volume Reslice Driver Programatically"
date: 2023-08-09
url: https://discourse.slicer.org/t/31076
---

# Using Volume Reslice Driver Programatically

**Topic ID**: 31076
**Date**: 2023-08-09
**URL**: https://discourse.slicer.org/t/using-volume-reslice-driver-programatically/31076

---

## Post #1 by @pfrwilson (2023-08-09 20:44 UTC)

<p>Hello community,</p>
<p>I am having trouble using the volume reslice driver module programmatically. For many loadble scripted modules, I am used to accessing their logic and widget classes by importing them e.g <code>import MyModule</code> or accessing them through <code>slicer.modules.module_name.widgetRepresentation()</code> typically <code>help(...)</code> is then sufficient to figure out how to use it.</p>
<p>For volume reslice driver, I have found the class <code>slicer.vtkSlicerVolumeResliceDriverLogic</code>. However, when I try to use some of its methods, slicer crashes. for example:</p>
<pre><code class="lang-python">&gt;&gt;&gt; logic = slicer.vtkSlicerVolumeResliceDriverLogic()
&gt;&gt;&gt; red = slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeRed')
&gt;&gt;&gt; volume = getNode('BMode_5')
&gt;&gt;&gt; logic.SetDriverForSlice(volume.GetID(), red)
</code></pre>
<p>Causes slicer to immediately close.</p>
<p>My goal is to programatically do what the volume reslice driver module widget does.</p>
<p>Thanks in advance,</p>
<p>Paul</p>

---

## Post #2 by @pfrwilson (2023-08-09 20:45 UTC)

<p>I tried also visting here: <a href="https://github.com/openigtlink/VolumeResliceDriver/blob/master/Logic/vtkSlicerVolumeResliceDriverLogic.h" rel="noopener nofollow ugc">https://github.com/openigtlink/VolumeResliceDriver/blob/master/Logic/vtkSlicerVolumeResliceDriverLogic.h</a> but the header file does not give me too many clues how to use the class…</p>

---

## Post #3 by @lassoan (2023-08-10 09:11 UTC)

<p>Typically the easiest is to create MRML nodes and set its properties. You can save the scene and look at the .mrml file to see what nodes are created and what properties are set.</p>
<p>Module logic classes observe all the nodes that are added to the scene, so you rarely have to call any logic functions (except sometimes there are some convenience functions in logic classes that can be useful). It should never be necessary to call module widget methods directly (the module widgets are meant to respond to scene changes and user actions on the GUI).</p>

---

## Post #4 by @ungi (2023-08-10 20:35 UTC)

<p>I’ve compared your code with a working example, and the only difference I found was in the way you get an instance of the volume reslice driver logic. You don’t have “.modules” par of this line: <a href="https://github.com/SlicerIGT/LumpNav/blob/13511fccbee82553de91f0e495ba89eed82bbe4b/LumpNav2/LumpNav2.py#L1682" rel="noopener nofollow ugc">https://github.com/SlicerIGT/LumpNav/blob/13511fccbee82553de91f0e495ba89eed82bbe4b/LumpNav2/LumpNav2.py#L1682</a></p>

---

## Post #5 by @pfrwilson (2023-08-11 12:26 UTC)

<p>Hi Andras and Tamas,</p>
<p>Thanks for your responses. Tamas, the code you shared appears to do exactly what I need to do, so I should be able to implement that no problem!</p>
<p>Paul</p>

---
