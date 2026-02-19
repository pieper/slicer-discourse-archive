---
topic_id: 2554
title: "Dwiconvert Issue"
date: 2018-04-10
url: https://discourse.slicer.org/t/2554
---

# DWIConvert Issue

**Topic ID**: 2554
**Date**: 2018-04-10
**URL**: https://discourse.slicer.org/t/dwiconvert-issue/2554

---

## Post #1 by @zjx1805 (2018-04-10 07:48 UTC)

<p>I am having some trouble importing dicom files and converting them to dwi. I saw a few threads in the forum on this issue (for example, <a href="https://discourse.slicer.org/t/dwi-loading-from-dicom/1746">this</a>, <a href="https://discourse.slicer.org/t/errors-when-converting-dicom-to-nrrd-with-dwiconvert/1756">this</a>). I get the same error, which says “itk::ERROR:  LoadFromDisk not relevant”. These files can be loaded normally by DICOM browser but it is not recognized as DiffusionWeightedNode (I am trying to repeat this <a href="https://www.youtube.com/watch?v=yKt-cJKGnGY" rel="noopener nofollow ugc">video</a>) even I manually saved them into nrrd file through the SAVE module. And it also appeared garbled just as <span class="mention">@iassoan</span> showed in his <a href="https://discourse.slicer.org/t/dwi-loading-from-dicom/1746">post</a>. I am not sure if these data are taken from SIEMENS machine, since the manufacturer tag is empty. Here is the dropbox link to the data: <a href="https://www.dropbox.com/sh/763nop0x0x6nyse/AABsgML_5B6LrjDWRiQiuVmna?dl=0" class="inline-onebox" rel="noopener nofollow ugc">Dropbox - 4-Ax DWI-46959 - Simplify your life</a>, and it is also publicly available at TCGA-GBM database (Patient 06-0184, study 12-29-2007-61185, series AX DWI). I have also tried other DWI series but none of them works. From all the other posts, I could not find a very clear solution to this problem. Any help would be greatly appreciated!</p>
<p>BTW, I tried to install the latest nightly build (v4.9.0, revision 27131, built on April 9th) to see if it is resolved in this latest version. But when I opened it, it shows nothing (not exactly nothing since I can vaguely see the interface as below):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d9253e188693cca01d7642f9be8d4efc801a2e2.png" data-download-href="/uploads/short-url/4dBlPTfwEyYnaPWOGVJXZ0BKEaS.png?dl=1" title="aaa" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d9253e188693cca01d7642f9be8d4efc801a2e2_2_690x432.png" alt="aaa" data-base62-sha1="4dBlPTfwEyYnaPWOGVJXZ0BKEaS" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d9253e188693cca01d7642f9be8d4efc801a2e2_2_690x432.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d9253e188693cca01d7642f9be8d4efc801a2e2_2_1035x648.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d9253e188693cca01d7642f9be8d4efc801a2e2.png 2x" data-dominant-color="FBFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">aaa</span><span class="informations">1307×819 26.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have stable 4.8.1 version installed and my hardware is not old (I7-6700K+GTX1080+Windows10 64 bit). Any ideas why it looks like this?</p>

---

## Post #2 by @ihnorton (2018-04-10 15:47 UTC)

<p>Hi <a class="mention" href="/u/zjx1805">@zjx1805</a>, I checked the data, and the issue is exactly the same as in the thread you linked, specifically <a href="https://discourse.slicer.org/t/dwi-loading-from-dicom/1746/5">this answer</a>: the data is <em>very aggressively</em> anonymized, so it is missing the tags required to reconstruct as a diffusion volume (gradients, b-value, and even manufacturer are all removed).</p>

---

## Post #3 by @ihnorton (2018-04-10 15:52 UTC)

<p>For reference, here is the CTP script probably used for these TCIA datasets:</p>
<p><a href="https://wiki.nci.nih.gov/display/CIP/Finalized+CTP+Anonymization+Profile+-+Basic" class="onebox" target="_blank">https://wiki.nci.nih.gov/display/CIP/Finalized+CTP+Anonymization+Profile+-+Basic</a></p>
<p>Note at the bottom, any tags which are not specifically permitted are removed (which means that the private DICOM tags used to store diffusion parameters were removed, as we observe).</p>
<p>(and <a href="https://wiki.nci.nih.gov/display/CIP/Incorporation+of+DICOM+WG18+Supplement+142+into+CTP">related discussion</a>)</p>

---

## Post #4 by @zjx1805 (2018-04-10 15:57 UTC)

<p>Hi ihnorton, Thank you for your confirmation. Does that mean there is nothing I can do with these data? BTW, I am wondering if you have the same issue as me with the 4.9.0 nightly build?</p>

---

## Post #5 by @ihnorton (2018-04-10 16:31 UTC)

<aside class="quote no-group" data-username="zjx1805" data-post="4" data-topic="2554">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/f08c70/48.png" class="avatar"> zjx1805:</div>
<blockquote>
<p>Does that mean there is nothing I can do with these data?</p>
</blockquote>
</aside>
<p>Correct, unfortunately there is no way to process this data as diffusion MRI.</p>

---

## Post #6 by @zjx1805 (2018-04-10 17:48 UTC)

<p>Thank you anyway for your help!</p>

---
