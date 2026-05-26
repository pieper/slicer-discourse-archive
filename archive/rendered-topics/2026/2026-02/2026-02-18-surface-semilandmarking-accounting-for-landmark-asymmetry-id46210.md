---
topic_id: 46210
title: "Surface semilandmarking: accounting for landmark asymmetry?"
date: 2026-02-18
url: https://discourse.slicer.org/t/46210
last_bumped: 2026-02-19T04:55:09.451Z
---

# Surface semilandmarking: accounting for landmark asymmetry?

**Topic ID**: 46210
**Date**: 2026-02-18
**URL**: https://discourse.slicer.org/t/surface-semilandmarking-accounting-for-landmark-asymmetry/46210

---

## Post #1 by @raranda22 (2026-02-18 10:17 UTC)

<p>Hello,</p>
<p>I’ve been using various surface semilandmarking techniques (DeCAL, auto3dgm, Builder (part of ATLAS), PseudoLMGenerator) to landmark bird beak meshes from MarkMyBird. The only landmarking module I’m aware of that allows incorporation of symmetric landmarks across a 2D plane, for instance left/right sides, is PseudoLMGenerator. So I was wondering two things:</p>
<p>1.) Are there any other modules that allow for symmetric landmarks across planes?</p>
<p>2.) Is there a way to enforce symmetry of landmarks after the surface semilandmarking procedure has been applied to all specimens?</p>
<p>Thank you,</p>
<p>Ricardo Ely</p>

---

## Post #2 by @muratmaga (2026-02-18 16:44 UTC)

<p>No, not that I know of. To enforce symmetry, you can first create a mirroring plane, and then reflect one side of the semiLMs to the other side. That’s what pseudoLMGenerator does. You can look at its code to understand it, but you have to implement this yourself.</p>

---

## Post #3 by @drnoorfatima (2026-02-19 02:38 UTC)

<p>Hi Ricardo,</p>
<p>For symmetric landmarking beyond PseudoLMGenerator, you might want to look at:</p>
<ol>
<li>SlicerMorph’s GPA module has some symmetry enforcement options</li>
<li>ALPACA (if you’re working with template-based approaches)</li>
</ol>
<p>For post-hoc symmetry enforcement after semilandmarking, you could apply a reflection transformation and average the landmarks with their mirrored counterparts, but that would need custom scripting.</p>
<p>The morphometrics community on the SlicerMorph forums might have more specific recommendations for your use case.</p>
<p>Good luck with the project!</p>

---

## Post #4 by @muratmaga (2026-02-19 04:55 UTC)

<aside class="quote no-group" data-username="drnoorfatima" data-post="3" data-topic="46210">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/drnoorfatima/48/81980_2.png" class="avatar"> drnoorfatima:</div>
<blockquote>
<ol>
<li>SlicerMorph’s GPA module has some symmetry enforcement options</li>
<li>ALPACA (if you’re working with template-based approaches)</li>
</ol>
</blockquote>
</aside>
<ol>
<li>Actually, GPA module has no symmetry enforcement option. We do talked about it, but currently there is no immediate plan to implement it, as in doing that in geomorph and visualizing in Slicer offers a remedy.</li>
<li>While you can create a symmetrical template with PseudoLMGenerator, and definitely transfer that template to the samples with ALPACA, ALPACA itself does not have any constraints enforcing symmetry axis.</li>
</ol>
<p>I do want to make those clear. As suggested those need to be done post-hoc with scripting.</p>

---
