---
topic_id: 8977
title: "Extension Manager For Comparing Before And After Drill Holes"
date: 2019-10-31
url: https://discourse.slicer.org/t/8977
---

# Extension manager for comparing before and after drill holes in bone

**Topic ID**: 8977
**Date**: 2019-10-31
**URL**: https://discourse.slicer.org/t/extension-manager-for-comparing-before-and-after-drill-holes-in-bone/8977

---

## Post #1 by @mccarthyvetsurg (2019-10-31 21:01 UTC)

<p>Is there an extension in the extension manager that is similar to comparing the outcome of a proposed drill hole trajectory in a bone?</p>
<p>I am a surgeon working on drilling a hole and 3d printing  drill guides.  I want to be able to mathematically, area, etc. compare the trajectory of the  proposed hole to the hole that was drilled into a bone.  Or does anyone have a better idea for this? Thanks.</p>

---

## Post #2 by @lassoan (2019-11-01 04:33 UTC)

<p>How do you define the optimal drill trajectory? Using target point and entry point?</p>
<p>How do you determine the actual drill trajectory? Verification CT scan after drilling the hole?</p>
<p>There are several metrics that may be usable, such as distance of actual drill trajectory from target point and entry point, angle between optimal and actual trajectory, distance of actual entry point from optimal entry point. These metrics are so simple to compute (1-2 lines of code) that there is no module developed for them. If you clarify the questions above then we can provide code for a few metrics you are interested in that you can copy-paste into the Python console in Slicer.</p>

---

## Post #3 by @mccarthyvetsurg (2019-11-01 13:22 UTC)

<p>Yes. All of the above.  We are using a targeted point and entry point, post-drilling CT scan to evaluate the trajectory,</p>
<p>I am interested in distance from target point and entry point, comparison of the optimal trajectory to the actual.  If there are a few lines of code that can be written, that would be much appreciated!!!</p>
<p>Thank you.</p>

---

## Post #4 by @pieper (2019-11-01 13:40 UTC)

<p>Hi <a class="mention" href="/u/mccarthyvetsurg">@mccarthyvetsurg</a> - sounds like a really interesting project.  Is it possible you could share some deidentified sample data of the pre- and post-drilling CT for prototyping?</p>

---

## Post #5 by @lassoan (2019-11-01 16:09 UTC)

<p>Yes, a sample scene would be very useful. Without that it is hard to guess how you store the trajectories (markup points, lines, rulers, etc.; in how many nodes, etc). For this purpose it does not have to be a real image (a phantom or animal data set, or even any of the Slicer sample data sets would work, too).</p>

---

## Post #6 by @mccarthyvetsurg (2019-11-01 18:46 UTC)

<p>Yeah, I would rather not show a screen shot, I was just curious to see what was out there.  If there is some code that could be written, it basically would be to measure angles from a projected angle to the actual angle.</p>

---

## Post #7 by @lassoan (2019-11-04 04:12 UTC)

<p>You can use markups module in Latest Slicer Preview Release to compute angles (using markups angle nodes).</p>
<p>You can also access markups control point positions and do custom computations using numpy or VTK (or any other Python package). See for example a simple angle computation <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Measure_angle_between_two_slice_planes">here</a>.</p>
<p><a href="https://gist.github.com/lassoan/9bf334743871e400f7e3b3745b312b14">Here</a> is an example of a module that performs custom angle measurements based on ruler nodes. You can write similar modules for computing custom metrics based on other nodes (e.g., markups).</p>

---
