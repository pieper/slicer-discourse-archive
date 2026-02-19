---
topic_id: 22709
title: "Proposition To Preserve Slice View Aspect Ratio When Resizin"
date: 2022-03-27
url: https://discourse.slicer.org/t/22709
---

# Proposition to preserve Slice view aspect ratio when resizing the window

**Topic ID**: 22709
**Date**: 2022-03-27
**URL**: https://discourse.slicer.org/t/proposition-to-preserve-slice-view-aspect-ratio-when-resizing-the-window/22709

---

## Post #1 by @keri (2022-03-27 14:41 UTC)

<p>Hi,</p>
<p>In SlicerCAT I add support to modify slice view’s aspect ratio, i.e. the horizontal scaling may not be equal to vertical scaling.</p>
<p>When slice window is resized it calls <a href="https://github.com/Slicer/Slicer/blob/b362a139d35373c6cccfff501c3935c482c52024/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1741" rel="noopener nofollow ugc">vtkMRMLSliceLogic::ResizeSliceNode</a> that modify FOV while resetting the aspect ratio.</p>
<p>For example if I set aspect ratio for slice view 2:1 then after the slice window is resized I get the restored aspect ratio 1:1. If I manually changed the aspect ratio then most likely I don’t want that it was reset after resizing the window.<br>
May we change that so that the aspect ratio stays untouched?<br>
To do so it is enough to delete <a href="https://github.com/Slicer/Slicer/blob/b362a139d35373c6cccfff501c3935c482c52024/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1778-L1783" rel="noopener nofollow ugc">5 lines of code</a> of <code>ResizeSliceNode</code> function.</p>
<p>If the user wants to reset the aspect ratio (to 1:1) then there is a button that resets FOV and aspect ratio:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4effc30a8f13fb7927ec2f73597539eadcc58197.png" alt="image" data-base62-sha1="bgRd1dNc2YHLOtTeyRvEkAOQIon" width="224" height="136"></p>

---

## Post #2 by @pieper (2022-03-27 17:00 UTC)

<p>I’d be very wary of introducing the possibility of accidental distortions for our core medical imaging use cases.  Instead of changing the view, why don’t you use a transformation to compress or expand the data along an axis.  Or you could observe the slice node and set it to the desired aspect ratio any time it’s updated.</p>

---

## Post #3 by @keri (2022-03-27 17:14 UTC)

<p>Thank for response,</p>
<p>Applying transform to every node is much harder as I also use XYZ axes shown at all borders that are represented by axes actors. It is much easier to set FOV.</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="22709">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Or you could observe the slice node and set it to the desired aspect ratio any time it’s updated.</p>
</blockquote>
</aside>
<p>That is possible solution.</p>
<p>Just to clarify: it is completely fine if this proposition will be declined. I can patch this function during SlicerCAT build so it is not a problem for me. I just thought that it would be more intuitive for any Slicer user.</p>

---
