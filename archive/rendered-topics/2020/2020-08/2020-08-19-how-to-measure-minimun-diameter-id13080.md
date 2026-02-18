# How to measure minimun diameter?

**Topic ID**: 13080
**Date**: 2020-08-19
**URL**: https://discourse.slicer.org/t/how-to-measure-minimun-diameter/13080

---

## Post #1 by @apparrilla (2020-08-19 00:00 UTC)

<p>Hi everyone!</p>
<p>Slicer version: 4.11.0-2020-07-04 r29204 Win</p>
<p>I want to measure the minimun diameter of a pseudotube segment</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9d408cb3b78238a511acd27d63403ed68a0bfa6.jpeg" data-download-href="/uploads/short-url/v4ZTl74sUl4MYFSBw5vrwWp7E1M.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d9d408cb3b78238a511acd27d63403ed68a0bfa6_2_304x250.jpeg" alt="image" data-base62-sha1="v4ZTl74sUl4MYFSBw5vrwWp7E1M" width="304" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d9d408cb3b78238a511acd27d63403ed68a0bfa6_2_304x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d9d408cb3b78238a511acd27d63403ed68a0bfa6_2_456x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d9d408cb3b78238a511acd27d63403ed68a0bfa6_2_608x500.jpeg 2x" data-dominant-color="9693AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1062×872 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48bd286fae4fd070cb5f0b15fda56f439e25476f.jpeg" data-download-href="/uploads/short-url/antE6L8rEtuJpLHyPNIXv6hUx4z.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48bd286fae4fd070cb5f0b15fda56f439e25476f_2_294x250.jpeg" alt="image" data-base62-sha1="antE6L8rEtuJpLHyPNIXv6hUx4z" width="294" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48bd286fae4fd070cb5f0b15fda56f439e25476f_2_294x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48bd286fae4fd070cb5f0b15fda56f439e25476f_2_441x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48bd286fae4fd070cb5f0b15fda56f439e25476f_2_588x500.jpeg 2x" data-dominant-color="A09DBA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1327×1125 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3391d166aa14c5b839136917e6be18983eb0c7b3.png" alt="image" data-base62-sha1="7mcLoXL48nuVfqH0w0ZMmrSdvBF" width="189" height="197"></p>
<p>I´ve tryed Extract Centerline Module and Segment Statistics Module but I think radius data in output table is the mean value.</p>

---

## Post #2 by @lassoan (2020-08-19 00:25 UTC)

<p>You can use Segment Cross Section Area module (in Sandbox extension) to get cross section area along the segment, look up the minimum value, and compute the equivalent diameter (<code>sqrt(4*a/pi)</code>).</p>

---

## Post #3 by @apparrilla (2020-08-26 00:39 UTC)

<p>Segment Cross Section Area module is pretty near to what I need. I´ve been trying some code but i have a trouble with labelmap data.</p>
<pre><code># a.- Create labelmap node
LabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode', "SegmentLabelmap")

# b.- Export Segment to Labelmap volume
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, LabelmapVolumeNode, None)

# c.- Export Labelmap to numpy array
voxels = slicer.util.arrayFromVolume(LabelmapVolumeNode)

# d.- Get all slices of the volume as numpy array
for i in range(voxels.shape[0]):
  slice = voxels[i,:,:]  
</code></pre>
<p>Images I get are like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3325b6fe92e8bbcca32526752bc5fa0bb48bb01a.png" data-download-href="/uploads/short-url/7it9AnMUpyqNG1EcuREXT1spJq2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3325b6fe92e8bbcca32526752bc5fa0bb48bb01a_2_193x250.png" alt="image" data-base62-sha1="7it9AnMUpyqNG1EcuREXT1spJq2" width="193" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3325b6fe92e8bbcca32526752bc5fa0bb48bb01a_2_193x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3325b6fe92e8bbcca32526752bc5fa0bb48bb01a_2_289x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3325b6fe92e8bbcca32526752bc5fa0bb48bb01a_2_386x500.png 2x" data-dominant-color="4F4F4F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">494×638 5.69 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Expected image:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cd4faa954fe0c7f64f02331e79670e50b9d0eba.png" data-download-href="/uploads/short-url/hOjvKkmY13YEmudU5jlkycYpjei.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cd4faa954fe0c7f64f02331e79670e50b9d0eba.png" alt="image" data-base62-sha1="hOjvKkmY13YEmudU5jlkycYpjei" width="311" height="250" data-dominant-color="555555"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">700×562 786 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I thought i was a problem related with labelmap reference (although ExportVisibleSegmentsToLabelmapNode(segmentationNode, LabelmapVolumeNode, <strong>None</strong>)) so I get the inverted segment transform to move it to RAS and harden it to force resample.</p>
<p>Code between b and c steps:</p>
<pre><code>invSegTransform = slicer.mrmlScene.GetFirstNodeByName("SegTransform (-)")    
LabelmapVolumeNode.SetAndObserveTransformNodeID(invSegTransform.GetID())
LabelmapVolumeNode.HardenTransform()
</code></pre>
<p>Labelmap Volume Rendering shows like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/8538888f31f2ea6f11e46e6e8326de841bf62278.png" data-download-href="/uploads/short-url/j0wCNWrcrGCurWmftbIFVQzrYVy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8538888f31f2ea6f11e46e6e8326de841bf62278_2_260x375.png" alt="image" data-base62-sha1="j0wCNWrcrGCurWmftbIFVQzrYVy" width="260" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8538888f31f2ea6f11e46e6e8326de841bf62278_2_260x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8538888f31f2ea6f11e46e6e8326de841bf62278_2_390x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8538888f31f2ea6f11e46e6e8326de841bf62278_2_520x750.png 2x" data-dominant-color="9A9FCF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1196×1723 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For my surprice, slice images didn´t change at all, numpy array values from labelmap can´t be changed by this method. Even resampling a new copied labelmap volumen, images are still the same.</p>
<p>Could you help me with this issue?<br>
Thanks on advance.</p>

---

## Post #4 by @apparrilla (2020-08-27 17:06 UTC)

<p>Can you give some idea about this <a class="mention" href="/u/lassoan">@lassoan</a>, please?</p>

---

## Post #5 by @lassoan (2020-08-27 17:09 UTC)

<p>You need to choose an axis that is aligned with the axis of the object. the object is not aligned with any of the image axes then you can create an ROI that is aligned with the principal axes (or oriented bounding box) of the segmented object and then crop the volume with that ROI.</p>
<p>Alternatively, the cross section analysis module could be enhanced to take an arbitrary line as input and it would resample the image along that direction.</p>

---

## Post #6 by @apparrilla (2020-08-28 00:29 UTC)

<p>Crop Labelmap with a transformed ROI for resampling works perfect.<br>
Thanks so much</p>

---
