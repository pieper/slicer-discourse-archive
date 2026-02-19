---
topic_id: 27221
title: "How To Set Private Extension"
date: 2023-01-13
url: https://discourse.slicer.org/t/27221
---

# How to set private extension?

**Topic ID**: 27221
**Date**: 2023-01-13
**URL**: https://discourse.slicer.org/t/how-to-set-private-extension/27221

---

## Post #1 by @dsa934 (2023-01-13 06:01 UTC)

<p>Operating system: Window 11<br>
Slicer version: 4.13.0</p>
<p>Previously, I copied and pasted the code into the Python Interactor every time I ran the code to make sure the Python module worked properly within the 3D slicer. This is because if the module does not operate normally, it is impossible to determine whether the Python module extension method is wrong or my code is wrong.</p>
<p>With the help of many people, I was able to complete the custom module I wanted. thank you.<br>
However, there is still some work left to improve the usability of the module. Extensions are essential because events such as mouse and keyboard clicks and modules must be linked.</p>
<p>Therefore, I need a private module extension method for testing.<br>
What part of the document should I refer to?</p>
<p>Specifically, I would like to know if the extension’s private or public mode changes depending on what action is taken when following the module extension guide.</p>

---

## Post #2 by @RafaelPalomar (2023-01-13 06:41 UTC)

<blockquote>
<p>Operating system: Window 11<br>
Slicer version: 4.13.0</p>
<p>Previously, I copied and pasted the code into the Python Interactor every time I ran the code to make sure the Python module worked properly within the 3D slicer. This is because if the module does not operate normally, it is impossible to determine whether the Python module extension method is wrong or my code is wrong.</p>
</blockquote>
<p>When developing your extensions it is useful to enable the <em>developer mode</em> (you can do this in Edit &gt; Application Settings &gt; Developer &gt; Developer Mode). This, by default, creates a new set of buttons for the scripted modules (these are located on each scripted module side panel): Reload, Reload and Test, Edit and Restart Slicer. These are very useful to make your development a little bit more interactive since you can change your code and reload it without (mostly) the need to restart Slicer. The test button will launch the tests located in the Test class of your module.</p>
<blockquote>
<p>With the help of many people, I was able to complete the custom module I wanted. thank you.<br>
However, there is still some work left to improve the usability of the module. Extensions are essential because events such as mouse and keyboard clicks and modules must be linked.</p>
<p>Therefore, I need a private module extension method for testing.<br>
What part of the document should I refer to?</p>
</blockquote>
<p>There is testing documentation here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#test-an-extension" class="inline-onebox" rel="noopener nofollow ugc">Extensions — 3D Slicer documentation</a>. I personally find very useful to have a look at well-established extensions to learn how to do better testing code.</p>
<blockquote>
<p>Specifically, I would like to know if the extension’s private or public mode changes depending on what action is taken when following the module extension guide.</p>
</blockquote>
<p>I understand that you want to know about the requiements you need to comply with to make your extension available through the extension manager. There is documentation on how to develop and release an extension (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#distribute-an-extension" class="inline-onebox" rel="noopener nofollow ugc">Extensions — 3D Slicer documentation</a>), as well as a checklist you need to comply with (<a href="https://github.com/Slicer/ExtensionsIndex/blob/main/.github/PULL_REQUEST_TEMPLATE.md#todo-list-for-submitting-a-new-extension" rel="noopener nofollow ugc">https://github.com/Slicer/ExtensionsIndex/blob/main/.github/PULL_REQUEST_TEMPLATE.md#todo-list-for-submitting-a-new-extension</a>)</p>

---

## Post #3 by @dsa934 (2023-01-13 06:55 UTC)

<h2><a name="p-88831-test-an-extension-1" class="anchor" href="#p-88831-test-an-extension-1" aria-label="Heading link"></a>Test an extension</h2>
<h3><a name="p-88831-run-slicer-with-your-custom-modules-2" class="anchor" href="#p-88831-run-slicer-with-your-custom-modules-2" aria-label="Heading link"></a>Run Slicer with your custom modules</h3>
<p>To test an extension, you need to specify location(s) where Slicer should look for additional modules.</p>
<ul>
<li>If the extension is not built: add all source code folders that contain module .py files to “additional module paths” in modules section in application settings.</li>
</ul>
<p>If you test by adding the path, is it correct to test only on the local side, not to expose the module?<br>
If this is correct then this is the answer I was looking for.</p>
<p>After all the code is complete, I want to remove the security part and release it.</p>
<p>edit:</p>
<p>What’s the ‘Module .py file’ in 3D slicer?<br>
I know that the python file itself functions as a module, but is it different in 3d slicer?</p>
<p>I guess I asked too hastily. I’ll read the doc properly again and come back. I’m sorry</p>

---
