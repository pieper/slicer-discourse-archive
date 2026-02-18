# New experimental feature: Boolean operations (union, intersection, difference) on meshes

**Topic ID**: 16048
**Date**: 2021-02-17
**URL**: https://discourse.slicer.org/t/new-experimental-feature-boolean-operations-union-intersection-difference-on-meshes/16048

---

## Post #1 by @lassoan (2021-02-17 23:56 UTC)

<p>We have added a new module - <strong>Combine models</strong> - to <em>Sandbox extension</em> to compute union, intersection, or subtraction operations on models (surface meshes).</p>
<p>This can be used to construct surgical guides and various other patient-specific devices by combining patient-specific meshes with CAD-designed parts.</p>
<p>See short demo here:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="2MOAk2oNbKw" data-video-title="Combine patient and CAD models in 3D Slicer using union/intersection/difference operations" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=2MOAk2oNbKw" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/2MOAk2oNbKw/maxresdefault.jpg" title="Combine patient and CAD models in 3D Slicer using union/intersection/difference operations" width="" height="">
  </a>
</div>

<p>Although Segment Editor can also combine models using Logical operators effect, this effect requires conversion of the mesh to a labelmap representation. Meshes that contain small, sharp features requires very fine resolution labelmap, resulting in high memory usage and long computation times.</p>
<p>The module relies on <a href="https://github.com/zippy84/vtkbool">vtkbool</a> package instead of VTK’s built-in Boolean operations filter, because vtkbool appears to be much more stable.</p>
<p>We would like to hear from users if these operations work well. If they do, then the feature will be made available in Slice core (as a new tool in Dynamic modeler module).</p>

---

## Post #2 by @lassoan (2021-02-18 00:03 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> and other 3D printing folks - we would like to hear from you. Do you find this feature useful? What can we do further improve your workflows?</p>

---

## Post #3 by @mikebind (2021-02-23 22:06 UTC)

<p>Thanks for tagging, I’ve passed this on to my 3D printer colleague.</p>

---

## Post #4 by @Selva (2021-02-24 04:47 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> where can I install this pls</p>
<p>It does not come up with extensions?</p>
<p>Thanks</p>

---

## Post #5 by @lassoan (2021-02-24 05:39 UTC)

<p>Sandbox extension shows up in the Examples category (you can also search for its name).</p>

---

## Post #6 by @Selva (2021-02-24 07:51 UTC)

<p>This is really helpful for custom designed implants</p>
<p>And even studying deformity cotrrection surgery</p>
<p>But I cannot visualise the output model</p>

---

## Post #7 by @John_Moore (2021-03-01 00:43 UTC)

<p>I’ve only used it a few times so far, but this is a very helpful feature for combining multiple segments, or adding labels to parts created in Slicer.</p>
<p>Prior to this functionality, I had to train people in using something like Meshmixer or Blender, in addition to Slicer. This simplifies the rapid prototyping workflow quite a lot. Thanks.</p>

---

## Post #8 by @Dexter777 (2021-03-03 02:48 UTC)

<p>Thank you. I found a Perk Lab video 3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications that will be helpful as well. And I installed the Sandbox extension.  This should streamline our process. I’ll let you know how it works. Thanks.</p>

---
