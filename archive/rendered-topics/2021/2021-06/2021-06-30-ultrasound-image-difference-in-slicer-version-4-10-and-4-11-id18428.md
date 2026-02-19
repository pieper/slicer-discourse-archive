---
topic_id: 18428
title: "Ultrasound Image Difference In Slicer Version 4 10 And 4 11"
date: 2021-06-30
url: https://discourse.slicer.org/t/18428
---

# Ultrasound image difference in Slicer version 4.10 and 4.11

**Topic ID**: 18428
**Date**: 2021-06-30
**URL**: https://discourse.slicer.org/t/ultrasound-image-difference-in-slicer-version-4-10-and-4-11/18428

---

## Post #1 by @Marijn_H (2021-06-30 12:14 UTC)

<p>Hi,</p>
<p>I am using slicerIGT with plusserver to load tracked ultrasound images into 3D Slicer. We use the BK ultrasound system. On Slicer version 4.10, this worked fine and the ultrasound image is displayed like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75d8e9b67c4b9ba31246058bcd11c9a52fc89594.png" data-download-href="/uploads/short-url/gOwB4eiHcIOCXSvwcD9CZSfnx1q.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75d8e9b67c4b9ba31246058bcd11c9a52fc89594_2_489x375.png" alt="image" data-base62-sha1="gOwB4eiHcIOCXSvwcD9CZSfnx1q" width="489" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75d8e9b67c4b9ba31246058bcd11c9a52fc89594_2_489x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75d8e9b67c4b9ba31246058bcd11c9a52fc89594_2_733x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75d8e9b67c4b9ba31246058bcd11c9a52fc89594_2_978x750.png 2x" data-dominant-color="6D6969"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1042×799 76.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now we want to update our setup to Slicer version 4.11, but something seems to go wrong with the orientation of the image. The origin of the ultrasound image (top left corner) is displayed at the center of the red slice field of view, which looks like this (after automatic field of view selection):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/762e13b9c0a27c1a2d605e801f4b01bb7a7f824f.png" data-download-href="/uploads/short-url/gRt3N2k1gerBroQQzwHgSVmprwH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/762e13b9c0a27c1a2d605e801f4b01bb7a7f824f_2_487x375.png" alt="image" data-base62-sha1="gRt3N2k1gerBroQQzwHgSVmprwH" width="487" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/762e13b9c0a27c1a2d605e801f4b01bb7a7f824f_2_487x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/762e13b9c0a27c1a2d605e801f4b01bb7a7f824f_2_730x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/762e13b9c0a27c1a2d605e801f4b01bb7a7f824f_2_974x750.png 2x" data-dominant-color="221F1F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1035×795 21.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>We did not change anything in the plus config file or transformations. Could you solve this problem to visualize the ultrasound image correctly in Slicer 4.11?</p>

---

## Post #2 by @lassoan (2021-07-02 03:38 UTC)

<p>Does clicking on the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">“Reset field of view” button</a> fix the issue?</p>
<p>If not, can you save an example scene (in .mrb format), upload it somewhere, and post the link here so that we can have a look?</p>

---

## Post #3 by @Marijn_H (2021-07-05 08:55 UTC)

<p>Thanks for your response! Reset the field of view button did not work.</p>
<p>Here is the uploaded scene: <a href="https://ufile.io/25tlqpo3" class="inline-onebox" rel="noopener nofollow ugc">Upload files for free - 2021-07-05-Scene.mrb - ufile.io</a></p>
<p>However, when opening this scene, the view of the ultrasound image is correct. But when connecting to the real time ultrasound device through openIGTlink, the image view shifts.<br>
It seems like there is a shift of the origin, since the (0,0) coordinate is in the top left corner of the red slice and the supposed origin of the ultrasound image is at the center of the red slice:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1da102a081d96a1bc0c38b180105662e9548c2a2.png" data-download-href="/uploads/short-url/4e6ObRuhase1nLO5h4marazYEKe.png?dl=1" title="US Slicer 4.11 coordinates" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1da102a081d96a1bc0c38b180105662e9548c2a2_2_650x500.png" alt="US Slicer 4.11 coordinates" data-base62-sha1="4e6ObRuhase1nLO5h4marazYEKe" width="650" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1da102a081d96a1bc0c38b180105662e9548c2a2_2_650x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1da102a081d96a1bc0c38b180105662e9548c2a2_2_975x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1da102a081d96a1bc0c38b180105662e9548c2a2.png 2x" data-dominant-color="231F1F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">US Slicer 4.11 coordinates</span><span class="informations">1035×795 23.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you know what could be causing this problem and how I could fix it?</p>

---

## Post #4 by @lassoan (2021-07-17 23:04 UTC)

<p>I cannot reproduce the behavior that you describe. For me, the image appears in the center by default. But it should not be an issue if the image does not fill the view or not centered by default, because you can always center it by clicking the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">“Reset field of view” button</a> or if you use a Python code snippet to set up the scene then you can add <code>slicer.util.setSliceViewerLayers(fit=True)</code>.</p>

---
