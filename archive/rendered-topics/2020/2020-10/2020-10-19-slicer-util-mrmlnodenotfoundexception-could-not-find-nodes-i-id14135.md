---
topic_id: 14135
title: "Slicer Util Mrmlnodenotfoundexception Could Not Find Nodes I"
date: 2020-10-19
url: https://discourse.slicer.org/t/14135
---

# slicer.util.MRMLNodeNotFoundException: could not find nodes in the scene by name or id '' error

**Topic ID**: 14135
**Date**: 2020-10-19
**URL**: https://discourse.slicer.org/t/slicer-util-mrmlnodenotfoundexception-could-not-find-nodes-in-the-scene-by-name-or-id-error/14135

---

## Post #1 by @marianaslicer (2020-10-19 12:44 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.11.20200930<br>
Expected behavior: run a scripted python module without errors</p>
<p>Hello. I’m using a scripted python module on 3D slicer version 4.4 and it works as it should.<br>
However, when I use the same module in the 3D slicer version 4.11.20200930 it has different behavior and I’m getting this error message:</p>
<p>slicer.util.MRMLNodeNotFoundException: could not find nodes in the scene by name or id ‘’.<br>
Are there any changes in getting the imported data?</p>
<p>I would really appreciate your help.</p>
<p>Thanks,<br>
Mariana</p>

---

## Post #2 by @pieper (2020-10-19 12:56 UTC)

<p><code>getNode</code> is a helper function that used to return <code>None</code> when there were no matches, but in more recent Slicer it raises that exception to be explicit.  Now you need to add a catch it, <a href="https://github.com/Slicer/Slicer/blob/47deb76d7556e40de4e25e585c4b24a63a153da5/Base/Python/sitkUtils.py#L225-L232">something like this</a>.</p>

---

## Post #3 by @marianaslicer (2020-10-19 13:53 UTC)

<p>Thank you very much. It works!</p>

---

## Post #4 by @lassoan (2020-10-19 13:55 UTC)

<p>You can also use <code>slicer.mrmlScene.GetNodeByID()</code> as a drop-in replacement (if node is not found then it returns <code>None</code> instead of throwing an exception). Key differences between the two methods are described <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_node_object_from_the_scene_from_node_name_or_ID">here</a>.</p>

---
