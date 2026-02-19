---
topic_id: 33199
title: "Grow From Seeds Limit To Some Segmentations No Overlap"
date: 2023-12-04
url: https://discourse.slicer.org/t/33199
---

# Grow from seeds - limit to some segmentations, no overlap

**Topic ID**: 33199
**Date**: 2023-12-04
**URL**: https://discourse.slicer.org/t/grow-from-seeds-limit-to-some-segmentations-no-overlap/33199

---

## Post #1 by @Tomasz_Bartczak (2023-12-04 12:33 UTC)

<p>Hello.</p>
<p>I’ve been using ‘grow from seeds’ successfully for some cases. I do understand it requires at least two segments to run (foreground + background).<br>
However I have a case, where I would like to use a 3rd segmentation as an additional boundary for the segmentation.</p>
<p>The context is that I have Left Atrium that is segmented to some extent and I would like to expand it to cover more of PV. So I load the initial segmentation, put some seeds in the uncovered part of the organ, draw some background and…</p>
<p>Now I would like to run ‘grow from seeds’ only on those two new segments, with the setting ‘editable area’ == outside all visible segments.<br>
But this is as well growing my initial segmentation, and I don’t want it, because it is not a good source of seeds, it has some over-segmentations here and there.</p>
<p>I managed to move the original segmentation to another segmentation node, which excludes it from being used in ‘grow from seeds’. Is there another way to achieve that?</p>
<p>However - as one can see on the screenshot it didn’t fully stop at my other segmentation - they do overlap:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/4949fd843a7a7c15a759049df63763b6e9565ebe.png" alt="image" data-base62-sha1="aslnud5XD682JyAmOk9he7GMYDs" width="504" height="257"></p>
<p>I understand I can now run other operations to get what I need, I just wonder if this the best way I’m doing it?</p>

---

## Post #2 by @rbumm (2023-12-04 14:31 UTC)

<p>You can only make autoupdates to your grow from seed process if you have saved it in a “non-applied” state before.<br>
As soon as you “Apply” changes via Grow from seeds changes to the original are not possible.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52b48182f3b1934e6a62af466e12ff463acdc8cf.jpeg" data-download-href="/uploads/short-url/bNDSQLdE9rVgTKYWBvaXCVRK9kj.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52b48182f3b1934e6a62af466e12ff463acdc8cf_2_690x286.jpeg" alt="image" data-base62-sha1="bNDSQLdE9rVgTKYWBvaXCVRK9kj" width="690" height="286" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52b48182f3b1934e6a62af466e12ff463acdc8cf_2_690x286.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52b48182f3b1934e6a62af466e12ff463acdc8cf_2_1035x429.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52b48182f3b1934e6a62af466e12ff463acdc8cf.jpeg 2x" data-dominant-color="7C8683"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1153×479 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Tomasz_Bartczak (2023-12-05 07:18 UTC)

<p>Yes, I get the difference between ‘unsaved’ and ‘saved’ state of ‘grow from seeds’.</p>
<p>My concern here was that even though I selected ‘editable area’ == ‘outside all visible segments.’ → the growed segmentation overlapped with another visible segment, and this is something I don’t want.</p>

---
