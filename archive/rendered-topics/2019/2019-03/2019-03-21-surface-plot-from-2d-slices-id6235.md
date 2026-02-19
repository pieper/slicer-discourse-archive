---
topic_id: 6235
title: "Surface Plot From 2D Slices"
date: 2019-03-21
url: https://discourse.slicer.org/t/6235
---

# surface plot from 2D slices

**Topic ID**: 6235
**Date**: 2019-03-21
**URL**: https://discourse.slicer.org/t/surface-plot-from-2d-slices/6235

---

## Post #1 by @nahida (2019-03-21 12:55 UTC)

<p>Hi , I have 24 slices of one eye from OCT images. When I load them in slicer and view in volume rendering all slices are placed in horizontally, not make a circle, I want every slices spaced at 30 degree and makes a round eye.</p>
<p>Can anyone please help me in this regards?</p>

---

## Post #2 by @pieper (2019-03-21 14:32 UTC)

<p>Could you add a screenshot so we have a better idea about the data?</p>

---

## Post #3 by @lassoan (2019-03-21 15:12 UTC)

<p>Do you read the images from DICOM? If yes, then you might be able to reconstruct acquisition geometry by setting “Acquisition geometry regularization” to “apply regularization transform” in application settings (menu: Edit / Application settings / DICOM / DICOMScalarVolumePlugin) before loading the image from the DICOM browser.</p>

---

## Post #4 by @nahida (2019-03-21 23:44 UTC)

<p>Thank you Andras, my images are not from DICOM, they are in jpg format. export as jpeg from OCT pentacam machine.</p>

---

## Post #5 by @lassoan (2019-03-22 00:07 UTC)

<p>If you only have a set of JPEG images, then there is no information about positions of each image slice in 3D. Slicer assumes that they should be stacked on top of each other with a constant spacing. Is this a correct assumption? Or they should be arranged in some circular pattern?</p>
<p>As Steve asked above, could you post screenshots of how the images should appear (e.g., screenshot from your OCT imaging console) and how it appears in Slicer?</p>

---

## Post #6 by @nahida (2019-03-22 00:42 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa42089c760b317a5de6ecfeba6778ca57c5f30a.png" data-download-href="/uploads/short-url/oiaE4JjoMQvhe7ShPLoLTo7691E.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa42089c760b317a5de6ecfeba6778ca57c5f30a_2_690x270.png" alt="Untitled" data-base62-sha1="oiaE4JjoMQvhe7ShPLoLTo7691E" width="690" height="270" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa42089c760b317a5de6ecfeba6778ca57c5f30a_2_690x270.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa42089c760b317a5de6ecfeba6778ca57c5f30a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa42089c760b317a5de6ecfeba6778ca57c5f30a.png 2x" data-dominant-color="838683"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1016×399 229 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi Steve, here are the screenshot, all the slices sectioning by green color, total 25 slices from whole section.<br>
Now i want to reconstruct the original round image from all of those slices.</p>

---

## Post #7 by @nahida (2019-03-22 00:58 UTC)

<p>Hi Andras, they should be arranged in circular pattern.  I also upload the real images in reply of Steve and  here I am uploading how they appear when I saw as volume rendering.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62fcc81a45e5599d14f67780891a7e0ff725e909.jpeg" data-download-href="/uploads/short-url/e7GncMzxIRQf3nK8mJx2zsg4gzL.jpeg?dl=1" title="slicer2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62fcc81a45e5599d14f67780891a7e0ff725e909_2_690x411.jpeg" alt="slicer2" data-base62-sha1="e7GncMzxIRQf3nK8mJx2zsg4gzL" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62fcc81a45e5599d14f67780891a7e0ff725e909_2_690x411.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62fcc81a45e5599d14f67780891a7e0ff725e909_2_1035x616.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62fcc81a45e5599d14f67780891a7e0ff725e909_2_1380x822.jpeg 2x" data-dominant-color="32313A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer2</span><span class="informations">1420×846 71.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It  could be great if I select every slices and I can manually fix their position.</p>

---

## Post #8 by @pieper (2019-03-22 13:04 UTC)

<p>Thanks, those images help a lot.  The acquisitions need to be resampled into a rectilinear space for Slicer to volume render them.  There are many ways to do this with a little programming, but no point-and-click method right now that I’m aware of.  If you are up for the programming we’d be glad to give some suggestions.</p>

---

## Post #9 by @nahida (2019-03-22 13:21 UTC)

<p>Thanks Steve, I can do some programming, would you please tell me the details.</p>

---

## Post #10 by @pieper (2019-03-22 14:06 UTC)

<aside class="quote no-group" data-username="nahida" data-post="9" data-topic="6235" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nahida/48/3307_2.png" class="avatar"> nahida:</div>
<blockquote>
<p>Thanks Steve, I can do some programming, would you please tell me the details</p>
</blockquote>
</aside>
<p>Great, well, depending on how concerned you are about efficiency you might need to try some more sophisticated methods, but I’d suggest starting with something simple that you can use as a baseline.</p>
<p>As an example, here’s an easy way to make a volume node with random data in it.  Run this in the python interactor and you should be able to see the random noise in the slice views.</p>
<pre><code class="lang-auto">n = slicer.mrmlScene.CreateNodeByClass('vtkMRMLScalarVolumeNode')
n.SetName('my volume')
slicer.mrmlScene.AddNode(n)
import numpy
slicer.util.updateVolumeFromArray(n, numpy.random.sample([30,30,30]))
</code></pre>
<p>Working from there you could make an array of zeros instead, and then iterate through the OCT slices and just copy (or interpolate) the pixels into the corresponding voxels.   Since you have the jpg files loaded you can get them as numpy arrays with <code>slicer.util.arrayFromVolume(volumeNode)</code>.</p>

---

## Post #11 by @nahida (2019-03-22 14:40 UTC)

<p>Thank you Steve, I will try these code and let you know how it goes.</p>

---
