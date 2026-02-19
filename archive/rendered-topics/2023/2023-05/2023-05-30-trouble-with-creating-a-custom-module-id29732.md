---
topic_id: 29732
title: "Trouble With Creating A Custom Module"
date: 2023-05-30
url: https://discourse.slicer.org/t/29732
---

# Trouble with creating a custom module

**Topic ID**: 29732
**Date**: 2023-05-30
**URL**: https://discourse.slicer.org/t/trouble-with-creating-a-custom-module/29732

---

## Post #1 by @Patrick_Li (2023-05-30 17:59 UTC)

<p>I am currently trying to create my own module with ExtensionWizard. I used QTDesigner to create the UI, which is now mostly done. What I’m trying to do now is to get the module to save data to specific folders based on user input. In this case, I want the module to be able to create new folders and then save markup data, tables, and texts within these new folders.</p>
<p>Here is an example of the kind of data hierarchy I’m aiming to create.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b27016a2c83e9f5f15d1a2ebd117b51d97cf2d5.jpeg" data-download-href="/uploads/short-url/d0n1a8n77AHupPypy3nm9N2Tto9.jpeg?dl=1" title="Screenshot (843)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b27016a2c83e9f5f15d1a2ebd117b51d97cf2d5_2_690x388.jpeg" alt="Screenshot (843)" data-base62-sha1="d0n1a8n77AHupPypy3nm9N2Tto9" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b27016a2c83e9f5f15d1a2ebd117b51d97cf2d5_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b27016a2c83e9f5f15d1a2ebd117b51d97cf2d5_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b27016a2c83e9f5f15d1a2ebd117b51d97cf2d5_2_1380x776.jpeg 2x" data-dominant-color="A6A9BD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (843)</span><span class="informations">1920×1080 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here’s what my module looks like.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/549cdb37003b3c5f06120734aed13f7c7c1ad561.jpeg" data-download-href="/uploads/short-url/c4wazOAFBy4zwpfHx4MbuvaorF7.jpeg?dl=1" title="Screenshot (845)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/549cdb37003b3c5f06120734aed13f7c7c1ad561_2_690x388.jpeg" alt="Screenshot (845)" data-base62-sha1="c4wazOAFBy4zwpfHx4MbuvaorF7" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/549cdb37003b3c5f06120734aed13f7c7c1ad561_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/549cdb37003b3c5f06120734aed13f7c7c1ad561_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/549cdb37003b3c5f06120734aed13f7c7c1ad561_2_1380x776.jpeg 2x" data-dominant-color="A4A8BC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (845)</span><span class="informations">1920×1080 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-05-30 20:05 UTC)

<p>You can create folders using standard Python functions and then export nodes into them using <code>slicer.util.saveNode</code> or <code>slicer.util.exportNode</code> functions.</p>

---

## Post #3 by @Patrick_Li (2023-05-31 18:36 UTC)

<p>I used QT Designer to design the UI, and didn’t use any Python. I’m not sure how to make it so that pressing a certain button (“Save”) in the UI will create a folder and export the nodes.</p>

---

## Post #4 by @lassoan (2023-07-25 12:34 UTC)

<p>Your can <code>connect</code> a button event (e.g., <code>click</code>) to a Python method as it is shown in the scripted module template.</p>

---
