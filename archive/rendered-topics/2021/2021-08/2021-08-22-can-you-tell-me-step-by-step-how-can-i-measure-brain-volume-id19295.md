# can you tell me step by step how can i measure brain volume in slicer 4.11 from structural mri 

**Topic ID**: 19295
**Date**: 2021-08-22
**URL**: https://discourse.slicer.org/t/can-you-tell-me-step-by-step-how-can-i-measure-brain-volume-in-slicer-4-11-from-structural-mri/19295

---

## Post #1 by @aalaa12341 (2021-08-22 04:21 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @Mehran (2021-08-24 07:12 UTC)

<p>In order to measure the volume of any part of body, you can label that part and then go to:<br>
“Welcome to Slicer” → Quantification → Label Statistics<br>
then, set the original image and the label that you provided. Next,  you can see the volume of each label in voxel size,…<br>
In order to label a brain, several tools have been provided in “segmentation” as well as other modules  in “Extension managers”.  See also,<br>
<a href="https://www.youtube.com/results?search_query=slicerbs" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.youtube.com/results?search_query=slicerbs</a></p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Mehrancd/TsallisBrainSegmentation">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Mehrancd/TsallisBrainSegmentation" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <img src="https://opengraph.githubassets.com/54c688611e502043980a43345bdc7f9f35a835ba76405a457b39e48f02799092/Mehrancd/TsallisBrainSegmentation" class="thumbnail" width="" height="">

<h3><a href="https://github.com/Mehrancd/TsallisBrainSegmentation" target="_blank" rel="noopener nofollow ugc">GitHub - Mehrancd/TsallisBrainSegmentation: A Slicer module for brain...</a></h3>

  <p>A Slicer module for brain extraction and segmentation - GitHub - Mehrancd/TsallisBrainSegmentation: A Slicer module for brain extraction and segmentation</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2021-08-25 02:35 UTC)

<p><a class="mention" href="/u/mehran">@Mehran</a> thanks for the pointer, this brain segmentation module looks nice. Have you submitted to the extension index? I don’t see it in the extension manager in the latest Slicer Preview Release.</p>
<p><a class="mention" href="/u/aalaa12341">@aalaa12341</a> If you only need to measure the brain volume then you can use the extension that <a class="mention" href="/u/mehran">@Mehran</a> recommended above, or the SwissSkullStripper, or ROBexBrainExtraction extensions. If you are interested in volume of different parts of the brain and you have a GPU then you can use the <a href="https://github.com/fepegar/SlicerParcellation">SlicerParcellation extension</a>, which automatically extracts 160 subcortical structures in the brain.</p>

---

## Post #4 by @Mehran (2021-08-26 06:17 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks. I was working on some issues to improve the performance of the module. Please let me know how can I submit it to the extension index(simplest way <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"> )</p>

---

## Post #5 by @lassoan (2021-08-27 02:19 UTC)

<aside class="quote no-group" data-username="Mehran" data-post="4" data-topic="19295">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mehran/48/11080_2.png" class="avatar"> Mehran:</div>
<blockquote>
<p>Please let me know how can I submit it to the extension index(simplest way <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> )</p>
</blockquote>
</aside>
<p>See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html">this page</a> for details.</p>

---

## Post #6 by @Mehran (2021-08-27 07:33 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I had a look at the link. There are several other links may not work or out of date. It is widely confusing to follow an instruction to create an extension index. For example, there no information about <code>s4ext</code>. After searching a lot you will see this file should be created automatically while it is not true. Some people suggested to do it manually while the others suggested to create using other ways. I am not complaining about it, but at least a reference should be enough to follow. Always refer people to other links is not efficient at all. Sorry, I gave up to make it.</p>

---

## Post #7 by @lassoan (2021-09-02 06:13 UTC)

<p>I’ve reviewed all the extension development documentation. The information was quite up-to-date, but there were indeed a few things that were not clear or relevant anymore. I’ve moved the entire developer documentation for extensions to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html">this readthedocs page</a>.</p>
<aside class="quote no-group" data-username="Mehran" data-post="6" data-topic="19295">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mehran/48/11080_2.png" class="avatar"> Mehran:</div>
<blockquote>
<p>For example, there no information about <code>s4ext</code> .</p>
</blockquote>
</aside>
<p>Full specification of the extension description was already available on the wiki, but you can now find it <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#extension-description-file">here</a>.</p>
<aside class="quote no-group" data-username="Mehran" data-post="6" data-topic="19295">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mehran/48/11080_2.png" class="avatar"> Mehran:</div>
<blockquote>
<p>After searching a lot you will see this file should be created automatically while it is not true.</p>
</blockquote>
</aside>
<p>It is still true. The s4ext file is generated automatically if you build your extension. However, building the extension requires you to build Slicer first, which is not easy to do when you do it the first time. If you don’t need to build Slicer (e.g., because you only have Python scripted modules in the extension) then you are probably better off creating that very simple 15-line text file in a text editor.</p>

---

## Post #8 by @Mehran (2021-09-02 14:49 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> for update.</p>

---
