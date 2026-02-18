# How to properly use the segment editor with transformed volumes

**Topic ID**: 21861
**Date**: 2022-02-08
**URL**: https://discourse.slicer.org/t/how-to-properly-use-the-segment-editor-with-transformed-volumes/21861

---

## Post #1 by @muratmaga (2022-02-08 23:08 UTC)

<p>A colleague gave me a volume which she aligned in a particular orientation she want the data to be collected. This a linear transform and it is hardened.</p>
<p>When I open this volume in Segment Editor, there is the little warning about “Slice views are not aligned with segmentation and warns me that striping artifact may appear”.</p>
<p>As it happens I want to paint a single slice in this orientation and export this slice. And when I do this and yes, stripping effects do appear in slice above and below. I can align the slice views with respect to the segmentation, and the stripping effects disappear, but then I am not in the orientation i want to be in to extract the data.</p>
<p>I find this behavior confusing and it is a common complaint among our users (samples are often scanned in random orientations and one of the common things they do is to reorient the sample in approximate anatomical planes before doing segmentation).</p>
<p>Why can’t we rotate the segmentation to the slice view as opposed to doing the other way around? It defeats the purpose of aligning the volume in the first place.</p>

---

## Post #2 by @pieper (2022-02-09 00:06 UTC)

<p>If you want to segment a single slice in an orientation that is not aligned with the acquisition you need to resample the volume, not just harden it.  We could probably make this easier to do, but normally you want to segment a 3D region so this isn’t really an issue most of the time.</p>

---

## Post #3 by @muratmaga (2022-02-09 04:42 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="21861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>We could probably make this easier to do, but normally you want to segment a 3D region so this isn’t really an issue most of the time</p>
</blockquote>
</aside>
<p>Even in 3D it is an issue, because it confuses users. Where it rotates the slices back to segmentation orientation, would it be possible to give user the resampling the volume option too?</p>

---

## Post #4 by @jamesobutler (2022-02-09 14:05 UTC)

<p>Since some users will want to segment in a reformat/reslice slice view, I think the improvement here will be needing to improve the understanding between reslicing and resampling.</p>
<p>Reslicing to align to the anatomical plane is not resampling. Therefore that should be a first step of the user prior to segmenting for the voxels to be aligned in this new direction. Then they can utilize effects like “Fill between slices” as painting won’t be across slices which would prevent this in the non resampled case. When resampling the user is going to have to be mindful of whether they save this new volume as an additional volume, overwrite the original, or don’t save it and only get the statistics out of the segmentation.</p>

---

## Post #5 by @pieper (2022-02-09 15:28 UTC)

<p>It could make sense to add an option to the Segmentation Geometry dialog to resample so that the image grid aligns with the current orientation directions of the volume.  Or there could be a module that makes it simple to resample acquisitions to anatomical space (e.g. click on the nose, center of head, and one ear) if people have resolution to spare and prefer better painting over preserving resolution.</p>

---

## Post #6 by @muratmaga (2022-02-09 16:16 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="21861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>resample the volume, not just harden it</p>
</blockquote>
</aside>
<p>This is also one of the issues: <strong>Harden</strong> does two different things depending on the transform. It actually resamples the volume when you choose a non-linear transform, but it only modifies the directional matrix, if it is a linear transform. THe point is, it is not clear to the user the which action it is going to happen by choosing “harden transform”, if they do not know this difference.</p>
<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="21861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>It could make sense to add an option to the Segmentation Geometry dialog to resample so that the image grid aligns with the current orientation directions of the volume.</p>
</blockquote>
</aside>
<p>We can try to work on this, with some guidance from you or <a class="mention" href="/u/lassoan">@lassoan</a>. However, I still think as opposed to doing a patch to the segment editor, I think the language and functionality around the transforms and hardening can be improved to make the communication better.</p>
<p>Another typical complaint is that <strong>hardened</strong> volumes do not show up as in the orientation the user thought they saved in programs like ImageJ, which does not read the directional matrix in the header.</p>

---

## Post #7 by @lassoan (2022-02-09 20:17 UTC)

