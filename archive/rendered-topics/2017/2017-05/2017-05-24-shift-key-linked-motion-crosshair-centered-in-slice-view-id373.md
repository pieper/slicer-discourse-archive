# Shift key linked motion - crosshair centered in slice view

**Topic ID**: 373
**Date**: 2017-05-24
**URL**: https://discourse.slicer.org/t/shift-key-linked-motion-crosshair-centered-in-slice-view/373

---

## Post #1 by @hherhold (2017-05-24 15:23 UTC)

<p>I often use the shift key to jump to the same stack position in all views, but if I’m zoomed in on one or more views, the slice does not translate to the same point. Is there a way to do this? Meaning, it should center the point in all views, not just jump the slice to the point.</p>
<p>Hope this makes sense…</p>
<p>Thanks in advance!</p>
<p>-Hollister</p>

---

## Post #2 by @pieper (2017-05-24 17:24 UTC)

<p>The SliceNode <a href="https://github.com/Slicer/Slicer/blob/6d1f4bb820d02c86c865517d7524f3641836ccf4/Libs/MRML/Core/vtkMRMLSliceNode.h#L356-L374">supports this</a> but it looks like it’s not used in <a href="https://github.com/Slicer/Slicer/blob/84f11249053c6da1c4f3abcb3edd9d20d226ef44/Libs/MRML/DisplayableManager/vtkSliceViewInteractorStyle.cxx#L543-L556">the InteractorStyle</a>.  It seems like we could add a setting for this.</p>
<hr>

---

## Post #3 by @lassoan (2017-05-24 17:36 UTC)

<p>I agree it can be useful sometimes, and it should be easy to implement. I’ll have a look.</p>

---

## Post #4 by @lassoan (2017-05-24 19:16 UTC)

<p>I’ve added a centered slice jump option for crosshair behavior. It’ll be available in the Crosshair menu in tomorrow’s nightly version.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e828b70ab409dbd33d1ea0adb9554c8efa71162.png" alt="image" data-base62-sha1="fLCdaFAHbX839wxkWMsAZ8pIZ46" width="300" height="229"></p>

---

## Post #5 by @pieper (2017-05-24 20:38 UTC)

<p>Just tried this in my local build and it’s great!</p>

---

## Post #6 by @hherhold (2017-05-24 22:03 UTC)

<p>Me too - this is fantastic! I can’t even guess how much time this is going to save me.</p>
<p>Thank you very much!!</p>
<p>-Hollister</p>

---

## Post #7 by @Fernando (2018-06-22 15:37 UTC)

<p>FYI a clinician just asked me if this feature was available in Slicer, so thanks again!</p>

---

## Post #8 by @lassoan (2023-03-21 02:59 UTC)



---
