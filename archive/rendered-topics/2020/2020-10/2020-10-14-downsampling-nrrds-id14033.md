# Downsampling NRRDs

**Topic ID**: 14033
**Date**: 2020-10-14
**URL**: https://discourse.slicer.org/t/downsampling-nrrds/14033

---

## Post #1 by @Christopher_Pinto (2020-10-14 12:14 UTC)

<p>What is the best way to make my NRRDs more lightweight? I tried using the Brain Resampling module, but its very temperamental and only works on a few occasions. I have files on the 3-4MB size that need to be around 10-20KB.</p>

---

## Post #2 by @muratmaga (2020-10-14 15:57 UTC)

<p>CropVolume and set the factor to 3 or 4. That will give a reduce your total data volume by 27 or 64.</p>

---

## Post #3 by @lassoan (2020-10-15 03:37 UTC)

<aside class="quote no-group" data-username="Christopher_Pinto" data-post="1" data-topic="14033">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/christopher_pinto/48/8444_2.png" class="avatar"> Christopher_Pinto:</div>
<blockquote>
<p>I tried using the Brain Resampling module, but its very temperamental and only works on a few occasions</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a>’s solution should work well - I’m just curious: what you did, what you expected to happen, and what happened instead when you tried to use “Resample Image (BRAINS)” module?</p>

---

## Post #4 by @Chris_Rorden (2020-10-15 13:21 UTC)

<p>When shrinking images you need to be concerned about <a href="https://nbviewer.jupyter.org/urls/dl.dropbox.com/s/s0nw827nc4kcnaa/Aliasing.ipynb" rel="noopener nofollow ugc">aliasing effects</a>. The slicer CropVolume feature does not use an anti-aliasing filter. You can see this in the image below. The source image is a 512x512x512 zone plate created with the Python code at the bottom of the post. The left panel shows the original image. The upper right shows Slicer’s CropVolume with a x4 scale factor and linear interpolation. The lower right shows MRIcroGL’s Import/Tools/Resize with the same scale factor and interpolation, but using an anti-aliased filter. Note that MRIcroGL also allows you to reduce precision, e.g. from 32-bits per voxel to 8-bits. Reducing precision works well for some modalities (e.g. many MRI scans, or CT scan where you are only interested in bone), but not others (e.g. CT scan where you want to preserve soft tissue and bone).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91a3410316e88e0854041594493aa3fef121f815.jpeg" data-download-href="/uploads/short-url/kMn0chXUjijFralQyr3kxlKeq2x.jpeg?dl=1" title="ZonePlate" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91a3410316e88e0854041594493aa3fef121f815_2_649x500.jpeg" alt="ZonePlate" data-base62-sha1="kMn0chXUjijFralQyr3kxlKeq2x" width="649" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91a3410316e88e0854041594493aa3fef121f815_2_649x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91a3410316e88e0854041594493aa3fef121f815.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91a3410316e88e0854041594493aa3fef121f815.jpeg 2x" data-dominant-color="858585"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ZonePlate</span><span class="informations">665×512 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Another way to create images that require less disk space is to remove haze. MRI and CT scans tend to exhibit a little random noise in air. If you identify the air and set them to all consistently have the same intensity as the darkest value in the image, the compression will be much more effective.</p>
<p>The way I do this is to use a multi-level implementation of <a href="https://en.wikipedia.org/wiki/Otsu%27s_method" rel="noopener nofollow ugc">Otsu’s Method</a> to detect the darkest voxels. I then erode this mask by one voxel to allow for better partial voluming and gradient generation.</p>
<p>You can try this out using <a href="https://www.nitrc.org/plugins/mwiki/index.php/mricrogl:MainPage" rel="noopener nofollow ugc">MRIcroGL</a>. Drag and drop your NRRD file to open it, and then choose the View/RemoveHaze or View/RemoveHazeWithOptions menu item. If you are happy with the result, choose File/SaveVolume. The efficiency of this method will depend on the ratio of air to object in your image. If you want to combine both resizing and removing haze, I would remove haze as the last step. The one issue with removing haze is that it can disrupt intensity homogeneity correction and mixed-Gaussian models for segmentation, such as employed by SPM. However, given your aggressive size reduction, I do not think those are your intended application.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e88ce7c594a4faa4db15e87191fcd3e7757cfa70.jpeg" data-download-href="/uploads/short-url/xbeF0JQa5lSdau6mdo0z4S1qUve.jpeg?dl=1" title="haze" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e88ce7c594a4faa4db15e87191fcd3e7757cfa70_2_690x456.jpeg" alt="haze" data-base62-sha1="xbeF0JQa5lSdau6mdo0z4S1qUve" width="690" height="456" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e88ce7c594a4faa4db15e87191fcd3e7757cfa70_2_690x456.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e88ce7c594a4faa4db15e87191fcd3e7757cfa70_2_1035x684.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e88ce7c594a4faa4db15e87191fcd3e7757cfa70_2_1380x912.jpeg 2x" data-dominant-color="7A797A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">haze</span><span class="informations">1769×1170 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code>#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python3 d_speed_size.py        : test speed/compression for folder 'corpus'
# python3 d_speed_size.py indir  : test speed/compression for folder 'indir'

