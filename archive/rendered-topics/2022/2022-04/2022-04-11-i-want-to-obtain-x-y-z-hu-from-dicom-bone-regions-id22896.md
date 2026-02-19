---
topic_id: 22896
title: "I Want To Obtain X Y Z Hu From Dicom Bone Regions"
date: 2022-04-11
url: https://discourse.slicer.org/t/22896
---

# I want to obtain x,y,z,HU from DICOM(bone regions)

**Topic ID**: 22896
**Date**: 2022-04-11
**URL**: https://discourse.slicer.org/t/i-want-to-obtain-x-y-z-hu-from-dicom-bone-regions/22896

---

## Post #1 by @kookoo9999 (2022-04-11 02:45 UTC)

<p>I want to obtain bone regions of each coordinate(x,y,z,HU) from DICOM.<br>
You can see my source at <a href="https://github.com/kookoo9999/HounsFieldUnit" rel="noopener nofollow ugc">here</a>.<br>
I use input volume from DICOM loaded, and input segment from segment of DICOM.<br>
so I obtain x,y,z,HU and display each x,y,z , but result like photo is not I want .<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2da04bcd6b8beec64c407ef8aaaa651f5651858.png" data-download-href="/uploads/short-url/neEs4d7QxwglT81DrsQ6zTdadfy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2da04bcd6b8beec64c407ef8aaaa651f5651858_2_690x347.png" alt="image" data-base62-sha1="neEs4d7QxwglT81DrsQ6zTdadfy" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2da04bcd6b8beec64c407ef8aaaa651f5651858_2_690x347.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2da04bcd6b8beec64c407ef8aaaa651f5651858_2_1035x520.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2da04bcd6b8beec64c407ef8aaaa651f5651858.png 2x" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1345×678 36 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Did I do anything wrong to obtain coordinate(x,y,z,HU) from DICOM?</p>

---

## Post #2 by @lassoan (2022-04-11 20:48 UTC)

<p>(x,y,z,HU) would be an incredibly inefficient representation of segmented structures. Segmentations are stored in a much better, memory-efficient and processing-friendly 3D array representation. You can compute anything you need from this array. What is your end goal?</p>

---

## Post #3 by @kookoo9999 (2022-04-12 00:37 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Thanks for reply!<br>
I want to obtain every coordinate(x,y,z,hu) of a full-bodied bone from DICOM.<br>
If I want to obtain full-bodied bone’s ever coordinate ,  Am I doing it right?</p>

---

## Post #4 by @kookoo9999 (2022-04-12 01:45 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44c95417afd04f2c05500c2148ae03dd7f39f214.png" data-download-href="/uploads/short-url/9OvOmpS64BsjFWz5bp5l3Vv0aws.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44c95417afd04f2c05500c2148ae03dd7f39f214_2_690x373.png" alt="image" data-base62-sha1="9OvOmpS64BsjFWz5bp5l3Vv0aws" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44c95417afd04f2c05500c2148ae03dd7f39f214_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44c95417afd04f2c05500c2148ae03dd7f39f214_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44c95417afd04f2c05500c2148ae03dd7f39f214_2_1380x746.png 2x" data-dominant-color="B3B4BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 203 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Using the DICOM file and the segmented area, I want to get all the coordinates (x, y, z) of the green area shown in the picture and the corresponding HU value</p>

---

## Post #5 by @pieper (2022-04-12 12:43 UTC)

<p>It sounds like you are looking for this script:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html?highlight=numpy.where#get-the-values-of-all-voxels-for-a-label-value" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html?highlight=numpy.where#get-the-values-of-all-voxels-for-a-label-value</a></p>

---

## Post #6 by @kookoo9999 (2022-04-12 13:52 UTC)

<p>Thanks for reply.<br>
I checked the script you mentioned, but I didn’t get all the x,y,z,hu of the segment I wanted.<br>
You can check my code at <a href="https://github.com/kookoo9999/HounsFieldUnit" rel="noopener nofollow ugc">here</a>.</p>

---

## Post #7 by @pieper (2022-04-12 14:00 UTC)

