---
topic_id: 9646
title: "Set A Node As A Parent For The Other Nodes"
date: 2019-12-29
url: https://discourse.slicer.org/t/9646
---

# Set a node as a parent for the other nodes

**Topic ID**: 9646
**Date**: 2019-12-29
**URL**: https://discourse.slicer.org/t/set-a-node-as-a-parent-for-the-other-nodes/9646

---

## Post #1 by @Mik (2019-12-29 18:32 UTC)

<p>Greetings,</p>
<p>How to setup vtkMRMLRTBeamNode as a parent node for a other nodes (e.g., vtkMRMLTableNode)?</p>
<p>The beam node observed some table node, and in the hierarchy tree view widget the drag-and-drop operation allows to put table node as a child the beam node, but how to do same thing using C++?</p>
<p>The code like: <code>shNode-&gt;SetItemParent( tableNodeId, beamNodeId) </code>  doesn’t work even if all item IDs are valid.</p>
<p>The result should look like on the After picture.</p>
<p>Before<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b837522059f81295efbf42739353155ed0b436c6.png" data-download-href="/uploads/short-url/qhEnugVPJZ5IH9BvGsdndhZkXJA.png?dl=1" title="HierarchyBefore" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b837522059f81295efbf42739353155ed0b436c6_2_267x500.png" alt="HierarchyBefore" data-base62-sha1="qhEnugVPJZ5IH9BvGsdndhZkXJA" width="267" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b837522059f81295efbf42739353155ed0b436c6_2_267x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b837522059f81295efbf42739353155ed0b436c6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b837522059f81295efbf42739353155ed0b436c6.png 2x" data-dominant-color="E7EBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">HierarchyBefore</span><span class="informations">384×719 38.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b5030247033547d70543af7cea1c128d6aa26af.png" data-download-href="/uploads/short-url/aKfBY4nK2J8SKKPSmeELQUNjuWP.png?dl=1" title="HierarchyAfter" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b5030247033547d70543af7cea1c128d6aa26af_2_283x500.png" alt="HierarchyAfter" data-base62-sha1="aKfBY4nK2J8SKKPSmeELQUNjuWP" width="283" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b5030247033547d70543af7cea1c128d6aa26af_2_283x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b5030247033547d70543af7cea1c128d6aa26af.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b5030247033547d70543af7cea1c128d6aa26af.png 2x" data-dominant-color="EBECEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">HierarchyAfter</span><span class="informations">380×671 56.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-12-29 19:16 UTC)

<p><code>SetItemParent</code> method should work well. Use subject hierarchy item IDs (not MRML node IDs) as inputs. Make sure you use latest stable or latest preview release.</p>

---

## Post #3 by @Mik (2019-12-30 18:16 UTC)

<p>Could it be that batch process state of the scene prevent such operation? It works well after <code>scene-&gt;EndState(vtkMRMLScene::BatchProcessState);</code>.</p>

---

## Post #4 by @lassoan (2019-12-30 18:45 UTC)

<p>There are limited or no widget updates while in batch processing state, but after batch processing ends, all the pending changes should be applied.</p>

---
