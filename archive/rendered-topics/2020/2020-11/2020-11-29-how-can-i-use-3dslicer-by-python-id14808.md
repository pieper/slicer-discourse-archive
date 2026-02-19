---
topic_id: 14808
title: "How Can I Use 3Dslicer By Python"
date: 2020-11-29
url: https://discourse.slicer.org/t/14808
---

# How can I use 3DSlicer by python?

**Topic ID**: 14808
**Date**: 2020-11-29
**URL**: https://discourse.slicer.org/t/how-can-i-use-3dslicer-by-python/14808

---

## Post #1 by @zhang-qiang-github (2020-11-29 18:58 UTC)

<p>Thanks for all developer for 3D slicer. Currently, I want to use the semi-automatic segmentation method of 3D slicer in python.</p>
<ol>
<li>Can I install 3D slicer by <code>pip install slicer</code>?</li>
<li>Which module of 3D slicer is designed for semi-automatic segmentation?</li>
</ol>
<p>It is appreciated for any suggestion.</p>

---

## Post #2 by @lassoan (2020-11-29 19:00 UTC)

<p>Slicer has a Python environment set up and you can install in it any additional Python packages that you need (using the <code>pip_install()</code> convenience function). You can find examples of using segmentation tools from Python in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">script repository</a>.</p>

---
