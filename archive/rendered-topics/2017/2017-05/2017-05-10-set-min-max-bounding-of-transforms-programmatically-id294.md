# Set min/max bounding of transforms programmatically

**Topic ID**: 294
**Date**: 2017-05-10
**URL**: https://discourse.slicer.org/t/set-min-max-bounding-of-transforms-programmatically/294

---

## Post #1 by @mangotee (2017-05-10 17:25 UTC)

<p>Hi all,</p>
<p>I am trying to manipulate the entries of a transform (vtkMRMLLinearTransformNode) in Slicer programmatically, specifically, I’d like to set the translation part to a value larger than 200 (or smaller than -200).<br>
Unfortunately, the bounding between [-200,200] in the transforms module prohibits that and it gets capped to 200.<br>
How can I set these bounds to a higher value?<br>
I couldn’t find an approriate “Set” method in the function of the vtkMRMLLinearTransformNode, so I assume this must be done in the module’s logic? I couldn’t find an appropriate function in slicer.modules.transforms.logic() either though…<br>
A bit lost here… <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=5" title=":confused:" class="emoji" alt=":confused:"> any help is appreciated.</p>
<p>Thanks and Cheers,<br>
Ahmad</p>

---

## Post #2 by @lassoan (2017-05-10 17:26 UTC)

<p>You should be able to set any values in a transform, regardless of how the display of values are set up in the Transforms module.</p>
<p>A related problem was fixed a couple of months ago in the trunk. Could you try if you still have the problem in the latest nightly version?</p>

---

## Post #3 by @mangotee (2017-05-11 07:20 UTC)

<p>Dear Andras,<br>
you were right - I was still using Slicer 4.5.0-1, I switched to 4.6.2 and this problem does not occur anymore - the min/max bounds are extended automatically.<br>
Thanks a lot!<br>
Cheers,A</p>

---
