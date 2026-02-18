# How to increase the image quality when I convert Dicom file to nii file

**Topic ID**: 12928
**Date**: 2020-08-10
**URL**: https://discourse.slicer.org/t/how-to-increase-the-image-quality-when-i-convert-dicom-file-to-nii-file/12928

---

## Post #1 by @samsonaie (2020-08-10 15:12 UTC)

<p>Hi There,<br>
I had successfully converted a 3D ultrasound dicom file  into a nii file. I am doing this because I can use a python script to convert nii file to a series of image (png) file with X/Y/Z dimension info.  However, I found the quality of nii is very low ,thus the png files are also very low resolution.</p>
<p>I would like to ask a favor from the expert in the forum:</p>
<ol>
<li>is there a special parameter / or setting I need to configure in 3D slicer  when I convert dicom to nii ?</li>
<li>is there a way , I can convert dicom file , DIRECTLY,  to a series of png files.</li>
</ol>
<p>Any suggestion or  tips will be definitely helpful !! thanks ,</p>
<p>Samson</p>

---

## Post #2 by @lassoan (2020-08-10 16:12 UTC)

<p>There is no image quality loss when you save an image in Nifti format. It is a very simple operation and not much can go wrong.</p>
<p>It is much more likely that there is a problem during DICOM import. 3D ultrasound data is usually stored in proprietary DICOM tags, so importing it is not trivial. How did you open the 3D ultrasound DICOM file? Using <a href="https://github.com/SlicerHeart/SlicerHeart#importing-dicom-files">SlicerHeart extension</a>? Is it fetal or cardiovascular ultrasound? Which vendor, which ultrasound system?</p>

---

## Post #3 by @samsonaie (2020-08-11 01:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="12928">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a href="https://github.com/SlicerHeart/SlicerHeart#importing-dicom-files" rel="noopener nofollow ugc">SlicerHeart extension</a></p>
</blockquote>
</aside>
<p>The dicom is acquired from GE E8.<br>
I had installed <a href="https://github.com/SlicerHeart/SlicerHeart#importing-dicom-files" rel="noopener nofollow ugc">SlicerHeart extension</a>, and also successfully load the ultrasound file in 3D slicer and view it in volume rendering mode.</p>
<p>any other tips , please advice, thanks</p>

---

## Post #4 by @lassoan (2020-08-11 03:14 UTC)

<p>Is the image quality you see in Slicer good? If you save as .nii and load the .nii is the image quality the same? Can you attach a screenshot that shows the bad image quality?</p>

---
