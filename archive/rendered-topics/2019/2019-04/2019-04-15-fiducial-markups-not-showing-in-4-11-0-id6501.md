# Fiducial markups not showing in 4.11.0

**Topic ID**: 6501
**Date**: 2019-04-15
**URL**: https://discourse.slicer.org/t/fiducial-markups-not-showing-in-4-11-0/6501

---

## Post #1 by @Hao_Li (2019-04-15 11:47 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da8e1d30fe550d875f1f5e1a8c4e8a36f7ab72cd.png" data-download-href="/uploads/short-url/vbqz7tnBDGePwRgcUyql3t6n7yJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/da8e1d30fe550d875f1f5e1a8c4e8a36f7ab72cd_2_690x490.png" alt="image" data-base62-sha1="vbqz7tnBDGePwRgcUyql3t6n7yJ" width="690" height="490" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/da8e1d30fe550d875f1f5e1a8c4e8a36f7ab72cd_2_690x490.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/da8e1d30fe550d875f1f5e1a8c4e8a36f7ab72cd_2_1035x735.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/da8e1d30fe550d875f1f5e1a8c4e8a36f7ab72cd_2_1380x980.png 2x" data-dominant-color="94939C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2849×2025 484 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hi!</p>
<p>Sorry for stupid question. Fiducial markups I’ve created using slicer 4.8.1 don’t appear in the 3D window (appear fine on the other 3 windows) on slicer 4.11.0. Any idea where I did wrong?</p>
<p>Best regards<br>
Hao</p>

---

## Post #2 by @lassoan (2019-04-15 13:58 UTC)

<p>I could not reproduce the issue. Please try with the latest nightly build. If it still fails then please upload an example scene somewhere (dropbox, onedrive, etc.) and post the link here.</p>

---

## Post #3 by @Hao_Li (2019-04-16 08:18 UTC)

<p>Hi!</p>
<p>Thanks for replying.</p>
<p>I have tried further versions of slicer. The fiducial markups show fine on (4.10.1) but only not on (4.11.0-2019-04-12).</p>
<p><a href="https://www.dropbox.com/sh/1bkqco8w9ej7d9z/AACynDK0DeFvnBH_-2trBoWIa?dl=0" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.dropbox.com/sh/1bkqco8w9ej7d9z/AACynDK0DeFvnBH_-2trBoWIa?dl=0</a></p>
<p>Here are two movies showing 4.10.1 and 4.11.0. The fiducials were saved in slicer 4.8.1.</p>
<p>I’ve also figured out how to make it work in 4.11.0-2019-04-12. You need original data (CT), then add a few fiducials. Then open the previously saved fiducials, and it will work.</p>
<p>Best regards<br>
Hao Li</p>

---

## Post #4 by @lassoan (2019-04-16 14:01 UTC)

<p>Thanks for the videos. I was able to reproduce the issue and fix it. Tomorrow’s nightly build should work well.</p>

---

## Post #5 by @jancarad (2021-04-09 12:03 UTC)

<p>Hi, the problem still occurs in 4.11.20210226 (Win10).<br>
The mrml/mrb files build in 4.10.2 are incorrectly showed without markups-fiducials in slice windows. Pleas, keep back-compatibility =)<br>
Best regards,<br>
Radek</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/255666a2e767911c5524984a9a99b756f73d77d7.png" data-download-href="/uploads/short-url/5kiMkw27dnJYAoxA0jFGuYIDxfF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/255666a2e767911c5524984a9a99b756f73d77d7.png" alt="image" data-base62-sha1="5kiMkw27dnJYAoxA0jFGuYIDxfF" width="690" height="386" data-dominant-color="EAEFF2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">753×422 17.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2021-04-10 15:11 UTC)

