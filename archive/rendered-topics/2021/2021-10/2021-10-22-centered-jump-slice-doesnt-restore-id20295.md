# Centered Jump Slice doesn't restore

**Topic ID**: 20295
**Date**: 2021-10-22
**URL**: https://discourse.slicer.org/t/centered-jump-slice-doesnt-restore/20295

---

## Post #1 by @hherhold (2021-10-22 01:20 UTC)

<p>I have a scene file that I’ve switched to use Centered Jump Slice crosshair behavior. But when I save the file, quit slicer, restart slicer, and open the file, the Centered Jump Slice behavior isn’t restored, and I get the following error:</p>
<pre><code>Failed to read #xmlAttributeName attribute value from string 'CenteredJumpSlice'
</code></pre>
<p>I looked through the code to see if it should be “Centered Jump Slice” instead of “CenteredJumpSlice” but didn’t see anything obvious… Any ideas?</p>
<p>Thanks!!!</p>

---

## Post #2 by @hherhold (2021-10-22 01:27 UTC)

<p>I did also notice this while grepping through the code:</p>
<pre><code>Libs/MRML/Core/vtkMRMLCrosshairNode.h:      CenteredJumpSlice = 2,
Libs/MRML/Core/vtkMRMLSliceNode.h:  enum {DefaultJumpSlice=-1, CenteredJumpSlice=0, OffsetJumpSlice};
</code></pre>
<p>Shouldn’t matter, because these are in different name spaces (different classes)?</p>

---

## Post #3 by @lassoan (2021-10-22 15:15 UTC)

<p>Thank you good catch, it was just a side effect of some line reordering. I’ll push a fix today.</p>

---

## Post #4 by @hherhold (2021-10-22 15:16 UTC)

<p>Awesome, thanks again!</p>

---
