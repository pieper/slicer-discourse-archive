# Scissors segment editor effects from a script

**Topic ID**: 8348
**Date**: 2019-09-09
**URL**: https://discourse.slicer.org/t/scissors-segment-editor-effects-from-a-script/8348

---

## Post #1 by @giovform (2019-09-09 17:36 UTC)

<p>Hello, I am using <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" rel="nofollow noopener">this</a> script example and its already working fine for the threshold step I needed to segment my data. I need also to apply the Scissors circle effect, <strong>from the axial view</strong>, using the following options:</p>
<ul>
<li>operation: erase outside;</li>
<li>shape: circle</li>
<li>slice cut: unlimited</li>
</ul>
<p>I already have the coordinates for the circle center and it’s radius.</p>
<p>I apologise if I am asking too much, but I am new to the software and don’t know where to look for the options names like: effect.setParameter(“MinimumThreshold”, …) that are in the example script.</p>
<p>Thank you in advance,</p>
<p>Giovanni</p>

---

## Post #2 by @lassoan (2019-09-09 17:44 UTC)

<p>You can print all Segment Editor effect parameter names by typing this into the Python console:</p>
<pre><code>print(slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentEditorNode"))
</code></pre>
<p>You should get something like this:</p>
<pre><code class="lang-auto">vtkMRMLSegmentEditorNode (000001867E52D360)
  ID: vtkMRMLSegmentEditorNodeSegmentEditor
  ClassName: vtkMRMLSegmentEditorNode
  Name: SegmentEditor
  Debug: false
  MTime: 1527281
  Description: (none)
  SingletonTag: SegmentEditor
  HideFromEditors: true
  Selectable: true
  Selected: false
  UndoEnabled: false
  Attributes:
    BrushAbsoluteDiameter:25
    BrushAbsoluteMaximumDiameter:128
    BrushAbsoluteMinimumDiameter:0.5
    BrushDiameterIsRelative:1
    BrushMaximumAbsoluteDiameter:100
    BrushMinimumAbsoluteDiameter:0.01
    BrushPixelMode:0
    BrushRelativeDiameter:3
    BrushSphere:0
    EditIn3DViews:0
    Erase.ColorSmudge:0
    Erase.EraseAllSegments:0
    Fill between slices.AutoUpdate:1
    Grow from seeds.AutoUpdate:1
    Hollow.ShellMode:INSIDE_SURFACE
    Hollow.ShellThicknessMm:3
    Islands.MinimumSize:1000
    Islands.Operation:KEEP_LARGEST_ISLAND
    Logical operators.BypassMasking:1
    Logical operators.Operation:COPY
    Margin.MarginSizeMm:3
    Paint.ColorSmudge:0
    Paint.EraseAllSegments:0
    Scissors.Operation:EraseInside
    Scissors.Shape:FreeForm
    Scissors.SliceCutDepthMm:0
    Scissors.SliceCutMode:Unlimited
    Smoothing.GaussianStandardDeviationMm:3
    Smoothing.JointTaubinSmoothingFactor:0.5
    Smoothing.KernelSizeMm:3
    Smoothing.SmoothingMethod:MEDIAN
    Threshold.AutoThresholdMethod:OTSU
    Threshold.AutoThresholdMode:SET_LOWER_MAX
    Threshold.MaximumThreshold:279
    Threshold.MinimumThreshold:69.75
  Node references:
    masterVolumeRef: vtkMRMLScalarVolumeNode5
    segmentationRef: vtkMRMLSegmentationNode1
  SelectedSegmentID: Segment_1
  ActiveEffectName: 
  MaskMode: PaintAllowedEverywhere
  MaskSegmentID: 
  OverwriteMode: OverwriteAllSegments
  MasterVolumeIntensityMask: false
  MasterVolumeIntensityMaskRange: 0 0
</code></pre>
<p>You can find valid parameter values by looking at the source code of the effects (e.g., search for the parameter name in entire Slicer core or SegmentEditorExtraEffects extension source code).</p>

---

## Post #3 by @giovform (2019-09-09 18:20 UTC)

<p>Thank you Andras. I still stuck on how to emulate the event of creating a circle at a specific locaion (in the red panel for example), with a specific radius. From what I understood, the processInteractionEvents() function is called after the user has drawn his segmentation, but I wanted to do it inside the script direcly, emulating this action.</p>

---

## Post #4 by @lassoan (2019-09-09 18:36 UTC)

<p>You can certainly call <code>processInteractionEvents()</code> to simulate user interaction, but it is a very low-level API, which may not be appropriate for a module to call.</p>
<p>What would you like to achieve? Simulate drilling?</p>

---

## Post #5 by @giovform (2019-09-09 18:51 UTC)

<p>I did a threshold segmentation on my data, and ended up with two cylinders. One is hollow and is enclosing the other, but they still have small points of contact. The best way to separate them is to use the scissors from the axial view and since I have the diameter of the internal cylinder and it’s center, it would be nice to have a one click operation, instead of manually trying to draw the best circle.</p>
<p>In the end, I just want exclude the region of my segmentation beyond some radius r, centered at some (x ,y), for all slices (the cylinders are oriented in SI axis).</p>

---

## Post #6 by @lassoan (2019-09-09 19:24 UTC)

<p>For this, it would be more appropriate to create a cylinder using <a href="https://vtk.org/doc/nightly/html/classvtkCylinderSource.html" rel="nofollow noopener">vtkCylinderSource</a>, import into the segmentation node, and use Logical operators effect to subtract it from the segment of interest. See first steps of <a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b" rel="nofollow noopener">this example</a> to see how to create a segment using a VTK source and import it into a segmentation node.</p>

---

## Post #7 by @giovform (2019-09-10 16:40 UTC)

<p>Thanks again Andras. I did what you told. So now I have:</p>
<ul>
<li>
<p>a threshold segment, that selects two cylinders from my data (a hollow one enclosing a smaller one, separated by a little gap);</p>
</li>
<li>
<p>and the newly created cylinder segment from the vtkCylinderSource, that is located in between the two threshold segment cylinders;</p>
</li>
</ul>
<p>I want to now exclude the external hollow cylinder segment, using the newly created cylinder segment located in between the two. You mentioned the use of logical operators… do you have any examples of how can I do that? Thank you very much.</p>
<p>Giovanni</p>

---

## Post #8 by @lassoan (2019-09-10 17:17 UTC)

<p>Examples for using segmentations and segment editor from Python scripts: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations </a>. You’ll activate the Logical operators effect, set its parameters, and call its Apply method.</p>

---

## Post #9 by @giovform (2019-09-11 14:01 UTC)

<p>I noticed that the cylinder I createad using CreateClosedSurfaceRepresentation following your hint is showing up in the 3D view, but it is not applied as a segmentation. How can I use it to segment everything inside? I tried tu use as a mask also, but no success. The last step in the code was:</p>
<pre><code>    segmentationNode.CreateClosedSurfaceRepresentation()</code></pre>

---

## Post #10 by @lassoan (2019-09-11 14:16 UTC)

<p>If you create a model node and you want to use it as a segment then then you need to <a href="https://apidocs.slicer.org/v4.8/classvtkSlicerSegmentationsModuleLogic.html#a19cdf27aa9e1068d6b39221600086f35" rel="nofollow noopener">import it into the segmentation</a>.</p>
<p>If you create a vtkPolyData using a VTK source then you can add it as a segment as shown in this example: <a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b#file-segmentgrowcutsimple-py-L16-L21" rel="nofollow noopener">https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b#file-segmentgrowcutsimple-py-L16-L21</a></p>

---

## Post #11 by @giovform (2019-09-11 14:22 UTC)

<p>I did exactly that, but it does’t segment nothing, it just shows the cylinder in the 3D view (because I also called segmentationNode.CreateClosedSurfaceRepresentation()), with no segmentation in the slice panels.</p>
<p>Here is my code:</p>
<pre><code>    # Cylinder for separation of the core from its casing
    segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
    segmentationNode.CreateDefaultDisplayNodes()
    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(inputVolume)
    segmentationCylinder = vtk.vtkCylinderSource()
    segmentationCylinder.SetRadius(coreDiameter / 2)
    segmentationCylinder.SetHeight(len(slicer.util.arrayFromVolume(inputVolume)) * self.imageSpacing[2] * 1.5)
    segmentationCylinder.SetResolution(100)
    segmentationNode.AddSegmentFromClosedSurfaceRepresentation(segmentationCylinder.GetOutput(), "Core", [0.0, 1.0, 0.0])
    segmentationCylinder.Update()</code></pre>

---

## Post #12 by @giovform (2019-09-11 14:29 UTC)

<p>Ok. Now it is working. I was calling Update() after adding it. The correct way is:</p>
<pre><code>    segmentationCylinder.Update()
    segmentationNode.AddSegmentFromClosedSurfaceRepresentation(segmentationCylinder.GetOutput(), "Core", [0.0, 1.0, 0.0])
</code></pre>
<p>Thank you Andras.</p>

---

## Post #13 by @giovform (2019-09-17 16:03 UTC)

<p>Andras, what is the proper way to set this parameter: MasterVolumeIntensityMaskRange</p>
<p>I tried:</p>
<pre><code>    effect.setParameter("MasterVolumeIntensityMaskRange", "(-1000, 0)")
</code></pre>
<p>or</p>
<pre><code>    effect.setParameter("MasterVolumeIntensityMaskRange", "-1000 0")
</code></pre>
<p>but no success.</p>
<p>I want to use with the Mask Volume effect.</p>

---

## Post #14 by @lassoan (2019-09-17 16:10 UTC)

<p>Masking parameters are not effect parameters. They are stored directly in the segment editor node and you can change them like this: <code>getNode('SegmentEditor').SetMasterVolumeIntensityMaskRange(15, 80)</code></p>

---

## Post #15 by @giovform (2019-09-17 16:40 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="8348">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>print(slicer.mrmlScene.GetFirstNodeByClass(“vtkMRMLSegmentEditorNode”))</p>
</blockquote>
</aside>
<p>Still not being able to make it take effect:</p>
<pre><code>    segmentEditorNode.SetMaskSegmentID(segmentationNode.GetSegmentation().GetNthSegmentID(0))
    segmentEditorNode.SetMasterVolumeIntensityMask(True)
    segmentEditorNode.SetMasterVolumeIntensityMaskRange(-3000, -2800)
</code></pre>
<p>Is there anything else I have to set up?</p>

---

## Post #16 by @lassoan (2019-09-17 17:20 UTC)

<p>Probably you don’t want to use both a segment as a mask and also an intensity range. What would you like to do? Blank out parts of the original volume?</p>
<p>Also note that you may have several segment editor nodes in the scene. One is created by Segment Editor module but you may have created several others.</p>

---

## Post #17 by @giovform (2019-09-17 17:45 UTC)

<p>I would like to apply both with the same segment, yes. I can do it manually, using the segmentation editor, but in the code I still can’t replicate the intensity range effect. I will post here the sequence of commands I am currently running (I have only one segmentation):</p>
<pre><code>    # Create segment editor to get access to effects
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
    slicer.mrmlScene.AddNode(segmentEditorNode)
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(segmentationNode)
    segmentEditorWidget.setMasterVolumeNode(inputVolume)

    segmentEditorWidget.setCurrentSegmentID(segmentationNode.GetSegmentation().GetNthSegmentID(0))
    # Set up masking parameters
    segmentEditorWidget.setActiveEffectByName("Mask volume")
    effect = segmentEditorWidget.activeEffect()
    segmentEditorNode.SetMaskSegmentID(segmentationNode.GetSegmentation().GetNthSegmentID(0))
    segmentEditorNode.SetMasterVolumeIntensityMask(True)
    segmentEditorNode.SetMasterVolumeIntensityMaskRange(6900, 7000)
    effect.setParameter("Operation", "FILL_OUTSIDE")
    effect.setParameter("FillValue", str(inputVolume.GetImageData().GetScalarRange()[0]))
    maskedVolume = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", "Temporary masked volume")
    effect.self().outputVolumeSelector.setCurrentNode(maskedVolume)
    effect.self().onApply()
</code></pre>
<p>The FillValue parameter is working.</p>

---

## Post #18 by @lassoan (2019-09-17 17:49 UTC)

<p>You can debug the issue by showing the segmentEditorWidget (<code>segmentEditorWidget.show()</code>) and see what parameter is not set as you expected.</p>

---

## Post #19 by @giovform (2019-09-17 17:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="18" data-topic="8348">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>segmentEditorWidget.show()</p>
</blockquote>
</aside>
<p>I tried that, but unfortunately it closes soon after opening, before it can display anything. Maybe has something to do with the version I am currently running? Will try with the latest nightly.</p>

---

## Post #20 by @lassoan (2019-09-17 18:44 UTC)

<aside class="quote no-group" data-username="giovform" data-post="19" data-topic="8348">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovform/48/4687_2.png" class="avatar"> giovform:</div>
<blockquote>
<p>I tried that, but unfortunately it closes soon after opening</p>
</blockquote>
</aside>
<p>The widget is hidden when the variable is deleted. To prevent this, you can run the code from the console or store a reference to the widget a variable that is not deleted (e.g., add this line <code>slicer.savedWidget = segmentEditorWidget</code>).</p>

---

## Post #21 by @lassoan (2021-06-04 13:38 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-split-segmentation-the-islands/17952">How to split segmentation the islands?</a></p>

---

## Post #22 by @Saima (2022-09-09 03:02 UTC)

<p>Hi Andras,<br>
How to get the parameter value of the OTSU method for thresholding an image</p>

---
