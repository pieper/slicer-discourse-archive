---
topic_id: 35608
title: "Trouble Loading Vff File"
date: 2024-04-19
url: https://discourse.slicer.org/t/35608
---

# Trouble loading vff file

**Topic ID**: 35608
**Date**: 2024-04-19
**URL**: https://discourse.slicer.org/t/trouble-loading-vff-file/35608

---

## Post #1 by @sieunmiin96 (2024-04-19 02:08 UTC)

<p>When I try to import my vff file into 3D slicer, I get the following error message:</p>
<ul>
<li>LoadVffFile: The values for the origin must each be greater than or equal to 0.</li>
<li>LoadVffFile: Incorrect parameters or required parameters that were not set, vff file failed to load. The required parameters are: rank, type, format, bits, bands, size, spacing, origin, rawsize, data scale, data offset, and title.</li>
<li>Warning: In C:\D\N\S462-E-b\SlicerRT\VffFileReader\Logic\vtkSlicerVffFileReaderLogic.cxx, line 104</li>
<li>vtkSlicerVffFileReaderLogic (000001E09458D120): ReadVffFileHeader: Nothing follows the equal sign in header item: ‘batch’</li>
<li>Warning: In C:\D\N\S462-E-b\SlicerRT\VffFileReader\Logic\vtkSlicerVffFileReaderLogic.cxx, line 104</li>
<li>vtkSlicerVffFileReaderLogic (000001E09458D120): ReadVffFileHeader: Nothing follows the equal sign in header item: ‘gel’</li>
<li>Warning: In C:\D\N\S462-E-b\SlicerRT\VffFileReader\Logic\vtkSlicerVffFileReaderLogic.cxx, line 104</li>
<li>vtkSlicerVffFileReaderLogic (000001E09458D120): ReadVffFileHeader: Nothing follows the equal sign in header item: ‘modification_history’</li>
</ul>
<p>In order to resolve these errors, I got rid of the headers (batch, gel, and history) and manually put the origin to 0 0 0 since in the original vff file, the origin was -79.75 -79.75 -79.75. However, when I do this, I get the following error message:</p>
<ul>
<li>LoadVffFile: The end of the file was reached earlier than specified.</li>
</ul>
<p>And my vff file looks like the below image, which is not what it’s supposed to look like.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a6f7b0f6bf678c5623258a982cc8012f6c53771.png" data-download-href="/uploads/short-url/fbzspdOAyrS3QQv20SXvL7obpv3.png?dl=1" title="vff screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a6f7b0f6bf678c5623258a982cc8012f6c53771_2_626x500.png" alt="vff screenshot" data-base62-sha1="fbzspdOAyrS3QQv20SXvL7obpv3" width="626" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a6f7b0f6bf678c5623258a982cc8012f6c53771_2_626x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a6f7b0f6bf678c5623258a982cc8012f6c53771_2_939x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a6f7b0f6bf678c5623258a982cc8012f6c53771_2_1252x1000.png 2x" data-dominant-color="68686F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vff screenshot</span><span class="informations">1294×1032 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve also tried setting the origin to 79.75 79.75 79.75 and got the same result.</p>

---

## Post #2 by @cpinter (2024-04-22 12:53 UTC)

<p>I think you use an old version of Slicer, because I fixed this error in January, see</p><aside class="quote quote-modified" data-post="1" data-topic="34265">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sieunmiin96/48/67738_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/unable-to-open-vff-file/34265">Unable to open vff file</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I have Slicer 5.6.1, but I’m unable to open the vff file despite having the SlicerRT extension installed. The following is the error log: 
LoadVffFile: The values for the origin must each be greater than or equal to 0. 
LoadVffFile: Incorrect parameters or required parameters that were not set, vff file failed to load. The required parameters are: rank, type, format, bits, bands, size, spacing, origin, rawsize, data scale, data offset, and title. 
Warning: In vtkSlicerVffFileReaderLogic.cxx, lin…
  </blockquote>
</aside>

<p>Please update to the latest version and try again. Let is know how it goes.</p>

---

## Post #3 by @sieunmiin96 (2024-04-23 18:18 UTC)

<p>Yes, I’m using an older version of Slicer because when I use the latest version, I am unable to perform registration. I’ve also posted a <a href="https://discourse.slicer.org/t/unable-to-open-vff-file/34265">link</a> about this.</p>

---

## Post #4 by @cpinter (2024-04-29 11:00 UTC)

<p>The link you posted seems to be the VFF file loading issue, which has been fixed.</p>
<p>If your main problem now is about registration, please let us know about that in a different thread.</p>

---

## Post #5 by @sieunmiin96 (2024-04-29 17:39 UTC)

<p>It seems like I posted the incorrect link.<br>
I’ve already posted on the forum regarding the errors I’ve been having when performing registration <a href="https://discourse.slicer.org/t/error-when-performing-registration-in-slicelets-gel-dosimetry-analysis/35478">here</a></p>

---
