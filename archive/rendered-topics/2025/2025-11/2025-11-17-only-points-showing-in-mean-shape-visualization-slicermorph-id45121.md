---
topic_id: 45121
title: "Only Points Showing In Mean Shape Visualization Slicermorph"
date: 2025-11-17
url: https://discourse.slicer.org/t/45121
---

# Only points showing in Mean Shape Visualization - Slicermorph

**Topic ID**: 45121
**Date**: 2025-11-17
**URL**: https://discourse.slicer.org/t/only-points-showing-in-mean-shape-visualization-slicermorph/45121

---

## Post #1 by @emmm_m (2025-11-17 15:35 UTC)

<p>I’m new to slicer so I apologize if this is a question driven by my ineptness. I am working on generating GPA/PCA visualizations, however when I try to generate a Mean shape visualization for the proximal and distal end of a bone (I have run into this problem running full bone analyses as well) the points will show up but the underlying model will not. I have tried running it multiple times, restarting Slicer, and updating to the latest version and reinstalling SlicerMorph. Is there something I can do to in order to get this to show up? Thanks!</p>

---

## Post #2 by @muratmaga (2025-11-17 16:01 UTC)

<aside class="quote no-group" data-username="emmm_m" data-post="1" data-topic="45121">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/emmm_m/48/81436_2.png" class="avatar"> emmm_m:</div>
<blockquote>
<p>the points will show up but the underlying model will not. I</p>
</blockquote>
</aside>
<p>Because there is no underlying model. GPA is an analysis that operates on the coordinates (landmarks) collected, not the models. You might want to read a review article about geometric morphometrics and how it is implemented.</p>
<p>However, you can still approximate this visualization by using a proxy. You need to select a sample, and their corresponding set of landmarks. See the tutorial: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/GPA_2" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/GPA_2 at main · SlicerMorph/Tutorials · GitHub</a></p>

---

## Post #3 by @emmm_m (2025-11-17 16:12 UTC)

<p>I’ve done this in the mean shape vis. section , picking a proxy sample from the dataset to upload, so it has all the correct points. I am thinking it may be an issue with the python code it is running or selecting the landmarks. In 3D model vis. it says I cannot use it due to the points not corresponding to the selected ones in the analysis. Is this because I am excluding points included in the proxy? Could I fix this by re-landmarking the scan used in the visualization?</p>

---

## Post #4 by @muratmaga (2025-11-17 16:21 UTC)

<aside class="quote no-group" data-username="emmm_m" data-post="3" data-topic="45121">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/emmm_m/48/81436_2.png" class="avatar"> emmm_m:</div>
<blockquote>
<p>. it says I cannot use it due to the points not corresponding to the selected ones in the analysis</p>
</blockquote>
</aside>
<p>Error is very clear. You do not have the exact same number of landmarks you used in your proxy and and the GPA analysis. They need to match (and be in exactly the same order).</p>
<aside class="quote no-group" data-username="emmm_m" data-post="3" data-topic="45121">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/emmm_m/48/81436_2.png" class="avatar"> emmm_m:</div>
<blockquote>
<p>Is this because I am excluding points included in the proxy? Could I fix this by re-landmarking the scan used in the visualization?</p>
</blockquote>
</aside>
<p>If I understood correctly, you chose to exclude LMs in GPA. So, just make a copy of the LMs belonging to the proxy you want to use, then delete the ones you excluded in the gpa analysis and retry</p>

---

## Post #5 by @Stephan_Collins (2025-11-19 16:47 UTC)

<p>useful post as I was also wondering what we are supposed to do when we exclude LMs and was suprised the deformation model was not taking this into account.<br>
Would be nice though not to have to copy and edit the landmarks especially when we have a lot of them…</p>

---

## Post #6 by @muratmaga (2025-11-19 16:58 UTC)

<aside class="quote no-group" data-username="Stephan_Collins" data-post="5" data-topic="45121">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/stephan_collins/48/81446_2.png" class="avatar"> Stephan_Collins:</div>
<blockquote>
<p>Would be nice though not to have to copy and edit the landmarks especially when we have a lot of them…</p>
</blockquote>
</aside>
<p>You can open an issue on the SlicerMorph github page on this.</p>

---

## Post #7 by @Stephan_Collins (2025-11-19 17:30 UTC)

<p>Done and thanks for a great module !</p>

