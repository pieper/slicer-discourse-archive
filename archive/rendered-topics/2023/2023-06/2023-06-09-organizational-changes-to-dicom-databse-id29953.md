---
topic_id: 29953
title: "Organizational Changes To Dicom Databse"
date: 2023-06-09
url: https://discourse.slicer.org/t/29953
---

# Organizational Changes to DICOM Databse

**Topic ID**: 29953
**Date**: 2023-06-09
**URL**: https://discourse.slicer.org/t/organizational-changes-to-dicom-databse/29953

---

## Post #1 by @AnishJag (2023-06-09 20:24 UTC)

<p>I’ve been using a custom extension for Slicer3D for bone analysis and realized that I accidentally ran an analysis on incorrect images because when importing the DICOMs from a folder, it appears extremely similar in the DICOM Database. If there was an easier way to distinguish these DICOMs, my analysis would have run smoother. I thought that the following changes may help:</p>
<ol>
<li>Having the File Names in the DICOM Database where the DICOMs were imported from.</li>
<li>Anything that pertains to dates, have it in a simpler format such as dd/mm/yyyy. For times, use the local machine’s time and have the option to switch between military and non-military formats.</li>
<li>Have arrows on both sides of a column to change its size. I was trying to adjust the column widths and it wasn’t quite intuitive.</li>
</ol>

---

## Post #2 by @lassoan (2023-06-16 14:41 UTC)

<p>Thanks for the suggestions. We are working on a completely new, patient-oriented, visual DICOM browser with thumbnails and more clear separation of patients and studies. We expect to make it available within a few months.</p>

---

## Post #3 by @AnishJag (2023-07-27 15:46 UTC)

<p>Hello again!</p>
<p>I was just curious to know if there was any new information regarding the release of the new DICOM database. I’ve been tasked to create a tutorial video regarding how to use our custom extension with Slicer, and I’d like to incorporate the new database in the video to help prevent confusion. Thanks!</p>

---

## Post #4 by @lassoan (2023-07-29 16:39 UTC)

<p>We experienced some performance issues that we are addressing in the coming weeks, so probably the feature will be available around the end of August.</p>

---
