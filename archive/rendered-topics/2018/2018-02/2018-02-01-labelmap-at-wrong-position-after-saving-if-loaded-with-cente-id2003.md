---
topic_id: 2003
title: "Labelmap At Wrong Position After Saving If Loaded With Cente"
date: 2018-02-01
url: https://discourse.slicer.org/t/2003
---

# Labelmap at wrong position after saving if loaded with Centered option

**Topic ID**: 2003
**Date**: 2018-02-01
**URL**: https://discourse.slicer.org/t/labelmap-at-wrong-position-after-saving-if-loaded-with-centered-option/2003

---

## Post #1 by @BenFux (2018-02-01 20:34 UTC)

<p>Hi I would like to mark a lesion within a structural mri image and save it as a nifti file.<br>
Therefore I click “rotate to volume plane” in the axial, sagittal and coronal view. Then I click on the editor to create a labelmap. In the option “Volumes” I make sure that the original image and the label map have the same origin. I then use the draw effect of the editor to color out the lesion region, slice by slice pixel by pixel.<br>
Now I click save, select only the labelmap and change its format to nifti.</p>
<p>When I overlay the so created labelmap-nifti with the orignal image with the program Mricron the position of the lesion is shifted. What might be the reason for that? Thx in advance</p>

---

## Post #2 by @pieper (2018-02-01 20:52 UTC)

<p>Are you using the (legacy) Editor or the newer Segment Editor?</p>
<p>Maybe you can provide a screenshot to clarify what’s going on.</p>

---

## Post #3 by @BenFux (2018-02-02 15:02 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02d70d257f752305189c1c1dfd0e2418087fb453.jpeg" data-download-href="/uploads/short-url/p7Hq6N3EVgm1pLPQTDNBYaDUQP.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02d70d257f752305189c1c1dfd0e2418087fb453_2_690x388.jpg" alt="image" data-base62-sha1="p7Hq6N3EVgm1pLPQTDNBYaDUQP" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02d70d257f752305189c1c1dfd0e2418087fb453_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02d70d257f752305189c1c1dfd0e2418087fb453_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02d70d257f752305189c1c1dfd0e2418087fb453_2_1380x776.jpg 2x" data-dominant-color="9E9FA1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 400 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I used the (legacy)Editor to really draw pixel by pixel the small area of the lesion.</p>
<p>I saved the drawing as nifti.</p>
<p>the screenshot shows the overlay of the two niftis, the original and my drawing, but the position of my drawing relative to the original has shifted, it’s not where the lesion was but higher up. The blue double arrow shows, where I had drawn it originally.</p>

---

## Post #4 by @fedorov (2018-02-02 21:41 UTC)

<p>You didn’t check “Centered” on loading the data, or in the Volumes module, for either volume or label, right?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f3affab8a75f5467332c5e94fc65769c8afa0e3.png" alt="image" data-base62-sha1="dArLmeuULJQYj0DwapqBOO1lIFt" width="584" height="283"></p>

---

## Post #5 by @pieper (2018-02-02 22:57 UTC)

<p>Thanks for the screenshot <a class="mention" href="/u/benfux">@BenFux</a> - unfortunately I still don’t know what’s going on.</p>
<p>Are you able to reproduce this with a defined series of steps?  If so and you can share the sample data I’d be interested to see if we can debug this.</p>

---

## Post #6 by @BenFux (2018-02-03 15:00 UTC)

<p>Hi thank you I now know the problem: I didn’t realize that orientation and origin are saved with the image!</p>
<p>The goal was: given a T1 nifti file of a brain with a lesion, I wanted a second nifti of same size, resolution and orientation with only the lesion marked (binary mask).</p>
<p>Mistake: I applied “Center Volume” and “rotate into volume plane” to the original image to draw my lesion mask (aka “label map”), but then saved ONLY the label map, not the original. So then the original kept its old image origin and orientation and didn’t overlap properly with the new labelmap.</p>
<p>So when using “center Volume” or “rotate to volume plane” for drawing a label map, the original needs to be saved as well to have the same origin and orientation as the labelmap. Retrospectively obvious!<br>
Thank you for your help!</p>

---
