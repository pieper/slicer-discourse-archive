---
topic_id: 9147
title: "Horos Compatibility"
date: 2019-11-14
url: https://discourse.slicer.org/t/9147
---

# Horos compatibility

**Topic ID**: 9147
**Date**: 2019-11-14
**URL**: https://discourse.slicer.org/t/horos-compatibility/9147

---

## Post #1 by @Melodicpinpon (2019-11-14 13:34 UTC)

<p>Hi,</p>
<p>If I work with 3D Slicer, can I import and export all the data with ‘Horus’ and ‘Osirix’?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2019-11-14 13:49 UTC)

<p>Last time I helped someone with Osirix a few months ago, we found that:</p>
<ul>
<li>Osirix can only import DICOM images (not any of the standard research formats, such a nrrd, nifti, …)</li>
<li>You can only export segmentations/annotations in a proprietary format (neither DICOM nor research formats)</li>
</ul>
<p>The guy who segmented a few hundred patients in Osirix was in a pretty bad situation, as he realized too late that he cannot do the analysis he needs in Osirix and reverse-engineering the Osirix proprietary file formats and converting the data would be significant amount of work.</p>
<p>What would you like to do? What data flow do you envision between Slicer/Horos/Osirix? Is there any feature in Horos/Osirix that you cannot find in Slicer?</p>

---

## Post #3 by @Melodicpinpon (2019-11-14 17:02 UTC)

<p>Well received. Thank you.</p>
<p>I am trying to enlighten the choice of my new colleague who works on a Mac.</p>
<p>There are several persons that can help her with Horos.</p>
<p>I recommend 3DSlicer since I begin to have some success with it and that I would like us to be able to share data and learn together.</p>

---

## Post #4 by @brhoom (2021-08-23 09:28 UTC)

<p>It would be nice to have a horos “theme” in Slicer. Many radiologists find it easier to work with horos. Since it uses vtk, it would be nice to have the same visualization functionalities in horos as an option in 3d Slicer.</p>

---

## Post #5 by @pieper (2021-08-23 12:10 UTC)

<p>Slicer has always aimed to be more of a flexible research platform and less of a polished radiology reading application.  This has met the needs of the people who primarily built and used Slicer.  But the building blocks in Slicer could be reused in a custom user interface focused on diagnostic radiology.  Mainly this would require someone to map out a user interface that makes sense for this purpose determining if there are missing pieces or performance bottlenecks.  Probably it could all be done with some python, ui, and qss configurations.</p>

---

## Post #6 by @lassoan (2021-08-23 12:39 UTC)

<p>I fully agree. This is the kind of work that <a class="mention" href="/u/dougporter">@dougPorter</a> is doing for the Slicer installations at Mayo Clinics.</p>
<p>We are continuously improving the Slicer core, too, to make it easier to use Slicer for simple tasks; and making custom, trimmed-down Slicer versions easier to create and maintain.</p>

---
