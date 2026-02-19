---
topic_id: 487
title: "Resample Dtivolume Error"
date: 2017-06-13
url: https://discourse.slicer.org/t/487
---

# Resample DTIVolume error!

**Topic ID**: 487
**Date**: 2017-06-13
**URL**: https://discourse.slicer.org/t/resample-dtivolume-error/487

---

## Post #1 by @Rewati_Kulkarni (2017-06-13 02:35 UTC)

<p>Operating system: Windows 7 professional<br>
Slicer version: 4.6.2<br>
Expected behavior: Sample data from tutorial should execute registration<br>
Actual behavior: I downloaded the sample data set to perform registration of DTI to MRI from the Slicer page: <a href="https://na-mic.org/wiki/Projects:RegistrationLibrary:RegLib_C03" class="inline-onebox" rel="noopener nofollow ugc">Projects:RegistrationLibrary:RegLib C03 - NAMIC Wiki</a></p>
<p>However, I am able to successfully perform only part 1 of this two-step process. The program takes too long to compute resampling of the DTI volume, and then I get an error message as attached with this post. I tried doing the registration on 2 different computers, but the error persisted. How can I resolve this?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/9eadba1ebe1d9e60a1ec0a355bfd8e10fe96f395.JPG" data-download-href="/uploads/short-url/mDJEdUkqgtG4VSvquF2I1zkEnyt.JPG?dl=1" title="slicer error.JPG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9eadba1ebe1d9e60a1ec0a355bfd8e10fe96f395_2_650x500.JPG" width="650" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9eadba1ebe1d9e60a1ec0a355bfd8e10fe96f395_2_650x500.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9eadba1ebe1d9e60a1ec0a355bfd8e10fe96f395_2_975x750.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9eadba1ebe1d9e60a1ec0a355bfd8e10fe96f395.jpeg 2x" data-dominant-color="909096"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer error.JPG</span><span class="informations">1279×983 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2017-06-13 11:48 UTC)

<p>Could you try after changing this setting: Edit / Application settings / Modules -&gt; check Prefer Executable CLIs?</p>
<p>Could you please also try with the latest nightly version?</p>

---

## Post #3 by @Rewati_Kulkarni (2017-06-13 14:41 UTC)

<p>I tried both suggestions but they didn’t work. When I used the nightly build, the same error showed up again (image below)<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/810f1ee0910369d238981fc4fc2d003ad677c453.JPG" data-download-href="/uploads/short-url/ipHZlsExihJ71IHwN84iyyiIY1B.JPG?dl=1" title="error.JPG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/810f1ee0910369d238981fc4fc2d003ad677c453_2_689x472.JPG" width="689" height="472" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/810f1ee0910369d238981fc4fc2d003ad677c453_2_689x472.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/810f1ee0910369d238981fc4fc2d003ad677c453_2_1033x708.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/810f1ee0910369d238981fc4fc2d003ad677c453.jpeg 2x" data-dominant-color="AAABB2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error.JPG</span><span class="informations">1279×876 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2017-06-13 14:54 UTC)

<p>Could you save the scene into a .mrb file right before you click Apply (that would cause the crash), upload it somewhere, and copy the link here?</p>

---

## Post #5 by @Rewati_Kulkarni (2017-06-13 15:04 UTC)

<p>Sure, or how about I upload the file here directly? Would that work?</p>

---

## Post #6 by @lassoan (2017-06-13 15:07 UTC)

<p>File size and type are limited here. Use Dropbox, OneDrive, Google Drive, etc.</p>

---

## Post #7 by @Rewati_Kulkarni (2017-06-13 15:16 UTC)

<p>Here is the Google drive link: <a href="https://drive.google.com/file/d/0B9ZRwZrndb2DR0Q5SF9EQ2YxRDA/view?usp=sharing" rel="nofollow noopener">https://drive.google.com/file/d/0B9ZRwZrndb2DR0Q5SF9EQ2YxRDA/view?usp=sharing</a></p>

---

## Post #8 by @lassoan (2017-06-13 16:05 UTC)

<p>I was able to reproduce the issue. The problem is that due to some reason this CLI module uses .mat extension for writing transforms, which is not capable of handling composite transforms. I’ll change it to use .h5, as that can handle any combination of transforms. Tomorrow’s nightly version should work well.</p>

---

## Post #9 by @Rewati_Kulkarni (2017-06-13 16:17 UTC)

<p>Thank you very much! I’ll wait for the new nightly version, in that case.</p>
<p>And as far as the tutorial steps are concerned, instead of selecting “displacement”, I would then have to pick “h5”, is that right?</p>

---

## Post #10 by @lassoan (2017-06-13 16:22 UTC)

<p>You don’t have to do anything differently, it’s just an internal change in file format.</p>

---

## Post #11 by @Rewati_Kulkarni (2017-06-13 16:33 UTC)

<p>Alright, thanks!</p>
<p><em>Rewati Kulkarni</em></p>
<p><em>Research Assistant, Injury Biomechanics Lab.</em></p>
<p>University of Pennsylvania,<br>
Department of Bioengineering<br>
<em>+1 267-648-7960</em> | <em><a href="mailto:rewati.p.k01@gmail.com">rewati.p.k01@gmail.com</a> <a href="mailto:rewati.p.k01@gmail.com">rewati.p.k01@gmail.com</a></em></p>

---
