---
topic_id: 46210
title: "Surface Semilandmarking Accounting For Landmark Asymmetry"
date: 2026-02-18
url: https://discourse.slicer.org/t/46210
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
