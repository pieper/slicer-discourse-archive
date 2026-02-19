---
topic_id: 43398
title: "Setcolor In Scripting Lost All Light Reflection Effect"
date: 2025-06-17
url: https://discourse.slicer.org/t/43398
---

# SetColor() in scripting lost all light reflection effect

**Topic ID**: 43398
**Date**: 2025-06-17
**URL**: https://discourse.slicer.org/t/setcolor-in-scripting-lost-all-light-reflection-effect/43398

---

## Post #1 by @chz31 (2025-06-17 19:32 UTC)

<p>Whenever I set up color using <code>modelNode.GetDisplayNode().SetColor()</code> in Slicer Pytho console or a python script, the model appeared to lose all the light reflection and material effects.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c1368b761e25c7b9140bb789fcbfb8b144e2ccd.png" data-download-href="/uploads/short-url/hHCMYSbBUcVf3tN9HgtgwpuYfnv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c1368b761e25c7b9140bb789fcbfb8b144e2ccd_2_315x250.png" alt="image" data-base62-sha1="hHCMYSbBUcVf3tN9HgtgwpuYfnv" width="315" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c1368b761e25c7b9140bb789fcbfb8b144e2ccd_2_315x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c1368b761e25c7b9140bb789fcbfb8b144e2ccd_2_472x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c1368b761e25c7b9140bb789fcbfb8b144e2ccd_2_630x500.png 2x" data-dominant-color="3C3EEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1021×808 70.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I just click the color table, and “OK” to select the same select, the color then became normal.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2c60f95edc3ca35a0657e6fb6aa043bffbb77c0.png" data-download-href="/uploads/short-url/pvvkEU0aBGI9qEdN5lSoafJ6Rry.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2c60f95edc3ca35a0657e6fb6aa043bffbb77c0.png" alt="image" data-base62-sha1="pvvkEU0aBGI9qEdN5lSoafJ6Rry" width="328" height="219"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">657×438 27.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Did I miss anything in setting the color? Thanks!</p>

---

## Post #2 by @pieper (2025-06-17 20:53 UTC)

<p>You should use the more specific rendering-related fields like diffuse color, specular color etc.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://apidocs.slicer.org/main/classvtkMRMLDisplayNode.html">
  <header class="source">

      <a href="https://apidocs.slicer.org/main/classvtkMRMLDisplayNode.html" target="_blank" rel="noopener">apidocs.slicer.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://apidocs.slicer.org/main/classvtkMRMLDisplayNode.html" target="_blank" rel="noopener">Slicer: vtkMRMLDisplayNode Class Reference</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @chz31 (2025-06-18 14:47 UTC)

<p>I went through all the settings, including <code>SetShading(), SetDiffuse, SetSpecular, SetAmbient, and SetLighting</code>, but none of it worked.</p>
<p>Interestingly, when I used <code>SetColor</code> directly in a function in the logic() class, the shading and lighting effects displayed normally.</p>

---

## Post #5 by @cpinter (2025-06-18 15:40 UTC)

<p><code>SetColor</code> is supposed to only change the color, and not the lighting properties. I just tried and it works as expected, so something is different on your side. What Slicer version do you use? What extensions are installed? If you use custom code, what does it do? Do you get any errors/warnings in the log? And whatever information you consider useful…</p>

---

## Post #6 by @lassoan (2025-06-18 19:32 UTC)

<p>It looks like you have called <code>SetColor(0, 0, 255)</code> instead of the correct <code>SetColor(0, 0, 1)</code>.</p>
<p>VTK (and therefore Slicer) specifies color and opacity components uses floating point numbers between 0 and 1 to . It is sometimes useful to be able to set color intensity slightly above 100%, but 25500% is way too high, threfore all that you see is the flat ambient color. When you interact with the GUI, it normalizes the value ranges between 0-100%, that’s why after that everything looks normal again.</p>

---

## Post #7 by @chz31 (2025-06-18 21:20 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Yes, I did do SetColor(0, 0, 255). Sorry I did not describe my issue clearly. I did not realize that was the problem. SetColor() with value between 0 to 1 solved my problem. Thanks!</p>

---
