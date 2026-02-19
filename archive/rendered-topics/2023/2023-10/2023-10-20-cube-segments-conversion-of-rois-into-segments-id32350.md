---
topic_id: 32350
title: "Cube Segments Conversion Of Rois Into Segments"
date: 2023-10-20
url: https://discourse.slicer.org/t/32350
---

# Cube Segments / Conversion of ROIs into Segments

**Topic ID**: 32350
**Date**: 2023-10-20
**URL**: https://discourse.slicer.org/t/cube-segments-conversion-of-rois-into-segments/32350

---

## Post #1 by @dokay1 (2023-10-20 16:34 UTC)

<p>Dear Slicers,</p>
<p>I have a project where I want to place a number of 2x2x2cm voxels on brain scans to imitate MR Spectroscopy voxel placement. It seems that using ROIs to generate these is the best approach, however, I couldn’t find an efficient way to convert these CUBIC ROIs into Segments/Label maps.</p>
<p>Is there a solution for this?</p>
<p>Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4aaebae710af6ba1245435f9e5768cbdd7b145d2.jpeg" data-download-href="/uploads/short-url/aEFGNw19TeeecZT6XvH1nhRCqd4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4aaebae710af6ba1245435f9e5768cbdd7b145d2_2_690x465.jpeg" alt="image" data-base62-sha1="aEFGNw19TeeecZT6XvH1nhRCqd4" width="690" height="465" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4aaebae710af6ba1245435f9e5768cbdd7b145d2_2_690x465.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4aaebae710af6ba1245435f9e5768cbdd7b145d2_2_1035x697.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4aaebae710af6ba1245435f9e5768cbdd7b145d2_2_1380x930.jpeg 2x" data-dominant-color="3E3E47"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1684×1136 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @dokay1 (2023-10-21 00:40 UTC)

<p>Well, figured it out. You create a template Segment using thresholding 0-to-max (i.e. to select all voxels). Convert the segment to a labelmap. Use this labelmap with Crop Volume module and use the ROI for cropping, and there you go. A labelmap with shaped exactly as the ROI.</p>

---

## Post #3 by @muratmaga (2023-10-21 04:07 UTC)

<p>Flood fill effect in aegment editor extra effects extension takes an ROi.</p>
<p>That may save you a couple steps.</p>

---

## Post #4 by @dokay1 (2023-10-21 12:34 UTC)

<p>Neat! Thank you!</p>
<p>I tested it (see below). It seems like the Flood Fill provides an approximation of the ROI, while Crop will make it match the ROI’s exact dimensions.</p>
<p>Probably the scalable solution will be a python script for Batch Cropping. I’ll share once I made it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/6164202311784ee86c71cecb0be0dd1394039854.jpeg" data-download-href="/uploads/short-url/dTyPCwE44BAd6evAHE8CStQO3ju.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/6164202311784ee86c71cecb0be0dd1394039854_2_690x345.jpeg" alt="image" data-base62-sha1="dTyPCwE44BAd6evAHE8CStQO3ju" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/6164202311784ee86c71cecb0be0dd1394039854_2_690x345.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/6164202311784ee86c71cecb0be0dd1394039854_2_1035x517.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/6164202311784ee86c71cecb0be0dd1394039854_2_1380x690.jpeg 2x" data-dominant-color="5C5955"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2352×1176 209 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you again!</p>

---

## Post #5 by @muratmaga (2023-10-21 20:10 UTC)

<p>To me, they align quite well. The extra space outside of the ROI is due your spacing. Segmentation has to follow the voxel boundaries.</p>
<p>If you want to ROI boundary and the segmentation to align more precisely, you can increase the resolution of the segmentation (but of course that will also increase the memory consumption).</p>
<p>(purple is output of flood will, red box is the ROI).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43e5bef2e202eb3ce9c21c1c74fbb7f3e2687b76.jpeg" data-download-href="/uploads/short-url/9GEdzaB6u2m8POn2pVfmmdkV3p4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43e5bef2e202eb3ce9c21c1c74fbb7f3e2687b76_2_690x274.jpeg" alt="image" data-base62-sha1="9GEdzaB6u2m8POn2pVfmmdkV3p4" width="690" height="274" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43e5bef2e202eb3ce9c21c1c74fbb7f3e2687b76_2_690x274.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43e5bef2e202eb3ce9c21c1c74fbb7f3e2687b76_2_1035x411.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43e5bef2e202eb3ce9c21c1c74fbb7f3e2687b76_2_1380x548.jpeg 2x" data-dominant-color="79747D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2908×1156 353 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @muratmaga (2023-10-21 20:15 UTC)

