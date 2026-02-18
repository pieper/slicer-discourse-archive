# How to expand a segment size via Python

**Topic ID**: 14361
**Date**: 2020-11-01
**URL**: https://discourse.slicer.org/t/how-to-expand-a-segment-size-via-python/14361

---

## Post #1 by @marianaslicer (2020-11-01 12:58 UTC)

<p>Hi everyone,</p>
<p>I would like to create a new segment from an existing segment. The idea would be to expand the existing segment in the three directions, adding different margins to each of the directions (e.g. x = 1 mm, y = 2 mm and z = 3 mm) via Python script.</p>
<p>I found the margin effect of the Segment Editor module a possibility, but I think the margin for growth has to be the same in all directions. Am I wrong? Is there any workaround? Thank you in advance.</p>

---

## Post #2 by @lassoan (2020-11-01 20:04 UTC)

<p>We use distance map transform for fast grow/shrink (regardless of margin size), which requires isotropic growth. However, you can use morphological operations to grow by different amount along each axis - see Margin effect’s <a href="https://github.com/Slicer/Slicer/blob/1b64b5cc4131a613271cffe7d513a1101567916f/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorMarginEffect.py#L142-L151">old implementation</a>.</p>
<p>What is the reason you would like to increase the margin by different amount along different axes?</p>

---

## Post #3 by @marianaslicer (2020-11-02 11:51 UTC)

<p>Thank you for your response.</p>
<p>I would like to increase the margin by different amounts along different axes for radiotherapy purposes. During radiation treatments, geometrical uncertainties are taking into account by adding a margin to the target volume. And my question comes up since I want to grow a segment by a margin that is related to the 3D movement of the target volume. I was expected to use the SegmentMorphology module but the SlicerRT extension does not have this module anymore.</p>
<p>Is there any surrogate module for 3D slicer version 4.11?</p>

---

## Post #4 by @marianaslicer (2020-12-04 13:17 UTC)

<p>Hi Andras,</p>
<p>I tried to use the Margin effect’s implementation to increase the segment margins, but the argument of the SetDilateValue function must be a real number and not a list.</p>
<pre><code>erodeDilate = vtk.vtkImageDilateErode3D()

erodeDilate.SetInputData(contour.GetSegmentation().GetSegmentRepresentation(target, 'Binary labelmap'))

marginX = patient.ptvMargins[0]
marginY = patient.ptvMargins[1]
marginZ = patient.ptvMargins[2]

margins = [marginX, marginY, marginZ]
erodeDilate.SetDilateValue(margins)
</code></pre>
<p>What I really needed is something like the ContourMorphology module of SlicerRT extension. But this module is no longer available in the latest nightly version.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b8d7aea38e813551132b7cc2d86d67b6b5206bb.png" data-download-href="/uploads/short-url/d3UzjyShG9zLj8qIteJusY9XBVx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b8d7aea38e813551132b7cc2d86d67b6b5206bb.png" alt="image" data-base62-sha1="d3UzjyShG9zLj8qIteJusY9XBVx" width="375" height="500" data-dominant-color="F1F2F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">418×557 11.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How can I get the same output? I would really appreciate your help.</p>

---

## Post #5 by @lassoan (2020-12-04 20:26 UTC)

<p>Expanding a segment with anisotropic margin size using vtkImageDilateErode3D is just a few lines of code. I’ve included a link above that shows the exact code that you can use: <a href="https://github.com/Slicer/Slicer/blob/1b64b5cc4131a613271cffe7d513a1101567916f/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorMarginEffect.py#L142-L151">https://github.com/Slicer/Slicer/blob/1b64b5cc4131a613271cffe7d513a1101567916f/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorMarginEffect.py#L142-L151</a></p>
<p>However, I would not recommend to simulate effect of motion by applying anisotropic margin growing along imaging axes, because in general the motion axis directions and magnitudes are not the same as imaging axes, and you cannot simulate rotations at all.</p>
<p>Instead, I would recommend to actually simulate motion. Copy a segment to a separate segmentation node, apply a small transform to that node, copy the segment back to the original segmentation node, and combine it with the existing segment using Logical operators effect. Repeat this with slightly different translations, rotations (a set of representative typical displacements).</p>

---

## Post #6 by @marianaslicer (2020-12-08 19:12 UTC)

<p>Thanks a lot for your reply.</p>
<p>The margins that I want to add take into account the 3D movement of the tumour. They were calculated using the B-spline image registration method and the transform module available in 3D Slicer.</p>
<p>I tried to use the aforementioned code but there was no change in the segment. The parameters and the code that I am using are the following:</p>
<p>kernelsize = [3,3,6]<br>
segment spacing = (0.0731959, 0.0731959, 0.0731959)</p>
<pre><code>selectedSegmentLabelmap = contour.GetSegmentation().GetSegmentRepresentation(target, 'Binarylabelmap')
marginX = patient.ptvMargins[0]
marginY = patient.ptvMargins[1]
marginZ = patient.ptvMargins[2]