<p>We always maintain backward compatibility with at least the previous major version (and as much as possible, with earlier versions, too).</p>
<p>The problem you encountered is due to that Slicer-4.10 did not take into account slice visibility attribute for markup nodes and Slicer-4.11 does (and by default slice visibility was turned off for markups).</p>
<p>As a workaround, you can right-click on eye icon of the markups node in Data module and check “2D visibility”,  I’ve also submitted a <a href="https://github.com/Slicer/Slicer/commit/135f359dace2ad52f911604177dc064d7076da89">fix</a> that enables 2D visibility for markups by default when an old scene is loaded (it will be available in Slicer Preview Releases downloaded tomorrow or later).</p>

---

## Post #7 by @jancarad (2021-04-12 07:47 UTC)

<p>Dear Mr. Lasso,</p>
<p>Thank you for your response, but my problem is probably different. I remember on your described solution, some fields in .fcsv were incorrectly read (older version read 1.00 as true, in 4.10.2 only 1 was accepted).</p>
<p>However, the actual problem is different. Markups module of 4.11 shows everything as showing. The warning is similar for both versions, which can be confusing. Fiducials in 3D view are shown, not in slices, and change properties affect only 3D. The only working way is manually adding the fiducial list to the scene, which leads to a built-up new DataNode.</p>
<p>Here are a screenshot and link to the example .mrb file.</p>
<p><a href="https://owncloud.cesnet.cz/index.php/s/qCKvS4Yi0sAX1RE" rel="noopener nofollow ugc">https://owncloud.cesnet.cz/index.php/s/qCKvS4Yi0sAX1RE</a></p>
<p>This problem covers an extensive dataset of our research that prohibits using actual versions of Slicer.</p>
<p>Thank you for your time.</p>
<p>Best regards,</p>
<p>Radek Janca</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7f88ee3a94d5705f62cc2a32e0e972540bbb4ee.jpeg" data-download-href="/uploads/short-url/x66PoYAF3yjQHbpLTvqLvua4XVQ.jpeg?dl=1" title="image002.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7f88ee3a94d5705f62cc2a32e0e972540bbb4ee_2_690x376.jpeg" alt="image002.jpg" data-base62-sha1="x66PoYAF3yjQHbpLTvqLvua4XVQ" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7f88ee3a94d5705f62cc2a32e0e972540bbb4ee_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7f88ee3a94d5705f62cc2a32e0e972540bbb4ee.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7f88ee3a94d5705f62cc2a32e0e972540bbb4ee.jpeg 2x" data-dominant-color="9EA0A8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image002.jpg</span><span class="informations">811×442 50.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2021-04-13 04:17 UTC)

<p>As I wrote above, you can right-click on the eye icon of markups fiducial node in Data module and check “2D visibility” option to fix the loading from old scenes.</p>
<p>You can also use the latest Slicer Preview Release that automatically enables 2D visibility for markups fiducials when loaded from old scenes (I’ve just tested Slicer-4.13.0 2020-04-10 and it displays your Slicer-4.10.2 scene correctly).</p>
<p>Slicer-4.13 has lots of improvements in markups. I would recommend to have a look at markups curves, which you can use to display electrodes as lines instead of just point sets (but you can assign names to each control point of the curve as you can do for markups fiducials):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45ca46a1022b415a6dee087688cc05a1e943f015.jpeg" data-download-href="/uploads/short-url/9XojOptMNUTFJBFjfjwmPRhvxXf.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45ca46a1022b415a6dee087688cc05a1e943f015_2_690x419.jpeg" alt="image" data-base62-sha1="9XojOptMNUTFJBFjfjwmPRhvxXf" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45ca46a1022b415a6dee087688cc05a1e943f015_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45ca46a1022b415a6dee087688cc05a1e943f015_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45ca46a1022b415a6dee087688cc05a1e943f015_2_1380x838.jpeg 2x" data-dominant-color="919397"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1370 548 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @jancarad (2021-04-13 09:21 UTC)

<p>Oh, it is working, amazing!</p>
<p>Thank you a lot for your time, and I am sorry for my ignorance. It is a new feature for me.</p>
<p>Best wishes,</p>
<p>Radek Janca</p>

---
