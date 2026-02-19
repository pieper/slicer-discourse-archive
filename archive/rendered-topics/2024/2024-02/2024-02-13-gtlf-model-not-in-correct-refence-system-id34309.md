---
topic_id: 34309
title: "Gtlf Model Not In Correct Refence System"
date: 2024-02-13
url: https://discourse.slicer.org/t/34309
---

# Gtlf model not in correct refence system

**Topic ID**: 34309
**Date**: 2024-02-13
**URL**: https://discourse.slicer.org/t/gtlf-model-not-in-correct-refence-system/34309

---

## Post #1 by @Caterina (2024-02-13 20:41 UTC)

<p>Dear support,<br>
I exported a model (result of Slicer segmentation), using Open Anatomy, and I visualized it in Unity environment. The model seems to be not in correct position in the reference system. More specifically, the visualization box seems to be clearly superior to the model, as if the origin of the two reference systems were different. Any suggestions? Thanks</p>

---

## Post #2 by @lassoan (2024-02-27 14:08 UTC)

<p>Unity computes the bounding box. Slicer does not have any influence on how that operation is performed. Therefore, this is a problem in your Unity glTF importer or in how you use it. Check your code and if you are completely sure that you do everything correctly then you can report the problem to the developers of the glTF importer plugin.</p>
<p>I suspect the issue is around the “matrix” property in the file, which specifies how to convert coordinates from LPS coordinate system (in millimeters, this is used for the model point coordinates) to LSA coordinate system (in meters, this is the glTF world coordinate system). It is a complex topic, further complicated by the fact that glTF uses right-handed coordinate system while Unity uses left-handed. Developers and users of the glTF importer plugin in Unity have been struggling with this (see for example <a href="https://github.com/KhronosGroup/UnityGLTF/issues/319">here</a>) and maybe not all problems have been fixed or it perhaps it is easy to misuse the imported data.</p>
<p>Note that until recently the only way to use Slicer with HoloLens was to use Unity (or other graphics engine, but Unity has been the most popular). Since about a month ago, this extra layer of complexity is no longer needed. Slicer can directly render the 3D scene (including volume rendering, 4D time sequence data display, GUI widgets, etc.) in the HoloLens, using SlicerVirtualReality extension. See for example this <a href="https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/ArInSlicer/">AR project from the last Slicer Project Week</a>:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="rlEyJWCXmk8" data-video-title="OpenXR integration in 3D Slicer with demonstration in birth delivery training" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=rlEyJWCXmk8" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/rlEyJWCXmk8/maxresdefault.jpg" title="OpenXR integration in 3D Slicer with demonstration in birth delivery training" width="" height="">
  </a>
</div>


---
