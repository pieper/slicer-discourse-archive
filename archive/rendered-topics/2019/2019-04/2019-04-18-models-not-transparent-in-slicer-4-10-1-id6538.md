---
topic_id: 6538
title: "Models Not Transparent In Slicer 4 10 1"
date: 2019-04-18
url: https://discourse.slicer.org/t/6538
---

# Models not Transparent in Slicer 4.10.1

**Topic ID**: 6538
**Date**: 2019-04-18
**URL**: https://discourse.slicer.org/t/models-not-transparent-in-slicer-4-10-1/6538

---

## Post #1 by @Nicole_Seider (2019-04-18 22:20 UTC)

<p>Dear all,</p>
<p>We are currently working with Slicer 4.4.0 and Slicer 4.10.1.  In Slicer 4.4, we can make models transparent using the opacity button: in the image below, the gray ‘leftpial’ surface is at .5 opacity, the green ‘rightpial’ surface is at 1.  If we try to use the Models module in Slicer 4.10.1, the surfaces are always opaque.  If we set the opacity at 0.9, the model will disappear. Any suggestions? We can work for now in 4.4 for the visualizations, but it’d be nice to have this working in 4.10.1.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2fd49456769d9ab077ef14e8cf41719c3c9c3ac.jpeg" data-download-href="/uploads/short-url/pxpEtX50LBlB3BXikypxkQIwJKk.jpeg?dl=1" title="SlicerTransparent" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2fd49456769d9ab077ef14e8cf41719c3c9c3ac_2_690x372.jpeg" alt="SlicerTransparent" data-base62-sha1="pxpEtX50LBlB3BXikypxkQIwJKk" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2fd49456769d9ab077ef14e8cf41719c3c9c3ac_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2fd49456769d9ab077ef14e8cf41719c3c9c3ac_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2fd49456769d9ab077ef14e8cf41719c3c9c3ac_2_1380x744.jpeg 2x" data-dominant-color="A8ACCB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerTransparent</span><span class="informations">2266×1222 470 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jamesobutler (2019-04-18 23:15 UTC)

<p>I tried loading a model in Slicer 4.10.1 and was able to change the opacity without any issue. I should clarify this was on Windows while I see you are using the Linux version.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46fba81a55b321f3cded6617ec0e9b3b5799c89f.png" data-download-href="/uploads/short-url/a7WASuAgGLejQgl8EfIOQ8K08Q7.png?dl=1" title="models-opacity" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46fba81a55b321f3cded6617ec0e9b3b5799c89f_2_690x373.png" alt="models-opacity" data-base62-sha1="a7WASuAgGLejQgl8EfIOQ8K08Q7" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46fba81a55b321f3cded6617ec0e9b3b5799c89f_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46fba81a55b321f3cded6617ec0e9b3b5799c89f_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46fba81a55b321f3cded6617ec0e9b3b5799c89f_2_1380x746.png 2x" data-dominant-color="B5B8DC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">models-opacity</span><span class="informations">1920×1040 80.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @cpinter (2019-04-18 23:40 UTC)

<p>Try the latest nightly. The Models module was largely reimplemented since 4.10.1, so maybe that helps. If not, then it’s your data, and we’ll need it to fix the issue.<br>
Let us know either way. Thanks!</p>

---

## Post #4 by @lassoan (2019-04-18 23:51 UTC)

<p>To correctly display semitransparent surfaces you need to enable depth peeling - see <a href="https://discourse.slicer.org/t/mixed-volume-rendering-and-surface-representation-of-segmentation-has-incorrect-3d-appearance-if-segment-is-not-fully-opaque/6532/2?u=lassoan" class="inline-onebox">Mixed volume rendering and surface representation of segmentation has incorrect 3D appearance if segment is not fully opaque</a></p>

---

## Post #5 by @muratmaga (2019-04-19 03:33 UTC)

<p>Depth peeling is a fairly buried setting for new users. Is there a reason or downside why it is not being enabled by default?</p>

---

## Post #7 by @cpinter (2019-04-19 16:46 UTC)

<p>Depth peeling should not be needed to avoid the bug <a class="mention" href="/u/nicole_seider">@Nicole_Seider</a> is reporting.</p>
<p>I just created some models and verified that opacity works fine with depth peeling off. There is another reason for her dataset to behave like this in her environment (GPU, driver, Slicer version, etc.)</p>

---

## Post #8 by @lassoan (2019-04-19 17:55 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="7" data-topic="6538">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>opacity works fine with depth peeling off</p>
</blockquote>
</aside>
<p>Yes, models should look transparent regardless of depth peeling enabled or not. Semi-transparent just not appear with correct opacity if depth peeling is disabled.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="6538" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Depth peeling is a fairly buried setting for new users. Is there a reason or downside why it is not being enabled by default?</p>
</blockquote>
</aside>
<p>Depth peeling makes rendering slower and had some problems in the past. With current graphics hardware and VTK’s current rendering backend, these issues are mostly resolved, so I think we could enable depth peeling by default. What do you think <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/fedorov">@fedorov</a>?</p>

---

## Post #9 by @cpinter (2019-04-19 19:12 UTC)

<aside class="quote no-group" data-username="Nicole_Seider" data-post="1" data-topic="6538">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nicole_seider/48/3489_2.png" class="avatar"> Nicole_Seider:</div>
<blockquote>
<p>If we set the opacity at 0.9, the model will disappear.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> This should not happen with or without depth peeling. The reported issue I think is independent of the current discussion about depth peeling default setting.</p>
<p>About that discussion: Although rendering without depth peeling is still 50% faster than with depth peeling (based on a very quick test), I think it could be enabled by default.</p>

