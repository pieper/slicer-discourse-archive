# How to export compile commands?

**Topic ID**: 31410
**Date**: 2023-08-28
**URL**: https://discourse.slicer.org/t/how-to-export-compile-commands/31410

---

## Post #1 by @somso2e (2023-08-28 20:39 UTC)

<p>Hi clangd depends on the compile_commands.json file to work but I can’t  generate it by setting the  <code>CMAKE_EXPORT_COMPILE_COMMANDS</code> flag like below.</p>
<pre><code class="lang-auto">cmake -DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=ON Slicer-SuperBuild-Debug/
</code></pre>

---

## Post #2 by @somso2e (2023-10-13 09:24 UTC)

<p>I just needed to run make as well and the file was generated.</p>

---
