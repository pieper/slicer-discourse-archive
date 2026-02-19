---
topic_id: 540
title: "How To Convert Dicom Files To Nrrd"
date: 2017-06-20
url: https://discourse.slicer.org/t/540
---

# How to convert dicom files to nrrd

**Topic ID**: 540
**Date**: 2017-06-20
**URL**: https://discourse.slicer.org/t/how-to-convert-dicom-files-to-nrrd/540

---

## Post #1 by @Josiah_McAllister (2017-06-20 13:48 UTC)

<p>Operating system:Windows<br>
Slicer version:4.6.2<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @ihnorton (2017-06-20 13:49 UTC)

<p>Use the DICOM module to import the files, and then export as NRRD:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM</a></p>

---

## Post #3 by @Josiah_McAllister (2017-06-20 14:01 UTC)

<p>When I do that, only one of the three files saves as an nrrd. I need the<br>
segmentation to also be in nrrd form in order for it to be used by<br>
pyradiomics. How can I convert that segment then also to nrrd, as it is not<br>
a choice to save it as that.</p>

---

## Post #4 by @lassoan (2017-06-20 14:10 UTC)

<p>Export it to labelmap node using Segmentations module (Import/Export section).</p>

---

## Post #5 by @fedorov (2017-06-21 17:12 UTC)

<aside class="quote no-group" data-username="Josiah_McAllister" data-post="3" data-topic="540">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ccd318/48.png" class="avatar"> Josiah_McAllister:</div>
<blockquote>
<p>I need the<br>
segmentation to also be in nrrd form in order for it to be used by<br>
pyradiomics</p>
</blockquote>
</aside>
<p>If you are on Mac or Windows, you can also use SlicerRadiomics extension to calculate pyradiomics features. SlicerRadiomics works with either label maps, or segmentations.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/AIM-Harvard/SlicerRadiomics">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/AIM-Harvard/SlicerRadiomics" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/d9d6a3e987eef15295d2f5c3aa4dcbc0ba740c37d9866cecf7b8e92b541ab0aa/AIM-Harvard/SlicerRadiomics" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/AIM-Harvard/SlicerRadiomics" target="_blank" rel="noopener">GitHub - AIM-Harvard/SlicerRadiomics: A Slicer extension to provide a GUI...</a></h3>

  <p>A Slicer extension to provide a GUI around pyradiomics - GitHub - AIM-Harvard/SlicerRadiomics: A Slicer extension to provide a GUI around pyradiomics</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @Josiah_McAllister (2017-06-21 17:31 UTC)

<p>Do you know of anywhere I can go to learn how to use SlicerRadiomics? I now<br>
have it installed, but I cannot find how to use the extension.</p>

---

## Post #7 by @fedorov (2017-06-21 18:07 UTC)

<p>We have very basic usage instructions here: <a href="https://github.com/Radiomics/SlicerRadiomics/blob/master/USAGE.md#usage">https://github.com/Radiomics/SlicerRadiomics/blob/master/USAGE.md#usage</a></p>
<p>Are there specific issues where you are confused? It would be helpful to get some feedback what are exactly the challenges using the module.</p>

---

## Post #8 by @jfhartzell (2017-07-21 15:18 UTC)

<p>Hello, I’m new to Slicer<br>
Could you send updated instructions for how to convert a DICOM folder to NRRD?<br>
Thanks<br>
James</p>

---

## Post #9 by @cpinter (2017-07-21 17:35 UTC)

<p>Please refer to the <a href="https://discourse.slicer.org/t/how-to-convert-dicom-files-to-nrrd/540/2">comment</a> of <a class="mention" href="/u/ihnorton">@ihnorton</a></p>
<p>You can save the loaded DICOM volume as NRRD in the Save data dialog.</p>

---

## Post #10 by @b_s_umesh_sherkhane (2018-03-07 05:17 UTC)

<p>hello,i am on the same boat,i am looking at mass conversion of thousands of dicom files to nrrd.<br>
hence thought to use it in python script to automate it. is there any way that i can use command line slicer to mass convert dicom to nrrd ?</p>

---

## Post #11 by @cpinter (2018-03-07 14:39 UTC)

<p>You can load DICOM from python like this</p>
<pre><code>from DICOMLib import DICOMUtils
DICOMUtils.openDatabase('path/to/tempDatabase') # For batch processing it's better to use a  temporary database
DICOMUtils.loadPatientByUID(patientUID)
</code></pre>
<p>You can load patients by name, UID, and patient ID (an incremental integer Slicer assigns to imported patients), see <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMUtils.py#L105-L110">https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMUtils.py#L105-L110</a></p>
<p>Then you can save NRRD like this</p>
<pre><code>slicer.util.saveNode(node, 'fileName.nrrd')
</code></pre>
<p>For this you’ll need the MRML node which you can get in several ways, depending how you want your batch script to operate (for example dynamically with onNodeAdded, by getting the last volume node from the scene, or simply by closing scene after each save and get the only volume node)</p>

