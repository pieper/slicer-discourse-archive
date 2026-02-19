---
topic_id: 15782
title: "Surface Registration Original Stl With Cbct Converted To Stl"
date: 2021-02-01
url: https://discourse.slicer.org/t/15782
---

# Surface Registration (original STL with cbct converted to STL )

**Topic ID**: 15782
**Date**: 2021-02-01
**URL**: https://discourse.slicer.org/t/surface-registration-original-stl-with-cbct-converted-to-stl/15782

---

## Post #1 by @robertoruizmu (2021-02-01 19:23 UTC)

<p>Hi everyone!<br>
I´m trying to make a surface registration with 2 STL files:<br>
one STL obteined with an intraoral scanner , and the other STL is a numpy array(cbct) that I segmented and converted to STL with a code I made in python (not python in 3d slicer).</p>
<p>Both images cames from the same patient , but when I visualize them, they look in a different scale, so registration of surfaces failed. Here I leave some images of the result:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/3523761df5b098f2c5640bedbbffd8b82e2242c4.png" data-download-href="/uploads/short-url/7A5hsyh0Tl0iGJXDWn0tvl7cyLG.png?dl=1" title="surface_registration" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/3523761df5b098f2c5640bedbbffd8b82e2242c4.png" alt="surface_registration" data-base62-sha1="7A5hsyh0Tl0iGJXDWn0tvl7cyLG" width="423" height="500" data-dominant-color="9B98BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">surface_registration</span><span class="informations">506×597 26.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/2223664aeab9f27f81380748275c9c13432a010a.png" data-download-href="/uploads/short-url/4S04MW7Ixr1um19eGSBRB5wCvDI.png?dl=1" title="stl_surfaces" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/2223664aeab9f27f81380748275c9c13432a010a.png" alt="stl_surfaces" data-base62-sha1="4S04MW7Ixr1um19eGSBRB5wCvDI" width="664" height="500" data-dominant-color="9C9BC7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">stl_surfaces</span><span class="informations">813×612 26.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>thanks all.<br>
Operating system: windows 10<br>
Slicer version:4.11<br>
Expected behavior: optimal rgistration<br>
Actual behavior: the registration of surface fail due to de different scale .</p>

---

## Post #2 by @lassoan (2021-02-01 19:25 UTC)

<p>Which one has the correct scale: the surface scan or the CBCT? (you can measure distance using <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html">markups line</a>)</p>

---

## Post #3 by @robertoruizmu (2021-02-01 19:45 UTC)

<p>I think that STL from intraoral has the correct scale (about 50 mm from the last molar of left side to the last molar of right side ) because stl from cbct is about 100 mm.</p>
<p>(Also i measure the distance in the original cbct volume (100mm) and in the intraoral stl converted to volume(400mm), that because i wanna try volume registration too)</p>

---

## Post #4 by @lassoan (2021-02-01 20:01 UTC)

<p>CBCT manufacturers are known to be very bad in implementing the DICOM standard. Probably this is just yet another example. If this is a known issue then the DICOM Patcher module may fix it (see <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#image-is-stretched-or-compressed-along-one-axis">instructions</a>).</p>

---

## Post #5 by @robertoruizmu (2021-02-03 19:12 UTC)

<p>the problem is not de cbct , bacause I´ve just measured the distance between the two last molar  in the original dicom cbct file and is the same distance (50mm) as in STL file , so the problem appear when I go from dicom file to an array ( to make segmentation and preprocess image ) and then save the segmentation or make the surface .  how can I solve this problem ?</p>

---

## Post #6 by @muratmaga (2021-02-03 19:16 UTC)

<aside class="quote no-group" data-username="robertoruizmu" data-post="1" data-topic="15782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/9f8e36/48.png" class="avatar"> robertoruizmu:</div>
<blockquote>
<p>the other STL is a numpy array(cbct) that I segmented and converted to STL with a code I made in python (not python in 3d slicer).</p>
</blockquote>
</aside>
<p>Since you made this outside of Slicer, it is hard to get where the scale is loss (during the array conversion or your segmentation). Why don’t you import the CBCT directly into Slicer and do the segmentation in it?</p>

---

## Post #7 by @lassoan (2021-02-04 13:43 UTC)

<aside class="quote no-group" data-username="robertoruizmu" data-post="5" data-topic="15782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/9f8e36/48.png" class="avatar"> robertoruizmu:</div>
<blockquote>
<p>go from dicom file to an array</p>
</blockquote>
</aside>
<p>The exported numpy array does not contain information about the image geometry (origin, spacing, axis directions). See these examples about how to process images with preserving the image geometry:</p>
<ol>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_labelmap_node_from_segmentation_node">Convert segmentation to labelmap</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Running_an_ITK_filter_in_Python_using_SimpleITK">Running an ITK filter in Python</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume">Modify voxel of a volume using numpy</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D">Convert labelmap to segmentation</a></li>
</ol>

---
