---
topic_id: 42858
title: "Multivolume Rendering"
date: 2025-05-10
url: https://discourse.slicer.org/t/42858
---

# Multivolume rendering

**Topic ID**: 42858
**Date**: 2025-05-10
**URL**: https://discourse.slicer.org/t/multivolume-rendering/42858

---

## Post #1 by @muratmaga (2025-05-10 01:45 UTC)

<p>I am testing multiple volume rendering for a visualization. When I turn on the 3rd volume, it doesn’t displayed, and I receive this message</p>
<pre><code class="lang-auto">Links failed: ERROR: Implementation limit of 16 active fragment shader samplers (e.g., maximum number of supported image units) exceeded, fragment shader uses 18 samplers
Shader failed to compile
</code></pre>
<p>These are very small volumes 178x314x221. Is there any way to mitigate this?</p>

---

## Post #2 by @pieper (2025-05-10 03:24 UTC)

<p>I don’t know for sure, but that sounds like a hardware limit that would be hard to workaround without rewriting the renderer.</p>

---

## Post #3 by @cpinter (2025-05-12 09:49 UTC)

<p>I just managed to show three sample datasets with Multi-volume rendering:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fca39732a8cb85b6463890610d89a4db814e424.jpeg" data-download-href="/uploads/short-url/6OLHHHV5rro6pUQQ8wjVumRPuMk.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fca39732a8cb85b6463890610d89a4db814e424_2_690x403.jpeg" alt="image" data-base62-sha1="6OLHHHV5rro6pUQQ8wjVumRPuMk" width="690" height="403" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fca39732a8cb85b6463890610d89a4db814e424_2_690x403.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fca39732a8cb85b6463890610d89a4db814e424_2_1035x604.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fca39732a8cb85b6463890610d89a4db814e424_2_1380x806.jpeg 2x" data-dominant-color="7C7B7F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1123 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This computer has a 4090, But based on the message you posted this does not seem to be a hardware problem.</p>
<p>What Slicer version do you use?</p>
<p>Update: I just saw that the “regular” GPU Ray Casting now seems to support multiple volumes (the volumes are not just rendered on top of each other). I am surprised, because I try to follow updates about this, and we even talked about this at the PW in January and I wasn’t aware.</p>

---

## Post #4 by @muratmaga (2025-05-12 15:22 UTC)

<p>This was on a M3 pro with a recent (within a few days of latest) preview version. I will give it a try with a windows box later.</p>

---
