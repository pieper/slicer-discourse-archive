---
topic_id: 13970
title: "Export Segmentation As Dicom"
date: 2020-06-18
url: https://discourse.slicer.org/t/13970
---

# Export segmentation as DICOM

**Topic ID**: 13970
**Date**: 2020-06-18
**URL**: https://discourse.slicer.org/t/export-segmentation-as-dicom/13970

---

## Post #1 by @Jan_Alexander (2020-06-18 13:35 UTC)

<p>Hello,</p>
<p>I try to do the same discussed above and as is shown in <a href="https://youtu.be/nzWf4xHy1BM" rel="noopener nofollow ugc">this tutorial</a>.<br>
Unfortunately, this does not work.</p>
<p>I believe the extensions <code>SlicerRT</code> and <code>Quantitave reporting</code> are correctly installed, but I do not even get the <code>RT</code> export option. Instead, I get this <code>DICOMSegmentation</code> export type. This type gives an error when I try to export : VolumeNode Panoramix-cropped has no attribute DICOM.instanceUIDs</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80b43fc4bba66c8f3d058c08ab81865818d46f81.png" data-download-href="/uploads/short-url/imzitZgw7hf33y3yaHM5WSgRL0J.png?dl=1" title="DICOM slicer fail" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80b43fc4bba66c8f3d058c08ab81865818d46f81.png" alt="DICOM slicer fail" data-base62-sha1="imzitZgw7hf33y3yaHM5WSgRL0J" width="640" height="500" data-dominant-color="E5E7E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DICOM slicer fail</span><span class="informations">687×536 30.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks for your advice.<br>
Jan</p>

---

## Post #2 by @lassoan (2020-10-10 00:32 UTC)

<aside class="quote no-group quote-modified" data-username="Jan_Alexander" data-post="17" data-topic="543">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jan_alexander/48/6831_2.png" class="avatar"><a href="https://discourse.slicer.org/t/convert-image-and-segmentation-to-dicom/543/17">Convert image and segmentation to DICOM</a></div>
<blockquote>
<p>I do not even get the <code>RT</code> export option</p>
</blockquote>
</aside>
<p>If you want to export segmentation as DICOM RT structure set then you need to install SlicerRT extension. However, RT structure set is a very bad format for storing segmentation: it has many issues and limitations related to both importing and exporting it. To store segmentation in DICOM format, use Segmentation object format (the exporter that you show in your screenshot above).</p>
<p>DICOM Segmentation object exporter expects that the master volume is loaded from DICOM and has all the necessary unique identifiers (UIDs). If you want to use non-DICOM image source then first you can export the image to DICOM, which adds all the necessary identifiers.</p>

---

## Post #3 by @Mgi (2020-10-13 18:22 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> When I tried to convert to DICOM using DICOM Segmentation exporter appear this error.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05dbe24f0c41b0bfa040263c74aa8c9b96bf3d49.png" data-download-href="/uploads/short-url/PPuaPKBv8Y2iFadcQJEhhQGP1L.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05dbe24f0c41b0bfa040263c74aa8c9b96bf3d49.png" alt="image" data-base62-sha1="PPuaPKBv8Y2iFadcQJEhhQGP1L" width="645" height="500" data-dominant-color="EDEFF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">666×516 27.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Mgi (2020-10-13 20:06 UTC)

<p>My debug report. <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a67da0e3f9d62b9df64ed2473b9c51e64df99951.png" alt="image" data-base62-sha1="nKQpUhO0vi7KS4Erv8M0NWWAvyp" width="675" height="292"></p>

---

## Post #5 by @lassoan (2020-10-13 20:33 UTC)

<p>Are you using the latest Slicer Stable Release?</p>

---

## Post #6 by @dszimatore (2021-06-15 09:55 UTC)

<p>Hello!<br>
Can anybody suggest me the easiest way to export a segmentation with MRI in DICOM, so that the file can be used for neuronavigation? I tried with RT, but hospital DICOM viewers were not able to read the .rtss file. I tried to create new subject and new study as suggested in tutorials but still the segmention isn’t saved but only the original file.<br>
Where can I find a deteiled descritpion of the procedure not to run into mistakes?</p>
<p>Thank you very much</p>

---

## Post #7 by @lassoan (2021-06-15 17:20 UTC)

<p>Many DICOM viewers cannot display image segmentation. You can find the DICOM conformance statement of all commercial DICOM viewers online (just google <code>(productname) DICOM conformance statement</code>) where they describe what kind of image segmentation they can display (DICOM RT structure set is more common among old software, DICOM Segmentation object is supported in new software).</p>

---

## Post #8 by @dszimatore (2021-06-23 21:31 UTC)

<p>I tried with “DICOM segmentation” but i obtained only a <strong>subjct_hyerarchy_export</strong> file, impossible to open with a viewer. Where can I find complete intructions for exporting segmentaion to DICOM? Is there a DICOM viewer by which I can test if the procedure was correct?</p>
<p>Thank you</p>

---

## Post #9 by @lassoan (2021-06-25 21:58 UTC)

<p>See step-by-step instructions for DICOM export <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database">here</a>.</p>
<p>Only very few image viewers can display segmentations. Most of them are really just that, image viewers and cannot deal with any other objects (segmentaton object, spatial registration object, structured report, etc.). I think recent MITK versions can display segmentations and I know that the web-based OHIF viewer can do basic segmentation display, too. You can get an OHIF viewer without setting up a web server by uploading your data set to <a href="https://kheops.online/">Kheops</a> and open its built-in viewer (that is an OHIF viewer).</p>

---

## Post #10 by @dszimatore (2021-06-25 23:02 UTC)

<p>Thank you very much for answering!</p>

---
