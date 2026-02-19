---
topic_id: 33431
title: "How To Reuse Segmentation Label Setting"
date: 2023-12-18
url: https://discourse.slicer.org/t/33431
---

# How to reuse segmentation label setting?

**Topic ID**: 33431
**Date**: 2023-12-18
**URL**: https://discourse.slicer.org/t/how-to-reuse-segmentation-label-setting/33431

---

## Post #1 by @XianDong_Zhang (2023-12-18 01:42 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>
<p>My segmentation contains about 50 labels, I want to reuse it for new segmentation of other case, but I can not figure out how to do it.</p>
<p>This is similar to <a href="https://discourse.slicer.org/t/how-to-predefine-sets-of-segmentation-labels/7724">this question</a> .</p>
<p>I’ve tried to create a blank segmentation template scene, but I can not add any segmentation label without specify volume.</p>
<p>I’ve also tried load an existing segmengation, clone the segmentation data, and specify it to a new volume, but it looks like the cloned data is still bound to the old source volume, the intensity range is totally wrong.</p>

---

## Post #2 by @muratmaga (2023-12-18 02:31 UTC)

<p>Proper way of doing this is using a <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/terminologies.html">custom terminology</a> with your segment names and colors predetermined. You can then, double click their colors and choose the appropriate name from the terminology list.</p>
<p>If your terms are not covered by existing terminologies bundled with Slicer, you can use this simple python script to generate a JSON file that’s is readable by the <code>Terminology</code> module and you can add it as your custom terminology, by hitting the little + sign on the top right.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Imageomics/slicerMorph_JSON_generator">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Imageomics/slicerMorph_JSON_generator" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/56534a4ffc769264af16a0bed12c1b01f825f842118817539e6935f748ccc9bb/Imageomics/slicerMorph_JSON_generator" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Imageomics/slicerMorph_JSON_generator" target="_blank" rel="noopener">GitHub - Imageomics/slicerMorph_JSON_generator: Tool to generate a JSON for...</a></h3>

  <p>Tool to generate a JSON for use with SlicerMorph from a CSV of a particular format. - GitHub - Imageomics/slicerMorph_JSON_generator: Tool to generate a JSON for use with SlicerMorph from a CSV of ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/518388b6a7018cbfe8a0eb35601213bef35c6a69.png" data-download-href="/uploads/short-url/bD6u6bJlKstmWXpDbZyE4FzRMGl.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/518388b6a7018cbfe8a0eb35601213bef35c6a69_2_690x105.png" alt="image" data-base62-sha1="bD6u6bJlKstmWXpDbZyE4FzRMGl" width="690" height="105" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/518388b6a7018cbfe8a0eb35601213bef35c6a69_2_690x105.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/518388b6a7018cbfe8a0eb35601213bef35c6a69_2_1035x157.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/518388b6a7018cbfe8a0eb35601213bef35c6a69.png 2x" data-dominant-color="E3E3E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1102×168 18.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
