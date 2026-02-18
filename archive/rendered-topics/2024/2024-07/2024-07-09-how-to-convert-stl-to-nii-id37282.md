# How to convert stl to nii

**Topic ID**: 37282
**Date**: 2024-07-09
**URL**: https://discourse.slicer.org/t/how-to-convert-stl-to-nii/37282

---

## Post #1 by @pc666nice (2024-07-09 14:03 UTC)

<p>Dear all:<br>
I’m trying to convert stl file to nii for the medical image segmentation, however,  when I use the method in the link :<br>
[<a href="https://discourse.slicer.org/t/converting-stl-files-to-binary-label-maps-in-nii-format-using-python/13038">Converting .stl files to binary label maps in .nii format using Python - Support - 3D Slicer Community</a>](https://), but the generated mask didn’t match the original image very well.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3553160ec144b54ea0fbe14c9c50ea85b61cfb4.jpeg" data-download-href="/uploads/short-url/niUlRnWxEdcFJNXheGRtWRlt3k8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3553160ec144b54ea0fbe14c9c50ea85b61cfb4_2_690x386.jpeg" alt="image" data-base62-sha1="niUlRnWxEdcFJNXheGRtWRlt3k8" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3553160ec144b54ea0fbe14c9c50ea85b61cfb4_2_690x386.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3553160ec144b54ea0fbe14c9c50ea85b61cfb4_2_1035x579.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3553160ec144b54ea0fbe14c9c50ea85b61cfb4_2_1380x772.jpeg 2x" data-dominant-color="BABBBE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1793×1005 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I use the similar method in Mimics, the mask matched the image:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f028b2ed2b023373e15f77e3f2af3d90bb1b5b9b.jpeg" data-download-href="/uploads/short-url/ygxMYD388hKln5P39qcAObmpteb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f028b2ed2b023373e15f77e3f2af3d90bb1b5b9b_2_690x345.jpeg" alt="image" data-base62-sha1="ygxMYD388hKln5P39qcAObmpteb" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f028b2ed2b023373e15f77e3f2af3d90bb1b5b9b_2_690x345.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f028b2ed2b023373e15f77e3f2af3d90bb1b5b9b_2_1035x517.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f028b2ed2b023373e15f77e3f2af3d90bb1b5b9b_2_1380x690.jpeg 2x" data-dominant-color="747470"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×960 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is the code that I use:</p>
<pre><code class="lang-auto">
import os
import slicer

stl_file_name = "D:/PengChen/zhongshan/CFDPCNNmd/stls/1.stl"
output_file_name = "D:/PengChen/zhongshan/CFDPCNNmd/stl_niis/1.nii.gz"
reference_volume_path = "D:/PengChen/zhongshan/CFDPCNNmd/images/1.nii.gz"

referenceVolumeNode = slicer.util.loadVolume(reference_volume_path)
segmentationNode = slicer.util.loadSegmentation(stl_file_name)  ## stl
outputLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, outputLabelmapVolumeNode, referenceVolumeNode)
slicer.util.saveNode(outputLabelmapVolumeNode, output_file_name)


</code></pre>
<p>Using the above code, I can generated the file but it only has the background, not the binary labelmap.</p>
<p>I’m looking forward to get the correct method, thanks a lot.</p>

---

## Post #2 by @cpinter (2024-07-10 09:12 UTC)

<p>First of all we need to know where do you get the STL from. If you produce it in Slicer, the answer will be quite different from if you get it externally.</p>
<aside class="quote no-group" data-username="pc666nice" data-post="1" data-topic="37282">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pc666nice/48/77252_2.png" class="avatar"> pc666nice:</div>
<blockquote>
<p>didn’t match the original image very well</p>
</blockquote>
</aside>
<p>I assume you are talking about the voxelization error, meaning that the voxels are too large to fit well the smooth STL boundaries. Do I understand correctly?</p>

---

## Post #3 by @pc666nice (2024-12-27 08:57 UTC)

<p>Thanks for your reply,  that’s right, because there is something wrong when I transfer the dicom files to the nii.gz files</p>

---
