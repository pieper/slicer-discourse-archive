# Create a master from MRI for 3D print

**Topic ID**: 12231
**Date**: 2020-06-26
**URL**: https://discourse.slicer.org/t/create-a-master-from-mri-for-3d-print/12231

---

## Post #1 by @Alejandro_Terrado (2020-06-26 13:25 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d3ab762aa094c0022ac1a916098327f255739aa.jpeg" alt="Captura 1" data-base62-sha1="mqULflTEG7MGZ6WFp1uOTSYlWb0" width="472" height="379"> <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3095964fcb0996a0029db8fbe5b8fce6eb73028c.jpeg" alt="Captura 2" data-base62-sha1="6VNpgKtKkW8Ypbgi4rATI7asjAE" width="478" height="166"> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65ba6bd6c1eb8acfaa4cbb6568367eeb50146f63.jpeg" data-download-href="/uploads/short-url/evVD4srL9QlKI6gUqf3pFjJf8LF.jpeg?dl=1" title="Captura 3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/65ba6bd6c1eb8acfaa4cbb6568367eeb50146f63_2_573x499.jpeg" alt="Captura 3" data-base62-sha1="evVD4srL9QlKI6gUqf3pFjJf8LF" width="573" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/65ba6bd6c1eb8acfaa4cbb6568367eeb50146f63_2_573x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65ba6bd6c1eb8acfaa4cbb6568367eeb50146f63.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65ba6bd6c1eb8acfaa4cbb6568367eeb50146f63.jpeg 2x" data-dominant-color="616769"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura 3</span><span class="informations">668×582 56.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd536db67cea2e4e4a0f8968888a6ab523b7d857.jpeg" alt="Captura 4" data-base62-sha1="A91xMBh7fGGpInlItjRmH8hbeHZ" width="253" height="442"></p>
<p>Hi!!! I have been trying to get a volume from a brain MRI (my own brain). The problem is that the scan have many volumes, but each volume has only one plane in high resolution. I can’t get the high-resolution plane of each volume, to generate a new master volume with the hi-res planes. The idea is to use segmentation to 3D print my brain.<br>
I already did this with my maxilar with excellent results.<br>
I hope you can help me out!<br>
Thanks in advance</p>

---

## Post #2 by @pieper (2020-06-26 18:33 UTC)

<p>It’s a common issue - the post below and some of the ones it links to should give you the background.</p>
<aside class="quote" data-post="2" data-topic="8695">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-can-i-import-in-the-same-volume-3-dicom-files-of-the-same-volume/8695/2">How can I import in the same volume 3 DICOM files of the same volume</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Quite often 3 anisotropic MRI images are acquired (high resolution along two axes, very low resolution along a third axis) to reduce time spent in the MRI scanner. However, these images are not well suited for 3D segmentation. See more information here: <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2">Combining volumes - what am I missing? </a>. To reduce artifacts caused by low-resolution third axis you can follow the technique explained here: <a href="https://discourse.slicer.org/t/segmenting-issue-i-cant-remove-ridges-in-3-d-model/4792/5">Segmenting Issue: I Can’t Remove “ridges” in 3-D model </a>
  </blockquote>
</aside>


---

## Post #3 by @Alejandro_Terrado (2020-06-27 11:48 UTC)

<p>Thanks for your reply! I am trying to aply the tools and get a better 3D volume. If not I’ll be back <img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:"></p>

---

## Post #4 by @Alejandro_Terrado (2020-06-27 15:37 UTC)

<p>Unfortunately, I wasn’t successful by trying to apply those tools. Still the same result. Is there a step by step to follow?</p>

---

## Post #5 by @lassoan (2020-06-27 16:24 UTC)

<p>Please describe what you tried. Post a few screenshots, too.</p>

---
