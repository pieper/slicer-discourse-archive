---
topic_id: 10647
title: "Using Slicer In Clusters"
date: 2020-03-11
url: https://discourse.slicer.org/t/10647
---

# Using slicer in clusters

**Topic ID**: 10647
**Date**: 2020-03-11
**URL**: https://discourse.slicer.org/t/using-slicer-in-clusters/10647

---

## Post #1 by @Aep93 (2020-03-11 17:43 UTC)

<p>Hello all,<br>
Are there any special tutorials on how to use slicer on clusters?<br>
I mean in the cases that we generally do not have access to the GUI. Is there any way to generate the commands for all tasks we do in GUI?<br>
Thanks</p>

---

## Post #2 by @lassoan (2020-03-11 18:18 UTC)

<p>Yes, you can use Slicer on <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_run_Slicer_on_a_headless_compute_node.3F">headless compute nodes</a> and all features should be accessible via Python scripting.</p>

---

## Post #3 by @Aep93 (2020-03-11 19:46 UTC)

<p>Thank you very much for your response. Are there any tools to get something like a log file which shows the codes for the tasks I do in GUI so that I can use them in the cluster?<br>
Or is there any source which mentions all codes for all tasks like opening files, installing extension .etc ?<br>
Thanks</p>

---

## Post #4 by @lassoan (2020-03-12 22:38 UTC)

<p>There is no simple shortcut like that. <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">Developer tutorials</a> and the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python">script repository</a> should help you getting started.</p>

---