---

## Post #12 by @fedorov (2018-03-07 21:59 UTC)

<p>You can also consider one of the many tools out there that are much easier to use than Slicer for batch volume reconstruction (faster, easier to use, possibly more robust).</p>
<p>You can find a list of some of the most popular ones (incomplete, I am sure) here: <a href="https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/DICOMVolumeReconstruction/">https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/DICOMVolumeReconstruction/</a>.</p>
<p>A number of them (including Slicer converters) are set up in this dockerfile: <a href="https://github.com/QIICR/dcmheat/blob/master/docker/Dockerfile">https://github.com/QIICR/dcmheat/blob/master/docker/Dockerfile</a> (just noticed <a href="https://hub.docker.com/r/qiicr/dcmheat/">the corresponding container on Docker Hub</a> is broken, I need to fix that).</p>
<p>How they compare to each other and which specific one to recommend remains the open question (for me at least). As we make progress with the project referenced above, hopefully we will be able to recommend one specific tool, or say that all/subset of them are equivalent for practical purposes.</p>

---

## Post #13 by @pieper (2018-03-07 22:23 UTC)

<p>And just to make sure this is clear: converting DICOM to nrrd is not a simple well defined operation in general.  DICOM is a very expressive and flexible standard and there are several possibilities for any one collection of DICOM files:</p>
<ul>
<li>it may correspond to many nrrd files (e.g. different series in a study)</li>
<li>there may be more than one valid conversion and only the user knows which is preferred</li>
<li>it may not be possible for nrrd to represent the DICOM data (such as a DICOM structured report or something)</li>
</ul>
<p>That said, if you are dealing with a fairly standard case like converting one CT series to a nrrd scalar volume there are many good options as <a class="mention" href="/u/fedorov">@fedorov</a> points out.  It all depends on the data and what you hope to use it for.  Luckily there are lots of examples to learn from and by writing a script you can control the process to get what you need.</p>

---

## Post #14 by @S_Arbabi (2024-03-28 10:43 UTC)

<p>I created a nifti dataset (converting dicom to nifti using slicer), and trained an nnUNet segmentation model (with noMirroring trainer).<br>
in the inference time I use dicom2nifti for nifti generation from new dicom files, then I observe that the segmentation model does not work properly, providing bad segmentations.</p>
<p>I checked volume information of dicom:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fc35d4cb208ff9e7ee89b797bf75c12a53bc90f.png" alt="image" data-base62-sha1="dF9VpVtFuH11xKuLrW286STArPV" width="597" height="233"></p>
<p>volume information of dicom2nifti generated file:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/883af3d5de873b6abd8dbfe4cde82fd33b665bed.png" alt="image" data-base62-sha1="jr9eWKRvZDoQ71pmN9kSqKyIrVP" width="603" height="234"></p>
<p>and the volume information for a nifti volume I generate in slicer from the same dicom:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d5b0984ea787805433feb9be32a90aa71c43c9f.png" alt="image" data-base62-sha1="6tex0GVTbjVXoZArMp94GyNWJqv" width="603" height="237"></p>
<p>any ideas what is a workaround?</p>

---

## Post #15 by @pieper (2024-03-28 12:18 UTC)

<p>It looks like dicom2nifti (whichever one that is - I believe there are many tools with similar names) interprets the dicom differently than Slicer does.  Note that the IJK to RAS matrices differ as do the origins.  Probably these are the same geometry in terms of pixels ending up at the same places in space, but the layout of pixels in memory may be different (e.g. slices may be reversed) and it’s possible that the machine learning code doesn’t take this into account.</p>

---

## Post #16 by @S_Arbabi (2024-03-28 13:34 UTC)

<p>I believe the same is the case. What do you suggest to solve this? I can not run slicer on target machine so I have to convert to nifti using another package.</p>

---

## Post #17 by @dave3d (2024-03-28 13:52 UTC)

<p>I wrote a python script using SimpleITK that scans a directory for DICOM series and can convert any series it finds to NRRD (or Nifti).</p>
<p>Here’s a link to it on Github:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/dave3d/sitk_tools/blob/main/dicomseries.py">
  <header class="source">

      <a href="https://github.com/dave3d/sitk_tools/blob/main/dicomseries.py" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/dave3d/sitk_tools/blob/main/dicomseries.py" target="_blank" rel="noopener nofollow ugc">dave3d/sitk_tools/blob/main/dicomseries.py</a></h4>


      <pre><code class="lang-py">#! /usr/bin/env python

import sys
import getopt
import os
import SimpleITK as sitk

#
#  Scan a directory for DICOM series.
#
#  Can also covert all series to other formats with
#  the '--convert' flag.
#

verbose = 0
recFlag = False
suffix = ".nrrd"
min_z = 20
convertFlag = False
name_src = 1
</code></pre>



  This file has been truncated. <a href="https://github.com/dave3d/sitk_tools/blob/main/dicomseries.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
