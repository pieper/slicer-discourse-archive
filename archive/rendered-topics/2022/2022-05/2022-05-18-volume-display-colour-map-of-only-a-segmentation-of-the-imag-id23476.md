---
topic_id: 23476
title: "Volume Display Colour Map Of Only A Segmentation Of The Imag"
date: 2022-05-18
url: https://discourse.slicer.org/t/23476
---

# Volume display colour map of only a segmentation of the image

**Topic ID**: 23476
**Date**: 2022-05-18
**URL**: https://discourse.slicer.org/t/volume-display-colour-map-of-only-a-segmentation-of-the-image/23476

---

## Post #1 by @Jacchevalier (2022-05-18 20:01 UTC)

<p>Hi guys,<br>
I’m trying to create this heat map but only within the segmentation and the remaining image to be a greyscale CT as usual. Any suggestions?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e46f09002b0d9c935cdf443fa311fd2e37b8c99e.png" data-download-href="/uploads/short-url/wAOKObYhNGZH01ASKLgGGBK5IhU.png?dl=1" title="Screen Shot 2022-05-18 at 3.58.19 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e46f09002b0d9c935cdf443fa311fd2e37b8c99e.png" alt="Screen Shot 2022-05-18 at 3.58.19 PM" data-base62-sha1="wAOKObYhNGZH01ASKLgGGBK5IhU" width="618" height="500" data-dominant-color="722015"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-05-18 at 3.58.19 PM</span><span class="informations">668×540 75.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2022-05-18 20:12 UTC)

<p>One way would be to use the Mask Volume effect in the Segment Editor to make a version with just the segmented region, apply the color map to the new volume, and put it in the Foreground layer in the slice viewers with a threshold that makes all the Background show everywhere else.</p>

---

## Post #3 by @Jacchevalier (2022-05-18 20:25 UTC)

<p>Thank you so much! the only part I’m not having success with is moving it to the foreground… how would i do that?</p>

---

## Post #4 by @pieper (2022-05-18 20:28 UTC)

<p>You can use the volume selectors in the view controller and the Foreground volume opacity slider.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view</a></p>
<p>Good luck!</p>

---
