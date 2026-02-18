# Cannot find rectangle segmentation option

**Topic ID**: 13286
**Date**: 2020-09-01
**URL**: https://discourse.slicer.org/t/cannot-find-rectangle-segmentation-option/13286

---

## Post #1 by @Yusuke (2020-09-01 23:10 UTC)

<p>Hi,</p>
<p>This page mentions ‘Rectangle’ in segmentation effect but I cannot find it in my options.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Editor" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Editor</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5db8844defd02e74842b147e6dbff075b868fa7.jpeg" data-download-href="/uploads/short-url/pWMLBWP1jb3loQe0pF8KTWbuuF1.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5db8844defd02e74842b147e6dbff075b868fa7_2_690x283.jpeg" alt="image" data-base62-sha1="pWMLBWP1jb3loQe0pF8KTWbuuF1" width="690" height="283" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5db8844defd02e74842b147e6dbff075b868fa7_2_690x283.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5db8844defd02e74842b147e6dbff075b868fa7_2_1035x424.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5db8844defd02e74842b147e6dbff075b868fa7_2_1380x566.jpeg 2x" data-dominant-color="2D2D2C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2194×900 279 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Could you tell me where I can find ‘Rectangle’ for segmentation?<br>
And is the same function available for own development?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-09-01 23:22 UTC)

<p>That documentation page is for the legacy Editor module. Rectangle option in Segment Editor module is available in Scissors effect.</p>

---

## Post #3 by @Yusuke (2020-09-02 12:23 UTC)

<p>Thank you. I was able to find the rectangle icon in Scissors.</p>
<p>Is there any way to modify the rectangle after making one on the image?<br>
I would like to make a cube in the 3D volume or 2D rectangle on 2D image but it apparently makes a column in 3D volume.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d2d5b6e80b6465967743cf701794a78a3009dc1.jpeg" data-download-href="/uploads/short-url/b0JWqTydVFagJ1J5JfsZbmPWmzf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d2d5b6e80b6465967743cf701794a78a3009dc1_2_475x500.jpeg" alt="image" data-base62-sha1="b0JWqTydVFagJ1J5JfsZbmPWmzf" width="475" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d2d5b6e80b6465967743cf701794a78a3009dc1_2_475x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d2d5b6e80b6465967743cf701794a78a3009dc1_2_712x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d2d5b6e80b6465967743cf701794a78a3009dc1_2_950x1000.jpeg 2x" data-dominant-color="42454B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1422×1496 293 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can I edit the boundary?</p>
<p>In addition, I would like to make the rectangle available in AIAA (by Nvidia) instead of Markups so that the user can define rectangle in the 2D image or a cube in the 3D volume then the trained CNN will take the cropped rectangle or cube to predict the mask.</p>
<p>Would it be possible? and how could I use the rectangle in my codes in AIAA?</p>
<p>I am very new to Slicer development and still struggling with understanding a whole architecture.<br>
Any advice would be very helpful!</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2020-09-02 12:44 UTC)

<aside class="quote no-group" data-username="Yusuke" data-post="3" data-topic="13286">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/ad7895/48.png" class="avatar"> Yusuke:</div>
<blockquote>
<p>Is there any way to modify the rectangle after making one on the image?</p>
</blockquote>
</aside>
<p>Yes, you can use any effects to modify the segment. You can also use Surface cut effect with smoothing disabled, to adjust corners of the rectangle or prism before applying it.[quote=“Yusuke, post:3, topic:13286”]<br>
I would like to make a cube in the 3D volume or 2D rectangle on 2D image but it apparently makes a column in 3D volume<br>
[/quote]</p>
<p>You can use the Scissors effect on an orthogonal slice to crop the column to the desired region (erase outside). You can also choose to restrict painting a single slice or a specified thickness.</p>
<aside class="quote no-group" data-username="Yusuke" data-post="3" data-topic="13286">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/ad7895/48.png" class="avatar"> Yusuke:</div>
<blockquote>
<p>Would it be possible? and how could I use the rectangle in my codes in AIAA?</p>
</blockquote>
</aside>
<p>In a AIAA module, you can define an input box by placing 6 markups fiducial points.</p>

