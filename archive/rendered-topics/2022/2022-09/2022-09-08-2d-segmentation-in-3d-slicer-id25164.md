---
topic_id: 25164
title: "2D Segmentation In 3D Slicer"
date: 2022-09-08
url: https://discourse.slicer.org/t/25164
---

# 2d segmentation in 3d slicer 

**Topic ID**: 25164
**Date**: 2022-09-08
**URL**: https://discourse.slicer.org/t/2d-segmentation-in-3d-slicer/25164

---

## Post #1 by @luna1 (2022-09-08 18:33 UTC)

<p>hello,am trying to programme an extension in python that does brain tumour segmentation.<br>
my plan was that i draw a contour around the tumour once in each one of the axes then iterate in each of the slices where the initial contour will shrink until it finds the tumour in each slice<br>
but am really just a beginner and even though i have read many tutorials i still have a hard time understanding how I get to show my segmentation, i understand that i have to create a segment but beyond that, i have no idea how to connect it to the contour that my programme generated and how do i connect it to a labelmap ?<br>
am i sorry for asking a question that is probably basic i would really appreciate the help !!<br>
ps the contour is a numpy array that contains ras coordinates</p>

---

## Post #2 by @lassoan (2022-09-08 18:45 UTC)

<p>Lots of solutions have been developed over past few decades for brain tumor segmentation. There are AI models for fully automatic tumor detection and segmentation or tumor segmentation from a region of interest. There are semi-automatic tools, such as “Grow from seeds” or “Local threshold” in Segment Editor module, for segmenting more challenging cases from a single click or a few scribbles in the image. There are also many manual tools that can segment a tumor that you can use to create segmentations from scratch or touch-up automatic segmentation results.</p>
<p>Since this segmentation task has been so widely worked on, for so long, by so many groups, it would be hard to come up with something really new or significantly better. However, if your goal is mainly learning then experimenting with development of a new segmentation algorithm may make sense. If your goal is to solve the clinical task then I would recommend to try the existing tools (and improve them as needed).</p>

---

## Post #3 by @luna1 (2022-09-08 19:06 UTC)

<p>yes i would really like to learn and experiment! my idea was to use my own segmentation algorithm for the input images and then maybe use some of the tools that already exist<br>
my question is since my segmentation algorithm is a 2d segmentation is it possible to link them to for example segment editor effect modules  since most of them use a 3d segmentation<br>
and can you please explain to me how do i get to show the result of the segmentation   what confuses me in the tutorials is the concept of creating a segment and how to link to the results of the algorithm i implemented to it<br>
thank you for your response !</p>

---

## Post #4 by @lassoan (2022-09-08 19:13 UTC)

<p>Even if you segment only single slices, those slices still exist in 3D space (their position, orientation, pixel size are still in 3D), so they are still 3D images, they just happen to have a single slice. You could create a separate segmentation for each slice, but most probably it makes your life simpler if you store all the slices in one 3D segmentation. You can access voxels of a segmentation as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array">these examples</a>.</p>

---

## Post #5 by @luna1 (2022-09-09 12:41 UTC)

<p>okey thank you so much!!! but now i have this problem  so i did write my algorithme and at the end  i get a   numpy array containing RAS coordinates of the contour of the tumeur, i tried to use the surface cut module because it seemed the one that would most likely allow me to display my segmentation using this code :</p>
<pre data-code-wrap="python"><code class="lang-python"> segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
            #segmentationNode = slicer.vtkMRMLSegmentationNode()
            #slicer.mrmlScene.AddNode(segmentationNode)
            segmentationNode.CreateDefaultDisplayNodes()
            segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

            segmentName = "Tumor"

            import vtkSegmentationCorePython as vtkSegmentationCore

            segment = vtkSegmentationCore.vtkSegment()
            segment.SetName(segmentationNode.GetSegmentation().GenerateUniqueSegmentID(segmentName))
            segmentationNode.GetSegmentation().AddSegment(segment)
            ##################################
           

            segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
           
            segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
            segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
            slicer.mrmlScene.AddNode(segmentEditorNode)
            segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
            segmentEditorWidget.setSegmentationNode(segmentationNode)
            segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)
           

            segmentEditorWidget.setActiveEffectByName("Surface cut")
            effect = segmentEditorWidget.activeEffect()

            effect.self().fiducialPlacementToggle.placeButton().click()
            points=contour
            for p in points:
                 effect.self().segmentMarkupNode.AddControlPoint(p)

            effect.self().onApply()

            ##################################
           
            segmentationDisplayNode = segmentationNode.GetDisplayNode()
            segmentationDisplayNode.SetSegmentVisibility(segmentName, True)
</code></pre>
<p>it’s basically the same code  used in the test of the  SegmentEditorSurfaceCut.py but i removed  segmentEditorWidget.show() because when i executed the code it would show me this<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97203ef3fb6ca52d117851f96c830dc903b683b7.png" alt="image" data-base62-sha1="lyVbrx5Wg0CpSMnPys2LAuvy1p5" width="207" height="298"></p>
<p>then slicer would bug and stops working so when i removed it i did get  the segmentation that i wanted but it took too long almost 10 min<br>
all of this happened with me using slicer 5<br>
the interesting part is when i tried the same code in a better performing computer but has slicer 4 i got this erreur<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f82cb88b8a43c433079f55f3bdefc6a820a1678c.png" data-download-href="/uploads/short-url/zpse3u6g0n2E3E5azPHzOqDfdQ8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f82cb88b8a43c433079f55f3bdefc6a820a1678c.png" alt="image" data-base62-sha1="zpse3u6g0n2E3E5azPHzOqDfdQ8" width="690" height="71" data-dominant-color="2C2020"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">766×79 3.37 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
so what is actually happening why did it work in one version but not the other</p>

---

## Post #6 by @lassoan (2022-09-09 18:23 UTC)

<aside class="quote no-group" data-username="luna1" data-post="5" data-topic="25164">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/7bcc69/48.png" class="avatar"> luna1:</div>
<blockquote>
<p><code>effect.self().segmentMarkupNode.AddControlPoint(p)</code></p>
</blockquote>
</aside>
<p>Please use a current Slicer version. The error message about vtkVector3d required should not appear for current Slicer versions when you provide a numpy array as input.</p>

---

## Post #7 by @luna1 (2022-09-11 07:25 UTC)

<p>ok thank you so much it’s working fine now !</p>

---
