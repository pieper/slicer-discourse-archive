---
topic_id: 42950
title: "Identify Hu Range For Air On Ct Image"
date: 2025-05-15
url: https://discourse.slicer.org/t/42950
---

# Identify HU range for Air on CT image

**Topic ID**: 42950
**Date**: 2025-05-15
**URL**: https://discourse.slicer.org/t/identify-hu-range-for-air-on-ct-image/42950

---

## Post #1 by @imbeatriz (2025-05-15 17:05 UTC)

<p>Hi everyone,</p>
<p>I used TotalSegmentator on a CT image, and it successfully segmented all relevant structures. However, I noticed that it does not include a specific label for air that I need.</p>
<p>I need to determine the HU range—minimum and maximum voxel values—that correspond to air in the original CT image. Could anyone please explain how I can extract or visualize this information using 3D Slicer?</p>
<p>Any guidance would be greatly appreciated.</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2025-05-16 12:27 UTC)

<p>Air is usually -1000 (<a href="https://en.wikipedia.org/wiki/Hounsfield_scale" class="inline-onebox">Hounsfield scale - Wikipedia</a>) and you can segment with simple thresholding.  But if you are inside the body be aware there’s a lot of partial volume effects (a voxel has air and tissue) so it can be challenging to get an exact volume.</p>

---

## Post #3 by @imbeatriz (2025-05-16 16:35 UTC)

<p>Hi,</p>
<p>Thank you for your help! I have another question — do you happen to know how I can assign labels to different segments (obtained from the Total Segmentator tool) and save them together in a single .mhd file? Is that possible?</p>
<p>I’d really appreciate any guidance on how to do this properly.</p>

---

## Post #4 by @pieper (2025-05-17 13:27 UTC)

<p>I’m not sure what you mean.  It is possible to export selected segments (the visible ones) to a labelmap and then save that in mhd format.  If that’s not what you mean please describe what you are trying to accomplish.</p>

---

## Post #5 by @imbeatriz (2025-05-17 13:37 UTC)

<p>Yeah, I have tried doing that. But the generated file doesn’t save the original name I had for each segmentation. It gives the names like the ones for the label:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/529bd39b23e8b2d91725273e5c62078862f7b9e4.png" data-download-href="/uploads/short-url/bMN0AvxKtAAV2Z5koeFQzhXcgQs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/529bd39b23e8b2d91725273e5c62078862f7b9e4_2_690x395.png" alt="image" data-base62-sha1="bMN0AvxKtAAV2Z5koeFQzhXcgQs" width="690" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/529bd39b23e8b2d91725273e5c62078862f7b9e4_2_690x395.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/529bd39b23e8b2d91725273e5c62078862f7b9e4_2_1035x592.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/529bd39b23e8b2d91725273e5c62078862f7b9e4_2_1380x790.png 2x" data-dominant-color="3B3B36"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1494×857 200 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’d like for each segment to have its original name and then the label number if possible.</p>

---

## Post #6 by @pieper (2025-05-17 13:45 UTC)

<p>You can use a color table for that.  <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html</a></p>

---

## Post #7 by @imbeatriz (2025-05-17 15:01 UTC)

<p>I followed the steps and exported the segmentation in the format I wanted. However, when I load the file back into 3D Slicer, the segment names aren’t preserved—it behaves the same way as before, without showing the original segment names.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b7c29b8333b7d0f24537eb7a43220962e272fec.jpeg" data-download-href="/uploads/short-url/hCoKiG9QeaONDieMA8uOdUcbvME.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b7c29b8333b7d0f24537eb7a43220962e272fec_2_275x500.jpeg" alt="image" data-base62-sha1="hCoKiG9QeaONDieMA8uOdUcbvME" width="275" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b7c29b8333b7d0f24537eb7a43220962e272fec_2_275x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b7c29b8333b7d0f24537eb7a43220962e272fec_2_412x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b7c29b8333b7d0f24537eb7a43220962e272fec.jpeg 2x" data-dominant-color="3A3939"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">431×782 83 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Am I selecting something wrong?</p>
<p>I saw that when I go to the data and select segmentsss-label, I am able to see how I want the name next to the label. It’s when I save the file and reopen it separately that the name disappears, so I am confused why this happens.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f116928e5176d8585d64432138a570a8280218e.png" data-download-href="/uploads/short-url/bht1oPRsS4npvNCOsJr5WHBUhWe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f116928e5176d8585d64432138a570a8280218e_2_547x500.png" alt="image" data-base62-sha1="bht1oPRsS4npvNCOsJr5WHBUhWe" width="547" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f116928e5176d8585d64432138a570a8280218e_2_547x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f116928e5176d8585d64432138a570a8280218e_2_820x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f116928e5176d8585d64432138a570a8280218e.png 2x" data-dominant-color="36302B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">872×796 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @jamesobutler (2025-05-17 15:10 UTC)

<p>A segmentation node which contains segments (as produced by say TotalSegmentator) by default can be saved to a .seg.nrrd file format which saves the entire segmentation node (with all the segments) and that can be reloaded back into Slicer with the segment names you specified.</p>

---

## Post #9 by @imbeatriz (2025-05-17 15:24 UTC)

<p>Yes, I’m aware of that, but the issue is that it doesn’t show the label values for each segment—such as the liver, which I specifically need. What I am trying to do   is to create a map where I can define which label value corresponds to which anatomical structure (e.g., label value 3 = liver, etc.).</p>

---

## Post #10 by @pieper (2025-05-17 19:18 UTC)

<p>You can also specify a color table when you load the data <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#load-data">https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#load-data</a></p>

---

## Post #11 by @imbeatriz (2025-05-18 13:24 UTC)

<p>Hi, I did that and created a Python code that gave me the labels identified with the segmentation’s name. Thank you!</p>

---