<p>I think the root cause of the issue is that segmentation on oblique slices of a binary labelmap looks simple, and users don’t realize just how complex this problem is.</p>
<p>One possible solution is to educate users about complex things. That’s why I’ve added <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/">this page</a>, which explains why this is hard and two possible solutions. Do your users know about this page? Does it solve their problem of segmentation on oblique slices?</p>
<p>Another potential improvement could be to make it easier to align the ROI markup with slices. Currently, when an ROI is placed on a 2D slice, its axes are aligned with the world coordinate system axes by default (and so the user needs to enable rotation interaction and then align the ROI manually). Instead of this, we could align the ROI axes with the slice axes by default (similarly to how it is done for plane markups). This way, the steps for resampling the volume would be:</p>
<ul>
<li>draw a new ROI on a slice view</li>
<li>click specify geometry button in segment editor</li>
<li>select the ROI</li>
<li>click OK</li>
</ul>
<p>This takes about 6-8 mouse clicks, but since this resampling permanently damages the image, it should not be performed frequently anyway. Would this help?</p>
<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="21861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Another typical complaint is that <strong>hardened</strong> volumes do not show up as in the orientation the user thought they saved in programs like ImageJ, which does not read the directional matrix in the header.</p>
</blockquote>
</aside>
<p>We cannot fix 2D imaging software, such as ImageJ. They have other problems to worry about, such as dealing with extremely large images, so probably they just don’t want the complexity of arbitrarily positioned and oriented 3D images.</p>
<p>Users need to accept that ImageJ, Adobe PhotoShop (that some people use for DICOM segmentation), etc. are just not suitable for 3D imaging and they should not trust these software when they work with 3D images.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="21861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p><strong>Harden</strong> does two different things depending on the transform. It actually resamples the volume when you choose a non-linear transform, but it only modifies the directional matrix, if it is a linear transform. THe point is, it is not clear to the user the which action it is going to happen by choosing “harden transform”, if they do not know this difference.</p>
</blockquote>
</aside>
<p>Harden does one thing: permanently applies a transform to the node. The process to achieve this is chosen automatically and non-technical users don’t need to know the difference: the application handles this transparently for them. If they open the resulting image in ImageJ then they can see unexpected results - as for any other 3D data sets. If the user rotated the image so that oblique slices can be edited then that was a mistake: the image position or orientation should never be corrupted just to allow editing in oblique slices, but instead the slice views should be rotated.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="21861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I think the language and functionality around the transforms and hardening can be improved to make the communication better.</p>
</blockquote>
</aside>
<p>I don’t really like the “harden” term, but at least it is unique enough that there are no misunderstandings it you can easily google search for its meaning in Slicer. In Blender it is called just “<a href="https://docs.blender.org/manual/en/2.79/editors/3dview/object/editing/transform/clear_apply.html">apply</a>” which is just too generic. Similar words for persistently applying some modifications are “burn in” for annotations, “bake” for textures, but none of these seem significantly better than “harden”.</p>
<p>Any suggestions for improving wording in documentation or user interface are very welcome.</p>

---

## Post #8 by @muratmaga (2022-02-09 21:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="21861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>One possible solution is to educate users about complex things. That’s why I’ve added <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/">this page</a>, which explains why this is hard and two possible solutions. Do your users know about this page? Does it solve their problem of segmentation on oblique slices?</p>
</blockquote>
</aside>
<p>This page does a good job of explaining the complexity of why the way the Slicer works the way it works, but does not necessarily help them very much. Here is what I get following the suggestion of resampling via CropVolume:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a556dea3f6429f1c4a42a93b69293e510cbb502.jpeg" data-download-href="/uploads/short-url/hsdhxDIhIrheDYWbMXflc5oXgtQ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a556dea3f6429f1c4a42a93b69293e510cbb502_2_494x500.jpeg" alt="image" data-base62-sha1="hsdhxDIhIrheDYWbMXflc5oXgtQ" width="494" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a556dea3f6429f1c4a42a93b69293e510cbb502_2_494x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a556dea3f6429f1c4a42a93b69293e510cbb502_2_741x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a556dea3f6429f1c4a42a93b69293e510cbb502_2_988x1000.jpeg 2x" data-dominant-color="807179"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1259×1272 95.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is confusing because, the only way I can see my newly resampled volume in the rotated orientation is when I choose the “reformat” axis. If I click on the sagittal, it goes back to the untransformed orientation. What I am going to do when I wanted to see the new volume what I think is the axial plane? Click axial, and expand the dialog box and click rotate volume to plane? This is too much in my opinion. Not only this is still confusing, it doesn’t resolve the issue of exported volume will still not be read in the anticipated direction in ImageJ or others, even though the user thinks they resampled the volume (It just looks like noisy volume).</p>
<p>I understand why you guys are doing this, Slicer is a predominantly for medical imaging, and you don’t want to mess with the acquired data randomly. But that’s not common for our datasets (again it is very common for scans to be in totally random orientation). So what we need is a tool (as part of SlicerMorph, not in core Slicer) to resample the volume with the warning to the user that this will potentially degrade their volume, particularly if they keep doing it (transform -&gt;resample, then further transform and resample). But it is a need.</p>

---

## Post #9 by @pieper (2022-02-09 21:08 UTC)

<p>It’s true that bad metadata about patient orientation is rare in most medical imaging (MR, CT…), but not all (US).  I think having some easy ways to define and resample the data along standard reference planes makes sense.  It could start in SlicerMorph and migrate to the core if generally useful.</p>

---

## Post #10 by @lassoan (2022-02-09 22:38 UTC)

<p>Crop volume module does something very similar to what is needed. Of course a dedicated Python module wrapped over it could simplify the GUI and workflow.</p>
<p>I think the only missing feature is assigning image axes to arbitrary RAS axes. Current modules strive to preserve the original image position and orientation (because once they are lost, they cannot be recovered), but if the scan contains a bucket of specimens in random orientation then it is safe to discard the original orientation. There is an “Orient Scalar Volume” module that reorders the voxels, which is useful, but it still preserves the original axis directions and the GUI is very user-unfriendly. The small Python module could take care of these, too (discard the original orientation and show immediate preview of the new image orientation).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="8" data-topic="21861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Click axial, and expand the dialog box and click rotate volume to plane? This is too much in my opinion.</p>
</blockquote>
</aside>
<p>In recent Slicer versions, if you click the eye icon in data module for a volume then it will take care of all this: it automatically resets the slice views to the default (axial, sagittal, coronal) directions, and then rotates them to the volume axes. Of course, this is only relevant if the goal is to preserve the original image orientation.</p>

