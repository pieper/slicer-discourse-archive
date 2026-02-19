---
topic_id: 28553
title: "How Can I Export 4D Volume As Dicom"
date: 2023-03-24
url: https://discourse.slicer.org/t/28553
---

# How can I export 4D volume as DICOM?

**Topic ID**: 28553
**Date**: 2023-03-24
**URL**: https://discourse.slicer.org/t/how-can-i-export-4d-volume-as-dicom/28553

---

## Post #1 by @STRF87 (2023-03-24 04:08 UTC)

<p>Hello! I am fairly new to Slicer and I was hoping for some advice.</p>
<p>I have created a sequence of volumes (4D volume) of PET data. It is for a dynamic PET kinetic modeling application.</p>
<p>I can export the sequence as .seq.nrrd and import it back perfectly fine. But, I can’t export the sequence as a series of DICOM files.</p>
<p>In the Create a DICOM Series Module, it only shows me options of the regular 3D volumes, but not the 4D one.</p>
<p>Incidentally, I can import 4D DICOM serieses as well, but I can’t export such sequences. Could someone help?</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2023-03-24 04:12 UTC)

<p>We haven’t implemented a 4D exporter. It should not be hard to do it - you simply dump all the slices (all frames of all time points) into a single series - but there was just not a lot of request from users.</p>
<p>If you have Python scripting experience and willing to spend some time with it then we can help you getting started. Alternatively, if you are not ready to start working on this then we can move this topic to the “feature requests” category and if enough people vote on it then we’ll work on it.</p>

---

## Post #3 by @STRF87 (2023-03-24 11:45 UTC)

<p>Appreciate it! I have some experience with Python Scripting. Could you give me a few pointers as to how I would go about it?</p>
<p>Just to clarify, I already have different "MRMLvolume"s of the exact same dimensions at different time points. How can I go about creating a DICOM series from it?</p>

---

## Post #4 by @lassoan (2023-03-27 02:45 UTC)

<p>I was looking for DICOM exporter examples and I’ve found that I actually implemented an exporter for 4D volumes (see <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMVolumeSequencePlugin.py">source code</a>).</p>
<p>Please test if it works for you. If there is an issue then you can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/python.html">attach a Python debugger</a> and step through the code to see what goes wrong.</p>

---

## Post #5 by @Saima (2023-04-25 07:27 UTC)

<p>Hi Andras,<br>
I want to export the DICOM 4D volume. When I export it using DICOM I can see only one volume and not all the available series. Can Slicer help to view the DICOM 4D volumes with 6-8 frames of cardiac cycles? Any help ? I wan to view like horoas application gives a view for a 4D volume with different frames.</p>
<p>regards,<br>
Saima</p>

---

## Post #6 by @lassoan (2023-04-25 10:51 UTC)

<p>Yes, Slicer can import, visualize, export 4D volumes. If something does not work at you expect then describe what you did (in a way that allows us to reproduce it), what you expected to happen, and what happened instead. Share the data you load (make sure it is anonymized or use publicly available data set) and include screenshots.</p>

---

## Post #7 by @Saima (2023-05-02 02:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="28553">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>lude screenshots</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
I do not see the 8 different frames with 246 images each. I can open the 4D volume but don’t see all the frames.</p>
<p>any suggestions?<br>
In horoas application I can view all the 8 frames on the side<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a88fc03767c939387cdee07462bca21bdf01ef5.png" data-download-href="/uploads/short-url/3MJTVlniyBch7Dl2KAhwlWyzTgN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a88fc03767c939387cdee07462bca21bdf01ef5_2_690x423.png" alt="image" data-base62-sha1="3MJTVlniyBch7Dl2KAhwlWyzTgN" width="690" height="423" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a88fc03767c939387cdee07462bca21bdf01ef5_2_690x423.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a88fc03767c939387cdee07462bca21bdf01ef5_2_1035x634.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a88fc03767c939387cdee07462bca21bdf01ef5.png 2x" data-dominant-color="1A1A1A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1164×715 87.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>regards,<br>
Saima</p>

---

## Post #8 by @lassoan (2023-05-02 02:46 UTC)

<p>Horos probably just shows you a list of 2D slices. In contrast, Slicer reconstruct 3D volumes. If a slice is missing from a volume then the entire volume may be discarded. If you enable detailed logging in Application Settings / DICOM then you may find more details in the application log. If you can share the anonymized data set then I can have a look, too.</p>

---
