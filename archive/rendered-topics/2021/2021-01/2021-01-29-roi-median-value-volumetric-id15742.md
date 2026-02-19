---
topic_id: 15742
title: "Roi Median Value Volumetric"
date: 2021-01-29
url: https://discourse.slicer.org/t/15742
---

# ROI Median Value Volumetric

**Topic ID**: 15742
**Date**: 2021-01-29
**URL**: https://discourse.slicer.org/t/roi-median-value-volumetric/15742

---

## Post #1 by @SmHoop (2021-01-29 22:46 UTC)

<p>Hi,</p>
<p>Is there a feature that allows an ROI selection that will inform of basic metrics in the ROI such as median, mean, etc? I would like to select a cylinder through a volume and have the data of every slice available (eg median value in the ROI in every slice) possibly exported as a .csv.</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2021-01-29 23:01 UTC)

<p>Without coding, you can do this by making a segmentation and then using the SegmentStatistics module.</p>

---

## Post #3 by @SmHoop (2021-01-29 23:14 UTC)

<p>Thanks for the reply. So I tried that earlier, but I’m only seeing metrics for the entire volume (this is like a 15 cm long cylinder at this point). Is there any way to show the slice by slice data or is this a slice by slice process if I wanted to do it this way?</p>

---

## Post #4 by @lassoan (2021-01-29 23:31 UTC)

