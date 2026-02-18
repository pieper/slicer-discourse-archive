# Change segmentation oversampling factor

**Topic ID**: 19025
**Date**: 2021-08-02
**URL**: https://discourse.slicer.org/t/change-segmentation-oversampling-factor/19025

---

## Post #1 by @PJ_Yu (2021-08-02 12:44 UTC)

<p>Hello,</p>
<p>I have been trying to mimic SegmentationGeometryWidget in python. In the widget, I can select a segmentation node and give a oversampling factor. After pressing the OK button, I will get a modified segmentation.</p>
<p>I have searched for some python implementation, such as <a href="https://discourse.slicer.org/t/update-oversampling-factor/11717">Update oversampling factor</a> and <a href="https://discourse.slicer.org/t/create-cylinder-shell-shaped-segment/8449">Create cylinder shell shaped segment</a>. However, SetConversionParameter seems not working at all for me.</p>
<p>Here’s my code. Am I doing anything wrong or do I miss anything else? Thank for helping.</p>
<pre><code class="lang-auto"># Create the segmentation, the segmentation is created correctly.
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.SetName('Result')
segmentationNode.CreateDefaultDisplayNodes()
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(inputVolume)
segmentationNode.AddSegmentFromBinaryLabelmapRepresentation(orientedImage, "Segmentation")

#Modify the oversampling factor
segmentationNode.GetSegmentation().SetConversionParameter('Oversampling factor', str(self.oversamplingFactorSpinBox.value))
segmentationNode.GetSegmentation().CreateRepresentation('Binary labelmap', True)
segmentationNode.GetSegmentation().Modified()
segmentationNode.Modified()
</code></pre>
<p>By the way, the reason I tried to code the function is I can’t correctly show the SegmentationGeometryWidget. I have tried to open it based on <a href="https://discourse.slicer.org/t/how-through-python-to-reach-or-open-segmentation-geometry-widget-dialog-or-set-up-parameters-before-opening-a-dialog/8297">How, through python, to reach or open Segmentation-Geometry-Widget dialog or set up parameters before opening a dialog?</a>, but the widget will suddenly open and then close itself.</p>

---

## Post #2 by @lassoan (2021-08-03 13:59 UTC)

<p>Conversion parameters are only used if conversion is performed.</p>
<p>If you have a closed surface master representation then you can delete the binary labelmap representation and then recreate it.</p>
<p>If you already have a binary labelmap representation then you need to resample manually. In latest Slicer Preview Release, we have made manual resampling conveniently available from Python (<code>vtkSlicerSegmentationGeometryLogic::ResampleLabelmapsInSegmentationNode</code> method).</p>

---

## Post #3 by @PJ_Yu (2021-08-03 14:54 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks for your reply!</p>
<p>It’s good to know that there’s a simple way to resample the binary labelmap in preview release. However, I’m afraid I can’t switch to latest Slicer Preview Release due to other issues. My current working version of Slicer is 4.11, is there any code example for manually resample binary labelmap?</p>

---

## Post #4 by @lassoan (2021-08-03 16:34 UTC)

<p>You need to run [all the steps implemented in <code>vtkSlicerSegmentationGeometryLogic::ResampleLabelmapsInSegmentationNode</code> method. See the source code <a href="https://github.com/Slicer/Slicer/blob/4d18c2d3579dea23d142c7d7e9fd80343445273b/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationGeometryLogic.cxx#L476-L527">here</a>.</p>
<p>We’ll soon replace the stable release with the content of the current preview release. What issues prevent you from upgrading?</p>

---

## Post #5 by @PJ_Yu (2021-08-04 09:10 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks for your help again!</p>
<p>The source code of <code>vtkSlicerSegmentationGeometryLogic::ResampleLabelmapsInSegmentationNode</code> is really helpful, and I finally completed this function correctly based on the source code. The issues aren’t technical issues, and since it works right now, there’s no needs to worry about upgrading.</p>
<p>For those who are interested, here is my code.</p>
<pre><code class="lang-python">segmentIDs = vtk.vtkStringArray()
segmentationNode.GetSegmentation().GetSegmentIDs(segmentIDs)

#Create desired geometryImageData with overSamplingFactor
segmentationGeometryLogic = slicer.vtkSlicerSegmentationGeometryLogic()
segmentationGeometryLogic.SetInputSegmentationNode(segmentationNode)
segmentationGeometryLogic.SetSourceGeometryNode(segmentationNode)
segmentationGeometryLogic.SetOversamplingFactor(0.5)
segmentationGeometryLogic.CalculateOutputGeometry()
geometryImageData = segmentationGeometryLogic.GetOutputGeometryImageData()

for index in range(segmentIDs.GetNumberOfValues()):
    currentSegmentID = segmentIDs.GetValue(index)
    currentSegment = segmentationNode.GetSegmentation().GetSegment(currentSegmentID)
    currentLabelmap = currentSegment.GetRepresentation("Binary labelmap")

    success = slicer.vtkOrientedImageDataResample.ResampleOrientedImageToReferenceOrientedImage(currentLabelmap, geometryImageData, currentLabelmap, False, True)

    if not success:
            print("Segment {}/{} failed to be resampled".format(segmentationNode.GetName(), currentSegmentID))

segmentationNode.Modified()
</code></pre>

---

## Post #6 by @jcfr (2023-01-31 16:56 UTC)

<p>2 posts were split to a new topic: <a href="/t/support-for-applying-settings-to-updated-slicer-applicaiton/27562">Support for applying settings to updated Slicer applicaiton</a></p>

---

## Post #7 by @dalv.silvermann (2022-10-14 20:23 UTC)

<p>Thanks a lot!<br>
Fantastic decision!<br>
I’ve inserted some additional lines for my case and the flight is normal!)</p>

---