<p>I’m not sure where in your code to look.  The <code>numpy.where</code> command and related lines in the link I sent should give you what I understand you are looking for.</p>

---

## Post #8 by @kookoo9999 (2022-04-12 14:18 UTC)

<p>Thanks for reply!<br>
You can check my code at <a href="https://github.com/kookoo9999/HounsFieldUnit/blob/main/HounsFieldUnit.py" rel="noopener nofollow ugc">here</a> from 360 line.<br>
and result .csv of coordinate  you can check <a href="https://github.com/kookoo9999/HounsFieldUnit" rel="noopener nofollow ugc">here</a> (ex : <a href="https://github.com/kookoo9999/HounsFieldUnit/blob/main/Extraction_IJK_of_HU(DCM).csv" rel="noopener nofollow ugc">Extraction_IJK_of_HU(DCM).csv</a>, <a href="https://github.com/kookoo9999/HounsFieldUnit/blob/main/volumes.csv" rel="noopener nofollow ugc">volumes.csv</a>).</p>

---

## Post #9 by @cpinter (2022-04-12 15:41 UTC)

<p>We can only guess here but maybe what you really need is the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html">Segment Statistics module</a>.</p>

---

## Post #10 by @kookoo9999 (2022-04-12 16:29 UTC)

<p>Thanks for reply.<br>
I used Segment Statics Module for obtain x,y,z,hu but this module does not provide.</p>

---

## Post #11 by @cpinter (2022-04-12 16:57 UTC)

<p>What you keep describing (x,y,z,HU) cannot possibly be your end goal. It would help us a lot if you explained what it is actually that you want to achieve.</p>

---

## Post #12 by @kookoo9999 (2022-04-13 00:07 UTC)

<p>My goal is to obtain the coordinates of all the voxels in the bone, including the HU value (ex: x,y,z,HU), as shown in the picture in the text. When taking the currently extracted coordinates (Point Cloud), the scale does not seem to fit better than it does on the Slicer. It is difficult for me to understand that the number of voxels in the Segment Statistics module is the same.</p>

---

## Post #13 by @lassoan (2022-04-14 00:29 UTC)

<p>Getting a list of (x,y,z,HU) values is the <em>first step</em> of your data processing workflow. We would like to know what you plan to use these values for and ultimately what is the <em>end goal</em>, what would you like to compute from these values, what is that you want to display to your end users.</p>
<p>The reason is that most relevant clinical problems are not new and there are plenty of known, reasonably good solutions to common problems that you can use as a starting point. We would rather help you finding relevant prior work to build on, instead of assisting with reimplementing a new, potentially suboptimal method.</p>

---

## Post #14 by @kookoo9999 (2022-04-14 01:10 UTC)

<p>Thanks for reply <a class="mention" href="/u/lassoan">@lassoan</a> .<br>
I want to get Femur’s x,y,z,hu values from DICOM for finite element analysis.<br>
Currently, the labelMapNode was constructed using VolumeNode and SegmentNode, and the value thought to be x, y, z was obtained, which I think is a different coordinate system as shown in the picture. So I thought I should convert this into RAS coordinates, so I tried looking <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-centroid-of-a-segment-in-world-ras-coordinates" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a> and edit my code at <a href="https://github.com/kookoo9999/HounsFieldUnit/blob/main/HounsFieldUnit.py" rel="noopener nofollow ugc">HounsFieldUnit.py</a> from 360 line , but it’s not working.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37b25acc0d354c67cb05fc6ed5c7a81364f3d634.png" data-download-href="/uploads/short-url/7WInO7lIiKGsGURyZqzAWICM0KM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37b25acc0d354c67cb05fc6ed5c7a81364f3d634_2_690x362.png" alt="image" data-base62-sha1="7WInO7lIiKGsGURyZqzAWICM0KM" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37b25acc0d354c67cb05fc6ed5c7a81364f3d634_2_690x362.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37b25acc0d354c67cb05fc6ed5c7a81364f3d634_2_1035x543.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37b25acc0d354c67cb05fc6ed5c7a81364f3d634_2_1380x724.png 2x" data-dominant-color="B4B5BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1912×1004 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @lassoan (2022-04-15 12:24 UTC)