<p>To compute slice-by-slice metrics, probably the simplest is to blank out areas outside the segment using Mask volume effect (provided by SegmentEditorExtraEffects extension) and then iterate through the slices using numpy (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_axial_slice_as_numpy_array">example</a>).</p>

---

## Post #5 by @SmHoop (2021-02-01 16:42 UTC)

<p>This looks very promising! I have not used any python functionality with Slicer before. With the segment created (I made a cylinder with the SegmentEditorExtraEffects and then masked out the outside of the rest so I’m left with a 1cm cylinder of segment), do I start typing in the python code into the Python Interactor Window in the Slicer application or is there a way to save this segment as data somewhere and then use Python in a separate interface? This is my first experience with anything like this, I appreciate all the help!</p>

---

## Post #6 by @lassoan (2021-02-01 16:45 UTC)

<p>You can either use the built-in Python console (copy-paste code between a text editor and the console) or use a <a href="https://github.com/Slicer/SlicerJupyter">Slicer Jupyter notebook</a>. If you need to run the code often with a convenient user interface then you can put it into a scripted module (see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">tutorials</a>).</p>

---

## Post #7 by @SmHoop (2021-02-01 18:26 UTC)

<p>With my masked data, I now have an image of 0s everywhere except a cylinder of values. I’m not sure I’m following the documentation correctly. I am trying to follow the example code below</p>
<p>import SampleData<br>
volumeNode = SampleData.SampleDataLogic().downloadMRHead()<br>
sliceIndex = 12</p>
<p>voxels = slicer.util.arrayFromVolume(volumeNode)  # Get volume as numpy array<br>
slice = voxels[sliceIndex:,:]  # Get one slice of the volume as numpy array</p>
<p>My segment is called “LF_H04_1mm_Permuted masked” in Slicer. It appears that this is already a volume but maybe I’m missing something?</p>

---

## Post #8 by @SmHoop (2021-02-01 20:25 UTC)

<p>edit: I am able to export my transformed image (hardened), and masked as an .nrrd and just read into python/matlab. However it is not saving the rotations and transforms I had used to make the segment/mask even with a harden on the transform.</p>

---

## Post #9 by @lassoan (2021-02-01 20:27 UTC)

<p>Sorry, I don’t understand what you mean. Maybe you can add a few screenshots to illustrate the question.</p>

---

## Post #10 by @SmHoop (2021-02-01 20:40 UTC)

<p>Sure sorry about that.</p>
<p>Here is the initial imported NRRD recon (Apparently I accidentally saved the rotation I made permanent to the file? Normally had to rotate this image to make it look this way):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fccb4efcc9e70c81fd4d8f80f91d4b2fec37075.jpeg" data-download-href="/uploads/short-url/bnWiKwXtv4tl2EZ8JRM9c3xMSAR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fccb4efcc9e70c81fd4d8f80f91d4b2fec37075_2_690x388.jpeg" alt="image" data-base62-sha1="bnWiKwXtv4tl2EZ8JRM9c3xMSAR" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fccb4efcc9e70c81fd4d8f80f91d4b2fec37075_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fccb4efcc9e70c81fd4d8f80f91d4b2fec37075_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fccb4efcc9e70c81fd4d8f80f91d4b2fec37075_2_1380x776.jpeg 2x" data-dominant-color="9A9AA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 226 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is the segment tube:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6b9f7d19cb00feaacccb1d349c01bda836304df.jpeg" data-download-href="/uploads/short-url/zcDTkts4jekx076RmxPRcXJDdkr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6b9f7d19cb00feaacccb1d349c01bda836304df_2_690x388.jpeg" alt="image" data-base62-sha1="zcDTkts4jekx076RmxPRcXJDdkr" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6b9f7d19cb00feaacccb1d349c01bda836304df_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6b9f7d19cb00feaacccb1d349c01bda836304df_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6b9f7d19cb00feaacccb1d349c01bda836304df_2_1380x776.jpeg 2x" data-dominant-color="9899A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 298 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is the masked segment (all outside vals = 0):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63bbc8081408382662caf3b7e8cc5113458b1fe6.png" data-download-href="/uploads/short-url/eehAxjmfdt03YcYILxZgvhj6Yui.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63bbc8081408382662caf3b7e8cc5113458b1fe6_2_690x387.png" alt="image" data-base62-sha1="eehAxjmfdt03YcYILxZgvhj6Yui" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63bbc8081408382662caf3b7e8cc5113458b1fe6_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63bbc8081408382662caf3b7e8cc5113458b1fe6_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63bbc8081408382662caf3b7e8cc5113458b1fe6_2_1380x774.png 2x" data-dominant-color="68696E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1079 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>At this point I save the masked segment nrrd and open in Matlab, but as you can see the image is rotated differently than expected:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/236c9c183ab3f2bb9203f1f44e8f760ce4d65f4c.png" data-download-href="/uploads/short-url/53npdCOK8CEUJqc6KHNecQ6njk0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/236c9c183ab3f2bb9203f1f44e8f760ce4d65f4c.png" alt="image" data-base62-sha1="53npdCOK8CEUJqc6KHNecQ6njk0" width="558" height="500" data-dominant-color="7D7D7D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">565×506 10.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @lassoan (2021-02-01 20:42 UTC)

<p>Transform hardening on images is only performed by resampling if it is necessary (e.g., when applying non-linear transform), because resampling the image data is a lossy operation. Linear transforms are applied by changing the image geometry (image origin, spacing, and axis directions), without touching the voxel data, this preserving all information. If you want to resample the image data along axes defined by a transform then you can use one of the image resampling filters.</p>

---

## Post #12 by @SmHoop (2021-02-01 20:48 UTC)

<p>So rather than saving the Nrrd right after the masking step, I should resample the data so it is aligned the same way as I see in the windows? I’m not sure I see why the initial image is oriented such yet when saved and reopened in Matlab it is rotated back to it’s “original” position?</p>

---

## Post #13 by @lassoan (2021-02-01 20:59 UTC)

<p>Yes, if you want to have the image axis directions to be aligned with a particular physical axis directions then you need to resample the image.</p>
<p>You can create a volume with the desired axis directions (see example <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_new_volume">here</a>) and use that as reference volume in “Resample scalar/vector/dwi volume” module.</p>
<p>However, it is probably even simpler to start everything with segmenting the jar. You can then get oriented bounding box of the jar fully automatically from Segment Statistics module. Example script to get the bounding box as ROI node is <a href="https://discourse.slicer.org/t/new-segment-statistics-oriented-bounding-box-diameter-and-more/10203">here</a>. If you set this ROI as input to Crop volume module then you get a cropped, resampled volume that has its axes aligned with the axes of the jar.</p>

---

## Post #14 by @SmHoop (2021-02-01 21:08 UTC)

<p>Okay I will give this a shot, thank you!</p>

---

## Post #15 by @SmHoop (2021-02-02 15:49 UTC)

<p>The second suggestion worked beautifully, thank you!</p>

---
