---
topic_id: 13146
title: "Accessing Sequence Browser Proxy Node In Python For Screen R"
date: 2020-08-24
url: https://discourse.slicer.org/t/13146
---

# Accessing sequence browser proxy node in python for screen recording

**Topic ID**: 13146
**Date**: 2020-08-24
**URL**: https://discourse.slicer.org/t/accessing-sequence-browser-proxy-node-in-python-for-screen-recording/13146

---

## Post #1 by @ifried01 (2020-08-24 19:29 UTC)

<p>Hi,</p>
<p>I am trying to use Python to generate screen-recorded videos of actions in Slicer. I am trying to do so by initializing a sequence browser and recording the main 3D view of ‘Camera’ in Python. I can do it manually, but would like to do it all programmatically.</p>
<p>I am stuck on how to set the main 3D-view camera to be the proxy node for the sequence browser.</p>
<p>Here is what I have so far:</p>
<pre><code># create a new sequence browser node
newSequenceBrowserNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSequenceBrowserNode', 'MySBN')
# create a new sequence node
newSequenceNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSequenceNode', 'Seq1')
# pair the sequence browser node and the sequence node
newSequenceBrowserNode.SetAndObserveMasterSequenceNodeID(newSequenceNode.GetID())
# enable recording
newSequenceBrowserNode.SetRecording(newSequenceNode,True)
*** [somehow set the proxy node] ***
# start recording
newSequenceBrowserNode.RecordingActiveOn()
# perform operations that will be recorded
...
# stop recording
newSequenceBrowserNode.RecordingActiveOff()
# use screen capture module to save as video
...
</code></pre>
<p>I am able to get the cameraNode, but am unable to set it as the proxy node from which information will be recorded.</p>
<pre><code>layoutManager  = slicer.app.layoutManager()
view           = layoutManager.threeDWidget(0).threeDView()
threeDViewNode = view.mrmlViewNode()
cameraNode     = slicer.modules.cameras.logic().GetViewActiveCameraNode(threeDViewNode)
</code></pre>
<p>Any help will be greatly appreciated!</p>

---

## Post #2 by @pieper (2020-08-24 19:36 UTC)

<p>The SlicerAnimator code probably has what you need.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/pieper/SlicerAnimator" target="_blank" rel="noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/126077?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/pieper/SlicerAnimator" target="_blank" rel="noopener">pieper/SlicerAnimator</a></h3>

<p>High level interface for Sequences and Screen Capture - pieper/SlicerAnimator</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @ifried01 (2020-08-24 19:57 UTC)

<p>Thanks, I’ll take a look and follow up if any questions come up</p>

---

## Post #4 by @ifried01 (2021-05-27 22:35 UTC)

<p>Hi,</p>
<p>Just following up on this thread. I have a working version of code that records actions in the 3D view using the sequence browser and then outputs them to a video using the screen capture module. The ‘proxy node’ that gets recorded is ‘Default Scene Camera’.</p>
<p>All motions are logged in the sequence browser, but changes in color are not. More specifically, I change the color of the segmentation object every 10 seconds, but only the final color gets captured in the video. I can capture just the color change if I set the ‘proxy node’ to the segmentation object.</p>
<p>Is it possible to follow two nodes (i.e. the scene camera and the object color) so that I can record both the color changes and the camera motions simultaneously?</p>
<p>Thanks</p>

---
