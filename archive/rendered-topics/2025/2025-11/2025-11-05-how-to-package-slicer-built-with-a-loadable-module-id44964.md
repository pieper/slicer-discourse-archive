---
topic_id: 44964
title: "How To Package Slicer Built With A Loadable Module"
date: 2025-11-05
url: https://discourse.slicer.org/t/44964
---

# How to package Slicer built with a loadable module?

**Topic ID**: 44964
**Date**: 2025-11-05
**URL**: https://discourse.slicer.org/t/how-to-package-slicer-built-with-a-loadable-module/44964

---

## Post #1 by @Suhaim (2025-11-05 05:27 UTC)

<p>Hi everyone,<br>
I am creating this post as a reference for anyone who was wondering on how to package slicer built with a custom loadable module. I was not able to find any documentation on this, please correct me if I am wrong.</p>

---

## Post #2 by @Suhaim (2025-11-05 05:35 UTC)

<p>There are a few steps to do this for <strong>linux</strong>(I only did this on linux) :-</p>
<ol>
<li>
<p>Package slicer built from source as mentioned in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html" rel="noopener nofollow ugc">build instructions</a>.</p>
</li>
<li>
<p>Extract the compressed file that was generated in some directory.</p>
</li>
<li>
<p>Inside the build directory containing slicer built with the loadable module, run</p>
<pre><code class="lang-auto">make package
</code></pre>
</li>
<li>
<p>Extract the contents of the compressed file in another folder.</p>
<ol>
<li>On linux, three folders will be generate for the packaged extension(include, lib, share).</li>
</ol>
</li>
<li>
<p>Merge the three folders of the packaged extension with the same folders inside entire packaged slicer.</p>
<ol>
<li>Merge the extension’s include, lib, share with the directories of same name but inside packaged slicer’s directory.</li>
</ol>
</li>
</ol>
<p>The packaged slicer executable will now have your loadable module as well. You just included it’s headers and compiled binaries into the packaged slicer. Hope this was useful to someone. Please correct me if anything is wrong.</p>

---
