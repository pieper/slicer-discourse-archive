---
topic_id: 8798
title: "Nasal Cavity Geometry Extraction"
date: 2019-10-16
url: https://discourse.slicer.org/t/8798
---

# Nasal Cavity Geometry Extraction

**Topic ID**: 8798
**Date**: 2019-10-16
**URL**: https://discourse.slicer.org/t/nasal-cavity-geometry-extraction/8798

---

## Post #1 by @MSheheryar (2019-10-16 14:24 UTC)

<p>I need to extract geometry of nasal cavity of sample patients for CFD simulation. Kindly guide me what would be the best method to do so.</p>

---

## Post #2 by @MSheheryar (2019-10-16 15:47 UTC)

<p>What is the most effective and efficient way to extract geometry of nasal cavity from DICOM data?</p>

---

## Post #3 by @pieper (2019-10-16 19:14 UTC)

<p>If it’s just air surrounded by tissue, maybe you can get by with just thesholding and scissors.  The <a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Segmentation" rel="nofollow noopener">segmentation tutorials</a> are a good place to start.  Beyond that you’d need to describe your data more (maybe with screenshots).</p>

---

## Post #4 by @MSheheryar (2019-10-16 19:35 UTC)

<p>That is what I have been doing but there are a lot of holes in the surface and I am not able to fix that using smoothies tools. Can segmentation be done using GrayScale Model Maker? How does it work?</p>

---

## Post #5 by @pieper (2019-10-16 19:51 UTC)

<p>It might help - we can only guess without seeing your data.</p>
<p>One thing you can try is increasing the resolution of the segmentation compared to the background image.</p>

---

## Post #6 by @MSheheryar (2019-10-16 21:13 UTC)

<p>Thanks for the reply. I am not allowed to share the data. Do you have any tutorial that tells how to extract geometry using Grayscale Model Maker?</p>

---

## Post #7 by @muratmaga (2019-10-16 22:07 UTC)

<p>You should use Segment Editor from a recent preview version. Here are some pointers to get you started:</p>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html" rel="nofollow noopener">https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a></li>
<li><a href="https://www.youtube.com/watch?v=BJoIexIvtGo" rel="nofollow noopener">https://www.youtube.com/watch?v=BJoIexIvtGo</a></li>
<li><a href="https://github.com/SlicerMorph/S_2019/tree/master/Lab05_Slicer_4_Segmentation" rel="nofollow noopener">https://github.com/SlicerMorph/S_2019/tree/master/Lab05_Slicer_4_Segmentation</a></li>
</ul>

---

## Post #8 by @MSheheryar (2019-10-17 03:06 UTC)

<p>How do I increase resolution of my segmentation?</p>
<p>Also, what is the most appropriate method to determine the exact threshold range for a specific patient?</p>

---

## Post #9 by @muratmaga (2019-10-17 03:18 UTC)

<p>For thresholds, I don’t think there is an ‘exact’ method. You can try the provided automated thresholding algorithms (e.g., Otsu, isodata etc), as a starting to point and see if they help you identify a range that works for the structure you isolate. Benefit of such algorithms is the reproducibility, but that doesn’t mean the range that they estimate is going to be range you will need for your case.</p>
<p>To change the resolution of the segmentation, you can click the little cube next to do Master Volume field of segment editor, and select Segmentation node. Then you can specify the resolution you would like to have. Note that for me this resulted in a crash with MRHead.nrrd when I was testing it.</p>
<p>My preferred method is to increase the resolution of the master volume using the Crop Volume or ResampleScalarVolume so that thin structures that I want to segment are at least 4-5 voxels thick. After that you can proceed with the segmentation normally.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f7f8336c14eb64b56d10c9b2f6560d8dace8b38.png" alt="image" data-base62-sha1="blgUHxAgmTfFx3zInHxcm9TS7RC" width="647" height="119"></p>

---

## Post #10 by @MSheheryar (2019-10-17 04:04 UTC)

<p>Thank you for the help. After trial and error, I was able to find a suitable threshold range with minimum holes and extrusions. However, I am not sure whether this is the correct way to do it. What I mean to say is that this may result<br>
in adding extra segments to the geometry which are not originally part of the patient’s actual nasal cavity.</p>
<p>I read in a paper (attached) about determining the right threshold value (Table 1). I am working on it. If you know anything about it or come across anything relevant in future, kindly do let me know. Furthermore, the authors have<br>
mentioned about using the Grayscale Model Maker for geometry reconstruction (section 2.3 para 1). I have been trying it. I was able to create iso-surfaces. Is there any way to turn that is-surface into a segment?</p>
<p>Thank you.</p>
<p>(Attachment Zwicker_2018_Biomed._Phys._Eng._Express_4_045022.pdf is missing)</p>

---

## Post #11 by @MSheheryar (2019-10-17 04:05 UTC)

<p>Attachment has been rejected. You can view that paper here:</p>
<p><a href="https://iopscience.iop.org/article/10.1088/2057-1976/aac6af/pdf" class="onebox" target="_blank" rel="nofollow noopener">https://iopscience.iop.org/article/10.1088/2057-1976/aac6af/pdf</a></p>
<p>Thanks!</p>

---

## Post #12 by @lassoan (2019-10-17 04:49 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="8798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>To change the resolution of the segmentation, you can click the little cube next to do Master Volume field of segment editor, and select Segmentation node. Then you can specify the resolution you would like to have. Note that for me this resulted in a crash with MRHead.nrrd when I was testing it.</p>
</blockquote>
</aside>
<p>It worked well for me with any parameter combinations that I tried. Can you describe the steps that led to the crash?</p>

