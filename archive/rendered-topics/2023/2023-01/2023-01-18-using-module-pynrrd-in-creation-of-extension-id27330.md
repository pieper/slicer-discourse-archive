# Using module pynrrd in creation of extension

**Topic ID**: 27330
**Date**: 2023-01-18
**URL**: https://discourse.slicer.org/t/using-module-pynrrd-in-creation-of-extension/27330

---

## Post #1 by @devD (2023-01-18 17:43 UTC)

<p>Hi,</p>
<p>I am currently creating an extension for Slicer that uses the model nrrd from pynrrd. However i get the error:<br>
ModuleNotFoundError: No module named ‘nrrd’</p>
<p>(I installed pynrrd by using “pip install pynrrd”)</p>
<p>What could this depend on and can it be fixed?</p>
<p>Thank you</p>

---

## Post #2 by @mau_igna_06 (2023-01-18 18:30 UTC)

<p>Maybe try:</p>
<pre><code class="lang-auto">import pynrrd
</code></pre>
<p>Hope it helps</p>

---