---

## Post #5 by @Yusuke (2020-09-02 21:08 UTC)

<p>Thank you very much for your help!</p>
<p>I think what I want to do is something similar to MarkupPlane but just square.</p>
<p>Do you have any idea how to keep the plane square? I would like to refer the codes for MarkupPlane. Could you please tell me where I can find it?</p>
<p>Again, thank you for your support!</p>

---

## Post #6 by @lassoan (2020-09-02 21:15 UTC)

<p>You can enforce a markups plane to be a square by adding an observer to it. The observer’s callback function is executed whenever a control point is changed and then you can move other control points accordingly.</p>
<p>Inwould recommend to check out markups examples in script repository.</p>

---

## Post #7 by @Yusuke (2020-09-03 20:11 UTC)

<p>Thank you for your support!</p>
<p>I understood that I can add some function to observer using <code>planeNode.AddObserver()</code> but I’m still not quite sure how I can force the plane to be a square.</p>
<p>Could you please point me some script that change the point in plane node to be a square if you have one?</p>
<p>Thanks!</p>

---

## Post #8 by @lassoan (2020-09-03 21:07 UTC)

<p>When you get a notification that a control point is moved then update position of the other control point so that the shape remains a square.</p>

---

## Post #9 by @Yusuke (2020-09-04 18:12 UTC)

<p>My understanding is that the plane markup class is ‘vtkMRMLMarkupsPlaneNode’ but I couldn’t find any reference documentation for it.</p>
<p>In this link, it describes Line, Curve, Angle, and Fiducial.<br>
<a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html" class="onebox" target="_blank" rel="nofollow noopener">https://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html</a></p>
<p>Am I referring to old documents?  Can you please point me the reference for the plane markup class?</p>

---

## Post #10 by @lassoan (2020-09-04 18:35 UTC)

<p>Unfortunately, the documentation has not been updated for a while (you can track progress <a href="https://github.com/Slicer/Slicer/issues/4906">here</a>). Until this gets fixed, you can find documentation in <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/Markups/MRML">header files</a> or you can use <code>help</code> command in Python:</p>
<pre><code class="lang-nohighlight">
&gt;&gt;&gt; help(slicer.vtkMRMLMarkupsPlaneNode)
Help on class vtkMRMLMarkupsPlaneNode in module vtkSlicerMarkupsModuleMRMLPython:

