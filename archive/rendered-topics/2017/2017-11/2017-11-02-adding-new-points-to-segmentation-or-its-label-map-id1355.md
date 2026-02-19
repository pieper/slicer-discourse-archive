---
topic_id: 1355
title: "Adding New Points To Segmentation Or Its Label Map"
date: 2017-11-02
url: https://discourse.slicer.org/t/1355
---

# Adding new points to segmentation (or its label map)

**Topic ID**: 1355
**Date**: 2017-11-02
**URL**: https://discourse.slicer.org/t/adding-new-points-to-segmentation-or-its-label-map/1355

---

## Post #1 by @mschumaker (2017-11-02 17:04 UTC)

<p>I have a list of RAS points I would like to assign to a pre-existing segment, either directly or via a label map. I looked at what’s in the nightly script repository, and it doesn’t appear to cover this situation.<br>
I like the design of the segmentation nodes. I noticed that the label map associated with a segment has a minimal size. If there is only one labelled voxel, the array associated with the segment’s label map will only have one element.<br>
Given this, I don’t know how to add a new point to a segment. I assume the array needs to be resized, and a new transform assigned. Is there a method that accomplishes this? How do the paint tools accomplish this?<br>
Thanks.</p>

---

## Post #2 by @lassoan (2017-11-02 17:26 UTC)

<p>If you implement this in a segment editor effect then you can use <code>modifySelectedSegmentByLabelmap</code> method (most effects use this method to modify segments).</p>
<p>If you need to modify a segment from outside of a segment editor effect, then probably the easiest is to add a new segment (that has an image data with the additional voxels painted) and add it to the existing segment by using Logical effect. Or, just use vtkImagePadFilter to change extents of your image data (no need to change origin or apply any transform, as only the image extents will be changed; having negative extents are completely fine).</p>

---

## Post #3 by @cpinter (2017-11-02 17:46 UTC)

<p>In the second case <a class="mention" href="/u/lassoan">@lassoan</a> mentions, instead of the vtkImagePadFilter you can use the convenience function vtkOrientedImageDataResample::PadImageToContainImage if imakes it easier.</p>

---

