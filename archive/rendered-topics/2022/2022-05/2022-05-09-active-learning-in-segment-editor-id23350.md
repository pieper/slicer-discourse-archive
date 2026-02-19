---
topic_id: 23350
title: "Active Learning In Segment Editor"
date: 2022-05-09
url: https://discourse.slicer.org/t/23350
---

# Active Learning in segment editor

**Topic ID**: 23350
**Date**: 2022-05-09
**URL**: https://discourse.slicer.org/t/active-learning-in-segment-editor/23350

---

## Post #1 by @TaraGh (2022-05-09 20:22 UTC)

<p>Hello,</p>
<p>I have a question about the “segment editor”. I have a large dataset that I have to label and it is taking a lot of time to be done, so I am looking for something like an active learning concept in this tool or similar modules that ease this annotation.<br>
I appreciate any help with this issue.</p>
<p>Many Thanks.</p>

---

## Post #2 by @mangotee (2022-05-09 20:30 UTC)

<p>Hi there,<br>
indeed there is a tool for that, please check out MONAI-Label:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Project-MONAI/MONAILabel">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Project-MONAI/MONAILabel" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/e40825da3964a81316a60b91c9e34cabf1a2e3869f358836950edbd2bd6a2c28/Project-MONAI/MONAILabel" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Project-MONAI/MONAILabel" target="_blank" rel="noopener nofollow ugc">GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source...</a></h3>

  <p>MONAI Label is an intelligent open source image labeling and learning tool. - GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source image labeling and learning tool.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
There is a 3D Slicer extension for that already which nicely interacts with the Slicer’s segment editor:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer" target="_blank" rel="noopener nofollow ugc">MONAILabel/plugins/slicer at main · Project-MONAI/MONAILabel</a></h3>

  <p><a href="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer" target="_blank" rel="noopener nofollow ugc">main/plugins/slicer</a></p>

  <p><span class="label1">MONAI Label is an intelligent open source image labeling and learning tool.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
For an introduction to the concepts, you can watch this tutorial on Youtube:<br>
            <iframe src="https://www.youtube.com/embed/o8HipCgSZIw?feature=oembed&amp;wmode=opaque&amp;list=PLtoSVSQ2XzyCobzE6NvwjNpITsQyPUtfs" width="480" height="360" frameborder="0" allowfullscreen="" seamless="seamless" sandbox="allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-presentation"></iframe>
<br>
Please note that the latest version introduced some slight changes compared to that video, but the underlying ideas are the same. The “Getting started” guide in the first link gives up-to-date instructions for usage.<br>
Hope it works smoothly for you, if not, you can post your problems here.</p>

---
