---
topic_id: 40388
title: "Help With Blood Vessel Segmentation Module For My Engineerin"
date: 2024-11-26
url: https://discourse.slicer.org/t/40388
---

# Help with Blood Vessel Segmentation Module for My Engineering Thesis

**Topic ID**: 40388
**Date**: 2024-11-26
**URL**: https://discourse.slicer.org/t/help-with-blood-vessel-segmentation-module-for-my-engineering-thesis/40388

---

## Post #1 by @igi133 (2024-11-26 18:12 UTC)

<p>Hello everyone,</p>
<p>I am currently working on my engineering thesis and I am developing a module for 3D Slicer that aims to detect and segment blood vessels from CT scan images. This module will be part of my research project, and my goal is to automate the process of extracting vascular structures from medical imaging data.</p>
<p>At the moment, I am in the early stages of the project, and I have written some code that allows me to segment the blood vessels from CT images. I would greatly appreciate any feedback or suggestions regarding my approach.</p>
<p>Below is the code I have written so far. If anyone has experience with blood vessel segmentation or working with medical image data in 3D Slicer, your help in reviewing and improving this code would be invaluable.</p>
<pre data-code-wrap="python"><code class="lang-python"># Retrieve the volume node
volumeNode = slicer.util.getNode("CTChest")  # Replace with your volume node's actual name

if not volumeNode:
    raise ValueError("Volume node 'CTChest' not found. Check the name and ensure it's loaded into the scene.")

# Create a new segmentation node
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes()  # Ensure display nodes are initialized

# Initialize the Segment Editor
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorWidget.setSegmentationNode(segmentationNode)

# Explicitly set the Master Volume Node
segmentEditorWidget.setMasterVolumeNode(volumeNode)

# Debugging: Ensure the Master Volume Node is set correctly
if not segmentEditorWidget.masterVolumeNode():
    raise RuntimeError("Master volume node is not set correctly in the Segment Editor Widget.")

# Activate the Threshold effect
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()

if effect:
    print("Threshold effect activated successfully!")
    # Set threshold values
    effect.setParameter("MinimumThreshold", "100")  # Replace with your desired lower threshold
    effect.setParameter("MaximumThreshold", "300")  # Replace with your desired upper threshold
    effect.self().onApply()  # Apply the threshold effect
    print("Threshold segmentation applied successfully.")
else:
    raise RuntimeError("Failed to activate the Threshold effect. Check Slicer configuration and plugins.")

# Optional: Smooth the segmentation to refine it
segmentEditorWidget.setActiveEffectByName("Smoothing")
effect = segmentEditorWidget.activeEffect()

if effect:
    effect.setParameter("SmoothingMethod", "Gaussian")
    effect.setParameter("KernelSizeMm", "1.5")
    effect.self().onApply()
    print("Smoothing applied successfully.")
else:
    print("Smoothing effect could not be activated.")

# Finalize (clean up resources)
segmentEditorWidget = None
</code></pre>
<p>Thank you in advance for any help you can provide!</p>

---

## Post #2 by @chir.set (2024-11-26 20:24 UTC)

<p>The qMRMLSegmentEditorWidget needs a vtkMRMLSegmentEditorNode.</p>
<p>An effet needs a segment that you must create <em>and</em> select. Identify the added lines below.</p>
<pre><code class="lang-auto"># Initialize the Segment Editor
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
mrmlSegmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(mrmlSegmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)

# Explicitly set the Master Volume Node
segmentEditorWidget.setMasterVolumeNode(volumeNode)

# Debugging: Ensure the Master Volume Node is set correctly
if not segmentEditorWidget.masterVolumeNode():
    raise RuntimeError("Master volume node is not set correctly in the Segment Editor Widget.")

segmentID = segmentationNode.GetSegmentation().AddEmptySegment()
segmentEditorWidget.setCurrentSegmentID(segmentID)
</code></pre>
<p>Please note that bones have a wide intensity range, that includes the range in the contrast media.</p>

---

## Post #3 by @igi133 (2024-11-27 13:08 UTC)

