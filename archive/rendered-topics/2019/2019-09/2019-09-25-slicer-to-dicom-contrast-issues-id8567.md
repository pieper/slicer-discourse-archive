---
topic_id: 8567
title: "Slicer To Dicom Contrast Issues"
date: 2019-09-25
url: https://discourse.slicer.org/t/8567
---

# Slicer to DICOM contrast Issues

**Topic ID**: 8567
**Date**: 2019-09-25
**URL**: https://discourse.slicer.org/t/slicer-to-dicom-contrast-issues/8567

---

## Post #1 by @rsheth (2019-09-25 17:33 UTC)

<p>Hi All!</p>
<p>I am having an issue regarding the transport of a newly converted nrrd file to DICOM (done using slicer). When I go to import the file into a DICOM viewer (Horos), the contrast suddenly changes drastically and the images become unusable. The DICOM and nrrd should be identical, is there a setting that I am missing to make sure that they are? Thank you!</p>

---

## Post #2 by @lassoan (2019-09-25 17:35 UTC)

<aside class="quote no-group" data-username="rsheth" data-post="1" data-topic="8567">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/9de0a6/48.png" class="avatar"> rsheth:</div>
<blockquote>
<p>The DICOM and nrrd should be identical, is there a setting that I am missing to make sure that they are?</p>
</blockquote>
</aside>
<p>What is the data type of the voxels in your nrrd file? What is the range of voxel values?</p>

---

## Post #3 by @rsheth (2019-10-01 23:12 UTC)

<p>Hi,</p>
<p>I am downloading the images off of a third party website, and do not have access to this info. Do you think that the problem could lie here? Thank you</p>

---

## Post #4 by @lassoan (2019-10-02 01:01 UTC)

<p>Can you post a few screenshots how the data looks before/after import/export in various software? Where did you download the original data sets from?</p>

---

## Post #5 by @rsheth (2019-10-02 01:20 UTC)

<p>The data was taken from the international mouse phenotyping consortium, the link is as follows: <a href="https://www.mousephenotype.org/embryoviewer/?mgi=MGI:2679336" class="inline-onebox" rel="noopener nofollow ugc">Interactive Embryo Viewer</a></p>
<p>As for pictures, attatched is an image in slicer, as well as an image in HOROS DICOM viewer. For some reason, the exposure is always increased and the image becomes impossible to view.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8eb5b5406b39d7e503d25907d7f5c0621c1bca30.jpeg" data-download-href="/uploads/short-url/kmt6INBkTIAo55tsLs27xN5HU2Y.jpeg?dl=1" title="01%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8eb5b5406b39d7e503d25907d7f5c0621c1bca30_2_656x500.jpeg" alt="01%20PM" data-base62-sha1="kmt6INBkTIAo55tsLs27xN5HU2Y" width="656" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8eb5b5406b39d7e503d25907d7f5c0621c1bca30_2_656x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8eb5b5406b39d7e503d25907d7f5c0621c1bca30_2_984x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8eb5b5406b39d7e503d25907d7f5c0621c1bca30_2_1312x1000.jpeg 2x" data-dominant-color="B4B4B7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">01%20PM</span><span class="informations">2076×1580 516 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you for your assistance!</p>

---

## Post #6 by @lassoan (2019-10-02 01:30 UTC)

<p>The mousephenotype website always times out for me when I’m trying to download any data. Can you upload a data set to dropbox/onedrive/gdrive and post the ink?</p>
<p>Would you like to export to DICOM just so that Horos can read it? Slicer is a much more flexible and feature-rich application compared to Horos, why don’t you analyze your data directly in Slicer?</p>

---

## Post #7 by @rsheth (2019-10-02 01:54 UTC)

<p><a href="https://studentuml-my.sharepoint.com/:u:/g/personal/ram_sheth_student_uml_edu/EUFkYAm2X3FCsvZTkA33vEEBo5P5p2HgyGdlDhhC0OSccw?e=UZ8VkT" class="onebox" target="_blank" rel="nofollow noopener">https://studentuml-my.sharepoint.com/:u:/g/personal/ram_sheth_student_uml_edu/EUFkYAm2X3FCsvZTkA33vEEBo5P5p2HgyGdlDhhC0OSccw?e=UZ8VkT</a></p>
<p>Please let me know if you have trouble accessing it from this link.</p>
<p>As for the software, truthfully I am more familiar with the UX of Horos, especially when it comes to 3D volume rendering to analyze bone and soft tissue. I have only recently learned of slicer and was primarily using it as a method to convert nrrd files to DICOM. I am attempting to analyze homologies between diseased and healthy mice, and Horos was the original software that I was using. In the interim, I am trying to play around to Slicer to see if it fits my needs.</p>

---

## Post #8 by @lassoan (2019-10-02 01:59 UTC)

<p>Slicer has tons of features and they are all exposed on the GUI, so indeed it takes some time to learn how to get around. If you describe what your current workflow is then we can give you pointers about how to accomplish it in Slicer.</p>
<p>In the meantime, I’ve checked the file. It has very unusual scalar range (0 to 51615) which does not fit into the maximum scalar range of signed short that is used in CT/MR volumes (-32767 to 32767). If you want clinical software to work well with such images then bring down its scalar range to a couple of thousands. For this you can use “Simple filters” module, “RescaleIntensityImageFilter”, with something like Output minimum = -1000, Output maximum = 3000.</p>

---

## Post #9 by @rsheth (2019-10-07 23:01 UTC)

<p>Thank you for your suggestion, I have tried it and found that it works. I appreciate your support.</p>
<p>I am definitely interested in switching over to slicer, however I am not sure about the functionality that I will need to utilize. I am aiming to segment a 3D volume of a uCT scan and calculate the volumes of specific regions. Can I use slicer as an atlas to achieve this? Thank you.</p>

---

## Post #10 by @lassoan (2019-10-07 23:22 UTC)

<aside class="quote no-group" data-username="rsheth" data-post="9" data-topic="8567">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/9de0a6/48.png" class="avatar"> rsheth:</div>
<blockquote>
<p>I am aiming to segment a 3D volume of a uCT scan and calculate the volumes of specific regions</p>
</blockquote>
</aside>
<p>This is a very common use case and there are good tools for this in Slicer. You can segment regions using Segment Editor module (see linkts to tutorials and recipes <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">here</a>) then use Segment Statistics module to compute volumes and other statistics.</p>

---
