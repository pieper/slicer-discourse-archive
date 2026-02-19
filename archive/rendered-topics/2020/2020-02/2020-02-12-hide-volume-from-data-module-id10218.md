---
topic_id: 10218
title: "Hide Volume From Data Module"
date: 2020-02-12
url: https://discourse.slicer.org/t/10218
---

# Hide volume from data module

**Topic ID**: 10218
**Date**: 2020-02-12
**URL**: https://discourse.slicer.org/t/hide-volume-from-data-module/10218

---

## Post #1 by @giovform (2020-02-12 16:19 UTC)

<p>Hello! I would like to know if there is a way to programmatically hide a volume node from the Data module, as there is other nodes hidden. Tried to find the function to do that, but no success.</p>
<p>Thanks!</p>

---

## Post #2 by @adamrankin (2020-02-12 16:34 UTC)

<p><a href="https://apidocs.slicer.org/v4.8/classvtkMRMLNode.html#a5b00bd936194a0aeb791a5bf8832c993" class="onebox" target="_blank" rel="nofollow noopener">https://apidocs.slicer.org/v4.8/classvtkMRMLNode.html#a5b00bd936194a0aeb791a5bf8832c993</a></p>

---

## Post #3 by @giovform (2020-02-12 16:37 UTC)

<p>Hi Adam, I tried this and unfortunately it does not hide from the Data module tree view, just from the select boxes.</p>

---

## Post #4 by @adamrankin (2020-02-12 16:50 UTC)

<p>Is show hidden checked in the data module?</p>
<p>Nightly 2019-12-02 behaves as expected, what version are you using?</p>

---

## Post #5 by @lassoan (2020-02-12 16:51 UTC)

<p>For performance reasons, HideFromEditor status is not refreshed for all the nodes in all node selectors all the time. You need to set HideFromEditor immediately after you create the node (even before you add it to the scene).</p>
<p>If you want to just hide it from the Subject Hierarchy tree then you can exclude it from only there (that can be done anytime). You can also filter the subject hierarchy tree or show only a sub-tree.</p>
<p>What would you like to achieve? Why would you like to hide that node?</p>

---

## Post #6 by @giovform (2020-02-12 17:05 UTC)

<p>I wanted to apply some voxel intensity changing operations on my data, and allow to revert it back as needed (the hidden volume node would store the original data). The solution to set hidden on the node creation is then sufficient for what I am trying to do.</p>
<p>Thanks all!</p>

---

## Post #7 by @jcfr (2020-02-12 20:54 UTC)

<blockquote>
<p>You need to set HideFromEditor immediately after you create the node (even before you add it to the scene).</p>
</blockquote>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Should we update the the doxygen referenced by <a class="mention" href="/u/adamrankin">@adamrankin</a> to include this information. See <a href="https://apidocs.slicer.org/v4.8/classvtkMRMLNode.html#a5b00bd936194a0aeb791a5bf8832c993" class="inline-onebox">Slicer: vtkMRMLNode Class Reference</a></p>

---

## Post #8 by @lassoan (2020-02-12 21:17 UTC)

<aside class="quote no-group" data-username="giovform" data-post="6" data-topic="10218">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovform/48/4687_2.png" class="avatar"> giovform:</div>
<blockquote>
<p>I wanted to apply some voxel intensity changing operations on my data, and allow to revert it back as needed (the hidden volume node would store the original data).</p>
</blockquote>
</aside>
<p>For this, creating a new node and adding it to the scene is an overkill (and it may create loose ends - what if the user saves the scene, would you like this temporary node to be saved? do you want to restore node references and various other properties from the saved node? etc.).</p>
<p>If you only care about saving the image data so that you can later restore if needed then you can create a <code>vtk.vtkImageData</code> object and <code>DeepCopy</code> the <code>volumeNode.GetImageData()</code> output into that.</p>

---

## Post #9 by @smrolfe (2020-10-16 17:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="10218">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For performance reasons, HideFromEditor status is not refreshed for all the nodes in all node selectors all the time. You need to set HideFromEditor immediately after you create the node (even before you add it to the scene).</p>
</blockquote>
</aside>
<p>Is there a way to force the HideFromEditor status to update in specific modules (i.e. Data module subject hierarchy)?</p>
<p>My module hides some nodes it creates so its UI is the main way to interact with the visualization of results. But I’d also like to provide a few lines of python to expose specific nodes if needed to customize the visualization. Is this possible or does the hide setting need to be set on node creation?</p>

---

## Post #10 by @lassoan (2020-10-16 17:20 UTC)

<p>There is no way of forced refreshing HideFromEditor status. Since batch processing is already a costly operation, it could be possible to update the scene models then. Scene model already has a few issues (such as <a href="https://github.com/Slicer/Slicer/issues/4570">https://github.com/Slicer/Slicer/issues/4570</a>), maybe this feature could be added while resolving those issues.</p>
<p>However, I think what you want can be much more easily achieved: by enabling display of hidden nodes in node selector widgets in your modules.</p>
<p>There may be other approaches, too. What nodes would you like to hide and why?</p>

---

## Post #11 by @smrolfe (2020-10-16 18:18 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, this came up because we were trying to change the selected viewer through the module module for a hidden model. Our module creates several visualization models that the user can toggle through and these nodes are currently hidden from display for simplicity.</p>
<p>For scripted modules it seems that reloading will update the HideFromEditor status for the node selector widgets, so I was wondering if there was an equivalent for loaded modules.</p>
<p>I think we’ll consider just unhiding the models, since it is creating more issues than it is solving.</p>

---

## Post #12 by @lassoan (2020-10-16 18:43 UTC)

<p>Hidden nodes have several limitations, for example they are not saved with the scene (not shown in Save data dialog). So, I agree that it is better to use alternative solutions, such as filtering by node attribute or show a specific branch in the subject hierarchy tree (or put all infrequently used nodes in a subject hierarchy tree branch, collapsed).</p>

---
