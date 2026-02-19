---
topic_id: 23759
title: "About Displaying Mni Atlas On Patient Head Mri"
date: 2022-06-07
url: https://discourse.slicer.org/t/23759
---

# About displaying MNI atlas on patient head MRI

**Topic ID**: 23759
**Date**: 2022-06-07
**URL**: https://discourse.slicer.org/t/about-displaying-mni-atlas-on-patient-head-mri/23759

---

## Post #1 by @Lin (2022-06-07 21:54 UTC)

<p>Hi I’m new to use slicer. Can someone point me a bit on how to display the atlases (eg. MNI 2009 atlas or others used by Lead DBS) on patient space MRI images? I tried by dragging the atlas onto slicer, but the center is not aligned, or its’ not in correct location.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd0a8f4e0d7daa00fbd6093d6743b4d4ed504249.jpeg" data-download-href="/uploads/short-url/tfSvlOS9aCAAz8pBYGvDRPayXih.jpeg?dl=1" title="IMG_7832" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cd0a8f4e0d7daa00fbd6093d6743b4d4ed504249_2_690x388.jpeg" alt="IMG_7832" data-base62-sha1="tfSvlOS9aCAAz8pBYGvDRPayXih" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cd0a8f4e0d7daa00fbd6093d6743b4d4ed504249_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cd0a8f4e0d7daa00fbd6093d6743b4d4ed504249_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cd0a8f4e0d7daa00fbd6093d6743b4d4ed504249_2_1380x776.jpeg 2x" data-dominant-color="78767D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_7832</span><span class="informations">1920×1080 347 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I tried to google for methods but did not find clear explanation. If I have run Lead DBS normalization beforehand, is it possible to use the results? Thanks for any suggestions.</p>

---

## Post #2 by @simonoxen (2022-06-08 09:48 UTC)

<p>Hi Lin, you can import the Lead-DBS normalization results as transforms in Slicer. You can use the inverse transform (MNI to patient) to transform the atlas models into patient space.</p>

---

## Post #4 by @simonoxen (2022-06-09 07:24 UTC)

<p>Hi, the glanatComposite is the transform. There should also be a glanatInverseComposite (weird - perhaps an error from lead).</p>
<p>You can use the glanatComposite, import it as transform in Slicer, and invert it in the transforms module. Then apply it to the models.</p>

---

## Post #5 by @Lin (2022-06-09 10:14 UTC)

<p>Thanks a lot, man. I’ll take a try and get back to you soon.</p>

---

## Post #7 by @simonoxen (2022-06-09 15:31 UTC)

<p>The normalization transforms from lead use the anat_t*.nii as reference.</p>
<p>If you center the volumes in slicer, you should take into account this transform.</p>
<p>I’d recommend to keep track of the transforms you apply to the images and you can use the transforms hierarchies in slicer to apply transforms to transforms, and so on.</p>
<p>You could also register the anat_t* from lead folder to your centered volume. And then use the resulting transform together with the glanat composite. This is probably easier.</p>
<p>This is a bit complex, and requires some knowledge of how images are represented in space, and how slicer manages this. I’d recommend to look a bit into this.</p>

---

## Post #8 by @Lin (2022-06-26 14:39 UTC)

<p>Hi Simon, thanks for providing the two methods. I tried both but only did it correctly with the second way.<br>
I’ll keep on trying.<br>
Many thanks.</p>

---

## Post #9 by @Lin (2022-07-01 02:28 UTC)

<p>Hi Simon, I’ve aligned the atlas, with your help.<br>
Now I need to do with the Warp module. Can you please tell me a bit about how to use it?<br>
See the pic attached, what should I use as displacement field? Do I need to create one? I used Elastix to register anat_t1 with T1 image in slicer, but didn’t get grid transforms. Can you give me some clue on how to proceed? Thanks a lot.</p>

---

## Post #10 by @Lin (2022-07-01 02:33 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e328f356a6208a91503787dab011b360fa36c6e2.jpeg" data-download-href="/uploads/short-url/wpy7yFexV9PA2PlxdpRNANEWLBw.jpeg?dl=1" title="SlicerApp-real_uo3VgYiSS8" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e328f356a6208a91503787dab011b360fa36c6e2_2_690x370.jpeg" alt="SlicerApp-real_uo3VgYiSS8" data-base62-sha1="wpy7yFexV9PA2PlxdpRNANEWLBw" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e328f356a6208a91503787dab011b360fa36c6e2_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e328f356a6208a91503787dab011b360fa36c6e2_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e328f356a6208a91503787dab011b360fa36c6e2_2_1380x740.jpeg 2x" data-dominant-color="B9B8B8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerApp-real_uo3VgYiSS8</span><span class="informations">1920×1030 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @simonoxen (2022-07-01 07:57 UTC)

<aside class="quote no-group" data-username="Lin" data-post="9" data-topic="23759">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lin/48/15559_2.png" class="avatar"> Lin:</div>
<blockquote>
<p>what should I use as displacement field?</p>
</blockquote>
</aside>
<p>You’d generally use the normalization output. Or any non linear transform you want to modify.</p>
<p>See <a href="https://github.com/netstim/SlicerNetstim/tree/master/WarpDrive" class="inline-onebox" rel="noopener nofollow ugc">SlicerNetstim/WarpDrive at master · netstim/SlicerNetstim · GitHub</a> and <a href="https://netstim.gitbook.io/leaddbs/appendix/warpdrive" rel="noopener nofollow ugc">https://netstim.gitbook.io/leaddbs/appendix/warpdrive</a> for some more info. Still working on warpdrive to make it more user friendly.</p>

---
