---
topic_id: 34394
title: "Elastix Registration 3D Ct Monomodal Lung"
date: 2024-02-19
url: https://discourse.slicer.org/t/34394
---

# Elastix Registration 3D CT monomodal lung

**Topic ID**: 34394
**Date**: 2024-02-19
**URL**: https://discourse.slicer.org/t/elastix-registration-3d-ct-monomodal-lung/34394

---

## Post #1 by @Alice_Durante (2024-02-19 11:59 UTC)

<p>Hello to all<br>
I’ve been using the toolbox “registration” of 3d Slicer, especially “elastix”. Trying with a registration with “generic (all)” preset I get a discreet result, but not great. My goal is to get the best possible recording of the lungs.<br>
(I am recording 2 CT scans of the same pig before ablation and after ablation, so in two distinct moments). I have questions</p>
<ol>
<li>What is the difference between the various “3D CT, monomodal lung” I have more than one and I do not understand the difference? (I’m always referring to the preset)</li>
<li>Do you have any idea why it is not working? I get an error message. I’m using the same fixed and moving volume of “generic all”, but it doesn’t wok<br>
Thank you</li>
</ol>

---

## Post #2 by @Matteboo (2024-02-19 12:19 UTC)

<p>Hello,</p>
<p>One thing that could work is to segment the lung and to register only the lung if that’s the region of interest in your use case</p>

---

## Post #3 by @Alice_Durante (2024-02-19 14:21 UTC)

<p>How do I do this? I created two segments, one for pre ablation lungs and one for post ablation lungs. I applied a rigid linear transformation, trying to make both images and volumes coincide as much as possible, but when I use the “elastix” toolbox and try to insert the mask, it is as if my segmentations did not exist.<br>
Thank you</p>

---

## Post #4 by @Alice_Durante (2024-02-19 14:30 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/550b028998b1ba062d2dc0d7559c164dcd7384c2.png" data-download-href="/uploads/short-url/c8kaLnxJOlyY5lzGty3SjYZMpV0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/550b028998b1ba062d2dc0d7559c164dcd7384c2_2_690x132.png" alt="image" data-base62-sha1="c8kaLnxJOlyY5lzGty3SjYZMpV0" width="690" height="132" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/550b028998b1ba062d2dc0d7559c164dcd7384c2_2_690x132.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/550b028998b1ba062d2dc0d7559c164dcd7384c2_2_1035x198.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/550b028998b1ba062d2dc0d7559c164dcd7384c2.png 2x" data-dominant-color="F8F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1142×219 10.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> This is the error that i find</p>

---

## Post #5 by @Matteboo (2024-02-19 16:23 UTC)

<p>Did you transform your segments into volume ?<br>
I don’t know a way to do it directly, I usually first convert it to a labelmap then transform the labelmap to volume using the “mask scalar volume toolbox”.<br>
Elastix only accept volume as input not segmentation, it might be why you couldn’t find them</p>

---
