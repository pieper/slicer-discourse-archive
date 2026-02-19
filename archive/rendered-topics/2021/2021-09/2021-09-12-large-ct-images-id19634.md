---
topic_id: 19634
title: "Large Ct Images"
date: 2021-09-12
url: https://discourse.slicer.org/t/19634
---

# Large CT images

**Topic ID**: 19634
**Date**: 2021-09-12
**URL**: https://discourse.slicer.org/t/large-ct-images/19634

---

## Post #1 by @coreg (2021-09-12 21:13 UTC)

<p>Hello,<br>
I am working with large CT images of an entire human body.<br>
Dicom convertion is done with Dicom to Nifti converter from C.Rorden.<br>
Voxel spacing is typically 0.9x0.9x0.6 and the dims ranging rnd 512x512x2000.<br>
The filesize after dicom import ranges between 750mb to 1.500gb.<br>
In order to reduce filesize,<br>
I ususally crop ‘air’ and resample to voxelsize o 1x1x1 (lin. interpolation),<br>
which does help a bit in reducing filesize. We save the volume as a .nrrd filetype.<br>
Using Slicerversion 4.10.1</p>
<p>What other steps can be taken in order to reduce filesize?</p>
<p>Thank you.</p>

---

## Post #2 by @muratmaga (2021-09-13 01:36 UTC)

<p>750-1.gGB volumes are not actually that big. Why do you need to reduce the filesize any further?</p>

---

## Post #3 by @lassoan (2021-09-13 14:14 UTC)

<aside class="quote no-group" data-username="coreg" data-post="1" data-topic="19634">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/0ea827/48.png" class="avatar"> coreg:</div>
<blockquote>
<p>Using Slicerversion 4.10.1</p>
</blockquote>
</aside>
<p>Always use at least the latest Slicer Stable Release and try the latest Slicer Preview Release, too, because we are constantly improve performance, add features, and remove bugs.</p>
<aside class="quote no-group" data-username="coreg" data-post="1" data-topic="19634">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/0ea827/48.png" class="avatar"> coreg:</div>
<blockquote>
<p>Voxel spacing is typically 0.9x0.9x0.6 and the dims ranging rnd 512x512x2000.<br>
The filesize after dicom import ranges between 750mb to 1.500gb.<br>
In order to reduce filesize,<br>
I ususally crop ‘air’ and resample to voxelsize o 1x1x1 (lin. interpolation),</p>
</blockquote>
</aside>
<p>This sounds good, but 0.9x0.9x0.6 to 1.0x1.0x1.0 resampling means that you reduce the file size to about half, which is not much. If your computer has problems dealing with this file size then you can increase the spacing to 1.5x1.5x1.5 or 2.0x2.0x2.0 or even higher.</p>

---

## Post #4 by @coreg (2021-09-13 21:48 UTC)

<p>Computer does not handle those filesizes all that well.</p>

---

## Post #5 by @coreg (2021-09-13 21:53 UTC)

<p>Thank you.<br>
I typically use the latest release, but Im somewhat locked into 4.10 for this project.<br>
We use the markup tool a lot and export fiducial points to .fcsv. I believe the coordinate systems are different between 4.10 and 4.11. and I dont want to change the existing processing pipeline.</p>

---

## Post #6 by @lassoan (2021-09-13 22:59 UTC)

