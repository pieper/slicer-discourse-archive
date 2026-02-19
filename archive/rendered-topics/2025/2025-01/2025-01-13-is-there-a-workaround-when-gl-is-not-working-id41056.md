---
topic_id: 41056
title: "Is There A Workaround When Gl Is Not Working"
date: 2025-01-13
url: https://discourse.slicer.org/t/41056
---

# Is there a workaround when GL is not working?

**Topic ID**: 41056
**Date**: 2025-01-13
**URL**: https://discourse.slicer.org/t/is-there-a-workaround-when-gl-is-not-working/41056

---

## Post #1 by @ferhue (2025-01-13 11:48 UTC)

<p>In my Ubuntu 22.04 computer, I have an old computing GPU and a display GPU, both of them NVIDIA. <a href="https://askubuntu.com/questions/1442001/cuda-8-and-gcc-5-on-ubuntu-22-04-for-tesla-c2070" rel="noopener nofollow ugc">Long story</a> short: I had to set the driver display to “nouveau” instead of “NVIDIA”, and as a consequence, glxgears / glxinfo does not work. Other than that, everything else in my Xwayland Ubuntu desktop works, web browsers too, Office, etc.<br>
Now I downloaded 3DSlicer, and when opening it, splashscreen shows fine, but later, it just produces an empty screen. I can click on the dialogs to open/close File, but everything inside is transparent, I see my desktop instead.<br>
The terminal keeps showing this error infinitely:</p>
<pre><code class="lang-auto">QXcbIntegration: Cannot create platform OpenGL context, neither GLX nor EGL are enabled
composeAndFlush: makeCurrent() failed
</code></pre>
<p>Is there a way to define an environment variable to make 3D Slicer work in this type of situation, bypassing the need for GL?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @pieper (2025-01-13 15:55 UTC)

<p>Yes, there are fallback options but there’s no easy recipe for configuring linux drivers (lots of forums with questions and answers that sometimes work and sometimes don’t).  Probably the easiest in my experience would be to use software rendering in Docker (the <a href="https://github.com/pieper/SlicerDockers">SlicerDockers</a> should still work fine.  They haven’t been updated to the latest Slicer, but it’s easy to install once you have the environment running).</p>

---

## Post #3 by @muratmaga (2025-01-13 22:04 UTC)

<p>Sometimes <code>export "LIBGL_ALWAYS_INDIRECT=1"</code> helps.</p>
<p>But as <a class="mention" href="/u/pieper">@pieper</a> said there are some many variables it is hard to find a consistent recipe.</p>

---
