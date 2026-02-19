---
topic_id: 13253
title: "Trouble Viewing My Files"
date: 2020-08-31
url: https://discourse.slicer.org/t/13253
---

# trouble viewing my files

**Topic ID**: 13253
**Date**: 2020-08-31
**URL**: https://discourse.slicer.org/t/trouble-viewing-my-files/13253

---

## Post #1 by @bob (2020-08-31 15:02 UTC)

<p>I have watched a couple of youtube introductions to 3D Slicer, but am having challenges to get my .DCM files to display properly.  Either no image appears or I see collapsed views. Any suggestions how to work past this?  Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93fb111451312aac3c0238d4a4180d781251a63f.png" data-download-href="/uploads/short-url/l765XsQDFoLIQ6v0dNsKNfnaQkn.png?dl=1" title="flat" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93fb111451312aac3c0238d4a4180d781251a63f_2_416x500.png" alt="flat" data-base62-sha1="l765XsQDFoLIQ6v0dNsKNfnaQkn" width="416" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93fb111451312aac3c0238d4a4180d781251a63f_2_416x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93fb111451312aac3c0238d4a4180d781251a63f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93fb111451312aac3c0238d4a4180d781251a63f.png 2x" data-dominant-color="3A3A45"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">flat</span><span class="informations">560×673 59 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-08-31 16:13 UTC)

<p>Please try with latest Slicer Preview Release. Let us know if any warnings or errors are displayed during loading.</p>

---

## Post #3 by @bob (2020-08-31 16:35 UTC)

<p>Thank you for the reply.  I downloaded v4.11.0, as you suggested.  No error messages appeared when I dragged my .dcm files into 3D Slicer.  Still, the MRI images either don’t appear or are collapsed.</p>

---

## Post #4 by @muratmaga (2020-08-31 16:41 UTC)

<p>In general, to import DICOM images you should use the DICOMBrowser (the icon that says DCM). That might fix some of the issues you are facing.</p>

---

## Post #5 by @lassoan (2020-08-31 17:54 UTC)

<p>Very good point!</p>
<p><a class="mention" href="/u/bob">@bob</a> Make sure you are in DICOM module when you drag-and-drop your DICOM folder to Slicer’s application window to import files into your DICOM database. Slicer will then index the files and you can double-click on a patient, study, or series, to load it into the current scene.</p>

---