---

## Post #10 by @pieper (2019-04-19 20:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="6538">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>so I think we could enable depth peeling by default.</p>
</blockquote>
</aside>
<p>I agree - there should be no penalty unless there are translucent surfaces, and it helps resolve what can be a very confusing situation.</p>

---

## Post #11 by @Nicole_Seider (2019-04-22 15:48 UTC)

<p>Thanks everyone for the suggestions.  We downloaded and testing the latest nightly version of slicer (rev 21852 for Linux), found and enable depth peeling (it would be nice it this wasn’t buried), but it had no effect on 4.10 or 4.11 (4.4 on Linux still works properly).</p>
<p>To make things interesting, we can load and visualize the model properly with different opacities (and without turning on depth peeling) on a local Mac machine.  <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/748e1e189de0658ccf2bf3cbcd70b18591adcc0e.png" data-download-href="/uploads/short-url/gD5S49aBgmBRjkEn14EDMBD1m1M.png?dl=1" title="10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/748e1e189de0658ccf2bf3cbcd70b18591adcc0e_2_690x444.png" alt="10" data-base62-sha1="gD5S49aBgmBRjkEn14EDMBD1m1M" width="690" height="444" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/748e1e189de0658ccf2bf3cbcd70b18591adcc0e_2_690x444.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/748e1e189de0658ccf2bf3cbcd70b18591adcc0e_2_1035x666.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/748e1e189de0658ccf2bf3cbcd70b18591adcc0e_2_1380x888.png 2x" data-dominant-color="9D9EBB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">10</span><span class="informations">1768×1138 325 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Since it seems the issue might be related to my data and to the Linux version of Slicer, how do I share the necessary files for further troubleshooting?</p>

---

## Post #12 by @jamesobutler (2019-04-22 18:11 UTC)

<p>You can post a Dropbox/onedrive/google drive link here that shares your data set.</p>
<p>You can also post the Slicer log file. So load your model and then under I believe the “Help” file menu you can go to “Report a bug” which shows the current and recent log files. You can then post this text document which should also include information about your Linux machine at the very top.</p>
<p>Hopefully we can narrow down between data set and the Linux version of Slicer!</p>

---

## Post #13 by @Nicole_Seider (2019-04-22 18:33 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="12" data-topic="6538">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>You can post a Dropbox/onedrive/google drive link here that shares your data set.</p>
</blockquote>
</aside>
<p>I’ve uploaded the model file and Linux log files here: <a href="https://drive.google.com/drive/folders/1_jSZrO4WelVRH8uAqa7OhjV5AVNFaVom?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1_jSZrO4WelVRH8uAqa7OhjV5AVNFaVom?usp=sharing</a></p>
<p>If you have any trouble accessing the files, please let me know.  Thanks again to everyone for all the help so far!</p>

---

## Post #14 by @lassoan (2019-04-22 19:16 UTC)

<p>What graphics card do you have? Are your drivers up-to-date? Slicer-4.4 uses 15-year-old OpenGL API, while Slicer-4.10 uses 6-8-year-old APIs, so very old GPU drivers may be a problem for Slicer versions released in the last few years.</p>
<p>How is the rendering if you convert it to a segmentation node? To create a segmentation from the model node, go to Data module, right-click the model, and select “Convert model to segmentation node”; you can then delete the model node and adjust opacity of the segmentation node in Segmentations module).</p>
<p>How is rendering if you use <a href="https://www.paraview.org/download/" rel="nofollow noopener">ParaView 5.6</a>?</p>
<p>The attached log file did not contain any errors. Transparent visualization of the model that you’ve uploaded worked fine for me on Windows, using Slicer-4.10.1.</p>

---

## Post #15 by @lassoan (2019-04-23 17:23 UTC)

<aside class="quote no-group" data-username="pieper" data-post="10" data-topic="6538">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I agree - there should be no penalty unless there are translucent surfaces, and it helps resolve what can be a very confusing situation.</p>
</blockquote>
</aside>
<p>I’ve updated Slicer nightly version to <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28161">enable depth peeling by default</a>. It only has effect if Slicer.ini does not exist (Slicer has not been installed before or the .ini file is deleted).</p>

---

## Post #16 by @Nicole_Seider (2019-04-23 19:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="6538">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What graphics card do you have? Are your drivers up-to-date?</p>
</blockquote>
</aside>
<p>Our IT replies the following: 04:03.0 VGA compatible controller [0300]: Matrox Electronics Systems Ltd. MGA G200eW WPCM450 [102b:0532] (rev 0a)<br>
The drivers haven’t been updated in years, but since it’s an older model IT thinks it is on the latest update for that driver.</p>
<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="6538">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How is rendering if you use <a href="https://www.paraview.org/download/" rel="noopener nofollow ugc">ParaView 5.6</a>?</p>
</blockquote>
</aside>
<p>IT just installed ParaView5.6 for me, so I’ll test that and report back.</p>

---

## Post #17 by @lassoan (2019-04-24 23:52 UTC)

<p>That computer is about 10 years old, which is too old to run recent versions of Slicer (due to incompatibility of the graphics chipset/driver). Current Slicer versions require computers that are not older than about 5 years.</p>

---

## Post #18 by @Nicole_Seider (2019-08-28 21:15 UTC)

<p>After several months, we finally got a new Linux machine with a newer graphics card, specifically NVIDIA Corporation GM206 [GeForce GTX 960].  I can confirm that the visualization works appropriately now.  Thanks to everyone for the assistance and suggestions!</p>

---
