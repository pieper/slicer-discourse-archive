---
topic_id: 13914
title: "Problem With Thin Vessel Walls"
date: 2020-10-07
url: https://discourse.slicer.org/t/13914
---

# Problem with thin vessel walls

**Topic ID**: 13914
**Date**: 2020-10-07
**URL**: https://discourse.slicer.org/t/problem-with-thin-vessel-walls/13914

---

## Post #1 by @Andreas (2020-10-07 11:32 UTC)

<p>I would like to print vessel models with a wall thickness of 0.3 mm. As you can see from the attached appendix, I already have problems with a wall thickness of 0.4 and 0.5 mm. Can you please tell me why these holes are created and how I can print a vessel model without holes?</p>
<p>I have already tried the Fill Holes function without success or possibly used it incorrectly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9cbc588b8a4a225d1973905f066ece1ca45db6b8.jpeg" data-download-href="/uploads/short-url/mmy0U1GeDDLgInFtzKRZZ967w1O.jpeg?dl=1" title="Shell thickness 0.4mm_new" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9cbc588b8a4a225d1973905f066ece1ca45db6b8_2_690x402.jpeg" alt="Shell thickness 0.4mm_new" data-base62-sha1="mmy0U1GeDDLgInFtzKRZZ967w1O" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9cbc588b8a4a225d1973905f066ece1ca45db6b8_2_690x402.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9cbc588b8a4a225d1973905f066ece1ca45db6b8_2_1035x603.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9cbc588b8a4a225d1973905f066ece1ca45db6b8_2_1380x804.jpeg 2x" data-dominant-color="75757C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Shell thickness 0.4mm_new</span><span class="informations">1676×978 304 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32c5f109c94995f8ccf9a0a37cdb5bd842ecea35.jpeg" data-download-href="/uploads/short-url/7f9XBqtNQqLHBuuBSakP44quuoZ.jpeg?dl=1" title="Shell thickness 0.5mm_new" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/32c5f109c94995f8ccf9a0a37cdb5bd842ecea35_2_690x399.jpeg" alt="Shell thickness 0.5mm_new" data-base62-sha1="7f9XBqtNQqLHBuuBSakP44quuoZ" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/32c5f109c94995f8ccf9a0a37cdb5bd842ecea35_2_690x399.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/32c5f109c94995f8ccf9a0a37cdb5bd842ecea35_2_1035x598.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/32c5f109c94995f8ccf9a0a37cdb5bd842ecea35_2_1380x798.jpeg 2x" data-dominant-color="74747A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Shell thickness 0.5mm_new</span><span class="informations">1680×972 290 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-10-07 12:21 UTC)

<p>Spacing of the segmentation’s binary labelmap representation must be at least a couple of times smaller than the wall thickness. For a 0.3mm wall thickness I would use at least 0.1mm spacing. You can change segmentation geometry as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html?highlight=geometry#panels-and-their-use">here</a>.</p>
<p>A finer resolution segmentation requires much more memory and computation time (2x finer resolution uses 8x more memory), so you may need a stronger computer if you want to have extremely fine resolution.</p>
<p>Note that most 3D printers cannot print a stable model with 0.3mm wall thickness. Which printer do you use?</p>

---

## Post #3 by @Andreas (2020-10-07 15:27 UTC)

