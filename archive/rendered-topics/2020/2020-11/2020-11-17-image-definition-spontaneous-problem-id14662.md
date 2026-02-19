---
topic_id: 14662
title: "Image Definition Spontaneous Problem"
date: 2020-11-17
url: https://discourse.slicer.org/t/14662
---

# Image definition spontaneous problem! 

**Topic ID**: 14662
**Date**: 2020-11-17
**URL**: https://discourse.slicer.org/t/image-definition-spontaneous-problem/14662

---

## Post #1 by @hernandez42 (2020-11-17 14:13 UTC)

<p>Hi everybody!<br>
This problem happened spontaneously, I did not change any setting of 3D Slicer so I can not get around why I am having this issue! So, any help will be more than welcome!<br>
I am working with .nii.gz files (rats skulls scans, for a landmarking project) and instead of a clear image I got a blurry/grey image (attached photos). Any of you got this problem before?<br>
I ask one of our IT department to check the computer for any potential hardware issue and he told me that everything is ok.</p>
<p>Thanks in advance!</p>
<p>Yen</p>
<p>Suddenly the program is not uploading the images properly,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de0f5c597be563bf382bcf6f906b5eb6b00634c4.jpeg" data-download-href="/uploads/short-url/vGqUkWw4A6p6hdw1xO7RDiPbMhe.jpeg?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de0f5c597be563bf382bcf6f906b5eb6b00634c4_2_690x487.jpeg" alt="Untitled" data-base62-sha1="vGqUkWw4A6p6hdw1xO7RDiPbMhe" width="690" height="487" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de0f5c597be563bf382bcf6f906b5eb6b00634c4_2_690x487.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de0f5c597be563bf382bcf6f906b5eb6b00634c4.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de0f5c597be563bf382bcf6f906b5eb6b00634c4.jpeg 2x" data-dominant-color="A49CB9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">979×691 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0f499c244534e25cdfbf75c698d2962b7c35328.jpeg" data-download-href="/uploads/short-url/tOvmPC5Il4QZzpseAiui2ebsUrK.jpeg?dl=1" title="Untitled2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0f499c244534e25cdfbf75c698d2962b7c35328_2_690x494.jpeg" alt="Untitled2" data-base62-sha1="tOvmPC5Il4QZzpseAiui2ebsUrK" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0f499c244534e25cdfbf75c698d2962b7c35328_2_690x494.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0f499c244534e25cdfbf75c698d2962b7c35328_2_1035x741.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0f499c244534e25cdfbf75c698d2962b7c35328.jpeg 2x" data-dominant-color="C4BFD0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled2</span><span class="informations">1205×863 209 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2020-11-17 18:16 UTC)

<p>It looks like it’s stuck in a low-quality preview mode somehow.  Can you toggle to GPU rendering?  Otherwise try toggling a few of the setting in the Advanced tab.</p>

---

## Post #3 by @lassoan (2020-11-17 20:49 UTC)

<p>Also make sure to use at least the latest Slicer Stable Release.</p>
<p>There is a bug in CPU/GPU volume rendering switching Iatest stable (causing a crash), so if you want to switch between CPU/GPU rendering then use the latest Slicer Preview Release where this issue has been already fixed.</p>

---

## Post #4 by @lassoan (2020-11-19 03:15 UTC)

<p>You can also try different presets, enable/disable depth peeling (in 3D view controller), and edit transfer functions to get better rendering results.</p>

---

## Post #5 by @hernandez42 (2020-11-19 06:07 UTC)

<p>Hi Steve! Thanks a lot for your reply and suggestion! I will try it today! Have a nice day!</p>

---

## Post #6 by @hernandez42 (2020-11-19 06:09 UTC)

<p>Hi Andras! Thanks a lot for your reply and your suggestions!<br>
I have the last release installed.<br>
I will try it your recommendations today!</p>
<p>Have a nice day!</p>

---

## Post #7 by @hernandez42 (2020-11-19 13:04 UTC)

<p>Hi Steve and Andras!<br>
THANKS A LOT FOR HELPING ME! !<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/024bd7f3c08a275452f3b8530d19f49b0ffac6b7.jpeg" data-download-href="/uploads/short-url/kjrQ3kVXPlvavtIIab57ZwwijR.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/024bd7f3c08a275452f3b8530d19f49b0ffac6b7_2_690x436.jpeg" alt="Screenshot" data-base62-sha1="kjrQ3kVXPlvavtIIab57ZwwijR" width="690" height="436" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/024bd7f3c08a275452f3b8530d19f49b0ffac6b7_2_690x436.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/024bd7f3c08a275452f3b8530d19f49b0ffac6b7_2_1035x654.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/024bd7f3c08a275452f3b8530d19f49b0ffac6b7_2_1380x872.jpeg 2x" data-dominant-color="A09BBF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1438×909 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Now I can re-start my landmarking work <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
Wish you all a nice day!</p>
<p>Yen</p>

---
