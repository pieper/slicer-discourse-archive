---
topic_id: 512
title: "Transformation Does Not Match Registration"
date: 2017-06-15
url: https://discourse.slicer.org/t/512
---

# Transformation does not match registration

**Topic ID**: 512
**Date**: 2017-06-15
**URL**: https://discourse.slicer.org/t/transformation-does-not-match-registration/512

---

## Post #1 by @Ivan_Hidrovo (2017-06-15 19:41 UTC)

<p>Hello guys,</p>
<p>I have done a registration in the general registration module (BRAINS) and saved the transformation matrix in a text file. Using the transforms module, I now apply the same linear transformation to the original moving image of the registration, expecting it to match the output image of the registration but they do not. Can someone please help me understand why this happens?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2017-06-15 20:07 UTC)

<p>Try with latest nightly version.</p>
<p>What kind of transform did you create (linear, linear+bspline, …)?<br>
If you apply the transform to the moving image right after registration, is the alignment correct?<br>
By the images not matching you mean that in Slicer they don’t appear aligned?<br>
Can you reproduce this with built-in sample data sets (MRBrainTumor1, MRBrainTumor2)?<br>
Can you upload sample input data and results?</p>

---

## Post #3 by @Ivan_Hidrovo (2017-06-16 04:22 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I created a linear transformation and no the alignment is not correct. I am viewing them on matlab. My goal is to use the same transformation (from the registration) on an image of a different modality, but I was suspicious that slicer was not giving me the correct transformation. That is why I decided to apply the  linear transformation (from the registration) to the original moving image, expecting it to match (be aligned) to  the output image of the registration, but they do not. I will try to do reproduce this with the sample data sets.</p>

---

## Post #4 by @lassoan (2017-06-16 10:45 UTC)

<p>Are the images aligned correctly in Slicer, right after the registration is complete? If not then you need to tune the registration parameters or try using another registration module. For example, install Elastix extension and try “General registration (Elastix)” module. You may also try labdmark based registration (you define matching set of landmarks in both images and compute transform based on that), using Landmark registration module in Slicer core or Fiducial registration wizard module in SlicerIGT extension.</p>
<p>What kind of images you are trying to align? What anatomical part?</p>

---

## Post #5 by @Ivan_Hidrovo (2017-06-16 22:21 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I think I figured out the problem- I am just going to manually change the transformation values in the transforms module. But, now I am having trouble saving  (in .mhd format) the transformation after I apply the transformation. When I upload the <em>transformed</em>  image, I view the the old image (before it was transformed). Is there some bug present in saving transformations in the transforms module?</p>
<ul>
<li>I figured out that I need to “harden” the transform and then I can save it</li>
</ul>

---

## Post #6 by @lassoan (2017-06-16 23:40 UTC)

<p>If your software ignores image origin, orientation, or spacing then you must resample the transformed moving image in the fixed image’s coordinate system. See details here: <a href="https://www.slicer.org/wiki/Registration:Resampling">https://www.slicer.org/wiki/Registration:Resampling</a></p>

---

## Post #7 by @Marjaneh_Taghavi (2019-10-03 12:26 UTC)

<p>Hello Guys,</p>
<p>The goal of my project is to find the minimum margin between lesion and ablation zone from pre-ablation CT scan and post-ablation CT scan. To do that I need the registration post to pre CT scan.<br>
I’m using Elastix to registre post-ablation CT scan to pre-ablation CT scan. I have liver lesion and ablation zone segmentation as a label for both pre and post scan.<br>
For registration I resample CT scans and labels (lesion segmentation) into 512<em>512</em>512.<br>
For some patients the registration is good but for others is not good. Therefore, I load the registred CT scan and pre -ablation CT scan to correct the registrarion manually in the 3D slicer.<br>
I’ve saved the correct registration CT scan and label in nii.gz format.<br>
The problem is here:<br>
When I load the Correction regitration CT and its label in 3D slicer and also in ITK snap, they are similar.<br>
But when I load correction registation CT and pre-label CT scan, they are not the same in 3D slicer and ITK snap anymore.<br>
Can anyone give me a hint where could be a problem?</p>

---

## Post #8 by @lassoan (2019-10-03 12:49 UTC)

<p>From this much information we cannot guess what is happening.</p>
<ul>
<li>What do you exactly when you “correct the registrarion manually in the 3D slicer”?</li>
<li>Do you apply the registration transform on the CT scan?</li>
<li>Do you resample the CT scan?</li>
<li>Can you post screenshots to show what you mean by “they are not the same in 3D slicer and ITK snap anymore”?</li>
<li>Does all the data show up at the position you expect in 3D Slicer?</li>
<li>Does ITK-Snap display correct if you saved everything in .nrrd format?</li>
<li>Is there any specific processing or analysis step that you want to do in ITK-Snap instead of Slicer or you are just interested in general why position is different in ITK-Snap and Slicer?</li>
<li>Can you share an example scene (save as .mrb file - by clicking on the package icon in Sava data window)? Make sure no patient information is included - you can download public datasets from TCIA.</li>
</ul>

---

## Post #9 by @Marjaneh_Taghavi (2019-10-03 13:38 UTC)

<p>Thank you for your quick reply, I’ll answer your questions one by one:</p>
<ol>
<li>I go to Data icon and in Transform hierarchy, right-click on old registration (which I want to correct it) and select instert transform which creates new nodes called LinearTransform_3. Then click the Transforms, select the LinearTransform_3 and play with the Translation option until the registration will be correct.  then I click on Harden transform for both CT registration and label and then save them.</li>
<li>Yes, I apply the registration on CT scans</li>
<li>when I load the correct registration which I’ve saved in the 3D slicer and ITK snap, they are the same (the slices and the location), but when I load the pre-label scan on top of them, the location of the label is not the same.</li>
<li>Yes, in 3D slicer everything is perfect as I did registration manually and save them.</li>
<li>yes, I also try to save them in .nrrd format, it has the same problem.</li>
<li>Yes, I need to load the images in the python and find the minimum margin between the liver lesion and the ablation zone.<br>
I’ll try to make an example scene as well.<br>
Thanks,<br>
Marjaneh</li>
</ol>

---

## Post #10 by @lassoan (2019-10-03 14:36 UTC)

<p>There does not seem to be anything wrong with your workflow, so the example scene would be very useful.</p>
<p>You can get minimum margin by exporting segmentations to models, running Model to model distance module (provided by Model to model distance extension), get the point scalars as numpy array, and get the minimum value (or histogram, etc.). It can all be python-scripted within Slicer, probably in 20-30 lines.</p>

---

## Post #11 by @Marjaneh_Taghavi (2019-10-03 15:19 UTC)

<p>Thanks for your reply.<br>
I had a discussion with <a class="mention" href="/u/joostjm">@JoostJM</a> in our office, and we found the problem. The origin of manual registration was different from the pre-label scan. And 3D slicer could recorrect for that while ITK cannot. So I need to change the origin of manual registration into the original pre-image.</p>
<p>Thanks for your time:)<br>
Marjaneh</p>

---
