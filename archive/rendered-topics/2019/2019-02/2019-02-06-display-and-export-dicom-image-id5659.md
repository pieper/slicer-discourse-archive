---
topic_id: 5659
title: "Display And Export Dicom Image"
date: 2019-02-06
url: https://discourse.slicer.org/t/5659
---

# Display and export DICOM image.

**Topic ID**: 5659
**Date**: 2019-02-06
**URL**: https://discourse.slicer.org/t/display-and-export-dicom-image/5659

---

## Post #1 by @Ekaterina (2019-02-06 13:31 UTC)

<p>Operating system: manOS High Sierra version 10.13.6<br>
Slicer version: 4.10<br>
Expected behavior:</p>
<ol>
<li>Upload images of DICOM format. Display of the whole image.</li>
<li>Export the built fraction anisotropy of the program in format DICOM.</li>
</ol>
<p>Actual behavior:</p>
<ol>
<li>Program cuts off the image in two projections (sagittal and coronary). I tried to use DWI envelope, he did not solve the problem.</li>
<li>When saving the model back to DICOM format (I use DICOM browser =&gt; DICOM Export).<br>
I tried to upload a series of pictures with  fraction anisotropy and completely all patient pictures (‘export series’ and ‘export entire scene’) - the result is one: instead of my images, black empty files are saved.<br>
Answer please how to solve these problems!!!</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e24f3cec03ab84d1128e26cc873dd2fb0a9a9f6.png" data-download-href="/uploads/short-url/8RKLWqdxNZcKLaSglfPy64hHunQ.png?dl=1" title="17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e24f3cec03ab84d1128e26cc873dd2fb0a9a9f6_2_690x214.png" alt="17" data-base62-sha1="8RKLWqdxNZcKLaSglfPy64hHunQ" width="690" height="214" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e24f3cec03ab84d1128e26cc873dd2fb0a9a9f6_2_690x214.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e24f3cec03ab84d1128e26cc873dd2fb0a9a9f6_2_1035x321.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e24f3cec03ab84d1128e26cc873dd2fb0a9a9f6.png 2x" data-dominant-color="323231"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">17</span><span class="informations">1277×397 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2019-02-06 16:28 UTC)

<p>Hi - can you explain what the screenshot is showing?  It looks like this is the original data the scan did not include the top of the head.  Otherwise it looks correct.</p>
<p>As for exporting the FA, it may be because the FA in slicer is floating point (0 to 1) but this is basically zero in DICOM images that are only integers.  Typically DICOM scales by a factor of 1000 (or maybe 1024 I’m not sure).  If you scale first it should work. You could use numpy or SimpleFilters with the ShiftScaleImageFilter option for this.</p>
<p>Hope that helps</p>

---

## Post #3 by @Ekaterina (2019-02-06 16:47 UTC)

<p>Thank you for help!</p>
<p>ср, 6 февр. 2019 г., 19:38 Steve Pieper via 3D Slicer Forum <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>:</p>

---

## Post #4 by @cpinter (2019-02-06 17:26 UTC)

<aside class="quote no-group" data-username="Ekaterina" data-post="1" data-topic="5659">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/bc79bd/48.png" class="avatar"> Ekaterina:</div>
<blockquote>
<p>saving the model back to DICOM format (I use DICOM browser =&gt; DICOM Export)</p>
</blockquote>
</aside>
<p>What do you mean by this? What exactly do you activate and what is selected? Exporting the FA to DICOM requires going a <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export">different path</a>, but as far as I know there is no DICOM export plugin supporting this data type yet.</p>

---

## Post #5 by @Ekaterina (2019-02-07 06:02 UTC)

<p>I load DWI image in DICOM format into the program. Building FA. I want to express FA in DICOM format.<br>
What path are you talking about?</p>
<p>ср, 6 февр. 2019 г., 20:37 Csaba Pinter via 3D Slicer Forum <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>:</p>

---

## Post #6 by @cpinter (2019-02-07 14:39 UTC)

<aside class="quote no-group" data-username="Ekaterina" data-post="5" data-topic="5659">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/bc79bd/48.png" class="avatar"> Ekaterina:</div>
<blockquote>
<p>What path are you talking about?</p>
</blockquote>
</aside>
<p>There is a DICOM export feature that is different from the one you thought would do the export. Please follow the link I added.</p>
<p>Also please try to answer all the questions, because that help us understand your problem better:</p>
<ol>
<li>What do you mean by “saving the model back to DICOM format (I use DICOM browser =&gt; DICOM Export)” ? What is the model you want to save? The FA result?</li>
<li>What exactly do you activate and what is selected?</li>
</ol>

---