<p>Thanks for your help.</p>
<p>As you recommended, I set the distance to 0.1mm (image) and then smoothed it with the smoothing median (1.00mm) (image). Then I set the desired wall thickness of 0.3 mm with the hollow function, but the holes appear again (image). Could you please give me some extra help?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f924f6b82b0951cdb170c8f55b2f167b075e40df.jpeg" alt="Spacing 0.1 mm" data-base62-sha1="zy25fdYqv5fHqHgjvu7fy7gAD15" width="502" height="373"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d949b61e7ac80b5a489c26c4fc7e8012de410fd.jpeg" data-download-href="/uploads/short-url/4dGeBCctFDMbo749maYIVYZZMrb.jpeg?dl=1" title="Shell thickness 0.3 mm (2)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d949b61e7ac80b5a489c26c4fc7e8012de410fd_2_690x402.jpeg" alt="Shell thickness 0.3 mm (2)" data-base62-sha1="4dGeBCctFDMbo749maYIVYZZMrb" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d949b61e7ac80b5a489c26c4fc7e8012de410fd_2_690x402.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d949b61e7ac80b5a489c26c4fc7e8012de410fd_2_1035x603.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d949b61e7ac80b5a489c26c4fc7e8012de410fd_2_1380x804.jpeg 2x" data-dominant-color="BAB7D6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Shell thickness 0.3 mm (2)</span><span class="informations">1680×980 200 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7be4552405fe2b1523da5138eebbabbcbd2723c2.jpeg" data-download-href="/uploads/short-url/hFZVBHIX4SQDaJJECWtCSxbcIuu.jpeg?dl=1" title="Shell thickness 0.3 (median 1.00 mm)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7be4552405fe2b1523da5138eebbabbcbd2723c2_2_690x400.jpeg" alt="Shell thickness 0.3 (median 1.00 mm)" data-base62-sha1="hFZVBHIX4SQDaJJECWtCSxbcIuu" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7be4552405fe2b1523da5138eebbabbcbd2723c2_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7be4552405fe2b1523da5138eebbabbcbd2723c2_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7be4552405fe2b1523da5138eebbabbcbd2723c2_2_1380x800.jpeg 2x" data-dominant-color="BAB8D8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Shell thickness 0.3 (median 1.00 mm)</span><span class="informations">1680×976 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7ef20d9036ed407a3b99c0a602680423f69fa17.jpeg" data-download-href="/uploads/short-url/nXC4bTaTXYK30WjNMGHqitTnDEP.jpeg?dl=1" title="Shell thiness 0.3 mm (Holes)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7ef20d9036ed407a3b99c0a602680423f69fa17_2_690x414.jpeg" alt="Shell thiness 0.3 mm (Holes)" data-base62-sha1="nXC4bTaTXYK30WjNMGHqitTnDEP" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7ef20d9036ed407a3b99c0a602680423f69fa17_2_690x414.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7ef20d9036ed407a3b99c0a602680423f69fa17_2_1035x621.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7ef20d9036ed407a3b99c0a602680423f69fa17_2_1380x828.jpeg 2x" data-dominant-color="BBBBDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Shell thiness 0.3 mm (Holes)</span><span class="informations">1680×1010 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-10-07 15:49 UTC)

<p>Can you upload the data set somewhere and post the link here?</p>

---

## Post #5 by @Andreas (2020-10-07 22:17 UTC)

<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="32" height="32">
      <a href="https://www.dropbox.com/sh/zofo9c0fpfj4c0j/AADfuHH0GmwTgMlq4D4u3GDIa?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/sh/zofo9c0fpfj4c0j/AADfuHH0GmwTgMlq4D4u3GDIa?dl=0" target="_blank" rel="noopener nofollow ugc">Vessel model</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2020-10-08 02:04 UTC)

<p>I’ve tested segmentation of this data set with latest Slicer Stable Release (4.11.20200930) and it worked well. I’ve performed these steps:</p>
<ul>
<li>load the DICOM volume</li>
<li>cast volume to “short” (using Cast scalar volume module) to reduce memory usage (optional)</li>
<li>crop and resample volume: reduce ROI to the minimum necessary (to reduce memory usage) and set spacing scale to 0.3</li>
<li>segment vessels using thresholding in Segmentations module</li>
<li>remove disconnected vessel fragments using Islands effect (default options)</li>
<li>create shell using Hollow effect, setting Shell thickness to 0.3mm</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d18e32b2eb690dee84b6d09d9367b0a137258996.gif" data-download-href="/uploads/short-url/tTOrQOUelX0sZVkuNG5oM3JwfVs.gif?dl=1" title="SlicerCapture"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d18e32b2eb690dee84b6d09d9367b0a137258996_2_528x500.gif" alt="SlicerCapture" data-base62-sha1="tTOrQOUelX0sZVkuNG5oM3JwfVs" width="528" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d18e32b2eb690dee84b6d09d9367b0a137258996_2_528x500.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d18e32b2eb690dee84b6d09d9367b0a137258996_2_792x750.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d18e32b2eb690dee84b6d09d9367b0a137258996_2_1056x1000.gif 2x" data-dominant-color="474952"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerCapture</span><span class="informations">1184×1120 2.07 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @Andreas (2020-10-08 20:56 UTC)

