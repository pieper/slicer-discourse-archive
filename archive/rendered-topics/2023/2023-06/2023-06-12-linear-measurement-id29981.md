# Linear measurement

**Topic ID**: 29981
**Date**: 2023-06-12
**URL**: https://discourse.slicer.org/t/linear-measurement/29981

---

## Post #1 by @mohammed_alshakhas (2023-06-12 08:53 UTC)

<p>is there a way to measure without placing a line in markup ? if not available I guess it would be a good idea to be able to measure without it</p>
<p>thanks</p>

---

## Post #2 by @muratmaga (2023-06-12 17:51 UTC)

<p>I am not sure I understand what you are requesting. If you don’t want the line showing up, you can turn it off under the display settings. Or alternatively use the pointList object and record two landmarks (and then calculate the distance between them).</p>

---

## Post #3 by @mohammed_alshakhas (2023-06-12 18:45 UTC)

<p>I thought plain measurements like basic viewers might exist. i do too many measurements on images so id rather skip all the extra steps</p>

---

## Post #4 by @jamesobutler (2023-06-12 18:55 UTC)

<p><a class="mention" href="/u/mohammed_alshakhas">@mohammed_alshakhas</a> Can you provide images of the type of plain measurements? Are you talking about scale bars?</p>

---

## Post #5 by @mohammed_alshakhas (2023-06-12 19:01 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/0245d3a28cab9b786467e0586526fa9c7da4a344.jpeg" data-download-href="/uploads/short-url/k6yALYT0ourkXxIHm19EsUsQQY.jpeg?dl=1" title="Screenshot 2023-06-12 at 21.59.04" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/0245d3a28cab9b786467e0586526fa9c7da4a344_2_690x448.jpeg" alt="Screenshot 2023-06-12 at 21.59.04" data-base62-sha1="k6yALYT0ourkXxIHm19EsUsQQY" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/0245d3a28cab9b786467e0586526fa9c7da4a344_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/0245d3a28cab9b786467e0586526fa9c7da4a344_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/0245d3a28cab9b786467e0586526fa9c7da4a344_2_1380x896.jpeg 2x" data-dominant-color="11110D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-06-12 at 21.59.04</span><span class="informations">1920×1247 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>just something direct like that instead of  big points  that  make it hard to know precisely where measurements start and end</p>

---

## Post #6 by @jamesobutler (2023-06-12 19:51 UTC)

<p>There are various glyph types you can try including “Vertex2D” that you may like better. Since everyone has their own preference, you are able to make your choices and then press “Save to defaults” and then those defaults will be used anytime you open Slicer and you won’t have to keep making this customization.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ea5a0d00bdfe7ded481d5b1ce1a6b5cbedb451c.jpeg" data-download-href="/uploads/short-url/fMPnsRBJxGpSSfDzKlyfPPl9LPu.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ea5a0d00bdfe7ded481d5b1ce1a6b5cbedb451c_2_690x372.jpeg" alt="image" data-base62-sha1="fMPnsRBJxGpSSfDzKlyfPPl9LPu" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ea5a0d00bdfe7ded481d5b1ce1a6b5cbedb451c_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ea5a0d00bdfe7ded481d5b1ce1a6b5cbedb451c_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ea5a0d00bdfe7ded481d5b1ce1a6b5cbedb451c_2_1380x744.jpeg 2x" data-dominant-color="83838B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×1036 343 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
