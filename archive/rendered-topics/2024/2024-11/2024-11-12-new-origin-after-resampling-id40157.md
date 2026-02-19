---
topic_id: 40157
title: "New Origin After Resampling"
date: 2024-11-12
url: https://discourse.slicer.org/t/40157
---

# New origin after resampling

**Topic ID**: 40157
**Date**: 2024-11-12
**URL**: https://discourse.slicer.org/t/new-origin-after-resampling/40157

---

## Post #1 by @sebquetin (2024-11-12 18:43 UTC)

<p>Hello,</p>
<p>I would like to ask about 3D slicer coordinate system. I understand from <a href="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html" class="inline-onebox" rel="noopener nofollow ugc">Coordinate systems — 3D Slicer documentation</a> that the origin is in the middle of the first (corner) voxel. However, after resampling, the origin stays the same, which I do not understand. If the origin is indeed the center of the corner voxel (and not the corner of the corner voxel), then the origin of the resampled volume should be new_origin = original_origin - original_spacing/2 + new_spacing/2 to be in the center of the new corner voxel. Am I missing something?<br>
This behavior was observed by doing the following:</p>
<ul>
<li>Importing a dcm series of CT scan in 3D slicer</li>
<li>Exporting this series a nrrd and observing the origin by opening the volume in python with sitk</li>
<li>go back to 3D slicer, resmaple the volume to a new spacing with “Resample Scalar Volume” linear interpolation</li>
<li>Exporting the new series to nrrd and observing in python with sitk that the spacing changed but the origin did not.</li>
</ul>
<p>Thank you for your help.<br>
Best regards,<br>
Sebastien</p>

---

## Post #2 by @lassoan (2024-11-12 18:46 UTC)

<p>Each voxel stores a sample of a continuous signal at the position of the voxel center. There is no need to change the origin of the sampling grid if you resample an image.</p>

---

## Post #3 by @sebquetin (2024-11-12 20:34 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8080be25c62bc7fe98501bcc6f242d3150cb3da.jpeg" data-download-href="/uploads/short-url/x6E0M99w2bUO5zxKupj4wGcBVLY.jpeg?dl=1" title="1000015679" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8080be25c62bc7fe98501bcc6f242d3150cb3da_2_666x500.jpeg" alt="1000015679" data-base62-sha1="x6E0M99w2bUO5zxKupj4wGcBVLY" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8080be25c62bc7fe98501bcc6f242d3150cb3da_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8080be25c62bc7fe98501bcc6f242d3150cb3da_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8080be25c62bc7fe98501bcc6f242d3150cb3da_2_1332x1000.jpeg 2x" data-dominant-color="989491"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000015679</span><span class="informations">1920×1440 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is the origin used to place the volume in space? If not, what is used to place the volume? For my application I need to retain the image original location. And to my current understanding I need to shift the origin when resampling in order to retain the image original location. Please see the attached pictures to understand my reasoning. Let’s say we have a 3mm by 3mm by 3mm volume (represented in blue in the graph) and then we resample it to 1mm by 1mm by 1mm (represented in red). Don’t we need to modify the origin in order for the resampled volume and the original volume to overlap perfectly?</p>
<p>Thank you for your support.</p>

---

## Post #4 by @lassoan (2024-11-13 01:20 UTC)

<aside class="quote no-group" data-username="sebquetin" data-post="3" data-topic="40157">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sebquetin/48/78510_2.png" class="avatar"> sebquetin:</div>
<blockquote>
<p>I need to retain the image original location. And to my current understanding I need to shift the origin when resampling in order to retain the image original location</p>
</blockquote>
</aside>
<p>No, there is no need to shift the origin to retain the location of the image. Maybe you think that the image starts at the corner of the first voxel and ends at the opposite corner of the last voxel, but this is not true. All that we know are samples of a continuous signal at grid point positions (voxel centers). Where the image appears to start and end on screen is just a matter of display choice.</p>
<p>It is reasonable to display the image as if it started a half voxel beyond the first and last sampling positions to give a hint to the user about voxel size at that position. However, it is actually an arbitrary decision. For nearest neighbor interpolation, showing the image starting half voxel before the first sample is justifiable; for linear interpolation, you would need to make some assumptions if you want to extrapolate, so some image viewers choose to not display anything beyond the centers of first and last voxels; for higher order interpolation you start to have exact information from the second or third voxel, and so it is common to pad the image (e.g., using mirroring) so that you can display something near the first voxel.</p>

