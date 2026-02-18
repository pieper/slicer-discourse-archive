# Is it possible to combine Label Maps and Images into a single file?

**Topic ID**: 5680
**Date**: 2019-02-07
**URL**: https://discourse.slicer.org/t/is-it-possible-to-combine-label-maps-and-images-into-a-single-file/5680

---

## Post #1 by @Kevin.Kn (2019-02-07 14:41 UTC)

<p>Currently I have pairs of .nii images and labelmaps, which I would like to combine into single files where the label map overlaps with the image.</p>
<p>Is there a way to do this that doesn’t mess with the spatial dimensions of the image and labelmap? I know that you can create larger volumes and save multiple images to that volume as long as they fit the dimensions, but doing that stacks the images on top of each other.</p>

---

## Post #2 by @cpinter (2019-02-07 14:50 UTC)

<p>You can mask out parts of your images with the labelmaps like this:</p>
<ol>
<li>Make sure that the SegmentEditorExtraEffects extension is installed</li>
<li>Import the labelmap into a segmentation (right-click labelmap in Data module and choose “Convert labelmap to segmentation node”</li>
<li>Go to Segment Editor</li>
<li>Select the new segmentation, and your image as master volume</li>
<li>Use Mask volume effect</li>
</ol>
<p>I don’t quite understand your comment on stacks of images. How different are the geometries of the images and labelmaps?</p>

---
