---
topic_id: 4591
title: "Transfering Transformed Ras Cordinates To Fscv Excel"
date: 2018-10-30
url: https://discourse.slicer.org/t/4591
---

# Transfering transformed RAS cordinates to fscv/excel

**Topic ID**: 4591
**Date**: 2018-10-30
**URL**: https://discourse.slicer.org/t/transfering-transformed-ras-cordinates-to-fscv-excel/4591

---

## Post #1 by @Melanie (2018-10-30 15:32 UTC)

<p>Hi All, sorry I am posting again.</p>
<p>I use 3 D slicer for tracking bones during joint motion. I am using 4.9 nightly. My main question is I am trying to extract world coordinates for transformed volumes off the screen. I tried this following  python script, but failed. When I harden the transform I can copy them to clip board but readings are different. ( transformed coordinates appearing before hardening-they are changed from non transformed coordinates- after hardening) Also hardening changes the parent volume looks like, and I cannot get my original non transformed coordinates when I play back. ( even if I transform again). My steps are I load the 4d ct as volume sequence, create a fiducial node and register sequence and get the readings. Also, which registration gives better accuracy- rigid or non rigid please.</p>
<pre><code># If volume node is transformed, apply that transform to get volume's RAS coordinates
transformVolumeRasToRas = vtk.vtkGeneralTransform()
slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(volumeNode.GetParentTransformNode(), None, transformVolumeRasToRas)
point_Ras = transformVolumeRasToRas.TransformPoint(point_VolumeRas[0:3])
</code></pre>
<p>Thank you</p>

---

## Post #2 by @lassoan (2018-10-31 05:00 UTC)

<aside class="quote no-group" data-username="Melanie" data-post="1" data-topic="4591">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>When I harden the transform I can copy them to clip board but readings are different</p>
</blockquote>
</aside>
<p>Could you send us the scene (through dropbox, onedrive, etc.) or can you take a screen capture video?</p>
<p>Also, could you send a screenshot of the transformation using “Grid” mode to see if the transformation looks correct (invertible) - in Transforms module / Display section, check “Visible in slice view” and click “Grid”.</p>
<aside class="quote no-group" data-username="Melanie" data-post="1" data-topic="4591">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>Also hardening changes the parent volume looks like</p>
</blockquote>
</aside>
<p>If you harden transform on a markup then volume display should not change.</p>
<aside class="quote no-group" data-username="Melanie" data-post="1" data-topic="4591">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>which registration gives better accuracy- rigid or non rigid please</p>
</blockquote>
</aside>
<p>If there is no deformation (only translation and rotation) between registered images then rigid transform is appropriate. If you register soft tissue then non-rigid transformation is expected to provide more accurate results.</p>

---

## Post #3 by @Melanie (2018-10-31 06:34 UTC)

<p>Thank you very much Prof lasso, <a class="mention" href="/u/lassoan">@lassoan</a>. screen shots attached. It still changes the values even if F and output volumes both transformed or F alone is transformed. Both change my frame 0- RAS readings and I cant get it back my original positions when I play pack, ( Both screen shots attache<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a08f3e48bf429eb4aae3bb1578a49143b5462071.jpeg" data-download-href="/uploads/short-url/mUni8PSnzf16TNqYacq3LLRMOTD.jpeg?dl=1" title="Screenshot%20(191)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a08f3e48bf429eb4aae3bb1578a49143b5462071_2_690x388.jpeg" alt="Screenshot%20(191)" data-base62-sha1="mUni8PSnzf16TNqYacq3LLRMOTD" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a08f3e48bf429eb4aae3bb1578a49143b5462071_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a08f3e48bf429eb4aae3bb1578a49143b5462071_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a08f3e48bf429eb4aae3bb1578a49143b5462071_2_1380x776.jpeg 2x" data-dominant-color="9A9B9F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20(191)</span><span class="informations">1920×1080 315 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>.</p>

---

## Post #4 by @Melanie (2018-10-31 06:45 UTC)

<p>I will do a small video, as I am not sure how to send the scene, Thanks. Also my whole sequence is 80-100 frames. when I reference everything ti first frame by sequence registration- say 4oth frame , which is about 25 degrees angulated from the fistrt , could this introduce an error, please.</p>
<p>Also ,what could be this error message<br>
Loading with imageIOName: GDCM<br>
Irregular volume geometry detected (maximum error of 0.00518799 mm is above tolerance threshold of 0.001 mm).  Regularization transform is not added, as the option is disabled.</p>

---

## Post #5 by @lassoan (2018-10-31 12:59 UTC)

<aside class="quote no-group" data-username="Melanie" data-post="4" data-topic="4591">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>Irregular volume geometry detected (maximum error of 0.00518799 mm is above tolerance threshold of 0.001 mm). Regularization transform is not added, as the option is disabled.</p>
</blockquote>
</aside>
<p>It means that the volume slices are not exactly equally spaced. Maximum error of 0.005 is small enough so that you can safely ignore this warning.</p>
<aside class="quote no-group" data-username="Melanie" data-post="4" data-topic="4591">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>I am not sure how to send the scene</p>
</blockquote>
</aside>
<p>You can save the entire scene by clicking File / Save, click the “Giftbox” icon <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4eb5bf39f19393f10c2a7e653f7918d9714ff8d.jpeg" alt="image" data-base62-sha1="yWEKXUhs2bFKNt4vsa2aFdVeeHH" width="31" height="31"> and click Save. You have many time points, so the saving may take a while and file may be large, but just wait for it to end and then upload the resulting .mrb file to dropbox/onedribe/google drive and post the link here.</p>

---

## Post #6 by @Melanie (2018-10-31 13:21 UTC)

<p>Thank you ever so much. Will do it Prof Lasso <a class="mention" href="/u/lassoan">@lassoan</a>. One more question if that alright. Having 100 frames being referenced to frame no. 01- with angle of first and last being at least 25 deg rotated, will this affect accuracy, please. Thanks</p>

---

## Post #7 by @Melanie (2018-11-01 08:20 UTC)

<p>Hi , Prof Lasso <a class="mention" href="/u/lassoan">@lassoan</a>, I did manage to save the scene and .mrb. But the whole thing is about 8Gig and is not uploading(I am trying for hours). I saved the sequence as nrrd to anonymise patient details and did the other steps. Infact I deleted 70 frames so its less data. But still probably the mrb contains the original sequence and I cannot upload it. Do you have any other suggestions please. ( may be to cut down on frames- I deleted it in the sequences module). Thank you ever so much. Sorry I am taking your time</p>

---

## Post #8 by @lassoan (2018-11-01 16:14 UTC)

<p>If dropbox cannot deal with so large files then use dedicated large file sharing services. There are many of them out there, you should be able to find ones that you can use for free.</p>

---

## Post #9 by @Melanie (2018-11-01 16:16 UTC)

<p>Thank you very much. I am trying some way out. Would it make a difference if I create my fiducial node and put markers on surface before sequence registration. Or should It be done on the output volumes reference frame, please. Thanks</p>

---
