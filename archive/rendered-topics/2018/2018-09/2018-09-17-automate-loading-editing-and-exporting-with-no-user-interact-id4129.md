---
topic_id: 4129
title: "Automate Loading Editing And Exporting With No User Interact"
date: 2018-09-17
url: https://discourse.slicer.org/t/4129
---

# Automate loading, editing and exporting with no user interaction

**Topic ID**: 4129
**Date**: 2018-09-17
**URL**: https://discourse.slicer.org/t/automate-loading-editing-and-exporting-with-no-user-interaction/4129

---

## Post #1 by @javi0unavailable (2018-09-17 04:20 UTC)

<p>Greetings.</p>
<p>I want to help a doctor friend to achieve what the title says. I have no idea from medical argot but I know about software development.</p>
<p>Basically what I need is to know the easiest way to automate a few steps:</p>
<ul>
<li>Import and Load DICOM from a specified folder.</li>
<li>Use Editor module with ThresholdEffect (submodule?) to adjust the lower threshold with a specified number.</li>
<li>Again, use Editor module now with MakeModelEffect to generate 3d model</li>
<li>Export model generated in .stl</li>
</ul>
<p>I see I can open Slicer from command line but don’t know if is possible to execute all I described before from command line.</p>
<p>Other way I see is developing a new custom module with Python that ‘calls’ the others modules (load DICOM, ThresholdEffect, MakeModelEffect, Export). I found an API (<a href="http://apidocs.slicer.org/master/" rel="nofollow noopener">http://apidocs.slicer.org/master/</a>) but I could not find any like ThresholdEffect method or something.</p>
<p>So… command line? new python module? other way?</p>
<p>Hope you can point me the right direction.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2018-09-17 04:27 UTC)

<aside class="quote no-group" data-username="javi0unavailable" data-post="1" data-topic="4129">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/0ea827/48.png" class="avatar"> javi0unavailable:</div>
<blockquote>
<p>Import and Load DICOM from a specified folder.</p>
</blockquote>
</aside>
<p>This is described in this topic: <a href="https://discourse.slicer.org/t/load-dicom-series-using-python/3257/2" class="inline-onebox">Load DICOM series using python - #2 by cpinter</a></p>
<aside class="quote no-group" data-username="javi0unavailable" data-post="1" data-topic="4129">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/0ea827/48.png" class="avatar"> javi0unavailable:</div>
<blockquote>
<ul>
<li>Use Editor module with ThresholdEffect (submodule?) to adjust the lower threshold with a specified number.</li>
<li>Again, use Editor module now with MakeModelEffect to generate 3d model</li>
</ul>
</blockquote>
</aside>
<p>Use Segment Editor module instead (the legacy Editod module is being phased out). See example for simple thresholding and model generation here (in particular, skin surface extraction example shows everything you need):</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>
<aside class="quote no-group" data-username="javi0unavailable" data-post="1" data-topic="4129">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/0ea827/48.png" class="avatar"> javi0unavailable:</div>
<blockquote>
<p>I see I can open Slicer from command line</p>
</blockquote>
</aside>
<p>Probably the simplest is to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_run_slicer_operations_from_a_batch_script.3F">specify a Python script that Slicer will execute</a>.</p>

---
