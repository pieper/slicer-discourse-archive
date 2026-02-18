# Segment editor effect sourceVolumeImageData not updated

**Topic ID**: 37500
**Date**: 2024-07-22
**URL**: https://discourse.slicer.org/t/segment-editor-effect-sourcevolumeimagedata-not-updated/37500

---

## Post #1 by @Llujoo (2024-07-22 13:59 UTC)

<p>Hello I am writing a SegmentEditorEffect based on AbstractScriptedSegmentEditorEffect.</p>
<p>When I call <code>self.scriptedEffect.sourceVolumeImageData()</code> everything works fine. However if I change the selected source volume in the segment editor the change will not be recognized and once I call <code>self.scriptedEffect.sourceVolumeImageData()</code> again, I get the old image data.</p>
<p>If I change the segmentation this is reset and I will get the first selected volume but cannot get any follow up selection</p>
<p>Is there a way to force an update of this?</p>

---

## Post #2 by @lassoan (2024-07-22 15:57 UTC)

<p>It all works well for me. For example, load two volumes, use threshold effect, select another source volume, use threshold effect.</p>
<p>Please provide full script that I can simply copy-paste into the Python console and reproduces the behavior you reported.</p>

---

## Post #3 by @Llujoo (2024-07-23 07:17 UTC)

<p>Thanks for your quick reply, Andras.</p>
<p>I tried ThresholdEffect’s and it works fine here. I don’t know why though. When I copy code and add a check to see if the sourceVolume has changed it has the same behavior.</p>
<p>I am pretty new to slicer and python so I might be making obvious mistakes.</p>
<p>I’ve tried to create a minimal version:</p>
<ol>
<li>Save this to MySegmentEditorEffect.py</li>
<li>Run the lines below after fixing the path.</li>
<li>Drag and drop at least 2 images</li>
<li>Switch the images in Segment Editor’s ComboBox.</li>
<li>In my opinion you shoulg get the “sourceImageData changed”-Message every time you change the image</li>
</ol>
<pre><code class="lang-auto">from SegmentEditorEffects import *
class MySegmentEditorEffect(AbstractScriptedSegmentEditorEffect):
    def __init__(self, scriptedEffect):
        AbstractScriptedSegmentEditorEffect.__init__(self, scriptedEffect)
        scriptedEffect.name = "MySegmentEditorEffect"
        self.sourceImageData = None

    def clone(self):
        # It should not be necessary to modify this method
        import qSlicerSegmentationsEditorEffectsPythonQt as effects
        clonedEffect = effects.qSlicerSegmentEditorScriptedEffect(None)
        clonedEffect.setPythonSource(__file__.replace('\\','/'))
        return clonedEffect
    
    def sourceVolumeNodeChanged(self):
        sourceImageData = self.scriptedEffect.sourceVolumeImageData()

        if(self.sourceImageData != sourceImageData):
            if( sourceImageData is None):
                print(f"sourceImageData changed: None")
            else:
                print(f"sourceImageData changed: {sourceImageData.GetExtent()}")
            self.sourceImageData = sourceImageData
</code></pre>
<pre><code class="lang-auto">import qSlicerSegmentationsEditorEffectsPythonQt as effects
scriptedEffect = effects.qSlicerSegmentEditorScriptedEffect(None)
scriptedEffect.setPythonSource(r"Your_Location\MySegmentEditorEffect.py")
scriptedEffect.self().register()
</code></pre>

---

## Post #4 by @Llujoo (2024-07-25 12:38 UTC)

<p>I’ve investigated further and while the SegmentEditorThresholdEffect works as it should it has the same issue. If i change up the sourceVolumeNodeChanged method as below, I get the same behavior.<br>
Maybe I will find out where it get’s the correct data but this seems like a genuine bug to me.<br>
Have you found anything <a class="mention" href="/u/lassoan">@lassoan</a> ?</p>
<pre><code class="lang-auto">    def sourceVolumeNodeChanged(self):
        # Set scalar range of source volume image data to threshold slider
        masterImageData = self.scriptedEffect.sourceVolumeImageData()
        if masterImageData:
            print(f"this should change: {masterImageData.GetDimensions()}")
            lo, hi = masterImageData.GetScalarRange()
            self.thresholdSlider.setRange(lo, hi)
            self.thresholdSlider.singleStep = (hi - lo) / 1000.
            if (self.scriptedEffect.doubleParameter("MinimumThreshold") == self.scriptedEffect.doubleParameter("MaximumThreshold")):
                # has not been initialized yet
                self.scriptedEffect.setParameter("MinimumThreshold", lo + (hi - lo) * 0.25)
                self.scriptedEffect.setParameter("MaximumThreshold", hi)
</code></pre>

---

## Post #5 by @Llujoo (2024-07-25 12:46 UTC)

<p>Okay I found a solution. I can get the Node instead and then the image data. The node is updated.</p>
<pre><code class="lang-auto">sourceImageData = self.scriptedEffect.parameterSetNode().GetSourceVolumeNode().GetImageData()
</code></pre>

---

## Post #6 by @lassoan (2024-07-25 15:57 UTC)

<p>This code gives you the source volume’s image data as is:</p>
<pre><code class="lang-auto">self.scriptedEffect.parameterSetNode().GetSourceVolumeNode().GetImageData()
</code></pre>
<p>This is usually not what you need, because the source volume’s geometry (origin, spacing, axis directions, extents) may differ from the segmentation’s.</p>
<p>This gives you the image data resampled to the segmentation’s geometry (taking into account all parent transforms, including warping transforms):</p>
<pre><code class="lang-auto">masterImageData = self.scriptedEffect.sourceVolumeImageData()
</code></pre>
<p>What you observed (image data is resampled to the segmentation’s geometry, therefore dimension does not change) maybe unexpected, but it is the correct, intended behavior.</p>

---
