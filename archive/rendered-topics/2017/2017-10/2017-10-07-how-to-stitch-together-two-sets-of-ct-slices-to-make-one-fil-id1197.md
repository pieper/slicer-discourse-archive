---
topic_id: 1197
title: "How To Stitch Together Two Sets Of Ct Slices To Make One Fil"
date: 2017-10-07
url: https://discourse.slicer.org/t/1197
---

# How to stitch together two sets of CT slices to make one file

**Topic ID**: 1197
**Date**: 2017-10-07
**URL**: https://discourse.slicer.org/t/how-to-stitch-together-two-sets-of-ct-slices-to-make-one-file/1197

---

## Post #1 by @Noemi_Perez (2017-10-07 20:02 UTC)

<p>Operating system: Mac OS X 10.10<br>
Slicer version: 4.6.2<br>
Expected behavior: I import a folder with 421 DICOM slices that should show all of the cranium and mandible of an individual<br>
Actual behavior: The program says that 421 slices have been successfully loaded, when the files of the individual are loaded, the upper part of the cranium is cut out, so it doesn’t show.</p>
<p>Is there a limit of images that can be loaded? How should I solve this problem?? Thank you very much in advance</p>

---

## Post #2 by @cpinter (2017-10-07 20:56 UTC)

<p>Do you know if the DICOM series has a uniform slice thickness? The symptom you mention has occurred with datasets with non-uniform slice thickness.</p>
<p>In any case, please try it out again with the latest nightly, 4.6.2 is almost a year old now. Thanks!</p>

---

## Post #3 by @Noemi_Perez (2017-10-08 08:54 UTC)

<p>Thank you very much, I’ve downloaded the newest version of the program and now I realised that the problem is that each individual is comprised of two series of CT scans, I have been looking for an explanation or a tutorial on how to stitch these two sets together but so far I haven’t found anything. Is it possible to do it with Slicer??</p>
<p>EDIT: I’m going to change the name of the topic to make it more accurate</p>

---

## Post #4 by @cpinter (2017-10-08 16:04 UTC)

<p>Thanks for the update, it seems we are making progress! Also thanks for changing the title.</p>
<p>Stitching the volumes is possible, but it won’t be trivial. I imagine the major steps will be these:</p>
<ol>
<li>Make sure the two volumes align. If showing them together (set one as background, the other as foreground with 50% opacity) shows overlap, or the two parts are otherwise do not align, then a transform needs to be created to make them align perfectly (create linear transform in Transforms module, set it to one of the volumes, and tweak the transform until alignment is reached)</li>
<li>Resample the volumes to a common frame of reference. Need to create an empty volume that spans both images, ideally in a way that the voxels do not need to be interpolated. I’d try to do this with the Crop Volume module, but I’m not sure that a ROI larger than the cropped image is handled. Then both volumes need to be resampled to this common frame of reference with Resample Image (BRAINS).</li>
<li>Add the two volumes together with Add Scalar Volumes</li>
</ol>
<p>The exact details of these steps will need to be figured out. Let us know how it goes.</p>

---

## Post #5 by @Noemi_Perez (2017-10-08 17:08 UTC)

<p>First of all, thank you again! The thing is that when I load the folder with all of the images Slicer just recognises one patient, and it’s always the same part of the CT scan. I realised the folder contained two different scans because I tried opening the folder in Mimics 10.1, which “made me” choose to load one of the sets.<br>
I’m sorry for all of the trouble, I’m fairly new to using Slicer so I’m still getting used to it</p>

---

## Post #6 by @cpinter (2017-10-08 17:24 UTC)

<p>No worries! Let us know if you have further quetsions.</p>

---

## Post #7 by @lassoan (2017-10-09 14:47 UTC)

<p>If multiple series are stored in a folder or files of a series is spread across multiple folders then you need to use the DICOM module to import it. It will show you a similar patient/study/series selector as Mimics.</p>

---

## Post #8 by @Noemi_Perez (2017-10-17 08:56 UTC)

<p>Thank you very much for your answer.<br>
The problem is that it just recognises one patient and shows just one of the halves, whereas Mimics recognises two different sets. I’m still trying to open both halves at the same time to try to stitch both parts together.</p>

---

## Post #9 by @lassoan (2017-10-17 11:34 UTC)

<p>To see both sets, you need to import the folder into Slicer (drag-and-drop the folder and choose to import as DICOM), then load it using the DICOM browser. See details here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM</a></p>

---

## Post #10 by @kayarre (2018-03-30 19:57 UTC)

<p>What about if there is a large region of overlap? How can I get either the average, max, or some kind of boolean, i.e. pick volume A over B except where A = -1024</p>

---

## Post #11 by @lassoan (2018-03-31 01:31 UTC)

<p>You can get images as numpy arrays, so you can very easily combine them in any way you want using numpy operations.</p>
<p>Just a few illustrative examples (I haven’t tested these expressions, so syntax may not be fully correct, but something similar should work):</p>
<p>Get minimum of two images: <code>imageCombined = numpy.minimum(imageA,imageB)</code></p>
<p>Get image A voxels if it is above a certain intensity threshold, otherwise return the mean of image A and B: <code>imageCombined = numpy.where(imageA&gt;1500, imageA, (imageA+imageB)/2.0)</code></p>

---

## Post #12 by @Alex_Wiley (2018-05-24 13:02 UTC)

<p>I am trying to piece together multiple VTK files. When I go to add scalar volumes, its says completes with errors.</p>

---

## Post #13 by @lassoan (2018-05-27 18:44 UTC)

<p>You have to follow the instructions above. Most importantly: resample the volumes using the same reference volume (to make them have the same origin, spacing, axis directions, and extent).</p>

---

## Post #14 by @Alex_Wiley (2018-05-29 14:43 UTC)

<p>When performing BRAINSresample it is saying completed with error and indicates that it was only performed with 1.</p>

---

## Post #15 by @lassoan (2018-05-29 16:48 UTC)

<p>Do you use the latest stable version (Slicer-4.8.1)? Can you attach a screenshot of the BRAINSresample  module user interface to see how you set your inputs and outputs?</p>

---

## Post #16 by @lassoan (2022-10-20 15:09 UTC)

<p>Just in case somebody comes across this topic now: <a class="mention" href="/u/mikebind">@mikebind</a> recently contributed the <a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes">Stitch Volumes module</a> for stitching multiple volumes into one. It is available in Sandbox extension.</p>

---

## Post #17 by @Unicom (2025-10-16 01:36 UTC)

<p>Just in case somebody comes across this topic now:</p><aside class="onebox githubrepo" data-onebox-src="https://github.com/PerkLab/SlicerSandbox#stitch-volumes">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/f05ce5acee24819701d297eb33bb9e51/PerkLab/SlicerSandbox#stitch-volumes" class="thumbnail">

  <h3><a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes" target="_blank" rel="noopener nofollow ugc">GitHub - PerkLab/SlicerSandbox: Collection of utilities that are not polished...</a></h3>

    <p><span class="github-repo-description">Collection of utilities that are not polished implementations but can be useful to users</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
The tool was built only for 3D image volumes; it would likely require source code modification before it could work for blending 2D images.</p>

---