---

## Post #13 by @MSheheryar (2019-10-17 07:21 UTC)

<p>Thanks. Is there any way to convert an iso-surface (obtained form Grayscale Model Maker) into a segment which can later be exported into an STL file?</p>
<p>Regards,</p>

---

## Post #14 by @lassoan (2019-10-17 11:24 UTC)

<p>You do not need to use Grayscale model maker module anymore. All you need is available in Segment Editor and Segmentations modules:</p>
<ul>
<li>Thresholding effect to generate segment from iso-value</li>
<li>Create 3D to generate isosurface that is automatically regenerated as you edit the segmentation</li>
<li>Export to files to create 3D-printable STL file, etc</li>
</ul>

---

## Post #15 by @pieper (2019-10-17 14:13 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, Doesn’t the Segment Editor require a labelmap for thresholding?  That would technically be a different final mesh than the Grayscale model maker for the same threshold (depends on oversample level).</p>

---

## Post #16 by @lassoan (2019-10-17 14:42 UTC)

<p>Segment editor Threshold effect does not require labelmap input - as master volume it can use the same scalar volume input as Grayscale model maker.</p>
<p>Segmentations can generate the same output as Grayscale model maker. You can tune smoothing, decimation, normal computation options in Segmentations module / Representations / Closed Surface - Update / Binary Labelmap -&gt; Closed surface path.</p>

---

## Post #17 by @pieper (2019-10-17 17:18 UTC)

<p>But Grayscale model maker never creates a labelmap, so the isosurface is defined by the continuous tone values of the image, not from the output of the threshold, which introduces a voxel level discretation.</p>
<p>When I try editing a Segmentation where the master representation is Closed Surface I get this dialog, so it looks like you can’t bypass having the labelmap.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fcead4bd730c86e43ce5f86eeb98ebfe4ecc9d1.png" data-download-href="/uploads/short-url/2fPXQPbASrAugHXtCjopEDG7Xod.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fcead4bd730c86e43ce5f86eeb98ebfe4ecc9d1_2_690x361.png" alt="image" data-base62-sha1="2fPXQPbASrAugHXtCjopEDG7Xod" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fcead4bd730c86e43ce5f86eeb98ebfe4ecc9d1_2_690x361.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fcead4bd730c86e43ce5f86eeb98ebfe4ecc9d1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fcead4bd730c86e43ce5f86eeb98ebfe4ecc9d1.png 2x" data-dominant-color="DFDFDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">858×450 53.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #18 by @lassoan (2019-10-17 19:35 UTC)

<p>I see what you mean now. Yes, if you use binary labelmap representation then the subpixel-precision adjustment of surface point positions is missed. In practice, this does not make much difference because we smooth the generated mesh.</p>
<p>Maybe there is some degree of surface roughness that can be preserved if scalar volume is meshed immediately, but smoothed out if performing thresholding, meshing, and smoothing. In the rare case that this would matter, you can use fractional labelmap representation instead of binary labelmap. Or, you can use binary labelmap representation with oversampling. Or, if you don’t need any editing, then you can use Grayscale model maker.</p>

---

## Post #19 by @pieper (2019-10-17 19:52 UTC)

<p>Yes, I agree - in most use cases you need to edit anyway, so the best option is to pick a segmentation oversampling that is able to represent the details you need (so that any important feature is a few voxels thick).</p>
<p>For special cases where thresholding works well in the area of interest, another option is to edit the things you want to remove into a segment and then use that to mask the original volume before running the Grayscale model maker.</p>

---

## Post #20 by @MSheheryar (2019-10-26 08:01 UTC)

<p>I just had an idea. I was thinking if there is any way to cut down my segmentation into small segments so that I can manually edit them by filling the holes and then later merge all the segments into a single segment. I need the geometry to be one closed surface. I will use it later in ICEM CFD for meshing, so it needs to be totally error free. Thank you for your time.</p>

---

## Post #21 by @MSheheryar (2019-10-30 08:45 UTC)

<p>I need a sample CT DICOM data of a head. Where can I find it?</p>

---

## Post #22 by @muratmaga (2019-10-30 15:49 UTC)

<p><a href="https://www.cancerimagingarchive.net/" class="onebox" target="_blank" rel="nofollow noopener">https://www.cancerimagingarchive.net/</a><br>
Search for head and neck.</p>

---

## Post #23 by @pieper (2019-10-30 16:18 UTC)

<p>Also on the same site the CPTAC-GBM dataset includes some head CTs.</p>

---

## Post #24 by @MSheheryar (2019-11-04 16:52 UTC)

<p>This data is in TCIA format. How do I convert it to DICOM or is any there any way to load it in Slicer?</p>

---

## Post #25 by @pieper (2019-11-04 17:22 UTC)

<p>Most of the data on TCIA is in dicom, you just need to download it.</p>

---

## Post #26 by @MSheheryar (2019-11-04 17:33 UTC)

<p>I have downloaded it but how do I import it in Slicer. I tried to drag and drop but it shows nothing.</p>

---

## Post #27 by @pieper (2019-11-04 18:14 UTC)

<p>Did you use the download manager? <a href="https://wiki.cancerimagingarchive.net/display/NBIA/Download+Manager+7.0">https://wiki.cancerimagingarchive.net/display/NBIA/Download+Manager+7.0</a></p>

---

## Post #28 by @pieper (2019-11-04 18:15 UTC)

<p>You might also try <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/TCIABrowser">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/TCIABrowser</a></p>

---
