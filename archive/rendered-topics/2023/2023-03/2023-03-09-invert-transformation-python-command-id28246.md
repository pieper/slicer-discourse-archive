# Invert transformation Python Command?

**Topic ID**: 28246
**Date**: 2023-03-09
**URL**: https://discourse.slicer.org/t/invert-transformation-python-command/28246

---

## Post #1 by @nalindgr (2023-03-09 02:33 UTC)

<p>Hi!</p>
<p>I have a loaded displacement field and a loaded volume that I want to transform by the inverse.<br>
In Slicer GUI, when applying the transform, one can easily check the “Invert” box.<br>
How do I specify that I want to do an invert transform in my Python script?</p>
<blockquote>
<p>inputDisplacementfield = mainFolder+‘displacementfield.mhd’<br>
inputTemplateVolume = mainFolder+‘volume.nrrd’<br>
loadedDisplacementfield = slicer.util.loadTransform(inputDisplacementfield)<br>
loadedTemplateVolume = slicer.util.loadVolume(inputTemplateVolume)</p>
<p>displacementfield_node = slicer.util.getNode(“displacementfield”)<br>
/# Here I want to invert the transform<br>
templateVolume_node = slicer.util.getNode(“volume”)</p>
</blockquote>
<p>Any advice?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @pieper (2023-03-09 14:52 UTC)

<p>If you don’t get a specific answer here, there are general instructions: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features</a></p>

---
