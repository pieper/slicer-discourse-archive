---
topic_id: 2952
title: "How To Save Nrrd As A Dicom File"
date: 2018-05-28
url: https://discourse.slicer.org/t/2952
---

# How to save nrrd as a dicom file?

**Topic ID**: 2952
**Date**: 2018-05-28
**URL**: https://discourse.slicer.org/t/how-to-save-nrrd-as-a-dicom-file/2952

---

## Post #1 by @ElonKou (2018-05-28 17:46 UTC)

<p>After I used the brainsFit plug-in for slicer to register two dicoms, I got a node object. I plan to export this node to show it to others, but I didn’t find how to use code to convert node  object to dicom series file. Somebody helped. Me?<br>
I know that DICOMScalarVolumePlugin and DicomRtImportExported can do this, but I don’t know where to find their calling function.<br>
So my question is as follows (using scripting):<br>
1.How to add a patient’s(and study) node to a node object?<br>
2. Which commands and function can be used to add patient’s tag information and set the output folder?<br>
If anyone knows these questions, can you help me? Thank you very much!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64081b4eee127f2cdb30e102a603f9be01d0888b.png" data-download-href="/uploads/short-url/egV7a1JKwx0gJTrnE0C7im6UqtZ.png?dl=1" title="35" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64081b4eee127f2cdb30e102a603f9be01d0888b_2_690x330.png" alt="35" data-base62-sha1="egV7a1JKwx0gJTrnE0C7im6UqtZ" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64081b4eee127f2cdb30e102a603f9be01d0888b_2_690x330.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64081b4eee127f2cdb30e102a603f9be01d0888b_2_1035x495.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64081b4eee127f2cdb30e102a603f9be01d0888b.png 2x" data-dominant-color="E7E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">35</span><span class="informations">1127×539 99.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Or there are other ways to export the registered image into dicom</p>

---

## Post #2 by @brhoom (2018-05-28 18:51 UTC)

<p>I convert nrrd to dicom using slicer’s <a href="https://www.slicer.org/wiki/Documentation/4.0/Modules/CreateDICOMSeries" rel="nofollow noopener">Create a DICOM Series module</a>. You can input the important metadata as well. It is also available as CLI so you can call it with some arguments in your python <a href="https://www.slicer.org/wiki/Documentation/4.2/Developers/Python_scripting#Running_a_CLI_from_Python" rel="nofollow noopener">script</a>.</p>

---

## Post #3 by @lassoan (2018-05-28 20:15 UTC)

<aside class="quote no-group" data-username="ElonKou" data-post="1" data-topic="2952">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/e19b73/48.png" class="avatar"> ElonKou:</div>
<blockquote>
<p>1.How to add a patient’s(and study) node to a node object?</p>
</blockquote>
</aside>
<p>In Data module / Subject hierarchy tab, drag-and-drop the series under the study.</p>
<aside class="quote no-group" data-username="ElonKou" data-post="1" data-topic="2952">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/e19b73/48.png" class="avatar"> ElonKou:</div>
<blockquote>
<p>Which commands and function can be used to add patient’s tag information and set the output folder?</p>
</blockquote>
</aside>
<p>Do you mean using Python scripting? Have you exported successfully using the graphical user interface?</p>

---

## Post #4 by @ElonKou (2018-05-29 04:38 UTC)

<p>Thank you very much. I used your method and succeed.</p>

---

## Post #5 by @ElonKou (2018-05-29 04:44 UTC)

<p>Yes, thanks for your help, I want to use python script to convert volume to dicom series. I use the method provided by <a class="mention" href="/u/brhoom">@brhoom</a> and succeed. Thank you, the people in the Slicer community are very enthusiastic。</p>

---

## Post #6 by @lassoan (2018-05-29 04:53 UTC)

<p>For reference, <a href="https://github.com/SlicerRt/SegmentRegistration/tree/master/ProstateMRIUSContourPropagation">ProstateMRIUSContourPropagation</a> module implements a complete clinical workflow for registering prostate MRI to ultrasound images. All inputs are imported from DICOM and registered images are written to DICOM. See a short demo of the module:</p>
<div class="lazyYT" data-youtube-id="6VT5xPQQyBQ" data-youtube-title="MRI-US fusion for prostate HDR brachytherapy" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>If you need a similar tool that can register clinical images that you retrieve from PACS and you can push back to a PACS then you can use this module as a starting point. It is implemented in Python, so it should be very easy to adapt it to your specific use case.</p>

---

## Post #7 by @ElonKou (2018-05-29 09:35 UTC)

<p>In fact, I am looking for a way to register MR images on CT images，and export it to dicom-series for display. Thank you very much for your suggestion. This plugin may solve my problem.</p>

---
