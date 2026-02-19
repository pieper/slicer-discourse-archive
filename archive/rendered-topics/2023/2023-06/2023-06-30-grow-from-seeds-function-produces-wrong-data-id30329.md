---
topic_id: 30329
title: "Grow From Seeds Function Produces Wrong Data"
date: 2023-06-30
url: https://discourse.slicer.org/t/30329
---

# Grow from seeds function produces wrong data

**Topic ID**: 30329
**Date**: 2023-06-30
**URL**: https://discourse.slicer.org/t/grow-from-seeds-function-produces-wrong-data/30329

---

## Post #1 by @LavaBunny (2023-06-30 19:17 UTC)

<p>This image shows the segmentations I have drawn.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea932b9256b41b7561ac842be13e01a91f139ee9.png" data-download-href="/uploads/short-url/xt92p6gTPzu1Hfe7mrndcBvzpAl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea932b9256b41b7561ac842be13e01a91f139ee9_2_690x483.png" alt="image" data-base62-sha1="xt92p6gTPzu1Hfe7mrndcBvzpAl" width="690" height="483" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea932b9256b41b7561ac842be13e01a91f139ee9_2_690x483.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea932b9256b41b7561ac842be13e01a91f139ee9_2_1035x724.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea932b9256b41b7561ac842be13e01a91f139ee9_2_1380x966.png 2x" data-dominant-color="32323E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1583×1109 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, after I grow from seeds, it gives me something completely wrong. What am I doing wrong here?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d1ffffd928ae9dda7e4d178fef11dc1b3dec327.png" data-download-href="/uploads/short-url/hQUf5FystNSQ7AySTv5LoUWyXFZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d1ffffd928ae9dda7e4d178fef11dc1b3dec327_2_690x483.png" alt="image" data-base62-sha1="hQUf5FystNSQ7AySTv5LoUWyXFZ" width="690" height="483" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d1ffffd928ae9dda7e4d178fef11dc1b3dec327_2_690x483.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d1ffffd928ae9dda7e4d178fef11dc1b3dec327_2_1035x724.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d1ffffd928ae9dda7e4d178fef11dc1b3dec327_2_1380x966.png 2x" data-dominant-color="342B36"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1584×1111 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @rbumm (2023-07-01 15:01 UTC)

<p>Are you trying to segment the lungs with 3D Slicer´s grow from seeds effect?<br>
<a href="https://www.youtube.com/watch?v=9iiOBmaP8bA">This YouTube video</a> may help.</p>
<p>However, this is a time-consuming process. Alternatively, you could use modules from the Chest Imaging Platform, LungCTAnalyzer, or the TotalSegmentator extension for that purpose.</p>

---

## Post #3 by @lassoan (2023-07-01 16:55 UTC)

<p>The segmentation looks correct for these inputs. It seems that you did not add seeds into regions that you are <em>not</em> interested in, therefore your other segments leaked into the unclaimed area. You can fix that by adding an “other” segment and use it to draw scribbles in all areas that you want to be ignored. Once the segmentation is completed, you can delete this segment. For segmenting textureless structures (that are typical in phantoms like yours and sometimes appear in clinical images in regions filled with fluid or air) you may want to increase <code>Seed locality</code> value a little bit (0.1-0.5 may be enough) to reduce leaking.</p>
<p>Since your phantom looks completely noise-free (is it an <em>in silico</em> phantom - a computationally generated image?), probably the simplest is to segment it using <code>Threshold</code> effect.</p>

---

## Post #4 by @LavaBunny (2023-07-05 15:19 UTC)

