# Adding control points with undefined position from Python

**Topic ID**: 12344
**Date**: 2020-07-02
**URL**: https://discourse.slicer.org/t/adding-control-points-with-undefined-position-from-python/12344

---

## Post #1 by @smrolfe (2020-07-02 18:07 UTC)

<p>I’d like to create a landmarking template with named, unplaced points. I can unset the position status of a point I have placed, but would like to add points to the node with uninitialized positions. It looks like I could do this if I could access <a href="https://github.com/Slicer/Slicer/blob/07bc92102ca225e3d46c5545af650aac3455125d/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.cxx#L517" rel="nofollow noopener">vtkMRMLMarkupsNode::AddNControlPoints</a> from python. Would this be the best approach, or is there a way to call  <a href="https://github.com/Slicer/Slicer/blob/07bc92102ca225e3d46c5545af650aac3455125d/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.cxx#L476" rel="nofollow noopener">vtkMRMLMarkupsNode::AddControlPoint</a> with an uninitialized control point?</p>
<p>Alternatively, would it be preferable to set the coordinates of unplaced points to something like [0,0,0]?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I’m interested in your thoughts on the correct approach.</p>

---

## Post #2 by @lassoan (2020-07-02 19:10 UTC)

<p>Unplaced points can have any point coordinates, as they would not be showed to users and they would not be used in any computations.</p>
<p>vtkMRMLMarkupsNode API already allows adding points and undefining their point position (for example, using <code>vtkMRMLMarkupsNode::UnsetNthControlPointPosition(int pointIndex)</code>), so you don’t need to do anything with that.</p>
<p>What is still to be implemented:</p>
<ul>
<li>improve control points table in Markups module GUI:
<ul>
<li>hide positions of unplaced points</li>
<li>add “place” button to the table to each line, which allows (re)placing the control point</li>
</ul>
</li>
<li>improve the markup point placement logic (probably <a href="https://github.com/Slicer/Slicer/blob/43300c7b9a3b27265c2bc736693cb881f05e3ea9/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsDisplayNode.cxx#L542-L633">here</a>): when control point placement is activated then check first if there is a control point with undefined position and if there is one then place that (instead of creating a new control point)</li>
</ul>

---