<p>Thank you for your feedback!</p>
<p>I really appreciate your suggestions and the time you took to help me with my code. Your insights are very helpful, and I’ll definitely implement your recommendations to improve my approach.</p>
<p>I also have a follow-up question: do you think it’s possible to segment only the blood vessels using the threshold function in 3D Slicer? If not, do you have any ideas or suggestions on alternative methods to achieve this? I’m open to exploring different techniques if thresholding alone isn’t sufficient.</p>
<p>Thank you again for your assistance!</p>

---

## Post #4 by @chir.set (2024-11-27 13:31 UTC)

<aside class="quote no-group" data-username="igi133" data-post="3" data-topic="40388">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/igi133/48/78666_2.png" class="avatar"> igi133:</div>
<blockquote>
<p>any ideas or suggestions on alternative methods</p>
</blockquote>
</aside>
<p>You may investigate the “Flood filling” effect of the “Segment editor” with high values of “Intensity tolerance”. Other effects allow an efficient segmentation also, but this one is probably the fastest. No segmentation technique is magic, you’ll have to play a lot and a lot to grasp their offerings and limits.</p>
<p>A few modules of the SlicerVMTK installable extension use the “Flood filling” effect, this time on  targeted regions that you define.</p>
<p>In all cases, you need good quality CT scans with sufficiently contrasted lumen.</p>

---

## Post #5 by @igi133 (2024-11-27 14:52 UTC)

<p>To put it simply, the module I want to create looks as follows in my mind. First, a script would perform segmentation of regions containing blood vessels from a specific CT image. Due to the similarity in grayscale values to bone, the module would need to prompt the user to select the regions of interest.</p>
<p>Next, I need my module to calculate values such as the volume and other related parameters of the blood vessels, and then display the obtained results. Do you have any advice that could help me achieve this?</p>
<p>Currently, the segmentation part works, but it also segments parts of the bone. The image I’m using to test my program is from Slicer and is named <em>CTACArdio</em>. I would be very grateful for any suggestions you might have.</p>

---

## Post #6 by @chir.set (2024-11-27 16:37 UTC)

<aside class="quote no-group" data-username="igi133" data-post="5" data-topic="40388">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/igi133/48/78666_2.png" class="avatar"> igi133:</div>
<blockquote>
<p>I need my module to calculate values</p>
</blockquote>
</aside>
<p>To do that, you must work on segmented blood vessels and segmented blood vessels only. That’s why you want your users to select regions of interest.</p>
<p>With a volume like CTA-cardio and most real-life volumes, thresholding will give you a lumen that will be attached to bones and soft tissues often. Even the ‘Islands’ segment editor effect won’t be of much help, it many remove some detached parts of the segment, called Islands, but you won’t get just nice blood vessels.</p>
<p>You may still use the ‘Scissors’ effect to cut anything that is not an artery but it’s obviously impractical in this use case.</p>
<p>Consider using the ‘Flood filling’ effect with an “Intensity tolerance” of 90 and a “Neighbourhood size” of 2.0. Just click in the abdominal aorta for example and you will see the difference. Your module can ask the user to do that.</p>
<p>Another option is to crop CTA-cardio to a ROI and threshold in that targeted volume.</p>

---

## Post #7 by @igi133 (2024-11-28 16:26 UTC)

<p>Can u tell me what is wrong with activing flood filling effect in this script?</p>
<h1><a name="p-119998-step-2-refine-with-flood-filling-1" class="anchor" href="#p-119998-step-2-refine-with-flood-filling-1" aria-label="Heading link"></a>Step 2: Refine with Flood Filling</h1>
<blockquote>
<blockquote>
<blockquote>
<p>segmentEditorWidget.setActiveEffectByName(“FloodFilling”)<br>
effect = segmentEditorWidget.activeEffect()</p>
<p>if effect:<br>
…     print(“Flood Filling effect activated successfully!”)<br>
…     # Set flood filling parameters<br>
…     effect.setParameter(“IntensityTolerance”, “90”)  # Adjust intensity tolerance<br>
…     effect.setParameter(“NeighborhoodSize”, “2.0”)  # Adjust neighborhood size<br>
…     print(“Click on a vessel in the volume to apply the flood filling effect.”)<br>
…     input(“Press Enter after applying flood filling…”)  # Wait for user interaction<br>
… else:<br>
…     raise RuntimeError(“Failed to activate the Flood Filling effect. Check Slicer configuration and plugins.”)</p>
</blockquote>
</blockquote>
</blockquote>