<p>Thanks again for your help</p>
<p>I tried to follow your instructions. Unfortunately I have the same problem again.</p>
<p>Here is my approach:</p>
<ol>
<li>
<p>Load the master volume. Then I selected the “Cast Scalar Volume” module with “Short”. (Image)</p>
</li>
<li>
<p>Select “segmentation geometry” and set the oversampling factor to 1.58 → Spacing 0.3 mm (Image)</p>
</li>
<li>
<p>Threshold tool → automatic threshold with Otsu (Image)</p>
</li>
<li>
<p>Inside surface with 0.3mm and Apply → Failed (picture)</p>
</li>
</ol>
<p>Can you please tell me what the problem is?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f51342be1a28591db58fb46e96d2bebb67468bc.jpeg" data-download-href="/uploads/short-url/4t2MlYJdLTrE3oDWfA7NdOJYxjK.jpeg?dl=1" title="short1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f51342be1a28591db58fb46e96d2bebb67468bc_2_690x400.jpeg" alt="short1" data-base62-sha1="4t2MlYJdLTrE3oDWfA7NdOJYxjK" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f51342be1a28591db58fb46e96d2bebb67468bc_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f51342be1a28591db58fb46e96d2bebb67468bc_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f51342be1a28591db58fb46e96d2bebb67468bc_2_1380x800.jpeg 2x" data-dominant-color="8E8FA1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">short1</span><span class="informations">1678×974 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/168430190911fe73c9a6e995b0d5cc921915b8ee.jpeg" alt="0,3 mm spacing" data-base62-sha1="3dbImGYg5ksrgnxC7KTB3OdHvwW" width="510" height="373"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aab6a904fac3c10b96058ba29095718c519308cd.jpeg" data-download-href="/uploads/short-url/omcw66Wbqk4EpdkMA6Znkr9MCgB.jpeg?dl=1" title="threshold(automatic otsu)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aab6a904fac3c10b96058ba29095718c519308cd_2_690x400.jpeg" alt="threshold(automatic otsu)" data-base62-sha1="omcw66Wbqk4EpdkMA6Znkr9MCgB" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aab6a904fac3c10b96058ba29095718c519308cd_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aab6a904fac3c10b96058ba29095718c519308cd_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aab6a904fac3c10b96058ba29095718c519308cd_2_1380x800.jpeg 2x" data-dominant-color="8C8D9D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">threshold(automatic otsu)</span><span class="informations">1680×976 293 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9c169a8cf4db40a78c08ec7fa9ab2fc59d152a9.jpeg" data-download-href="/uploads/short-url/xlTDoN9t4OuIyLjtbnZTKgZbkAF.jpeg?dl=1" title="fail" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9c169a8cf4db40a78c08ec7fa9ab2fc59d152a9_2_690x400.jpeg" alt="fail" data-base62-sha1="xlTDoN9t4OuIyLjtbnZTKgZbkAF" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9c169a8cf4db40a78c08ec7fa9ab2fc59d152a9_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9c169a8cf4db40a78c08ec7fa9ab2fc59d152a9_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9c169a8cf4db40a78c08ec7fa9ab2fc59d152a9_2_1380x800.jpeg 2x" data-dominant-color="8D8E9F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fail</span><span class="informations">1678×974 286 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2020-10-09 01:08 UTC)

