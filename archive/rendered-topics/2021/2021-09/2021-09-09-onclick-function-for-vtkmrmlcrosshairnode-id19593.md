# onClick() function for vtkMRMLCrosshairNode?

**Topic ID**: 19593
**Date**: 2021-09-09
**URL**: https://discourse.slicer.org/t/onclick-function-for-vtkmrmlcrosshairnode/19593

---

## Post #1 by @shatz (2021-09-09 11:52 UTC)

<p>Currently working on a python extension. I want to know ras coords for where the user clicks in the Crosshair Node.</p>
<p>I see that we have <code>CursorPositionModifiedEvent</code>, but this fires every time the cursor moves. I want an event that fires only when the user clicks. Cant find it in the class reference for <a href="https://apidocs.slicer.org/v4.8/classvtkMRMLCrosshairNode.html#details" rel="noopener nofollow ugc">crosshairnode</a> nor its <a href="https://apidocs.slicer.org/v4.8/classvtkMRMLNode.html#a75940c80287f5ebfd922d3ecf1c2d0d7" rel="noopener nofollow ugc">parent class</a> <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=10" title=":frowning:" class="emoji" alt=":frowning:"></p>
<p>Im sure this functionality exists, just not under whatever function name im expecting haha.</p>

---

## Post #2 by @lassoan (2021-09-10 04:38 UTC)

<p>We usually want users to be able to see the clicked positions and adjust them as needed, so we use markup fiducials. If you really just want to get clicks from the user and immediately start processing based on those points, then you can do that by adding observers to the markups node. See for example how this is done in the LungCTAnalyzer extension’s <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/tree/master/LungCTSegmenter">Lung CT segmenter module</a>:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="fpLxm7uAvZQ" data-video-title="Automated lung CT segmentation and analysis for COVID-19 assessment" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=fpLxm7uAvZQ" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/fpLxm7uAvZQ/maxresdefault.jpg" title="Automated lung CT segmentation and analysis for COVID-19 assessment" width="" height="">
  </a>
</div>


---

## Post #3 by @shatz (2021-09-12 08:11 UTC)

<p>Wow this is great, thanks!</p>

---
