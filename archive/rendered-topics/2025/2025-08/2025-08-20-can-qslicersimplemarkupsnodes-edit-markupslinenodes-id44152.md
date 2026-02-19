---
topic_id: 44152
title: "Can Qslicersimplemarkupsnodes Edit Markupslinenodes"
date: 2025-08-20
url: https://discourse.slicer.org/t/44152
---

# Can qSlicerSimpleMarkupsNodes edit MarkupsLineNodes?

**Topic ID**: 44152
**Date**: 2025-08-20
**URL**: https://discourse.slicer.org/t/can-qslicersimplemarkupsnodes-edit-markupslinenodes/44152

---

## Post #1 by @mrsh0r3s (2025-08-20 22:06 UTC)

<p>Hello,</p>
<p>I am trying to centralize some steps in a workflow and thus want to add a markups widget to the extension. I tried a qSlicerSimpleMarkupsWidget but it only seems to interact with point list markupsnodes rather than markupslinenodes. Is there a way to make it interact with Line nodes?</p>
<p>qMRMLNodeComboBox has a ‘node types’ parameter that allows me to only show Line nodes and gives the desired effect. However, there isn’t a display table with the RAS coordinates, visibility, locks, etc. The SimpleMarkupsWidget has those elements but doesn’t seem to acknowledge LineNodes.</p>
<p>My primary goal is to be able to view and edit the control points of a specific line node from the custom module. Any suggestions?</p>
<p>Combo Box</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab6596bab3d60de5ee5c73086d015fcd170e79ba.png" data-download-href="/uploads/short-url/osfiCNXyNfwOtInMRwCUclzaXDs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab6596bab3d60de5ee5c73086d015fcd170e79ba.png" alt="image" data-base62-sha1="osfiCNXyNfwOtInMRwCUclzaXDs" width="544" height="151"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">544×151 34.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>SimpleMarkupsWidget</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/910f41e6d7c67962b27983df2c6a2d8fab5484b5.png" data-download-href="/uploads/short-url/kHfVazuf3A8ArQWcbdrV8aUfJvT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/910f41e6d7c67962b27983df2c6a2d8fab5484b5.png" alt="image" data-base62-sha1="kHfVazuf3A8ArQWcbdrV8aUfJvT" width="563" height="193"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">563×193 40.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-08-20 22:11 UTC)

<p>You can choose what node types you want to see in the <code>qSlicerSimpleMarkupsWidget</code>’s node selector by calling methods of the <a href="https://apidocs.slicer.org/main/classqSlicerSimpleMarkupsWidget.html#ae710c0c9a43fbc228ea4e8a8bde0ed64">node selector</a>. Something like this:</p>
<pre><code>simpleWidget.markupsSelectorComboBox().nodeTypes = ["vtkMRMLMarkupsLineNode"]
</code></pre>

---

## Post #3 by @mrsh0r3s (2025-08-20 22:25 UTC)

<p>Ah I see, that makes sense. Thank you, I didn’t realize that the elements that make up the widget could be interfaced with directly. What is the best way to see the available children elements of a higher level widget like this? Like all of the options for “simpleWidget.whatever” to follow the conventions of you example? In Qt it always appeared as a single object.</p>

---

## Post #4 by @lassoan (2025-08-20 22:41 UTC)

<p>The <a href="https://apidocs.slicer.org/main/classqSlicerSimpleMarkupsWidget.html">API documentation</a> lists all the members of Slicer classes.</p>
<p>Note that internal components of a widget are rarely exposed, as it can be misused. It is sometimes done when the risk is deemed to be low and it significantly simplifies the implementation, but it would be safer and nicer to just expose methods.</p>

---

## Post #5 by @mrsh0r3s (2025-08-20 22:47 UTC)

<p>I see where I went wrong now. This clarifies some of the documentation for me, thank you.</p>

---
