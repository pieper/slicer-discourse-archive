# How can i make 'redo' & 'undo'?

**Topic ID**: 30836
**Date**: 2023-07-28
**URL**: https://discourse.slicer.org/t/how-can-i-make-redo-undo/30836

---

## Post #1 by @dsa934 (2023-07-28 00:04 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p>Hi, slicer users</p>
<p>I want to make redo &amp; undo functions related to location movement in fiducialnode in 3d slicer.<br>
Is there any example or code I can refer to?</p>

---

## Post #2 by @jamesobutler (2023-07-28 00:57 UTC)

<p>Your previous post has the how-to for undo/redo for markups fiducial nodes. If something is still not working for you I recommend that you continue the discussion over there with what you tried and what you expected to happen.</p>
<aside class="quote quote-modified" data-post="1" data-topic="27368">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/custom-undo-redo-develop/27368">Custom Undo/Redo develop</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Operating system: window 11 
Slicer version: slicer 5.2.1 
Q1. After searching various materials, it was said that the undo/redo function for all nodes drawn in the scene is difficult to implement. Is this true? 
Q2. If so, I want to create a redo and undo function for a specific node (markupFiducial, Closedcurved). 
# Enable undo for the scene

slicer.mrmlScene.SetUndoOn()

# Enable undo for markups fiducial nodes

defaultMarkupsNode = slicer.mrmlScene.GetDefaultNodeByClass("vtkMRMLMarkupsFiduc…
  </blockquote>
</aside>


---
