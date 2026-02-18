# Algorithm used for growing seeds

**Topic ID**: 11817
**Date**: 2020-06-01
**URL**: https://discourse.slicer.org/t/algorithm-used-for-growing-seeds/11817

---

## Post #1 by @flaviu2 (2020-06-01 17:43 UTC)

<p>Hello everyone. I saw on youtube an interesting liver segmentation done it by growing by seeds: <a href="https://www.youtube.com/watch?v=R-lBsqAvSTA" rel="nofollow noopener">https://www.youtube.com/watch?v=R-lBsqAvSTA</a> (at the ending of the movie is liver segmentation).</p>
<p>Is there any way to know what ITK filters has been used for this “<strong>growing from seeds</strong>” approach ? I really need to do in my project. As you see, the user must define <em>an inside organ seeds</em>, <strong>AND</strong> <em>outside the organ seeds</em>. In which ITK filters  can I use those two seeds array, one from inside organ, another one from outside of organ ? Can you guide me a little bit please ?</p>
<p>Regards,<br>
Flaviu.</p>

---

## Post #2 by @lassoan (2020-06-01 17:55 UTC)

<p>There are region growing based segmentation algorithms in ITK, but in “Grows from seeds” effect we use a custom grow-cut based method, which was implemented from scratch many years ago and has been continuously improved based on lots of user feedback.</p>
<p>The simplest is to use it from Python, either <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">using segment editor effect API</a> or as a plain VTK image filter (<code>slicer.vtkImageGrowCutSegment</code>).</p>
<p>If you work in C++ then you can use the filter as is (it is a VTK filter that has no other dependency than VTK) or with a little work you should be able to port it to an ITK remote module. See source code <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkImageGrowCutSegment.h">here</a>.</p>

---
