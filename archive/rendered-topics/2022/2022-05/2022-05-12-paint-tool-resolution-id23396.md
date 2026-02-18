# Paint tool resolution

**Topic ID**: 23396
**Date**: 2022-05-12
**URL**: https://discourse.slicer.org/t/paint-tool-resolution/23396

---

## Post #1 by @BoneArtist (2022-05-12 21:08 UTC)

<p>Is there a way to increase the resolution of the paint tool or some other method of getting a finer stepped pattern, as seen in the red line. I come from an illustration background and understand the smoothing that happens - like a subdivision with a 3D mesh in Blender - but my artist side wants a finer line <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I tried volume cropping but didn’t see that much difference, perhaps because I didn’t have much extra to crop.<br>
Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e21297ba9d334f9b9336074084a3f1235c517970.jpeg" data-download-href="/uploads/short-url/wfVK40E95rW7Jq7wsM9hX4X3jAk.jpeg?dl=1" title="Slicer Resolution" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e21297ba9d334f9b9336074084a3f1235c517970_2_690x406.jpeg" alt="Slicer Resolution" data-base62-sha1="wfVK40E95rW7Jq7wsM9hX4X3jAk" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e21297ba9d334f9b9336074084a3f1235c517970_2_690x406.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e21297ba9d334f9b9336074084a3f1235c517970_2_1035x609.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e21297ba9d334f9b9336074084a3f1235c517970_2_1380x812.jpeg 2x" data-dominant-color="BAC1B9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer Resolution</span><span class="informations">1713×1008 232 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-05-12 22:03 UTC)

<p>What you are seeing is the binary labelmap representation, where one value is assigned, by default, to each voxel in the master volume.</p>
<p>A couple suggestions:</p>
<p>You can change the "Representation in 2D views to be Closed surface and this will show you the smoothed result as you paint.  Be aware it will take a bit longer to update, so you may use this for a while to learn what your label map will look like when smoothed and then switch back to label map display.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dcd20c3585b2b79c3355565ed33ff8ebfc3c4c8c.png" data-download-href="/uploads/short-url/vvt4fHX1Z7YDg1dGm5gdVEfGfko.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dcd20c3585b2b79c3355565ed33ff8ebfc3c4c8c_2_690x150.png" alt="image" data-base62-sha1="vvt4fHX1Z7YDg1dGm5gdVEfGfko" width="690" height="150" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dcd20c3585b2b79c3355565ed33ff8ebfc3c4c8c_2_690x150.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dcd20c3585b2b79c3355565ed33ff8ebfc3c4c8c_2_1035x225.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dcd20c3585b2b79c3355565ed33ff8ebfc3c4c8c.png 2x" data-dominant-color="4E4E4F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1144×250 33.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Second, if you still feel you want better resolution you can increase the resolution of the labelmap with respect to the reference volume using the Segmentation geometry dialog, accessible with the button to the right of the master volume selector (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#panels-and-their-use">described here</a>).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c0745ace9f8ed6c537da0cd34d4656b63d09782.jpeg" data-download-href="/uploads/short-url/3ZWWSJTAuJyCP4VUrclAH2eJQIi.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c0745ace9f8ed6c537da0cd34d4656b63d09782_2_690x356.jpeg" alt="image" data-base62-sha1="3ZWWSJTAuJyCP4VUrclAH2eJQIi" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c0745ace9f8ed6c537da0cd34d4656b63d09782_2_690x356.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c0745ace9f8ed6c537da0cd34d4656b63d09782_2_1035x534.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c0745ace9f8ed6c537da0cd34d4656b63d09782.jpeg 2x" data-dominant-color="424243"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1300×672 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @mikebind (2022-05-12 22:05 UTC)

<p>By default, segmentation segments are shown in slice views as consisting only of whole voxels, which is how their binary labelmap representations are encoded. Each voxel of the segmentation volume is either part of the segment or not part of the segment.  If this view is too “pixelated” for you, there are two ways to address this: 1) Increase the resolution of the segmentation volume so that the stair steps are smaller, or 2) display a smoothed model representation on slice views instead of the binary label map representation.</p>
<p>There are many other posts in this forum about how to do option 1. Here’s one which might be helpful: <a href="https://discourse.slicer.org/t/how-do-i-set-segmentation-resolution/19068" class="inline-onebox">How do I set segmentation resolution</a></p>
<p>For option 2, if you go to the Segmentations module, you can select to show the smoothed “Closed surface” representation in slice views instead of the “Binary labelmap”.  This will not change your underlying segmentation at all, just the view you are seeing of it.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/676080aa1ca5ecef18e4f924d99b0769005841a0.png" alt="image" data-base62-sha1="eKvVZlvRySIDgHJwRJlaYgcRKEw" width="439" height="433"></p>

---
