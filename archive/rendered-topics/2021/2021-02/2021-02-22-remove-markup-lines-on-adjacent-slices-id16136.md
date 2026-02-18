# Remove markup lines on adjacent slices

**Topic ID**: 16136
**Date**: 2021-02-22
**URL**: https://discourse.slicer.org/t/remove-markup-lines-on-adjacent-slices/16136

---

## Post #1 by @kmalexander (2021-02-22 15:26 UTC)

<p>I’m drawing straight lines across a CT image (using the ruler markup tool).  When scrolling between adjacent slices, the line still appears on slices adjacent (either blue or red).  Is there any way to have the markup line only appear on the one slice where it is drawn, and not ‘fade’ out on adjacent slices?  Thanks.</p>

---

## Post #2 by @muratmaga (2021-02-22 16:09 UTC)

<p>SOunds like you might have 2D Projection enabled. You can disable that from the Display option of the Markups module (find the section called 2D Display).</p>

---

## Post #3 by @kmalexander (2021-02-22 16:17 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a>  That’s what I thought too - but everything in the 2D Display tab is unchecked yet it still appears.  Checking the ‘projection visibility’ box and adjusting the opacity slider only seems to change the opacity of the glyphs, and not the line itself.</p>

---

## Post #4 by @lassoan (2021-02-22 16:45 UTC)

<p>Projection only controls visibility of control points. Indeed, lines are fading out gradually, by default along 10 slices. You can make the line fade out</p>
<pre><code class="lang-python">dn=getNode('C').GetDisplayNode()
dn.SetLineColorFadingStart(0.1)
dn.SetLineColorFadingEnd(0.5)
</code></pre>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> What do you think? It makes sense to make a line look like 2D annotation (appear in a single slice) if it is planar and it is in the current slice, but I’m not sure if it is better to A. reduce fading range, or B. hide the line outside the (similarly how we hide the ROI widget completely when it does not intersect the current slice view). For lines both A and B could work similarly, but for curves, probably only B would work well.</p>

---

## Post #5 by @kmalexander (2021-02-22 16:53 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>
<p>Thanks!  I suppose I was used to using the ruler tool in previous usages such as the Line Profile Tool, or the gel/film slicelets and figured the markup line would only appear on the single slice.  Would be interesting if there was a way to set the thickness of a markup line.</p>

---

## Post #6 by @Sunderlandkyl (2021-02-22 17:00 UTC)

<p>I’m not sure either. Probably B is better since it would still help with visualization of lines/curves that intersect but are mostly perpendicular with the slice.</p>

---

## Post #7 by @lassoan (2021-02-22 17:10 UTC)

<p>I’ve created an issue for it:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/5480" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5480" target="_blank" rel="noopener">Hide markups in slice views when their region does not intersect the slice</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-02-22" data-time="17:09:14" data-timezone="UTC">05:09PM - 22 Feb 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">Is your feature request related to a problem? Please describe.
It is confusing for users that lines are visible on neighbor slices....</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:enhancement</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
