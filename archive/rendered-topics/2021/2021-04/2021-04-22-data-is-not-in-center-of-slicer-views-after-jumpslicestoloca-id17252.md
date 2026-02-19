---
topic_id: 17252
title: "Data Is Not In Center Of Slicer Views After Jumpslicestoloca"
date: 2021-04-22
url: https://discourse.slicer.org/t/17252
---

# Data is not in center of slicer views after JumpSlicesToLocation process

**Topic ID**: 17252
**Date**: 2021-04-22
**URL**: https://discourse.slicer.org/t/data-is-not-in-center-of-slicer-views-after-jumpslicestolocation-process/17252

---

## Post #1 by @luxiaoyang9999 (2021-04-22 12:50 UTC)

<p>Hi all<br>
I use the JumpSlicesToLocation to change data in slicer view when mouse position changed, but images in slicer view will not be in view center, how can I solve the problm, this is my code</p>
<pre><code>def jumpToCursor(self):
    ras = [0, 0, 0]
    slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLCrosshairNode').GetCursorPositionRAS(ras)
    slicer.modules.markups.logic().JumpSlicesToLocation(ras[0], ras[1], ras[2], slicer.vtkMRMLCrosshairNode.JumpSlice)
    print(ras[1])
shortcut = qt.QShortcut(slicer.util.mainWindow())
shortcut.setKey(qt.QKeySequence("Ctrl+B"))
shortcut.connect('activated()', jumpToCursor)</code></pre>

---

## Post #2 by @luxiaoyang9999 (2021-04-22 12:57 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/808dca7d3893647741ff69a816a7159b2772ae63.png" data-download-href="/uploads/short-url/ileTVcgHOYSdrohNeRmCqlnoEhl.png?dl=1" title="1619096161(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/808dca7d3893647741ff69a816a7159b2772ae63_2_690x130.png" alt="1619096161(1)" data-base62-sha1="ileTVcgHOYSdrohNeRmCqlnoEhl" width="690" height="130" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/808dca7d3893647741ff69a816a7159b2772ae63_2_690x130.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/808dca7d3893647741ff69a816a7159b2772ae63_2_1035x195.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/808dca7d3893647741ff69a816a7159b2772ae63_2_1380x260.png 2x" data-dominant-color="131313"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1619096161(1)</span><span class="informations">1595×302 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
here is the screenshot after the code excuted</p>

---

## Post #3 by @lassoan (2021-04-25 15:25 UTC)

<p>You can choose to you can use <code>CenteredJumpSlice</code> option if you want the chosen position be centered.</p>

---

## Post #4 by @luxiaoyang9999 (2021-04-26 04:06 UTC)

<p>I try this, but it seems not to work, I want to get a similiar function like ‘Shift + mouse’ in slicer, and rewrite it. Could you tell  me where to rewrite  ‘Shift + mouse’ in Python or  realize similar function like it?</p>

---

## Post #5 by @lassoan (2021-04-26 04:25 UTC)

<p><code>CenteredJumpSlice</code> options works. You can also use this static method of <code>vtkMRMLSliceNode</code>:</p>
<pre><code>slicer.vtkMRMLSliceNode.JumpAllSlices(slicer.mrmlScene, 2.3, 4.5, 6.7, slicer.vtkMRMLSliceNode.CenteredJumpSlice)
</code></pre>
<p>If you also want to move the crosshair position then you can call:</p>
<pre><code class="lang-python">crosshairNode = slicer.vtkMRMLCrosshairDisplayableManager.FindCrosshairNode(slicer.mrmlScene)
crosshairNode.SetCrosshairRAS([2.3, 4.5, 6.7])
</code></pre>

---
