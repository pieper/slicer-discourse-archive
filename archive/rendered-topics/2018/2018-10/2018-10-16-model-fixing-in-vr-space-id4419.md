# Model fixing in VR space

**Topic ID**: 4419
**Date**: 2018-10-16
**URL**: https://discourse.slicer.org/t/model-fixing-in-vr-space/4419

---

## Post #1 by @M_pavi (2018-10-16 21:31 UTC)

<p>How do we fix the model in VR space without moving anywhere? IUsusally when we move the model using controllers we can move it. But I want to fix the  model in the surface.</p>

---

## Post #2 by @lassoan (2018-10-16 21:36 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> could you add the node attribute name that controls movability to the <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/DeveloperGuide.md">developer guide</a>?</p>

---

## Post #3 by @cpinter (2018-10-16 22:10 UTC)

<p>I updated the guide, see the bottom of the page.</p>
<p>Also I added a feature in the Data module where you can set this flag in the context menu of nodes and folders, but I think it’s not updated in the downloadable extension yet. I’ll do that very soon.</p>

---

## Post #4 by @M_pavi (2018-10-16 22:47 UTC)

<p>I tried but there is an error by saying " NameError: name ‘nodeLocked’ is not defined"</p>

---

## Post #5 by @lassoan (2018-10-16 23:35 UTC)

<p><code>nodeLocked</code> refers to a MRML node object. You can use <code>nodeLocked=getNode("My node")</code> to get a node object from node name.</p>

---
