# Visualize transform between moving and fixed points

**Topic ID**: 28148
**Date**: 2023-03-03
**URL**: https://discourse.slicer.org/t/visualize-transform-between-moving-and-fixed-points/28148

---

## Post #1 by @JASON (2023-03-03 02:00 UTC)

<p>Hello! I wanted a way to visualize the connections between ‘moving’ and ‘fixed’ points (<strong>vtkMRMLMarkupsFiducialNode</strong>) and wrote a script that created a <strong>vtkMRMLMarkupsLineNode</strong> for each connection, but this was very slow over hundreds of points. Then I wrote a script to draw the lines using <strong>vtkPolyData</strong> / <strong>vtkCellArray</strong>, and this is super fast to update, but Slicer crashes shortly after creating the mesh Node.</p>
<p>Here’s what my script looks like:</p>
<pre><code class="lang-auto">fixedPoints_node = slicer.util.getNode('fixed_landmarks')
movingPoints_node = slicer.util.getNode('moving_landmarks')
num_landmarks = fixedPoints_node.GetNumberOfControlPoints()
fixed_points = vtkPoints()
points = vtkPoints()
for i in range(num_landmarks):
    fixed_pos = [0, 0, 0]
    fixedPoints_node.GetNthControlPointPosition(i, fixed_pos)
    moving_pos = [0, 0, 0]
    movingPoints_node.GetNthControlPointPosition(i, moving_pos)
    points.InsertNextPoint(moving_pos)
    points.InsertNextPoint(fixed_pos)
# Build PolyData from Points
lines = vtk.vtkCellArray()
for i in range(200):
    line = vtk.vtkLine()
    line.GetPointIds().SetId(0, i*2)
    line.GetPointIds().SetId(1, i*2+1)
    lines.InsertNextCell(line)
polydata = vtk.vtkPolyData()
polydata.SetPoints(points)
polydata.SetLines(lines)
# Build Model from PolyData
modelNode = slicer.vtkMRMLModelNode()
modelNode.SetAndObservePolyData(polydata)
slicer.mrmlScene.AddNode(modelNode)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5f84b80e688e38dabcfbefd6fbb7aaa7c570375.jpeg" data-download-href="/uploads/short-url/sfk1VDRBqPcB5kUph5USwmlx3Zr.jpeg?dl=1" title="meshLines" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5f84b80e688e38dabcfbefd6fbb7aaa7c570375_2_513x500.jpeg" alt="meshLines" data-base62-sha1="sfk1VDRBqPcB5kUph5USwmlx3Zr" width="513" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5f84b80e688e38dabcfbefd6fbb7aaa7c570375_2_513x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5f84b80e688e38dabcfbefd6fbb7aaa7c570375_2_769x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5f84b80e688e38dabcfbefd6fbb7aaa7c570375_2_1026x1000.jpeg 2x" data-dominant-color="020807"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">meshLines</span><span class="informations">1278×1245 236 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This will draw the lines correctly, but after you click anywhere in Slicer, the app will hang for a second, then crash silently.  No information is available logs related to the crash. Using Slicer 5.3.0 (2023-02-17).<br>
I have confirmed that the points stored in the markupNodes are all valid, all line segments have a non-zero length, all points within 60mm from origin.</p>
<p>I also notice that the docs for <strong>SetAndObservePolyData</strong> say “<em>Deprecated: Use SetAndObserveMesh instead.</em>”<br>
I tried this variation, which also successfully draws the correct mesh, but also crashes Slicer.</p>
<pre><code class="lang-auto">polydata = vtk.vtkPolyData()
polydata.SetPoints(points)
polydata.SetLines(lines)
mesh = vtk.vtkPolyData()
mesh.DeepCopy(polydata)
modelNode = slicer.vtkMRMLModelNode()
mesh = vtk.vtkPolyData()
mesh.DeepCopy(polydata)
modelNode.SetAndObserveMesh(mesh)
slicer.mrmlScene.AddNode(modelNode)
</code></pre>

---

## Post #2 by @JASON (2023-03-03 02:11 UTC)

<p>nevermind… this was user error <img src="https://emoji.discourse-cdn.com/twitter/man_facepalming.png?v=12" title=":man_facepalming:" class="emoji" alt=":man_facepalming:" loading="lazy" width="20" height="20"></p>
<p>When setting the lines, I should have used<br>
<code>for i in range(num_landmarks):</code><br>
instead of:<br>
<code>for i in range(200):</code></p>
<p>I was originally testing this with 200 random points, but only have 132 control points, so my <strong>vtkLine</strong> ends up with some invalid PointIDs. Correcting my script produces a good mesh without the crash.</p>

---

## Post #3 by @lassoan (2023-03-03 03:08 UTC)

<p>This features is available in Transforms module. It is a bit hidden - in Display → Visualization → Advanced → set your fixed (“from”) points in <code>Source points</code>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51e90fa2462a84da8dfef67f22b531e0f4ffbc87.jpeg" data-download-href="/uploads/short-url/bGC0nCGbAvwpQ796ESvGR3BePgr.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51e90fa2462a84da8dfef67f22b531e0f4ffbc87_2_690x382.jpeg" alt="image" data-base62-sha1="bGC0nCGbAvwpQ796ESvGR3BePgr" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51e90fa2462a84da8dfef67f22b531e0f4ffbc87_2_690x382.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51e90fa2462a84da8dfef67f22b531e0f4ffbc87_2_1035x573.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51e90fa2462a84da8dfef67f22b531e0f4ffbc87_2_1380x764.jpeg 2x" data-dominant-color="4C4B4F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1064 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<blockquote>
<p>wrote a script that created a <strong>vtkMRMLMarkupsLineNode</strong> for each connection, but this was very slow over hundreds of points</p>
</blockquote>
<p>When you add hundreds of markup nodes then the view may slow down because each line markup is interactive. If you don’t need interaction (you don’t need the control points to be clickable, you don’t want to drag the control points) then lock the markup and the rendering will be a magnitude faster.</p>

---
