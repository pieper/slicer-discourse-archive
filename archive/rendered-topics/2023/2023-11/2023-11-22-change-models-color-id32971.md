---
topic_id: 32971
title: "Change Models Color"
date: 2023-11-22
url: https://discourse.slicer.org/t/32971
---

# Change models color

**Topic ID**: 32971
**Date**: 2023-11-22
**URL**: https://discourse.slicer.org/t/change-models-color/32971

---

## Post #1 by @Santiago_Cutiller (2023-11-22 21:06 UTC)

<p>Hello! I’m trying to take my first steps in developing extensions for 3D slicer.<br>
I want to make an extension that changes the color of a model:</p>
<pre data-code-wrap="python"><code class="lang-python">model_name = "ModelName"
node_model = getNode(model_name)
node_model.GetDisplayNode().SetColor(1, 0, 0)
</code></pre>
<p>This works fine to change the color but the color is not changed in the 3D view or in the cuts.</p>
<p>Should the scene be updated after changing a parameter?</p>

---

## Post #2 by @lassoan (2023-11-23 21:09 UTC)

<aside class="quote no-group" data-username="Santiago_Cutiller" data-post="1" data-topic="32971">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_cutiller/48/5909_2.png" class="avatar"> Santiago_Cutiller:</div>
<blockquote>
<p>This works fine to change the color but the color is not changed in the 3D view or in the cuts.</p>
</blockquote>
</aside>
<p>Where do you see the color change?</p>
<p>By default, when you load a model a display node is automatically added. Have you added an additional display node for the model?</p>
<p>How many models do you have in the scene? Is it possible that you have loaded the same model multiple times and the one that you are changing is occluded by the others?</p>
<aside class="quote no-group" data-username="Santiago_Cutiller" data-post="1" data-topic="32971">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_cutiller/48/5909_2.png" class="avatar"> Santiago_Cutiller:</div>
<blockquote>
<p>Should the scene be updated after changing a parameter?</p>
</blockquote>
</aside>
<p>The change takes effect immediately. No manual updates are needed after changing properties of the display node.</p>

---

## Post #3 by @Santiago_Cutiller (2023-11-24 03:39 UTC)

