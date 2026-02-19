---
topic_id: 15396
title: "Changing Folder Colors Changes The Normals Of Segmentation 3"
date: 2021-01-07
url: https://discourse.slicer.org/t/15396
---

# Changing folder colors, changes the normals of segmentation 3D surface inside of that folder

**Topic ID**: 15396
**Date**: 2021-01-07
**URL**: https://discourse.slicer.org/t/changing-folder-colors-changes-the-normals-of-segmentation-3d-surface-inside-of-that-folder/15396

---

## Post #1 by @NoobForSlicer (2021-01-07 21:16 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21d81ccaf402ffd92de6ff46dc16f6b4811dc714.jpeg" data-download-href="/uploads/short-url/4PoM4u3U6YXNvHfDjQpZI5HQS9u.jpeg?dl=1" title="difference" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21d81ccaf402ffd92de6ff46dc16f6b4811dc714_2_690x193.jpeg" alt="difference" data-base62-sha1="4PoM4u3U6YXNvHfDjQpZI5HQS9u" width="690" height="193" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21d81ccaf402ffd92de6ff46dc16f6b4811dc714_2_690x193.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21d81ccaf402ffd92de6ff46dc16f6b4811dc714_2_1035x289.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21d81ccaf402ffd92de6ff46dc16f6b4811dc714_2_1380x386.jpeg 2x" data-dominant-color="7E6B7E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">difference</span><span class="informations">2114×593 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This only happens to one segmentation I am working on…</p>
<p>Other segmentations look perfectly fine.</p>
<p>I realized that I can put hundreds of segmentations into one folder and change the color for the entire folder and that way have them red or green temporarily as long as they are inside of the folder. Which is kind of cool for quick changes to pin point and show different segmentations or pathologies.</p>
<p>Problem: one segmentation, once put inside of a folder, and applied a color, has its normals flipped and surface is displayed inside-out. I wonder, why?</p>

---

## Post #2 by @lassoan (2021-01-07 21:18 UTC)

<p>Can you provide a minimal .mrb file that we can use to reproduce this issue?</p>

---

## Post #3 by @NoobForSlicer (2021-01-08 06:18 UTC)

<p>Dear Lassoan,</p>
<p>here is the link to the file:</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1Lz87Zhra7wmvFWNs6eLzUc88tEh8pqW8/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1Lz87Zhra7wmvFWNs6eLzUc88tEh8pqW8/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1Lz87Zhra7wmvFWNs6eLzUc88tEh8pqW8/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1Lz87Zhra7wmvFWNs6eLzUc88tEh8pqW8/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">2021-01-08-Scene.mrb</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I don’t know how to upload a file to our discourse forum besides images so I uploaded it to google drive.</p>
<p>Here is a description of what you will find in the scene:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc1dc474f4a434d4b749ab939fbe15b170db6a9d.png" data-download-href="/uploads/short-url/zYk68iLtV1L79j4LUVGyrlfUDI9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc1dc474f4a434d4b749ab939fbe15b170db6a9d_2_690x244.png" alt="image" data-base62-sha1="zYk68iLtV1L79j4LUVGyrlfUDI9" width="690" height="244" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc1dc474f4a434d4b749ab939fbe15b170db6a9d_2_690x244.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc1dc474f4a434d4b749ab939fbe15b170db6a9d_2_1035x366.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc1dc474f4a434d4b749ab939fbe15b170db6a9d.png 2x" data-dominant-color="F8F8F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1080×383 14.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>with red encircled is the segmentation inside of a folder, with flipped normals for some reason.<br>
with green is encircled segmentation OUTSIDE of the folder, with okay surface and okay normals. I have hidden it so you can see the first semgnetation with flipped normals.</p>
<p>Keep in mind I have just copied the segmentation, and just dragged it out of the folder and then surface looked perfectly normal.</p>

---

## Post #4 by @lassoan (2021-01-08 16:46 UTC)

<p>Thank you for the example. The problem is that for some reason the surface normals are inverted in the generated surface (we can investigate it separately, if needed) and by default the folder display node hides backfaces (backface culling is enabled by default).</p>
<p>You can fix the issue by disabling backface culling for the folder by typing this into the Python console:</p>
<pre><code>slicer.util.getNodesByClass("vtkMRMLFolderDisplayNode")[0].BackfaceCullingOff()
</code></pre>
<p>We’ll turn off backface culling in folder display nodes by default to avoid similar issues in the future.</p>

---