import math
import numpy as np
import nibabel as nib

nvox = 256
print(nvox)
img = np.zeros((nvox, nvox, nvox))
center = (img.shape[0]/2.,img.shape[1]/2.,img.shape[2]/2.)
grid_x, grid_y,grid_z  = np.mgrid[0:img.shape[0], 0:img.shape[1], 0:img.shape[2]]
grid_x = grid_x - center[0]
grid_y = grid_y - center[1]
grid_z = grid_z - center[2]
img = np.sqrt (np.square(grid_x) + np.square(grid_y) + np.square(grid_z))
img = np.reshape(img, (nvox, nvox, nvox))
header = nib.Nifti1Header()
affine = np.array([[1,0,0,-center[0]],[0,1,0,-center[1]],[0,0,1,-center[2]],[0,0,0,1] ])
nii = nib.Nifti1Image(img, affine, header)
nib.save(nii, 'distance.nii')
km = 0.7*math.pi
rm = max(center)
w = rm/10.0;
with np.nditer(img, op_flags=['readwrite']) as it:
    for vox in it:
        term1 = math.sin( (km * math.pow(vox,2)) / (2 * rm) )
        term2 = 0.5*np.tanh((rm - vox)/w) + 0.5;
        vox[...] = term1 * term2;
nii = nib.Nifti1Image(img, affine, header)
nib.save(nii, 'zoneplate.nii')
</code></pre>

---

## Post #5 by @Christopher_Pinto (2020-10-15 13:57 UTC)

<p>Hi! I imagine the Resample Image module was meant to match the pixel density / slicing of a reference image. I would put the NRRD that I wanted to downsample in the Input Image, and the reference image would be a model that was the right size. After running the module, it would output an NRRD of similar size (on the MB scale).</p>
<p>At one point, I was putting no reference imagine in and then it perfectly downsampled the images to about 10-15 KB. However, it doesn’t work that way anymore which is why I am confused.</p>

---

## Post #6 by @lassoan (2020-10-15 18:26 UTC)

<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> thank you for your very insightful response.</p>
<p>Blanking out voxels outside the head to reduce image size is a good idea. It can be done in Slicer using Mask volume effect in Segment Editor. You can preview the mask, restrict it to outside air, grow/shrink before you apply it. The automatic steps Chris described could be easily implemented, too (except Otsu thresholding does not generally work well for identifying background on many image types), but probably we will not work on it unless users ask for it.</p>
<p>You are right that in theory, low-pass filter should be applied before strong undersampling. In practice, however, images are rarely undersampled very heavily in analysis pipelines, because the loss of information would be so significant, that some extra aliasing artifacts (which are usually very mild for medical images) would not matter much, and removing them would take extra processing time. I agree that we should offer an optional antialiasing filtering step for the very few special cases where it does matter and the additional computation time is not a problem. Interestingly, ITK does not offer a readily usable solution (the advice they give is essentially to “do some Gaussian smoothing” see <a href="https://discourse.itk.org/t/resampling-to-isotropic-signal-processing-theory/1403/16">here</a>), but VTK has a very nicely designed filter for this (vtkImageResize, which performs all necessary anti-aliasing and interpolation).</p>