class vtkMRMLMarkupsPlaneNode(vtkMRMLMarkupsNode)
 |  vtkMRMLMarkupsPlaneNode - MRML node to represent a plane markup
 |  
 |  Superclass: vtkMRMLMarkupsNode
 |  
 |  Plane Markups nodes contain three control points. Visualization
 |  parameters are set in the vtkMRMLMarkupsDisplayNode class.
 |  
 |  Markups is intended to be used for manual marking/editing of point
 |  positions.
 |  
 |  Coordinate systems used:
 |  - Local: Local coordinates
 |  - World: All parent transforms on node applied to local.
 |  - Plane: Plane coordinate space (Origin of plane at 0,0,0, XYZ axis
 |    aligned to XYZ unit vectors). Can have additional offset/rotation
 |    compared to local.\ingroup Slicer_QtModules_Markups
 |  
 |  Method resolution order:
 |      vtkMRMLMarkupsPlaneNode
 |      vtkMRMLMarkupsNode
 |      MRMLCorePython.vtkMRMLDisplayableNode
 |      MRMLCorePython.vtkMRMLTransformableNode
 |      MRMLCorePython.vtkMRMLStorableNode
 |      MRMLCorePython.vtkMRMLNode
 |      vtkCommonCorePython.vtkObject
 |      vtkCommonCorePython.vtkObjectBase
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  CopyContent(...)
 |      V.CopyContent(vtkMRMLNode, bool)
 |      C++: void CopyContent(vtkMRMLNode *node, bool deepCopy=true)
 |          override;
 |      
 |      Copy node content (excludes basic data, such as name and node
 |      references).
 |      \sa vtkMRMLNode::CopyContent
 |  
 |  CreateNodeInstance(...)
 |      V.CreateNodeInstance() -&gt; vtkMRMLNode
 |      C++: vtkMRMLNode *CreateNodeInstance() override;
 |      
 |      MRMLNode methods
 |  
 |  GetAutoSizeScalingFactor(...)
 |      V.GetAutoSizeScalingFactor() -&gt; float
 |      C++: virtual double GetAutoSizeScalingFactor()
 |      
 |      The plane size multiplier used to calculate the size of the
 |      plane. This is only used when the size mode is auto. Default is
 |      1.0.
 |  
 |  GetAxes(...)
 |      V.GetAxes([float, float, float], [float, float, float], [float,
 |          float, float])
 |      C++: void GetAxes(double x[3], double y[3], double z[3])
 |      
 |      The direction vectors defined by the markup points. Calculated as
 |      follows and then transformed by the offset matrix: X: Vector from
 |      1st to 0th point. Y: Cross product of the Z vector and X vectors.
 |      Z: Cross product of the X vector and the vector from the 2nd to
 |      0th point.
 |  
 |  GetAxesWorld(...)
 |      V.GetAxesWorld([float, float, float], [float, float, float],
 |          [float, float, float])
 |      C++: void GetAxesWorld(double x[3], double y[3], double z[3])
 |  
 |  GetClosestPointOnPlaneWorld(...)
 |      V.GetClosestPointOnPlaneWorld((float, float, float), [float,
 |          float, float], bool) -&gt; float
 |      C++: double GetClosestPointOnPlaneWorld(const double posWorld[3],
 |          double closestPosWorld[3], bool infinitePlane=true)
 |      
 |      Get the closest position on the plane in world coordinates.
 |      Returns the signed distance from the input point to the plane.
 |      Positive distance is in the direction of the plane normal, and
 |      negative distance is in the opposite direction.
 |      \param posWorld input position
 |      \param closestPosWorld: output found closest position
 |      \param infinitePlane if false, the closest position will be
 |          restricted to the plane bounds
 |      \return Signed distance from the point to the plane. Positive
 |          distance is in the direction of the plane normal
 |  
 |  GetIcon(...)
 |      V.GetIcon() -&gt; string
 |      C++: const char *GetIcon() override;
 |  
...
</code></pre>

---

## Post #11 by @Yusuke (2020-09-08 16:42 UTC)

<p>Thank you Iassoan!<br>
I think now I see the updated documentation here: <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsPlaneNode.html#a73ada3ec7e62d0d4d471725853894613" rel="nofollow noopener">https://apidocs.slicer.org/master/classvtkMRMLMarkupsPlaneNode.html#a73ada3ec7e62d0d4d471725853894613</a></p>
<p>I tried some of the methods but I was not able to find which method can be used for forcing the plane square.</p>
<p>Could you tell me which method forces points to locate as desired?</p>

---

## Post #12 by @jcfr (2020-09-08 16:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="13286">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Unfortunately, the documentation has not been updated for a while (you can track progress <a href="https://github.com/Slicer/Slicer/issues/4906">here</a>).</p>
</blockquote>
</aside>
<p>Documentation available at <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html" class="inline-onebox">Slicer: vtkMRMLMarkupsNode Class Reference</a> is now updated daily.</p>
<p>Thanks for your patience <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---

## Post #13 by @Yusuke (2020-09-08 18:28 UTC)

<p>Thank you for the link.</p>
<p>I’ve been trying to make a plane markup square but not sure how to.<br>
According to the documentation, SetPlaneBounds() looks to change the shape of it.</p>
<p>But SetPlaneBounds() does nothing in my codes and not sure why.<br>
planeMarkup = slicer.mrmlScene.GetFirstNodeByClass(“vtkMRMLMarkupsPlaneNode”)<br>
bounds = [0, 0, 0, 0, 0, 0]<br>
planeMarkup.GetPlaneBounds(bounds)<br>
print(‘currenty bounds : {}’.format(bounds))<br>
new_bounds = [-11, 11, -11, 11, 0, 0]<br>
planeMarkup.SetPlaneBounds(new_bounds)<br>
planeMarkup.GetPlaneBounds(bounds)<br>
print(‘currenty bounds : {}’.format(bounds))</p>
<p>the above codes shows<br>
currenty bounds : [-17.476825980903453, 17.476825980903453, -19.1019142042501, 19.1019142042501, 0.0, 0.0]<br>
currenty bounds : [-17.476825980903453, 17.476825980903453, -19.1019142042501, 19.1019142042501, 0.0, 0.0]<br>
which means the rectangle didn’t change.</p>
<p>Could you tell me how to use the method?</p>

