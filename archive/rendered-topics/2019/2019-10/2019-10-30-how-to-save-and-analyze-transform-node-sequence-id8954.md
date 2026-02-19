---
topic_id: 8954
title: "How To Save And Analyze Transform Node Sequence"
date: 2019-10-30
url: https://discourse.slicer.org/t/8954
---

# How to save and analyze transform node sequence?

**Topic ID**: 8954
**Date**: 2019-10-30
**URL**: https://discourse.slicer.org/t/how-to-save-and-analyze-transform-node-sequence/8954

---

## Post #1 by @Prashant_Pandey (2019-10-30 03:57 UTC)

<p>I’m recording the motion of a tracked tool using the sequences module. I am able to record the transform node as a sequence and play it back. How can I export this sequence as a series of timestamped matrices (such as .mha or even just a txt file format) so that I can open and analyze it externally (w/ python or matlab for example)? This is a very basic question but I can’t seem to find the correct doumentation anywhere.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2019-10-30 11:10 UTC)

<p>You can compute many metrics using PerkTutor extension and you can also run any custom analysis in Python, either using the interactive console or using Slicer as a Jupyter notebook kernel (using SlicerJupyter extension).</p>
<p>As far as I remember, you can also save export a linear transform sequence as an .mha file (<a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> <a class="mention" href="/u/ungi">@Ungi</a> do you know where?) and of course to can iterate through the sequence and write it to file in any format you prefer.</p>

---

## Post #3 by @Sunderlandkyl (2019-10-30 13:30 UTC)

<p>You should just be able to save your transform sequence as an mha using the regular save dialog (ctrl+s).</p>
<p>Under the file format for the sequence node it should read “Linear transform sequence (.seq.mha)”.</p>

---

## Post #4 by @mholden8 (2019-10-30 15:19 UTC)

<p>Yes, the Perk Evaluator module of the Perk Tutor extension is designed for exactly these purposes. There are already many metrics included as part of the module, and you can download more metrics directly from the Perk Evaluator module using the “Advanced &gt; Options” tab. See here for a list of available metrics: <a href="https://github.com/PerkTutor/PythonMetrics" rel="nofollow noopener">https://github.com/PerkTutor/PythonMetrics</a>.</p>
<p>But most importantly, it allows you to write your metrics and do your own analysis in Python. Please see here for details: <a href="https://github.com/PerkTutor/PerkTutor/wiki/Tutorials:-Perk-Evaluator" rel="nofollow noopener">https://github.com/PerkTutor/PerkTutor/wiki/Tutorials:-Perk-Evaluator</a>, <a href="https://github.com/PerkTutor/PerkTutor/wiki/User-Configurable-Metrics" rel="nofollow noopener">https://github.com/PerkTutor/PerkTutor/wiki/User-Configurable-Metrics</a>. Let us know if you have any questions or run into any difficulties.</p>

---

## Post #5 by @Prashant_Pandey (2019-10-30 17:33 UTC)

<p>Thanks all, Perk Tutor looks like exactly what I need.</p>
<p>The work/publications on the perk tutor page looks very relevant to my work. I’m curious if you are aware of anyone who has studied the effectiveness of different visualizations of images and tools (e.g. 2D or 3D visualizations, reslicing vs. static) for targeting? I am in the midst of planning a study where I vary the different views/angles shown to users and time how long it takes for them to line a tool trajectory with a target (a cylinder model), so it would be good to know if similar work has already been done (did not find any when searching google scholar, etc)</p>

---
