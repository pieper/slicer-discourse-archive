# Distorted Images from DICOM File

**Topic ID**: 16617
**Date**: 2021-03-18
**URL**: https://discourse.slicer.org/t/distorted-images-from-dicom-file/16617

---

## Post #1 by @JacobD (2021-03-18 14:51 UTC)

<p>Hello,</p>
<p>I have imported a DICOM file of a shoulder MRI scan, however, each view appears distorted. When attempting to load the axial view image set, the axial view scan is clear, and the other views are blurry. When attempting to load the coronal view image set, the axial view is blurry, and the other views are partially clear, with a ripple appearance along the edges of the bones. I have included images of each loaded file in this post to show how the views appear. Is there a method to viewing these images clearly?</p>
<p>Thank you,<br>
Jacob</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f1c4c9517d44eb3140de603ac6073950b69c864.jpeg" data-download-href="/uploads/short-url/kq0UlTTRImzd5M9d3EDSUgWbX92.jpeg?dl=1" title="Axial View Scan" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f1c4c9517d44eb3140de603ac6073950b69c864_2_690x385.jpeg" alt="Axial View Scan" data-base62-sha1="kq0UlTTRImzd5M9d3EDSUgWbX92" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f1c4c9517d44eb3140de603ac6073950b69c864_2_690x385.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f1c4c9517d44eb3140de603ac6073950b69c864_2_1035x577.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f1c4c9517d44eb3140de603ac6073950b69c864_2_1380x770.jpeg 2x" data-dominant-color="B4B4B9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Axial View Scan</span><span class="informations">2880×1608 530 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c663b1b8e55126adb424e1ea257833940b313baf.jpeg" data-download-href="/uploads/short-url/sj28fqFazIlCM2sZ49H8jLX1UOH.jpeg?dl=1" title="Coronal View Scan" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c663b1b8e55126adb424e1ea257833940b313baf_2_690x385.jpeg" alt="Coronal View Scan" data-base62-sha1="sj28fqFazIlCM2sZ49H8jLX1UOH" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c663b1b8e55126adb424e1ea257833940b313baf_2_690x385.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c663b1b8e55126adb424e1ea257833940b313baf_2_1035x577.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c663b1b8e55126adb424e1ea257833940b313baf_2_1380x770.jpeg 2x" data-dominant-color="A5A5A9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Coronal View Scan</span><span class="informations">2880×1608 538 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2021-03-18 14:56 UTC)

<p>Those are not distortions. As shown in the volume spacing you have a very anisotropic data, z spacing is almost 20 times less resolution that xy plane.</p>

---

## Post #3 by @lassoan (2021-03-18 15:44 UTC)

<p>This protocol of acquiring 3 sparse volumes (instead of one high-resolution volume) is very common for musculoskeletal MRI, probably because it saves acquisition time and it is fine for humans to read such images. Unfortunately, these images are not optimal for 3D analysis. See this topic for more details:</p>
<aside class="quote quote-modified" data-post="2" data-topic="2941">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2">Combining volumes - what am I missing?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In general, these multiple low-resolution acquisitions are not well suited for any 3D processing, so the best would be to acquire proper 3D volume, with as isotropic spacing (cubic voxel shape) as possible. 
You may try to find toolkits that can create an isotropic super-resolution image from multiple low-resolution sweeps, but this is a difficult image reconstruction problem, so there are no standard solutions. Have a look at this post <a href="https://discourse.slicer.org/t/import-volume-by-projections/2871/6">Import volume by projections</a> for info on a toolkit that mig…
  </blockquote>
</aside>


---

## Post #4 by @pieper (2021-03-18 16:56 UTC)

<p>A colleague suggested this work and the SMORE technique from Jerry Prince’s group at JHU.  I don’t know if there’s an implementation available.</p>
<aside class="onebox pdf">
  <header class="source">
      <a href="https://arxiv.org/pdf/1802.09431.pdf" target="_blank" rel="noopener">arxiv.org</a>
  </header>
  <article class="onebox-body">
    <a href="https://arxiv.org/pdf/1802.09431.pdf" target="_blank" rel="noopener"><span class="pdf-onebox-logo"></span></a>
<h3><a href="https://arxiv.org/pdf/1802.09431.pdf" target="_blank" rel="noopener">1802.09431.pdf</a></h3>

<p class="filesize">1026.25 KB</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p><a href="http://www.cs.jhu.edu/cista/455/Lectures/Segmentation-2%20%28Rev%20D%29.pdf">http://www.cs.jhu.edu/cista/455/Lectures/Segmentation-2%20(Rev%20D).pdf</a></p>

---

## Post #5 by @lassoan (2021-03-18 18:30 UTC)

<p>That SMORE super-resoution looks beautiful. Let’s continue the discussion at the original topic (<a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2" class="inline-onebox">Combining volumes - what am I missing? - #2 by lassoan</a>) so that we have all the information about potentially useful approaches in one place.</p>

---

## Post #6 by @JacobD (2021-03-18 22:48 UTC)

<p>Thank you for the information. My knowledge of using 3D Slicer is limited as I am learning information, and I appreciate your time and assistance. If using data with isotropic spacing for better resolution images is the better way to analyze 3D volumes, are there methods for obtaining this type of data without understanding computer programming?</p>
<p>Would anyone be able to explain or provide a source that explains how to complete the crop volume module method that was mentioned?</p>
<aside class="quote no-group" data-username="Combining volumes - what am I missing?" data-post="2" data-topic="2941">
<div class="title">
<div class="quote-controls"></div>
<a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2">Combining volumes - what am I missing?</a></div>
<blockquote>
<p>Create a high-resolution isotropic volume from any of the input volumes, using Crop volume module. Then create a segmentation node using this isotropic volume as master volume. After this you can switch between master volumes - the segmentation node’s internal binary labelmap representation will remain high-resolution and isotropic.</p>
</blockquote>
</aside>
<p>Thank you,<br>
Jacob</p>

---

## Post #7 by @Juicy (2021-03-22 21:27 UTC)

<p>To get a more isotropic dataset this ideally needs to be done on the MRI machine by using thinner slice thicknesses when performing the scan, however, I think that this would result in very long scan times which is why MRI often uses thick slices.</p>
<p>You can use the crop volume module to make the voxels isotropic. Go to the crop volume module (under converters). You need to make a Region of Interest (ROI) you can click display ROI and one usually appears. If you want to make the volume smaller you can adjust that shape of the ROI in the slice view windows. You need to click isotropic spacing in the advanced area and b spline interpolation may help slightly to smooth the volume.</p>
<p>Unfortunately you will find that this will not help much. Without a dataset originally acquired with thin slices it is pretty difficult to get good results when segmenting, doing 3D rendering etc. What are you actually trying to do with this volume?</p>

---
