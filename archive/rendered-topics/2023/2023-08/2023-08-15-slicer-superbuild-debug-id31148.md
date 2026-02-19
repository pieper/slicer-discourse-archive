---
topic_id: 31148
title: "Slicer Superbuild Debug"
date: 2023-08-15
url: https://discourse.slicer.org/t/31148
---

# Slicer-SuperBuild-Debug

**Topic ID**: 31148
**Date**: 2023-08-15
**URL**: https://discourse.slicer.org/t/slicer-superbuild-debug/31148

---

## Post #1 by @Kening_Zhang (2023-08-15 09:18 UTC)

<pre><code class="lang-auto">$ mkdir MyExtension-debug
$ cd MyExtension-debug
$ cmake -DCMAKE_BUILD_TYPE:STRING=Debug -DSlicer_DIR:PATH=/path/to/Slicer-SuperBuild-Debug/Slicer-build ../MyExtension
$ make
</code></pre>
<p>Here I cannot find <code>Slicer-SuperBuild-Debug</code> in my Slicer package, I just downloaded Slicer before, should I build it? If so, is there some tutorial?<br>
Best wishes,<br>
Zhang Kening</p>

---

## Post #2 by @pieper (2023-08-15 16:32 UTC)

<p>To build any extension with C++ code you need to also have built Slicer on your machine (not just downloaded a binary).</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html</a></p>

---

## Post #3 by @Kening_Zhang (2023-08-15 18:26 UTC)

<p>Sorry I only use Python to form my extension, does that means I also nedd C++?</p>

---

## Post #4 by @jcfr (2023-08-15 20:33 UTC)

<blockquote>
<p>Sorry I only use Python to form my extension, does that means I also nedd C++?</p>
</blockquote>
<p>To elaborate on <a class="mention" href="/u/pieper">@pieper</a> answer, it is not required to build Slicer if you intend to only write a Slicer module using Python.</p>
<p>Reading the  <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#extensions"> Extensions / Create an extension</a> page should be informative.</p>
<p>It will lead you to use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/extensionwizard.html#extension-wizard">ExtensionWizard</a> available in the Slicer package you download from <a href="https://download.slicer.org">https://download.slicer.org</a></p>
<p>When adding a module, simply select <code>scripted</code> and start developing <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=12" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @Kening_Zhang (2023-08-15 20:38 UTC)

<p>I already use Wizard to create a extension, but now I want to try it by extension manager, may be try it offline first, which step I should move to confuses me a lot. Thank u very much.</p>

---