---

## Post #11 by @muratmaga (2022-02-10 21:08 UTC)

<p>This is a sample mouse skull in random orientation for test cases:<br>
<a href="https://app.box.com/shared/static/c2cblsqg1bf86vgipt4e9nv4d879e8qc.gz" class="onebox" target="_blank" rel="noopener nofollow ugc">https://app.box.com/shared/static/c2cblsqg1bf86vgipt4e9nv4d879e8qc.gz</a></p>

---

## Post #12 by @lassoan (2022-02-11 15:11 UTC)

<p>Thank you, this sample image was helpful.</p>
<p>A simple workflow can be:</p>
<ul>
<li>Select volume
<ul>
<li>The module switches to four-up view and enables interactive slice intersections</li>
</ul>
</li>
<li>Rotate slice intersections using drag-and-drop to show axial slice in red and coronal slice in green</li>
<li>Click “Align” button
<ul>
<li>The module rotates volume to make the slice planes aligned with anatomical axes. The result is that the volume is oriented correctly in physical space, except there may be flips.</li>
</ul>
</li>
<li>Click Flip LR, Flip AP, or Flip IS button if needed to fix any inverted axis
<ul>
<li>The module “flips” the volume along the chosen direction (actually it rotates by 180 degrees)</li>
</ul>
</li>
<li>Define clipping ROI (optional, if not specified then the entire volume is kept)</li>
<li>Click “Finish” button
<ul>
<li>The module uses Crop volume module to crop and resample the volume</li>
</ul>
</li>
</ul>
<p>Even without the automations, the workflow takes about 1.5 minutes:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="zshSF9FbdZA" data-video-title="Reorienting volume using interactive slice intersections" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=zshSF9FbdZA" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/zshSF9FbdZA/maxresdefault.jpg" title="Reorienting volume using interactive slice intersections" width="" height="">
  </a>
</div>

<p>With the module it should take less than 1 minutes. It could be automated further by asking the user to specify a threshold and generate a segmentation from that, get principal axes, and use that to initialize the slice orientations. The segmentation can be also used for automatic cropping.</p>
<p>These code snippets were used in the video (that would be in the custom scripted module):</p>
<pre><code class="lang-python">def rotateVolumeToSlicePlanes(volumeNode):
    sliceViewNames = ["Yellow", "Green", "Red"]  # sagittal, coronal, axial
    # Rotate slice planes to standard anatomical planes
    roiToWorld = vtk.vtkMatrix4x4()
    for axisIndex, sliceViewName in enumerate(sliceViewNames):
        # Set roiToWorld column to slice normal
        sliceToRas = slicer.app.layoutManager().sliceWidget(sliceViewName).mrmlSliceNode().GetSliceToRAS()
        for component in range(3):
            roiToWorld.SetElement(component, axisIndex, sliceToRas.GetElement(component, 2))
    # Invert matrix
    worldToRoi = vtk.vtkMatrix4x4()
    vtk.vtkMatrix4x4.Invert(roiToWorld, worldToRoi)
    # Apply transform to volume
    volumeNode.ApplyTransformMatrix(worldToRoi)
    slicer.modules.volumes.logic().CenterVolume(volumeNode)
    # Reset view axes to default
    for sliceViewName in sliceViewNames:
        slicer.app.layoutManager().sliceWidget(sliceViewName).mrmlSliceNode().SetOrientationToDefault()
    # Reset field of view in slice views
    slicer.util.setSliceViewerLayers(fit=True)

def flipVolumeOrientation(volumeNode, axis):
    transform = vtk.vtkTransform()
    if axis == 0:
        transform.RotateX(180)
    if axis == 1:
        transform.RotateY(180)
    if axis == 2:
        transform.RotateZ(180)
    volumeNode.ApplyTransform(transform)

volumeNode = getNode('809_1-resample_sample')
rotateVolumeToSlicePlanes(volumeNode)

flipVolumeOrientation(volumeNode, 0)
#flipVolumeOrientation(volumeNode, 1)
#flipVolumeOrientation(volumeNode, 2)
</code></pre>

---

## Post #13 by @jmlevin (2024-05-07 15:54 UTC)

<p>Thank you for your explanations above.</p>
<p>Where can I find the “align” button? I am working through a similar problem where I am trying to re-orient the planes of a CT scan. I am able to re-align using the interaction feature, but cannot then “align” the image to the window.</p>

---

## Post #14 by @lassoan (2024-05-10 13:49 UTC)

<p>I described how a module could be developed for this (and the “align” button would be displayed on that module). I’m not sure if somebody has implemented this module.</p>

---
