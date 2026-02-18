# Defining a new coordinate system using markups plane node

**Topic ID**: 19726
**Date**: 2021-09-17
**URL**: https://discourse.slicer.org/t/defining-a-new-coordinate-system-using-markups-plane-node/19726

---

## Post #1 by @matsuba8 (2021-09-17 14:39 UTC)

<p>Continuing the discussion from <a href="https://discourse.slicer.org/t/creating-a-new-coordinate-system/19446/16">Creating a new coordinate system</a>:</p>
<p>Hello all, I would like to continue this discussion on defining a coordinate system using the markups plane node, as suggested by Andras in the forum linked above.<br>
I had a couple of questions about this process:</p>
<ol>
<li>How do I make sure that my axes that I set are orthogonal to each other?</li>
<li>How do I use the <a href="http://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html#ae2b237c8d8ca2bbb6c304263f2800720" rel="noopener nofollow ugc">markupsNode.SetNthControlPointPositionWorld(i, r, a, s) </a> method to place a fiducial at a specific coordinate point in the global system?<br>
a. It would be great if I could see a screenshot of the Python interactor, where the code has run successfully.<br>
b. What is a pointIndex?</li>
</ol>
<p>Thank you very much for your help!</p>
<p>Michele</p>

---

## Post #2 by @mikebind (2021-09-17 23:20 UTC)

<aside class="quote no-group" data-username="matsuba8" data-post="1" data-topic="19726">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/59ef9b/48.png" class="avatar"> matsuba8:</div>
<blockquote>
<ul>
<li>How do I make sure that my axes that I set are orthogonal to each other?</li>
</ul>
</blockquote>
</aside>
<p>The axes of a MarkupsPlane node are always orthogonal, even if the triangle of points used to define the plane is not a right triangle. If you have a MarkupsFiducial node with your three defining points, this function will produce a MarkupsPlane node</p>
<pre><code class="lang-auto">def makePlaneMarkupFromFiducial(self, FNode, planeName):
    """Create MarkupsPlane using first three control points of the input fiducial node.
    """
    if FNode.GetNumberOfControlPoints()&lt;3:
      logging.warning('Not enough control points to create plane markup!')
      return
    planeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsPlaneNode', planeName)
    for cpIdx in range(3):
      pos = vtk.vtkVector3d()
      FNode.GetNthControlPointPositionWorld(cpIdx, pos)
      planeNode.AddControlPointWorld(pos)

    return planeNode

</code></pre>
<p>The resulting orthogonal axes, X, Y and Z are determined from the three input points as follows:</p>
<ul>
<li>the positive X axis direction is the direction from point 1 to point 2</li>
<li>the positive Z axis is the cross product of the X-axis direction vector with the direction vector  from point 1 to point 3</li>
<li>the positive Y axis is the cross product of the Z-axis and the X-axis</li>
</ul>
<p>Conceptually, the Z-axis is perpendicular to the plane defined by the three points, and the positive Z-axis points such that, looking back at the three points from the positive Z side, point 1, point 2, and point 3 are counterclockwise (because the <a href="https://en.wikipedia.org/wiki/Cross_product">cross product</a> follows a <a href="https://en.wikipedia.org/wiki/Right-hand_rule">right hand rule</a>). The positive Y-axis direction is the projection of the point1 to point2 vector onto the vector perpendicular to the X-Z plane; the cross product of the positive X-axis and positive Z-axis is another way to find this direction.</p>
<p>In terms of the display of the MarkupsPlane in the 3D view, it is shown as a rectangle in space. Point1 is the center of the rectangle, and the edges of the rectangle are parallel to the X and Y axes as defined above.  The rectangle extends in the positive X direction far enough to touch Point2, which will always be at the midpoint of this edge because the X direction points directly from Point1 to Point2.  The rectangle extends the same distance on the other side of Point1, keeping Point1 in the center of the rectangle. In the positive Y direction, the rectangle extends far enough so that the edge touches Point3.  Note that Point3 will NOT necessarily be at the midpoint of this edge, because the angle Point2-Point1-Point3 may not be a right angle.  The rectangle extends in the negative Y direction exactly as far as it did in the positive Y direction, keeping Point1 in the center of the rectangle.</p>
<p>I had to work these details out by looking at the code for MarkupsPlane nodes, because, as far as I can tell there isn’t really documentation for them yet.</p>
<aside class="quote no-group" data-username="matsuba8" data-post="1" data-topic="19726">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/59ef9b/48.png" class="avatar"> matsuba8:</div>
<blockquote>
<p>How do I use the <a href="http://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html#ae2b237c8d8ca2bbb6c304263f2800720">markupsNode.SetNthControlPointPositionWorld(i, r, a, s) </a> method to place a fiducial at a specific coordinate point in the global system?</p>
</blockquote>
</aside>
<p>Here is sample code which will work in the Python interactor using the point of interest you listed in the <a href="https://discourse.slicer.org/t/creating-a-new-coordinate-system/19446/7">other thread</a>:</p>
<pre><code class="lang-auto">fiducialNodeForBoneBlock1 = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', 'BoneBlock1')
fiducialNodeForBoneBlock1 .SetNthControlPointPositionWorld(0, -110.676, -105.632, 31.2008)
</code></pre>
<p>The 0 which is the first input to <code>SetNthControlPointPositionWorld()</code> is the point index, which tells which control point you want to set the position of, numbered starting at 0.  So, the first control point has index 0, the second point has index 1, the third has index 2, etc. In my description above, Point1, the center point for the plane, would have index 0; Point2 would have index 1, and Point3 would have index 2.</p>
<p>In terms of a workflow, you could run the two lines above defining a fiducial node for the first bone block and placing the center control point, and then interactively place point 2 and point 3 on landmarks using the Markups module.  Then you could define <code>fiducialNodeForBoneBlock2</code>  in the same way, just using the centroid for block 2 instead of the one for block 1, place the point 2 and point 3 landmarks interactively (note that these must be clicked in the same order as for the first block, or else the plane node derived from them will be inverted relative to block1).   Lastly, you can use the makePlaneMarkupFromFiducial() function defined above to make plane nodes for each block:</p>
<pre><code class="lang-auto">planeNodeForBlock1 = makePlaneMarkupFromFiducial( fiducialNodeForBoneBlock1, 'Block1_Plane')
planeNodeForBlock2 = makePlaneMarkupFromFiducial( fiducialNodeForBoneBlock2, 'Block2_Plane')
</code></pre>
<p>Hope that helps!</p>

