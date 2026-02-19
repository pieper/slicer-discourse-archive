---
topic_id: 18377
title: "Left And Right Panel Ratio"
date: 2021-06-28
url: https://discourse.slicer.org/t/18377
---

# Left and Right Panel Ratio

**Topic ID**: 18377
**Date**: 2021-06-28
**URL**: https://discourse.slicer.org/t/left-and-right-panel-ratio/18377

---

## Post #1 by @OpenSource_Contri (2021-06-28 17:33 UTC)

<p>I want to know how the ratio of left panel and right panel work in slicer, which can be adjust by us. Which Slicer code-base file I have to explore to learn “how this actually work with the help of particular program”?</p>
<p>Three screenshot is attached.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64f052e23f9431e3e0f2e2d0710998cfe81352ae.png" data-download-href="/uploads/short-url/eoWDzLpq8tlT4o20Bp33xAoxMtM.png?dl=1" title="Screenshot (275)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64f052e23f9431e3e0f2e2d0710998cfe81352ae_2_690x388.png" alt="Screenshot (275)" data-base62-sha1="eoWDzLpq8tlT4o20Bp33xAoxMtM" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64f052e23f9431e3e0f2e2d0710998cfe81352ae_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64f052e23f9431e3e0f2e2d0710998cfe81352ae_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64f052e23f9431e3e0f2e2d0710998cfe81352ae_2_1380x776.png 2x" data-dominant-color="2E2E36"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (275)</span><span class="informations">1920×1080 77.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48a0478610a54300d488047f58ebb77ed01e6150.png" data-download-href="/uploads/short-url/amtM2DHEnpgJfAA5HFP8DDFHwju.png?dl=1" title="Screenshot (276)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48a0478610a54300d488047f58ebb77ed01e6150_2_690x388.png" alt="Screenshot (276)" data-base62-sha1="amtM2DHEnpgJfAA5HFP8DDFHwju" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48a0478610a54300d488047f58ebb77ed01e6150_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48a0478610a54300d488047f58ebb77ed01e6150_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48a0478610a54300d488047f58ebb77ed01e6150_2_1380x776.png 2x" data-dominant-color="2D2D33"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (276)</span><span class="informations">1920×1080 77.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28d83866b11500846a29f7a14c3bbe6ef356a221.png" data-download-href="/uploads/short-url/5PklCrub3dSLW2kvXKJhOniRDwJ.png?dl=1" title="Screenshot (277)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28d83866b11500846a29f7a14c3bbe6ef356a221_2_690x388.png" alt="Screenshot (277)" data-base62-sha1="5PklCrub3dSLW2kvXKJhOniRDwJ" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28d83866b11500846a29f7a14c3bbe6ef356a221_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28d83866b11500846a29f7a14c3bbe6ef356a221_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28d83866b11500846a29f7a14c3bbe6ef356a221_2_1380x776.png 2x" data-dominant-color="2D2D30"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (277)</span><span class="informations">1920×1080 73.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-06-28 22:39 UTC)

<p>It is all standard Qt behavior. Slicer does not impose any extra constraints, but Qt computes the allowed sizes for each section of the GUI (based on sizing policies set in each widget).</p>

---

## Post #3 by @OpenSource_Contri (2021-06-29 10:23 UTC)

<p>Sure, I will explore Qt.<br>
But I want to know which UI file I’ve to work on to learn this behavior for sliding left and right panel.</p>

---

## Post #4 by @ungi (2021-06-29 14:11 UTC)

<p>Often, hiding the Data Probe (lower left widget in Slicer main window) solves the problem of randomly resizing module panels, which is an extremely annoying feature of Slicer UI.</p>
<p>If the problem still persists, you could insert this code on the python interactor to force a fixed with on the module panel and its contents. Or add this code to your module setup function so it is automatically applied every time you open your module (if you are working on a custom module):</p>
<blockquote>
<p>modulePanelDockWidget = slicer.util.mainWindow().findChildren(‘QDockWidget’,‘PanelDockWidget’)[0]<br>
modulePanelDockWidget.setSizePolicy(qt.QSizePolicy.Fixed, qt.QSizePolicy.Expanding)<br>
modulePanelDockWidget.setFixedWidth(600)<br>
modulePanelScrollArea = modulePanelDockWidget.findChild(“QWidget”, “dockWidgetContents”)<br>
modulePanelScrollArea.setSizePolicy(qt.QSizePolicy.Fixed, qt.QSizePolicy.Expanding)<br>
modulePanelScrollArea.setFixedWidth(600)</p>
</blockquote>

---

## Post #7 by @OpenSource_Contri (2021-06-30 09:50 UTC)

<p>Thanks, I have done that before.<br>
But I want to know how this left and right panel in screenshot above works. Which GUI file I have to explore?<br>
For example: If I say, I want to fix that left and right panel in the ratio of 25:75 then how to do it.</p>

---

## Post #8 by @lassoan (2021-07-02 18:28 UTC)

<p>Since Qt dynamically changes the layout based on sizing policies of every visible widget. If you want to know what sizes the left panel may end up in various scenarios, you would need to review size policies of all the widgets of all the modules that you may use. This is of course practically infeasible.</p>
<p>Therefore, if you need to force a certain width for the left panel then probably your only option is to force a specific size as <a class="mention" href="/u/ungi">@ungi</a> described above. You can query the screen size to compute how many voxels 25% of the screen width corresponds to.</p>

---
