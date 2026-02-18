# "Save before exit?" always shows, even right after save

**Topic ID**: 21926
**Date**: 2022-02-11
**URL**: https://discourse.slicer.org/t/save-before-exit-always-shows-even-right-after-save/21926

---

## Post #1 by @hherhold (2022-02-11 19:40 UTC)

<p>4.13.0-2022-02-07, although this has been happening for some time.</p>
<p>If I save, then try to exit, I always get the “Some data have been modified. Do you want to save them before exit?”</p>
<p>Is there a way to figure out what nodes Slicer thinks have been modified since last save?</p>

---

## Post #2 by @lassoan (2022-02-11 20:35 UTC)

<p>Good catch! There was a bug in the logic that marks the scene as saved (introduced during recent improvement of scene save error handling). I’ll fix the issue and also include a code snippet that lists modified nodes since the last save.</p>

---

## Post #3 by @jamesobutler (2022-02-11 20:37 UTC)

<p>I think you can see what nodes it thinks have been modified since last save by opening the save dialog and the items that are unchecked are the things that haven’t been modified since last save. Here I saved everything and then reopened the save dialog (hence unchecked items) and noticed the mrml scene was still checked. So maybe something about the mrml scene is then reason for the continued alert of still unsaved data.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc3217045fade4fd7ecdeefa9d85d9426f22cc33.png" alt="image" data-base62-sha1="vpWmmhUxcnOFDg3dRDZJdJXyTLR" width="632" height="337"></p>

---

## Post #4 by @hherhold (2022-02-11 20:50 UTC)

<p>Yeah, it would always say just the MRML file had been modified. I was more curious if a node saved <em>in</em> the MRML was getting marked as modified.</p>

---

## Post #5 by @hherhold (2022-02-11 20:51 UTC)

<p>Awesome! Sounds great, thanks.</p>

---

## Post #6 by @lassoan (2022-02-11 23:52 UTC)

<p>Saving of scene or data is offered on application exit if either</p>
<ul>
<li>any nodes in the scene were modified (this logic got <a href="https://github.com/Slicer/Slicer/commit/8694fc789671ef66644d10fff66d9c37826c40bd">fixed</a> today), or</li>
<li>bulk data in any storable node is modified.</li>
</ul>
<p>From tomorrow in Slicer Preview Release you can get the lists of these modified nodes like this:</p>
<pre><code class="lang-python"># Modified nodes that are stored in the scene
nodesModifiedInScene = vtk.vtkCollection()
slicer.mrmlScene.GetModifiedSinceRead(nodesModifiedInScene)
for nodeIndex in range(nodesModifiedInScene.GetNumberOfItems()):
    print(nodesModifiedInScene.GetItemAsObject(nodeIndex).GetID())

# Nodes that contain modified bulk data (stored in files)
modifiedStorableNodes = vtk.vtkCollection()
slicer.mrmlScene.GetStorableNodesModifiedSinceRead(modifiedStorableNodes)
for nodeIndex in range(modifiedStorableNodes.GetNumberOfItems()):
    print(modifiedStorableNodes.GetItemAsObject(nodeIndex).GetID())
</code></pre>

---