---

## Post #3 by @jegberink (2022-10-11 08:08 UTC)

<p>Hello,</p>
<p>Sorry to revive this topic, however i have been trying to create a plane from 3 fiducial points using the code you’ve shown here. Right now i’m creating a 3 point plane and editing the control points manually in the properties.</p>
<p>I have an extremely limited knowledge of python, please bear with me.<br>
I have a fiducial node with 3 points. What are the steps i should take from this point?</p>
<p>When i run the code i get the following error:</p>
<p>File “”, line 1<br>
return planeNode<br>
IndentationError: unexpected indent</p>
<p>If someone could help me it would be greatly appreciated</p>

---

## Post #4 by @mikebind (2022-10-11 21:15 UTC)

<p>If you cut and paste into the python interactor, it doesn’t like blank lines in the middle of function definitions, so that’s what gave you the indentation error above.  Also, the default plane type changed since that post was written (it used to be 3points and is now pointNormal), so the function needed to be updated anyway before it would work now.</p>
<pre><code class="lang-auto">def makePlaneMarkupFromFiducial(FNode, planeName):
    """Create MarkupsPlane using first three control points of the input fiducial node.
    """
    if FNode.GetNumberOfControlPoints()&lt;3:
      logging.warning('Not enough control points to create plane markup!')
      return
    planeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsPlaneNode', planeName)
    planeNode.SetPlaneType(planeNode.PlaneType3Points)
    for cpIdx in range(3):
      pos = vtk.vtkVector3d()
      FNode.GetNthControlPointPositionWorld(cpIdx, pos)
      planeNode.AddControlPointWorld(pos)
    return planeNode
</code></pre>
<p>This should now work just fine from the python interactor, just cut and paste and hit enter twice.  If your fiducial point list is named ‘myPoints’, you could then use the first three to define a markups plane node by typing</p>
<p><code>makePlaneMarkupFromFiducial(getNode('myPoints'), 'myPlane')</code></p>
<p>into the interactor and hitting enter.</p>

---

## Post #5 by @lili-yu22 (2022-11-09 02:52 UTC)

<p>I follow the above process, but the results are as follows. Can you give me some help<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1fd82ea692dc6901100ac79327f1d546d4d32ff6.jpeg" alt="mmexport1667962279153" data-base62-sha1="4xHY8c6C6DqJ3dkdHTyRPoRz0mG" width="504" height="464"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03152e366b931690c371a32af1c55f778cb4e1bd.jpeg" alt="mmexport1667962284060" data-base62-sha1="rgOjg1K37miKsKl9rLBqwOUgcR" width="479" height="394"></p>

---

## Post #6 by @lili-yu22 (2022-11-09 04:54 UTC)

<p>I success ，thank you</p>

---

## Post #7 by @mikebind (2022-11-09 18:17 UTC)

<p>I think the issue here was again line breaks.  The python console won’t allow blank lines within a function definition (because it interprets it as ending the function, and then thinks the next indented line is an unexplained and incorrect indentation), and it also wants at least one full blank line at the end of a function definition before you try to use the function (I don’t know why this makes sense, but it seems to be how it works).  In this case, you didn’t leave a blank line between the <code>return</code> statement and the call to the function, so it gave an error.   It sounds like you got things working, I just figured I’d leave an explanation to help the next person who might try this.</p>

---
