# Using script for creating 'intersection' from 'Logical operators' of Segment Editor

**Topic ID**: 36104
**Date**: 2024-05-13
**URL**: https://discourse.slicer.org/t/using-script-for-creating-intersection-from-logical-operators-of-segment-editor/36104

---

## Post #1 by @chz31 (2024-05-13 03:07 UTC)

<p>Hi,</p>
<p>I am using python scrip to access Intersection operation from Logical Operators. I might did the script wrong. Using Logical Operators manually, the intersection between the orbit and the plate is:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6a0325e1a55d62a64fa852db991ecdfebe5489e.jpeg" data-download-href="/uploads/short-url/nM2tLibdc1lpAdOHfm5IlLTiwk6.jpeg?dl=1" title="Screenshot 2024-05-12 at 9.25.53 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6a0325e1a55d62a64fa852db991ecdfebe5489e_2_312x250.jpeg" alt="Screenshot 2024-05-12 at 9.25.53 PM" data-base62-sha1="nM2tLibdc1lpAdOHfm5IlLTiwk6" width="312" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6a0325e1a55d62a64fa852db991ecdfebe5489e_2_312x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6a0325e1a55d62a64fa852db991ecdfebe5489e_2_468x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6a0325e1a55d62a64fa852db991ecdfebe5489e_2_624x500.jpeg 2x" data-dominant-color="6D9D9E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-12 at 9.25.53 PM</span><span class="informations">786×628 90.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>   <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11ff1a6025f3a9c240dbdb8ac8341f25a1c3e0b0.png" data-download-href="/uploads/short-url/2zcFHVvnlno5syYO5gqvyTYEE5W.png?dl=1" title="Screenshot 2024-05-12 at 9.44.59 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11ff1a6025f3a9c240dbdb8ac8341f25a1c3e0b0_2_306x250.png" alt="Screenshot 2024-05-12 at 9.44.59 PM" data-base62-sha1="2zcFHVvnlno5syYO5gqvyTYEE5W" width="306" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11ff1a6025f3a9c240dbdb8ac8341f25a1c3e0b0_2_306x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11ff1a6025f3a9c240dbdb8ac8341f25a1c3e0b0_2_459x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11ff1a6025f3a9c240dbdb8ac8341f25a1c3e0b0_2_612x500.png 2x" data-dominant-color="999CCC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-12 at 9.44.59 PM</span><span class="informations">736×600 28.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I used the script:</p>
<pre><code class="lang-auto">#Logic operator
segmentEditorWidget.setActiveEffectByName("Logical operators")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("Operation","INTERSECT")

boneSegID = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName('bone_no_fx')
plateSegID = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName('plate_copy')

segmentEditorNode.SetSelectedSegmentID(plateSegID)
effect.setParameter("ModifierSegmentID", boneSegID)
effect.self().onApply()
</code></pre>
<p>It showed this effect:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e785849804ee620f205e2804acbdcac9c1bbc4b0.jpeg" data-download-href="/uploads/short-url/x28m6A2s3D1YyBghaMOQSnuSrXG.jpeg?dl=1" title="Screenshot 2024-05-12 at 9.29.19 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e785849804ee620f205e2804acbdcac9c1bbc4b0_2_467x375.jpeg" alt="Screenshot 2024-05-12 at 9.29.19 PM" data-base62-sha1="x28m6A2s3D1YyBghaMOQSnuSrXG" width="467" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e785849804ee620f205e2804acbdcac9c1bbc4b0_2_467x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e785849804ee620f205e2804acbdcac9c1bbc4b0_2_700x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e785849804ee620f205e2804acbdcac9c1bbc4b0_2_934x750.jpeg 2x" data-dominant-color="74747B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-12 at 9.29.19 PM</span><span class="informations">1390×1114 91.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I used <code>segmentEditorNode.SetSelectedSegmentID(plateSegID)</code> to set up the plate segment to be modified by the bone. I think I did this wrong. Can someone tell me how to properly set up the segment to be modified? This <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmenteditor.html#effect-parameters" class="inline-onebox" rel="noopener nofollow ugc">Segment editor — 3D Slicer documentation</a> only shows setting up the modifier ID.</p>
<p>Here is a <a href="https://drive.google.com/file/d/14ZLOH-gHlnHqL3cIbqDG2FOq3MH5T4yY/view?usp=sharing" rel="noopener nofollow ugc">sample vol and segments</a> and here is my <a href="https://github.com/chz31/surgical_plate_registration/blob/main/intersect_plate_orbit.py" rel="noopener nofollow ugc">snippet</a>.</p>

---

## Post #2 by @chir.set (2024-05-13 20:21 UTC)

<p>Your script works fine after commenting</p>
<p><code># segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)</code></p>
<p>In the default Segment editor node, or if you show yours (<em>segmentEditorWidget.show()</em>), we can see that the geometry of ‘5 DummySeriesDesc!’ does not fit in the segmentation or output geometry.</p>

---

## Post #3 by @chz31 (2024-05-14 04:06 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> Thank you for the response and solution! I cropped the volume to save the space but did not notify that I over cropped it.</p>
<p>As you suggested, my script did work after disable <code>segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)</code>.</p>
<p>However, when I tried to load the original volume of the <code>masterVolumeNode</code> set up, it stilled showed the same effect of not generating a proper intersection (here is the <a href="https://drive.google.com/file/d/1QZodtttwqjQiRe8PVpSPXNRf8r3iggZW/view?usp=sharing" rel="noopener nofollow ugc">volume</a> that fits the segmentation)</p>
<p>It also output this error message. It still shows there is a geometry mismatch between <code>inputImage and imageToAppend</code></p>
<pre><code class="lang-auto">[VTK] Generic Warning: In vtkOrientedImageDataResample.cxx, line 1126
[VTK] vtkOrientedImageDataResample::MergeImage failed: geometry mismatch between inputImage and imageToAppend
[VTK] vtkSegmentationModifier::SetBinaryLabelmapToSegment: Invalid input labelmap
[Qt] virtual void qSlicerSegmentEditorAbstractEffect::modifySegmentByLabelmap(vtkMRMLSegmentationNode *, const char *, vtkOrientedImageData *, qSlicerSegmentEditorAbstractEffect::ModificationMode, const int *, bool) : Failed to add modifier labelmap to selected segment
</code></pre>
<p>Perhaps I simply should not set up a master volume for intersection? I wonder if it is due to the two segments were converted back from surface models. I also acquired these samples segmented by other people. The Segment Editor did work well though even with the original unfitted master volume.</p>

---