<p>Please follow the instructions that I provided. Note that I did not use “Segmentation geometry” but cropped the volume so that there is enough memory space for achieving sufficiently small spacing (around 0.1). Spacing of 0.3 would not work if you want to have wall thickness of 0.3 (wall thickness must be 2-3x larger than the spacing).</p>

---

## Post #9 by @Andreas (2020-10-09 11:40 UTC)

<p>Unfortunately, I am not yet familiar with the “Crop and Resample Volume” function. Can you explain this step to me?</p>
<p>Many thanks for your help</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/623acf8c8f362130be5b839b7f8b3c6f65e801d8.jpeg" data-download-href="/uploads/short-url/e0YNcksmJcXhqSH0zvg2bpsVLiE.jpeg?dl=1" title="crop" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/623acf8c8f362130be5b839b7f8b3c6f65e801d8_2_690x402.jpeg" alt="crop" data-base62-sha1="e0YNcksmJcXhqSH0zvg2bpsVLiE" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/623acf8c8f362130be5b839b7f8b3c6f65e801d8_2_690x402.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/623acf8c8f362130be5b839b7f8b3c6f65e801d8_2_1035x603.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/623acf8c8f362130be5b839b7f8b3c6f65e801d8_2_1380x804.jpeg 2x" data-dominant-color="8F90A1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">crop</span><span class="informations">1678×978 236 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @manjula (2020-10-09 12:11 UTC)

<p>you can have alook at</p>
<div class="youtube-onebox lazy-video-container" data-video-id="cz9wLrlJSz0" data-video-title="How to use 3D Slicer to crop DICOM file" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=cz9wLrlJSz0" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/cz9wLrlJSz0/maxresdefault.jpg" title="How to use 3D Slicer to crop DICOM file" width="" height="">
  </a>
</div>


---

## Post #11 by @Andreas (2020-10-10 10:50 UTC)

<p>Thanks for the video.</p>
<p>Are all of these intermediate steps with saving really necessary? I want to keep it short and simple without having to load a new file.</p>
<p>Unfortunately, I still have problems creating a thin vessel wall thickness (0.3mm).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/714c87bf48797762545f8b30bbf224d103d9f509.jpeg" data-download-href="/uploads/short-url/gahV0wFWyAGB9ENLkV2gj4Ju9nP.jpeg?dl=1" title="crop_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/714c87bf48797762545f8b30bbf224d103d9f509_2_690x400.jpeg" alt="crop_1" data-base62-sha1="gahV0wFWyAGB9ENLkV2gj4Ju9nP" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/714c87bf48797762545f8b30bbf224d103d9f509_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/714c87bf48797762545f8b30bbf224d103d9f509_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/714c87bf48797762545f8b30bbf224d103d9f509_2_1380x800.jpeg 2x" data-dominant-color="8E8F9F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">crop_1</span><span class="informations">1680×976 291 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @lassoan (2020-10-10 15:00 UTC)

<p>How to use Crop volume: load your volume, go to Crop volume, click “Fix” to create default ROI, adjust it to minimum possible size (you can easily reduce memory usage by a factor of 5-10x), set spacing scale to have approximately 0.1mm voxel size in the output (in your case it is about 0.3), and click Apply.</p>

---

## Post #13 by @Andreas (2020-10-10 17:17 UTC)

<p>Thank you for your reply.</p>
<p>I loaded the volume and opened the Crop Volume module. Then I selected the desired master volume and clicked on Fix. Finally, I set the spacing to 0.1mm (spacing scale: 0.22x), but after the threshold I still can’t choose smaller wall thicknesses.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbe70767e380b477900cb2f248a0b8651adc9247.jpeg" data-download-href="/uploads/short-url/vnlxG9VxXpz978bt8TBcUsgLHPV.jpeg?dl=1" title="Crop Volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dbe70767e380b477900cb2f248a0b8651adc9247_2_453x500.jpeg" alt="Crop Volume" data-base62-sha1="vnlxG9VxXpz978bt8TBcUsgLHPV" width="453" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dbe70767e380b477900cb2f248a0b8651adc9247_2_453x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbe70767e380b477900cb2f248a0b8651adc9247.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbe70767e380b477900cb2f248a0b8651adc9247.jpeg 2x" data-dominant-color="F6F6F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Crop Volume</span><span class="informations">552×609 69.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #14 by @lassoan (2020-10-10 17:37 UTC)