## Post #4 by @mschumaker (2017-11-06 18:31 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/cpinter">@cpinter</a> for your help. I’ve made some progress, but could still use some assistance.<br>
Ultimately, what I’m doing is creating a new segmentation based on another segmentation, so the filtered one is fully contained in the range defined by the original. The original one is created using editor effects, while the filtered one is intended to appear automatically over it. Obtaining the points to assign to the filtered segmentation as a list of RAS points may not have been the best approach, but it’s the path I started down.<br>
The first question I have is about the result: I get a grouping of points with individual boundaries drawn around them. I don’t know how to turn the result into a segmentation with one overall boundary. An image is attached.<br>
The second question I have is about the efficiency of my approach. Is there a better way to accomplish what this method does?<br>
Thanks again.</p>
<pre><code>def NewAssignPointsToSegmentation(self, listOfPoints, originSegNodeID, originSegNumber, destinationSegNodeID, destinationSegNumber):
    """Assign a value at the given points in the segment with the given ID in the destination segmentation node."""
    if(len(listOfPoints)==0):
        #Clear the destination segment
        return self.ClearSegmentation(destinationSegNodeID, destinationSegNumber)
        
    #Get origin node
    originSegNode = slicer.util.getNode(originSegNodeID) #type is vtkMRMLSegmentationNode
    #... error checks
    #Access the origin segment number specified in the parameter list
    originSegmentation = originSegNode.GetSegmentation() #type is vtkSegmentation
    originSegmentID = originSegmentation.GetNthSegmentID(originSegNumber)

    #Get destination node
    destinationSegNode = slicer.util.getNode(destinationSegNodeID) #type is vtkMRMLSegmentationNode
    #... error checks
    #Access the origin segment number specified in the parameter list
    destinationSegmentation = destinationSegNode.GetSegmentation() #type is vtkSegmentation
    destinationSegmentID = destinationSegmentation.GetNthSegmentID(destinationSegNumber)

    #Segmentations module logic class (for static methods access)
    segmentationsLogic = slicer.modules.segmentations.logic()

    #Get the oriented image data for the originSegNode
    originLabelMapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
    segmentationsLogic.ExportAllSegmentsToLabelmapNode(originSegNode, originLabelMapVolumeNode)
    originOrientedImage = segmentationsLogic.CreateOrientedImageDataFromVolumeNode(originLabelMapVolumeNode)

    #Create the label node for the destination for the duration of this method
    destinationLabelMapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
    segmentationsLogic.ExportAllSegmentsToLabelmapNode(destinationSegNode, destinationLabelMapVolumeNode)
    destinationOrientedImage = segmentationsLogic.CreateOrientedImageDataFromVolumeNode(destinationLabelMapVolumeNode)
    
    #Increase the size of the destination image
    vtkSegmentationCore.vtkOrientedImageDataResample.PadImageToContainImage(destinationOrientedImage, originOrientedImage, destinationOrientedImage)
    #Fill destination image with zeros
    vtkSegmentationCore.vtkOrientedImageDataResample.FillImage(destinationOrientedImage, 0)

    #Get transform matrices
    IJKToRASMatrix = vtk.vtkMatrix4x4()
    originLabelMapVolumeNode.GetIJKToRASMatrix(IJKToRASMatrix)
    RASToIJKMatrix = vtk.vtkMatrix4x4()
    RASToIJKMatrix.DeepCopy(IJKToRASMatrix)
    RASToIJKMatrix.Invert()

    #Set new transform matrix for the destination oriented image
    destinationOrientedImage.SetImageToWorldMatrix(IJKToRASMatrix)

    valueToAssign = 1.0
    #Add points to the destination oriented image
    for labelPoint in listOfPoints:
        rasPos = list(labelPoint[:3])
        rasPos.append(1)
        ijkPos = RASToIJKMatrix.MultiplyPoint(rasPos)
        #Get IJK indices
        i = int(round(ijkPos[0],0))
        j = int(round(ijkPos[1],0))
        k = int(round(ijkPos[2],0))
        destinationOrientedImage.SetScalarComponentFromDouble(i,j,k,0,valueToAssign)

    #Assign back to the segment given by destinationSegmentID
    modeReplace = slicer.modules.segmentations.logic().MODE_REPLACE
    destinationExtent = originLabelMapVolumeNode.GetImageData().GetExtent()
    slicer.modules.segmentations.logic().SetBinaryLabelmapToSegment(destinationOrientedImage, destinationSegNode, destinationSegmentID, modeReplace, destinationExtent)
    destinationSegNode.Modified()

    #Clean up - delete the label map nodes
    if(originLabelMapVolumeNode is not None):
        slicer.mrmlScene.RemoveNode(originLabelMapVolumeNode)
    if(destinationLabelMapVolumeNode is not None):
        slicer.mrmlScene.RemoveNode(destinationLabelMapVolumeNode)
    return True
#end NewAssignPointsToSegmentation
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/792685698b0a52681f4ccc336210f5f7dc44dd88.png" data-download-href="/uploads/short-url/hhKiULrGRW5I3F8v1FFVLiOU0Oc.png?dl=1" title="individual-pixels" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/792685698b0a52681f4ccc336210f5f7dc44dd88_2_569x500.png" alt="individual-pixels" data-base62-sha1="hhKiULrGRW5I3F8v1FFVLiOU0Oc" width="569" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/792685698b0a52681f4ccc336210f5f7dc44dd88_2_569x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/792685698b0a52681f4ccc336210f5f7dc44dd88.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/792685698b0a52681f4ccc336210f5f7dc44dd88.png 2x" data-dominant-color="819287"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">individual-pixels</span><span class="informations">698×613 61.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @mschumaker (2017-11-08 15:43 UTC)

<p>Do you know what may cause the boundary pixellation in the image I added?<br>
Thanks.</p>

---

## Post #6 by @lassoan (2017-11-08 16:04 UTC)

<p>Can you take a screenshot of the Segmentations module GUI to see what visualization settings you have there?</p>

---

## Post #7 by @mschumaker (2017-11-08 16:42 UTC)

<p>Ok. Here is the whole screen, with the Segmentations module at right. Do you need to see the Segment Editor GUI as well?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19253b13d88883e34c79604f32a8e0e903d05578.jpeg" data-download-href="/uploads/short-url/3ArHBzbXfNqWaHc2NwGsDRlsAm4.jpg?dl=1" title="screen-with-segmentations" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/19253b13d88883e34c79604f32a8e0e903d05578_2_690x388.jpg" alt="screen-with-segmentations" data-base62-sha1="3ArHBzbXfNqWaHc2NwGsDRlsAm4" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/19253b13d88883e34c79604f32a8e0e903d05578_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/19253b13d88883e34c79604f32a8e0e903d05578_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/19253b13d88883e34c79604f32a8e0e903d05578_2_1380x776.jpg 2x" data-dominant-color="A5A9AE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screen-with-segmentations</span><span class="informations">1920×1080 589 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2017-11-08 17:24 UTC)

