# Converting Segmentation to Volume automatically w/ Python or Matlab

**Topic ID**: 16829
**Date**: 2021-03-29
**URL**: https://discourse.slicer.org/t/converting-segmentation-to-volume-automatically-w-python-or-matlab/16829

---

## Post #1 by @Hball99 (2021-03-29 19:54 UTC)

<p>Hello there! I have 200+ CT-Volumes with matching segmentations. The Volumes are in .nrrd format and the segmentations are in seg.nrrd format. I need both of those as .nii.gz format and I want to script the conversion from one into the other format.</p>
<p>Regarding the Volumes, everything has been quite easy, using sitk:</p>
<p>import SimpleITK as sitk</p>
<p>img = sitk.ReadImage(“your_image.nrrd”)<br>
sitk.WriteImage(img, “your_image.nii.gz”)</p>
<p>I just did the same thing with the segmenations, too, which worked fine at first glance. But the problem is now that the segmentations are not registered with the Volumes anymore. The image dimensions as well as image origins are not the same anymore and thus, I cannot process the converted images.</p>
<p>The same happens, when I do the following steps manually: 1. Load the .seg.nrrd files into Slicer as Segementation 2. Save the segmentation as .nrrd file instead of seg.nrrd 3. Import the .nrrd file as Volume and save the segmentation as .nii.gz</p>
<p>But I figured out a way to convert the data types manually while keeping all dimensions: 1. Import the Volume as well as the corresponding segmentation (.seg.nrrd) 2. Export the segmentation to a labelmap with reference volume set to my corresponding volume  3. Save the Labelmap as nii.gz (4. Not sure if I need that step for my project: Convert Labelmap to Scalar Volume and safe as nii.gz)</p>
<p>In both cases 3. and 4. I have a nii.gz file with matching dimensions. But since I have 200+ Volumes, I need to script that. But I haven’t found anything so far. Do you have any ideas? Thanks!</p>

---

## Post #2 by @lassoan (2021-04-03 02:50 UTC)

<p>You can load the segmentation and export to volume file. If you want the segmentation to have a particular geometry (origin, spacing, axis directions, and extents) then specify the CT volume as reference volume when you export to volume file (when you call <code>ExportSegmentsBinaryLabelmapRepresentationToFiles</code>).</p>
<p>See complete example here:</p>
<aside class="quote quote-modified" data-post="13" data-topic="15773">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/3ab097/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/overlapping-segmentions-export-to-nifti/15773/13">Overlapping Segmentions Export to NIFTI</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Great idea, working perfectly now. Thanks so much for your extensive help. In case anyone else wants to do something similar, here is my final code: 
# ***** THE FINAL SCRIPT *****

# Required to have 3 segments - "Mask", "Single", "Multi"

# Save Image data as Image Data.nii.gz

node = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')
file_path = "/Users/pete/OneDrive/ImageData.nii.gz"
properties = {'useCompression': 1}; #use compression
slicer.util.saveNode(node, file_path, prope…
  </blockquote>
</aside>


---
