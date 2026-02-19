---
topic_id: 30326
title: "New Fastmodelalign Module In Slicermorph"
date: 2023-06-30
url: https://discourse.slicer.org/t/30326
---

# New FastModelAlign module in SlicerMorph

**Topic ID**: 30326
**Date**: 2023-06-30
**URL**: https://discourse.slicer.org/t/new-fastmodelalign-module-in-slicermorph/30326

---

## Post #1 by @muratmaga (2023-06-30 18:18 UTC)

<p>The pointcloud based registration of 3D models is now incorporated into SlicerMorph as <strong>FastModelAlign</strong> (SlicerMorph-&gt;Utilities-&gt;FastModelAlign).</p>
<p>Instead of a full model registration, similar to ALPACA, module converts models to sparser point clouds, then computes scaling, rigid and affine registration on them as requested by the user. The outputs of the module are the modified source model, as well as the transformation matrices that were generated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/347cf530f4d726f709b8c3e05e72bdd498b066b8.jpeg" data-download-href="/uploads/short-url/7uky3o4W5BGKnNY0E7Y0hwQrI1y.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/347cf530f4d726f709b8c3e05e72bdd498b066b8_2_690x480.jpeg" alt="image" data-base62-sha1="7uky3o4W5BGKnNY0E7Y0hwQrI1y" width="690" height="480" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/347cf530f4d726f709b8c3e05e72bdd498b066b8_2_690x480.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/347cf530f4d726f709b8c3e05e72bdd498b066b8_2_1035x720.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/347cf530f4d726f709b8c3e05e72bdd498b066b8.jpeg 2x" data-dominant-color="B6B9CF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1144×796 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3395da8f74fdc0c8440281738d2123724b2f836.png" alt="image" data-base62-sha1="pzun7NJI1JBz7pyZ1iMZVATYmRU" width="499" height="179"></p>
<p>The initial prototype has been developed during the last PW by <a class="mention" href="/u/chz31">@chz31</a> with contributions from <a class="mention" href="/u/agporto">@agporto</a> and <a class="mention" href="/u/smrolfe">@smrolfe</a>.</p>

---

## Post #2 by @muratmaga (2023-07-01 02:09 UTC)

<p>FYI, today’s version requires the user to switch to <strong>ALPACA_preview</strong> module to install the necessary ITK python libraries that are used both modules. To do so, in the Module Finder, enable the testing mode and search for ALPACA_preview.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f80281f785b73380ba6aa9a8071da9e40678f817.png" alt="image" data-base62-sha1="znZMGUJuyQbay6lCVUyohq2QRYX" width="682" height="166"></p>
<p>It may take a minute to install the python packages, after which you can switch back to FastModelAlign. Starting with tomorrow’s build, this will be automatically invoked first time the user opens the <strong>FastModelAlign</strong> module.</p>

---

## Post #3 by @SANTIAGO_PENDON_MING (2023-07-03 07:53 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a>, very nice update.</p>
<p>In the process of installing the packages an error occurs. I’ll show you in the next image:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38a2178892b18076dd70adb39e20d2a5338fe107.png" data-download-href="/uploads/short-url/85019SovEWk9VrBIywxSCaAG5Ab.png?dl=1" title="Captura de pantalla 2023-07-03 094648" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38a2178892b18076dd70adb39e20d2a5338fe107_2_690x356.png" alt="Captura de pantalla 2023-07-03 094648" data-base62-sha1="85019SovEWk9VrBIywxSCaAG5Ab" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38a2178892b18076dd70adb39e20d2a5338fe107_2_690x356.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38a2178892b18076dd70adb39e20d2a5338fe107_2_1035x534.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38a2178892b18076dd70adb39e20d2a5338fe107_2_1380x712.png 2x" data-dominant-color="353335"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2023-07-03 094648</span><span class="informations">1386×716 79.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I run the ALPACA (preview) for the first time, it started to install all the necessary dependencies, but it fails with the error I show before.</p>
<p>If I try to use the Fast Align Model, it also occurs a new error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7d0092ff1de74742d19182225666375e7008140.png" data-download-href="/uploads/short-url/svCJlHPwGgvWt7KUBjH7giKupYA.png?dl=1" title="Captura de pantalla 2023-07-03 095037" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7d0092ff1de74742d19182225666375e7008140.png" alt="Captura de pantalla 2023-07-03 095037" data-base62-sha1="svCJlHPwGgvWt7KUBjH7giKupYA" width="690" height="173" data-dominant-color="292222"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2023-07-03 095037</span><span class="informations">1520×382 21.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As I understand, the last error becomes from the first one, is´nt it?</p>
<p>If you could help me it would be great. Thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> .</p>

---

## Post #4 by @muratmaga (2023-07-03 14:49 UTC)

<p>Instead of the screenshots, please copy and paste the text of all the error message, because things are truncated.</p>
<p>In your first screenshot the error is about not being being able to install open3d, which is neither used by ALPACA_preview nor by FastModelAlign, so I am not sure where it is coming from.</p>
<p>If you update your SlicerMorph extension, and try directly going to FastModelAlign, it should now automatically switch to ALPACA_preview and install the necessary files (it may take a minute). If doesn’t, please copy and paste the text of the full error log, and tell us what version of Slicer you are using.</p>

---
