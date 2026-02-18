# Grow from seeds not giving any results

**Topic ID**: 7645
**Date**: 2019-07-17
**URL**: https://discourse.slicer.org/t/grow-from-seeds-not-giving-any-results/7645

---

## Post #1 by @dfafalis (2019-07-17 22:41 UTC)

<p>Operating system:Window 7 Enterprise<br>
Slicer version: 4.11.0<br>
Expected behavior: create segments after applying “Grow from seeds” effect<br>
Actual behavior: no segments created; the seeds remained as initially painted</p>
<p>Hello,</p>
<p>I am trying to segment the non-bony parts of the cochlea.<br>
I add the segments and paint (or level trace) the segments into all three views (axial, sagittal, and coronal), in various slices<br>
Then, I try to use the effect “Grow from seeds” and I do not see any difference than the painted slices I made initially; no 3D segments generated; the seeds did not expand to the remaining slices<br>
See attached picture</p>
<p>Could you please give me an insight on what I am doing wrong?<br>
Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e68f7bc020a2a9084b495ba523ea787c06b317be.jpeg" data-download-href="/uploads/short-url/wTDeg0ujGAuzsa1hsVWFXLxXDiK.jpeg?dl=1" title="Cochlea_segmen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e68f7bc020a2a9084b495ba523ea787c06b317be_2_690x463.jpeg" alt="Cochlea_segmen" data-base62-sha1="wTDeg0ujGAuzsa1hsVWFXLxXDiK" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e68f7bc020a2a9084b495ba523ea787c06b317be_2_690x463.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e68f7bc020a2a9084b495ba523ea787c06b317be_2_1035x694.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e68f7bc020a2a9084b495ba523ea787c06b317be_2_1380x926.jpeg 2x" data-dominant-color="8C9196"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Cochlea_segmen</span><span class="informations">1503×1010 415 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-07-17 23:14 UTC)

<p>Click “Initialize” to compute full segmentation. To see preview of the full segmentation in 3D, click “Show 3D” in Grow from seeds section (next to “results” label).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a42e32cd5a4f1e689d1b45350c26c7a5bf5c7e5.png" data-download-href="/uploads/short-url/3KjID1YKlvtwVoTbeicvBt9r9op.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a42e32cd5a4f1e689d1b45350c26c7a5bf5c7e5_2_690x361.png" alt="image" data-base62-sha1="3KjID1YKlvtwVoTbeicvBt9r9op" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a42e32cd5a4f1e689d1b45350c26c7a5bf5c7e5_2_690x361.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a42e32cd5a4f1e689d1b45350c26c7a5bf5c7e5_2_1035x541.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a42e32cd5a4f1e689d1b45350c26c7a5bf5c7e5.png 2x" data-dominant-color="F2F2F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1099×575 37 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @dfafalis (2019-07-18 00:14 UTC)

<p>Hello Andras,</p>
<p>Thank you for your quick reply.</p>
<p>In the picture I had attached in my initial post I did not show that I had clicked on the effect “Grow from seeds”, then “Initialize”, etc.</p>
<p>I had just screenshot my segmentation model, so I apologize if it was misleading regarding my question.</p>
<p>I attach more figures to show the error displayed by Slicer; you can also see that the colors’ tones have changed from the original,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5f560355cfc4091095eeb9f7285b8177d8d77a1.jpeg" data-download-href="/uploads/short-url/wOj3te3BTDM0ax8wcbgDPHiIWcN.jpeg?dl=1" title="Cochlea_segmen_error_1.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5f560355cfc4091095eeb9f7285b8177d8d77a1_2_690x464.jpeg" alt="Cochlea_segmen_error_1.png" data-base62-sha1="wOj3te3BTDM0ax8wcbgDPHiIWcN" width="690" height="464" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5f560355cfc4091095eeb9f7285b8177d8d77a1_2_690x464.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5f560355cfc4091095eeb9f7285b8177d8d77a1_2_1035x696.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5f560355cfc4091095eeb9f7285b8177d8d77a1_2_1380x928.jpeg 2x" data-dominant-color="9B9EA4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Cochlea_segmen_error_1.png</span><span class="informations">1499×1009 452 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>however, no growth has happened as it is obvious from both the 3D view and the 2D views</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7ee5464dd2fc15af200764a3e5da7ed63fe9821.jpeg" data-download-href="/uploads/short-url/swFDp82WqWtkRSlV0XZqtbUO2WZ.jpeg?dl=1" title="Cochlea_segmen_error_2.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7ee5464dd2fc15af200764a3e5da7ed63fe9821_2_690x463.jpeg" alt="Cochlea_segmen_error_2.png" data-base62-sha1="swFDp82WqWtkRSlV0XZqtbUO2WZ" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7ee5464dd2fc15af200764a3e5da7ed63fe9821_2_690x463.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7ee5464dd2fc15af200764a3e5da7ed63fe9821_2_1035x694.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7ee5464dd2fc15af200764a3e5da7ed63fe9821_2_1380x926.jpeg 2x" data-dominant-color="84878A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Cochlea_segmen_error_2.png</span><span class="informations">1503×1010 453 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is this because I have used the “Paint”, “Draw” and “Level Tracing” effects in all three 2D views and not only one?</p>
<p>For your information, all segments shown have been drawn independently, that said, I have not used any masking effect at all. Could that be a problem?</p>
<p>I tried the “Grow from seeds” effect in another model, based on a substack of the model I show in these emails; there, I created the segments based on a mask and only on the “Axial” 2D view.</p>
<p>I really appreciate your feedback and insight.</p>
<p>Looking forward for your reply.</p>
<p>Best</p>
<p>Dimitrios</p>

---

## Post #4 by @lassoan (2019-07-18 02:00 UTC)

<p>The error message indicates that you’ve run out of memory. Increase your virtual memory size in your operating system settings, add more physical RAM to your computer, or crop/resample your input volume.</p>

---

## Post #5 by @Wissen (2019-08-07 03:49 UTC)

<p>I also face the same issue.Have you got the way to solve it?</p>

---

## Post #6 by @lassoan (2019-08-07 04:21 UTC)

<p>What error message do you see?<br>
How large is your input volume?<br>
How much RAM do you have in your computer?<br>
What operating system do you use?</p>

---

## Post #7 by @Wissen (2019-08-07 05:50 UTC)

<p>No errors represented.After I painted the images,the ‘supply’ button in ‘grow from seeds’ was not enabled.<br>
Input volume:1165 images<br>
RAM:8G<br>
operating system:Windows 10<br>
Thank you</p>

---

## Post #8 by @lassoan (2019-08-10 13:05 UTC)

<aside class="quote no-group" data-username="Wissen" data-post="7" data-topic="7645">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/a9adbd/48.png" class="avatar"> Wissen:</div>
<blockquote>
<p>After I painted the images,the ‘supply’ button in ‘grow from seeds’ was not enabled</p>
</blockquote>
</aside>
<p>You need to click “Initialize” first.</p>
<aside class="quote no-group" data-username="Wissen" data-post="7" data-topic="7645">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/a9adbd/48.png" class="avatar"> Wissen:</div>
<blockquote>
<p>Input volume:1165 images<br>
RAM:8G</p>
</blockquote>
</aside>
<p>You can find dimensions of your volume in Volumes module (information section), but most probably you are tight on memory. Add 30GB of virtual memory to make sure you have enough memory space.</p>

---
