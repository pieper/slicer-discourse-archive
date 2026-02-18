# Can't find segmentcomparison in SlicerRT in the 3d slicer 5.6.2

**Topic ID**: 38379
**Date**: 2024-09-14
**URL**: https://discourse.slicer.org/t/cant-find-segmentcomparison-in-slicerrt-in-the-3d-slicer-5-6-2/38379

---

## Post #1 by @Alice914 (2024-09-14 15:31 UTC)

<p>Hi!<br>
My 3d slicer version is 5.6.2 in Ubuntu24.04 and Windows11. I try to find Segment Comparison in two systems, but I can’t find it in the module. Could you taught me how to calculate <strong>Hausdorff Distance</strong>、<strong>Mean Distance</strong> or <strong>Dice Similarity Coefficient</strong> in 3d slicer? Thank you for your help.</p>

---

## Post #2 by @lassoan (2024-09-14 15:32 UTC)

<p>After you install 3D Slicer, please install SlicerRT extension in the Extensions Manager. Segment Comparison module will show up then in the module list:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/531843722f01fe25c1223325097d817a36719630.png" data-download-href="/uploads/short-url/bR5C5gpJSl54E5cUDrrMmst2zVm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/531843722f01fe25c1223325097d817a36719630_2_690x463.png" alt="image" data-base62-sha1="bR5C5gpJSl54E5cUDrrMmst2zVm" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/531843722f01fe25c1223325097d817a36719630_2_690x463.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/531843722f01fe25c1223325097d817a36719630_2_1035x694.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/531843722f01fe25c1223325097d817a36719630_2_1380x926.png 2x" data-dominant-color="393C3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1559×1048 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Alice914 (2024-09-18 09:08 UTC)

<p>Thank you for your teaching. Great. I found extension in the module, but I couldn’t find SlicerRT. 3d slicer in Ubuntu couldn’t normally download. So I downloaded slicrrt in the slicerrt website and SegmentComparison packege of SlicerRT from Github. And then segmentcomparison path added by additional module path of modules in additional settings. After these steps, Windows11 show SegmentComparison in the module. But Ubuntu24.04 doesn’t have.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/034f7a0ee07bc889ed20465225b425c9be4f95ff.jpeg" data-download-href="/uploads/short-url/thI3JcSiQtz9u8tUnMdr6JGoj5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/034f7a0ee07bc889ed20465225b425c9be4f95ff_2_493x500.jpeg" alt="image" data-base62-sha1="thI3JcSiQtz9u8tUnMdr6JGoj5" width="493" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/034f7a0ee07bc889ed20465225b425c9be4f95ff_2_493x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/034f7a0ee07bc889ed20465225b425c9be4f95ff_2_739x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/034f7a0ee07bc889ed20465225b425c9be4f95ff_2_986x1000.jpeg 2x" data-dominant-color="363536"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1945 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/985e784947f863d6e0d02215fffe19431fa8e62b.jpeg" data-download-href="/uploads/short-url/lJUYwLQIAYL7hJl2wdjPL7OMLPl.jpeg?dl=1" title="img_v3_02er_8c3e1e38-45a3-4917-8b73-be7cb1ee162g" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/985e784947f863d6e0d02215fffe19431fa8e62b_2_477x500.jpeg" alt="img_v3_02er_8c3e1e38-45a3-4917-8b73-be7cb1ee162g" data-base62-sha1="lJUYwLQIAYL7hJl2wdjPL7OMLPl" width="477" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/985e784947f863d6e0d02215fffe19431fa8e62b_2_477x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/985e784947f863d6e0d02215fffe19431fa8e62b_2_715x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/985e784947f863d6e0d02215fffe19431fa8e62b_2_954x1000.jpeg 2x" data-dominant-color="37373E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">img_v3_02er_8c3e1e38-45a3-4917-8b73-be7cb1ee162g</span><span class="informations">1920×2012 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/560a3c1b6fdf2f595296ac601fb0190a7a914e68.jpeg" data-download-href="/uploads/short-url/ch8Zp6JWF8epeMT3mSPn3CIW6og.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/560a3c1b6fdf2f595296ac601fb0190a7a914e68_2_482x499.jpeg" alt="image" data-base62-sha1="ch8Zp6JWF8epeMT3mSPn3CIW6og" width="482" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/560a3c1b6fdf2f595296ac601fb0190a7a914e68_2_482x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/560a3c1b6fdf2f595296ac601fb0190a7a914e68_2_723x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/560a3c1b6fdf2f595296ac601fb0190a7a914e68_2_964x998.jpeg 2x" data-dominant-color="31323A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1988 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @cpinter (2024-09-18 10:49 UTC)

