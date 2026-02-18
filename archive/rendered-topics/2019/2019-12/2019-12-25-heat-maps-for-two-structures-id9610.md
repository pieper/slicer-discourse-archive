# Heat maps for two structures

**Topic ID**: 9610
**Date**: 2019-12-25
**URL**: https://discourse.slicer.org/t/heat-maps-for-two-structures/9610

---

## Post #1 by @Jainey (2019-12-25 05:24 UTC)

<p>Is there a module that I can create heat maps for two segmented structures please. I want to assess the proximity of the surfaces</p>
<p>Thanks</p>

---

## Post #2 by @muratmaga (2019-12-25 06:31 UTC)

<p>Would model-to-model distance extension work for your needs?<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ModelToModelDistance" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ModelToModelDistance</a></p>

---

## Post #3 by @Jainey (2019-12-25 06:44 UTC)

<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<p>I want to get proximity of 2 different structures which are in close proximity, and to create an image as shown in the icon of model to model distance<br>
I m non-IT, non engineering  when I do model to model distance I cant get such an image</p>
<p>Thanks</p>

---

## Post #4 by @muratmaga (2019-12-25 18:30 UTC)

<p>I am not entirely sure what you mean by close proximity.</p>
<p>For model to model distance to work, you need to bring your segmentations into an alignment (you can use segment registration module to do that). While they are superimposed, model to model distance can calculate the distance between corresponding vertices of two different models, and display as a heat map on the reference model. It is assumed that you are comparing similar structured (e.g., mandible or skull before and after a surgery or repair) as oppose to total different structures (heart vs lung).</p>

---
