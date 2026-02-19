---
topic_id: 9039
title: "Automation Of Create Dicom File Step"
date: 2019-11-06
url: https://discourse.slicer.org/t/9039
---

# Automation of Create Dicom File step

**Topic ID**: 9039
**Date**: 2019-11-06
**URL**: https://discourse.slicer.org/t/automation-of-create-dicom-file-step/9039

---

## Post #1 by @deepz (2019-11-06 05:28 UTC)

<p>Hello Everyone.<br>
I wanted to automate the ‘create Dicom files’ from vol files. The conversion pipeline should be like the user just needs to import the vol files .</p>
<ol>
<li>It passes through slicer 3d. it gives the Dicom files.</li>
<li>The Dicom files go through a Unity plugin for an asset file creation.</li>
</ol>
<p>The two steps need to be condensed to one. I wanted to know how the automation of the first step can be done. Do I need to use python? Or, can it be done in C# if possible?</p>

---

## Post #2 by @pieper (2019-11-06 14:21 UTC)

<p>No C# in Slicer, just Python or C++.  For what you describe I’d suggest Python.</p>

---
