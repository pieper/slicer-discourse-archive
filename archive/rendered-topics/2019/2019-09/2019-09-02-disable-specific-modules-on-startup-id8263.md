---
topic_id: 8263
title: "Disable Specific Modules On Startup"
date: 2019-09-02
url: https://discourse.slicer.org/t/8263
---

# Disable specific modules on startup

**Topic ID**: 8263
**Date**: 2019-09-02
**URL**: https://discourse.slicer.org/t/disable-specific-modules-on-startup/8263

---

## Post #1 by @dtan (2019-09-02 16:43 UTC)

<p>I’m trying to disable modules on startup using <code>./Slicer -modules-to-ignore "Welcome, data"</code>, but I notice that only the welcome module is disabled while data module is still present. Am I using this command incorrectly?</p>
<p>Also, is there a way to change the default module through cli?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2019-09-02 18:34 UTC)

<p>Hi -</p>
<p>There can’t be a space, and also it’s case-sensitive, so you need:</p>
<pre><code class="lang-auto">./Slicer -modules-to-ignore Welcome,Data
</code></pre>

---
