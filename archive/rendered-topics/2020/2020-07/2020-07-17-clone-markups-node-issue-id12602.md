---
topic_id: 12602
title: "Clone Markups Node Issue"
date: 2020-07-17
url: https://discourse.slicer.org/t/12602
---

# Clone Markups Node Issue

**Topic ID**: 12602
**Date**: 2020-07-17
**URL**: https://discourse.slicer.org/t/clone-markups-node-issue/12602

---

## Post #1 by @mjg (2020-07-17 17:11 UTC)

<p>Hello,</p>
<p>I need to clone line, curve, and closed curve nodes. When I use the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Clone_a_node" rel="noopener nofollow ugc">method in the script repository</a> it creates a trace of the original node. Does anyone have a fix or better method? I am using Python.</p>
<p>The leftmost blue line is the original node and the rightmost red line is the clone node (which I have moved to show the trace). I want only the line connecting the two points.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83895030289b80fa320b411308dd74e5e506f9f1.png" data-download-href="/uploads/short-url/iLCJVVTsV6Q2vwmafXjnlSFAAgh.png?dl=1" title="Screen Shot 2020-07-17 at 11.04.11 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83895030289b80fa320b411308dd74e5e506f9f1.png" alt="Screen Shot 2020-07-17 at 11.04.11 AM" data-base62-sha1="iLCJVVTsV6Q2vwmafXjnlSFAAgh" width="503" height="500" data-dominant-color="020101"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-07-17 at 11.04.11 AM</span><span class="informations">648×644 2.02 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2020-07-17 17:37 UTC)

<p>I cannot reproduce this issue with latest Slicer Preview Release. I created a markups line node and ran this script:</p>
<pre><code class="lang-python">nodeToClone = getNode('L')
shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
itemIDToClone = shNode.GetItemByDataNode(nodeToClone)
clonedItemID = slicer.modules.subjecthierarchy.logic().CloneSubjectHierarchyItem(shNode, itemIDToClone)
clonedNode = shNode.GetItemDataNode(clonedItemID)
</code></pre>

---
