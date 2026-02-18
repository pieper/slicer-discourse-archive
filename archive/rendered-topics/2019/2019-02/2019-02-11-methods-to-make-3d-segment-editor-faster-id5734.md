# Methods to Make 3D Segment Editor Faster

**Topic ID**: 5734
**Date**: 2019-02-11
**URL**: https://discourse.slicer.org/t/methods-to-make-3d-segment-editor-faster/5734

---

## Post #1 by @triple_axel (2019-02-11 22:38 UTC)

<p>Hi,</p>
<p>Currently, the 3D segment editor tool is running very slowly on my laptop whenever I try to segment a 3D volume.</p>
<p>I was wondering if there were any methods to make this process faster?</p>
<p>Thanks</p>

---

## Post #2 by @gleman (2019-02-11 23:01 UTC)

<p>I just had the same issue and noticed that the GPU memory size in the Volume Rendering / Advanced widget had been reset to 128MB.  Setting it back to 6GB (which my video card supports) got it back to it’s old snappy self.  YMMV.</p>
<p>I’ve added the following in the startup code of my scripts:</p>
<pre><code>volumeRenderingGPUNode = slicer.util.getNodesByClass('vtkMRMLGPURayCastVolumeRenderingDisplayNode')[0]
volumeRenderingGPUNode.SetGPUMemorySize(6144)</code></pre>

---

## Post #3 by @triple_axel (2019-02-12 16:08 UTC)

<p>Hi, I set mine back to 4GP as that is what my video card supports, and it does in fact run faster then before, but not as fast as I need it to be. Do you have any other tips/tricks to make segmentation in 3D views faster? (Through scripts)</p>

---

## Post #4 by @triple_axel (2019-02-13 22:06 UTC)

<p>I managed to make it a bit faster by increasing the scaling for volume rendering through scripts (using Crop Volume).<br>
However, it still does not run fast enough.<br>
Would one issue perhaps creating a 3D Closed Surface rather then a Binary LabelMap? What is the difference between the two? If I were to instead create a binary labelmap to edit from could I use the same script I’ve been using to activate/run the Segment Editor?<br>
Would anyone have any example scripts for conversion to Binary Label Map?</p>
<p>Thanks</p>

---

## Post #5 by @cpinter (2019-02-13 22:23 UTC)

<p>The reason it’s slow is probably because you have Show 3D turned on, and whenever your segmentation changes it updates the 3D surface. You don’t need the surface for segmentation, it is only a visual aid. The underlying representation that you edit in Segment Editor is actually a binary labelmap, and conversion is done automatically. Please refer to this page:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations</a></p>
<p>It would be possible to not convert to surface but do volume rendering without any conversion, but it has not been added yet. In the meantime you can turn off 3D and only show it when necessary.</p>

---

## Post #6 by @lassoan (2019-02-13 22:37 UTC)

<p>You can get very fast 3D updates if you disable surface smoothing (see checkbox in drop-down menu of <code>Show 3D</code> button).</p>

---

## Post #7 by @triple_axel (2019-02-14 15:43 UTC)

<p>Thank you so much for all the help and quick replies!</p>

---

## Post #8 by @triple_axel (2019-02-14 17:01 UTC)

<p>Sorry I have one more quick question about this.<br>
I know how to disable surface smoothening by setting “smoothing factor” to 0 using the segmentation node:<br>
seg.GetSegmentation().SetConversionParameter(‘Smoothing factor’,‘0.0’)<br>
before activating the segment editor widget.</p>
<p>However, how do I enable the surface smoothening display again once I turn off any segment editor affects, or when I do:<br>
segmentEditorWidget.setActiveEffectByName(“None”)<br>
When I do seg.GetSegmentation().SetConversionParameter(‘Smoothing factor’,‘0.5’) nothing happens and it still stays unsmoothened.</p>
<p>Also, I was wondering how to set the diameter of the brush in segment editor to a specific size (ie 10%) through scripts?</p>

---

## Post #9 by @cpinter (2019-02-14 20:18 UTC)

<p>I guess you just need to request conversion again using the new conversion parameter:</p>
<pre><code>seg.GetSegmentation().CreateRepresentation('Closed surface', True) # Last parameter forces conversion even if it exists
seg.Modified() # Update display</code></pre>

---

## Post #10 by @triple_axel (2019-02-15 14:43 UTC)

<p>That did the trick, thanks a bunch.</p>

---
