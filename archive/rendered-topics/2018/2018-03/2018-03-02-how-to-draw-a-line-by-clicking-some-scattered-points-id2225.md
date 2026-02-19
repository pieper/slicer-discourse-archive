---
topic_id: 2225
title: "How To Draw A Line By Clicking Some Scattered Points"
date: 2018-03-02
url: https://discourse.slicer.org/t/2225
---

# How to draw a line by clicking some scattered points

**Topic ID**: 2225
**Date**: 2018-03-02
**URL**: https://discourse.slicer.org/t/how-to-draw-a-line-by-clicking-some-scattered-points/2225

---

## Post #1 by @spring (2018-03-02 05:51 UTC)

<p>Hi All,</p>
<p>I want to draw a line by connecting some scattered points which I have clicked in the view.</p>
<p>I can get each points RAS position, but it seems can not display the final line in Slicer, below is my code for drawing line, could someone share some guidance?</p>
<pre><code class="lang-auto">#coding----
def drawPolyLine(points):    
 #points is the list which contains each points pos,likes [(0.0,1.0),(1.0,2.0)],just one slice in the view.
    polyLine = vtk.vtkPolyLineSource()
    for i, (x, y) in enumerate(points):
        polyLine.SetPoint(i, x, y, 0)
    polyLine.SetNumberOfPoints(len(points))
    polyLine.SetClosed(True)
    polyLine.Update()
    polyData = polyLine.GetOutput()
    return showPolyData(polyData)

def showPolyData(polyData):
    model = slicer.vtkMRMLModelNode()
    if isinstance(polyData, vtk.vtkAlgorithmOutput):
        model.SetPolyDataConnection(polyData)
    elif isinstance(polyData, vtk.vtkPolyData):
        # print("type and polyData={},{}".format(type(polyData),polyData))
        model.SetAndObservePolyData(polyData)
    else:
        raise Exception('input error!')
    model.SetScene(slicer.mrmlScene)
    modelDisplay = slicer.vtkMRMLModelDisplayNode()
    modelDisplay.SetOpacity(1.0)
    modelDisplay.SetColor([1, 1, 0])
    modelDisplay.SetSliceIntersectionVisibility(True)   # Show in slice view
    modelDisplay.SetVisibility(True)                    # Hide in 3D view
    modelDisplay.SetScene(slicer.mrmlScene)
    slicer.mrmlScene.AddNode(modelDisplay)
    slicer.mrmlScene.AddNode(model)
    transform = slicer.vtkMRMLLinearTransformNode()
    slicer.mrmlScene.AddNode(transform)
    model.SetAndObserveDisplayNodeID(modelDisplay.GetID())
    model.SetAndObserveTransformNodeID(transform.GetID())
    return model
</code></pre>
<p>Thanks in advance!<br>
Chunbo</p>

---

## Post #2 by @lassoan (2018-03-02 12:48 UTC)

<p>You can use MarkupsToModel extension to create curves from markup fiducial or model points. It supports linear and various smooth interpolating and approximating methods.</p>

---

## Post #3 by @spring (2018-03-05 07:19 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks for your answer.</p>
<p>I have tried  MarkupsToModel,it really can draw the straight line by clicking scattered pointes.<br>
Just have one issue:if I want to delete the total polydata,I should switch to Models then select  corresponding model to delete it,correct?</p>
<p>I have implemented a simple module,which can draw some scattered points,then connect neighboring points with a straight line, used a polydata to show these lines at last,likes below screenshot:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc9100881f80d25f618732b540240c292154047a.jpeg" alt="image" data-base62-sha1="vtdHXsoOmxxhXt9NsPVuRAKRi54" width="333" height="280"></p>
<p>Since I want to setAndobserve this polydata in Slicer,the issue: this Polydata can not be displayed,since the area is 0,likes below screenshot:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89618657c020ce9d33b6b3c7c14988842069539c.png" data-download-href="/uploads/short-url/jBkmhemuUCo8UWKds0srdkjmcUs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89618657c020ce9d33b6b3c7c14988842069539c_2_690x316.png" alt="image" data-base62-sha1="jBkmhemuUCo8UWKds0srdkjmcUs" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89618657c020ce9d33b6b3c7c14988842069539c_2_690x316.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89618657c020ce9d33b6b3c7c14988842069539c_2_1035x474.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89618657c020ce9d33b6b3c7c14988842069539c.png 2x" data-dominant-color="2B2B2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1092×501 57.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Not sure if some parameters are incorrect? Or if there is some examples which can create a polydata and can be set and observed in Slicer?</p>
<p>Best，<br>
Chunbo</p>

---

## Post #4 by @lassoan (2018-03-05 13:40 UTC)

<p>If you set the output to be a closed surface instead of a line then you’ll get the surface area. Both sides of the surface will be included in the computation, so you probably want to divide the reported surface area by 2.</p>

---

## Post #5 by @spring (2018-03-05 14:54 UTC)

<p>Thanks,Lasson.<br>
I will try the method.<br>
Btw,I have solved my issue from this post:<a href="https://discourse.slicer.org/t/display-model-in-slice-viewer/208/2">Display model in slice viewer</a>.</p>
<p>Best,<br>
Chunbo</p>

---

## Post #6 by @spring (2018-03-06 08:34 UTC)

<p>Hi lassoan,<br>
I used the following codes :<br>
inputMarkups = getNode(‘F’)</p>
<p>outputModel = slicer.mrmlScene.AddNode(slicer.vtkMRMLModelNode())<br>
outputModel.CreateDefaultDisplayNodes()<br>
outputModel.GetDisplayNode().SetSliceIntersectionVisibility(True)<br>
outputModel.GetDisplayNode().SetColor(1,0,0)</p>
<p>markupsToModel = slicer.mrmlScene.AddNode(slicer.vtkMRMLMarkupsToModelNode())<br>
markupsToModel.SetAutoUpdateOutput(True)<br>
markupsToModel.SetAndObserveModelNodeID(outputModel.GetID())<br>
markupsToModel.SetAndObserveMarkupsNodeID(inputMarkups.GetID())</p>
<hr>
<p>It can create curves with clicking points,one issue is:the curve is convex hull,can we change it to false?<br>
since we found some points can not be seen,pls see below screenshots:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6eb3b366235afa9ad7ed8c352cc01e1b442febbb.png" alt="image" data-base62-sha1="fNjwN33ZhERUrMzEIsLXxLkt9mb" width="507" height="371"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09ddfdafeccf8b6114b1ae58a5fb4cb20504dc42.png" alt="image" data-base62-sha1="1phUsFBo04PL1i55nXFHatTokAG" width="546" height="398"></p>
<p>Thanks,<br>
Chunbo</p>

---

## Post #7 by @lassoan (2018-03-10 14:06 UTC)

<p>Do you need a line/curve connecting points? If yes, then set ModelType to Curve and probably enable TubeLoop as well.</p>
<p>If you want to reconstruct a surface from a sparse set of points then Delaunay triangulation is used. You can tune DelaunayAlpha parameter to control how much concavity is allowed in the reconstructed surface (if alpha is set to 0 then the result will be a convex hull).</p>

---
