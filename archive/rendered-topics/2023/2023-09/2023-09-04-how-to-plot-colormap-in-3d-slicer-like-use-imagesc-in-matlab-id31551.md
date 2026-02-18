# How to plot colormap in 3D SLICER，like use imagesc in matlab

**Topic ID**: 31551
**Date**: 2023-09-04
**URL**: https://discourse.slicer.org/t/how-to-plot-colormap-in-3d-slicer-like-use-imagesc-in-matlab/31551

---

## Post #1 by @iwangwangwang (2023-09-04 15:30 UTC)

<p>How to plot colormap in 3D SLICER，like use imagesc in matlab,<br>
or How to develop the module to Implement the function？</p>

---

## Post #2 by @pieper (2023-09-04 17:18 UTC)

<p>Hi <a class="mention" href="/u/iwangwangwang">@iwangwangwang</a>, it’s great to see your interest in developing with Slicer.  I saw from another thread that some websites aren’t easily available for you.  Are you able to access <a href="https://slicer.readthedocs.io/en/latest/">https://slicer.readthedocs.io/en/latest/</a>  and <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training" class="inline-onebox">Documentation/Nightly/Training - Slicer Wiki</a> ?  These are great places to start learning but let us know if there’s a way to make the information more available to you.</p>
<p>Regarding colormaps, I’m not familiar with matlab, but you should be able to render either direct color (RGB) or map scalar fields through a lookup table.  If you look at the documentation and it’s still not clear you can come back here for more specific information.  Usually it helps people provide you with answers if you give some more context. <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html" class="inline-onebox">Volumes — 3D Slicer documentation</a></p>

---

## Post #4 by @iwangwangwang (2023-09-05 02:15 UTC)

<p>Thanks, but let me provide a more detailed description, I want to plot 2D matrix data with color (RGB) or map scalar fields through a lookup table in 3D Slicer, just like “imshow” in python or “imagesc” in matlab， I think using 2D slice or 3D view representation is all not appropriate in 3D Slicer, so there is any other method to present 2d data ? or must develop a extension to Implement the function？<br>
sincerely wating for your answers.</p>

---

## Post #5 by @pieper (2023-09-05 12:00 UTC)

<p>Maybe you just want to us matplotlib directly: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#using-matplotlib" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>

---

## Post #6 by @iwangwangwang (2023-09-05 14:56 UTC)

<p>Of course, using Matplotlib is very convenient, but it can also make my program bulky, after all, I only need to use Matplotlib to draw color maps</p>

---

## Post #7 by @lassoan (2023-09-05 16:20 UTC)

<aside class="quote no-group" data-username="iwangwangwang" data-post="6" data-topic="31551">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/f1d935/48.png" class="avatar"> iwangwangwang:</div>
<blockquote>
<p>to draw color maps</p>
</blockquote>
</aside>
<p>Do you mean you want to display a color legend (color bar that shows what color correspond to what value) and you are not sure how to do it in Slicer?</p>

---

## Post #8 by @iwangwangwang (2023-09-05 18:58 UTC)

<p>I meant to plot a Matrix data as colormap, just like function “imshow” in python,    I don’t know if I expressed myself clearly，here is a picture for example</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2eccf32c2f12a9f324a87135dc3e622b960318d.png" alt="1693940223938" data-base62-sha1="rOnZroL6NY2Y1irTnLUrRE4jmnX" width="541" height="417"></p>

---

## Post #9 by @lassoan (2023-09-05 20:53 UTC)

<p>Slice views show “matrix data” (2D array) as an image as in your screenshot. You can select what color map you want to use for display and you can also enable displaying a color legend.</p>
<p>Do you have trouble setting these up using the GUI or Python scripting?</p>

---

## Post #10 by @iwangwangwang (2023-09-06 01:53 UTC)

<p>yes, I have trouble how to implement the function</p>

---
