---
topic_id: 45967
title: "Slice Resample And Export Along An Oblique Plane"
date: 2026-01-28
url: https://discourse.slicer.org/t/45967
---

# Slice, resample and export along an oblique plane

**Topic ID**: 45967
**Date**: 2026-01-28
**URL**: https://discourse.slicer.org/t/slice-resample-and-export-along-an-oblique-plane/45967

---

## Post #1 by @N-Van (2026-01-28 09:15 UTC)

<p>Hi,</p>
<p>new here. I’m processing CT scan data and I need to extract a resampled, arbitrarily oriented, cross section of my volume. I need a slice that doesn’t show artifacts/stripes, and I need it with the same resolution as the volume (i.e. not a screen shot). For those familiar with Fiji, I need the exact same thing as “Reslice”, but with a plane that can be oriented in any direction.</p>
<p>I found and adapted this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/volumes.html#extract-slice-from-volume" rel="noopener nofollow ugc">code</a></p>
<p>It requires the preliminary creation of a markup plane, which is used for creating a new volume with unitary thickness. This volume can then be exported as a 2D image with correct dimensions.</p>
<p>What I do is rotate a plane (Slice intersection/Interaction), focusing on the yellow view, until I find the orientation I need. Then I create a markup plane directly on the yellow view and run my script. That works very well.</p>
<p>The only problem is that the markup plane is always way too large when I create it:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a15a63bc3dbf61b9e0ac0393b8d6ffb45463bf2.jpeg" data-download-href="/uploads/short-url/f8sZIg5aAZTOiYroW215LbLPjea.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a15a63bc3dbf61b9e0ac0393b8d6ffb45463bf2_2_690x412.jpeg" alt="image" data-base62-sha1="f8sZIg5aAZTOiYroW215LbLPjea" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a15a63bc3dbf61b9e0ac0393b8d6ffb45463bf2_2_690x412.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a15a63bc3dbf61b9e0ac0393b8d6ffb45463bf2_2_1035x618.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a15a63bc3dbf61b9e0ac0393b8d6ffb45463bf2_2_1380x824.jpeg 2x" data-dominant-color="565362"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1148 288 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I know I can manually reduce its width and height, but I’m looking for an automatic way to do that. More precisely, I’m looking for a way to adjust the markup plane to the valid data displayed in the yellow view:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f775b0186a72594bbe34c8c55f535f588e6bccd9.jpeg" data-download-href="/uploads/short-url/zj84YGVs4g8jSl0la9oo7S01syR.jpeg?dl=1" title="Screenshot_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f775b0186a72594bbe34c8c55f535f588e6bccd9_2_690x429.jpeg" alt="Screenshot_2" data-base62-sha1="zj84YGVs4g8jSl0la9oo7S01syR" width="690" height="429" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f775b0186a72594bbe34c8c55f535f588e6bccd9_2_690x429.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f775b0186a72594bbe34c8c55f535f588e6bccd9_2_1035x643.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f775b0186a72594bbe34c8c55f535f588e6bccd9_2_1380x858.jpeg 2x" data-dominant-color="302D2B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2</span><span class="informations">1399×871 70.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The validity of the displayed data can be accessed with the data probe (it displays “out of frame” for the surrounding pixels), so maybe I’m looking for a way to get all the valid pixels in the selected view and then their bounding box.</p>
<p>Any idea, anyone ?</p>

---

## Post #2 by @pieper (2026-01-28 09:53 UTC)

<p>You can use the Transforms to move the volume instead of just using the view.  Then you can resample the volume through the transform so that the pixels are in the plane of interest and you can then access the data as a slice, e.g. as a numpy array.</p>

---

## Post #3 by @N-Van (2026-01-28 10:28 UTC)

<p>Thank you for your answer. This is probably what I’m going to do if don’t find any other solution.</p>
<p>I started by rotating the planes because I find it more convenient than rotating the whole volume, especially when there are multiple views to extract.</p>

---

## Post #4 by @muratmaga (2026-01-28 15:57 UTC)