---

## Post #7 by @Chris_Rorden (2020-10-16 14:49 UTC)

<p>There are a few options for downsampling 3D images with anti-aliasing:</p>
<ol>
<li>One can first apply a low-pass filter (e.g Gaussian blur) and then apply downsampling. Both functions are separable, so for a 3D image this is six 1D passes. The disadvantage is a Gaussian blur has pretty long tails, so it is a wide kernel. You also want to consider the appropriate precision for the data between these two stages, which might have heavy memory demands for large images. The advantage is that you can bolt together two existing stages.</li>
<li>Adjust the kernel width of the downsampling kernel. This is described by Schumacher’s <a href="http://inis.jinr.ru/sl/vol1/CMC/Graphics_Gems_3,ed_D.Kirk.pdf" rel="noopener nofollow ugc">General Filtered Image Rescaling</a>, with code <a href="http://www.realtimerendering.com/resources/GraphicsGems/gems.html#gemsiii" rel="noopener nofollow ugc">here</a>. Since the filter is separable, one completes three 1D passes. This is what MRIcroGL uses.</li>
<li>
<a href="http://chemaguerra.com/fast-convolutions/" rel="noopener nofollow ugc">FFT</a> can be even more efficient, but requires a bit of work to apply to non-power-of-two images.</li>
</ol>

---

## Post #8 by @lassoan (2020-10-16 15:43 UTC)