<aside class="quote no-group" data-username="coreg" data-post="5" data-topic="19634">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/0ea827/48.png" class="avatar"> coreg:</div>
<blockquote>
<p>I believe the coordinate systems are different between 4.10 and 4.11</p>
</blockquote>
</aside>
<p>You can choose that coordinate system you want to save in. We have not exposed this on the GUI, as we want to encourage everybody to consistently use LPS coordinate system in all files (as in DICOM, and as it has been always done for images, transforms, etc).</p>
<p>If for a legacy project you want to change what coordinate system is used, you can change the coordinate system for all newly created markups fiducial nodes that are saved in fcsv format, by adding this code snippet to your <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file">application startup script</a>:</p>
<pre data-code-wrap="python"><code class="lang-python">defaultFiducialStorageNode = slicer.vtkMRMLMarkupsFiducialStorageNode()
defaultFiducialStorageNode.SetCoordinateSystem(slicer.vtkMRMLStorageNode.RAS)
slicer.mrmlScene.AddDefaultNode(defaultFiducialStorageNode)
</code></pre>
<p>Coordinate system choice is preserved if you load and save a node, so you only need to switch the coordinate system for a node once. Even if you load and save the node on another Slicer instance where the startup file was not modified, the coordinate system will still be still RAS.</p>
<p>In case you ever need to change coordinate system in a node to RAS that has been already saved as<br>
LPS then you can run this:</p>
<pre data-code-wrap="python"><code class="lang-python">fiducialNode = getNode('F')
fiducialNode.GetStorageNode().SetCoordinateSystem(slicer.vtkMRMLStorageNode.RAS)
</code></pre>

---

## Post #7 by @muratmaga (2021-09-13 23:44 UTC)

<aside class="quote no-group" data-username="coreg" data-post="5" data-topic="19634">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/0ea827/48.png" class="avatar"> coreg:</div>
<blockquote>
<p>We use the markup tool a lot and export fiducial points to .fcsv. I believe the coordinate systems are different between 4.10 and 4.11. and I dont want to change the existing processing pipeline.</p>
</blockquote>
</aside>
<p>Coordinate transformaiton from RAS to LPS is very simple, and involves negating the sign of the first two coordinate. There are many benefits to keeping the fiducial coordinates in LPS so that they are exactly in the same reference frame as your images.</p>
<p>I would suggest converting your existing RAS fiducials to LPS, and then start using the latest version of Slicer. That you will also futureproof your data.</p>
<p>There are also quite a few updates to the Markups tool as well.</p>

---

## Post #8 by @coreg (2021-09-14 13:37 UTC)

<p>Thank you for the suggestion of editing the startup script. I was unaware of this option. That might be the way to go for now, since I do see the advantages of the newer version.</p>

---

## Post #9 by @coreg (2021-09-14 13:40 UTC)

<p>Thank you for your input. You certainly correct of the improved featurelist of the markuptool, which is  worth switching too.</p>

---

## Post #10 by @Chris_Rorden (2021-09-16 12:51 UTC)

<p>You may want to try <a href="https://github.com/rordenlab/MRIcroGL/releases" rel="noopener nofollow ugc">MRIcroGL</a> for resampling large images:</p>
<ol>
<li>Use the Import/Tools/Crop to interactively crop large images. Do this first to remove parts of the field of view that are not of interest.</li>
<li>Use Import/Tools/Resize to rescale your image. You can choose your interpolation <a href="https://legacy.imagemagick.org/Usage/filter/" rel="noopener nofollow ugc">filter</a> (nearest, Linear, hermite, bell, spline, Lanczos, or Mitchell). All downsampling interpolation uses <a href="https://nbviewer.jupyter.org/urls/dl.dropbox.com/s/s0nw827nc4kcnaa/Aliasing.ipynb" rel="noopener nofollow ugc">anti-aliasing</a>. The Lanczos sinc filter is used by default for downsampling, it preserves high frequency edges better than linear interpolation. While your can choose custom scaling, it does provide three quick buttons:</li>
</ol>
<ul>
<li>“Isotropic shrink”, e.g. this would convert your 0.9x0.9x0.6 to 0.9x0.9x0.9</li>
<li>512mb Texture is a common maximum texture size for many integrated graphics cards. It will provide fluid rendering performance for most modern integrated and discrete graphics.</li>
<li>2048mb Texture is the ultimate limit for any OpenGL-based texture.</li>
</ul>
<p>I know your primary interest is using Slicer, but it is worth noting that MRIcroGL preferences allows you to set the maximum texture size it will load (512mb is the default). If you have a high end graphics card, you can set this to 2048 to avoid downsampling images. If you do set this to 512 and load a bigger texture, the cropping and rescaling are applied to the original large dataset, not the dataset reduced to fit on your graphics card.</p>

---