margins = [marginX, marginY, marginZ]
kernelSizePixel = [int(round(margins[0])), int(round(margins[1])), int(round(margins[2]))]
         
labelValue = 1
backgroundValue = 0
thresh = vtk.vtkImageThreshold()
thresh.SetInputData(selectedSegmentLabelmap)
thresh.ThresholdByLower(0)
thresh.SetInValue(backgroundValue)
thresh.SetOutputScalarType(selectedSegmentLabelmap.GetScalarType())

erodeDilate = vtk.vtkImageDilateErode3D()
erodeDilate.SetInputConnection(thresh.GetOutputPort())

for margin in kernelSizePixel:
	if margin &gt; 0:
		# grow
            erodeDilate.SetDilateValue(labelValue)
            erodeDilate.SetErodeValue(backgroundValue)

erodeDilate.SetKernelSize(kernelSizePixel[0],kernelSizePixel[1],kernelSizePixel[2])
erodeDilate.Update()
modifierLabelmap = vtkSegmentationCore.vtkOrientedImageData()
modifierLabelmap.DeepCopy(erodeDilate.GetOutput())

# Save modifications

name = patient.ID + "_PTV_S" + str(SSigma) + "_s" + str(Rsigma)
SegmentationNode = slicer.vtkMRMLSegmentationNode()
slicer.mrmlScene.AddNode(SegmentationNode)
SegmentationNode.SetName(name)
          
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(modifierLabelmap,SegmentationNode)

return "Created PTV with name: " + name
</code></pre>
<p>Am I doing something wrong? Thank you!</p>

---

## Post #7 by @lassoan (2020-12-08 19:22 UTC)

<p>If you want to modify a segment then you can do this (instead of what you currently do in <code># Save modifications</code>):</p>
<pre><code>self.scriptedEffect.modifySelectedSegmentByLabelmap(
    modifierLabelmap,
    slicer.qSlicerSegmentEditorAbstractEffect.ModificationModeAdd)</code></pre>

---

## Post #8 by @marianaslicer (2020-12-08 21:40 UTC)

<p>Thank you for your quick reply.<br>
I have the following output: ‘FindMarginsLogic’ object has no attribute ‘scriptedEffect’</p>

---

## Post #9 by @lassoan (2020-12-09 01:24 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="14361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>self.scriptedEffect.modifySelectedSegmentByLabelmap</code></p>
</blockquote>
</aside>
<p>You need to run <code>self.scriptedEffect.modifySelectedSegmentByLabelmap</code> from inside a segment editor effect (as it is done in SegmentEditorSmoothingEffect.py). If you don’t want to put your code into a segment editor effect then you can call its methods from outside.</p>
<p>If you want to write a script that is independent from the Segment Editor then the simplest is to export to labelmap volume, apply the image processing operations on it, then import the modified labelmap volume into the segmentation node. I added a complete example that demonstrates this to the script repository: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#process-segment-using-a-vtk-filter" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>

---

## Post #10 by @marianaslicer (2020-12-09 11:45 UTC)

<p>Thank you a lot, it worked!<br>
I have another question: is it not possible to expand the segment with a float margin?<br>
As an example, I want to add these specific margins ([3,483 ; 3,494 ; 6,270] mm) but the kernel size must be integer ([3,3,6] mm).<br>
Is there any way to apply the image processing operations with these float margins?</p>
<p>Thank you again for your help.</p>

---

## Post #11 by @lassoan (2020-12-09 14:49 UTC)

<p>Segmentation is represented as a binary volume, so you the added margin is always a multiple of the spacing (=voxel size) of this volume. You can change segmentation’s internal volume spacing by clicking on the “Specify geometry” button next to the master volume selector.</p>

---

## Post #12 by @marianaslicer (2020-12-10 19:20 UTC)

<p>Thank you for your help.<br>
I ended up changing the segmentation geometry by using the referenceVolumeNode geometry with the code:</p>
<p><code>slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(segmentationNode, segmentIds,labelmapVolumeNode,referenceVolumeNode)</code></p>

---

## Post #13 by @Lionel (2022-03-22 08:17 UTC)

<p>Hi Andras,<br>
I would like to write a python script that use vtk.vtkImageDilateErode3D() function to dilate my segment size independently from the Segment Editor Module of 3D Slicer.<br>
The link you provided in this comment is no longer available, can you please tell me where I would be able to find the complete example you have cited ?</p>
<p>Thank you in advance.</p>

---

## Post #14 by @lassoan (2022-08-04 06:20 UTC)

<p>The script repository was moved to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="inline-onebox">Script repository — 3D Slicer documentation</a> and you can find the relevant section by searching for words in the full link. I’ve updated the link in my post above to point to the new location.</p>

---

## Post #15 by @erhushenshou (2023-09-11 09:57 UTC)

<p>Hi, Andras. I wonder how I can find the source code for erodeDilate this class? That is I want to study source code about expanding margin. It want to learn how it is implemented if I have the point coordinate of the geometry.</p>

---
