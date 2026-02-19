---
topic_id: 35778
title: "Generate Animations Easily Based On Keyframes In Slicer"
date: 2024-04-28
url: https://discourse.slicer.org/t/35778
---

# Generate animations easily based on keyframes in Slicer

**Topic ID**: 35778
**Date**: 2024-04-28
**URL**: https://discourse.slicer.org/t/generate-animations-easily-based-on-keyframes-in-slicer/35778

---

## Post #1 by @muratmaga (2024-04-28 04:01 UTC)

<p>SlicerMorph has a module called Animator that allows creating movies that are not possible to do with default Screen Capture module. eg.</p><div class="youtube-onebox lazy-video-container" data-video-id="oGtvTOhIFtA" data-video-title="SlicerAnimator" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=oGtvTOhIFtA" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/oGtvTOhIFtA/maxresdefault.jpg" title="SlicerAnimator" width="" height="">
  </a>
</div>

<p>It includes things like cropping volumes, interpolating between different transfer functons and rotating at different axes. However, its usage is complex and setting volume properties correctly is difficult and quite error prone. It also doesn’t work with the RGBA rendering provided by Colorize Volumes module in Sandbox.</p>
<p>I would like to see a tool (within SlicerMorph or core Slicer) that will provide this functionality more easily. The basic idea is that people should take snapshots of the views as keyframes, adjust them on a time track and the module will do the necessary interpolations based on these keyframes.</p>
<p>A possibility is to use Scene Views for this, but as I understand there are certain issues about it making it less than ideal. Please feel free to comment on it, if you have ideas about this functionality.</p>

---
