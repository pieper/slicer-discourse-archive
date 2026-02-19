---
topic_id: 30126
title: "We Assembled A Widget From 3D Slicer In The Browser"
date: 2023-06-19
url: https://discourse.slicer.org/t/30126
---

# We assembled a widget from 3D Slicer in the browser

**Topic ID**: 30126
**Date**: 2023-06-19
**URL**: https://discourse.slicer.org/t/we-assembled-a-widget-from-3d-slicer-in-the-browser/30126

---

## Post #1 by @mazurkin.daniel (2023-06-19 18:27 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/547edaa30c22f0689056b32bc595f0e743c12a28.jpeg" data-download-href="/uploads/short-url/c3tTfghhbtKEaZGKBYzgAVoMEje.jpeg?dl=1" title="demo_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/547edaa30c22f0689056b32bc595f0e743c12a28_2_690x382.jpeg" alt="demo_1" data-base62-sha1="c3tTfghhbtKEaZGKBYzgAVoMEje" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/547edaa30c22f0689056b32bc595f0e743c12a28_2_690x382.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/547edaa30c22f0689056b32bc595f0e743c12a28_2_1035x573.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/547edaa30c22f0689056b32bc595f0e743c12a28.jpeg 2x" data-dominant-color="87879A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">demo_1</span><span class="informations">1280×710 71.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09e728bd38e21a115ee8bd7ae7910e10eb5965a0.jpeg" data-download-href="/uploads/short-url/1pByjh6bdXxtqXXm4ZOSKBajRAI.jpeg?dl=1" title="demo_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09e728bd38e21a115ee8bd7ae7910e10eb5965a0_2_690x388.jpeg" alt="demo_2" data-base62-sha1="1pByjh6bdXxtqXXm4ZOSKBajRAI" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09e728bd38e21a115ee8bd7ae7910e10eb5965a0_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09e728bd38e21a115ee8bd7ae7910e10eb5965a0_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09e728bd38e21a115ee8bd7ae7910e10eb5965a0.jpeg 2x" data-dominant-color="0A0B0D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">demo_2</span><span class="informations">1280×720 31.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @mazurkin.daniel (2023-06-21 02:57 UTC)

<p>Link to instruction and source code <a href="https://docs.google.com/document/d/1dXtK01DpxkANEJEbvwo1Dnph-B_XpNmor3kCTDFklp0/edit?usp=sharing" rel="noopener nofollow ugc">Instruction by 3dSlicer - Google Docs</a></p>

---

## Post #3 by @lassoan (2023-06-21 18:42 UTC)

<p>Thanks for the information and instructions, this is very interesting because we often get questions about what options exists for running Slicer in the web browser. Running Slicer locally in a web browser (without a server backend) seemed very far fetched, but your experiments bring it closer to reality.</p>
<p>Which Slicer classes did you use? Did you have to modify them (e.g., remove dependency to MRML nodes)?</p>

---

## Post #4 by @mazurkin.daniel (2023-06-22 01:00 UTC)

<p>We implemented widget rendering using MRML and compiled the MRML source code as a static library for our WASM project. However, the main drawback is that this tool works quite slowly in WASM, and we have no idea why. We would appreciate any guidance on how to investigate this issue. More details can be found at <a href="https://discourse.slicer.org/t/slowly-rendering-widget-from-3d-slicer-in-wasm/30169" class="inline-onebox">Slowly rendering widget from 3D Slicer in wasm</a>. The 3D Slicer code was slightly modified in the MRML area (some methods were made public). If interested, I can provide more details about these changes</p>

---