---

## Post #5 by @pieper (2024-11-13 14:36 UTC)

<p><a class="mention" href="/u/sebquetin">@sebquetin</a> I agree with your premise that if you treat the “edge” of the volume as being a 1/2 pixel spacing box around the origin then you would want to pick an origin that takes into account the new pixel spacing so that edge remains in the same physical location.  There are several resampling options in Slicer, and Resample Scalar Volume is the simplest and comes from an old ITK example that apparently didn’t offer that behavior.  As <a class="mention" href="/u/lassoan">@lassoan</a> points out, the sampling grid is kind of arbitrary so as long as the pixel intensity values don’t shift in physical space this won’t matter for most purposes.  But it’s weird and maybe should be fixed if someone has time to investigate.</p>
<p>If you want to account for the spacing in the resampling, you can define your own sampling grid (i.e. a volume with specified origin, dimensions, directions, and spacings) and give it as the reference for one of the other more sophisticated resampling modules, such as Resample Image (BRAINS) or Resample Scalar/Vector/DWI.  Also I believe the Crop Volume module correctly offsets the origin when you specify the ROI and spacing, as opposed to the others where you provide the sampling grid explicitly.</p>

---

## Post #6 by @lassoan (2024-11-13 15:56 UTC)

<p>Good point, Slicer modules already performs this shift when the user sets an output image region explicitly. For example, in <a href="https://github.com/Slicer/Slicer/blob/9e1f2bd0b87c33aa74e1cb919e577c21a123463b/Modules/Loadable/CropVolume/Logic/vtkSlicerCropVolumeLogic.cxx#L553-L569">Crop volumes module</a> (user provides an ROI node and image spacing is modified via spacing scale parameter), and in <a href="https://github.com/Slicer/Slicer/blob/9e1f2bd0b87c33aa74e1cb919e577c21a123463b/Libs/vtkSegmentationCore/vtkCalculateOversamplingFactor.cxx#L477-L490">Segmentations module</a> (user provides region via a reference image and image spacing is modified via oversampling factor parameter).</p>
<p>I don’t think shifting the origin outside of the original voxel centers is a good default strategy in general, because that would burn in more of the <em>extrapolated</em> voxel values into the output image. This may not be desirable, because depending on the chosen interpolator and the extrapolation strategy, the result may be quite inaccurate. For example, you can test this by resampling an image using Crop volume module, using <code>Fit to volume</code>, and choosing <code>Windowed Sinc</code> interpolator:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21965853e41aeaabf1052d4261a1f3c2914ccee4.png" data-download-href="/uploads/short-url/4N7RTstgkBUifO6AAUtkKsloVLe.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21965853e41aeaabf1052d4261a1f3c2914ccee4_2_690x356.png" alt="image" data-base62-sha1="4N7RTstgkBUifO6AAUtkKsloVLe" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21965853e41aeaabf1052d4261a1f3c2914ccee4_2_690x356.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21965853e41aeaabf1052d4261a1f3c2914ccee4_2_1035x534.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21965853e41aeaabf1052d4261a1f3c2914ccee4_2_1380x712.png 2x" data-dominant-color="625D52"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3251×1680 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Anyway, it is good that all these options are already available in Slicer, so users can choose what works best for them.</p>

---

## Post #7 by @pieper (2024-11-13 16:09 UTC)

<p>Right, I don’t see a use case for picking an origin outside the original image volume, but adjusting it so that the “edge” of the volume is stationary does make sense.</p>

---

## Post #8 by @lassoan (2024-11-13 18:14 UTC)

<p>What we are discussing here (resampling an image to finer resolution while preserving the location of the image edges) is a use case. You could argue that since the new origin is still inside the “edges” of the original volume, we could still consider that the origin is inside the volume. However, this new origin is outside the bounding box of voxel centers of the original volume, which means that the voxel value at the new origin (and all new boundary voxels) are computed by extrapolation, therefore I would consider this origin to be picked outside of the original image volume.</p>
<p>People are aware that the image is interpolated when it is resampled but they may not be aware that if they also want to preserve the location of the image edges then the image has to be extrapolated as well, which may introduce additional error.</p>

---

## Post #9 by @pieper (2024-11-13 19:20 UTC)

<p>It’s not a huge issue, but my argument is that if you supersample the image, then the origin will shift ouside the bounding box of the original voxel centers, but it should shift exactly the amount so that it is 1/2 a spacing away from the same edges that were 1/2 spacing away from the original origin.  If you subsample, then the origin moves inside but still maintains the 1/2 spacing from the edge criteria.</p>

