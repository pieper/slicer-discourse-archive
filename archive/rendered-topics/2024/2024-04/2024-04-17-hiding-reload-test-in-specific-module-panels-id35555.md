# Hiding "Reload & Test" in Specific Module Panels

**Topic ID**: 35555
**Date**: 2024-04-17
**URL**: https://discourse.slicer.org/t/hiding-reload-test-in-specific-module-panels/35555

---

## Post #1 by @park (2024-04-17 10:03 UTC)

<p>Hi all,</p>
<p>I usually work with several module panels open at the same time.<br>
Is it possible to hide the “Reload &amp; Test” option in specific module panels?</p>
<p>Best,</p>

---

## Post #2 by @Sunderlandkyl (2024-04-17 15:07 UTC)

<p>You can hide the reload &amp; test section for specific modules in python like this:</p>
<pre><code class="lang-auto">slicer.modules.segmenteditor.widgetRepresentation().self().reloadCollapsibleButton.visible = False
</code></pre>

---

## Post #3 by @lassoan (2024-04-18 00:16 UTC)

<aside class="quote no-group" data-username="park" data-post="1" data-topic="35555">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/park/48/5717_2.png" class="avatar"> park:</div>
<blockquote>
<p>I usually work with several module panels open at the same time.</p>
</blockquote>
</aside>
<p>Do you mean you add an <em>entire module widget</em> into your own module widget? This is not supported and can lead to many issues (for example, only one module widget can be in “entered” state). Instead, you can add any reusable widgets to your module that other modules provide.</p>

---

## Post #4 by @park (2024-04-22 08:39 UTC)

<p>I want to display multiple widgets simultaneously as shown in the picture. Would this pose any long-term issues? If there are any issues, could I gain insights into implementing a layout like the one shown below? Even a little advice would be greatly helpful.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc61e3d47b838f9a055f0c4eac5469703f1fdc4e.png" data-download-href="/uploads/short-url/ta38clRudPU7zWQ1kUjS0VNiDlY.png?dl=1" title="example" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc61e3d47b838f9a055f0c4eac5469703f1fdc4e_2_690x273.png" alt="example" data-base62-sha1="ta38clRudPU7zWQ1kUjS0VNiDlY" width="690" height="273" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc61e3d47b838f9a055f0c4eac5469703f1fdc4e_2_690x273.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc61e3d47b838f9a055f0c4eac5469703f1fdc4e_2_1035x409.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc61e3d47b838f9a055f0c4eac5469703f1fdc4e.png 2x" data-dominant-color="D5D7D4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">example</span><span class="informations">1164×461 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @cpinter (2024-04-22 14:31 UTC)

<p>When I had to do something similar, I created custom layouts, in which some views showed the image (2D, 3D, anything that is supported currently), and other views contained a widget that I could set from my custom app code. These widgets were not entire Slicer module widgets (for the reason <a class="mention" href="/u/lassoan">@lassoan</a> mentioned), but widgets that I created myself. In this way you cannot get floating widgets, but at least a more flexible control over the layout. See an example of such a layout here: <a href="https://youtu.be/zs-0mZQLB48?t=137">https://youtu.be/zs-0mZQLB48?t=137</a></p>

---

## Post #6 by @koeglfryderyk (2024-12-05 14:16 UTC)

<p>Did you write the Dent.AI app shown in the video as a Python Scripted Module? Or do you have to do it in C++ to get this level of control over all the visual aspects?</p>

---
