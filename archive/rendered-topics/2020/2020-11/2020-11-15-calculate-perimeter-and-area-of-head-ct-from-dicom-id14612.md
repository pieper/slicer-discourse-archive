---
topic_id: 14612
title: "Calculate Perimeter And Area Of Head Ct From Dicom"
date: 2020-11-15
url: https://discourse.slicer.org/t/14612
---

# Calculate perimeter and area of Head CT from DICOM

**Topic ID**: 14612
**Date**: 2020-11-15
**URL**: https://discourse.slicer.org/t/calculate-perimeter-and-area-of-head-ct-from-dicom/14612

---

## Post #1 by @med_student (2020-11-15 06:15 UTC)

<p>I’m trying to calculate the perimeter and area of the outer lining of the skull from head computed tomography scans. I assume this involves edge detection.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39862924639c54b5c31ac790586d2e05a02fdadd.jpeg" alt="image" data-base62-sha1="8cSExggpsJ791iNrPjLQTA1PorX" width="377" height="442"></p>

---

## Post #2 by @lassoan (2020-11-16 07:13 UTC)

<p>What would you like to measure exactly: in one or few image planes or in 3D? do you need a fully-automatic/semi-automatic/manual method? what are your accuracy and time constraints? how many of these measurement you need to do (dozens/hundreds/thousands)?, what skills the operators have? What is the overall goal of your project?</p>

---

## Post #3 by @med_student (2020-11-16 18:44 UTC)

<p>Thanks.</p>
<p>I have 100 of these patients. I need to measure the perimeter and area of the outer table of the skull in one slice for each patient. I am choosing the slice in which to capture the greatest frontal-occipital length.</p>
<p>It would be great if this could be semiautomated but I can do this manually if needed.</p>
<p>My goal is to calculate the circularity of the skull in these slices. Along these lines:</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="http://rsb.info.nih.gov/ij/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://imagej.nih.gov/ij/docs/menus/analyze.html" target="_blank" rel="noopener nofollow ugc">imagej.nih.gov</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://imagej.nih.gov/ij/docs/menus/analyze.html" target="_blank" rel="noopener nofollow ugc">Analyze Menu</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2020-11-16 19:15 UTC)

<p>You can write a fully automatic script to do this analysis (segment the skull outer surface, find the slice with largest diameter or cross-sectional area, extract the cut the segmentation with the selected slice, and compute length and area for the contour). However, if you are new to Slicer’s Python API then implement this fully automatic method could take several days.</p>
<p>Since manually placement of a closed contour markup takes about 1 minute, most probably you could complete your entire analysis in a few hours - considerably faster than implementing the fully automatic solution. But if you are interested in investing into developing a fully automatic solution anyway then let us know, we are happy to help to get you started and give advice along the way.</p>
<p>Note that currently surface area of a closed contour is not displayed in the GUI but you need to copy-paste this script into the Python console to see it: <a href="https://discourse.slicer.org/t/how-can-i-calculate-an-area-on-a-ct-image-i-can-calculate-volumes-mm-3-but-not-areas-mm-2/1549/7" class="inline-onebox">How can I calculate an area on a CT image. I can calculate volumes (mm^3) but not areas (mm^2)</a> (probably surface are display will be available in Markups module’s user interface within a few months).</p>

---
