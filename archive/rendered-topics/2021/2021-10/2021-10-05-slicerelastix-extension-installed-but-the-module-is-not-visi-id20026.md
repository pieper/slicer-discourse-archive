---
topic_id: 20026
title: "Slicerelastix Extension Installed But The Module Is Not Visi"
date: 2021-10-05
url: https://discourse.slicer.org/t/20026
---

# SlicerElastix extension installed but the module is not visible anywhere

**Topic ID**: 20026
**Date**: 2021-10-05
**URL**: https://discourse.slicer.org/t/slicerelastix-extension-installed-but-the-module-is-not-visible-anywhere/20026

---

## Post #1 by @Roman (2021-10-05 16:11 UTC)

<p>Operating system: Win10<br>
Slicer version: 4.11.20210226 r29738 / 7a593c8<br>
Installed SlicerElastix extension - shows up in the Extensions Manager.<br>
Expected behavior: I expect to see module “General Registration (Elastix)” as in theis demo <a href="https://www.youtube.com/watch?v=cU0pWhn0-3o&amp;ab_channel=PerkLabResearch" class="inline-onebox" rel="noopener nofollow ugc">Elastix registration toolbox in 3D Slicer - YouTube</a><br>
Actual behavior: There is no module “General Registration (Elastix)” (or anything with the work elastix) in the Registration section of the list of the modules.</p>
<p>How can I locate the installed tool?<br>
Thanks</p>

---

## Post #2 by @Alex_Vergara (2021-10-05 16:28 UTC)

<p>I am sorry to ask but did you restarted Slicer after installing the extension?</p>

---

## Post #3 by @Roman (2021-10-05 16:40 UTC)

<p>Thanks. Several times.</p>

---

## Post #4 by @lassoan (2021-10-05 18:36 UTC)

<p>I’ve checked this and using this Slicer version on Windows, the extension shows up:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d66ce9fb7e1b3801f5c39cc49dd40f8dc58081a1.png" data-download-href="/uploads/short-url/uATwBimmNXe6u9rLZoJgkqO3Vcd.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d66ce9fb7e1b3801f5c39cc49dd40f8dc58081a1_2_690x456.png" alt="image" data-base62-sha1="uATwBimmNXe6u9rLZoJgkqO3Vcd" width="690" height="456" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d66ce9fb7e1b3801f5c39cc49dd40f8dc58081a1_2_690x456.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d66ce9fb7e1b3801f5c39cc49dd40f8dc58081a1_2_1035x684.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d66ce9fb7e1b3801f5c39cc49dd40f8dc58081a1_2_1380x912.png 2x" data-dominant-color="3D3E41"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1863×1233 295 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you still cannot find the module then please upload the application log somewhere (menu: Help / Report a bug) and copy the link here.</p>

---

## Post #5 by @Roman (2021-10-05 20:39 UTC)

<p>Thanks, Andras.<br>
Module finder does not locate it.<br>
Interestingly, log has a line “[DEBUG][Qt] 05.10.2021 21:23:56 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: (none)” Does this mean the extension didn’t actually get installed?<br>
Extension Manager screenshot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ee8de23076634aaee0ab31ea6422d05d98cf832.png" data-download-href="/uploads/short-url/27TBhHClQF5NIceL2cce02ipxzs.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ee8de23076634aaee0ab31ea6422d05d98cf832_2_497x118.png" alt="image.png" data-base62-sha1="27TBhHClQF5NIceL2cce02ipxzs" width="497" height="118" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ee8de23076634aaee0ab31ea6422d05d98cf832_2_497x118.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ee8de23076634aaee0ab31ea6422d05d98cf832_2_745x177.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ee8de23076634aaee0ab31ea6422d05d98cf832.png 2x" data-dominant-color="EAEFF2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">823×195 13.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is the log <a href="https://drive.google.com/file/d/1l-Vq0Co1YKLW1yKmFr3EPC5FyuVjprN-/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1l-Vq0Co1YKLW1yKmFr3EPC5FyuVjprN-/view?usp=sharing</a></p>

---

## Post #6 by @lassoan (2021-10-05 20:46 UTC)

<p>Yes, the extension should be listed in the additional module paths, something like this:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 05.10.2021 16:40:46 [] (unknown:0) - Additional module paths ..: NA-MIC/Extensions-29738/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules
</code></pre>
<p>Did you install Slicer in a location where you have write access?<br>
Is that a regular local disk (not a network drive or virtual network drive, such as google or box)?</p>
<p>Do you have a NA-MIC/Extensions-29738/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules folder within your Slicer installation folder?</p>
<p>Do you use Avast or other third-party antivirus? (they can silently delete files from your hard disk that they don’t trust)</p>

---

## Post #7 by @Roman (2021-10-05 21:01 UTC)

<p>Thanks for the prompt response. Extremely impressive!<br>
Installed locally where the installer suggested. Regular local disk<br>
C:\Users&lt;user name&gt;\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules</p>
<p>I use F-Secure. Not sure how it is configured (not by me).</p>
<p>Blaming antivirus?</p>

---

## Post #8 by @lassoan (2021-10-05 21:08 UTC)

<p>Does Elastix work well if you manually add the <code>C:\Users&lt;user name&gt;\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules</code> path to your additional module paths in menu: Edit / Application settings / Modules?</p>
<p>Do you have this problem with other extensions, too? (for example, SlicerIGT, Sandbox, SegmentEditorExtraEffects, …)</p>

---

## Post #9 by @Roman (2021-10-05 21:17 UTC)

<p>Many thanks. Adding the path manually resolved the issue.<br>
This is the only extension I have so far. Shall I test if this situation happens with other extensions?</p>

---

## Post #10 by @lassoan (2021-10-05 21:19 UTC)

<p>Yes it would be interesting to know if this is something specific to this extension. For example, install SlicerIGT and Sandbox extensions and see if their module folders get added to the additional module paths.</p>

---

## Post #11 by @Roman (2021-10-05 21:29 UTC)

<p>installed SlicerIGT.<br>
Is it IGT group which I should expect as a result?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b4d835f63378c3ace96e4a66cacba4a6d3ca635.png" data-download-href="/uploads/short-url/fjf9X94Fj4txj824JLs1pEIdWdf.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b4d835f63378c3ace96e4a66cacba4a6d3ca635.png" alt="image.png" data-base62-sha1="fjf9X94Fj4txj824JLs1pEIdWdf" width="438" height="497" data-dominant-color="CCCFCF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">520×590 31.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @lassoan (2021-10-05 22:07 UTC)

<p>Yes, it looks good. We’ll keep an eye on this but maybe we can blame the antivirus then.</p>

---
