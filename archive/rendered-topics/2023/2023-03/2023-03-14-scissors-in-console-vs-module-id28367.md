# Scissors in console vs module

**Topic ID**: 28367
**Date**: 2023-03-14
**URL**: https://discourse.slicer.org/t/scissors-in-console-vs-module/28367

---

## Post #1 by @pearsonm (2023-03-14 03:16 UTC)

<p>Hi,<br>
I am writing a module where I need to use threshold and scissors from the Segment Editor.</p>
<p>If I run the following code in the console it works as expected and I can draw the ROI but when I copy the code to my module, the thresholding is done and the cursor changes to the scissor icon but I cannot create the ROI. Any suggestions?</p>
<pre><code class="lang-auto">masterVolumeNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')

# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

# Create temporary segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setSourceVolumeNode(masterVolumeNode)

addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("t_stomach")
segmentEditorNode.SetSelectedSegmentID(addedSegmentID)

segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold","0")
effect.self().onApply()

segmentEditorWidget.setActiveEffectByName("Scissors")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("Operation","EraseOutside")
effect.setParameter("Shape","FreeForm")
</code></pre>

---

## Post #2 by @pearsonm (2023-03-14 03:45 UTC)

<p>If I put my code in a function on the console I have the same behavior so I need to pause for user input inside the function. What is the best way to do that?</p>

---

## Post #3 by @Honeee (2023-07-31 09:58 UTC)

<p>Hello Mark, I have the same issue.<br>
I’m using application startup script from Slicer. From my pyhton script, I managed to perform a few segmentation operations such as Tresholding and Smoothing, but then I’d like to create a rectangle shape from scissors and then Erase Outside.</p>
<p>I keep having the same mistake :<br>
AttributeError: qSlicerSegmentEditorScissorsEffect has no attribute named ‘onApply’</p>
<p>Did you manage to go further ?</p>

---

## Post #4 by @lassoan (2023-07-31 17:18 UTC)

<p>Scissors effect is an ineractive effect. How would you use it without user input?</p>

---

## Post #5 by @pearsonm (2023-07-31 22:42 UTC)

<p>I did make my code work by adding a pause after setting the Draw effect</p>
<pre><code class="lang-auto">        segmentEditorWidget.setActiveEffectByName("Draw")
        try:
            input("continue:")
        except:
            pass
</code></pre>
<p>which pauses further processing until the user presses the enter key in the python console.</p>
<p>I didn’t like this solution so now the user adds a markup ROI and then a binary mask is created from the markup points. Our images are very low resolution so using markups allows the user to adjust the ROI until they are satisfied with the result.</p>

---

## Post #6 by @Honeee (2023-08-01 09:14 UTC)

<p>Ok I understand and that’s what I thought.<br>
However, I was wondering if it could be possible with a python scrip because I read topic “Scissors segment editor effects from a script” and thought it could be possible to draw a shape (a rectangle for instance) inside a segment and then erase outside the shape.<br>
Tell me if i’m wrong or if I missunderstood.</p>

---

## Post #7 by @pearsonm (2023-08-02 00:12 UTC)

<p>Here is a complete example. As previously mentioned, I could not work out how to avoid using keyboard input in the python console and using markups is better in my application.</p>
<pre><code class="lang-auto">def makeMaskedVol(volumeNode):
    if volumeNode is None:
        return
    maskedVolume = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", "maskedvol")
    segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode", "testSegment")
    segmentationNode.CreateDefaultDisplayNodes() # only needed for display
    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(volumeNode)

    # Create temporary segment editor to get access to effects
    segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(segmentationNode)
    segmentEditorWidget.setSourceVolumeNode(volumeNode)

    addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment()
    segmentEditorNode.SetSelectedSegmentID(addedSegmentID)

    segmentEditorWidget.setActiveEffectByName("Threshold")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("MinimumThreshold","0")
    effect.self().onApply()
    segmentationNode.GetDisplayNode().SetOpacity(0.4)

    segmentEditorWidget.setActiveEffectByName("Scissors")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("Operation","EraseOutside")
    effect.setParameter("Shape","FreeForm")
    try:
        input("continue:")
    except:
        pass
    segmentEditorWidget.setActiveEffectByName("Mask volume")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("BinaryMaskFillValueInside","1")
    effect.setParameter("BinaryMaskFillValueOutside","0")
    effect.setParameter("FillValue","0")
    effect.setParameter("InputVisibility","True")
    effect.setParameter("Operation","FILL_OUTSIDE")
    effect.self().outputVolumeSelector.setCurrentNode(maskedVolume)
    effect.self().onApply()
    return segmentationNode

</code></pre>

---
