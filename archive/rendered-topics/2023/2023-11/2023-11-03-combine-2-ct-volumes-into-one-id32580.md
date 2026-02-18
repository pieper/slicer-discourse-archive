# Combine 2 ct volumes into one

**Topic ID**: 32580
**Date**: 2023-11-03
**URL**: https://discourse.slicer.org/t/combine-2-ct-volumes-into-one/32580

---

## Post #1 by @mijelsan (2023-11-03 12:02 UTC)

<p>I have 2 ct of same patient of 2 half bodys overlapping, one from head to pelvis and second from pelvis to feet.</p>
<p>I want to combine them into one, i’m going with this workflow:</p>
<p>first i enlarge body section to body_extended volume using crop volume module setting -1000 to the fill value and linear as interpòlator.</p>
<p>Nexti register two images body_extended and legs manually with transform module then with brains general registration ok.</p>
<p>now i have to combine two cts into one, i think a tool that can compare boxel by boxel and select maximun value would do the job but i cant find that tool.</p>
<p>I try to use add scalar volumes module but in the legs section the hu value isnt correct as it shows good value for bones (1000) but bad for muscle (-xxx) i think thats because it is linearly scalinf from body_extended (-1000) to leg values (say 100) and then it outputs something in range -xxx…</p>
<p>please may any help with this issue</p>
<p>thank you,</p>
<p>Miguel</p>

---

## Post #2 by @pieper (2023-11-03 12:05 UTC)

<p>This material should help:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/PerkLab/SlicerSandbox#stitch-volumes">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/d5f48668e76d2d8d9505579416ac573922c4c88738b460c203a8f479ccd34cfa/PerkLab/SlicerSandbox" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes" target="_blank" rel="noopener">GitHub - PerkLab/SlicerSandbox: Collection of utilities that are not polished...</a></h3>

  <p>Collection of utilities that are not polished implementations but can be useful to users - GitHub - PerkLab/SlicerSandbox: Collection of utilities that are not polished implementations but can be u...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote" data-post="1" data-topic="25786">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/young_wang/48/13926_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/multiple-partial-volumes-reconstruction/25786">Multiple partial volumes reconstruction</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi there, I’m trying to synthesize one full volume from multiple partial volumes(smaller FOV) of the same objects. I wonder if anyone else has explored this topic, and happy to hear any thoughts on what would be the best approach to this. 
I appreciate any ideas and advice on things to do or not to do.
  </blockquote>
</aside>


---

## Post #3 by @mijelsan (2023-11-03 17:09 UTC)

<p>Very much thank you for your answer, i’ve managed to get the job done with the tool you posted.  nevertheless i would like to dig into the details and know if this can be done manually with the tools included default</p>

---

## Post #4 by @mijelsan (2023-11-03 19:31 UTC)

<p>after play a little more with the modules i have reproduced what is done by the stitch script:</p>
<ol>
<li>
<p>use module resample image brains, image to warp is the smallest image in my case the legs, and reference image the bigger in my case body_extended. i have to use pixel tipe as short and linear interpolation with default value=-1000</p>
</li>
<li>
<p>go to the simple filters module named “maximunimagefilter” put the two volumes and then you get the combined ct</p>
</li>
</ol>
<p>problem is solved after this thank you!!! any correction or improvement would be apreciated!!</p>

---
