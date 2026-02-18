# Switch to Editor module by command line

**Topic ID**: 8492
**Date**: 2019-09-19
**URL**: https://discourse.slicer.org/t/switch-to-editor-module-by-command-line/8492

---

## Post #1 by @cogitas3d (2019-09-19 03:22 UTC)

<p>Hey there!</p>
<p>I would like to know if its possible open Slicer directly in “Editor” module.</p>
<p>More than this, if its possible open in ThresholdEffect, settinf the dicom file before.</p>
<p>Usually I use:</p>
<blockquote>
<p>./Slicer “/tmp/tmpz_9y59ib/0/0001.dcm”</p>
</blockquote>
<p>This open the DICOM, but I would like to let all right to see the Hounsfield value.</p>
<p>Is it possible?</p>
<p>Thank you for the attention. A big hug!</p>

---

## Post #2 by @lassoan (2019-09-19 03:38 UTC)

<p>These examples should help with applying segment editor effects from scripts: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>
<p>You can find general information and tutorials about Python scripting in Slicer here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting</a></p>

---

## Post #3 by @cogitas3d (2019-09-28 20:04 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>!</p>
<p>I solve it asking directly for the user open Slicer by Blender (OrtogOnBlender).</p>
<p>The video shows (in Portuguese) how we solve this: <a href="https://www.youtube.com/watch?v=DdjCrmVfq-Y" rel="nofollow noopener">https://www.youtube.com/watch?v=DdjCrmVfq-Y</a></p>
<p>Thank you very much!</p>

---

## Post #4 by @lassoan (2019-09-28 20:38 UTC)

<p>I’ve noticed that you use the Editor module, which is deprecated for about two years and will be removed soon. It is replaced by Segment Editor module. It has much more powerful tools than the old Editor and you can export the segmentation to OBJ file (that can be loaded directly into Blender) by two clicks.</p>
<p>Could you summarize what happens in the video? I could not catch the mean idea without understanding the voice over.</p>

---
