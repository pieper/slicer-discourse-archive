---
topic_id: 6695
title: "No Conversion From Dwi To Dti"
date: 2019-05-05
url: https://discourse.slicer.org/t/6695
---

# no conversion from DWI to DTI

**Topic ID**: 6695
**Date**: 2019-05-05
**URL**: https://discourse.slicer.org/t/no-conversion-from-dwi-to-dti/6695

---

## Post #1 by @ecgt (2019-05-05 12:56 UTC)

<p>Operating system:Windows<br>
Slicer version:4.4.0<br>
Expected behavior:transform DWI to DTI<br>
Actual behavior:completed with errors<br>
MR: GE 3T</p>

---

## Post #2 by @ljod (2019-05-05 13:18 UTC)

<p>Hi we need a lot more information to help you. What version of Slicer? What exact modules did you use? In what order? What happened at the end and how did the output look? What was the error message? Thanks.</p>

---

## Post #3 by @ecgt (2019-05-05 13:58 UTC)

<p>I used the version 4.4.0 that I always use. I started with DICOM converter  and I converted to nrrd</p>
<p>It did that. After that I did the DWI to DTI conversion and ended up with Completed with errors and I cannot get further.</p>
<p>The file was from a 3T GE</p>
<p>I work with a 1.5 GE and with a 3T Siemens withot any problem</p>
<p>Thanks for helping!!!</p>
<p>Eduardo</p>

---

## Post #4 by @doc-xie (2019-05-05 14:07 UTC)

<p>Hi,Lauren,<br>
I think the problem is the same one as I come across some days before. The data of GE scanner should be converted into nifti with dcm2niix for tractography. So I think we should update or add some opinions in our dMRI module as soon as possible.<br>
Best wishes,<br>
Xie</p>

---

## Post #5 by @ecgt (2019-05-05 14:10 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/b/b968fe18406774405c516f34fcf0d7fbc14b83c3.jpeg" data-download-href="/uploads/short-url/qsdhcTYPgwnbY88RzmECmspubRx.jpeg?dl=1" title="16 components.JPG" rel="noopener nofollow ugc"><img width="436" height="291" alt="16 components.JPG" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b968fe18406774405c516f34fcf0d7fbc14b83c3_2_436x291.jpeg" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b968fe18406774405c516f34fcf0d7fbc14b83c3_2_436x291.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b968fe18406774405c516f34fcf0d7fbc14b83c3_2_654x436.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b968fe18406774405c516f34fcf0d7fbc14b83c3_2_872x582.jpeg 2x" data-dominant-color="8C8C8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">16 components.JPG</span><span class="informations">1277×851 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/b/b80af593a2a0e8fee7ad98323b436d5a203f7e03.jpeg" data-download-href="/uploads/short-url/qg7kKFdfAKJ2oLPySn0BIREAAhl.jpeg?dl=1" title="error.JPG" rel="noopener nofollow ugc"><img width="436" height="293" alt="error.JPG" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b80af593a2a0e8fee7ad98323b436d5a203f7e03_2_436x293.jpeg" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b80af593a2a0e8fee7ad98323b436d5a203f7e03_2_436x293.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b80af593a2a0e8fee7ad98323b436d5a203f7e03_2_654x439.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b80af593a2a0e8fee7ad98323b436d5a203f7e03_2_872x586.jpeg 2x" data-dominant-color="8D8D8D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error.JPG</span><span class="informations">1274×856 96.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I checked the components and there are 16 components .I use generally 37 components Can this be the cause?</p>
<p>Thanks</p>

---

## Post #6 by @ljod (2019-05-05 14:31 UTC)

<p>Hi Eduardo (and hello Dr. Xie!).</p>
<p>We have made a new module to replace DWIConvert moving forward. It has recently become available in Slicer nightly version. It is called SlicerDcm2nii and you can install it from the extension manager.</p>
<p>There is a lot of active development happening in the Slicer nightly right now. Today is a good download: I checked today’s dashboard and SlicerDMRI and SlicerDcm2nii and UKFTractography are all built.</p>
<p>Please do an experiment and download the nightly build version of Slicer and test this new SlicerDcm2nii module for converting your data. You shouldn’t need to remove your current Slicer to do this (you should be able to name this one differently and have two installations, for example).</p>
<p>Let us know how this works for you!</p>

---

## Post #7 by @ecgt (2019-05-05 22:11 UTC)

<p>I tried the SlicerDcm2nii and send an error message</p>
<p>I run the new software and finally it appears a dark image, bright margins</p>
<p>When doing FA there is a distorted image and DTI color shows areas of red , and grey, lokking distorted. I can recognize genu, splenium and cingulum in red.</p>
<p>Thanks!!</p>

