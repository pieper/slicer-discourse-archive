---
topic_id: 25098
title: "Embedding Url In Mrml Format File"
date: 2022-09-05
url: https://discourse.slicer.org/t/25098
---

# Embedding URL in MRML format file

**Topic ID**: 25098
**Date**: 2022-09-05
**URL**: https://discourse.slicer.org/t/embedding-url-in-mrml-format-file/25098

---

## Post #1 by @Rajesh_Ds (2022-09-05 11:55 UTC)

<p>I wanted to embed the URL of a segmentation (segmentation generated on Slicer in .nrrd file format) in the MRML file which contains segmentation results visualized on Slicer. So that I can send this MRML to my friends who can in turn view the segmentation results remotely on their systems.</p>

---

## Post #2 by @lassoan (2022-09-05 12:32 UTC)

<p>So your mean that your would like to send a short file that Slicer would download and Slicer would download the bulk data when that file is opened?</p>
<p>Slicer used to support such use cases and maybe it still works. However, there are simpler or more flexible alternatives now.</p>
<p>You can simply send an url to a scene saved as an .mrb file (scene saved in a single-file). When the user clicks on the file it gets downloaded in the default web browser and it opens in Slicer. Mrb files are associated to be opened in Slicer on Windows by default (the installer takes care of this). On Linux and macOS you need to set up the file association manually (or you can add a module that sets this up automatically).</p>
<p>You can also associate the <code>slicer</code> custom URL protocol so that such links are opened auto]matically in Slicer. See more information <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#launch-slicer-directly-from-a-web-browser">here</a>. You can use a simple http server or a DICOMweb server. DICOMweb server may be more complicated to set up (unless you use Kheops or you have some other DICOMweb compatible server set up already), but it allows interoperability with other software, you can upload data from Slicer, browse patient data in Slicer, etc.</p>

---

## Post #3 by @Rajesh_Ds (2022-09-15 05:41 UTC)

<p>Thank you so much   Lassoan !!!</p>

---

## Post #4 by @Rajesh_Ds (2022-09-19 07:00 UTC)

<p>Hello Andras Lasso<br>
I have lung nodule segmentation results (in nii.gz format), using which I want to create a 3D slicer visualization scene and store the scene in “.mrb” format. This scene, later, I can share with my remote research friends who can provide comments/suggestions on the segmentation quality. May I know if there any python scripts available on the web which do the same ?  It would be great if I know these details</p>
<p>Thank you<br>
Rajesh</p>

---

## Post #5 by @lassoan (2022-09-19 07:45 UTC)

<p>Load the segmentation from NIFTI into Slicer. Then you can use Kheops (“dropbox for DICOM”) for sharing segmentations exported to DICOMweb as shown in this tutorial video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="60_hzSlptWY" data-video-title="Using 3D Slicer with cloud DICOMweb databases" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=60_hzSlptWY" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/60_hzSlptWY/maxresdefault.jpg" title="Using 3D Slicer with cloud DICOMweb databases" width="" height="">
  </a>
</div>

<p>If you don’t want to mess with setting up a server then you save the scene in .mrb format to a dropbox folder and have your collaborators open them from there.</p>

---

## Post #6 by @Rajesh_Ds (2022-09-19 08:06 UTC)

<aside class="quote no-group" data-username="Rajesh_Ds" data-post="4" data-topic="25098">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rajesh_ds/48/16526_2.png" class="avatar"> Rajesh_Ds:</div>
<blockquote>
<p>create a 3D slicer visualization scene</p>
</blockquote>
</aside>
<p>I want to create a 3D slicer visualization scene for the segmentations (in nii.gz format)  using Python coding, using “Slicer” library. Not using 3D slicer application.</p>

---

## Post #7 by @lassoan (2022-09-19 13:49 UTC)

<p>Do you mean you would like to show a simplified user interface - for example, just a viewer and a feedback form (accept and reject button and a comment field)?</p>

---

## Post #8 by @Rajesh_Ds (2022-09-19 13:52 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations</a></p>
<p>I want to do something like the code in above link</p>

---

## Post #9 by @Rajesh_Ds (2022-09-19 13:55 UTC)

<p>I have written python simpleitk code to perform nodule segmentation (the label volume is in nii.gz) and at the end of the code I want to create slicer scene visualization of this nodule segmentation using python. This scene visualization must be stored in .mrb format</p>

---

## Post #10 by @Rajesh_Ds (2022-09-19 13:59 UTC)

<p>All of the above must happen via python coding (using Slicer python library). This .mrb output file, i can share with a remote user on web. When clicked open must generate the 3D slicer visualization on the remote users 3D slicer application.</p>

---

## Post #11 by @Rajesh_Ds (2022-09-19 14:18 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f27e168367857783a3ed178846a4d066aa7de348.png" data-download-href="/uploads/short-url/yBbGMr1EdFWEhCjvpZABLOiHv04.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f27e168367857783a3ed178846a4d066aa7de348_2_690x335.png" alt="image" data-base62-sha1="yBbGMr1EdFWEhCjvpZABLOiHv04" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f27e168367857783a3ed178846a4d066aa7de348_2_690x335.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f27e168367857783a3ed178846a4d066aa7de348_2_1035x502.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f27e168367857783a3ed178846a4d066aa7de348.png 2x" data-dominant-color="9A999B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1324×644 97.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The viewer must display this slicer scene</p>

---

## Post #12 by @lassoan (2022-09-19 14:40 UTC)

<p>To import a NIFTI file as segmentation (with custom color and name assigned to each segment), you can load the color table file (or create the color table using Python scripting) then use that when loading the segmentation:</p>
<pre><code class="lang-python">colorNode = slicer.util.loadColorTable(r'c:\tmp\Segmentation-label_ColorTable.ctbl')
slicer.util.loadNodeFromFile(r'c:\tmp\Segmentation-label.nii.gz','SegmentationFile',{'colorNodeID': colorNode.GetID()})
</code></pre>
<p>You can save this as a .mrb file and it will show up for your users as in your screenshot above.</p>

---

## Post #13 by @Rajesh_Ds (2022-09-19 16:44 UTC)

<p>It worked. Got my work done. A lot of thanks to you Andras Lasso.</p>

---