---

## Post #10 by @lassoan (2024-11-14 05:57 UTC)

<p>The question was also posted and discussed on the ITK forum:</p>
<aside class="onebox discoursetopic" data-onebox-src="https://discourse.itk.org/t/how-should-one-set-the-output-origin-when-resampling-an-image/7307">
  <header class="source">
      <img src="https://discourse.itk.org/uploads/default/optimized/1X/71db04d41479c229accbe8bf0b99195f75f46770_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.itk.org/t/how-should-one-set-the-output-origin-when-resampling-an-image/7307" target="_blank" rel="noopener" title="06:30PM - 12 November 2024">ITK – 12 Nov 24</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:120/105;"><img src="https://discourse.itk.org/uploads/default/original/2X/3/3adf1dc6b8787513c050a8952744199b6b1843eb.png" class="thumbnail" width="120" height="105"></div>

<div class="title-wrapper">
  <h3><a href="https://discourse.itk.org/t/how-should-one-set-the-output-origin-when-resampling-an-image/7307" target="_blank" rel="noopener">How should one set the output origin when resampling an image?</a></h3>
  <div class="topic-category">
    <div class="topic-header-extra">
      <div class="list-tags">
        <div class="discourse-tags">
          <svg class="fa d-icon d-icon-tag svg-icon svg-string"><use href="#tag"></use></svg>
            <span class="discourse-tag simple">simpleitk</span>
        </div>
      </div>
    </div>
  </div>
