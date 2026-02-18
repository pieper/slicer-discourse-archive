# Segmentation threshold effect question

**Topic ID**: 10677
**Date**: 2020-03-13
**URL**: https://discourse.slicer.org/t/segmentation-threshold-effect-question/10677

---

## Post #1 by @rprueckl (2020-03-13 16:53 UTC)

<p>I have a question regarding the threshold functionality in the Segment Editor (Using build Slicer 4.11.0-2020-03-10).<br>
I do the following:</p>
<ul>
<li>Load scalar volume</li>
<li>Use the volume as master for segmentation</li>
<li>Add one segment</li>
<li>Modify segment (e.g. with the Paint effect)</li>
<li>Add a second segment</li>
<li>For the second segment, I want to apply thresholding.</li>
<li>I set a threshold and apply</li>
</ul>
<p>The second segment now correctly contains the areas identified by the thresholding process.<br>
Voxels of the first segment, however, are cleared at positions that are contained in the second segment. In other words, the threshold operation for the second segment “destroyed” my first segment. I guess this has to do with labelmaps shared between segments.</p>
<p>The behavior is not what I expected, and I would rather suspect a bug here. As the thresholding functionality is supposed to be widely used, however, I find it hard to believe that this hasn’t been observed before. So if this is working as intended, I would be happy about an explanation of this behavior.</p>
<p>Thanks.</p>

---

## Post #2 by @Sunderlandkyl (2020-03-13 16:57 UTC)

<p>By default modifying a segment will overwrite all segments underneath the modified area. If you don’t want to overwrite, you can change the “Modify other segments” setting in the Masking section of the segment editor to “Allow overlap”:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8fa20a596131cb01c61c0ee09e101967f294119.png" alt="image" data-base62-sha1="o6Q6RSiCVRAaQQddtcO4y7AJDx7" width="583" height="154"></p>

---

## Post #3 by @rprueckl (2020-03-13 17:05 UTC)

<p>I see, this makes sense. Thanks a lot for the quick explanation.</p>

---

## Post #4 by @Sunderlandkyl (2020-03-13 17:18 UTC)

<p>If you don’t want to overlap the segments, and would just like to modify the region outside of the first segment, you can also look at the “Editable area” setting.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bb90dbd0618db15d8bfca36e0de003ced4fabb6.png" alt="image" data-base62-sha1="mdAtYQ8S1WxqLmrsSa3i96BF8xg" width="584" height="149"></p>

---
