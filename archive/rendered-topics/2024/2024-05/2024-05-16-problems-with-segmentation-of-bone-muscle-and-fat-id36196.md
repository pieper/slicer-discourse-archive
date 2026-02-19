---
topic_id: 36196
title: "Problems With Segmentation Of Bone Muscle And Fat"
date: 2024-05-16
url: https://discourse.slicer.org/t/36196
---

# Problems with segmentation of bone, muscle and fat 

**Topic ID**: 36196
**Date**: 2024-05-16
**URL**: https://discourse.slicer.org/t/problems-with-segmentation-of-bone-muscle-and-fat/36196

---

## Post #1 by @concker99 (2024-05-16 05:29 UTC)

<p>Hello everyone,</p>
<p>I’m new to using 3D Slicer and could really use your help. My <strong>aim</strong> is to segment the muscle, fat, and bone on MRI slices of a rat. here is the data in question: <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c13017f01b9fe909b510dfcdda6c41e0ba8765c7.jpeg" alt="Gems06" data-base62-sha1="rz1bSKfwOdJj9RbIhCzACOr98kD" width="256" height="256">.</p>
<p>As for <strong>my steps</strong>,  I’ve uploaded the data in NIFTI format (.nii) into 3D Slicer and followed these steps:</p>
<ol>
<li>Uploaded the slices and used the Crop Volume module to define a Region of Interest (ROI) volume.<br>
2.In the Segment Editor module, I created two different segments, each representing a different muscle, using the paint tool.<br>
3.I then utilized the Grow from Seeds tool to generate a volume.</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99a41ef4c362ba9f75b221732871dbf8fdb18f60.png" alt="image" data-base62-sha1="lVaGbAeZaY19eXLjXUejBbhutTq" width="688" height="124"> <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f573e284eb1abb4e2a8267466cbfd41ecba543e4.jpeg" alt="image" data-base62-sha1="z1nggBX7c1FKVkXiqiADOPSGdFi" width="595" height="304"></p>
<p>However, I’m encountering <strong>issues</strong> with the segmentation results. They’re not matching what I saw in the tutorials, and the quality is poor.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1de94b79f9b556cd87655e8e62d2125f5e98d6a8.jpeg" alt="image" data-base62-sha1="4gBG4cahWGA52zNvwSCdl4FlcCs" width="578" height="469"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3445867a9f62c052e5d77ba87dcf05395f0f0cfe.jpeg" alt="image" data-base62-sha1="7spMIqdLBunTtl9Tp6DZwaXnnPg" width="464" height="395"></p>
<p>I’ve considered a couple of <strong>possible reasons</strong> for this:</p>
<p>1.The threshold the the slices. The threshold goes from 0 to 0.642 which is different from what I have worked with</p>
<ol start="2">
<li>I only work with one view and the other samples I worked with had the 3 views.</li>
</ol>
<p>Could you please provide some guidance and input to help me achieve better segmentation results?</p>
<p>Thank you all in advance for your assistance.</p>

---

## Post #2 by @LeidyMoraV (2024-05-29 14:28 UTC)

<p>Can you share the file that you’re working with?</p>

---

## Post #3 by @concker99 (2024-05-29 15:45 UTC)

<p>Sorry, I thought the JPEG version would be usable. It seems that I can’t upload .nii files. I hope this link will work, but unfortunately, it will expire on August 27.</p>
<p><a href="https://usherbrooke-my.sharepoint.com/:u:/g/personal/cota2317_usherbrooke_ca/EesDxJg23fxBgTs-1P36u0IB8NgNqvfNJIkyDo_lpDofug?e=ZmFzOQ" rel="noopener nofollow ugc">Gems06.nii</a></p>

---

## Post #4 by @LeidyMoraV (2024-05-29 21:40 UTC)

<p>I’m not an expert but it seems like you have a small number of layers, I only distinguish one where you can clearly see the two muscles. If you’re planning to use Grow from Seeds I think you need multiple layers where you can see the tissue. However, I just use the threshold as a mask and the paint the two segments. I also use grow from seeds but didn’t notice any visible change in the segmentation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27dea19a49c348401ba73dd7cb752c75d7203496.jpeg" data-download-href="/uploads/short-url/5GHBBRjJHrXnMGP2nbrm5qMfOGq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27dea19a49c348401ba73dd7cb752c75d7203496_2_690x297.jpeg" alt="image" data-base62-sha1="5GHBBRjJHrXnMGP2nbrm5qMfOGq" width="690" height="297" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27dea19a49c348401ba73dd7cb752c75d7203496_2_690x297.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27dea19a49c348401ba73dd7cb752c75d7203496_2_1035x445.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27dea19a49c348401ba73dd7cb752c75d7203496_2_1380x594.jpeg 2x" data-dominant-color="7B7F80"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×827 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
