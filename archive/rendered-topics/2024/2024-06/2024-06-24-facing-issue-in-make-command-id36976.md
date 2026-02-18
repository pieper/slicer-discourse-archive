# facing issue in make command

**Topic ID**: 36976
**Date**: 2024-06-24
**URL**: https://discourse.slicer.org/t/facing-issue-in-make-command/36976

---

## Post #1 by @maniron (2024-06-24 14:07 UTC)

<p>After giving make I am facing this issue</p>
<pre><code class="lang-auto">HTTP/2 stream 0 was not closed cleanly: INTERNAL_ERROR (err 2)

  stopped the pause stream!

  Connection #0 to host (nil) left intact
</code></pre>
<pre><code class="lang-auto">make[2]: *** [CMakeFiles/python-source.dir/build.make:98: python-source-prefix/src/python-source-stamp/python-source-download] Error 1
make[1]: *** [CMakeFiles/Makefile2:643: CMakeFiles/python-source.dir/all] Error 2
make: *** [Makefile:101: all] Error 2
</code></pre>
<p>Operating system: Ubuntu 22.04<br>
Slicer version: Latest version<br>
Expected behavior: make is not working</p>

---
