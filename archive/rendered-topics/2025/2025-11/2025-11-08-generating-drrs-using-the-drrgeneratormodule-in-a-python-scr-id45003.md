# Generating DRRs using the DRRGeneratorModule in a Python Script

**Topic ID**: 45003
**Date**: 2025-11-08
**URL**: https://discourse.slicer.org/t/generating-drrs-using-the-drrgeneratormodule-in-a-python-script/45003

---

## Post #1 by @fmarcantoni (2025-11-08 06:50 UTC)

<p>Hello everyone,</p>
<p>I’m been using 3D slicer for a couple of weeks now, and I’ve been using the DRRGeneratorModule extension to create DRRs of a volume. Now, I’m trying to change the module parameters and run the generation through a python script rather than through the GUI, running this python script on my Linux terminal externally from 3D slicer. I cannot figure out how to modify the parameters or generate the DRRs. I can access the module logic as follows: slicer.modules.drrgeneratormodule.logic()</p>
<p>But I don’t know how to proceed after this. I also found this problem on Github which is the exact same issue not resolved: <a href="https://github.com/lancelevine/SlicerDRRGenerator/issues/10" class="inline-onebox" rel="noopener nofollow ugc">Using the module in a python script · Issue #10 · lancelevine/SlicerDRRGenerator · GitHub</a></p>
<p>Please let me know if you know how I could go on with this, thank you.</p>

---

## Post #2 by @ebrahim (2025-11-09 21:36 UTC)

<aside class="quote no-group" data-username="fmarcantoni" data-post="1" data-topic="45003">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fmarcantoni/48/81384_2.png" class="avatar"> fmarcantoni:</div>
<blockquote>
<p>slicer.modules.drrgeneratormodule.logic()</p>
</blockquote>
</aside>
<p>I am not certain but I suspect this might construct a new logic rather than grabbing the one that is associated with the module you’ve already loaded into Slicer. To grab the already existing logic:</p>
<pre data-code-wrap="python"><code class="lang-python">slicer.util.getModuleLogic("DRRGeneratorModule")
</code></pre>
<p>Here is a good place to get started with accessing module logic methods: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#calling-methods-of-a-module-logic" class="inline-onebox" rel="noopener nofollow ugc">Python FAQ — 3D Slicer documentation</a></p>

---
