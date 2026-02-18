# Creating a hemisphere mask

**Topic ID**: 32427
**Date**: 2023-10-26
**URL**: https://discourse.slicer.org/t/creating-a-hemisphere-mask/32427

---

## Post #1 by @e0032127 (2023-10-26 17:16 UTC)

<p>Hello everyone!</p>
<p>I’m currently studying the effects of chemoradiotherapy on healthy brain tissues in a population of brain tumours, and I am trying to segment out the healthy tissues. However, I notice that some tumour segments end up in my healthy tissues. I looked up papers online and most have created a mask to produce a single healthy hemisphere.</p>
<p>Would you have any advice on how I could proceed to do this? For eg does it make sense to segment the GM, WM out followed by creating a hemisphere mask and cut my GM/WM into half? But would the tumour affect registration to the MNI152 space?</p>
<p>Or would it be better to create the mask first, so that when registration is done in the MNI152 space, only the healthy tissue is registered within that space?</p>
<p>Appreciate some advice here! Thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Regards,<br>
Jin</p>

---
