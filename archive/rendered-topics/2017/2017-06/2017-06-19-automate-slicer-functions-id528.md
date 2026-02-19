---
topic_id: 528
title: "Automate Slicer Functions"
date: 2017-06-19
url: https://discourse.slicer.org/t/528
---

# Automate Slicer functions

**Topic ID**: 528
**Date**: 2017-06-19
**URL**: https://discourse.slicer.org/t/automate-slicer-functions/528

---

## Post #1 by @f.cnunez (2017-06-19 15:54 UTC)

<p>Hi all,<br>
I was developing as my final degree project a OpenIGTLink communication between a software called ORB-SLAM2 and 3DSlicer(to pass a series of transforms). I have made the communication successfully but I have to operate with the OpenIGTLink and tranforms modules and I want to automate all the process. What I want to automate is:</p>
<ol>
<li>Load a .stl file in the scene.</li>
<li>Open a IGTLConnector in OpenIGTLink and set it as active client.</li>
<li>Apply the transforms sent by the OpenIGTLink module to the 3d model loaded in step 1 in the transforms module.</li>
</ol>
<p>My teacher told me that I can do this actions creating a python module with an apply button, and when you press the button you apply all the changes (making easier to the user to work with this information). I would like to know if this is possible and when I can find information about how can I develop that.</p>
<p>Thanks.</p>

---

## Post #2 by @ihnorton (2017-06-19 16:05 UTC)

<aside class="quote no-group" data-username="f.cnunez" data-post="1" data-topic="528">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/cc9497/48.png" class="avatar"> f.cnunez:</div>
<blockquote>
<p>Load a .stl file in the scene.</p>
</blockquote>
</aside>
<p>Look in <code>Base/Python/slicer/util.py</code>, there are utility functions for loading a variety of data.</p>
<aside class="quote no-group" data-username="f.cnunez" data-post="1" data-topic="528">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/cc9497/48.png" class="avatar"> f.cnunez:</div>
<blockquote>
<p>Open a IGTLConnector in OpenIGTLink and set it as active client.</p>
</blockquote>
</aside>
<p>Yes, it’s all scriptable. You might have to poke at the API a little bit in the prompt to find exactly what you need, but there’s plenty of python code to start from in SlicerIGT, e.g.:</p>
<p><a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/PlusRemote/PlusRemote.py" class="onebox" target="_blank" rel="noopener">https://github.com/SlicerIGT/SlicerIGT/blob/master/PlusRemote/PlusRemote.py</a></p>
<aside class="quote no-group" data-username="f.cnunez" data-post="1" data-topic="528">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/cc9497/48.png" class="avatar"> f.cnunez:</div>
<blockquote>
<p>Apply the transforms sent by the OpenIGTLink module to the 3d model loaded in step 1 in the transforms module.</p>
</blockquote>
</aside>
<p>You would only need to do this once: set the parent transform of the model to the transform that is receiving the OpenIGTLink updates. The model node will have a <code>SetAndObserveTransformNodeID</code> method, see:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Add_a_texture_mapped_plane_to_the_scene_as_a_model" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Add_a_texture_mapped_plane_to_the_scene_as_a_model</a></p>

---

## Post #3 by @f.cnunez (2017-06-19 16:11 UTC)

<p>Ok, I would try to do as you say. Then it should be possible to do it this way with only an apply button?</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2017-06-19 19:56 UTC)

<aside class="quote no-group" data-username="f.cnunez" data-post="3" data-topic="528">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/cc9497/48.png" class="avatar"> f.cnunez:</div>
<blockquote>
<p>it should be possible to do it this way with only an apply button</p>
</blockquote>
</aside>
<p>Yes.</p>
<p>Setting up a new connection using Python:</p>
<pre><code>cn=slicer.vtkMRMLIGTLConnectorNode()
slicer.mrmlScene.AddNode(cn)
cn.Start()
</code></pre>
<p>However, you only need to create the connector node from a script if you write a script for setting up the scene. Most often you manually set up everything in a scene (OpenIGTLink connection, transform, models, views, tool calibrations, etc.) and then save that scene. Then at the beginning of the procedure you open the scene and Slicer automatically connects to your tracker/imaging system and everything just works. If the “persistence” flag of the OpenIGTLink connection is disabled then you need to activate the connection manually (this is useful when the IP address of a clinical navigation system on the hospital network is stored in the scene and you want to avoid accidental connection attempts).</p>

---
