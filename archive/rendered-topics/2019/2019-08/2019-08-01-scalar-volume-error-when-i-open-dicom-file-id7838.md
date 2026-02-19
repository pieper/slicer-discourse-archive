---
topic_id: 7838
title: "Scalar Volume Error When I Open Dicom File"
date: 2019-08-01
url: https://discourse.slicer.org/t/7838
---

# scalar volume error when i open DICOM file.

**Topic ID**: 7838
**Date**: 2019-08-01
**URL**: https://discourse.slicer.org/t/scalar-volume-error-when-i-open-dicom-file/7838

---

## Post #1 by @Byung_Su_Kim (2019-08-01 12:15 UTC)

<p>When I open DICOM file, ‘could not load: 900: Unnamed series as a Scalar Volume’ error pops up.<br>
It pops up when I open DICOM made by specific radiography equipment.<br>
It’s not a anonymous DICOM. I have to open that DICOM because of my research project…<br>
Is there any solution?</p>
<p>If you need DICOM file, please contact me. <a href="mailto:skbs705@gmail.com">skbs705@gmail.com</a></p>

---

## Post #2 by @pieper (2019-08-01 17:33 UTC)

<p>Please try the suggestions in the <a href="https://www.slicer.org/wiki/Documentation/4.10/FAQ/DICOM" rel="nofollow noopener">DICOM FAQ</a>.  Be careful not to share any confidential health data.</p>

---

## Post #3 by @Chris_Rorden (2019-08-02 12:00 UTC)

<p>Most CT scans represent the image data as a single scalar value representing the attenuation of XRays. Typically, this is reported in Hounsfield Units (air=-1000, water=0, bone=1000) and stored as a single 16-bit integer for each voxel.</p>
<p>If you look at your DICOM header (I often use dcmdump or gdcmdump, but graphical DICOM viewers like Horos will display this as well), you will see that your image is not storing the image data as a single scalar, but is saving three values (Red, Green, Blue) with low precision for each (8-bits):</p>
<p>(0028,0002) US 3                                        #   2, 1 SamplesPerPixel<br>
(0028,0004) CS [RGB]                                    #   4, 1 PhotometricInterpretation<br>
(0028,0100) US 8                                        #   2, 1 BitsAllocated</p>
<p>Another issue I note with your images is that it is missing spatial information such as tag <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.2.html" rel="nofollow noopener">0020,0032</a>. Without this information, it is impossible to determine the spatial orientation and scaling of your image (in particular, spacing between slices).</p>
<p>My sense is that these images are derived images, where the observed intensity has been baked in as low precision R,G,B values. I suspect if you check the providence of your data you can get the original raw data that will be compatible with Slicer.</p>

---

## Post #4 by @Byung_Su_Kim (2019-08-03 00:22 UTC)

<p>Thank you for your reply. Your help is much appreciated.<br>
With your help, I was able to save a lot of time.</p>
<p>thank you very much! have a nice day. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>2019년 8월 2일 (금) 오후 9:10, Chris Rorden via 3D Slicer Community <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>님이 작성:</p>

---