<p>You may want to look into the “Reorient Volume” option in the CropVolume. Tutorial here to show an example of how to bring a randomly oriented volume to canonical orientation and then resample in that orientation, but the idea still applies:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/Tutorials/blob/main/Slicer_Modules/Crop_Volume/Readme.MD#using-cropvolume-to-simulatenously-reorient-and-resample-your-data">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials/blob/main/Slicer_Modules/Crop_Volume/Readme.MD#using-cropvolume-to-simulatenously-reorient-and-resample-your-data" target="_blank" rel="noopener nofollow ugc">github.com/SlicerMorph/Tutorials</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/Tutorials/blob/main/Slicer_Modules/Crop_Volume/Readme.MD#using-cropvolume-to-simulatenously-reorient-and-resample-your-data" target="_blank" rel="noopener nofollow ugc">Slicer_Modules/Crop_Volume/Readme.MD</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerMorph/Tutorials/blob/main/Slicer_Modules/Crop_Volume/Readme.MD#using-cropvolume-to-simulatenously-reorient-and-resample-your-data" rel="noopener nofollow ugc"><code>main</code></a>
</div>


      <pre><code class="lang-md">### Crop Volume
Regardless of whether you are only interested in a small subset of your volume, the entire volume (and volumes if you are working with more than one dataset in the same scene) is kept in the memory (RAM) in a Slicer session. During segmentation, memory consumption may increase 10X (e.g. if you have 1GB dataset, at times you may need 10GB of available RAM). For large volumes, you can greatly reduce your memory footprint and improve performance during segmentation, by creating a new volume that only contains the subset you are interested in. Alternatively, if you have to work with the full extend of the data, but encounter memory issue during subsequent operations, you may want to downsample your volume.  `CropVolume` is the easiest way of achieving downsampling (or alternatively supersampling) your volumes. 

Additionally, you can use the CropVolume module simulatenously reorient and resample your data (see below)

1. Load the Sample MicroCT data as shown in the `ImageStacks` module

2. Enter the settings shown below. If the ROI creates is too small, hit the **Fit ROI to Volume** button and hit Apply. Then choose to create a new volume that will contain the output of the operation. In my case I called it **left_side_damaged_reduced**, which will be reduced by 50% (Spacing Factor is 2) in each axis. Accordingly, the image spacing will doubled. Compare the reported input and output volume dimensions and spacing. This operation will result in 8 folds reduction in the data volume, at the expense of image detail. This is because spacing scale of 2 is applied to each axis, and since we have 3 axes, the resultant data is reduced 2^3 times, or 8 folds.

&lt;img src="CropVolume1.png" width="800px"/&gt;

2. Now, repeat the procedure one more time, but this time set the limits of the ROI by modifying the small circular handles in slice views. I set my ROI to contain only the nasal region. Choose to create a new output volume (mine was called **Nasal_septum_and_turbinates**), and disable the interpolation. We do not need to interpolate the voxel intensity values, because we simply removing the data outside of our ROI and not doing anything else to the rest. Compare the resultant image dimensions and spacing of input and output volumes. Hit Apply. This procedure also reduces the data volume approximately 10 folds, but there is no reduction in the image quality. 

&lt;img src = "CropVolume2.png"&gt;


**Technical Note:** you don't have to use integer values as the Spacing Scale. For example, if you enter **1.25**, you reduce memory usage by factor of 2 (1.953 to be more precise) because 1.25^3 is approximately 2. You only degraded your data by 25% in this case.  


More detail about [`CropVolume` can be found here.](https://slicer.readthedocs.io/en/latest/user_guide/modules/cropvolume.html)
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/Tutorials/blob/main/Slicer_Modules/Crop_Volume/Readme.MD#using-cropvolume-to-simulatenously-reorient-and-resample-your-data" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @N-Van (2026-01-28 17:36 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="45967">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>you can then access the data as a slice, e.g. as a numpy array.</p>
</blockquote>
</aside>
<p>Actually that gives me an idea: convert the resampled slice to an np array and get the bounding box of non zero values.</p>

---

## Post #6 by @N-Van (2026-01-28 17:43 UTC)

<p>Thank you for hinting me at this module. In my case I don’t have any prefered orientation for the whole scan (several specimens may have been scanned together), and I will have to select multiple planes in each volume. Reorienting the whole volume is not the most convenient approach, that’s why I started with cross section planes.</p>

---
