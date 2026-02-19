---
topic_id: 41334
title: "How To Integrate Threshold Effect From Segment Editor Into A"
date: 2025-01-28
url: https://discourse.slicer.org/t/41334
---

# How to Integrate Threshold Effect from Segment Editor into a Custom Module

**Topic ID**: 41334
**Date**: 2025-01-28
**URL**: https://discourse.slicer.org/t/how-to-integrate-threshold-effect-from-segment-editor-into-a-custom-module/41334

---

## Post #1 by @igi133 (2025-01-28 11:36 UTC)

<p>Hi everyone,</p>
<p>I am currently working on a custom module in 3D Slicer and would like to incorporate the functionality of the “Threshold” effect from the Segment Editor module.</p>
<p>My main goal is to allow users to:</p>
<ol>
<li>Set threshold values (e.g., lower and upper bounds).</li>
<li>Preview the thresholded region in real-time on a specific image.</li>
</ol>
<p>I’ve been trying to achieve this for some time now, but I haven’t been able to figure it out. I don’t need the full functionality of the Segment Editor, just these two features.</p>
<p>Could anyone guide me on how to accomplish this? Are there any Python examples or specific API calls I should look into?</p>
<p>Thank you in advance for your help!</p>

---

## Post #2 by @chir.set (2025-01-28 12:07 UTC)

<aside class="quote no-group" data-username="igi133" data-post="1" data-topic="41334">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/igi133/48/78666_2.png" class="avatar"> igi133:</div>
<blockquote>
<ul>
<li>Set threshold values (e.g., lower and upper bounds).</li>
<li>Preview the thresholded region in real-time on a specific image.</li>
</ul>
</blockquote>
</aside>
<p>You may get some inspiration from <a href="https://gitlab.com/chir-set/Tools7/-/blob/eeccfc6c096e587154b7dcf76a21242f091d5105/ArteryPartsSegmentation/ArteryPartsSegmentation.py#L233" rel="noopener nofollow ugc">this</a> module.</p>

---

## Post #3 by @igi133 (2025-01-31 17:25 UTC)

<p>Thank you for your response! It helped me a lot. Do you happen to have any modules that implement the <strong>Flood Filling</strong> effect and <strong>Keep Selected Island</strong> (from the Islands operation) that I could take inspiration from? It would be great to see how others have approached this topic.</p>

---

## Post #4 by @chir.set (2025-01-31 19:51 UTC)

<aside class="quote no-group" data-username="igi133" data-post="3" data-topic="41334">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/igi133/48/78666_2.png" class="avatar"> igi133:</div>
<blockquote>
<p>any modules that implement</p>
</blockquote>
</aside>
<p>For flood filling: <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/20257daa1965b75f75cbea92a3e32ff77e702516/GuidedArterySegmentation/GuidedArterySegmentation.py#L558" rel="noopener nofollow ugc">1</a>, <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/20257daa1965b75f75cbea92a3e32ff77e702516/QuickArterySegmentation/QuickArterySegmentation.py#L487" rel="noopener nofollow ugc">2</a>.</p>
<p>For ‘Keep selected island’: no known reference. The module I linked in my previous post uses <code>KEEP_LARGEST_ISLAND</code>; if you use<code> KEEP_SELECTED_ISLAND</code>, it should do the trick.</p>

---

## Post #5 by @igi133 (2025-02-01 18:49 UTC)

<p>I’m unsure how to properly capture the click event and translate it into a flood-filling operation. Could someone guide me on how to:</p>
<ol>
<li>Detect a user click in the Slice View.</li>
<li>Retrieve the voxel coordinates of the clicked point.</li>
<li>Apply a flood-filling operation (e.g., using ITK or other available methods).</li>
</ol>
<p>If there are any examples or similar implementations, I would greatly appreciate any references or advice.</p>

---

## Post #6 by @chir.set (2025-02-01 19:26 UTC)

<aside class="quote no-group" data-username="igi133" data-post="5" data-topic="41334">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/igi133/48/78666_2.png" class="avatar"> igi133:</div>
<blockquote>
<ol>
<li>Detect a user click in the Slice View.</li>
<li>Retrieve the voxel coordinates of the clicked point.</li>
<li>Apply a flood-filling operation (e.g., using ITK or other available methods).</li>
</ol>
</blockquote>
</aside>
<p>But the ‘Flood filling’ effect already does that. Your goal is not very clear. If you don’t plan to use the ‘Segment editor’, you’ll have to rewrite much code, a lot of work to achieve robustness and efficiency.</p>

---