<p>What is doesn’t work well with the rotated ROIs though.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> is it possible to add this feature?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d4f03c26de040e7f45f34d655dc3352ff4083f3.jpeg" data-download-href="/uploads/short-url/1TJuHVzdzySN5HBloSTf2jeC7ez.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d4f03c26de040e7f45f34d655dc3352ff4083f3_2_615x500.jpeg" alt="image" data-base62-sha1="1TJuHVzdzySN5HBloSTf2jeC7ez" width="615" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d4f03c26de040e7f45f34d655dc3352ff4083f3_2_615x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d4f03c26de040e7f45f34d655dc3352ff4083f3_2_922x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d4f03c26de040e7f45f34d655dc3352ff4083f3_2_1230x1000.jpeg 2x" data-dominant-color="9C9480"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1682×1366 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @chir.set (2023-10-21 20:43 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="32350">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>doesn’t work well with the rotated ROIs</p>
</blockquote>
</aside>
<p>You may have a look at a custom module, <a href="https://gitlab.com/chir-set/Tools7/-/tree/master/MarkupsToSurface/" rel="noopener nofollow ugc">Markups to surface,</a> that can handle a rotated ROI. It could probably fit this requirement.</p>

---

## Post #8 by @dokay1 (2023-10-22 01:02 UTC)

<p>But then It would still have to be converted to a segment or label map. So it’s 1 step less to just have a hi-resolution template file to Crop to the dimensions of the ROI.</p>

---

## Post #9 by @dokay1 (2023-10-22 02:37 UTC)

<p>OK, created a script (using chat GPT).</p>
<p>It uses the Template volume (“TEMPLATE_for_CROPPING”), and then the ROIs are named V1…10. And then the script iterates on the ROIs and generates Cropped_V1…Cropped_V10 scalar volumes. Simple but useful. My project is expected to have few hundreds of. Voxels, so this can save substantial amounts of time.</p>
<blockquote>
<h1>Initialize CropVolume logic</h1>
<p>cropVolumeLogic = slicer.modules.cropvolume.logic()</p>
<h1>Get the volume node for the template</h1>
<p>templateVolumeNode = slicer.util.getNode(‘TEMPLATE_for_CROPPING’)</p>
<h1>Loop through ROI nodes V1 to V10</h1>
<p>for i in range(1, 11):  # Adjust the range based on your actual ROI names<br>
roiName = f"V{i}"<br>
roiNode = slicer.util.getNode(roiName)</p>
<pre><code>if roiNode:  # Only proceed if the ROI node actually exists
    # Create a new CropVolumeParameters Node for each iteration
    cropVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLCropVolumeParametersNode')
    
    # Set the input volume and ROI for cropping
    cropVolumeNode.SetInputVolumeNodeID(templateVolumeNode.GetID())
    cropVolumeNode.SetROINodeID(roiNode.GetID())
    
    # Apply cropping
    cropVolumeLogic.Apply(cropVolumeNode)
    
    # Get the output volume node
    outputVolumeNode = slicer.mrmlScene.GetNodeByID(cropVolumeNode.GetOutputVolumeNodeID())
    
    # Rename the output volume node to match the ROI with 'Cropped_' prefix
    outputVolumeNode.SetName(f"Cropped_{roiName}")

    # Optionally, save the cropped volume to disk
    # outputPath = f"C:/path/to/save/Cropped_{roiName}.nrrd"
    # slicer.util.saveNode(outputVolumeNode, outputPath)

    # Remove the cropVolumeNode to avoid potential conflicts in the next iteration
    slicer.mrmlScene.RemoveNode(cropVolumeNode)
</code></pre>
</blockquote>

---