</div>

  <p>Hello,  I would like to know how to set the output origin when resampling a volume to a different spacing. I understand from Fundamental Concepts — SimpleITK 2.4.0 documentation that in SITK the origin is in the middle of the first (corner) voxel,...</p>

  <p>
    <span class="label1">Reading time: 1 mins 🕑</span>
      <span class="label2">Likes: 5 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @sebquetin (2024-11-14 14:15 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="40157">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>However, this new origin is outside the bounding box of voxel centers of the original volume, which means that the voxel value at the new origin (and all new boundary voxels) are computed by extrapolation, therefore I would consider this origin to be picked outside of the original image volume.</p>
</blockquote>
</aside>
<p>I understand that my usecase is specific. I want to have all my volumes perfectly overlapping and for me half a mm shift is important and that is why I am asking those questions. I also understand that for pixels/voxels outside the “voxel centers bounding box”, values will be extrapolated instead of interpolated and that this leads to an accuracy on position VS accuracy on voxel values trade-off.<br>
Now, there is still something I want to clarify.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35ee5df0139837994f0ca6bb49bddb16387ce789.jpeg" data-download-href="/uploads/short-url/7H60ihKYG12PamTyLpVYb25heJz.jpeg?dl=1" title="1000015702" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35ee5df0139837994f0ca6bb49bddb16387ce789_2_375x500.jpeg" alt="1000015702" data-base62-sha1="7H60ihKYG12PamTyLpVYb25heJz" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35ee5df0139837994f0ca6bb49bddb16387ce789_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35ee5df0139837994f0ca6bb49bddb16387ce789_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35ee5df0139837994f0ca6bb49bddb16387ce789_2_750x1000.jpeg 2x" data-dominant-color="B1A8A1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000015702</span><span class="informations">1920×2560 423 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please see the two graphs, where there are two cases, one image has been resampled with shifting of the origin and the other has been resamped without shifting of the origin. If we consider any value outside the “voxel centers bounding box” as being extrapolated; between the two problems, don’t we just move the extrapolation problem elsewhere? And isn’t it worse to have multiple adjacent voxels interpolated?</p>
<p>Please let me know if I am going in the wrong direction here.</p>

---

## Post #12 by @lassoan (2024-11-14 19:00 UTC)

<aside class="quote no-group" data-username="sebquetin" data-post="11" data-topic="40157">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sebquetin/48/78510_2.png" class="avatar"> sebquetin:</div>
<blockquote>
<p>I want to have all my volumes perfectly overlapping</p>
</blockquote>
</aside>
<p>Your volumes are not overlapping any better, regardless if you shift the origin or not: if you resample the volume it cannot perfectly overlap anymore with the original volume. In some image viewers it may appear that the images accurately overlap if you shift the origin; but in other image viewers (that don’t pad the image outside the voxel centers) the images appear to accurately overlap if you don’t shift the origin.</p>
<p>If you prefer to preserve the signal most accurately then <em>not</em> moving the origin is slightly better choice (you avoid burning in extrapolated data into the output image).</p>
<p>If you are not particularly concerned about introducing very subtle errors at the image boundary, and you want the resampled image edges appear at the same location as of the original image in <em>some</em> image viewers then you may decide to move the origin.</p>
<aside class="quote no-group" data-username="sebquetin" data-post="11" data-topic="40157">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sebquetin/48/78510_2.png" class="avatar"> sebquetin:</div>
<blockquote>
<p>for me half a mm shift is important and that is why I am asking those questions</p>
</blockquote>
</aside>
<p>Displacement of the image intensity signal would be a huge issue, but that’s not happening here in either case (with or without shift of the origin). You don’t need to worry about that.</p>
<aside class="quote no-group" data-username="sebquetin" data-post="11" data-topic="40157">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sebquetin/48/78510_2.png" class="avatar"> sebquetin:</div>
<blockquote>
<p>If we consider any value outside the “voxel centers bounding box” as being extrapolated; between the two problems, don’t we just move the extrapolation problem elsewhere?</p>
</blockquote>
</aside>
<p>No, you don’t have extrapolation elsewhere if you don’t shift the origin. The dashed region in the second image of your post above is not part of the output image.</p>

---

## Post #13 by @mikebind (2024-11-15 00:53 UTC)

<p>There are different, equally valid, metaphors for what the voxel values of an image might represent.  If your mental model is a continuous field which is sampled pointwise at the voxel centers, then it makes sense to consider that the “boundary” of the image does not extend beyond the outermost voxel centers.  On the other hand, if you imagine a CCD sensor (like on a digital camera), the voxel value represents something more like an integration of a signal over an area.  In that case, it makes sense to consider that the “boundary” of the image extends all the way to the edge of the voxel because the data summarized by that voxel value is gathered from that whole area.  In medical imaging, I think the truth is typically somewhere in between these two mental models.  We can’t actually sample anything at an infinitesimal point, but it also isn’t the case that a reconstruction algorithm really ends up representing a uniform data sampling across a full rectangular voxel out to the edges and no farther.  Instead, we get voxel values which represent something about the content of some signal that we attribute to a local spatial region. If we say that local spatial region is more like a point, then we get the interpretation of <a class="mention" href="/u/lassoan">@lassoan</a>.  If we say that local spatial region is more like an entire voxel, then we get the interpretation of <a class="mention" href="/u/pieper">@pieper</a>  and <a class="mention" href="/u/sebquetin">@sebquetin</a> , where the edge of the image is the edge of the voxel.</p>
<p>The argument of <a class="mention" href="/u/sebquetin">@sebquetin</a>  of just shifting the extrapolation comes from the assumption that the image should not change size in resampling voxel spacing from 3 mm to 1 mm voxels.  If an image is 10 voxels across and the voxel spacing (most people would say the voxel “size”) is 3 mm, then many people would say that the image is 30 mm across.  However, under <a class="mention" href="/u/lassoan">@lassoan</a> 's interpretation, it is only 27 mm across (the distance between the first voxel point and the last voxel point).  If we resample to 1 mm voxel spacing, <a class="mention" href="/u/lassoan">@lassoan</a> is saying that the resulting resampled image would still be 27 mm across, and would now have 28 samples in this dimension, rather than 10 samples in the original.  This would involve no extrapolation, only interpolation.   But 28 voxels which are 1 mm across would mean the image “size” in this dimension is now 28 mm rather than the original 30 mm. I think this would be a highly unexpected and unintuitive result for many people (“why should the image size, voxel size x number of voxels, change when resampling from 3mm to 1mm spacing, which divides perfectly?”).   If the origin was not moved, and the dimension of the image was maintained at 30 mm, that would require the additional extrapolated voxels which <a class="mention" href="/u/sebquetin">@sebquetin</a> drew in.</p>
<p>I am not arguing that one of these models is “right”.  I am trying to help clarify what I see as two different ways of looking at this and say that each interpretation leads to what seems like an unintuitive and undesirable characteristic under the other interpretation:</p>
<ul>
<li>Under the voxels-are-point-samples-of-a-continuous-field interpretation, resampling naturally leads to what looks like a change in image size under the other interpretation (“why don’t the image edges line up after resampling?”)</li>
<li>Under the voxels-are-volumetric-samples-summarized-by-one-number interpretation, it seems clearly necessary to move the image origin if we want to change the voxel size and want to keep the image edges in the same place.  Filling in the voxel values around the edge in this case does not feel like extrapolation, because we consider that these are regions we sampled from when gathering the original data. Yes, we do not have finer-grained data to allow distinguishing from the big voxel value, and we do not have a neighboring voxel to interpolate between, but it doesn’t feel like it is extrapolating to just say that the voxel value there is best approximated by the original big voxel value. So, around the edge we are doing nearest neighbor interpolation. Under the other interpretation, this origin-shifting seems entirely unnecessary, and the voxel values around the edge feel like non-intuitive extrapolation (“why extrapolate outside the data, but only for a defined little distance?”).</li>
</ul>

---

## Post #14 by @sebquetin (2024-11-15 02:30 UTC)

<p>Thank you <a class="mention" href="/u/mikebind">@mikebind</a> for clarifying the two different point of views.</p>
<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="40157">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>No, you don’t have extrapolation elsewhere if you don’t shift the origin. The dashed region in the second image of your post above is not part of the output image.</p>
</blockquote>
</aside>
<p>I don’t understand how the dashed region would not be part of the output image. Could you please clarify?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/668feeaa41b7ab48f7d477c00d87e0cf97b5009f.png" data-download-href="/uploads/short-url/eDj4Gad6yJ2xzzJv1beyK1sOCTB.png?dl=1" title="slicer_forum" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/668feeaa41b7ab48f7d477c00d87e0cf97b5009f_2_690x146.png" alt="slicer_forum" data-base62-sha1="eDj4Gad6yJ2xzzJv1beyK1sOCTB" width="690" height="146" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/668feeaa41b7ab48f7d477c00d87e0cf97b5009f_2_690x146.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/668feeaa41b7ab48f7d477c00d87e0cf97b5009f_2_1035x219.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/668feeaa41b7ab48f7d477c00d87e0cf97b5009f_2_1380x292.png 2x" data-dominant-color="381F32"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_forum</span><span class="informations">1409×299 58.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I followed the process mentioned in my original post and I am showing some metadata of the two volumes. Please see the above screenshot which shows that the extent/“size” of the volume is the same before and after resampling.</p>

---

## Post #15 by @lassoan (2024-11-15 05:56 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="13" data-topic="40157">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>There are different, equally valid, metaphors for what the voxel values of an image might represent</p>
</blockquote>
</aside>
<p>While there can be many metaphors that can approximately explain what a pixel may represent, they are not equally valid. Only the “voxels-are-point-samples-of-a-continuous-field” is valid, it is the one that is universally used in digital image processing. For more formal description and detailed explanation, you can read the first 4 chapters of the classic <a href="https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Digital_Image_Processing%2C_4th%20Edition-Rafael%20Gonzalez.pdf">Digital Image Processing textbook by Gonzalez &amp; Woods</a>.</p>
<p>Of course, you can fill up a matrix with any values you like and call it an image, but then you have to accept that many image processing methods may work slightly incorrectly on your data. For example, you can compute a thick slab reconstruction with mean blending mode and say that in this image “voxels-are-volumetric-samples-summarized-by-one-number”. However, all image processing algorithms still assume that “voxels-are-point-samples-of-a-continuous-field interpretation”, so they will just slightly misinterpret your data and may produce somewhat inaccurate results.</p>
<aside class="quote no-group" data-username="mikebind" data-post="13" data-topic="40157">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>On the other hand, if you imagine a CCD sensor (like on a digital camera), the voxel value represents something more like an integration of a signal over an area.</p>
</blockquote>
</aside>
<p>While each CCD sensor element integrates inputs in a certain neighborhood, the output image voxels usually still contain discrete point sample values (and not average in the neighborhood). The point samples are estimated by applying deblurring and denoising algorithms on the raw signal data.</p>
<aside class="quote no-group quote-modified" data-username="sebquetin" data-post="14" data-topic="40157">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sebquetin/48/78510_2.png" class="avatar"> sebquetin:</div>
<blockquote>
<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="40157">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>No, you don’t have extrapolation elsewhere if you don’t shift the origin. The dashed region in the second image of your post above is not part of the output image.</p>
</blockquote>
</aside>
<p>I don’t understand how the dashed region would not be part of the output image. Could you please clarify?</p>
</blockquote>
</aside>
<p>If you want to avoid extrapolation then only those voxels can be part of the output image, which have their center inside the bounding box of the original image voxel centers.</p>

---