<p>Display section in the Segmentations module widget is disabled. It either means that you don’t have a display node for your segmentation or there is something wrong with this widget. What do you see if you switch to Segmentations module? Is Display section disabled there, too? How does the segmentation looks in 3D and in other slice views?</p>

---

## Post #9 by @mschumaker (2017-11-08 17:38 UTC)

<p>You’re right, if I switch to the Segmentations module, the display section is enabled.<br>
I don’t see the segmentations on 3D, and it is unable to convert any of them to closed surfaces.<br>
It’s quite possible I’m doing something wrong with the display nodes. I am not sure how to handle those. I’ll post my segmentation configuration method.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af6e7ac0cff497036b2e1902ac3ade280d003663.jpeg" data-download-href="/uploads/short-url/p1Wg1XMrjPpKqalsi1IFSfpOmAP.jpg?dl=1" title="screen-with-segmentations" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/af6e7ac0cff497036b2e1902ac3ade280d003663_2_690x408.jpg" alt="screen-with-segmentations" data-base62-sha1="p1Wg1XMrjPpKqalsi1IFSfpOmAP" width="690" height="408" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/af6e7ac0cff497036b2e1902ac3ade280d003663_2_690x408.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/af6e7ac0cff497036b2e1902ac3ade280d003663_2_1035x612.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/af6e7ac0cff497036b2e1902ac3ade280d003663_2_1380x816.jpg 2x" data-dominant-color="929291"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screen-with-segmentations</span><span class="informations">1651×977 375 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @mschumaker (2017-11-08 17:40 UTC)

<pre><code>def ConfigureSegmentations(self):
    """Configure the Segmentation nodes used in this module."""
    SSFPSegmentationColor = self.ConfigureSegmentationColor('muscle')
    UTETissueSegmentationColor = self.ConfigureSegmentationColor('tissue')
    UTEFasciaOnlySegmentationColor = self.ConfigureSegmentationColor('connective tissue')

    #Create the segmentation nodes
    self.SSFPSegmentationNode = slicer.vtkMRMLSegmentationNode()
    self.UTETissueSegmentationNode = slicer.vtkMRMLSegmentationNode()
    self.UTEFasciaOnlySegmentationNode = slicer.vtkMRMLSegmentationNode()

    slicer.mrmlScene.AddNode(self.SSFPSegmentationNode)
    slicer.mrmlScene.AddNode(self.UTETissueSegmentationNode)
    slicer.mrmlScene.AddNode(self.UTEFasciaOnlySegmentationNode)

    self.SSFPSegmentationNode.CreateDefaultDisplayNodes()
    self.UTETissueSegmentationNode.CreateDefaultDisplayNodes()
    self.UTEFasciaOnlySegmentationNode.CreateDefaultDisplayNodes()

    SSFPVolumeNode = self.GetSSFPVolumeNodeReference()
    UTEVolumeNode = self.GetUTEVolumeNodeReference()
    self.SSFPSegmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(SSFPVolumeNode)
    self.UTETissueSegmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(UTEVolumeNode)
    self.UTEFasciaOnlySegmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(UTEVolumeNode)
    
    SSFPSegmentation = self.SSFPSegmentationNode.GetSegmentation()
    UTETissueSegmentation = self.UTETissueSegmentationNode.GetSegmentation()
    UTEFasciaOnlySegmentation = self.UTEFasciaOnlySegmentationNode.GetSegmentation()

    self.SSFPSegID = SSFPSegmentation.GenerateUniqueSegmentID('SSFPSeg')
    self.UTETissueSegID = UTETissueSegmentation.GenerateUniqueSegmentID('UTETissueSeg')
    self.UTEFasciaOnlySegID = UTEFasciaOnlySegmentation.GenerateUniqueSegmentID('UTEFasciaSeg')
    
    verifySSFP = SSFPSegmentation.AddEmptySegment(self.SSFPSegID, 'sartorial', SSFPSegmentationColor)
    verifyUTETissue = UTETissueSegmentation.AddEmptySegment(self.UTETissueSegID, 'tissuelabel', UTETissueSegmentationColor)
    verifyUTEFasciaOnly = UTEFasciaOnlySegmentation.AddEmptySegment(self.UTEFasciaOnlySegID, 'fascia', UTEFasciaOnlySegmentationColor)

