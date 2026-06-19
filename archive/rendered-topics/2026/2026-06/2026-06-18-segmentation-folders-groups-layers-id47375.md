---
topic_id: 47375
title: "Segmentation Folders / Groups / Layers"
date: 2026-06-18
url: https://discourse.slicer.org/t/47375
last_bumped: 2026-06-19T00:31:56.314Z
---

# Segmentation Folders / Groups / Layers

**Topic ID**: 47375
**Date**: 2026-06-18
**URL**: https://discourse.slicer.org/t/segmentation-folders-groups-layers/47375

---

## Post #1 by @LindenRB (2026-06-18 04:23 UTC)

<p>Hi,</p>
<p>Apologies in advance if this is obvious but I have tried to search for a solution for this but not found one.</p>
<p>I am doing a lot of full body segmentations from CT imaging, and have been using Total Segmentator to speed up the process (what a fantastic tool!)</p>
<p>However, I was hoping to find a way to group the segmentations into sub-groups. For example; it would be good if I could create sub-folders within my main “Segmentation” for say “Bones” vs “Organs” vs “Muscles”. This would then allow me to quickly show/hide each sub-group. I can create sub-folders inside my segmentation node but I haven’t been able to move individual segmentations into these folders (not sure if that’s a bug or user incompetence lol)</p>
<p>I know I can create other “Segmentation Nodes” and move segmentations over to their respective node, but when separating by different Nodes you lose the ability to do operations like Boolean joins and subtracts for anything in a different node.</p>
<p>I just thought this would be a great way to keep my workspace organised when dealing with ~50+ segmentation masks in a file.</p>
<p>Many thanks in advance for your support!</p>

---

## Post #2 by @lassoan (2026-06-18 05:58 UTC)

<p>If you have hundreds of segments in the segmentation then you can use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segments-table">filter bar</a> to search and show/hide segments in bulk (if you need multi-select then you can click the green arrow button to jump to the Segmentations module). You can filter/search by name, segment status (not started, in progress, flagged, etc.).</p>
<p>If you want to persistently merge segments then you can try the <a href="https://github.com/PerkLab/SlicerOpenAnatomy/blob/master/AtlasEditor/README.md">Atlas Editor</a> module in OpenAnatomy extension.</p>

---

## Post #3 by @cpinter (2026-06-18 13:12 UTC)

<p>Just want to cross-reference this issue, which I think exists since the day we released Segment Editor:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/4402">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/4402" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4402" target="_blank" rel="noopener">Hierarchical organization of segments</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-13" data-time="01:00:50" data-timezone="UTC">01:00AM - 13 Mar 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=4402). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote no-group" data-username="LindenRB" data-post="1" data-topic="47375">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lindenrb/48/76674_2.png" class="avatar"> LindenRB:</div>
<blockquote>
<p>I can create sub-folders inside my segmentation node but I haven’t been able to move individual segmentations into these folders</p>
</blockquote>
</aside>
<p>I am surprised you can actually create folders inside segmentation nodes! The “nodes” under the segmentation node corresponding to the segments are items in a “virtual branch”, meaning that they don’t correspond to actual MRML nodes in Slicer. At the current state I’d consider robust if Slicer wouldn’t allow you to even create/move a folder under a segmentation node.</p>
<p>A hybrid solution could be to allow folders to handle such virtual items, so what you say could be achieved in subject hierarchy (the Data module), while keeping the already really complicated segments table (in segment editor and segmentations) the same. I mean SH is also very complicated, but as I remember we haven’t touched this topic because we didn’t find a good way to add this to the segments table, but if we can have SH support this via the existing folders, maybe it’s a good tradeoff.</p>

---

## Post #4 by @LindenRB (2026-06-19 00:26 UTC)

<p>Thanks Andras, appreciate the response and the two suggestions. I didn’t even know there was a filter bar as it’s hidden by default.</p>
<p>The filter feature works well if I jump into “segmentations” module as you suggested, switch the masks I need, and then just back to “segmentation editor” module. It’s a little bit clunky but definitely workable all things considered!</p>
<p>I thought it was a bit weird that there seems to be multiple options when right clicking in the “segmentation editor” module such as “Show only selected segments” and “Toggle Selected Segments Visibility” which make it sound like I can select multiple but I cannot select multiple in the “segmentation editor” module. I’m guessing this is just shared context menu between these modules. I can see why selecting multiple would cause issues for the segmentation editing tools though…</p>
<p>I think just adding a prefix or suffix to my names, and then multi select and hide/show would probably work for my use case. I might hard code a lookup table of sorts for all the renaming I would typically do.</p>
<p>Thanks again for your support here!</p>

---

## Post #5 by @LindenRB (2026-06-19 00:31 UTC)

<p>Thanks Csaba!</p>
<p>Yes I think the fact I was able to create a sub folder became a red-herring for me, because if I was able to create a sub folder I assumed I must be able to organise my segmentations using said folders lol!</p>
<p>Can understand that the folders would then add an extra layer of complexity to the segmentations and segmentation editor modules for arguably little benefit to most users.</p>
<p>Not trying to propose my own solutions to you guys, but I had a thought of having a “category” field or something added to segmentations would be useful, that you could then filter by. Eg: if all the default bone segmentations are categorised under “Bone” and then you can filter by that. Or categorised by placement in the body such as abdominal vs head etc. It quickly gets complex…</p>

---
