---
topic_id: 27368
title: "Custom Undo Redo Develop"
date: 2023-01-20
url: https://discourse.slicer.org/t/27368
---

# Custom Undo/Redo develop

**Topic ID**: 27368
**Date**: 2023-01-20
**URL**: https://discourse.slicer.org/t/custom-undo-redo-develop/27368

---

## Post #1 by @dsa934 (2023-01-20 04:00 UTC)

<p>Operating system: window 11<br>
Slicer version: slicer 5.2.1</p>
<p>Q1. After searching various materials, it was said that the undo/redo function for all nodes drawn in the scene is difficult to implement. Is this true?</p>
<p>Q2. If so, I want to create a redo and undo function for a specific node (markupFiducial, Closedcurved).</p>
<pre><code class="lang-auto"># Enable undo for the scene

slicer.mrmlScene.SetUndoOn()

# Enable undo for markups fiducial nodes

defaultMarkupsNode = slicer.mrmlScene.GetDefaultNodeByClass("vtkMRMLMarkupsFiducialNode")
if not defaultMarkupsNode:
    defaultMarkupsNode = slicer.vtkMRMLMarkupsFiducialNode()
    slicer.mrmlScene.AddDefaultNode(defaultMarkupsNode)

defaultMarkupsNode.UndoEnabledOn()

# Add standard keyboard shortcuts for scene undo/redo

redoKeyBindings = qt.QKeySequence.keyBindings(qt.QKeySequence.Redo)
for redoBinding in redoKeyBindings:
    redoShortcut = qt.QShortcut(slicer.util.mainWindow())
    redoShortcut.setKey(redoBinding)
    redoShortcut.connect("activated()", slicer.mrmlScene.Redo)

undoKeyBindings = qt.QKeySequence.keyBindings(qt.QKeySequence.Undo)
for undoBinding in undoKeyBindings:
    undoShortcut = qt.QShortcut(slicer.util.mainWindow())
    undoShortcut.setKey(undoBinding)
    undoShortcut.connect("activated()", slicer.mrmlScene.Undo)
</code></pre>
<p>This <a class="mention" href="/u/lassoan">@lassoan</a> 's code not working in python interactor</p>
<p>After posting this question, I’ll add more detailed questions as I continue to investigate.</p>
<p>What I want to know is how to implement redo/undo for a specific node.</p>

---

## Post #2 by @lassoan (2023-01-20 06:38 UTC)

<p>After copy-pasting the code snippet in the Python console, undo/redo works well for markup point lists. Please describe what you did, what you expected to happen, and what happened instead.</p>

---

## Post #3 by @dsa934 (2023-01-20 07:18 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/add62a25e77a5eea139994a81770347282c5cd75.png" data-download-href="/uploads/short-url/oNPrMapZEqD6xqf0LaPZkVNlwln.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/add62a25e77a5eea139994a81770347282c5cd75_2_485x499.png" alt="image" data-base62-sha1="oNPrMapZEqD6xqf0LaPZkVNlwln" width="485" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/add62a25e77a5eea139994a81770347282c5cd75_2_485x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/add62a25e77a5eea139994a81770347282c5cd75_2_727x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/add62a25e77a5eea139994a81770347282c5cd75.png 2x" data-dominant-color="65656B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">946×974 21.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>step1) copy-pasting your full-code in python console</p>
<p>step2) check one markup points</p>
<p>step3) Press ‘Ctrl+z’ or ‘Alt + Backspace’</p>
<p>result ) The markup point does not disappear and is maintained.</p>

---

## Post #4 by @dsa934 (2023-01-20 08:41 UTC)

<pre><code class="lang-auto"># set undo flag on 
slicer.mrmlScene.SetUndoOn()

# set node types what you want to undo
m_node = slicer.mrmlScene.GetDefaultNodeByClass("vtkMRMLMarkupsFiducialNode")

# save current state
slicer.mrmlScene.SaveStateForUndo()


'making.. markups...'

'oh my mistakes ! let's undo '

# exe undo fucntions ! 
slicer.mrmlScene.Undo


# render preview view 
"um.. i don't know built-in functions"

</code></pre>
<p>I think the undo process for vtkMRMLMarkupsFiducialNode is the same as above. Is that correct?<br>
<a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #5 by @lassoan (2023-01-20 13:48 UTC)

<p>The code snippets changes the default markup point list node so that by default all new nodes of this class are created with undo enabled. If you already have a node then call <code>UndoEnabledOn()</code> method on that existing node.</p>

---
