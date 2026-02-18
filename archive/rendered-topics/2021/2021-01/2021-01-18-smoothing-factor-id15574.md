# Smoothing factor?

**Topic ID**: 15574
**Date**: 2021-01-18
**URL**: https://discourse.slicer.org/t/smoothing-factor/15574

---

## Post #1 by @slicer365 (2021-01-18 01:03 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1a13b6f113528d6e84138c4e9c887816de481cc.jpeg" data-download-href="/uploads/short-url/wc0RT57gWGrfCQ1Ug981IvZGTs8.jpeg?dl=1" title="科研部图章" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1a13b6f113528d6e84138c4e9c887816de481cc_2_690x484.jpeg" alt="科研部图章" data-base62-sha1="wc0RT57gWGrfCQ1Ug981IvZGTs8" width="690" height="484" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1a13b6f113528d6e84138c4e9c887816de481cc_2_690x484.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1a13b6f113528d6e84138c4e9c887816de481cc.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1a13b6f113528d6e84138c4e9c887816de481cc.jpeg 2x" data-dominant-color="CFD9D4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">科研部图章</span><span class="informations">1014×712 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
This tool can smooth the surface of the model, but I want to know if it changes the shape of the original model, such as the accuracy of the original model. This smoothing effect can indeed export the model, not just the display effect. Sometimes In order to smooth the model, I need to use Blender. I don’t know if this function is implemented in the same principle as Blender.</p>

---

## Post #2 by @muratmaga (2021-01-18 01:13 UTC)

<p>To alleviate your concerns, you can turn off the smoothing during segmentation, export the final segmentation (without smoothing again) as 3D model and then use the <code>Surface Toolbox</code> to smooth the model in various amounts. Then you can use the <code>Model 2 Model Distance</code> extension to visualize and quantify the difference between your original (not smoothened model) and your smoothened ones. The difference should be very very subtle.</p>

---

## Post #3 by @lassoan (2021-01-18 02:58 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="1" data-topic="15574">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>Sometimes In order to smooth the model, I need to use Blender. I don’t know if this function is implemented in the same principle as Blender</p>
</blockquote>
</aside>
<p>Many of the algorithms are based on the same principles but they are all different implementations. Blender is optimized for creating visually pleasing renderings, while Slicer is optimized for accurate data visualization and quantification. Therefore, in general you can expect that the two software provides slightly different results. If you create a mesh from an image and then process it in a mesh editor (Blender, MeshMixer, MeshLab, etc.), I would recommend to load back the results into Slicer to quickly verify that the edited mesh still accurately represents the source image.</p>

---

## Post #4 by @slicer365 (2021-01-18 07:14 UTC)

<p>Professors always give me a great idea, thank you very much with my poor English ! <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=9" title=":smile:" class="emoji" alt=":smile:"></p>

---

## Post #5 by @slicer365 (2021-01-18 07:15 UTC)

<p>Thank you very much with my poor English ! <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=9" title=":smile:" class="emoji" alt=":smile:"></p>

---
