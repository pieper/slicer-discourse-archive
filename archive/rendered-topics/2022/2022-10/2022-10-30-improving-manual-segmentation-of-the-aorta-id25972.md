---
topic_id: 25972
title: "Improving Manual Segmentation Of The Aorta"
date: 2022-10-30
url: https://discourse.slicer.org/t/25972
---

# Improving manual segmentation of the aorta

**Topic ID**: 25972
**Date**: 2022-10-30
**URL**: https://discourse.slicer.org/t/improving-manual-segmentation-of-the-aorta/25972

---

## Post #1 by @chendong9416 (2022-10-30 16:04 UTC)

<p>For aortic dissection, the measurement of aortic diameter (outer wall to outwall) in several levels is clinical relevent.</p>
<p>Automatic segmentation works well for the aortic lumen but will miss the aotic wall and intimal flap.</p>
<p>as far as i know, to make the measurement from outer wall to outer wall, the best workflow is manual segmentation+centerline extraction+measurement.</p>
<p>If i have a large database, how can i improve this workflow (by decrease time) ?</p>
<p>I have read some papers about deep learning method for achieve this goal, but i am majoring in vascular surgery and not capable of performing these techniques. Is there any simple step that i can do to achieve my goal?</p>
<p>Thanks and look forward to hear from you experts.</p>

---

## Post #2 by @lassoan (2022-10-30 17:57 UTC)

<p>Segmenting large-diameter contrasted vessels should be straightforward. The main concern is visibility of vessel walls. Could you provide an anonymized sample data set and an example segmentation/measurements that you need? That could give us an idea of the difficulty of the problems and how to resolve them.</p>
<p>Deep learning is becoming the standard method for automatic image segmentation. If you have access to lots of data sets (maybe a few hundred images are enough) and you are willing to spend time with segmentation using manual/semi-automatic methods then you have everything to train a neural network. We have examples of tech-savvy surgeons training networks successfully (with some help from engineers), so you may give it a try. <a class="mention" href="/u/rbumm">@rbumm</a> maybe you could share your experience/give some advice to a fellow surgeon.</p>

---

## Post #3 by @rbumm (2022-10-30 20:08 UTC)

<p>Thanks for the ping, will answer in more detail on Tuesday!</p>

---

## Post #4 by @chendong9416 (2022-10-31 07:49 UTC)

<p>Dear Andras Lasso<br>
I (and other doctors major in aortic disease) need to measure several levels in specific way as the guidelines recommended<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a766383fa1cb1fb0117bd18ffb4d1964996ffbd6.jpeg" data-download-href="/uploads/short-url/nSSK1qyRHB0dlwgmVJkW88hJPTg.jpeg?dl=1" title="a" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a766383fa1cb1fb0117bd18ffb4d1964996ffbd6_2_565x500.jpeg" alt="a" data-base62-sha1="nSSK1qyRHB0dlwgmVJkW88hJPTg" width="565" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a766383fa1cb1fb0117bd18ffb4d1964996ffbd6_2_565x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a766383fa1cb1fb0117bd18ffb4d1964996ffbd6_2_847x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a766383fa1cb1fb0117bd18ffb4d1964996ffbd6.jpeg 2x" data-dominant-color="A9A7A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">a</span><span class="informations">941×832 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e21dcb4db8cb0b3b61d435bd8ea56f20ffadc22.png" data-download-href="/uploads/short-url/hZOI3pEMg7lgYoVD6G3MF3oRtRw.png?dl=1" title="b" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e21dcb4db8cb0b3b61d435bd8ea56f20ffadc22_2_344x500.png" alt="b" data-base62-sha1="hZOI3pEMg7lgYoVD6G3MF3oRtRw" width="344" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e21dcb4db8cb0b3b61d435bd8ea56f20ffadc22_2_344x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e21dcb4db8cb0b3b61d435bd8ea56f20ffadc22_2_516x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e21dcb4db8cb0b3b61d435bd8ea56f20ffadc22_2_688x1000.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">b</span><span class="informations">1020×1482 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Below is a video after i had manually segmented the aorta (&gt;1 hour) and extracted the centerline, and this video shows 5 levels i am interested in (only the total diameter was measured in this case)</p>
<div class="youtube-onebox lazy-video-container" data-video-id="m8LoelEgq9A" data-video-title="3D slicer aortic measurements" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=m8LoelEgq9A" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/m8LoelEgq9A/maxresdefault.jpg" title="3D slicer aortic measurements" width="" height="">
  </a>