#end ConfigureSegmentations</code></pre>

---

## Post #11 by @cpinter (2017-11-08 17:49 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="9" data-topic="1355">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>unable to convert any of them to closed surfaces</p>
</blockquote>
</aside>
<p>What do you mean? How do you try and what happens instead? Is there an error message?</p>

---

## Post #12 by @mschumaker (2017-11-08 17:53 UTC)

<p>In the Representations box in the Segmentations module, if I click on Create, and then Convert in the dialog box that appears, I get a message box saying “Failed to convert Segmentation to Closed surface!”</p>

---

## Post #13 by @mschumaker (2017-11-08 18:01 UTC)

<p>Sorry, Create, then Update, then Convert.</p>

---

## Post #14 by @mschumaker (2017-11-08 18:08 UTC)

<p>I just noticed something interesting. Not all of the pixels are isolated. There are some pairs. In this slice, I can see two pairs.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d655f3e8b6ada38ea0c4965039e1b689fc45c08f.png" data-download-href="/uploads/short-url/uA6kyO6ptfGuY59RAqX6J1U4TOn.png?dl=1" title="pairs" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d655f3e8b6ada38ea0c4965039e1b689fc45c08f_2_383x500.png" alt="pairs" data-base62-sha1="uA6kyO6ptfGuY59RAqX6J1U4TOn" width="383" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d655f3e8b6ada38ea0c4965039e1b689fc45c08f_2_383x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d655f3e8b6ada38ea0c4965039e1b689fc45c08f_2_574x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d655f3e8b6ada38ea0c4965039e1b689fc45c08f.png 2x" data-dominant-color="475551"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pairs</span><span class="informations">602×784 64.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @cpinter (2017-11-08 18:27 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="13" data-topic="1355">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>Create, then Update, then Convert</p>
</blockquote>
</aside>
<p>You only need to click Create. Update is used for specifying conversion settings, such as smoothing. Do you do something like this?<br>
The log file would help a lot to identify why conversion failed.</p>
<p>Also your data seems wrong overall. If you could send a scene (mrb) what would clear things up.</p>

---

## Post #16 by @mschumaker (2017-11-08 18:37 UTC)

<p>Ok. Am I able to attach it here, or should I email it to you?<br>
The code used to create the fascia segmentation is in an earlier post. There are many things that could be wrong with how I’m creating it. If you can see a better way to do this, I’d be happy to fix it.</p>

---

## Post #17 by @cpinter (2017-11-08 19:14 UTC)

<p>I got the scene via email, thanks! There are two problems:</p>
<ol>
<li>The scalar range of binary labelmap in the segment ‘fascia’ is not (0,1) as expected, but (0,254). I did a threshold like this to fix it (I was very sloppy with variable names etc, but you get the gist):</li>
</ol>
<pre><code class="lang-auto">    s=getNode('Segmentation_2')
    im=s.GetBinaryLabelmapRepresentation('UTEFasciaSeg')
    im.GetScalarRange() # Will be (0.0, 254.0)
    t=vtk.vtkImageThreshold()
    t.SetInputData(im)
    t.ThresholdByUpper(1)
    t.SetInValue(1)
    t.Update()
    im2=t.GetOutput()
    im2.GetScalarRange() # Will be (0.0, 1.0)
    im.DeepCopy(im2)
</code></pre>
<ol start="2">
<li>The 3D viewer was turned off in the display node of this segmentation. I went to Display/Advanced/Views, and checked “View1” (only “Yellow” was checked)</li>
</ol>
<p>I also disabled smoothing so that no data is lost from this sparse one-slice labelmap: when you click Update for Closed surface you see the list of conversion parameters, and by setting Smoothing to 0, it is disabled. You can do this programmatically by</p>
<p><code>s.GetSegmentation().SetConversionParameter('Smoothing factor', '0.0')</code></p>

---

## Post #18 by @cpinter (2017-11-08 19:17 UTC)

<p>If you import the labelmap to the segmentation and not just set it directly (I’m not sure how you do it), then it will be thresholded automatically:<br>
<code>vtkSlicerSegmentationsModuleLogic::ImportLabelmapToSegmentationNode</code></p>

---

## Post #19 by @mschumaker (2017-11-08 20:01 UTC)

<p>Great, thanks! I’ll look in to this, and let you know how it goes.</p>

---
