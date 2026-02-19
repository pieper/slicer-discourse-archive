---
topic_id: 19189
title: "Can I Import Slicer By Python"
date: 2021-08-13
url: https://discourse.slicer.org/t/19189
---

# Can I import slicer by python?

**Topic ID**: 19189
**Date**: 2021-08-13
**URL**: https://discourse.slicer.org/t/can-i-import-slicer-by-python/19189

---

## Post #1 by @zhang-qiang-github (2021-08-13 23:13 UTC)

<p>Can I install slicer in python by</p>
<pre><code class="lang-auto">pip install slicer
or
pip install pyslicer
</code></pre>
<p>I can’t find such a way.</p>
<p>I know that I can firstly compile 3D slicer in c++, and then wrap it with python. But, I have compiled 3D slicer several times, and all failed.</p>
<p>Hope a simple way to install 3D slicer in python.</p>

---

## Post #2 by @lassoan (2021-08-14 13:46 UTC)

<p>Slicer is not distributed on PyPI. You need to download the Slicer installation package and run the Slicer executable, which embeds Python. You can pip-install any Python packages in this Slicer’s embedded Python environment. You can also run Slicer as <a href="https://github.com/Slicer/SlicerJupyter/">Jupyter notebook kernel</a>.</p>
<p>How would you like to use Slicer? What kind of data do you work with?</p>

---
