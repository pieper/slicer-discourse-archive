---
topic_id: 5354
title: "Free Hand Drawing Is Not Working Effectively In Slicer"
date: 2019-01-13
url: https://discourse.slicer.org/t/5354
---

# Free hand drawing is not working effectively in slicer

**Topic ID**: 5354
**Date**: 2019-01-13
**URL**: https://discourse.slicer.org/t/free-hand-drawing-is-not-working-effectively-in-slicer/5354

---

## Post #1 by @Tarun_Gangil (2019-01-13 14:14 UTC)

<p>Operating system:Windows 10 OS 64 bit<br>
Slicer version:4.10<br>
Expected behavior: While drawing free hand annotations slicer should draw the Region of interest as the shape drawn by me.<br>
Actual behavior: I am trying to draw annotations on CT images. I prefer using free hand drawing tool to make the annotations according the Region of interest. But the slicer tool is not letting me do so. Say on one slice I will make a free hand shape for the annotation. It will automatically cut the shape drawn by me and that cut part may be visible on the next slice automatically.<br>
I WANT SLICER TO RETAIN THE ANNOTATION DRAWN BY ME ON THE RESPECTIVE SLICE.</p>
<p>following images demonstrates the example of such scenario. Kindly help me in resolving this issue.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92f4af3ffc487b18e33ce706cccc74ae657c324d.png" data-download-href="/uploads/short-url/kY1WAqfdOrq4myZbW2FtkJTLdWR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92f4af3ffc487b18e33ce706cccc74ae657c324d_2_690x387.png" alt="image" data-base62-sha1="kY1WAqfdOrq4myZbW2FtkJTLdWR" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92f4af3ffc487b18e33ce706cccc74ae657c324d_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92f4af3ffc487b18e33ce706cccc74ae657c324d_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92f4af3ffc487b18e33ce706cccc74ae657c324d.png 2x" data-dominant-color="8E8D8D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/400f40ea69199ff6d71f62a322b2200254b5d9f6.png" data-download-href="/uploads/short-url/98HeNJWofOGO1jkeNQ5UWvNXTGm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/400f40ea69199ff6d71f62a322b2200254b5d9f6_2_690x387.png" alt="image" data-base62-sha1="98HeNJWofOGO1jkeNQ5UWvNXTGm" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/400f40ea69199ff6d71f62a322b2200254b5d9f6_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/400f40ea69199ff6d71f62a322b2200254b5d9f6_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/400f40ea69199ff6d71f62a322b2200254b5d9f6.png 2x" data-dominant-color="8D8C8C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Tarun_Gangil (2019-01-13 07:24 UTC)

<p>Operating system:  Windows 10<br>
Slicer version: 4.10.0<br>
Expected behavior: Segment Editor Draw tool should allow me to draw annotations on any surface of the CT slice<br>
Actual behavior: after annotating the first slice, the slicer is automatically marking the annotation on the next slice . I don’t want that to happen.</p>
<p>At another time Segment editor Draw tool is not letting me draw the complete shape and it is cutting my annotations by itself. Please help me out regarding the same .</p>
<p>Kindly see the uploaded image so i was trying to draw a full circle on the annotation, but it is automatically cutting it and not letting me draw the complete shape on the respective slice</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ed1cd5d44f7112e69e1e3cae7d8b798eee54a09.png" data-download-href="/uploads/short-url/bfgJZEqaFDlrpFMFRIzOC5q1761.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ed1cd5d44f7112e69e1e3cae7d8b798eee54a09_2_690x387.png" alt="image" data-base62-sha1="bfgJZEqaFDlrpFMFRIzOC5q1761" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ed1cd5d44f7112e69e1e3cae7d8b798eee54a09_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ed1cd5d44f7112e69e1e3cae7d8b798eee54a09_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ed1cd5d44f7112e69e1e3cae7d8b798eee54a09.png 2x" data-dominant-color="7F7F7E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @jamesobutler (2019-01-13 14:40 UTC)

<p>Hi Tarun,</p>
<p>This post appears to be the same as what you posted <a href="https://discourse.slicer.org/t/slicer-is-automatically-cutting-the-annotations-on-the-ct-slices-and-not-letting-me-draw-the-desired-region-of-interest/5347">here</a> several hours ago. I wanted to let you know your post wasn’t being ignored, but most Slicer developers are located in North American time zones and so there are fewer responses at night and on the weekends.</p>
<p>I did a search on the forum to find a post similar to yours. Please review it below. It appears you might have a volume with a tilted gantry. Let us know if this doesn’t work and if you don’t find another solution on another forum post. We are here to help!</p>
<aside class="quote quote-modified" data-post="4" data-topic="1459">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segmentation-editor-how-to-disable-painting-on-adjacent-slices/1459/4">Segmentation Editor - How to disable painting on adjacent slices?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    If the acquisition was tilted you may need to rotate to volume plane (click the “pushpin” icon in the top-left corner of the slice view, then click the double-arrow button on the left, then the “Rotate to volume plane” icon appears): 
[image] 
Here’s an example drawing on the original slice (patient space) 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee6244f649d4f68c2cd1a14c4e489972a0a5755e.jpeg" data-download-href="/uploads/short-url/y0Qb6Ef1694zMHYIT45Xx6cE0bQ.jpg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
And here the paint stroke on the right is after rotating the red slice into the acquisition plane and only one plane is painted in the other views. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27e575499b56b012ea2cc088c24f38cb43202281.jpeg" data-download-href="/uploads/short-url/5GWesknjInRIylPfDboX3rTkF8Z.jpg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a>
  </blockquote>
</aside>


---

## Post #4 by @Tarun_Gangil (2019-01-13 14:53 UTC)

<p>Hello James,</p>
<p>Thank You for your response. I will try working out with the solution you provided and let you know if this method works for me.</p>
<p>Regards</p>
<p>Tarun</p>

---

## Post #5 by @Tarun_Gangil (2019-01-13 15:29 UTC)

<p>This method worked out fine</p>

---
