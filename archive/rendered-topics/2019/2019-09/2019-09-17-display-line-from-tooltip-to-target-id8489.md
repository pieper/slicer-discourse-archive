---
topic_id: 8489
title: "Display Line From Tooltip To Target"
date: 2019-09-17
url: https://discourse.slicer.org/t/8489
---

# Display line from tooltip to target

**Topic ID**: 8489
**Date**: 2019-09-17
**URL**: https://discourse.slicer.org/t/display-line-from-tooltip-to-target/8489

---

## Post #1 by @Prashant_Pandey (2019-09-17 23:57 UTC)

<p>Hi Andras,</p>
<p>Thanks for your previous reply. I’ve been working on recreating views surgeons expect and this has mostly been successful using existing Slicer functionality. Now I’m trying to implement visualizations that surgeons are not used to seeing in conventional procedures but are useful in navigated procedures.</p>
<p>Specifically, I would like to find out what’s the easiest way to display a dynamic trajectory (just a line) going from the tool tip (which is a changing linear transform) to a predefined target (which could be a model or markup fiducial). VisuaLine (<a href="https://www.slicer.org/wiki/Documentation/4.3/Modules/VisuaLine" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.3/Modules/VisuaLine</a>) seemed like it could do this but it’s not in Slicer 4.10, and as you mentioned PathExplorer is not being actively maintained. I <em>could</em> use PathExplorer to create a tool fiducial and a target fiducial and an annotation trajectory, and then transform the tool fiducial by the tracked tool’s transform, but the trajectory won’t update unless the transform is hardened. Is there a better way?</p>

---

## Post #2 by @lassoan (2019-09-19 00:03 UTC)

<p>BreachWarning module in SlicerIGT module does exactly this. It shows a line that connects the tooltip to the target. It can display the distance value and also give sound and visual signal if the tool gets close to the target model.</p>

---

## Post #3 by @Prashant_Pandey (2019-09-19 04:49 UTC)

<p>Thanks! Not sure how I missed the BreachWarning module.</p>
<p>Is there a way to do the same thing with fiducials instead of models? The reason I’m asking is because I want to be able to visualize the trajectory to a point rather than the closest point on the model, which is what the breach warning module does. Additionally, I can’t seem to place a model intuitively/precisely like with a fiducial points. I can transform it and then view the transform node in 3D but this way it’s not easy to place the model exactly where I want on the image.</p>

---

## Post #4 by @lassoan (2019-09-19 12:29 UTC)

<p>You can add a model with a single point or a very small sphere that is placed at the fiducial’s position. This example shows how to do it (you can remove the radius adjustment, and set a small fixed radius instead): <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer</a></p>

---

## Post #5 by @Prashant_Pandey (2019-09-19 21:39 UTC)

<p>Thanks. Also found the ‘Markups to Model’ module quite useful for generating cylindrical paths for planning screw insertions.</p>

---
