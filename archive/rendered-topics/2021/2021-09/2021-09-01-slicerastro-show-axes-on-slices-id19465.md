---
topic_id: 19465
title: "Slicerastro Show Axes On Slices"
date: 2021-09-01
url: https://discourse.slicer.org/t/19465
---

# SlicerAstro: show axes on slices

**Topic ID**: 19465
**Date**: 2021-09-01
**URL**: https://discourse.slicer.org/t/slicerastro-show-axes-on-slices/19465

---

## Post #1 by @keri (2021-09-01 14:36 UTC)

<p>Hi,</p>
<p>I can see from the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerAstro#Use_Case:_Visualization_of_HI_dataset" rel="noopener nofollow ugc">Astro picture</a> that Slicer Astro is able to show axes on slice views but I can’t understand how…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc9f90266d66d7e3159b01cd1ad3b03c8a65e951.jpeg" data-download-href="/uploads/short-url/tcbgvGwEx2XjlMd4AeC1fRx7bI5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc9f90266d66d7e3159b01cd1ad3b03c8a65e951_2_690x367.jpeg" alt="image" data-base62-sha1="tcbgvGwEx2XjlMd4AeC1fRx7bI5" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc9f90266d66d7e3159b01cd1ad3b03c8a65e951_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc9f90266d66d7e3159b01cd1ad3b03c8a65e951_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc9f90266d66d7e3159b01cd1ad3b03c8a65e951_2_1380x734.jpeg 2x" data-dominant-color="9E9EA3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1600×852 94.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @keri (2021-09-01 15:47 UTC)

<p>By the way <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/AstroVolume#:~:text=color%20transfer%20function-,The%20display%20of%20the%20Astronomical%20World%20Coordinate%20(WCS)%20and%20Data%20Probing%20for%202D%20views,-The%20display%20of" rel="noopener nofollow ugc">according to the documentation</a> axes should appear when one clicks on ruler icon. But it doesn’t work.</p>

---

## Post #3 by @rbumm (2021-09-02 09:07 UTC)

<p>I tried to use the orientation marker “Axes” in Slicer 4.13.0-2021-08-24 and it works:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/175e327e86ba97b6c85c2e7988f202e76bdafc64.jpeg" data-download-href="/uploads/short-url/3kINvmQQedgoh2KGXe14KabRCHq.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/175e327e86ba97b6c85c2e7988f202e76bdafc64_2_690x313.jpeg" alt="image" data-base62-sha1="3kINvmQQedgoh2KGXe14KabRCHq" width="690" height="313" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/175e327e86ba97b6c85c2e7988f202e76bdafc64_2_690x313.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/175e327e86ba97b6c85c2e7988f202e76bdafc64_2_1035x469.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/175e327e86ba97b6c85c2e7988f202e76bdafc64_2_1380x626.jpeg 2x" data-dominant-color="5E5858"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1512×688 69.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @keri (2021-09-02 09:15 UTC)

<p>Hi,</p>
<p>Thank you but I was talking about other axes (<a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/AstroVolume#:~:text=color%20transfer%20function-,The%20display%20of%20the%20Astronomical%20World%20Coordinate%20(WCS)%20and%20Data%20Probing%20for%202D%20views,-The%20display%20of" rel="noopener nofollow ugc">link to the documentation</a>):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5024f641c6c2984b293406d8a48e9e7753c76f7.jpeg" data-download-href="/uploads/short-url/yXrVDETHH2SZ9USk67HJSzD1vin.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f5024f641c6c2984b293406d8a48e9e7753c76f7_2_684x500.jpeg" alt="image" data-base62-sha1="yXrVDETHH2SZ9USk67HJSzD1vin" width="684" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f5024f641c6c2984b293406d8a48e9e7753c76f7_2_684x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f5024f641c6c2984b293406d8a48e9e7753c76f7_2_1026x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5024f641c6c2984b293406d8a48e9e7753c76f7.jpeg 2x" data-dominant-color="5F5C5C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1051×768 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @rbumm (2021-09-02 09:33 UTC)

<p>Ok, I see. I am quite sure that the functions you refer to are parts of the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerAstro" rel="noopener nofollow ugc">SlicerAstro</a> extension. Have you installed that locally?</p>

---

## Post #6 by @keri (2021-09-02 09:39 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="5" data-topic="19465">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Have you installed that locally?</p>
</blockquote>
</aside>
<p>I installed the recent version of SLicer 3d Preview Release 4.13 few lays ago and installed Astro extension by clicking on <code>Install</code> in extension manager (it automatically downloads it and unpack).</p>
<p>Also I have tried to build Astro and use it in custom Slicer but axes still doesn’t work (even the extension works).</p>
<p>Did you try to display axes?</p>
<p>I forgot to tell that I use Ubuntu 20.04</p>

---

## Post #7 by @rbumm (2021-09-02 09:54 UTC)

<p>Unfortunately, I can not install SlicerAstro from my extensions manager and can not help you. I am on windows.</p>

---

## Post #8 by @lassoan (2021-09-02 19:46 UTC)

<p>Probably those axes are displayed by vtkMRMLAstroTwoDAxesDisplayableManager and might require position-velocimetry images. You should be able to clone and adapt it to display the kind of axes that you would like to have.</p>

---

## Post #9 by @keri (2021-09-02 19:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="19465">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Probably those axes are displayed by vtkMRMLAstroTwoDAxesDisplayableManager and might require position-velocimetry images</p>
</blockquote>
</aside>
<p>Thank you for reply.</p>
<p>You mean that I need to try to download some special data and display it?</p>
<p>I looked pretty carefully to the Slicer Astro volume source code and <code>vtkMRMLAstroTwoDAxesDisplayableManager</code> class but still cant understand how this manager is connected with button click in threD/slice control widget (button that is shown on the picture above “ruler icon”). Usually we do this with Qt’s <code>connect()</code> but it seems that in Astro it works somehow differently.</p>

---

## Post #10 by @lassoan (2021-09-02 23:37 UTC)

<p>Yes, it might require special volume nodes. But you can get definitive answer by reviewing the code and running it under a debugger.</p>
<p><a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> do you have any advice?</p>

---

## Post #11 by @iwangwangwang (2023-09-14 08:21 UTC)

<p>these axes only be displayed in Astro Slicer?   How to display it  in 3D Slicer?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be307b2430c8d4edac3ac8fa0953eb64b5ede4dd.jpeg" alt="" data-base62-sha1="r8uAy0Rb8VzrjtojD81pUnn3NcV" role="presentation" width="684" height="500"></p>

---

## Post #12 by @keri (2023-09-15 06:11 UTC)

<p>Hi <a class="mention" href="/u/iwangwangwang">@iwangwangwang</a>,</p>
<p>As far as I know original Slicer 3D doesn’t have such axes.<br>
They are implemented in SlicerAstro as Diplayable Manger.</p>
<p>Also I have reworked it and use it my custom app.<br>
If you know how to compile the module you can follow <a href="https://github.com/tierra-colada/Colada/tree/master/Modules/Loadable/Axes" rel="noopener nofollow ugc">this link</a>, download the module and compile it.<br>
Then add this directory to modules and you should see axes on 2D (like in SlicerAstro) and also there should be module named <code>Axes</code> which allows to use 3D axes on selected node.</p>

---

## Post #13 by @iwangwangwang (2023-09-15 09:17 UTC)

<p>Thank you so much, but the link seems invalid</p>

---

## Post #14 by @keri (2023-09-15 09:27 UTC)

<p>Oh Im sorry… I forgot this is closed source repository</p>

---