<aside class="quote no-group" data-username="kookoo9999" data-post="14" data-topic="22896">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kookoo9999/48/12394_2.png" class="avatar"> kookoo9999:</div>
<blockquote>
<p>I want to get Femur’s x,y,z,hu values from DICOM for finite element analysis.</p>
</blockquote>
</aside>
<p>Thank you, this is very important information. This confirms that, as expected, you should not try to create this (x, y, z, hu) point list. It takes you farther from achieving your goal.</p>
<p>You can create a volumetric mesh suitable for finite element analysis using <code>SegmentMesher</code> extension. You can then use <code>Probe volume with model</code> module to get HU values at each mesh point. The result is a FEM-ready mesh. If your finite element analysis software cannot use a mesh in vtu or vtk format then you can consider using a different engine (such as FEBio) or use <a href="https://pypi.org/project/meshio/"><code>meshio</code> Python package</a> or write custom code to convert to a different volumetric mesh format.</p>

---

## Post #16 by @leeyrics (2022-08-17 13:36 UTC)

<p>thanks <strong>kookoo9999s</strong> und your reply about the quetions and information.</p>
<p>I have the same problem like <strong>kookoo9999</strong> , the end goal is to calculate the density of each coordinate point (x, y, z), that why <strong>kookoo9999</strong> wants to get the point list (x, y, z, hu), because there is a formula between HU and density.</p>
<p>now there is a new way you provided to use <em>segmentmesher</em>. my steps are:</p>
<ol>
<li>install <em>segmentmesher</em> 2. use <em>segmentmesher</em> clever function 3. use <em>volume with model</em><br>
but there is an error as attachment shown. Is there something wrong with my operation?</li>
</ol>
<p>looking forward to your reply and many thanks <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3a4e18a0650ab3e4329d53f575ca5a544a768c9.png" data-download-href="/uploads/short-url/pDcIPMV81C2OjmP1fNePhhnhjcd.png?dl=1" title="12345" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3a4e18a0650ab3e4329d53f575ca5a544a768c9_2_690x373.png" alt="12345" data-base62-sha1="pDcIPMV81C2OjmP1fNePhhnhjcd" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3a4e18a0650ab3e4329d53f575ca5a544a768c9_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3a4e18a0650ab3e4329d53f575ca5a544a768c9_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3a4e18a0650ab3e4329d53f575ca5a544a768c9_2_1380x746.png 2x" data-dominant-color="47484B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">12345</span><span class="informations">1920×1040 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #17 by @kookoo9999 (2022-08-18 00:36 UTC)

<p><a class="mention" href="/u/leeyrics">@leeyrics</a> , I’m glad my issue looks helpful for you.<br>
I don’t know segmentmesher module and it’s usage in 3d slicer. Is it python script module for command line??</p>

---

## Post #18 by @lassoan (2022-08-18 11:48 UTC)

<aside class="quote no-group" data-username="leeyrics" data-post="16" data-topic="22896">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leeyrics/48/16329_2.png" class="avatar"> leeyrics:</div>
<blockquote>
<p>I have the same problem like <strong>kookoo9999</strong> , the end goal is to calculate the density of each coordinate point (x, y, z), that why <strong>kookoo9999</strong> wants to get the point list (x, y, z, hu), because there is a formula between HU and density.</p>
</blockquote>
</aside>
<p><code>Probe model with volume</code> module does exactly this: it saves the HU value to each model point.</p>
<aside class="quote no-group" data-username="leeyrics" data-post="16" data-topic="22896">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leeyrics/48/16329_2.png" class="avatar"> leeyrics:</div>
<blockquote>
<p>there is an error as attachment shown. Is there something wrong with my operation?</p>
</blockquote>
</aside>
<p>The error message indicates that the model node that you retrieved by the <code>Output model</code> name is empty. Double-check that the <code>Probe Volume with Model</code> input <code>Model</code> is valid, then click <code>Apply</code>, <strong>wait for the processing to complete</strong>,  check that the resulting <code>Output Model</code> looks good, and then run your script.</p>

---
