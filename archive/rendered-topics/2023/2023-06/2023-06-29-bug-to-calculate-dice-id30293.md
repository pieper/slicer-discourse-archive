---
topic_id: 30293
title: "Bug To Calculate Dice"
date: 2023-06-29
url: https://discourse.slicer.org/t/30293
---

# bug to calculate dice

**Topic ID**: 30293
**Date**: 2023-06-29
**URL**: https://discourse.slicer.org/t/bug-to-calculate-dice/30293

---

## Post #1 by @steph85 (2023-06-29 02:39 UTC)

<p>Hi, have you some problem to calculate a dice because for me it takes me too time.</p>

---

## Post #2 by @cpinter (2023-06-29 09:52 UTC)

<p>Please tell us more. Where does the data come from? What is the resolution? What Slicer version you are using? What module? How do you use the module? What did you expect to happen and what happened instead?</p>

---

## Post #3 by @steph85 (2023-06-29 15:23 UTC)

<p>The data are from a one drive and i import them to the software in the dicom database then i choose two strustures set to make a segment comparaison, i would like to compare two structures (oragan by organ) set dicom ( around fifty thousand bytes each), i dont know at that what is the resolution, i use the 5.2.2 version on slicer 3d plus slicerRT extension, i use segment comparaison for the choice of the module… I make a comparaison of two structures (ex: lung/ lung, buccal cavity/buccal cavity<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01646664bfcf311a8768509efb5b318257f5f416.png" data-download-href="/uploads/short-url/cjAaGnkHv5eN7KjnWaNlZfcyoe.png?dl=1" title="Capture d&amp;#39;écran 2023-06-29 172053" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01646664bfcf311a8768509efb5b318257f5f416_2_690x215.png" alt="Capture d'écran 2023-06-29 172053" data-base62-sha1="cjAaGnkHv5eN7KjnWaNlZfcyoe" width="690" height="215" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01646664bfcf311a8768509efb5b318257f5f416_2_690x215.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01646664bfcf311a8768509efb5b318257f5f416_2_1035x322.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01646664bfcf311a8768509efb5b318257f5f416_2_1380x430.png 2x" data-dominant-color="8F8E96"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d&amp;#39;écran 2023-06-29 172053</span><span class="informations">1600×499 52.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
) and</p>

---

## Post #4 by @gcsharp (2023-06-29 16:07 UTC)

<p>Out of memory.</p>
<p>My first thought is that you have too many structures for the size of your RAM.  You might try deleting any structures you don’t need.</p>
<p>My second thought is you might be running other memory-hungry applications.  You can check memory usage in Task Manager.</p>

---

## Post #5 by @steph85 (2023-06-29 16:22 UTC)

<p>Thank you i will try with checking the ram… The problem with the structures is i don’t know how to import structure by structure and not all the structure set like i made from eclipse. I will search if it’s possible.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e462ce39a051dfd1fe1d5fa56006fa8d5181f5d5.png" data-download-href="/uploads/short-url/wAoyiy8DpQfyIVmpvPvqW0i40GF.png?dl=1" title="Capture d&amp;#39;écran 2023-06-29 181924" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e462ce39a051dfd1fe1d5fa56006fa8d5181f5d5.png" alt="Capture d'écran 2023-06-29 181924" data-base62-sha1="wAoyiy8DpQfyIVmpvPvqW0i40GF" width="690" height="181" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d&amp;#39;écran 2023-06-29 181924</span><span class="informations">707×186 3.51 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @gcsharp (2023-06-29 16:45 UTC)

<p>If you can’t exclude them on export, you could delete them in 3D Slicer after import.</p>

---

## Post #7 by @steph85 (2023-07-23 12:21 UTC)

<p>thx for your reply, it’s all good now !</p>

---
