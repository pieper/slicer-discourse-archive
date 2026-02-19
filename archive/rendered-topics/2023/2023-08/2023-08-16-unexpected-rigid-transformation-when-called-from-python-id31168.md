---
topic_id: 31168
title: "Unexpected Rigid Transformation When Called From Python"
date: 2023-08-16
url: https://discourse.slicer.org/t/31168
---

# Unexpected rigid transformation when called from python

**Topic ID**: 31168
**Date**: 2023-08-16
**URL**: https://discourse.slicer.org/t/unexpected-rigid-transformation-when-called-from-python/31168

---

## Post #1 by @stephan13 (2023-08-16 09:53 UTC)

<p>Hi there,</p>
<p>if I rigidly register two volumes within Slicer using the Elastix module, everything is as expected. However, when called from Python, I encountered unexpected behavior. The code worked using Slicer 4.11 and Elastix 5.0.1, the issues appeared using Slicer 5.2.2 and Elastix 5.1.0:</p>
<ol>
<li>
<p>transform matrix is not shown in transform module<br>
expected:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6442947c012de2c76789cc30a57c37574f8a2dd3.png" alt="expected_transform" data-base62-sha1="eiWoqOOJ5VJyret2NvL6Xh87Mll" width="266" height="184"><br>
got:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13aea87916a7751bbf3d789dd3dee6fdcd6b6957.png" alt="got_transform" data-base62-sha1="2O7h3OL7WntS2opjUAA3sfsk1Dx" width="328" height="230"></p>
</li>
<li>
<p>When exporting the resulting transformation to file, the .tfm file is gigantic with &gt;700MB, normally it’s just the transformation matrix and a few KB in size.</p>
</li>
</ol>
<p>Here’s the relevant python code:</p>
<pre><code class="lang-auto"> elastixLogic = Elastix.ElastixLogic()
 # create result transform
 slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTransformNode', result_transform_name)
 # register
 elastixLogic.registerVolumes(get_node_by_name(slicer, fixed_name),
                           get_node_by_name(slicer, moving_name),
                           parameterFilenames=[path_params_rigid],
                           outputTransformNode=get_node_by_name(slicer,
                                                                result_transform_name))
</code></pre>
<p>get_node_by_name() just calls slicer.util.getNode()</p>
<p>I checked the rigid parameter file, it correctly uses a local copy of Parameters_Rigid.txt from the<br>
<a>https://github.com/lassoan/SlicerElastix/blob/master/Elastix/Resources/RegistrationParameters/Parameters_Rigid.txt</a> repo, which is consistent with the file in AppData (path see below).</p>
<p>As a reference also the Elastix output when called manually via the Elastix module UI within Slicer:</p>
<pre><code class="lang-auto">which elastix:   C:\Users\steph\AppData\Local\NA-MIC\Slicer 5.2.2\NA-MIC\Extensions-31382\SlicerElastix\lib\Slicer-5.2\elastix.exe
  elastix version: 5.1.0
  Git revision SHA: d652938573e5f193955908eba225a854b31ce36a
  Git revision date: Thu Jan 12 14:20:18 2023 +0100
  Build date: Apr 25 2023 06:37:51
  Compiler: Visual C++ version 193532217.1
  Memory address size: 64-bit
  CMake version: 3.22.1
  ITK version: 5.3.0

Command-line arguments:
  -f C:/Users/steph/AppData/Local/Temp/Slicer/Elastix/20230816_103312_020\input\fixed.mha 
-m C:/Users/steph/AppData/Local/Temp/Slicer/Elastix/20230816_103312_020\input\moving.mha 
-out C:/Users/steph/AppData/Local/Temp/Slicer/Elastix/20230816_103312_020\result-transform 
-p "C:\Users\steph\AppData\Local\NA-MIC\Slicer 5.2.2\NA-MIC\Extensions-31382\SlicerElastix\lib\Slicer-5.2\qt-scripted-modules\Resources\RegistrationParameters\Parameters_Rigid.txt"
</code></pre>
<p>What could be the issue here? Note that the python generated transformation is still fine, I can apply and correctly transform volumes with it.</p>
<p>Thanks!</p>

---

## Post #2 by @stephan13 (2023-09-27 06:30 UTC)

<p>any update on this post?</p>

---

## Post #3 by @mikebind (2023-09-27 18:37 UTC)

<p>I know that the Elastix module code changed since 5.0.1 because some of my module code which was using it broke in 5.2.2 (I haven’t figured out how to fix it yet, so I just know there was a breaking change).  As a simple first attempt, I would suggest that you try forcing the result transform to be linear and see if that works:</p>
<pre><code class="lang-auto">slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLinearTransformNode', result_transform_name)
</code></pre>
<p>Perhaps the Elastix module is now detecting the type of the transform node, and if it is a general transform node it returns a displacement field transform rather than the previously expected linear matrix.  If I recall correctly, the displacement field transform is the default output of Elastix registration, and there was some code in the Elastix module which tried to detect the special case where a linear transformation matrix could be returned instead and converted it. Perhaps that check is now only run if the output transformation node type seems to call for it.</p>

---

## Post #4 by @lassoan (2023-09-28 03:03 UTC)

<aside class="quote no-group" data-username="stephan13" data-post="1" data-topic="31168">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/7ea924/48.png" class="avatar"> stephan13:</div>
<blockquote>
<pre><code class="lang-auto">elastixLogic = Elastix.ElastixLogic()
 # create result transform
 slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTransformNode', result_transform_name)
 # register
 elastixLogic.registerVolumes(get_node_by_name(slicer, fixed_name),
                           get_node_by_name(slicer, moving_name),
                           parameterFilenames=[path_params_rigid],
                           outputTransformNode=get_node_by_name(slicer,
                                                                result_transform_name))
</code></pre>
</blockquote>
</aside>
<p>By default, displacement field is requested as registration output. Probably this choice was kept for backward compatibility (for a good while Elastix was not able to write ITK transforms and so it was safer and simpler to get a displacement field).</p>
<p>If you want to get a linear transform then you can add the <code>forceDisplacementFieldOutputTransform=False</code> argument to the <code>registerVolumes</code> call.</p>

---

## Post #5 by @stephan13 (2023-10-12 13:34 UTC)

<p>Perfect thanks! Adding the flag solved the issue <img src="https://emoji.discourse-cdn.com/twitter/ok_hand.png?v=12" title=":ok_hand:" class="emoji" alt=":ok_hand:" loading="lazy" width="20" height="20"></p>

---
