# Lung airway segmentation

**Topic ID**: 2467
**Date**: 2018-03-29
**URL**: https://discourse.slicer.org/t/lung-airway-segmentation/2467

---

## Post #1 by @anitakh1 (2018-03-29 07:52 UTC)

<p>i want to use lung airway segmentation tool in 3D slicer but i can’t find it in the slicer i downloaded. pl help</p>

---

## Post #2 by @pieper (2018-03-29 12:50 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://chestimagingplatform.org/workstation-slicer-cip">
  <header class="source">
      <img src="https://chestimagingplatform.org/profiles/openscholar/themes/hwpi_basetheme/favicon.png" class="site-icon" width="32" height="32">

      <a href="https://chestimagingplatform.org/workstation-slicer-cip" target="_blank" rel="noopener">chestimagingplatform.org</a>
  </header>

  <article class="onebox-body">
    <img src="https://chestimagingplatform.org/" class="thumbnail" width="" height="">

<h3><a href="https://chestimagingplatform.org/workstation-slicer-cip" target="_blank" rel="noopener">Workstation (SlicerCIP)</a></h3>

  <p>Extension to the Slicer that integrates:</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @anitakh1 (2018-03-29 14:07 UTC)

<p>i am quite new to 3d slicer. when i am viewing RGB image set, it’s giving me R G B values separately. pl tell me how to find HU at different locations</p>

---

## Post #4 by @anitakh1 (2018-03-29 14:07 UTC)

<p>thanks for workstation info</p>

---

## Post #5 by @pieper (2018-03-29 15:49 UTC)

<aside class="quote no-group" data-username="anitakh1" data-post="3" data-topic="2467" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anitakh1/48/3350_2.png" class="avatar"> anitakh1:</div>
<blockquote>
<p>i am quite new to 3d slicer. when i am viewing RGB image set, it’s giving me R G B values separately. pl tell me how to find HU at different locations</p>
</blockquote>
</aside>
<p>Sorry, you’ll need to provide more detail if you need help (what data you loaded, how you loaded it, what you expected to see and what you see instead).  Sometime screenshots help (but no patient-identifiable data please).  If your data is RGB typically the mapping back to HU is not recoverable.</p>

---

## Post #6 by @anitakh1 (2018-03-30 04:50 UTC)

<p>one more thing. i have downloaded workstation CIP but how to add it in 3D slicer??</p>

---

## Post #7 by @lassoan (2018-03-31 01:36 UTC)

<p>Download “Slicer with CIP integrated” - that contains a Slicer distribution that already contains CIP modules.</p>

---

## Post #8 by @anitakh1 (2018-04-02 05:35 UTC)

<p>thanks, could install slicer with CIP integrated. i am in the learning stage and working on airway and vessel segmentation of lung CT dicom images. i have segmented out the lung lobes. as airways and vessels are very different than bone, what strategy should i follow. moreover as i am doing phd, for research will it be enough if i use slicer tools for segmentation or i have to do coding. i am quite new, sorry if i sound stupid.</p>

---

## Post #9 by @anitakh1 (2018-04-02 09:10 UTC)

<p>one more thing. i did some vessel segmentation work on jpeg image set using matlab. is there any way to view its 3D view in 3D slicer?</p>

---

## Post #10 by @lassoan (2018-04-02 13:05 UTC)

<p>Saving 3D medical images as a sequence of JPEG files leads to many problems (decreased image quality: bit depth limited to 8 bits or less, potential compression artifacts; no slice spacing information, no anatomical image orientation information; etc). Instead, you can use image file formats that are developed for this purpose and widely supported by all medical image computing applications, such as NRRD.</p>
<p>You can find Matlab reader and writer for NRRD files here: <a href="https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver">https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver</a></p>
<p>You can also run your Matlab functions directly from Slicer using MatlabBridge extension:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge</a></p>

---

## Post #11 by @lassoan (2018-04-02 13:15 UTC)

<aside class="quote no-group" data-username="anitakh1" data-post="8" data-topic="2467">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anitakh1/48/3350_2.png" class="avatar"> anitakh1:</div>
<blockquote>
<p>as airways and vessels are very different than bone, what strategy should i follow</p>
</blockquote>
</aside>
<p>Could you please clarify segmentation of what structures you would like to get advice on?</p>

---

## Post #12 by @anitakh1 (2018-04-04 07:44 UTC)

<p>thanks for very informative words. i added MatlabBridge into 3D slicer and trying to understand. i have my own codes written in matlab, can i run these codes through MatlabBridge or have to use modules available.</p>
<p>moreover i have one serious problem. i have dicom data by the name ‘dicom_021.dcm’ with header file ‘dicom_021.mhd’. dicom_021.dcm contains all 459 dicom images but i can’t view it as dicom folder showing separate dicom images. how can i achieve that. actually i want to take images one by one and process them using my matlab code.</p>

---

## Post #13 by @anitakh1 (2018-04-04 07:45 UTC)

<p>actually i am working on CT lung airways and blood vessel segmentation.</p>

