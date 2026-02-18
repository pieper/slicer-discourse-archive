# Cannot edit outside a segmentation bounding box

**Topic ID**: 2451
**Date**: 2018-03-28
**URL**: https://discourse.slicer.org/t/cannot-edit-outside-a-segmentation-bounding-box/2451

---

## Post #1 by @bobread (2018-03-28 10:23 UTC)

<p>Hi, I have a segmentation which I am trying to edit but when I try to add or delete points outside of a bounding box nothing happens. I imported the segmentation from a label map and the bounding box encloses the non-background voxels. Does anyone have any ideas what I may be doing wrong or suggest a fix?</p>

---

## Post #2 by @lassoan (2018-03-28 11:06 UTC)

<p>You can use Crop volume module to reduce or expand the volume extent before you start segmentation. You may need to enable resampling for allowing expansion. If spacing of the volume is high anisotropic (not the same along all axes) then you can enable isotropic spacing option to increase segmentation quality.</p>

---

## Post #3 by @bobread (2018-03-28 16:13 UTC)

<p>I tried resampling and the crop volume module. I had no luck. I also tried exporting the segmentation to a labelmap and then reimporting it as a segmentation but that didn’t work either. I did get an warning when I first imported the DICOM data. I don’t know if this is relevant…</p>
<p>Warning in DICOM plugin Scalar Volume when examining loadable 13: Whole Body  1.0 Body Std. Volume Portal_Ven/Phase Whole Body CE for contentTime of 092548.000349: There is no pixel data attribute for the DICOM objects, but they might be readable as secondary capture images.  Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.</p>

---

## Post #4 by @lassoan (2018-03-28 20:18 UTC)

<aside class="quote no-group" data-username="bobread" data-post="3" data-topic="2451">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/8797f3/48.png" class="avatar"> bobread:</div>
<blockquote>
<p>I tried resampling and the crop volume module. I had no luck.</p>
</blockquote>
</aside>
<p>What do you mean by no luck? What did you do? What did you expect to happen? What happened instead? Can you attach a screenshot of the Crop volume module panel?</p>

---

## Post #5 by @bobread (2018-03-29 12:26 UTC)

<p>Sorry to be so vague! I think I need to go through this step by step. I’ve attached a screen shot of the initial problem where I have tried to paint pixels in the Segment Editor but I cannot do so beyond a bounding box. I have also attached a screenshot of the Volume Information which shows that the image spacing is different along the z-axis. Should my next step be to use the Resample Scalar Volume module or the Crop Volume module. I tried both ways round yesterday but neither of them resulted in me being able to edit outside of the bounding box.<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e85410293e2c1d85f11af7b4d549294a8836e1a.jpeg" alt="Slicer2" data-base62-sha1="fLI13odXG2UKLwcwgYm4aPNvGOu" width="677" height="460"><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d89c7d9054ea991d1c443c04a4358a5820a7439e.jpeg" data-download-href="/uploads/short-url/uUepBjcxGA6B8EXkEDscksHfAqa.jpg?dl=1" title="Slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d89c7d9054ea991d1c443c04a4358a5820a7439e_2_690x398.jpg" alt="Slicer" data-base62-sha1="uUepBjcxGA6B8EXkEDscksHfAqa" width="690" height="398" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d89c7d9054ea991d1c443c04a4358a5820a7439e_2_690x398.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d89c7d9054ea991d1c443c04a4358a5820a7439e_2_1035x597.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d89c7d9054ea991d1c443c04a4358a5820a7439e_2_1380x796.jpg 2x" data-dominant-color="908B8F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer</span><span class="informations">1685×974 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2018-03-29 13:05 UTC)

<p>Thanks for the additional information. You don’t need to use “Resample Scalar Volume” module, as “Crop volume” module has both cropping and resampling built in. Image spacing is almost isotropic (0.554 and 0.8 is not a huge difference), so you may get away without enabling isotropic option, in Crop volume. To expand the volume, create a ROI box and set it to the desired size, make sure “Interpolated cropping” option is enabled, and click Apply. Then, create a new segmentation, select the cropped (expanded) volume as master volume, and it should work. Changing master volume for an existing segmentation does not change the segmentation geometry, so you must create a new segmentation node.</p>

---

## Post #7 by @bobread (2018-04-03 10:05 UTC)

<p>Many, many thanks for your help. I managed to create a new cropped volume. I then created a new segmentation using this new cropped volume in the segment editor. This resulted in an empty segmentation so I used the data module to drag my existing segments from the old segmentation into the new one and that did the trick.</p>

---

## Post #8 by @Vincent_C (2020-07-16 03:33 UTC)

<p><a class="mention" href="/u/bobread">@bobread</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Hi guys,</p>
<p>I’m facing a similar problem where I am unable to edit outside of the segmentation bounding box. But instead of “importing the segmentation from a label map” as <a class="mention" href="/u/bobread">@bobread</a> did, I am converting a labelmap node to a segmentation node using the Data module which also results in a segmentation that has a bounding box in which I cannot edit outside of. The solution I tried is to go to the Segment Editor module with the following steps:</p>
<ol>
<li>Click on -&gt; Segmentations…</li>
<li>Go to Export/import models and labelmaps</li>
<li>Select Operation to be Import</li>
<li>Select Input type to be Labelmap</li>
<li>Select Input node to be the specific labelmap node</li>
<li>In Advanced, the settings are defaulted as Export segments: all and Reference volume: (some scalar volume node)</li>
<li>Then click Import.</li>
</ol>
<p>This creates a new segmentation node whose editable area is not limited by a bounding box. Is this a valid solution to editing outside the segmentation bounding box issue?</p>
<p>Thanks</p>

---

## Post #9 by @lassoan (2020-07-16 03:48 UTC)

<p>This solution is fine, but it is simpler to change the segmentation’s extent by clicking on the button next to the master volume’s selector and choose a node that has the extent you need. You can find some more information here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#panels-and-their-use">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#panels-and-their-use</a></p>

---