<p>Now that you have this cropped volume as shown as background volume in slice viewers, go to Segment Editor and create a new segmentation (it will use this cropped volume as master by default).</p>

---

## Post #15 by @Andreas (2020-10-10 20:42 UTC)

<p>I clicked Apply and created a new segment in the Segment Editor. (Image)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f43457e4c133f15f475f15c881b2a5175f563cf.jpeg" alt="Create new seg" data-base62-sha1="mIU2RJoXZ1xqFIHseQh3GNK0QOz" width="562" height="110"></p>
<p>But I still can’t go below 0.48mm. (Image)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da535abd3653a0ab2b9993810d10f921c3818c13.jpeg" alt="hollow" data-base62-sha1="v9oFPkehv6zmoeUaAZguMudBax5" width="552" height="199"></p>
<p>I also tried other master volumes but unfortunately without success (Image)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/886eeb9d40552199037e2470133d953c25daf368.jpeg" alt="Master Volume" data-base62-sha1="jsWA4l1vtsRUfadovTuEBsgpE7u" width="559" height="149"></p>
<p>Sometimes I also get the error message but I don’t think it’s because of that.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5573abb00057ccd5a77a335042a096e42c381293.jpeg" alt="error" data-base62-sha1="cbWpjcKQLgMxye9hOe64jBVXT7J" width="499" height="226"></p>

---

## Post #16 by @lassoan (2020-10-10 21:21 UTC)

<p>It seems that the last remaining problem is that you run out of memory. You need to crop the image to minimum size and/or increase virtual memory size. To further reduce memory usage, delete the original (non-cropped) image from the scene after cropping is completed. You can also try to use slightly larger spacing scale (0.3x worked well for me).</p>
<p>Just to see what kind of images you can get after proper cropping, have a look at the image that I got after cropping: <a href="https://1drv.ms/u/s!Arm_AFxB9yqHxJEfKDvMA3AYkaWoYw?e=noOOwy">https://1drv.ms/u/s!Arm_AFxB9yqHxJEfKDvMA3AYkaWoYw?e=noOOwy</a></p>

---

## Post #17 by @Andreas (2020-10-10 22:44 UTC)

<p>Many thanks for your effort.</p>
<p>Your version works perfectly. With my version I can now also set the wall thickness to 0.3 mm, but it disappears afterwards. (can no longer see the model in the 3D viewer)</p>
<p>Even if I just save it as “5 Untitled Series cropped” and only load this file, the program crashes due to insufficient memory.</p>

---

## Post #18 by @lassoan (2020-10-11 02:49 UTC)

<aside class="quote no-group" data-username="Andreas" data-post="17" data-topic="13914">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>Your version works perfectly. With my version I can now also set the wall thickness to 0.3 mm, but it disappears afterwards. (can no longer see the model in the 3D viewer)</p>
</blockquote>
</aside>
<p>Most likely you run out of memory. You either need to follow all the memory-saving steps that I described above (recommended) or significantly increase virtual memory size in your system settings.</p>

---

## Post #19 by @Andreas (2020-10-11 20:40 UTC)

<p>Why can I work with your version without any problems and the error message still appears with my version? (my “cropped.nrrd” file is very delayed)</p>
<p>Although I reduced the memory usage with Cast scalar volume module.</p>

---

## Post #20 by @lassoan (2020-10-11 21:30 UTC)

<p>You can check what is the difference between your and my version of the volume in Volumes module’s Volume Information section.</p>

---