---

## Post #8 by @chir.set (2024-11-28 17:05 UTC)

<aside class="quote no-group" data-username="igi133" data-post="7" data-topic="40388">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/igi133/48/78666_2.png" class="avatar"> igi133:</div>
<blockquote>
<p>… print(“Click on a</p>
</blockquote>
</aside>
<p>The user must type something or an error will be raised.</p>
<aside class="quote no-group" data-username="igi133" data-post="7" data-topic="40388">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/igi133/48/78666_2.png" class="avatar"> igi133:</div>
<blockquote>
<p>effect.setParameter(“IntensityTolerance”, “90”)</p>
</blockquote>
</aside>
<p>I’m not sure if the values can be passed as string; try with int and float respectively.</p>

---

## Post #9 by @chir.set (2024-11-28 17:08 UTC)

<aside class="quote no-group" data-username="igi133" data-post="7" data-topic="40388">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/igi133/48/78666_2.png" class="avatar"> igi133:</div>
<blockquote>
<p>effect.setParameter(</p>
</blockquote>
</aside>
<p>You could also call</p>
<blockquote>
<p>effect.updateGUIFromMRML()</p>
</blockquote>
<p>after setting the parameters.</p>

---

## Post #10 by @igi133 (2024-11-29 14:35 UTC)

<p>I have changed the code like this but I still have errors, any ideas? # Step 2: Refine with Flood Filling in a new segment</p>
<blockquote>
<blockquote>
<blockquote>
<p>floodFillSegmentID = segmentationNode.GetSegmentation().AddEmptySegment(“FloodFillVessels”)<br>
segmentEditorWidget.setCurrentSegmentID(floodFillSegmentID)</p>
<p>segmentEditorWidget.setActiveEffectByName(“FloodFilling”)<br>
effect = segmentEditorWidget.activeEffect()</p>
<p>if effect:<br>
…     print(“Flood Filling effect activated successfully!”)<br>
…<br>
…     # Set flood filling parameters with int and float values<br>
…     intensity_tolerance = 90  # Intensity tolerance as integer<br>
…     neighborhood_size = 2.0   # Neighborhood size as float<br>
…<br>
…     effect.setParameter(“IntensityTolerance”, intensity_tolerance)  # Use int for IntensityTolerance<br>
…     effect.setParameter(“NeighborhoodSize”, neighborhood_size)      # Use float for NeighborhoodSize<br>
…<br>
…     effect.updateGUIFromMRML()  # Synchronize GUI with parameters<br>
…     print(“Click on a vessel in the volume to apply the flood filling effect.”)<br>
…<br>
…     # Pause for user interaction<br>
…     input(“Press Enter after completing the flood filling interaction…”)<br>
… else:<br>
…     raise RuntimeError(“Failed to activate the Flood Filling effect. Check Slicer configuration and plugins.”)</p>
</blockquote>
</blockquote>
</blockquote>

---

## Post #11 by @chir.set (2024-11-29 15:13 UTC)

<aside class="quote no-group" data-username="igi133" data-post="10" data-topic="40388">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/igi133/48/78666_2.png" class="avatar"> igi133:</div>
<blockquote>
<p>any ideas?</p>
</blockquote>
</aside>
<p>Replace “FloodFilling” by “Flood filling”.</p>
<p>Also, ask the user to type something before pressing enter, else an EOL error will be raised. Just after this ‘input’ line, use setActiveEffect(None).</p>
<p>BTW, you seem to be targeting power users since your code should run in the Python console so that they get a chance to press enter. I don’t know what is the design of your research but it should not imply the console. You could add a button in your UI to restore the active effect to None rather. That part is however totally your design and target audience.</p>

---