---

## Post #14 by @cpinter (2018-04-04 14:24 UTC)

<p>Yes, you can run your own Matlab code using Matlab Bridge. After you generate your module skeleton you can call your function from the module’s Matlab file. There are nice tutorials, even videos in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge">page</a> <a class="mention" href="/u/lassoan">@lassoan</a> linked above.</p>
<p>Have you tried loading that DICOM with Slicer? You can do it in the DICOM module: in the browser that pops up you need to import the folder containing the DICOM files and the patient/study/series will appear in the browser. Once you load it, you have access to the 3D image data, which is then transferred to Matlab by Matlab Bridge (from the module you generate).</p>

---

## Post #15 by @anitakh1 (2018-04-06 06:05 UTC)

<p>thank you sir. i made a segmentation program on matlab for jpeg images. but now as i have to work on dicom images, i converted the whole lot into nifti ‘.nii’ and ran my program. i saved each individual output as .nii image in a folder. so now i have some 300 .nii segmented outputs. how can i do volume rendering to view the segmented output in volume form? i tried but slicer is taking single .nii image at a time.</p>

---

## Post #16 by @lassoan (2018-04-06 11:38 UTC)

<p>Unless you work with brain images (where nii is probably the most widely used file format), I would recommend to use nrrd file format instead of nii, because nrrd is a somewhat simpler and better specified file format, which has better support in Slicer. You can find nrrd reader and writer for Matlab here: <a href="https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver">https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver</a></p>
<p>Since you work with volumetric images, you must save the image as a 3D volume (so that you can specify position, orientation, and voxel size in 3D). The nrrdwrite.m script that I referenced above can save a 3D Matlab matrix as a single 3D nrrd file, which Slicer can load and render as a volume.</p>

---

## Post #17 by @anitakh1 (2018-04-09 07:30 UTC)

<p>thanks for your valuable advice. sir i am learning to use matlab with slicer and trying to understand how to do that. but i am not getting the essence. i have my matlab code which starts like…</p>
<p>“im_mask = nrrdread(‘C:/Users/ND_Londhe/Desktop/lung_mask.nrrd’);”<br>
and then i have to take images one by one and apply segmentation program which follows. but how to merge these codes in the module generated by module generator. do i have to transform codes in .m and XML file to be read by slicer. i followed the two videos but not understanding how to connect matlab and run codes from slicer. pl guide</p>

---

## Post #18 by @anitakh1 (2018-04-10 13:15 UTC)

<p>sir actually when i am making my own module using matlab module generator, it is showing threshold tabs. how to use my program and make it to run?</p>

---

## Post #19 by @cpinter (2018-04-10 13:39 UTC)

<p>You need to edit the XML so that the module UI contains the input fields you require. The threshold control is just part of the example.</p>
<p>This may help: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel#XML_Schema">https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel#XML_Schema</a></p>

---

## Post #20 by @anitakh1 (2018-04-11 06:29 UTC)

<p>thank you. i will try to understand. sir how can i see two image sets one over other?</p>

---

## Post #21 by @anitakh1 (2018-04-11 07:20 UTC)

<p>one more thing sir. i am loading and viewing dicom image as ‘dicom_021.dcm’ containing some 450 images. is it possible to convert it to ‘dicom_021/<em>.dcm’ where '</em>’ represents 459 image set using slicer. hope i have put my question correctly</p>

---

## Post #22 by @anitakh1 (2018-04-11 12:18 UTC)

