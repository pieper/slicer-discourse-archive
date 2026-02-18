# How to segment epicardial adipose tissue accurately?

**Topic ID**: 17402
**Date**: 2021-05-01
**URL**: https://discourse.slicer.org/t/how-to-segment-epicardial-adipose-tissue-accurately/17402

---

## Post #1 by @caiwei (2021-05-01 13:11 UTC)

<p>Hello everyone,<br>
I’m going to use cardiac enhanced CT to measure the volume of epicardial adipose tissue (between the myocardium and the visceral pericardium), and when I use the Threshold tool, the extra-pericardial adipose tissue is also included(shown in Figure 1). Is there a way to differentiate the paracardial tissue only from the adipose tissue within the visceral pericardium of segment? which tool or extension should I use to achieve this purpose? In addition, whether there is an extension to automatically achieve this purpose (automatically identify the boundary of the pericardium) as shown in figure 2, which is obtained by QFAT software (version 2.0; Cedars-Sinai Medical Center)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/263726287e686ded881cb8ff77695208da73ff84.jpeg" data-download-href="/uploads/short-url/5s4iBU5gyEJwkAr91UENiZvknis.jpeg?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/263726287e686ded881cb8ff77695208da73ff84_2_607x500.jpeg" alt="Screenshot_1" data-base62-sha1="5s4iBU5gyEJwkAr91UENiZvknis" width="607" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/263726287e686ded881cb8ff77695208da73ff84_2_607x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/263726287e686ded881cb8ff77695208da73ff84_2_910x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/263726287e686ded881cb8ff77695208da73ff84.jpeg 2x" data-dominant-color="8B8A73"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">1093×900 261 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thanks a lot.</p>

---

## Post #2 by @lassoan (2021-05-21 19:10 UTC)

<p>Instead of applying the threshold directly, use the threshold range for masking. Then you can create two segments - one for epicardial and another for extra-pericardial adipose tissue. It should be enough to just paint a few small parts of these segments and then you can generate a full segmentation automatically by using “Grow from seeds” effect.</p>
<p>See in this video how masking and grow from seeds effect are used to separate two touching bone segments that have the same intensity in the image:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="8Nbi1Co2rhY" data-video-title="Femur segmentation using masked region growing in 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=8Nbi1Co2rhY" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/8Nbi1Co2rhY/maxresdefault.jpg" title="Femur segmentation using masked region growing in 3D Slicer" width="" height="">
  </a>
</div>


---

## Post #3 by @caiwei (2021-05-23 06:10 UTC)

<p>Thank you very much, sir. That’s a wonderful suggestion and my problem has been solved. Wish you have a nice weekend.</p>

---