## Post #7 by @igi133 (2025-02-03 01:37 UTC)

<p>My plan is to use ‘Segment editor’ but I don`t know how to write the code to let my module use ‘Flood filling’</p>

---

## Post #8 by @igi133 (2025-02-03 12:45 UTC)

<p>To be more precise I want to chose values of ‘Intensity tolerance’ and ‘Neighborhood size’ from widget of my module and then click button in the widget to get ‘Flood filling’ efect from ‘Segment editor’ with those values. I have created something like this for widget:</p>
<h1><a name="p-122065-flood-filling-parameters-1" class="anchor" href="#p-122065-flood-filling-parameters-1" aria-label="Heading link"></a>Flood filling parameters</h1>
<pre><code>    floodFillingCollapsibleButton = ctk.ctkCollapsibleButton()
    floodFillingCollapsibleButton.text = "Flood Filling"
    self.layout.addWidget(floodFillingCollapsibleButton)

    floodFillingFormLayout = qt.QFormLayout(floodFillingCollapsibleButton)

    # Intensity tolerance for flood filling
    self.intensityToleranceSlider = ctk.ctkSliderWidget()
    self.intensityToleranceSlider.minimum = 0
    self.intensityToleranceSlider.maximum = 200  # Adjust based on your data
    self.intensityToleranceSlider.value = 80  # Default value
    self.intensityToleranceSlider.setToolTip("Set the intensity tolerance for flood filling.")
    floodFillingFormLayout.addRow("Intensity Tolerance:", self.intensityToleranceSlider)

    # Neighborhood size for flood filling
    self.neighborhoodSizeSlider = ctk.ctkSliderWidget()
    self.neighborhoodSizeSlider.minimum = 0
    self.neighborhoodSizeSlider.maximum = 10  # Adjust based on your data
    self.neighborhoodSizeSlider.value = 2  # Default value
    self.neighborhoodSizeSlider.setToolTip("Set the neighborhood size for flood filling.")
    floodFillingFormLayout.addRow("Neighborhood Size (mm):", self.neighborhoodSizeSlider)

    # Flood filling button
    self.floodFillButton = qt.QPushButton("Apply Flood Fill")
    self.floodFillButton.toolTip = "Apply flood filling."
    self.floodFillButton.enabled = True
    floodFillingFormLayout.addRow(self.floodFillButton)

    # Connect the Flood Fill button to logic
    self.floodFillButton.connect("clicked(bool)", self.onFloodFillButton)
</code></pre>
<p>And this for calling the efect:</p>
<p><span class="hashtag-raw">#Flood</span> filling<br>
def applyFloodFill(self, inputVolume, intensityTolerance, neighborhoodSize):<br>
if not self.segmentationNode:<br>
print(“No segmentation node found! Please apply thresholding first.”)<br>
return</p>
<pre><code>    if not self.currentSegmentID:
        print("No segment selected! Please create a new segment first.")
        return

    # Get the Segment Editor widget
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)

    if not self.segmentEditorNode:
        self.segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
    segmentEditorWidget.setMRMLSegmentEditorNode(self.segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(self.segmentationNode)
    segmentEditorWidget.setMasterVolumeNode(inputVolume)

    # Set the active effect to "Flood Filling"
    segmentEditorWidget.setActiveEffectByName("Flood filling")
    effect = segmentEditorWidget.activeEffect()

    if not effect:
        print("Failed to activate Flood Filling effect!")
        return

    # Set the parameters for the "Flood Filling" effect
    effect.setParameter("IntensityTolerance", str(intensityTolerance))
    effect.setParameter("NeighborhoodSizeMm", str(neighborhoodSize))

    # Apply the effect to the current segment
    segmentEditorWidget.setCurrentSegmentID(self.currentSegmentID)
    effect.self().onApply()

    print("Applied flood filling to the selected segment.")
</code></pre>
<p>But it is not working. That’s why I wanted to ask for some advice or what I should change to trigger the ‘Flood filling’ effect in the right way</p>

---

## Post #9 by @chir.set (2025-02-03 13:03 UTC)

<aside class="quote no-group" data-username="igi133" data-post="8" data-topic="41334">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/igi133/48/78666_2.png" class="avatar"> igi133:</div>
<blockquote>
<p>But it is not working.</p>
</blockquote>
</aside>
<p>See <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/20257daa1965b75f75cbea92a3e32ff77e702516/QuickArterySegmentation/QuickArterySegmentation.py#L516" rel="noopener nofollow ugc">here</a> to apply the effect.</p>

---