</div>

<p>This way is time consuming, and honestly, i am not satisfied with the segmentation and do not have much faith in it.</p>
<p>Below is a video showing the whole process of aortic measurements by manually centerline extraction (which i had proposed before), it is time saving, but not standardized. Is there a way i can use deep learning to standardize this process?</p>
<div class="youtube-onebox lazy-video-container" data-video-id="1vTfVTqp3rs" data-video-title="3D slicer aortic measurements 2" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=1vTfVTqp3rs" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/1vTfVTqp3rs/maxresdefault.jpg" title="3D slicer aortic measurements 2" width="" height="">
  </a>
</div>

<p>or maybe can you experts add two markers (shown as blue) for determine the midpoint (at least adjustable in two of axial, sagittal, and coronal plane)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8101951f941e2536bd60321431bbd3ff3f08c078.jpeg" data-download-href="/uploads/short-url/ipeZ1hZyEn830u61vT3uwtpqSPC.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8101951f941e2536bd60321431bbd3ff3f08c078_2_563x500.jpeg" alt="Screenshot" data-base62-sha1="ipeZ1hZyEn830u61vT3uwtpqSPC" width="563" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8101951f941e2536bd60321431bbd3ff3f08c078_2_563x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8101951f941e2536bd60321431bbd3ff3f08c078_2_844x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8101951f941e2536bd60321431bbd3ff3f08c078_2_1126x1000.jpeg 2x" data-dominant-color="6D6D77"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1884×1673 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>By the way, i had segmentate a single kidney for calculating the renal volume by using grow from the seed + segment statistics. Although it takes only minutes, i have a work loads of more than 1000 kidney measurement, can this simpler workflow be improved by deep learning? and if it works, can it be form into an extension so other researchers can use it? Thanks.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c236d721ceb38268c4c5c04d96bc873dc5f2f0a4.jpeg" data-download-href="/uploads/short-url/rI67Hpjp1zaxaNMW2bf4qUdbupC.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c236d721ceb38268c4c5c04d96bc873dc5f2f0a4_2_690x463.jpeg" alt="2" data-base62-sha1="rI67Hpjp1zaxaNMW2bf4qUdbupC" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c236d721ceb38268c4c5c04d96bc873dc5f2f0a4_2_690x463.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c236d721ceb38268c4c5c04d96bc873dc5f2f0a4_2_1035x694.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c236d721ceb38268c4c5c04d96bc873dc5f2f0a4_2_1380x926.jpeg 2x" data-dominant-color="8E8F8F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1920×1289 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @pieper (2022-10-31 14:19 UTC)

<p><a href="https://github.com/wasserth/TotalSegmentator">TotalSegmentator</a> should work well for both the aorta and the kidneys.  I don’t know of anything that will measure the aortic dissection well, but I can imagine a custom markup tool could be written to simplify the process a lot.</p>

---

## Post #6 by @chendong9416 (2022-11-01 07:05 UTC)

<p>Dear sir<br>
Please tell me how can it be used in 3D slicer, Thanks</p>

---

## Post #7 by @rbumm (2022-11-01 12:18 UTC)

<p>Totalsegmentator is a great nnU-Net segmentation tool from Jakob Wasserthal (University of Basel)  that needs to be installed and run separately from the command line. A call to Totalsegmentator AI is included in the Lung CT Segmenter module of the Lung CT Analyzer extension for user convenience.<br>
Setting this up can be a little tedious, but it works and you should be able to use Totalsegmentator from 3D Slicer in any kind of CT.</p>
<p>First, install the Lung CT Analyzer extension and restart Slicer. Then <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/wiki/Step-2-Using-Lung-CT-Segmenter-with-AI#totalsegmentator" rel="noopener nofollow ugc">follow all steps documented in the LCTA wiki</a>. If you are a Windows user, do the nnunet fix ( see “Change the line …”)</p>
<p>Then try</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83885de34cb7aed77063d97f1169714b502e483d.png" alt="image" data-base62-sha1="iLAIcVX0yoN5G3TkLmzJ7dsJ9BH" width="524" height="35"></p>
<p>If you get errors, keep in mind you need a rather strong GPU for this procedure and maybe run Totalsegmentator from the command line first.</p>

---

## Post #8 by @chendong9416 (2022-11-02 09:37 UTC)

<p>Thanks, i will try these steps.</p>

---
