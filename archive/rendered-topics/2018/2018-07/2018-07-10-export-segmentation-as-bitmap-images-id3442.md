# Export segmentation as bitmap images

**Topic ID**: 3442
**Date**: 2018-07-10
**URL**: https://discourse.slicer.org/t/export-segmentation-as-bitmap-images/3442

---

## Post #1 by @slojanko (2018-07-10 12:34 UTC)

<p>Hello,</p>
<p>I’m in need of some assistance with exporting one segmentation to a sequence of bitmap (png) images so I can do some calculation on the success of automatic segmentation. Are there any plugins that go through the entire volume and only the segmentation data would be saved to an image, doesn’t really matter which axis, if it’s always the same?</p>
<p>A segmentation such as:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cf9333322bf0f69a0c13ccca4eba58b074be4c8.png" alt="image" data-base62-sha1="hPz77z1LAvLzGlVO8K8oWssUaM0" width="238" height="273"></p>
<p>would be converted into an image:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00f7c4a30e5a7da55608e07455dbe6256d10df50.png" alt="Capture" data-base62-sha1="8yQ7MrFGzKXlaD3uCRSTWcNYM8" width="238" height="273"></p>
<p>Thanks,<br>
Janko</p>

---

## Post #2 by @lassoan (2018-07-10 14:22 UTC)

<aside class="quote no-group" data-username="slojanko" data-post="1" data-topic="3442">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slojanko/48/1518_2.png" class="avatar"> slojanko:</div>
<blockquote>
<p>exporting one segmentation to a sequence of bitmap (png) images so I can do some calculation on the success of automatic segmentation</p>
</blockquote>
</aside>
<p>Saving into consumer file format, such as png is usually a bad idea, as you lose essential information. These file formats don’t support storage of standard metadata fields, such as pixel and slice spacing, cannot store 16-bit images, etc.</p>
<p>What software do you plan to use to compute metrics on? All software environments that I know of can read nrrd and MetaIO images (and usually it is trivial to write a parser, in case it does not exist).</p>
<p>You may also consider using Segment Comparison module (in SlicerRT extension), which can compute Hausdorff distance and Dice coefficient.</p>

---

## Post #3 by @slojanko (2018-07-10 14:46 UTC)

<p>Hey,</p>
<p>I was not aware nrrd is a common format, it seems Matlab has plugins for importing it. I’ll take a look at them.<br>
I have to do a F-measure accuracy test for comparison of automatic segmentation to ground truth.</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2018-07-10 14:52 UTC)

<p>You can find a good NRRD reader/writer in <a href="https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver">source code of Slicer’s MatlabBridge extension</a>: nrrdread.m and nrrdwrite.m (it is a greatly improved version of some readers/writers found on Matlab exchange).</p>
<p>You may also consider running your F-measure accuracy test from Slicer, using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge">MatlabBridge extension</a>.</p>

---

## Post #5 by @pranaysingh (2021-05-08 12:39 UTC)

<p>Hi,</p>
<p>I had a question, I am facing the issue which you just mentioned here:</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="3442">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Saving into consumer file format, such as png is usually a bad idea, as you lose essential information. These file formats don’t support storage of standard metadata fields, such as pixel and slice spacing, cannot store 16-bit images, etc.</p>
</blockquote>
</aside>
<p>I want to save the slices on which I have done segmentation, for further image processing operations. But the png image is saved as 8 bit(uint8) image while my original dicom images were uint16 type. Is there a way I can save export it from 3D slicer in orginal quality ?</p>
<p>Any guidance would be lot helpful.</p>
<p>Regards,<br>
Pranay</p>

---

## Post #6 by @lassoan (2021-05-09 15:20 UTC)

<p>You can get a volume node as a numpy array then write it to png slice by slice (see example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rasterize-a-model-and-save-it-to-a-series-of-image-files">here</a>), but this should not be necessary, because your deep learning network can use numpy arrays as inputs.</p>

---
