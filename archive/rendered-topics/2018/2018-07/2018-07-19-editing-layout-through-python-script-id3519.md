---
topic_id: 3519
title: "Editing Layout Through Python Script"
date: 2018-07-19
url: https://discourse.slicer.org/t/3519
---

# Editing Layout through Python script

**Topic ID**: 3519
**Date**: 2018-07-19
**URL**: https://discourse.slicer.org/t/editing-layout-through-python-script/3519

---

## Post #1 by @brynpitt (2018-07-19 03:11 UTC)

<p>Hello all,</p>
<p>I have a very simple problem: I am looking for reference information on changing Slicer’s layout using Python scripts. I know I found such a page in the past (for an older version of Slicer), but I cannot seem to find it again in the Wiki.</p>
<p>Ultimately, I would like to use a script so that I can launch Slicer with a customized layout (3D Only view, toolbars disabled, etc). For now, I am just trying to find the documentation for existing classes and functions.</p>
<p>Thanks,<br>
BP</p>

---

## Post #2 by @jamesobutler (2018-07-19 03:32 UTC)

<p>You might be looking for the <a href="https://www.slicer.org/wiki/Documentation/4.8/ScriptRepository" rel="nofollow noopener">ScriptRepository</a> wiki page. There is also the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting" rel="nofollow noopener">Python scripting</a> wiki page which has some good information.</p>
<p>Slicer does have a 3D Only view (View-&gt;Layout-&gt;3D Only) and the last view is saved and used when relaunching Slicer.</p>

---

## Post #3 by @pieper (2018-07-19 13:35 UTC)

<p><a class="mention" href="/u/brynpitt">@brynpitt</a> you may also want to look at the info on <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets">Slicelets</a>.</p>
<p>For the viewer layouts specifically, the <a href="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L296">CompareVolumesLogic</a> is an example of dynamically configuring the mrml layout nodes for various scenarios.</p>

---
