---
topic_id: 45770
title: "Objects In Memory Exchange Between Modules"
date: 2026-01-13
url: https://discourse.slicer.org/t/45770
---

# Objects in-memory exchange between modules

**Topic ID**: 45770
**Date**: 2026-01-13
**URL**: https://discourse.slicer.org/t/objects-in-memory-exchange-between-modules/45770

---

## Post #1 by @Yaroslav_Plutenko (2026-01-13 16:02 UTC)

<p>Greeting!</p>
<p>I’m developing a few scripted modules for plant MRI data processing and lifecycle management, two of which act as clients for a remote FastAPI server. The modules have different purposes; therefore, they are kept separate, but the authorization is the same in each module, and I have to authorize twice every time when a user opens two modules.<br>
My question is: how to pass information in-memory between modules - is there some Slicer object/singleton with global accessibility?  I guess the scope of view of the parameter node is within the module only; I need a “global parameter node”.<br>
I also want to avoid exchanging information in temporary files and look for an  in-memory object. At first, I’d like to store authorization tokens there, but not limited to, in the future. Can you suggest if there is such a place in Slicer?</p>

---

## Post #2 by @cpinter (2026-01-13 16:10 UTC)

<p>I don’t quite understand. Are you using more Slicer instances? If not, then the “global parameter node” is the MRML scene, where you can keep anything, like a text node or a scripted module node for storing scene-wide information.</p>

---

## Post #3 by @Yaroslav_Plutenko (2026-01-13 18:59 UTC)

<p>I was blind, indeed.  I focused on a parameter node and its limitations. Yes, I mean modules within a single Slicer instance, and they really have access to the scene. So I can create a dummy folder, even an invisible one, and attach some properties to exchange tokens and other info. And the text node or a table - I just realized today they also exist in Slicer, offering a more elegant way for my purpose. Thank you!</p>

---
