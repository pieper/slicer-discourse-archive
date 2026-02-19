---
topic_id: 4369
title: "Segmentation Problem On Re Opening Files"
date: 2018-10-11
url: https://discourse.slicer.org/t/4369
---

# Segmentation, problem on re-opening files

**Topic ID**: 4369
**Date**: 2018-10-11
**URL**: https://discourse.slicer.org/t/segmentation-problem-on-re-opening-files/4369

---

## Post #1 by @wnzsofia (2018-10-11 20:36 UTC)

<p>Operating system: Windows10<br>
Slicer version: Slicer 4.9.0.<br>
Expected behavior:<br>
Actual behavior: Hi, I was doing segmentations on the liver and have a problem on re-opening files. Right after re-opening files I can roll with mouse between CT slices but after I begin to use Segment editor I could not roll between slices any more so I can not work on that file again. (Segment editor works on that one slide btw.)<br>
What can be the problem?<br>
Thank you!</p>

---

## Post #2 by @lassoan (2018-10-11 20:54 UTC)

<p>Can you scroll between slices if you move the slider at the top of slice view? Can you post a screenshot?</p>

---

## Post #3 by @wnzsofia (2018-10-12 05:51 UTC)

<p>No, the top slider does not work either. Here is the print screen.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a925f8efc95dcc8504ea5a8976ee8250dd3cfa5.jpeg" data-download-href="/uploads/short-url/fcMdl5DLNubNtOOuLrNx62VvLr7.jpeg?dl=1" title="prt%20sc" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a925f8efc95dcc8504ea5a8976ee8250dd3cfa5_2_690x388.jpeg" alt="prt%20sc" data-base62-sha1="fcMdl5DLNubNtOOuLrNx62VvLr7" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a925f8efc95dcc8504ea5a8976ee8250dd3cfa5_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a925f8efc95dcc8504ea5a8976ee8250dd3cfa5_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a925f8efc95dcc8504ea5a8976ee8250dd3cfa5_2_1380x776.jpeg 2x" data-dominant-color="84848B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">prt%20sc</span><span class="informations">1920×1080 283 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @cpinter (2018-10-12 13:32 UTC)

<p>The data probe (bottom left) says “no image” , and the sliders are stuck on the left side with no apparent range, so something is wrong with the volume display. Could you send an MRB to us? Click save, then click on the gift-looking icon.</p>

---

## Post #5 by @lassoan (2018-10-12 14:09 UTC)

<p>She showed this to me on Skype and you were right, the volume was invalid (did not contain any image data) due to some scene saving issues. There was a valid volume in the scene and that was shown in the viewers, but when she switched to Segment Editor, the segmentation master volume was set as background volume, which was the invalid volume.</p>
<p>We should fix the slice view pipeline so that if an invalid volume is selected (that has no image data) then a blank slice is displayed (currently the previously selected volume remains displayed).</p>

---

## Post #6 by @pieper (2018-10-12 16:02 UTC)

<p>Agreed - the case of an empty image data in a volume node is not handled well currently.  I’d always thought is should display a faint grid or something and maybe text that says ‘no image data’.</p>

---
