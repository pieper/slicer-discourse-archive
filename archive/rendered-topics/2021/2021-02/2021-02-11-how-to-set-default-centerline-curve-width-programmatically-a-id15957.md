---
topic_id: 15957
title: "How To Set Default Centerline Curve Width Programmatically A"
date: 2021-02-11
url: https://discourse.slicer.org/t/15957
---

# How to set default centerline curve width programmatically and how to have slice intersection displayed?

**Topic ID**: 15957
**Date**: 2021-02-11
**URL**: https://discourse.slicer.org/t/how-to-set-default-centerline-curve-width-programmatically-and-how-to-have-slice-intersection-displayed/15957

---

## Post #1 by @akshay_pillai (2021-02-11 20:29 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20200930</p>
<p>This is a 2 part question. First, I want to know how to programmatically set the default centerline curve width for the centerline curve obtained from the extract centerline module. I want to set the width to a higher number than what it generates now.  Second, Is there a way to display the slice intersections even when the view(layout) only has the yellow slice only? Currently, the slice intersections don’t show up when I select the yellow slice only layout. I want the slice intersection in sagittal view(when set to four-up layout) to appear when I set the layout to yellow only, is that possible? Any help is appreciated thanks.</p>

---

## Post #2 by @lassoan (2021-02-11 20:50 UTC)

<aside class="quote no-group" data-username="akshay_pillai" data-post="1" data-topic="15957">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akshay_pillai/48/8301_2.png" class="avatar"> akshay_pillai:</div>
<blockquote>
<p>First, I want to know how to programmatically set the default centerline curve width for the centerline curve obtained from the extract centerline module. I want to set the width to a higher number than what it generates now.</p>
</blockquote>
</aside>
<p>What do you mean by width? Diameter of the curve?<br>
As far as I remember, the module just uses default glyph scale and line thickness. To change the defaults, go to Markups module / Display section, change the values for any of the curves, and click Save to Defaults. Right now, glyph scale is saved to defaults but line thickness is not. We could consider adding line thickness to the defaults as well, but until then you can just control the thickness using glyph scale (line thickness is by default relative to the chosen glyph size), or copy-paste this into the Python console (to make thickness to 80% of glyph size by default):</p>
<pre><code>slicer.mrmlScene.GetDefaultNodeByClass('vtkMRMLMarkupsDisplayNode').SetLineThickness(0.8)
</code></pre>
<aside class="quote no-group" data-username="akshay_pillai" data-post="1" data-topic="15957">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akshay_pillai/48/8301_2.png" class="avatar"> akshay_pillai:</div>
<blockquote>
<p>Currently, the slice intersections don’t show up when I select the yellow slice only layout. I want the slice intersection in sagittal view(when set to four-up layout) to appear when I set the layout to yellow only, is that possible?</p>
</blockquote>
</aside>
<p>Intersection with non-existing views cannot be displayed. However, there are view layouts that contain multiple views yet they show maximized view of a selected one, for example “Tabbed slice”. You can also define any custom layout (with tabs, splitters, any number of slice, 3D, plot, and table views) by an <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout">XML string</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb9765f40900d83846210236865b1c198a89985e.png" data-download-href="/uploads/short-url/qLvEGAaJHgoBrhj8PV7awCScrjo.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb9765f40900d83846210236865b1c198a89985e_2_401x500.png" alt="image" data-base62-sha1="qLvEGAaJHgoBrhj8PV7awCScrjo" width="401" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb9765f40900d83846210236865b1c198a89985e_2_401x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb9765f40900d83846210236865b1c198a89985e_2_601x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb9765f40900d83846210236865b1c198a89985e_2_802x1000.png 2x" data-dominant-color="32271B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">937×1166 41.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @akshay_pillai (2021-02-11 21:20 UTC)

<p>Yes that’s what I was looking for, I meant glyph size only. Thanks. I’ll post here if I have further questions. Thanks again.</p>

---