---

## Post #8 by @muratmaga (2025-11-20 04:36 UTC)

<p><a class="mention" href="/u/stephan_collins">@Stephan_Collins</a> There is a pull request in response to your request. it would be great if you can test it and give feedback:</p>
<p>Instructions on how to test it is here:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/pull/425">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/pull/425" target="_blank" rel="noopener nofollow ugc">github.com/SlicerMorph/SlicerMorph</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/SlicerMorph/SlicerMorph/pull/425" target="_blank" rel="noopener nofollow ugc">Auto-detect and remove excluded landmarks before dimension check in 3D visualization</a>
      </h4>

    <div class="branches">
      <code>master</code> ← <code>copilot/auto-detect-excluded-landmarks</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-11-19" data-time="22:21:15" data-timezone="UTC">10:21PM - 19 Nov 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/apps/copilot-swe-agent" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/in/1143301?v=4" class="onebox-avatar-inline" width="20" height="20">
            Copilot
          </a>
        </div>

        <div class="lines" title="2 commits changed 1 files with 28 additions and 10 deletions">
          <a href="https://github.com/SlicerMorph/SlicerMorph/pull/425/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+28</span>
            <span class="removed">-10</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When landmarks are excluded during GPA analysis, users get a dimension mismatch <span class="show-more-container"><a href="https://github.com/SlicerMorph/SlicerMorph/pull/425" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">error during 3D model visualization because the loaded landmark file contains all landmarks while the analysis data has already removed the excluded ones.

## Changes

- **Reordered landmark processing in `onSelect()`**: Convert loaded landmarks to numpy and remove excluded landmarks *before* dimension checking (previously checked first, then never reached the removal logic)
- **Enhanced error messages**: Differentiate between dimension mismatches with and without excluded landmarks, showing which indices were removed and the resulting counts

## Before/After

```python
# Before: dimension check happened before exclusion removal
self.sourceLMNode = slicer.util.loadMarkups(path)
if self.sourceLMNode.GetNumberOfControlPoints() != self.LM.lmOrig.shape[0]:
    error_and_return()  # ❌ Failed here when exclusions present
# Remove excluded landmarks  # ❌ Never reached

# After: exclusions removed first, then dimension check
self.sourceLMnumpy = logic.convertFudicialToNP(self.sourceLMNode)
if len(self.LMExclusionList) != 0:
    self.sourceLMnumpy = np.delete(self.sourceLMnumpy, excludedIndices, axis=0)
if actualCount != expectedCount:
    # Contextual error message
```

Users no longer need to manually create landmark files with excluded landmarks removed.





&lt;details&gt;

&lt;summary&gt;Original prompt&lt;/summary&gt;

&gt; 
&gt; ----
&gt; 
&gt; *This section details on the original issue you should resolve*
&gt; 
&gt; &lt;issue_title&gt;Auto detect excluded landmarks in 3D model visualization&lt;/issue_title&gt;
&gt; &lt;issue_description&gt;If LMs are excluded landmarks from a dataset, at the time of the 3D model visualization there is an inconsistency in the number of landmarks between what's included in the PCA analysis and what is specified in the LM set for the 3D reference model on disk. This throws a dimension mismatch error and confuses users. To fix the problem, user need to create a copy of the file with the excluded landmarks removed from the control point list, save and reload. It is a cumbersome user experience.
&gt; 
&gt; In case a dimensionality mismatch, we should first check whether the user entered any values to Exclude landmarks field during the analysis setup, remove the same indices from the control points, and then if the dimensionality mismatch still continues alert the user with meaningul error. If there are no excluded landmarks but the dimensionaliy still mismatches, then we should alert with a different error message.&lt;/issue_description&gt;
&gt; 
&gt; ## Comments on the Issue (you are @copilot in this section)
&gt; 
&gt; &lt;comments&gt;
&gt; &lt;/comments&gt;
&gt; 


&lt;/details&gt;

- Fixes SlicerMorph/SlicerMorph#424


---

💡 You can make Copilot smarter by setting up custom instructions, customizing its development environment and configuring Model Context Protocol (MCP) servers. Learn more [Copilot coding agent tips](https://gh.io/copilot-coding-agent-tips) in the docs.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @muratmaga (2025-11-21 03:26 UTC)

<p>this is now integrated. Update your slicermorph extension and retry.</p>

---
