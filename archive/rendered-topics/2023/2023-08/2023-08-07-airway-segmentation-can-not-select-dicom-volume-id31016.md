# Airway segmentation can not select dicom volume

**Topic ID**: 31016
**Date**: 2023-08-07
**URL**: https://discourse.slicer.org/t/airway-segmentation-can-not-select-dicom-volume/31016

---

## Post #1 by @MikhayEeer (2023-08-07 03:38 UTC)

<p>I am a new slicer user. I have already loaded Dicom data , and I can edit the dicom volume in Editor Effect.But I found that if I try to use Extensions like Airway Segmentation or LungCT Segmenter, the CT volume selector became invalid, which means I can’t use Airway Segmentation Module to edit dicom data.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d019b88b2d02782af57e6f2d58b2c74478573fa.jpeg" data-download-href="/uploads/short-url/dgLQDfN1Dg2nOLPfaMKntylEzAC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d019b88b2d02782af57e6f2d58b2c74478573fa_2_594x500.jpeg" alt="image" data-base62-sha1="dgLQDfN1Dg2nOLPfaMKntylEzAC" width="594" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d019b88b2d02782af57e6f2d58b2c74478573fa_2_594x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d019b88b2d02782af57e6f2d58b2c74478573fa_2_891x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d019b88b2d02782af57e6f2d58b2c74478573fa_2_1188x1000.jpeg 2x" data-dominant-color="989897"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1441×1212 95.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Like this image, there is nothing in the CT volume selector box. But I can see this CT in “data” module .<br>
How can I solve this problem? Is there something wrong with my operation?<br>
Hope to get your help, very grateful!</p>

---

## Post #2 by @pieper (2023-08-07 12:59 UTC)

<p>it’ possible your dicom data loaded as a mutlivolume rather than a scalar volume.  This post might help, but you can also search for others on the optic if that’s what it turns out to be.</p>
<aside class="quote quote-modified" data-post="1" data-topic="22134">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tipunch/48/14418_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/newbie-struggling-with-dicom-multivolume-and-sequences/22134">[Newbie] Struggling with DICOM, MultiVolume and Sequences</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 
I would like first to thank you for this great and powerful open-source software! In a world where every postprocessing tool can cost a kidney, it is a relief to see people who care about improving and sharing research. 
I’m an absolute newbie in Slicer, and although I’m used to many programming tools, I’m pretty lost in what I’m trying to do. 
My goal: postprocessing DCE-MRI acquisitions 
My materials: 

T1 mapping: 3 separate series with different flip angles
DCE: 1 series with different …
  </blockquote>
</aside>


---

## Post #3 by @MikhayEeer (2023-08-08 04:36 UTC)

<p>Thank you,I tried your way and successfully to load Dicom data in Airwaysegmentation module! Thanks for your help very much!</p>

---