---

## Post #14 by @lassoan (2020-09-08 18:30 UTC)

<p>You need to adjust the control points. First control point defines the plane center, second control point defines X axis direction and size, and third control point defines Y axis direction and size.</p>

---

## Post #15 by @Yusuke (2020-09-08 22:23 UTC)

<p>Thank you Andras,<br>
I tried to change the control point as they are changed.<br>
However, I found changing other control points every time a control point was moved is very slow.<br>
The codes are below and this is just sample codes.</p>
<pre><code>def onControlPointChanged(caller, event):

    markupPlaneNode = caller
    controlPointIndex = markupPlaneNode.GetDisplayNode().GetActiveControlPoint()
    print(controlPointIndex)
    cp_0 = [0, 0, 0]
    cp_1 = [0, 0, 0]
    cp_2 = [0, 0, 0]
    markupPlaneNode.GetNthControlPointPositionWorld(0, cp_0)
    markupPlaneNode.GetNthControlPointPositionWorld(1, cp_1)
    markupPlaneNode.GetNthControlPointPositionWorld(2, cp_2)
    if controlPointIndex == 1:
        cp_2_new = [-(cp_1[1]),cp_1[0],cp_2[2]]
        markupPlaneNode.SetNthControlPointPositionWorld(2, cp_2_new[0], cp_2_new[1], cp_2_new[2])
    elif controlPointIndex == 2:
        cp_1_new = [-(cp_2[1]),cp_2[0],cp_1[2]]
        markupPlaneNode.SetNthControlPointPositionWorld(1, cp_1_new[0], cp_1_new[1], cp_1_new[2])

def test1():

    markupsNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLMarkupsPlaneNode")
    markupsNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent, onControlPointChanged)
</code></pre>
<p>Is it what you are saying or are there other faster ways?<br>
If you can give me advice, that would be helpful!<br>
Thank you!!</p>

---

## Post #16 by @lassoan (2020-09-08 22:29 UTC)

<p>Your code was slow because it recursively called itself (setting control point position triggers control point changed event). You can break this recursion by adding a flag (<code>slicer.updatingControlPoint</code>):</p>
<pre><code class="lang-python">def onControlPointChanged(caller, event):
    if slicer.updatingControlPoint:
        return
    slicer.updatingControlPoint = True
    markupPlaneNode = caller
    movedPointIndex = markupPlaneNode.GetDisplayNode().GetActiveControlPoint()
    planeToWorldMatrix = vtk.vtkMatrix4x4()
    markupPlaneNode.GetPlaneToWorldMatrix(planeToWorldMatrix)
    bounds = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    markupPlaneNode.GetPlaneBounds(bounds)
    sideLength = bounds[movedPointIndex * 2 - 1]
    if movedPointIndex == 1:
        adjustedPointPosition = planeToWorldMatrix.MultiplyPoint([0, sideLength, 0, 1])
        markupPlaneNode.SetNthControlPointPositionWorld(2, *(adjustedPointPosition[0:3]))
    else:
        adjustedPointPosition = planeToWorldMatrix.MultiplyPoint([sideLength, 0, 0, 1])
        markupPlaneNode.SetNthControlPointPositionWorld(1, *(adjustedPointPosition[0:3]))
        adjustedPointPosition = planeToWorldMatrix.MultiplyPoint([0, sideLength, 0, 1])
        markupPlaneNode.SetNthControlPointPositionWorld(2, *(adjustedPointPosition[0:3]))
    slicer.updatingControlPoint = False

