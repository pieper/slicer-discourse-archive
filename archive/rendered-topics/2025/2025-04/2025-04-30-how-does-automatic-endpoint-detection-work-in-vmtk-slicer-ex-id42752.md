---
topic_id: 42752
title: "How Does Automatic Endpoint Detection Work In Vmtk Slicer Ex"
date: 2025-04-30
url: https://discourse.slicer.org/t/42752
---

# How does automatic endpoint detection work in VMTK Slicer Extension?

**Topic ID**: 42752
**Date**: 2025-04-30
**URL**: https://discourse.slicer.org/t/how-does-automatic-endpoint-detection-work-in-vmtk-slicer-extension/42752

---

## Post #1 by @bfosso (2025-04-30 22:22 UTC)

<p>Hi, the title pretty much says it all. I am wondering how endpoints are ‘auto-detected’ in the ExtractCenterline extension module to Slicer. It seems to work really well and I am curious how it is  done. I Googled for an explanation but I haven’t tried looking at the source code. I am hoping for something in plain english <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Thanks for your help!</p>

---

## Post #2 by @lassoan (2025-04-30 22:46 UTC)

<p>Look at the source code - it is all openly and freely available and that gives definitive answer to what’s happening when you click the auto-detect button. It is all <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/9b304f3040c45aebda56e50077a568d847e03857/ExtractCenterline/ExtractCenterline.py#L349-L358">here</a>. I don’t think there is much documentation (other than description of parameters) and I’m not sure if there are papers that describe the algorithm (it was added to VMTK in 2006, years after Luca Antiga’s PhD work was finished). If you find it hard to decypher the algorithm by reading the code then you can probably learn more about by searching on old VMTK forum posts.</p>

---

## Post #3 by @bfosso (2025-04-30 22:55 UTC)

<p>I will, thanks for your help.</p>

---
