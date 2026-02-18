# How to use ProbeFilter command?

**Topic ID**: 22467
**Date**: 2022-03-12
**URL**: https://discourse.slicer.org/t/how-to-use-probefilter-command/22467

---

## Post #1 by @Muhammed_Fatih_Talu (2022-03-12 15:37 UTC)

<p>I have Volume and Model data.<br>
I can use ProbeVolumeWithModel and produce an OutputModel using Slicer.<br>
But I have to do this in code (Python) using Notebook.<br>
If there is an example usage of ProbeVolume, can you guide me?<br>
Thanks…</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5af89b775d464176e8d734081ebe43ed5e02d74e.png" alt="image" data-base62-sha1="cYLBSH74v8YvHBbKjP7MO1LfyNg" width="687" height="173"></p>

---

## Post #4 by @Muhammed_Fatih_Talu (2022-03-12 19:56 UTC)

<p>I found the answer to my question. As follows:</p>
<pre><code class="lang-auto">#Parameters for ProbeVolumeWithModel
parameters = {}
parameters["InputVolume"] = InputVolumeNode.GetID()
parameters["InputModel"] = InputModelNode.GetID()
parameters["OutputModel"] = OutputModelNode.GetID()

probe = slicer.modules.probevolumewithmodel
slicer.cli.run(probe, None, parameters, wait_for_completion=True)
</code></pre>

---