<p>Thanks a lot for these additional information. “General Filtered Image Rescaling” method looks nice. To me VTK’s image resize filter (<a href="https://github.com/Kitware/VTK/commit/5ced2edd97f8946e0e589f5c411d31bbc22c8371">https://github.com/Kitware/VTK/commit/5ced2edd97f8946e0e589f5c411d31bbc22c8371</a>) looks even better, more efficient, but I did not do a detailed review or comparison of processed outputs. The only thing that is missing from all these implementations is the ability to resample using arbitrary non-linear transforms. So, we could only use these methods if the image has no transform (or just a linear transform) applied on it.</p>

---

## Post #9 by @pieper (2020-10-16 16:12 UTC)

<p>I agree, thanks <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> for the insight.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>, we should be able to make a pipeline that applies the nonlinear transform first and then pipe it through <code>vtkImageResize</code> if we think the quality will be better.  This would make a nice cli alternative to BRAINSResample.  (would be interesting to see some examples anyway to assess the practical impact).</p>

---

## Post #10 by @lassoan (2020-10-16 17:01 UTC)

<p>It is hard to come up with cases where anti-aliasing matters in <em>quantitative image analysis</em> pipelines, because small details (that anti-aliasing artifacts can interfere with) are mostly lost anyway due to decreased resolution of the downsampled image. This image from <a href="http://bigwww.epfl.ch/publications/thevenaz9901.pdf">Thevenaz</a> demonstrates it very well:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01bd3efcc974ae3c61a74b36bbc1fb910fb77039.jpeg" data-download-href="/uploads/short-url/fnVZ6zGEAodb9jXVIsVmRyCmPT.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01bd3efcc974ae3c61a74b36bbc1fb910fb77039_2_566x500.jpeg" alt="image" data-base62-sha1="fnVZ6zGEAodb9jXVIsVmRyCmPT" width="566" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01bd3efcc974ae3c61a74b36bbc1fb910fb77039_2_566x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01bd3efcc974ae3c61a74b36bbc1fb910fb77039_2_849x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01bd3efcc974ae3c61a74b36bbc1fb910fb77039_2_1132x1000.jpeg 2x" data-dominant-color="C1C1C1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1212×1070 487 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Anti-aliasing may matter in very special cases, for example when you are not interested in structural details but just want to preserve overall texture appearance. Probably we don’t need to make the regular imaging pipeline more complicated because of such narrow use cases, but we could add a simple scripted module that offers anti-aliased resampling. If there are any SlicerMorph modules that offer image downsampling, then it should use vtkImageResize (which is, based on its documentation, is very fast and has the best memory efficiency among all the algorithms mentioned above).</p>

---

## Post #11 by @pieper (2020-10-16 18:44 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="14033">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If there are any SlicerMorph modules that offer image downsampling</p>
</blockquote>
</aside>
<p>Currently the only option in the ImageStacks module is skipping ever other slice and every other pixel row and column.  It was another one of those “perfect is the enemy of good” situations where we didn’t want to invest a lot of time in it and also wanted to make sure we didn’t need to read the whole volume before applying the resample (since a main point of downsampling in the module is to avoid reading the whole volume into memory because it’s too big to work with).</p>

---

## Post #12 by @lassoan (2020-10-16 18:56 UTC)

<p>It looks like that vtkImageResize supports streaming, so it should be able to resize huge volume without loading into memory. However, not all file readers support streaming, so the image may need to be first converted to a streamable format. It is all doable, but requires some work, which is hard to find time for if users are happy with the current implementation.</p>

---

## Post #13 by @muratmaga (2020-10-16 19:35 UTC)

<p>What formats would that be? Primarily we need the downsampling when users are importing these image sequences with thousands of slices, and they do not have the memory to import at full resolution. Data usually comes in traditional 2D formats (jpg, png, tiff, bmp). Would generating a nrrd header suffice to stream them?</p>

---

## Post #14 by @lassoan (2020-10-16 20:00 UTC)

<p>Yes, it seems VTK’s nrrd reader supports streaming and so it would be enough to decompress all tiff/png/jpg images and append them into a single large raw file.</p>

---

## Post #15 by @muratmaga (2020-10-16 20:51 UTC)

<p>I was thinking of generating a nhdr file that simply points out to the file list. But appending them into a single large raw file is a possibility.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> would this help with some of the weird selection issues we have been seeing on Mac in selection? And would it give us more flexibility in implementing the VOI subsetting at the import time than the current solution?</p>

---

## Post #16 by @pieper (2020-10-16 21:08 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="15" data-topic="14033">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>would this help with some of the weird selection issues we have been seeing on Mac</p>
</blockquote>
</aside>
<p>No, I don’t think it would help with the selection issue, which appears to be in the way Qt uses the native file browser.</p>
<p>But generating an nhdr filelist is essentially the same task that is already done with the UI.  If we switch to a filepattern to generate the filelist as we’ve discussed it would be basically the same thing.  I’m not sure uncompressing the whole dataset just to get streaming is going to be worth the effort/time/disk space if the goal is to quickly load the smaller volume.</p>
<p>Currently <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/ImageStacks/ImageStacks.py#L350-L374">ImageStacks</a> uses SimpleITK slice by slice and while it’s no good from an aliasing point of view it’s quick and efficient with little memory overhead.</p>
<p>It could be a good first step to compare some real-world data and see how much extra detail we might actually be able to preserve with extra filtering.  It’s possible the input data is oversampled to begin and there’s not much data loss, but it’s also possible there are some fine details that are worth trying to preserve.</p>

---

## Post #17 by @lassoan (2020-10-17 02:09 UTC)

<p>I agree that before developing any module, we would need to check on real data sets what improvement we can get.</p>
<p>Skipping anti-alias filtering may add a small high-frequency structured noise to the downsampled image, which may matter only in special cases, for example if you want to do bone texture analysis on the downsampled images. But if you wanted to take full advantage of your data then you would be better off with the original resolution, cropped to smaller chunk(s). So, high-quality downsampling may not be relevant for this either.</p>

---
