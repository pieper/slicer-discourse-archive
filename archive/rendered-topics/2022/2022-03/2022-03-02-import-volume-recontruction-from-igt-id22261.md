---
topic_id: 22261
title: "Import Volume Recontruction From Igt"
date: 2022-03-02
url: https://discourse.slicer.org/t/22261
---

# Import Volume Recontruction from IGT

**Topic ID**: 22261
**Date**: 2022-03-02
**URL**: https://discourse.slicer.org/t/import-volume-recontruction-from-igt/22261

---

## Post #1 by @Karl-Philippe (2022-03-02 14:02 UTC)

<p>Hello,</p>
<p>I am trying to import the logic of the volumereconstruction module from the SlicerIGT extension for use in my own python script but I get an error saying that the module is not found even though I installed the SlicerIGT extension with the extension manager.</p>
<p>When I try to import the VolumeReconstruction module into the Python Interactor, I get the following error:</p>
<pre><code class="lang-auto">import volumereconstruction
Traceback (most recent call):
File "&lt;console&gt;", line 1, in &lt;module&gt;
ModuleNotFoundError: No module named 'volumereconstruction'.
</code></pre>
<p>However, when I try with another module like Elastics (<code>import Elastix</code> in the python Interactor or in my Python script), it works correctly.</p>
<p>I have seen that the Elastix module is a Scripted module while the Volume reconstruction module is a loadable module, is that the source of the problem? If this is the case, is it possible (and how) to import a loadable module?</p>
<p>I am working with Slicer 4.11.20210226 on Ubuntu 20.04.</p>
<p>Thanks!</p>

---

## Post #2 by @Isabella_Romero (2022-10-03 10:42 UTC)

<p>You could use the following code to implement the logic of Volume Reconstruction:<br>
logic=slicer.modules.volumereconstruction.logic()</p>

---