<p>Thank you for your response.<br>
I see the color change in the models module but it does not change in the 3D view.</p>
<p>If I manually change the color from the models module, then the changes I make to the color from the Python interactor take effect. It would seem that there is something in the initial color configuration. The model is a VTK file of a tract that is initially loaded with the color I show in the image.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dcf1558a860d26eeca6de349da267d19e77ba17.jpeg" data-download-href="/uploads/short-url/keuZQ9h3W9G7aBzTfJBRyISNfPF.jpeg?dl=1" title="Captura de Pantalla 2023-11-24 a la(s) 00.20.43" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dcf1558a860d26eeca6de349da267d19e77ba17_2_345x216.jpeg" alt="Captura de Pantalla 2023-11-24 a la(s) 00.20.43" data-base62-sha1="keuZQ9h3W9G7aBzTfJBRyISNfPF" width="345" height="216" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dcf1558a860d26eeca6de349da267d19e77ba17_2_345x216.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dcf1558a860d26eeca6de349da267d19e77ba17_2_517x324.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dcf1558a860d26eeca6de349da267d19e77ba17_2_690x432.jpeg 2x" data-dominant-color="D7D8E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de Pantalla 2023-11-24 a la(s) 00.20.43</span><span class="informations">1920×1203 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43d3d95d0094e5269ab85251783dc0f3e2b33aeb.jpeg" data-download-href="/uploads/short-url/9G1SfLRcRvVN5WUMcSSm6hZa8sz.jpeg?dl=1" title="Captura de Pantalla 2023-11-24 a la(s) 00.21.08" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43d3d95d0094e5269ab85251783dc0f3e2b33aeb_2_345x215.jpeg" alt="Captura de Pantalla 2023-11-24 a la(s) 00.21.08" data-base62-sha1="9G1SfLRcRvVN5WUMcSSm6hZa8sz" width="345" height="215" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43d3d95d0094e5269ab85251783dc0f3e2b33aeb_2_345x215.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43d3d95d0094e5269ab85251783dc0f3e2b33aeb_2_517x322.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43d3d95d0094e5269ab85251783dc0f3e2b33aeb_2_690x430.jpeg 2x" data-dominant-color="D1D8E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de Pantalla 2023-11-24 a la(s) 00.21.08</span><span class="informations">1920×1197 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4568cf01405504867ef80ebfd826c43c74204cb3.png" data-download-href="/uploads/short-url/9U1uO01UFvekEQDyQ95Drbb54xZ.png?dl=1" title="Captura de Pantalla 2023-11-24 a la(s) 00.26.24" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4568cf01405504867ef80ebfd826c43c74204cb3_2_345x205.png" alt="Captura de Pantalla 2023-11-24 a la(s) 00.26.24" data-base62-sha1="9U1uO01UFvekEQDyQ95Drbb54xZ" width="345" height="205" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4568cf01405504867ef80ebfd826c43c74204cb3_2_345x205.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4568cf01405504867ef80ebfd826c43c74204cb3_2_517x307.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4568cf01405504867ef80ebfd826c43c74204cb3_2_690x410.png 2x" data-dominant-color="D2D6E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de Pantalla 2023-11-24 a la(s) 00.26.24</span><span class="informations">2454×1462 456 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad67668ec18b4180a860629ff3ee2954d2ea09a2.jpeg" data-download-href="/uploads/short-url/oK08vl61UMCutXAooh3uS4SLIt4.jpeg?dl=1" title="Captura de Pantalla 2023-11-24 a la(s) 00.26.46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad67668ec18b4180a860629ff3ee2954d2ea09a2_2_345x207.jpeg" alt="Captura de Pantalla 2023-11-24 a la(s) 00.26.46" data-base62-sha1="oK08vl61UMCutXAooh3uS4SLIt4" width="345" height="207" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad67668ec18b4180a860629ff3ee2954d2ea09a2_2_345x207.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad67668ec18b4180a860629ff3ee2954d2ea09a2_2_517x310.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad67668ec18b4180a860629ff3ee2954d2ea09a2_2_690x414.jpeg 2x" data-dominant-color="D1D8E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de Pantalla 2023-11-24 a la(s) 00.26.46</span><span class="informations">1920×1154 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b13928a6c565428662da813e34979f2ec8d9f5bd.jpeg" data-download-href="/uploads/short-url/phMYpG8EfC8soZqtKcnAb61QXql.jpeg?dl=1" title="Captura de Pantalla 2023-11-24 a la(s) 00.28.06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b13928a6c565428662da813e34979f2ec8d9f5bd_2_345x214.jpeg" alt="Captura de Pantalla 2023-11-24 a la(s) 00.28.06" data-base62-sha1="phMYpG8EfC8soZqtKcnAb61QXql" width="345" height="214" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b13928a6c565428662da813e34979f2ec8d9f5bd_2_345x214.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b13928a6c565428662da813e34979f2ec8d9f5bd_2_517x321.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b13928a6c565428662da813e34979f2ec8d9f5bd_2_690x428.jpeg 2x" data-dominant-color="D6D0E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de Pantalla 2023-11-24 a la(s) 00.28.06</span><span class="informations">1920×1191 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e44ad3c72728bc35b8375d4bdf4603272ddd200a.png" data-download-href="/uploads/short-url/wzzb9CxAzmkzQHJdCKkdE5KTak2.png?dl=1" title="Captura de Pantalla 2023-11-24 a la(s) 00.28.23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e44ad3c72728bc35b8375d4bdf4603272ddd200a_2_345x213.png" alt="Captura de Pantalla 2023-11-24 a la(s) 00.28.23" data-base62-sha1="wzzb9CxAzmkzQHJdCKkdE5KTak2" width="345" height="213" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e44ad3c72728bc35b8375d4bdf4603272ddd200a_2_345x213.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e44ad3c72728bc35b8375d4bdf4603272ddd200a_2_517x319.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e44ad3c72728bc35b8375d4bdf4603272ddd200a_2_690x426.png 2x" data-dominant-color="D6D0E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de Pantalla 2023-11-24 a la(s) 00.28.23</span><span class="informations">2472×1532 316 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Santiago_Cutiller (2023-11-26 21:52 UTC)

<p>Hello, I think I found the problem. The models are built from .trk files and have the Scalars visibility option active. After the instruction mi_node.GetDisplayNode().SetScalarVisibility(False) I can change the color of the models.</p>

---
