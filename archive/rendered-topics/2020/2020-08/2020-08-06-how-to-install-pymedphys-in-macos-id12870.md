---
topic_id: 12870
title: "How To Install Pymedphys In Macos"
date: 2020-08-06
url: https://discourse.slicer.org/t/12870
---

# How to: Install pymedphys in MacOS

**Topic ID**: 12870
**Date**: 2020-08-06
**URL**: https://discourse.slicer.org/t/how-to-install-pymedphys-in-macos/12870

---

## Post #1 by @Alex_Vergara (2020-08-06 10:02 UTC)

<p>The current code works in Linux and Windows:</p>
<p><code>from slicer.util import pip_install; pip_install('pymedphys')</code></p>
<p>However that is not the case for MacOS. In case you want to use this cool library that includes gamma comparison among other cool stuffs you need to make:</p>
<pre><code class="lang-auto">from slicer.util import pip_install
pip_install('dataclasses')
pip_install('pymedphys --no-deps')
</code></pre>
<p>And voila, it is working!</p>
<p>Example module for gamma comparison here <a href="https://github.com/BishopWolf/GammaIndex" rel="nofollow noopener">https://github.com/BishopWolf/GammaIndex</a><br>
Feel free to propose changes</p>
<p>Cheers</p>

---

## Post #2 by @Alex_Vergara (2020-09-09 09:49 UTC)

<p>From today 09/09/2020: pymedphys has changed its default behaviour and now there is no longer need for this trick. This line will work also in mac</p>
<p><code>from slicer.util import pip_install; pip_install('pymedphys')</code></p>

---
