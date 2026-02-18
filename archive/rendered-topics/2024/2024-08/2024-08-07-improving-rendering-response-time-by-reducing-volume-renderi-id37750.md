# Improving Rendering Response Time by Reducing Volume Rendering Quality

**Topic ID**: 37750
**Date**: 2024-08-07
**URL**: https://discourse.slicer.org/t/improving-rendering-response-time-by-reducing-volume-rendering-quality/37750

---

## Post #1 by @park (2024-08-07 10:14 UTC)

<p>Hello,</p>
<p>I am working on volume rendering and displaying multiple meshes simultaneously (Like below figure). The problem is that the rendering response time slows down as the number of models increases.</p>
<p>It seems this is due to volume rendering, as the rendering response time is much faster when the volume visibility is turned off.</p>
<p>The work I am doing does not require high-quality volume rendering (in fact, very low quality is fine), so I want to lower the quality and improve the rendering response time.</p>
<p>I have tried various things in the <code>application settings</code> under <code>volume rendering</code>, but there were only slight changes and no noticeable improvements.</p>
<p>Could you provide some advice on how to lower the quality of volume rendering and increase the speed?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c43c44d300b8dfe9052dd31025ada0f28968ff4f.jpeg" data-download-href="/uploads/short-url/rZYHZKrAbOEmG3h5V2xqt3BKJEH.jpeg?dl=1" title="sss.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c43c44d300b8dfe9052dd31025ada0f28968ff4f.jpeg" alt="sss.PNG" data-base62-sha1="rZYHZKrAbOEmG3h5V2xqt3BKJEH" width="569" height="500" data-dominant-color="CDCCC4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sss.PNG</span><span class="informations">800×702 35.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-08-07 22:33 UTC)

<aside class="quote no-group" data-username="park" data-post="1" data-topic="37750">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/park/48/5717_2.png" class="avatar"> park:</div>
<blockquote>
<p>e <code>application settings</code> under <code>volume rendering</code>, but there were only slight changes and no noticeable improvements.</p>
</blockquote>
</aside>
<p>Did you change the quality to adaptive and increase the fps? Honestly, most of the time volume rendering is so fast those settings have very minimal effect (unless your dataset is huge, which doesn’t appear to be the case). What kind of a computer and graphics card do you have?</p>

---

## Post #3 by @park (2024-08-13 12:28 UTC)

<p>As you can see in the video, when volume rendering is enabled, the FPS drops below 20, whereas when rendering is disabled, it goes up to 28. Could this be because there are too many models, or is it because the volume is large (493x482x452)?</p>
<p>Is there any way to improve this?<br>
(I have already tried using adaptive rendering and increasing FPS)</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5497b0d6f5bc19e0bdc4a0c7a08813519f19308.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14b7c0aab720d6c333468e30bbe101d021da9de3.jpeg">
  </div><p></p>
<p>*My computer has high specifications:<br>
CPU: Intel i7<br>
RAM: 128GB<br>
Graphics: RTX 3090</p>

---
