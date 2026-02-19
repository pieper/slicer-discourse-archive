---
topic_id: 6141
title: "Sub Mri Merging For Segmentation"
date: 2019-03-14
url: https://discourse.slicer.org/t/6141
---

# sub-MRI merging for segmentation

**Topic ID**: 6141
**Date**: 2019-03-14
**URL**: https://discourse.slicer.org/t/sub-mri-merging-for-segmentation/6141

---

## Post #1 by @David_M (2019-03-14 10:35 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.1<br>
Expected behavior: merging of multiple MRI images<br>
Actual behavior: no documentation found to help me to understand how to do it</p>
<p>I would like to merge multiple sub-MRI images (3 parts of an arm) in one bigger file, in order to make segmentation and model of the entire arm, and then resample them, to make the intersection smoother.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/923a030d3148adf21a1749493959704d29469292.png" data-download-href="/uploads/short-url/kRA02vabwMcBldVeqwYvo3avCls.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/923a030d3148adf21a1749493959704d29469292_2_690x254.png" alt="image" data-base62-sha1="kRA02vabwMcBldVeqwYvo3avCls" width="690" height="254" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/923a030d3148adf21a1749493959704d29469292_2_690x254.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/923a030d3148adf21a1749493959704d29469292.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/923a030d3148adf21a1749493959704d29469292.png 2x" data-dominant-color="9D9BC4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">871×321 93.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I read a few comments on the forum that it is possible. But, maybe because I am not an expert of Slicer, to do this is not easy for me.</p>
<p>I would really appreciate if someone could give me hints or a tutorial/documentation link that could help me to do it. I tried to follow the suggestion in the comments of someone who already got this problem, but to me, they were not too clear. Moreover, I am doing a lot of registration tutorials, but unfortunately they are not really helpful.</p>
<p>Thanks a lot</p>

---

## Post #2 by @pieper (2019-03-14 13:17 UTC)

<p>One approach would be to use the CropVolume module to make a volume big enough to hold all three volumes (e.g. use the hand volume and then extend the ROI to include the other volumes.  Then use Add Volumes to sequentially add the other two subvolumes into the new big volume.  If things don’t quite line up, e.g. due to patient motion, you could apply transforms and to the subvolumes before adding them.</p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @David_M (2019-03-14 18:32 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="6141">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>apply transforms and to the subvolume</p>
</blockquote>
</aside>
<p>Thank so much! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> yes i did it finally using</p>
<ol>
<li>Landmark registration in order to align them</li>
<li>Crop Volume  to make a large ROI (my mistake was that I resize the ROI of just one of the 2 volumes)</li>
<li>Add scalar volume to mix them</li>
</ol>

---
