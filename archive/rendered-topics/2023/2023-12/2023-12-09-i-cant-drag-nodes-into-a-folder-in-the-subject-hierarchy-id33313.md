# I can't drag nodes into a folder in the subject hierarchy

**Topic ID**: 33313
**Date**: 2023-12-09
**URL**: https://discourse.slicer.org/t/i-cant-drag-nodes-into-a-folder-in-the-subject-hierarchy/33313

---

## Post #1 by @jashrand (2023-12-09 12:24 UTC)

<p>I’m sure this is a silly question, but I can’t click-and-drag nodes in the subject hierarchy to put them into a folder. I’m using a Macbook with a normal touchpad, no external mouse or anything. Every time I click and drag a file it just highlights everything the mouse goes over, as though I were holding down the shift key to select multiple files.</p>
<p>See the attached video. All I’m trying to do is click-and-drag a single node into the folder in the subject hierarchy.</p>
<p>There doesn’t seem to be a cut/paste option either, so I have no idea how to move the nodes. Does anyone know how to do this?</p>
<p>Thanks!</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cc3588d5bcb6b0ca2394494d4ba6ce730daf99e.mp4">
  </div><p></p>

---

## Post #2 by @pieper (2023-12-09 14:50 UTC)

<p>Hmm, don’t know.  Dragging nodes into folders in the subject hierarchy works for me on a mac trackpad (mac book air M2)</p>

---

## Post #3 by @cpinter (2023-12-11 13:01 UTC)

<p>Can you paste this in the Python console:</p>
<pre><code class="lang-auto">dmw = slicer.modules.data.widgetRepresentation()
shtvs = findChildren(dmw, className='qMRMLSubjectHierarchyTreeView')
shtv = shtvs[0]
print(shtv.dragEnabled)
</code></pre>
<p>If it gives False, try <code>shtv.dragEnabled = True</code> and see what happens.</p>

---
