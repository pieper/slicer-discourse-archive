# Reading the .obj (+.mtl) brain atlas and exporting as .nii

**Topic ID**: 10161
**Date**: 2020-02-07
**URL**: https://discourse.slicer.org/t/reading-the-obj-mtl-brain-atlas-and-exporting-as-nii/10161

---

## Post #1 by @BegginerUser (2020-02-07 16:32 UTC)

<p>Hello,</p>
<p>I decided to use a Slicer in order to make a brain atlas conversion.<br>
I exported a brain atlas which includes different brain areas with Neurolucida as .obj + .mtl file.<br>
I need to convert that atlas into nifti (.nii) format in order to read it with an MRI imaging called NORA.<br>
Could you please help me how to do it?<br>
What I tried is:</p>
<ol>
<li>importing .obj as a model</li>
<li>importing .mtl as a volume<br>
Problem: I do not see different brain areas, the whole brain is gray<br>
Problem: I do not see a .nii format when I click the export button.</li>
</ol>
<p>Hope somebody could navigate me through the exporting process.<br>
Wish you all the best,<br>
Lara</p>

---

## Post #2 by @lassoan (2020-02-07 16:51 UTC)

<p>Is each brain area stored with a different material? Can you share a sample data set?</p>
<p>Currently, a single obj file is always loaded as a single segment, so you would need to split it into separate mesh files before you export it or write a short Python script in Slicer that splits the mesh based on material ID.</p>

---

## Post #3 by @BegginerUser (2020-02-10 17:04 UTC)

<p>Dear Andras,</p>
<p>Thank you for the answer! I saved the whole model as a single .obj accompanied with a single material. I will follow your advice on saving each segment separately! Thanks for the explanation.</p>
<p>Lara</p>

---

## Post #4 by @BegginerUser (2020-02-15 14:16 UTC)

<p>Hello Andras,</p>
<p>Thank you for the previous answer. I have followed your recommendation and have uploaded two brain regions as separated .obj files.</p>
<p>I visualized them as a solid and as a mesh <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa414e510c4f51a6fe59dd58830725b3e449719f.png" data-download-href="/uploads/short-url/zHRhFbVoIXqvzCRKK0VaOq0Ht5d.png?dl=1" title="test01_surface" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa414e510c4f51a6fe59dd58830725b3e449719f_2_490x500.png" alt="test01_surface" data-base62-sha1="zHRhFbVoIXqvzCRKK0VaOq0Ht5d" width="490" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa414e510c4f51a6fe59dd58830725b3e449719f_2_490x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa414e510c4f51a6fe59dd58830725b3e449719f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa414e510c4f51a6fe59dd58830725b3e449719f.png 2x" data-dominant-color="887FA2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">test01_surface</span><span class="informations">581×592 78.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I need to convert both objects into the volume.<br>
I cannot save it as a nifti (.nii) if I do not convert it to a volume.</p>
<p>Could you please advice me on how to make a conversion from a current model to a volume?</p>
<p>Thanks again for your help Andras!<br>
You are the best.<br>
Lara</p>

---

## Post #5 by @lassoan (2020-02-15 18:34 UTC)

<p>The most robust way to convert a mesh to an image is to import it into segmentation and export it to a labelmap image. You can find these conversion options in data module if you right-click the data node.</p>

---

## Post #6 by @BegginerUser (2020-02-16 14:21 UTC)

<p>Dear Andras,<br>
I got it!</p>
<p>I exported each segment as separated nifti, however I lost parameters of orientation and size in the nifti header.<br>
I believe I lost the parameters while importing the .obj into Slicer. Obj file is accompanied with .mtl, but I could not import the .mtl into as a scalar overlay.</p>
<p>Could you please help me to re-define the size and orientation?</p>
<p>Best regards,<br>
Lara</p>

---

## Post #7 by @lassoan (2020-02-16 15:03 UTC)

<p>Physical size and orientation of the labelmaps are correct. Probably you only checked the voxel coordinates. If you want the labelmap in a specific physical geometry (origin, spacing, axis directions, extents) then export using Segmentations module and specify a reference volume.</p>

---

## Post #8 by @BegginerUser (2020-02-18 12:14 UTC)

<p>I found where the problem was - the exported property of Image Spacing was defined in wrong units thus it was read as 2.4 instead of 0.024 in a slicer (Model was exported with Neurolucida in case other user finds the same obstacle).</p>
<p>Finally my histology image (image I worked with in Slicer) was the same size as the MRI image.<br>
Now I ran into another trouble -  my histology image has more z slices than the MRI so I cannot superimpose them. Is there a way to down-sample the z direction of the nii image in Slicer?</p>
<p>Thank you much for your help Andras!</p>

---

## Post #9 by @lassoan (2020-02-18 13:25 UTC)

<aside class="quote no-group" data-username="BegginerUser" data-post="8" data-topic="10161">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/c2a13f/48.png" class="avatar"> BegginerUser:</div>
<blockquote>
<p>my histology image has more z slices than the MRI so I cannot superimpose them</p>
</blockquote>
</aside>
<p>Superimposing histology and MRI in Slicer should be no problem, regardless of the size or resolution of the images, as both images are displayed in the physical coordinate system. Do you mean that you would like to superimpose the images in some third-party software that ignores physical coordinate system information?</p>

---

## Post #10 by @BegginerUser (2020-03-01 12:26 UTC)

<p>Dear Andras,</p>
<p>Thank you for your help again!<br>
Yes, I used a third party software for alignment after exporting the model from Slicer. The problem is in the third-party software I used. I tried the same in slicer and it worked perfectly. Thank you for leading me through the process. I am very grateful.</p>
<p>Wish you a wonderful day,<br>
Lara</p>

---