slicer.updatingControlPoint = False
markupsNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLMarkupsPlaneNode")
observationId = markupsNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent, onControlPointChanged)
</code></pre>
<p>Also make sure you don’t print anything in the console at each modified event, as logging takes time, too.</p>

---

## Post #17 by @Yusuke (2020-09-09 16:39 UTC)

<p>Thank you so much for the codes!!<br>
(<code>markupsNode</code> should be <code>markupPlaneNode</code>, correct?)</p>
<p>I still have to consider the cases where I move movedPointIndex==0 to translate the rectangle.</p>
<p>I changed the codes as the follow but still it doesn’t behave as desired.</p>
<pre><code>def onControlPointChanged(caller, event):
    print('test')
    if slicer.updatingControlPoint:
        return
    print('test2')
    slicer.updatingControlPoint = True
    markupPlaneNode = caller
    movedPointIndex = markupPlaneNode.GetDisplayNode().GetActiveControlPoint()
    planeToWorldMatrix = vtk.vtkMatrix4x4()
    markupPlaneNode.GetPlaneToWorldMatrix(planeToWorldMatrix)
    bounds = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    markupPlaneNode.GetPlaneBounds(bounds)
    sideLength = bounds[movedPointIndex * 2 - 1]
    if movedPointIndex == 1:
        adjustedPointPosition = planeToWorldMatrix.MultiplyPoint([0, sideLength, 0, 1])
        markupPlaneNode.SetNthControlPointPositionWorld(2, *(adjustedPointPosition[0:3]))
    elif movedPointIndex == 2:
        adjustedPointPosition = planeToWorldMatrix.MultiplyPoint([sideLength, 0, 0, 1])
        markupPlaneNode.SetNthControlPointPositionWorld(1, *(adjustedPointPosition[0:3]))
        adjustedPointPosition = planeToWorldMatrix.MultiplyPoint([0, sideLength, 0, 1])
        markupPlaneNode.SetNthControlPointPositionWorld(2, *(adjustedPointPosition[0:3]))
    elif movedPointIndex == 0:
        adjustedPointPosition = planeToWorldMatrix.MultiplyPoint([bounds[3],0, 0, 1])
        markupPlaneNode.SetNthControlPointPositionWorld(1, *(adjustedPointPosition[0:3]))
        adjustedPointPosition = planeToWorldMatrix.MultiplyPoint([0, bounds[3], 0, 1])
        markupPlaneNode.SetNthControlPointPositionWorld(2, *(adjustedPointPosition[0:3]))

    slicer.updatingControlPoint = False
</code></pre>
<p>Do you have any idea how to deal with if movedPointIndex == 0? to move the square without changing the orient and size?</p>

---

## Post #18 by @lassoan (2020-09-09 18:51 UTC)

<aside class="quote no-group" data-username="Yusuke" data-post="17" data-topic="13286">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/ad7895/48.png" class="avatar"> Yusuke:</div>
<blockquote>
<p>I changed the codes as the follow but still it doesn’t behave as desired.</p>
</blockquote>
</aside>
<p>It works well for me. What problem did you have?</p>
<aside class="quote no-group" data-username="Yusuke" data-post="17" data-topic="13286">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/ad7895/48.png" class="avatar"> Yusuke:</div>
<blockquote>
<p>Do you have any idea how to deal with if movedPointIndex == 0? to move the square without changing the orient and size?</p>
</blockquote>
</aside>
<p>There are many options. For example you can store the previous <code>planeToWorldMatrix</code>, update it with the new center point position, and get the two new point positions by transforming <code>(sideLength,0,0,1)</code> and <code>(0,sideLength,0,1)</code> points by this updated <code>planeToWorldMatrix</code>.</p>

---

