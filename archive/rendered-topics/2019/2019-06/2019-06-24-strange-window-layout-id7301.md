---
topic_id: 7301
title: "Strange Window Layout"
date: 2019-06-24
url: https://discourse.slicer.org/t/7301
---

# Strange Window Layout

**Topic ID**: 7301
**Date**: 2019-06-24
**URL**: https://discourse.slicer.org/t/strange-window-layout/7301

---

## Post #1 by @Lorensen (2019-06-24 22:06 UTC)

<p>When I run Slicer, the left window is very large. Do I have some old config file somewhere?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4267df2067f84275564f0df2e354bc6452bc14c.png" data-download-href="/uploads/short-url/nq8LYAUXKO68VGRDFY6YqMHGHw0.png?dl=1" title="Slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a4267df2067f84275564f0df2e354bc6452bc14c_2_690x388.png" alt="Slicer" data-base62-sha1="nq8LYAUXKO68VGRDFY6YqMHGHw0" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a4267df2067f84275564f0df2e354bc6452bc14c_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a4267df2067f84275564f0df2e354bc6452bc14c_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a4267df2067f84275564f0df2e354bc6452bc14c_2_1380x776.png 2x" data-dominant-color="BEBCC4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer</span><span class="informations">1920×1080 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jamesobutler (2019-06-24 22:21 UTC)

<p>Looks like some weird scaling going on. Did you switch to a 4K/higher-res monitor or something?</p>
<p>Anyways, the left side window area should be resizeable. Just grab the divider between the left window area and the layout manager and move it to the left.</p>

---

## Post #3 by @Lorensen (2019-06-24 22:26 UTC)

<p>The monitor is 1920x1080.  The interface will not let me move it to the left,</p>

---

## Post #4 by @rkikinis (2019-06-25 02:20 UTC)

<p>The control are the five discrete dots, arranged vertically, between the red viewer and the slider. Did you grab there?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47df720d7d4405f953702bec42b20274a76da517.png" data-download-href="/uploads/short-url/afOD4ymyEfr8SLNa1yY6bRfIzbN.png?dl=1" title="a4267df2067f84275564f0df2e354bc6452bc14c.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47df720d7d4405f953702bec42b20274a76da517_2_690x388.png" alt="a4267df2067f84275564f0df2e354bc6452bc14c.png" data-base62-sha1="afOD4ymyEfr8SLNa1yY6bRfIzbN" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47df720d7d4405f953702bec42b20274a76da517_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47df720d7d4405f953702bec42b20274a76da517_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47df720d7d4405f953702bec42b20274a76da517.png 2x" data-dominant-color="BEBCC3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">a4267df2067f84275564f0df2e354bc6452bc14c.png</span><span class="informations">1280×720 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Lorensen (2019-06-25 02:37 UTC)

<p>Yes I did. It only lets it move left s tiny bit.</p>
<p>Where is the screen configuration stored? I might have some old config file around.</p>

---

## Post #6 by @Lorensen (2019-06-25 02:51 UTC)

<p>I found the Slicer.ini file and deleted it,  but the results are the same.</p>

---

## Post #7 by @jamesobutler (2019-06-25 02:51 UTC)

<p>Did you previously have a higher resolution monitor? It appears that it is scaling all the widgets by maybe 250%. Maybe your OS is doing this for the specific application. There’s probably some widget in the left side area that has a larger minimum size which is why you can’t collapse it much further.</p>
<p>QSettings typically stores window location and size but I don’t believe anything related to scaling. The location of the file can be found <a href="https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/ApplicationSettings#Settings_file_location" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/ApplicationSettings#Settings_file_location</a></p>

---

## Post #8 by @Lorensen (2019-06-25 02:58 UTC)

<p>For sure the widgets are being scaled.</p>

---

## Post #9 by @lassoan (2019-06-25 03:13 UTC)

<p>You can try adjusting application scaling manually by modifying environment variables before starting Slicer:</p>
<pre><code class="lang-auto">QT_AUTO_SCREEN_SCALE_FACTOR=0
QT_SCALE_FACTOR=2
</code></pre>
<p>or</p>
<pre><code class="lang-auto">QT_AUTO_SCREEN_SCALE_FACTOR=1
</code></pre>
<p>You may also try to adjust font size in menu: Edit / Application settings / Appearance.</p>

---

## Post #10 by @Lorensen (2019-06-25 03:39 UTC)

<p>QT_AUTO_SCREEN_SCALE_FACTOR=0<br>
QT_SCALE_FACTOR=1</p>
<p>Works!</p>
<p>Thanks</p>

---