<p>sorry. Actually i wrote convert to dicom_021/*.dcm’. don’t know why * didn’t show in my earlier message</p>

---

## Post #23 by @lassoan (2018-04-11 13:22 UTC)

<blockquote>
<p>Actually i wrote</p>
</blockquote>
<p>You can go back and edit your posts. Please do so instead of writing additional posts.</p>
<p><code>*</code> is a formatting character in markdown. If you need verbatim display of text containing formatting characters then select the text and click <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f47e5506cce2c2cfb0575f82414e6a5f486c761.png" alt="image" data-base62-sha1="mJ3X8e9oW7bZ01tAguujQc9IV1f" width="21" height="25"> button in the editor.</p>

---

## Post #24 by @lassoan (2018-04-18 14:13 UTC)

<p>A post was split to a new topic: <a href="/t/show-two-volumes-overlaid/2626">Show two volumes overlaid</a></p>

---

## Post #25 by @anitakh1 (2018-04-20 06:41 UTC)

<p>sir i have attempted lung vessel segmentation. how can i remove very smallbroken pieces of segmented results and also make vessels smooth using slicer?</p>

---

## Post #26 by @anitakh1 (2018-04-26 09:06 UTC)

<p>how can i view int16 dicom images with HU units in 3D slicer. many codes are with Hu units of dicom images.<br>
sorry to ask but are my questions not relevant to be answered sir.<br>
regards</p>

---

## Post #27 by @pieper (2018-04-26 21:30 UTC)

<p>Slicer should be displaying HU if the dicom header is correct.  Do you have a reason to think the pixels are not in HU?</p>

---

## Post #28 by @anitakh1 (2018-05-03 10:31 UTC)

<p>thanks for reply<br>
sir i want to know two things:</p>
<ol>
<li>how to give seed points in simple region growing module</li>
<li>after region growing, how can i find areas of segmented region and remove areas smaller than a threshold.<br>
pl suggest</li>
</ol>

---

## Post #29 by @pieper (2018-05-03 12:09 UTC)

<p>Hi <a class="mention" href="/u/anitakh1">@anitakh1</a> - have a look at the segmentation tutorials and documentation - you’ll find lots of ways to do define regions and use thresholds:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Training#Segmentation" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Training#Segmentation</a></p>
<p>Cheers,<br>
Steve</p>

---

## Post #30 by @anitakh1 (2018-05-15 12:55 UTC)

<p>hello. i am stuck badly. i did some segmentation work and stored the image volume as .nrrd using slicer. but when i am opening single images in matlab, image is opening in double format but pixel values as not between [0 1] (as is the case with double image in matlab) but in numbers like 45, 23 etc . this is creating problem for me to run an algorithm in matlab. pl help to read each image in matlab as double image between [0 1].</p>

---

## Post #31 by @lassoan (2018-05-19 15:14 UTC)

<p>You can use the nrrd file reader/writer (nrrdread.m and nrrd write.m) in Slicer MatlabBridge, which work correctly: <a href="https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver">https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver</a></p>
<p>Note that segmentation result is stored in a 4D array, each segment is a 3D array in it.</p>
<p>You may use Slicer’s MatlabBridge extension for running Matlab functions directly from Slicer: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge</a></p>
<p>At some point, you may consider moving from Matlab environment to Python, as there are much better and many more tools for medical image computing in Python packages and in Slicer and there are no licensing hassles.</p>

---

## Post #32 by @anitakh1 (2018-05-21 09:29 UTC)

<p>thanks a lot. sir can i get some training on slicer and matlab bridge module in india. it would be quite helpful</p>

---

## Post #33 by @lassoan (2018-05-23 16:07 UTC)

<p>A post was split to a new topic: <a href="/t/vessel-tracking-algorithm-on-lung-ct/2913">Vessel tracking algorithm on lung CT</a></p>

---

## Post #34 by @anitakh1 (2018-06-07 00:51 UTC)

<p>hello sir. can you please help me. i made some code and applied it on .raw volume data where pixel intensities were positive numbers. but rest of the data i have has HU units both positive and negative. my code is not working properly on these HU units. pl guide me how to get .raw file with all positive pixel values. i am not sure but some window level change is required i think. pl tell me how. my work has stopped because of that. regards</p>

---

## Post #35 by @lassoan (2018-06-07 02:26 UTC)

<p>How did you create the .raw file? How did you read it? Did you implement processing in Matlab, Python, or C++?</p>

---

## Post #36 by @anitakh1 (2018-06-07 03:12 UTC)

<p>I made code in python using simpleitk, numpy etc. but region growing works well when pixel intensity is &gt;0. So how to change pixel range of ,raw n make all positive. Thanks</p>

---

## Post #37 by @anitakh1 (2018-06-07 03:15 UTC)

<p>Sorry. I think u asked about file. Well i downloaded the file from vessel12 data n did 7zip to get .mhd n .raw folder but HU units are -&amp;+ as usual. I m reading it on slicer.</p>

---

## Post #38 by @lassoan (2018-06-07 04:03 UTC)

<aside class="quote no-group" data-username="anitakh1" data-post="36" data-topic="2467">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anitakh1/48/3350_2.png" class="avatar"> anitakh1:</div>
<blockquote>
<p>region growing works well when pixel intensity is &gt;0</p>
</blockquote>
</aside>
<p>Have you implemented region growing or you used SimpleITK or VTK filters?</p>

---

## Post #39 by @anitakh1 (2018-06-07 04:34 UTC)

<p>I used region growing using simpleitk command on raw images with pixel intensity above zero.</p>

---

## Post #40 by @lassoan (2018-06-07 11:46 UTC)

<p>Which SimpleITK command?</p>

---

## Post #41 by @anitakh1 (2018-06-11 05:13 UTC)

<p>connectedthreshold command of simpleitk. well i could solve my problem of changing intensity range. thanks a lot to have heeded my problem</p>

---

## Post #42 by @anitakh1 (2018-06-21 06:54 UTC)

<p>hello sir. can you please tell me how to get picture of axial and volume rendered images from 3D slicer to put in doc file?</p>

---

## Post #43 by @lassoan (2018-06-21 15:57 UTC)

<p>The simplest is to hit PrintScreen (PrtScn) key on your keyboard then switch to Word and hit Ctrl-V. For capturing videos or image sequences, you can also use <code>Screen Capture</code> module.</p>

---

## Post #44 by @lassoan (2018-07-10 14:08 UTC)

<p>A post was split to a new topic: <a href="/t/show-seed-points-on-3d-volume/3446">Show seed points on 3D volume</a></p>

---
