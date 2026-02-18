# How to get a segment in a vtkImageData whithout location issue

**Topic ID**: 678
**Date**: 2017-07-12
**URL**: https://discourse.slicer.org/t/how-to-get-a-segment-in-a-vtkimagedata-whithout-location-issue/678

---

## Post #1 by @Marine (2017-07-12 14:29 UTC)

<p>Hi everyone!</p>
<p>I would like to get a segment from a segmentation node as a vtkImageData (not a vtkOrientedImageData).</p>
<p>My pipeline is:</p>
<ol>
<li>I create a segment from a binary vtkImageData</li>
<li>Then I modify this segment in the segment editor</li>
<li>I want to get back that segment after these modifications in the vtkImageData I had before (in step 1)</li>
<li>To check, I create a new segment from the vtkImageData with the modifications done (got from step 3)</li>
</ol>
<p>I am currently doing this:</p>
<p>std::string segmentID = “…”;<br>
vtkOrientedImageData* labelmap = segmentationNode-&gt;GetBinaryLabelmapRepresentation(segmentID);<br>
vtkImageData* image;<br>
image-&gt;DeepCopy(labelmap);</p>
<p>My problem is that the vtkImageData (“image”) I get back has a spacing and an origin not set to 0 (I was told that for a vtkImageData it has to be 0) and that if I create a new segment from that image the two segmentations don’t match, meaning the shape is the same but the location is not, see: the blue segment is the one I have in Slicer after using tools in the segment editor and the yellow one is the one created from the vtkImageData I get back (I want them to be the same)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/d4946236a58742fb49acaacfb476d6827b6bcf91.jpg" data-download-href="/uploads/short-url/ukz8jZ4KiSp8lJEIAZdbK4lUJfH.jpg?dl=1" title="Capture d’écran 2017-07-12 à 15.48.58.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d4946236a58742fb49acaacfb476d6827b6bcf91_2_341x199.jpg" width="341" height="199" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d4946236a58742fb49acaacfb476d6827b6bcf91_2_341x199.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d4946236a58742fb49acaacfb476d6827b6bcf91_2_511x298.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d4946236a58742fb49acaacfb476d6827b6bcf91_2_682x398.jpg 2x" data-dominant-color="585859"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2017-07-12 à 15.48.58.jpg</span><span class="informations">780×608 77.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efb0d064c53e366c9cd19f8d9f689d9365c73bdc.png" data-download-href="/uploads/short-url/ycoW8LRfXZLpztT2R6BCKFzfsOU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efb0d064c53e366c9cd19f8d9f689d9365c73bdc.png" alt="image" data-base62-sha1="ycoW8LRfXZLpztT2R6BCKFzfsOU" width="589" height="500" data-dominant-color="3C3B3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">800×678 70.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m not sure how to deal with this location problem</p>
<p>Thanks for your help,<br>
Marine.</p>

---

## Post #2 by @lassoan (2017-07-12 16:01 UTC)

<p>Unfortunately, VTK cannot store orientation information in vtkImageData. Therefore you either have to store image in a vtkOrientedImageData object; or store origin+spacing+orientation in a separate matrix and store pixels in vtkImageData (setting spacing to (1,1,1), origin to (0,0,0) in the vtkImageData). It might be tempting to just ignore the image orientation and use a vtkImageData object to store spacing and origin but this approach completely fails when an image is not axis-aligned.</p>
<p>In the long term we’ll try to get vtkOrientedImageData integrated into VTK, but until then you have to learn how to convert between these two representations. There are lots of examples for processing vtkOrientedImageData using VTK filters in segment editor effects:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/Segmentations/EditorEffects/Python">Built-in segment editor effects</a></li>
<li><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorFloodFilling/SegmentEditorFloodFillingLib/SegmentEditorEffect.py">A simple VTK filter based effect</a></li>
<li><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects">A couple of other effects</a></li>
</ul>

---

## Post #3 by @Marine (2017-07-13 09:26 UTC)

<p>Ok, I’ll see what I can do with these information.</p>
<p>Thank you !</p>

---