<p>Your approach does not work with modules that have any C++ component. You will either need to build Slicer and SlicerRT from source code, or make sure the Extensions Manager can download the extension.</p>
<p>Do you have download problems only for SlicerRT or all the extensions? Are you behind a firewall (such as in hospital environment)? If so, then maybe that’s why. In that case you can download SlicerRT for 5.6.2 Ubuntu here:<br>
<a href="https://slicer.cdash.org/build/3527219/files" class="onebox" target="_blank" rel="noopener">https://slicer.cdash.org/build/3527219/files</a><br>
You can install it using the “Install from file” button in the Extensions manager.</p>

---

## Post #5 by @Alice914 (2024-09-20 09:25 UTC)

<p>I am sorry. May you explain what is C++ component? Now I download SlicerRT from slicerrt website and install it in the Slicer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/777d705da6f4d85dce45b91b62138f52f51647d3.jpeg" data-download-href="/uploads/short-url/h33znzJ8idtz699NqkMdsqg4Fp1.jpeg?dl=1" title="img_v3_02er_144ec033-d9c6-4ab7-81a8-7184af5e52fg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/777d705da6f4d85dce45b91b62138f52f51647d3_2_478x500.jpeg" alt="img_v3_02er_144ec033-d9c6-4ab7-81a8-7184af5e52fg" data-base62-sha1="h33znzJ8idtz699NqkMdsqg4Fp1" width="478" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/777d705da6f4d85dce45b91b62138f52f51647d3_2_478x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/777d705da6f4d85dce45b91b62138f52f51647d3_2_717x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/777d705da6f4d85dce45b91b62138f52f51647d3_2_956x1000.jpeg 2x" data-dominant-color="343434"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">img_v3_02er_144ec033-d9c6-4ab7-81a8-7184af5e52fg</span><span class="informations">1920×2005 217 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
And then I add segmentcomparison package from github in slicerrt.  But I didn’t see segmentcomparison in the module.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5280bfbb0224be3d8ffaadf645313330fe9b85df.jpeg" data-download-href="/uploads/short-url/bLQZKkCf98rLah1ocoDUBA416An.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5280bfbb0224be3d8ffaadf645313330fe9b85df_2_475x500.jpeg" alt="image" data-base62-sha1="bLQZKkCf98rLah1ocoDUBA416An" width="475" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5280bfbb0224be3d8ffaadf645313330fe9b85df_2_475x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5280bfbb0224be3d8ffaadf645313330fe9b85df_2_712x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5280bfbb0224be3d8ffaadf645313330fe9b85df_2_950x1000.jpeg 2x" data-dominant-color="32333B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×2017 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
How can I do? please teach me! Thanks</p>

---

## Post #6 by @lassoan (2024-09-20 16:29 UTC)

<p>Probably your organization interferes with your internet access (they use Zscaler or similar heuristic software that often breaks legitimate web applications).</p>
<p>Fortunately, there are alternative ways of downloading and installing Slicer extensions - see instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#install-extensions-without-network-connection">here</a>.</p>

---

## Post #7 by @cpinter (2024-09-23 08:24 UTC)

<p>I sent an actual download link above. <a class="mention" href="/u/alice914">@Alice914</a> you can use that to download the zip.</p>

---

## Post #8 by @Alice914 (2024-09-23 09:22 UTC)

<p>Thank you a lot. It is internet problem.</p>

---