---

## Post #8 by @ljod (2019-05-06 10:03 UTC)

<p>Hi this is not enough information for us to help.</p>
<p>What was the error message? Did you get any output DWI from SlicerDCM2nii? Did you use this output for anything?</p>
<p>What “new software” do you mean? What “image” were you viewing? (DWI? tensors?)</p>
<p>What do you mean by “distorted”? Spatially distorted? The wrong colors? Can you share a screenshot that does not contain any patient identifying information?</p>

---

## Post #9 by @ecgt (2019-05-06 11:25 UTC)

<p>I sent you the pictures but the mail was rejected because of the pictures</p>

---

## Post #10 by @ljod (2019-05-06 12:26 UTC)

<p>Thanks. I still cannot try to help because I cannot yet understand exactly what you did or what happened. Please do answer some of the questions above in my previous post. Also, if you go to the website you should be able to post updated pictures without needing email.</p>

---

## Post #11 by @doc-xie (2019-05-10 08:40 UTC)

<p>Hi Lauren,<br>
I have installed the nightly version and run the SlicerDcmenii. The module can work correctly, but sometimes the converted files can not be found in time. I do not know the reason about this. So I have to run the module several times. As a result, a lot of files are produced in the dictionary.  Why not set an additional opinion of “output dictionary” in the module?<br>
Best wishes,<br>
Xie</p>

---

## Post #12 by @ljod (2019-05-10 12:01 UTC)

<p>Hi Dr Xie. Thanks for trying the module!  The module converts to nrrd and loads this DWI into Slicer. The module should not change any DICOM dictionary at all. Could you please explain in more detail what steps you used and where you saw this dictionary output? What do you mean by dictionary? (You do not need to load the DICOM into slicer. Just give the dcm2nii module the DICOM directory or folder that only contains the DWI.)</p>

---

## Post #13 by @doc-xie (2019-05-16 08:27 UTC)

<p>Hi Lauren,<br>
I mean the converted files can not be found in the same DICOM dictionary. So I think we should add an output folder opinion that the converted files can be used correctly.  The details about this problem are belows.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52622beb19a7f0ec6d784c847d74f2eb47b759fd.png" data-download-href="/uploads/short-url/bKNu18fiM5GURXsNTBunjVx8ewl.png?dl=1" title="15%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52622beb19a7f0ec6d784c847d74f2eb47b759fd_2_690x292.png" alt="15%20PM" data-base62-sha1="bKNu18fiM5GURXsNTBunjVx8ewl" width="690" height="292" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52622beb19a7f0ec6d784c847d74f2eb47b759fd_2_690x292.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52622beb19a7f0ec6d784c847d74f2eb47b759fd_2_1035x438.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52622beb19a7f0ec6d784c847d74f2eb47b759fd_2_1380x584.png 2x" data-dominant-color="C6C7E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">15%20PM</span><span class="informations">2702×1144 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> !<br>
<a href="/404" data-orig-href="upload://9LNkzwWrWEJq2zpTXhNpsRmT5jz.png">09%20PM|690x479</a><br>
Best wishes,<br>
Xie</p>

---

## Post #14 by @doc-xie (2019-05-16 08:28 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/811d4b74fdd837c22d70b5695943a0bbf81f91b1.jpeg" data-download-href="/uploads/short-url/iqcm9SuXZMyMiSGVJGLNzxVCZGh.jpeg?dl=1" title="09%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/811d4b74fdd837c22d70b5695943a0bbf81f91b1_2_690x479.jpeg" alt="09%20PM" data-base62-sha1="iqcm9SuXZMyMiSGVJGLNzxVCZGh" width="690" height="479" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/811d4b74fdd837c22d70b5695943a0bbf81f91b1_2_690x479.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/811d4b74fdd837c22d70b5695943a0bbf81f91b1_2_1035x718.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/811d4b74fdd837c22d70b5695943a0bbf81f91b1_2_1380x958.jpeg 2x" data-dominant-color="D5D4E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">09%20PM</span><span class="informations">2718×1890 882 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
In the same folder, the converted files(bval bvec…) can not be found.</p>

---

## Post #15 by @ljod (2019-05-16 12:54 UTC)

<p>Hi Dr. Xie!</p>
<p>The module just loads the data into Slicer. Do you see the DWI data in Slicer after you run the module?</p>
<p>It does not save as bval and bvec. To save the data you can save from Slicer as nrrd. Will that work for your needs?</p>

---

## Post #16 by @doc-xie (2020-02-08 02:58 UTC)

<p>Sorry for my later reply.<br>
The dcm2niiGUI module works well for my data.<br>
Best wishes,<br>
Xie</p>

---
