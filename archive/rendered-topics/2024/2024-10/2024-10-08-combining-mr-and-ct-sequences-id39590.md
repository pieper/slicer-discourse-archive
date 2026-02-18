# Combining MR and CT sequences

**Topic ID**: 39590
**Date**: 2024-10-08
**URL**: https://discourse.slicer.org/t/combining-mr-and-ct-sequences/39590

---

## Post #1 by @MaxVs (2024-10-08 20:27 UTC)

<p>Hi everyone.<br>
I’m struggling with a one problem.<br>
I have patient CT and MRI. I would like to render different structures on CT and different on MRI, then I would like to combine both models and here my problem appears.<br>
Both models appear in different places of space and I can not reorientate image volume (would be great if its possible to combine it permanently) or if the previous option is not possible, to reorientate and merge both models based on CT-scan and MRI.<br>
Does anyone have an idea how to deal with it?</p>
<p>Thank you in advance!</p>

---

## Post #2 by @pieper (2024-10-08 20:33 UTC)

<p>Sounds like you need to perform registration: <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html" class="inline-onebox">Registration — 3D Slicer documentation</a></p>

---

## Post #3 by @MaxVs (2024-11-12 17:52 UTC)

<p>Thank you so much! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
