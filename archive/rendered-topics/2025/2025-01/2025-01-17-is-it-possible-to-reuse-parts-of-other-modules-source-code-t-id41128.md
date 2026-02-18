# Is it possible to reuse parts of other modules' source code to create a custom module?

**Topic ID**: 41128
**Date**: 2025-01-17
**URL**: https://discourse.slicer.org/t/is-it-possible-to-reuse-parts-of-other-modules-source-code-to-create-a-custom-module/41128

---

## Post #1 by @igi133 (2025-01-17 13:47 UTC)

<p>Hello everyone,</p>
<p>I’ve been working with Slicer and I’m interested in creating my own custom module. I wanted to ask the community whether it’s possible to reuse parts of source code from other existing modules to help build my own module.</p>
<p>Specifically, I’m wondering about the best practices for integrating or adapting existing code in a way that follows the Slicer framework’s guidelines and avoids any potential issues.</p>
<p>Has anyone had experience with this? Are there any limitations or things to consider when reusing code from other modules?</p>
<p>Any tips or advice would be greatly appreciated!</p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2025-01-17 14:18 UTC)

<p>Yes, reusing functionality from modules to build new modules is a core part of Slicer.  Typically you can just use the <code>Logic</code> classes directly and sometimes you may want to use widgets.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/index.html">https://slicer.readthedocs.io/en/latest/developer_guide/modules/index.html</a></p>

---
