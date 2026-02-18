# Loaded .dcm, Segment Editor, Threshold Range flashes continuously when selected

**Topic ID**: 3142
**Date**: 2018-06-12
**URL**: https://discourse.slicer.org/t/loaded-dcm-segment-editor-threshold-range-flashes-continuously-when-selected/3142

---

## Post #1 by @Seth (2018-06-12 01:17 UTC)

<p>Greetings,</p>
<p>I’m using the latest stable version - 4.8.1</p>
<p>I’m relatively new but think this maybe a bug.  I’m using a MacBook with macOS High Sierra v10.13.5</p>
<p>I can load dicom files (.dcm) and view axial, coronal, sagittal fine.  The issue is when I am in the Segment Editor, and create a segmentation.  On the effects window below, it has ‘Threshold’.  I’ve used tools like this before but when I try it with this - the image will refresh with min -&gt; max - going back and forth.  It isn’t static based on the threshold inputted.  It’s continuously cycling, revolving, flashing, etc.  I’ve tried everything, installed earlier and newer versions, restarted, etc.</p>
<p>When I click ‘apply’ and exit from the threshold tool, it’ll stop.  But it’s difficult to determine the actual threshold it’s picking up because it’s continuously cycling through flashing when I’m in the threshold tool.</p>
<p>I can post a video but thought maybe it’s a known bug/issue that can be worked around / fixed.</p>
<p>Any help or input appreciated!<br>
Thanks</p>

---

## Post #2 by @lassoan (2018-06-12 02:02 UTC)

<aside class="quote no-group" data-username="Seth" data-post="1" data-topic="3142">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f14d63/48.png" class="avatar"> Seth:</div>
<blockquote>
<p>It’s continuously cycling, revolving, flashing</p>
</blockquote>
</aside>
<p>That’s a great feature that nobody has ever complained about. It makes it very clear what is inside the selected region while also allowing seeing the original image.</p>
<p>It may help us understand your problem if you send a video about what you see and mark where you have trouble seeing boundaries of the selected area or the underlying image.</p>

---

## Post #3 by @Seth (2018-06-12 02:12 UTC)

<p>Yes - I wasn’t used to the flashing of opacity.  To the un-initiated it looks sort of like it’s cycling through the thresholds instead of just opacity.</p>
<p>It’s alright now that I know what it’s doing.  You can lock or delete this post.</p>
<p>Thanks for the quick reply- soon as I posted, I realized what it was doing!</p>

---
