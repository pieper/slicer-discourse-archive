---
topic_id: 23238
title: "Loadable Custom Markups How To Install The Packaged Extensio"
date: 2022-05-02
url: https://discourse.slicer.org/t/23238
---

# Loadable custom markups : how to install the packaged extension

**Topic ID**: 23238
**Date**: 2022-05-02
**URL**: https://discourse.slicer.org/t/loadable-custom-markups-how-to-install-the-packaged-extension/23238

---

## Post #1 by @chir.set (2022-05-02 14:03 UTC)

<p>I’m in the very early stages trying to create a loadable custom markups in C++, using extension wizard’s template. I can build the extension and module outside Slicer’s build tree, and create an extension package.</p>
<ol>
<li>When the lib directory of this package is simply copied to Slicer’s lib directory, I can make the custom markups appear in th eMarkups module and use it with this code in Python console :</li>
</ol>
<pre><code class="lang-auto">d = slicer.vtkMRMLMarkupsCustomNode()
w = slicer.vtkSlicerCustomWidget()
l=slicer.modules.markups.logic()
l.RegisterMarkupsNode(d, w)
</code></pre>
<ol start="2">
<li>If I install the extension with the Extension Manager pointing to the local file, it gets rightly unpacked in NA-MIC/Extensions-30783/. However, on restart, the custom markups button is not available in the Markups module. And the above code fails, vtkMRMLMarkupsCustomNode is not found.</li>
</ol>
<p>I expected, perhaps wrongly, that <span class="hashtag">#2</span> would make the custom markups available transparently. How can we reach a nice development workflow in this context ?</p>
<p>Thank you.</p>

---

## Post #2 by @chir.set (2022-05-02 17:22 UTC)

<p>Ok, I could solve it by starting Slicer with <em>–additional-module-paths</em> pointing to the lib directory of the module build tree. The ‘Testing’ checking should also be removed in <em>qSlicerCustomModule::setup()</em> and <em>qSlicerCustomModule::createLogic()</em>.</p>
<p>By the way, what’s this <em>qSlicerCoreApplication::AA_EnableTesting</em> flag ? Greping Slicer source and Slicer-build/*, it appears only in compiled binaries and the qSlicerTemplateKeyModule.cxx files.</p>

---
