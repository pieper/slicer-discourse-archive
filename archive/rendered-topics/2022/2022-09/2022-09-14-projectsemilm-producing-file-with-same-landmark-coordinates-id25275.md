---
topic_id: 25275
title: "Projectsemilm Producing File With Same Landmark Coordinates"
date: 2022-09-14
url: https://discourse.slicer.org/t/25275
---

# ProjectSemiLM producing file with same landmark coordinates for 78 surface landmarks

**Topic ID**: 25275
**Date**: 2022-09-14
**URL**: https://discourse.slicer.org/t/projectsemilm-producing-file-with-same-landmark-coordinates-for-78-surface-landmarks/25275

---

## Post #1 by @Corinthia_Black (2022-09-14 18:48 UTC)

<p>I am trying to produce surface landmarks on an extremely variable sclarite (hard bits of spiders/insects); however, when I run ProjectSemiLM, the data that is being generated seems to overwrite each line with the same information, producing a file that has the same landmark coordinates for every landmark. See details below:</p>
<p>There are no homologous landmarks for this object, so I used semilandmarks that follow the dorsal midline of the sclarite as my base landmarks. In PseudoLMGenerator, I project surface landmarks onto sclarite for the most average object (according to PCA of curves). In ProjectSemiLM, I used the most average shape for mesh, semilandmarks from curves as base landmarks, and pseudolandmarks as base semi-landmarks. When I run the program, it does not produce any errors in the python interactor section, but when I open the .fcsv file in a text editor, I can see each line being overwritten (see gif made from a video where each update overwrites the lines).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6d55e8cc3a790296b922205b6ec1fa8f2d91857.gif" alt="021EB536-A44F-40A2-96D9-C38322910E75" data-base62-sha1="q5q2yOoNB4BlYJH1fNhDdVolLtt" width="180" height="320" class="animated"></p>

---

## Post #2 by @muratmaga (2022-09-14 20:24 UTC)

<p>Procedure you describe sounds right. Can you share some of your data so that we cna look into it. SPecificaly we need a pair models, the base lm for the target and reference, and the pseudoLM set for the reference.</p>
<p>By the way, people usually prefer projecting pseudoLM to a surface via TPS deformation (what ProjectSemiLM does), because they use anatomical (fixed) landmarks to anchor the deformation. If you are using semiLMs to do that method should still perform but you may get push back from your reviewers.</p>
<p>We developed the pseudoLM + ALPACA pipeline exactly for situations like this. Did you try that? (you don’t need to have semiLMs for your target models. (see figure 5 in this paper. <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8864294/" class="inline-onebox" rel="noopener nofollow ugc">Computational anatomy and geometric shape analysis enables analysis of complex craniofacial phenotypes in zebrafish - PMC</a>)</p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a></p>

---

## Post #3 by @Corinthia_Black (2022-09-14 20:39 UTC)

<p>A partial dataset is attached as a zip file to this email.</p>
<p>Unfortunately, with these sclerites, there are no homologous landmarks, and when I tried the pseudoLM + ALPACA, the sclerites did not seem to orient to one another correctly. There is so much variation in shape that primarily automated processes have a difficult time with alignment.</p>
<p>I think I need to hold the object in place (anterior → posterior and dorsal → ventral) somehow in order to generate pseudolandmarks for these sclerites.</p>
<p>If you have any ideas, I’m willing to hear them. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>-Cori</p>
<p>(Attachment ExampleData.zip is missing)</p>

---

## Post #4 by @Corinthia_Black (2022-09-14 20:41 UTC)

<p>The zip did not attach, so here is a dropbox file. <a href="https://www.dropbox.com/s/bxxu7fx8wj7f0r0/ExampleData.zip?dl=0" class="inline-onebox" rel="noopener nofollow ugc">Dropbox - ExampleData.zip - Simplify your life</a></p>

---

## Post #5 by @muratmaga (2022-09-14 20:41 UTC)

<aside class="quote no-group" data-username="Corinthia_Black" data-post="3" data-topic="25275">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/corinthia_black/48/16662_2.png" class="avatar"> Corinthia_Black:</div>
<blockquote>
<p>A partial dataset is attached as a zip file to this email.</p>
</blockquote>
</aside>
<p>Forum doesn’t include the attachments in the email. Can you upload on the cloud and share the link here? (or you can email me directly).</p>

---

## Post #6 by @muratmaga (2022-09-14 21:27 UTC)

<aside class="quote no-group" data-username="Corinthia_Black" data-post="4" data-topic="25275" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/corinthia_black/48/16662_2.png" class="avatar"> Corinthia_Black:</div>
<blockquote>
<p>The zip did not attach, so here is a dropbox file. <a href="https://www.dropbox.com/s/bxxu7fx8wj7f0r0/ExampleData.zip?dl=0">Dropbox - ExampleData.zip - Simplify your life</a></p>
</blockquote>
</aside>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> will look into a bit more detailed why you are getting a set of fix coordinates, but I don’t think this TPS based deformation is going to work for you. Mostly because you have sampled your pseudoLMs on the entire sclerite, but those 10 equidistant points that will define the transformation is only the 1/2 of the perimeter of the specimen, and worse they are planar.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/859dd4b9f1f86785f69c6a28db9f97fbf24162e7.png" data-download-href="/uploads/short-url/j41EBelZIYfZqmTcDhv9uR4xws7.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/859dd4b9f1f86785f69c6a28db9f97fbf24162e7_2_690x437.png" alt="image" data-base62-sha1="j41EBelZIYfZqmTcDhv9uR4xws7" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/859dd4b9f1f86785f69c6a28db9f97fbf24162e7_2_690x437.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/859dd4b9f1f86785f69c6a28db9f97fbf24162e7_2_1035x655.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/859dd4b9f1f86785f69c6a28db9f97fbf24162e7.png 2x" data-dominant-color="A6A7A3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1126×714 78.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So while you shouldn’t get a file with fixed LM outputs (and we will see why that’s the case), I don’t think it is going to work as is anyways.</p>
<p>Maybe you can try adding a few LMs in other axis, even if they are approximate they are still much better than having none.</p>

---

## Post #7 by @Corinthia_Black (2022-09-14 21:43 UTC)

<p>Perfect. Thank you so much for the help. I have struggled with this dataset and think your advice will come in handy.</p>
<p>Thanks again!</p>

---

## Post #8 by @smrolfe (2022-09-15 17:57 UTC)

<p>This error is caused by the failure to calculate an inverse TPS transform from this set of source/target points. I will update the module catch/fix this error, but  the results will still not be meaningful. The TPS transform needs to capture more of the shape to estimate the homologous points between the samples, as <a class="mention" href="/u/muratmaga">@muratmaga</a> suggested. If you can add some additional semi-landmarks it would be great to see the results.</p>

---