## Post #19 by @Yusuke (2020-09-09 19:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="18" data-topic="13286">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It works well for me. What problem did you have?</p>
</blockquote>
</aside>
<p>In your original codes, when I move the center point in the rectangle, the other two points will be located in the same as the center point, which made the rectangle converge into one point.<br>
In my codes above, when I move the center point in the rectangle, the size and the orient of the rectangle will be changed.</p>
<aside class="quote no-group" data-username="lassoan" data-post="18" data-topic="13286">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There are many options. For example you can store the previous <code>planeToWorldMatrix</code> , update it with the new center point position, and get the two new point positions by transforming <code>(sideLength,0,0,1)</code> and <code>(0,sideLength,0,1)</code> points by this updated <code>planeToWorldMatrix</code> .</p>
</blockquote>
</aside>
<p>Could you elaborate on this?<br>
My understanding is that what you mentioned is what my codes are doing.</p>
<p>Thank you so much for your help!!</p>

---

## Post #20 by @lassoan (2020-09-10 12:43 UTC)

<p>You can also translate and rotate planes using the interaction handles:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae31161a28e071c44dec467478b7b5586e41ffec.png" data-download-href="/uploads/short-url/oQYfiT7TyRDjCgsMZZoU5xqQIxu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae31161a28e071c44dec467478b7b5586e41ffec_2_534x500.png" alt="image" data-base62-sha1="oQYfiT7TyRDjCgsMZZoU5xqQIxu" width="534" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae31161a28e071c44dec467478b7b5586e41ffec_2_534x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae31161a28e071c44dec467478b7b5586e41ffec.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae31161a28e071c44dec467478b7b5586e41ffec.png 2x" data-dominant-color="918894"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">644×602 31.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Click-and-drag the displayed arrows:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18ec14a079cd76179cbaa5178c9812822df3af8b.png" data-download-href="/uploads/short-url/3ytg5QSFJ3G4AT5npEcHbVrp2Lp.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18ec14a079cd76179cbaa5178c9812822df3af8b.png" alt="image" data-base62-sha1="3ytg5QSFJ3G4AT5npEcHbVrp2Lp" width="474" height="500" data-dominant-color="9794C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">585×617 13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #21 by @Yusuke (2020-09-10 14:06 UTC)

<p>Thanks, Andras, good to know.<br>
This behavior in the 3D view looks what I want to do but my use-case is to draw a rectangle for legion on an axial slice.<br>
When I use ‘Interaction handles visible’ on an axial slice, the size and the orientation will be changed (same behavior as when I just move the center point on the axial view).</p>
<p>I’m pretty sure there are some ways to keep the size and the orientation moving the center point by modifying the codes in <code>elif movedPointIndex == 0:</code></p>
<p>I’m almost there but I’m not quite understanding <code>planeToWorldMatrix</code> and <code>MultiplyPoint </code>.</p>
<p>Again, Thank you so much for your help! I’m very new to the 3D slicer development but thanks to you guys, I can make small progress!</p>

---

## Post #22 by @lassoan (2020-09-10 21:13 UTC)

<p>Once you placed the rectangle, you can move the box with the interaction handles instead of the control points (you can hide the control points).</p>
<p>Of course you can also keep using the control points as I described above. Plane to World matrix stores the plane center and axes as a homogeneous transformation matrix. If you store the previous matrix then all you need to do after moving the plane center is to update the translation part of the matrix (last column) and then you can use it to get the two new side point positions (by multiplying the Plate to World matrix by <code>(sideLength,0,0,1)</code>  and  <code>(0,sideLength,0,1)</code> points).</p>

---

## Post #23 by @Yusuke (2020-09-11 17:46 UTC)

<p>How do you get and keep the previous planeToWorldMatrix?<br>
Is there any function that triggers before changing the control point?</p>

---

## Post #24 by @lassoan (2020-09-11 17:54 UTC)

<aside class="quote no-group" data-username="Yusuke" data-post="23" data-topic="13286">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/ad7895/48.png" class="avatar"> Yusuke:</div>
<blockquote>
<p>How do you get and keep the previous planeToWorldMatrix?</p>
</blockquote>
</aside>
<p>You can store the matrix in a member variable in your module (or in <code>slicer</code> namespace if you do just quick testing in scripts and don’t have a module yet). Set the variable’s value when you create it, then update it each time at the end of the callback function.</p>

---