<p>I am trying to use the totalSegmentator extension, but I get reproduceable data that is, for lack of a better word, wonky.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/902d27d29f2ea00b354bbf5c342132f6637339cd.png" data-download-href="/uploads/short-url/kzrv49xkXbi6ZVHziwFVt5IlpG5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/902d27d29f2ea00b354bbf5c342132f6637339cd_2_690x425.png" alt="image" data-base62-sha1="kzrv49xkXbi6ZVHziwFVt5IlpG5" width="690" height="425" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/902d27d29f2ea00b354bbf5c342132f6637339cd_2_690x425.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/902d27d29f2ea00b354bbf5c342132f6637339cd_2_1035x637.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/902d27d29f2ea00b354bbf5c342132f6637339cd_2_1380x850.png 2x" data-dominant-color="33333E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1806×1114 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can you help me out with this? Thanks</p>

---

## Post #5 by @rbumm (2023-07-06 05:50 UTC)

<p>We can probably help but need the dataset somehow. What is it exactly do you need to segment?</p>

---

## Post #6 by @lassoan (2023-07-06 14:01 UTC)

<p>The dataset looks so unrealistic that I’m not surprised that most tools fails to deal with it. There is no natural texture or noise in the image. There are gaps (e.g., below the skin). It is not even clear what imaging modelity it is supposed to be (looks more like an MRI, but what kind?). The orientation is incorrect (rotated by 90 degrees in axial view, sagittal/coronal are mixed up). Probably the physical size is off, too (you can check by making some measurements in Markups module).</p>
<p>Is it some <em>in silico</em> phantom? What software have you created it with? What is your overall goal?</p>

---

## Post #7 by @LavaBunny (2023-07-06 16:13 UTC)

<p>Okay, I’ll describe my project here.</p>
<p>This model is taken from the virtual family project. This one is duke. My goal is to take the model from sim4life and make it into a CAD model (.stl, .step, etc.).</p>
<p>How I went about this was extracting the sim4life data into matlab as sigma, rho, and epsilon variables. In Matlab, I converted it into a matrix and nii file. (I also corrected the orientation of the model by transposing and flipping the matrix). With the nii file, I took it into 3d slicer to try to segment it and export as a CAD viewable file. I believe it is an MRI scan.</p>

---

## Post #8 by @lassoan (2023-07-06 16:30 UTC)

<p>The simplest way to create meshes from such data set is to save it as a labelmap image (each value of the matrix is an integer value that specifies what segment that voxel belongs to). You can then load the image file as a segmentation (by choosing “Segmentation” in “Add data” window) and click “Show 3D” to generate meshes.</p>
<p>If you are interested in free, open solutions, you can use Slicer (and various automatic segmentation tools, such as TotalSegmentator extension) for creating patient models and FEBio for biomechanical simulation (or revive the Slicer-based <a href="https://www.kitware.com/bender-2-0/">Bender</a> project for posing patient models).</p>

---

## Post #9 by @LavaBunny (2023-07-06 16:34 UTC)

<p>Thanks for you help!</p>
<p>How would I go about creating this labelmap image? Is it a process that I do in matlab? Is there a website documenting this process?</p>

---

## Post #10 by @lassoan (2023-07-06 16:42 UTC)

<p>Yes, you do it in Matlab. All you need to do is to use an integer value type.</p>

---

## Post #11 by @LavaBunny (2023-07-06 16:46 UTC)

<p>Ok, so I take the original image matrix and change its type to integer? Wouldn’t this truncate many values and break the image?</p>

---

## Post #12 by @lassoan (2023-07-06 17:30 UTC)

<p>Make sure voxels corresponding to a segment all have the same value. Truncation is no problem, as long as voxel of different structures don’t get assigned to the same value.</p>

---

## Post #13 by @LavaBunny (2023-07-06 18:22 UTC)

<p>It worked well, thank you very much. However, the skin layer seems to be inconsistent. Sometimes muscle shows through or bones. Is this a model issue or can this be fixed in software?</p>

---

## Post #14 by @lassoan (2023-07-06 18:39 UTC)

<p>The “skin” barely exists, it looks like some disconnected single-voxel boundary that is just thrown on top of the other structures. Maybe you can try to hide all the other segments, in masking settings allow overlap (to prevent the “skin” from overwriting internal structures), then make the skin boundary thicker using Margin effect, and then fill what is inside the skin, using Islands effect.</p>

---
