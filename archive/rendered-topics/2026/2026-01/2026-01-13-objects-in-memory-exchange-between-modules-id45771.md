# Objects in-memory exchange between modules

**Topic ID**: 45771
**Date**: 2026-01-13
**URL**: https://discourse.slicer.org/t/objects-in-memory-exchange-between-modules/45771

---

## Post #1 by @Yaroslav_Plutenko (2026-01-13 16:02 UTC)

<p>Greeting!</p>
<p>I’m developing a few scripted modules for plant MRI data processing and lifecycle management, two of which act as clients for a remote FastAPI server. The modules have different purposes; therefore, they are kept separate, but the authorization is the same in each module, and I have to authorize twice every time when a user opens two modules.<br>
My question is: how to pass information in-memory between modules - is there some Slicer object/singleton with global accessibility?  I guess the scope of view of the parameter node is within the module only; I need a “global parameter node”.<br>
I also want to avoid exchanging information in temporary files and look for an  in-memory object. At first, I’d like to store authorization tokens there, but not limited to, in the future. Can you suggest if there is such a place in Slicer?</p>

---
