---
topic_id: 10628
title: "Cant Open Saved Mrml File"
date: 2020-03-10
url: https://discourse.slicer.org/t/10628
---

# Can't open saved MRML file

**Topic ID**: 10628
**Date**: 2020-03-10
**URL**: https://discourse.slicer.org/t/cant-open-saved-mrml-file/10628

---

## Post #1 by @getiwh (2020-03-10 22:27 UTC)

<p>Operating system: Mac OSX<br>
Slicer version: 4.11.0<br>
Expected behaviour: Open saved MRML file of MRI<br>
Actual behaviour: Zero bytes file and blank screen</p>
<p>I’m not very technically inclined, and have just recently downloaded Slicer to digitise some MRI scans for a project. I have been painting muscle boundaries and saved my work, but then when I try open the file on Slicer nothing happens. Info of the file says it’s zero bytes. There’s no error code, it just doesn’t open anything.</p>
<p>The file is named: 2020-03-08 Scene.mrml</p>
<p>I’m not very proficient with IT or Slicer so please help!</p>

---

## Post #2 by @lassoan (2020-03-10 22:29 UTC)

<p>What file has zero bytes? How did you save the scene? How do you open the scene?</p>
<p>If storage space is not a concern, the simplest is to save everything into a single .mrb file by clicking on the package icon in the Save data window.</p>

---

## Post #3 by @getiwh (2020-03-10 22:40 UTC)

<p>The 2020-03-08 Scene.mrml file that I saved has zero bytes.<br>
I saved the scene by the ‘command+S’ and just clicked enter, saving it by the default which created the mrml file. I didn’t click on anything else in the Save data window.</p>
<p>To try open the scene, I clicked the upload data icon in the top right of the toolbar and tried to open it here. I also tried opening the file by right clicking it in the desktop and choosing an application to open it but this didn’t work either.</p>

---

## Post #4 by @lassoan (2020-03-11 12:40 UTC)

<p>If the mrml file has zero length then it is empty and you cannot open it. Was any error logged during file scene saving (you can find logs of current and last 10 sessions in menu: Help / Report a bug)? Is the problem reproducible with any of the Slicer sample data sets (in Sample Data module)?</p>

---

## Post #5 by @getiwh (2020-03-11 20:26 UTC)

<p>I have saved a new set of MRI slides as an ‘.mrb’ file and it still won’t open on my Slicer programme.<br>
Attached is the error messaged displayed when trying to open the medical reality bundle. There’s lots of error messages saying there was an error loading file. I don’t have much space on my computer but have been trying to save my data on a server using a VPN from my university.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d64b3bfe936a9c29028ace7f7f143f229d81a2b.png" data-download-href="/uploads/short-url/dkc9NLhJ1wWhK9eB3Th3G96y7AD.png?dl=1" title="Screen Shot 2020-03-12 at 9.17.48 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d64b3bfe936a9c29028ace7f7f143f229d81a2b_2_690x412.png" alt="Screen Shot 2020-03-12 at 9.17.48 AM" data-base62-sha1="dkc9NLhJ1wWhK9eB3Th3G96y7AD" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d64b3bfe936a9c29028ace7f7f143f229d81a2b_2_690x412.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d64b3bfe936a9c29028ace7f7f143f229d81a2b_2_1035x618.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d64b3bfe936a9c29028ace7f7f143f229d81a2b_2_1380x824.png 2x" data-dominant-color="E3E8EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-03-12 at 9.17.48 AM</span><span class="informations">1498×896 87 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/187566b7de2cb59b3d53bc1e34e28adebcaca3cb.png" data-download-href="/uploads/short-url/3umZoGNXldZoGYlM6R0wHvD7e67.png?dl=1" title="Screen Shot 2020-03-12 at 9.20.41 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/187566b7de2cb59b3d53bc1e34e28adebcaca3cb_2_690x359.png" alt="Screen Shot 2020-03-12 at 9.20.41 AM" data-base62-sha1="3umZoGNXldZoGYlM6R0wHvD7e67" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/187566b7de2cb59b3d53bc1e34e28adebcaca3cb_2_690x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/187566b7de2cb59b3d53bc1e34e28adebcaca3cb_2_1035x538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/187566b7de2cb59b3d53bc1e34e28adebcaca3cb_2_1380x718.png 2x" data-dominant-color="E2E5EE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-03-12 at 9.20.41 AM</span><span class="informations">2560×1334 501 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @jamesobutler (2020-03-11 21:27 UTC)

<p>It appears that specific traceback error was resolved on March 5th <a href="https://github.com/Slicer/Slicer/commit/c6cfc9e6e909b1b201f4bdd29dd74e418973314e" rel="nofollow noopener">https://github.com/Slicer/Slicer/commit/c6cfc9e6e909b1b201f4bdd29dd74e418973314e</a><br>
so would’ve been included in any Slicer Preview build since March 6th.</p>
<p>Since the file has zero length you won’t be able to recover that work, but I would suggest trying again whatever you were attempting with the latest Slicer preview from <a href="https://download.slicer.org/" rel="nofollow noopener">https://download.slicer.org/</a>.</p>

---
