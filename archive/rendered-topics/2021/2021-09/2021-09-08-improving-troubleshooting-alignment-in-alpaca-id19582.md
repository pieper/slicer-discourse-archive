---
topic_id: 19582
title: "Improving Troubleshooting Alignment In Alpaca"
date: 2021-09-08
url: https://discourse.slicer.org/t/19582
---

# Improving/Troubleshooting alignment in ALPACA?

**Topic ID**: 19582
**Date**: 2021-09-08
**URL**: https://discourse.slicer.org/t/improving-troubleshooting-alignment-in-alpaca/19582

---

## Post #1 by @rsulser (2021-09-08 18:43 UTC)

<p>Operating system: Windows 10 (20H2)<br>
Slicer version: 4.11.20210226<br>
Expected behavior: Alignment and orientation of models prior to ALPACA landmarking<br>
Actual behavior: Models orient but do not appear to align</p>
<p>Hello all-</p>
<p>Having an odd spot of trouble with ALPACA, and wondering if anyone here has tips or has run into this issue before. I’m attempting to align two cochlear models as a part of standard ALPACA single alignment, but rigid alignment only seems to orient the models (not actually align in space).</p>
<p>While these two models are slightly different, I’ve had no trouble aligning similarly distinct cochlear models in the past and am at a loss as to what I may need to change or tweak to improve alignment, either in the module or with models themselves.  Any help would be greatly appreciated!</p>
<p>See photos (hopefully) attached, and a dropbox with the MRB and files can be found <a href="https://www.dropbox.com/sh/u9lwrl39h1iakp1/AABEPh9Qru9HNBa-ugqPGIPDa?dl=0" rel="noopener nofollow ugc">here</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba998083c538bd81815f797b2fab8120bb75489d.png" data-download-href="/uploads/short-url/qCJGx9Dqi3x6X374s3ybIgPq033.png?dl=1" title="Screenshot 2021-09-08 144022" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba998083c538bd81815f797b2fab8120bb75489d_2_690x370.png" alt="Screenshot 2021-09-08 144022" data-base62-sha1="qCJGx9Dqi3x6X374s3ybIgPq033" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba998083c538bd81815f797b2fab8120bb75489d_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba998083c538bd81815f797b2fab8120bb75489d_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba998083c538bd81815f797b2fab8120bb75489d_2_1380x740.png 2x" data-dominant-color="C4C5E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-09-08 144022</span><span class="informations">1920×1030 88.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2021-09-08 19:48 UTC)

<p>I donwloaded the MRB and the associated rigid transformation matrix has a huge translational component that seems unrealistic in relation to the scale of your data:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1371e651eb999a4590a4c460cf38b649d14c8dff.png" alt="image" data-base62-sha1="2M16fPLaeDHYjMqlWmmUGo2dw5h" width="626" height="387"></p>
<p>If you apply that transformation to a target model, it moves out of the scene. This might be one of the culprits.</p>
<p>Can you share the original models that you used to derive the point cloud? We need the models to test it for ourselves and see if we can replicate the issue.<br>
<a class="mention" href="/u/smrolfe">@smrolfe</a> <a class="mention" href="/u/agporto">@agporto</a></p>

---

## Post #3 by @rsulser (2021-09-08 20:32 UTC)

<p>Hello - thank you for the prompt response and for looking into this!</p>
<p>My apologies, I thought I had included a folder with the files in question. I’ve updated the original dropbox link with the models and points I have been using.</p>
<p>I’ll play around with tweaking the transform matrix - but let me know if there’s anything else I can provide on my end!</p>

---

## Post #4 by @muratmaga (2021-09-08 21:06 UTC)

<p>As I suspected the issue is with the huge translation with the models. Two cochlea that are about 5mm across, appears meters away in the scene when loaded together. So it was impossible to see them both at the same time. You were probably getting results, but not being able to see them.</p>
<p>I simply centered both models (Surface toolbox-&gt;Translate Model to origin), which ended up looking like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/423e80e43c1bb174eb543bae15fb62298654ff8c.jpeg" data-download-href="/uploads/short-url/9s1qq5Ve3MfhnMD9hn1s5bFrkM4.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/423e80e43c1bb174eb543bae15fb62298654ff8c_2_595x500.jpeg" alt="image" data-base62-sha1="9s1qq5Ve3MfhnMD9hn1s5bFrkM4" width="595" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/423e80e43c1bb174eb543bae15fb62298654ff8c_2_595x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/423e80e43c1bb174eb543bae15fb62298654ff8c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/423e80e43c1bb174eb543bae15fb62298654ff8c.jpeg 2x" data-dominant-color="9A8EA4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">739×621 92.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then I ran ALPACA with default settings, and that’s what I got at the end of rigid:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b94c51a1a0be84892c472a661df41666ca079c0.jpeg" data-download-href="/uploads/short-url/1ErZoDczT2Aeh1Y67Qr2lXPVTeU.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b94c51a1a0be84892c472a661df41666ca079c0_2_497x500.jpeg" alt="image" data-base62-sha1="1ErZoDczT2Aeh1Y67Qr2lXPVTeU" width="497" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b94c51a1a0be84892c472a661df41666ca079c0_2_497x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b94c51a1a0be84892c472a661df41666ca079c0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b94c51a1a0be84892c472a661df41666ca079c0.jpeg 2x" data-dominant-color="9E8894"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">684×688 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and this after deformable:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c73754580febad905172773eaae8b381df3f0c79.png" data-download-href="/uploads/short-url/sqlyGyPRewssfLEVYm3Y18iCxIt.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c73754580febad905172773eaae8b381df3f0c79_2_486x500.png" alt="image" data-base62-sha1="sqlyGyPRewssfLEVYm3Y18iCxIt" width="486" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c73754580febad905172773eaae8b381df3f0c79_2_486x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c73754580febad905172773eaae8b381df3f0c79.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c73754580febad905172773eaae8b381df3f0c79.png 2x" data-dominant-color="9C9AA5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">673×692 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
(I had to make a dummy curve, since I couldn’t use your curves after centering the models). These are all with default settings, I didn’t make any changes.</p>
<p>.</p>

---

## Post #5 by @rsulser (2021-09-08 21:39 UTC)

<p>Wonderful, thank you so much for your help here!</p>
<p>The target model came from a much larger scan, so I suppose the increased distance makes sense… Translating it the target to the origin seems to have done the trick, didn’t even have to adjust the reference - I’ll keep this in mind for future uses of the program!</p>

---
