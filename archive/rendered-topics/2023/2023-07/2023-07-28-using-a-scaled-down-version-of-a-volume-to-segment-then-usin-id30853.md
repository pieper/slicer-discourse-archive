---
topic_id: 30853
title: "Using A Scaled Down Version Of A Volume To Segment Then Usin"
date: 2023-07-28
url: https://discourse.slicer.org/t/30853
---

# Using a scaled down version of a volume to segment, then using this segment on original large size volumes

**Topic ID**: 30853
**Date**: 2023-07-28
**URL**: https://discourse.slicer.org/t/using-a-scaled-down-version-of-a-volume-to-segment-then-using-this-segment-on-original-large-size-volumes/30853

---

## Post #1 by @coco (2023-07-28 10:30 UTC)

<p>Dear all,<br>
I have large datasets (10 to 30GB per image) which are thus difficult to segment on original files. One solution I imagined is<br>
1- to use a 10X downscaled  version of my images,<br>
2- paint “seeds” in the 14 regions I want segmented,<br>
3- shrink the sizes of each segment by a couple of voxels,<br>
4- then apply the seg.nrrd file to the original large size image after  and<br>
5- apply a grow from seed function (and go make myself a coffee…).<br>
Everything works well up to step 5. Segments are matching to the new high resolution image but are somewhat fixed to low resolution settings.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a85d30ebe33c4371e69345b757575940e4db8c3.jpeg" data-download-href="/uploads/short-url/cUNGLVNLHSAJ0D2CDZDlbARkjx9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a85d30ebe33c4371e69345b757575940e4db8c3_2_690x388.jpeg" alt="image" data-base62-sha1="cUNGLVNLHSAJ0D2CDZDlbARkjx9" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a85d30ebe33c4371e69345b757575940e4db8c3_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a85d30ebe33c4371e69345b757575940e4db8c3_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a85d30ebe33c4371e69345b757575940e4db8c3_2_1380x776.jpeg 2x" data-dominant-color="8C8F8A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thanks for your help</p>

---

## Post #2 by @coco (2023-07-28 10:46 UTC)

<p>Apologies for posting something I eventually found a solution for.<br>
I needed to edit the Specify Geometry option to oversampling the seg.nrrd file and increase it 10X<br>
I am now running grow from seed the way it is supposed to on high resolution images.<br>
Kind regards (and if moderators feel this is not a useful topic, feel free to delete)</p>

---

## Post #3 by @pieper (2023-07-28 14:17 UTC)

<p>Thanks for posting this - yes, we definitely like to keep this kind of post in the system so that others can learn in the future.</p>

---
