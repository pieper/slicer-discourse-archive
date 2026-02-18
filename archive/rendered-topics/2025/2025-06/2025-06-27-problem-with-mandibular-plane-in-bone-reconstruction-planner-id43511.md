# Problem with mandibular plane in bone reconstruction planner

**Topic ID**: 43511
**Date**: 2025-06-27
**URL**: https://discourse.slicer.org/t/problem-with-mandibular-plane-in-bone-reconstruction-planner/43511

---

## Post #1 by @Marco_Sarcinella (2025-06-27 03:08 UTC)

<p>Hi! I’m new in 3slicer, i had only one case of mandibulectomy in 3 d slicer the past month.<br>
Now I’have a problem when i do te positioning of mandibolar plane. Why when i set mandibular plane in correct position they cut off a piece of contralateral mandible ? So i can’t have a pre plating model to print with all the mandible .<br>
For Example i had to do a recostruction of left ramus. When i set my 3 mandibular plane, the “prolong” the cut also in the right ramus, cutting condile and other pieces.</p>

---

## Post #2 by @mau_igna_06 (2025-06-27 13:22 UTC)

<p>Hi</p>
<p>Please check this:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/issues/164#issuecomment-3012596924">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/issues/164#issuecomment-3012596924" target="_blank" rel="noopener nofollow ugc">github.com/SlicerIGT/SlicerBoneReconstructionPlanner</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/issues/164#issuecomment-3012596924" target="_blank" rel="noopener nofollow ugc">Problem with mandibular cut plane</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-06-26" data-time="23:08:05" data-timezone="UTC">11:08PM - 26 Jun 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/marcosarcinella" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/218164190?v=4" class="onebox-avatar-inline" width="20" height="20">
          marcosarcinella
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Hello ! And thank you for sharing your experience . I have a problem when i out <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">mandibular plane in bone recostruction panel.
When I put them, the cut also a part of controlateral mandible non included in the resection, with the consequence that is impossible to print a model with a contralateral side like the original</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It should solve the problem</p>
<p>Mauro</p>

---

## Post #3 by @Marco_Sarcinella (2025-10-17 09:05 UTC)

<p>Hi mauro ! How are you ?</p>
<p>First thanks for your suggests and your work! Thank you so much.</p>
<p>I would like to ask you another advice.</p>
<p>When designing a surgical guide for the fibula, there is often a tendency to design the guide to fit perfectly to the bone.</p>
<p>This is a big problem because, although you always try to preserve the periosteum on the lateral side of the fibula, there are muscle insertions on the anterior/medial side that make the fibula thicker than the bone portion alone.</p>
<p>How can I generate a surgical guide that is 1-2 millimeters wider?</p>

---

## Post #4 by @Marco_Sarcinella (2025-10-17 09:08 UTC)

<p>Is possible for example to :<br>
A-Hollow the fibula 1-2 millimetres</p>
<p>B-add another segment and hollowing it for the surgical guide , based on precedent hollwing (letter A). And Using this for the fibula surgical guide ?</p>
<p>Thank you !!!</p>

---

## Post #5 by @mau_igna_06 (2025-10-20 18:42 UTC)

<p>After you create the <code>hollow</code> guidebase, you should be able to use <code>margin</code> effect with a negative value to get the result you are looking for</p>

---
