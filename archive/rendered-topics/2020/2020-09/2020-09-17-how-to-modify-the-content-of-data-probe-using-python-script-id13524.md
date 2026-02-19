---
topic_id: 13524
title: "How To Modify The Content Of Data Probe Using Python Script"
date: 2020-09-17
url: https://discourse.slicer.org/t/13524
---

# How to modify the content of "data probe" using python script

**Topic ID**: 13524
**Date**: 2020-09-17
**URL**: https://discourse.slicer.org/t/how-to-modify-the-content-of-data-probe-using-python-script/13524

---

## Post #1 by @valery (2020-09-17 11:25 UTC)

<p>Hi everybody,</p>
<p>I’m looking for a bit of help. I would like to modify the content of “data probe” in python script inside Slicer.<br>
For instance : how to</p>
<ul>
<li>activate the colorbar on the overlay</li>
<li>enable/disable corner text annotation</li>
<li>change font properties</li>
</ul>
<p>Maybe I missed it in the documentation, don’t hesitate to refer to it. Thanks a lot.<br>
Valéry</p>

---

## Post #2 by @lassoan (2020-09-17 19:48 UTC)

<p>See examples in script repository  - <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Hide_slice_view_annotations_.28DataProbe.29">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Hide_slice_view_annotations_.28DataProbe.29</a></p>
<p>If you don’t find how to access a specific function then have a look at the <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Scripted/DataProbe/DataProbeLib">DataProbe module source code</a> (it is implemented in Python) and take out or call the relevant code snippet.</p>

---
