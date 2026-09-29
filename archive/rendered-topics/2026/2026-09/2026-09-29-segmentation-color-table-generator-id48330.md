---
topic_id: 48330
title: "Segmentation color table generator"
date: 2026-09-29
url: https://discourse.slicer.org/t/48330
last_bumped: 2026-09-29T02:33:47.334Z
---

# Segmentation color table generator

**Topic ID**: 48330
**Date**: 2026-09-29
**URL**: https://discourse.slicer.org/t/segmentation-color-table-generator/48330

---

## Post #1 by @muratmaga (2026-09-29 02:33 UTC)

<p>This is mostly for people who are using Slicer to segment non-human imaging data.</p>
<p>If you want to use ontology mapped terms for your segmentations, I put together a small web-based tool that generates the table. <a href="https://morphodepot.github.io/term-lookup/" class="inline-onebox" rel="noopener nofollow ugc">Term Lookup Prototype</a></p>
<p>First choose the species (to decide what the best ontology to use), and then list the anatomical terms you would like to include.</p>
<p>When the terms are matched exactly, it shows matched. Dropdown still lists other possible choices. If you included a generic term like ventricle, you can have it replace by the proper ontology term by checking the **use ontology terms as the label** option (this is reversable). If the tool is not confident for the match, it displays either Review Suggestions or flat out No Match. In that case generic Tissue term is used.</p>
<p>Colors come from the order in the Labels color table. But can be edited.</p>
<p>This will be built into the MorphoDepot extension, but you can always use the standalone web version if you don’t want to.</p>
<p>Suggestions are welcomed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a15d038cda705bc115e8d381520df5f61ba0bdd4.png" data-download-href="/uploads/short-url/n1u9y6X18tFvKh4sjvknEuvjzBW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a15d038cda705bc115e8d381520df5f61ba0bdd4_2_317x500.png" alt="image" data-base62-sha1="n1u9y6X18tFvKh4sjvknEuvjzBW" width="317" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a15d038cda705bc115e8d381520df5f61ba0bdd4_2_317x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a15d038cda705bc115e8d381520df5f61ba0bdd4_2_475x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a15d038cda705bc115e8d381520df5f61ba0bdd4_2_634x1000.png 2x" data-dominant-color="F5F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1090×1718 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
