# Move effects from SegmentEditorExtraEffects into Slicer core

**Topic ID**: 19768
**Date**: 2021-09-20
**URL**: https://discourse.slicer.org/t/move-effects-from-segmenteditorextraeffects-into-slicer-core/19768

---

## Post #1 by @rbumm (2021-09-20 17:37 UTC)

<p>To make Slicer more user-friendly for beginners and more efficient for all:<br>
Could you please add the great effects from SegmentEditorExtraEffects to the default installation of the next stable build?<br>
Thank you.</p>

---

## Post #2 by @lassoan (2021-09-20 17:47 UTC)

<p>Effects in SegmentEditorExtraEffects extension are distributed separately from the main application due to one or more of the following reasons:</p>
<ul>
<li>has not proven to be sufficiently different or better then similar effects in Slicer core</li>
<li>is not complete or stable enough and so we want to distinguish them from the stable, well-tested effects in Slicer core</li>
<li>still in development and we want to be able to be able to update them frequently, even in the Slicer Stable Release (the stable release is updated a few times a year, while extensions are updated every night)</li>
<li>depends on other extensions</li>
<li>has proven to be useful only for a small fraction of users: by having rarely needed effects separately makes it easier for new users to learn basic tools</li>
</ul>
<p>Let us know if there is any specific effect that you would like to be moved to Slicer core.</p>

---

## Post #3 by @jamesobutler (2021-09-20 17:51 UTC)

<p>Currently unclear to me which is the most used effects in the extension that could make their way into Slicer core.</p>
<p>The “Surface cut” effect is the effect our group uses the most. We find it very easy to use when segmenting ellipsoidal shaped objects like tumors in our ultrasound images.</p>

---

## Post #4 by @rbumm (2021-09-20 17:58 UTC)

<blockquote>
<blockquote>
<p>very easy to use when segmenting ellipsoidal shaped objects like tumors</p>
</blockquote>
</blockquote>
<p>exactly !</p>
<p>SegmentEditorLocalThreshold<br>
SegmentEditorHollow<br>
SegmentEditorSurfaceCut</p>
<p>are the ones that I would love to see included.</p>

---

## Post #5 by @jamesobutler (2021-09-20 17:59 UTC)

<p>We also use “Draw tube”. If “Surface cut” is moved, it should be done with “Draw tube” as both classes are similarly written. Where a change in one would likely be beneficial in the other.</p>

---

## Post #6 by @muratmaga (2021-09-20 18:01 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="19768">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Let us know if there is any specific effect that you would like to be moved to Slicer core.</p>
</blockquote>
</aside>
<p>Alternatively, would it be possible to have a button that says “Enable experimental effects” (or something like that) to bring these one, and get away from having a separate extension? Extensions are not necessarily the first place new users to look into to get more features out of segment editor (because most extensions are separate modules, not necessarily enriching existing modules).</p>

---

## Post #7 by @pieper (2021-09-20 18:06 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="19768">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>a button that says “Enable experimental effects”</p>
</blockquote>
</aside>
<p>Yes, I was going to suggest this too.  A “+” button in the toolbar that brings up a dialog explaining that the extensions are experimental would make sense.</p>

---

## Post #8 by @lassoan (2021-09-20 18:14 UTC)

<p>“Surface cut” and “Draw tube” effect depends on another extension, so it cannot be moved to the Slicer core in its current form.</p>
<p>“Local Threshold” - is still a work in progress in the sense that most users cannot figure out how to use it.</p>
<p>“Hollow” - it is already in Slicer core.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="19768">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Alternatively, would it be possible to have a button that says “Enable experimental effects” (or something like that) to bring these one, and get away from having a separate extension?</p>
</blockquote>
</aside>
<p>Slicer core is not updated continuously for stable releases, so we cannot actually experiment with extensions there.</p>
<aside class="quote no-group" data-username="pieper" data-post="7" data-topic="19768">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>A “+” button in the toolbar that brings up a dialog explaining that the extensions are experimental would make sense.</p>
</blockquote>
</aside>
<p>The issue is somewhat similar to DICOM plugins. The challenge is that someone’s advanced tool is someone else’s basic tool. We could have a <code>+</code> button but it would be better to open the extension manager with extensions that contain segment editor effects.</p>

---

## Post #9 by @muratmaga (2021-09-20 18:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="19768">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The issue is somewhat similar to DICOM plugins. The challenge is that someone’s advanced tool is someone else’s basic tool. We could have a <code>+</code> button but it would be better to open the extension manager with extensions that contain segment editor effects.</p>
</blockquote>
</aside>
<p>Ok, at the minimum this could be something like “install experimental effects”. Something to help discovering these…</p>

---

## Post #10 by @jamesobutler (2021-09-20 18:51 UTC)

<p>Very much along the lines of <a href="https://github.com/Slicer/Slicer/issues/4753" class="inline-onebox" rel="noopener nofollow ugc">Advise users which extensions to install to load special file or DICOM formats · Issue #4753 · Slicer/Slicer · GitHub</a> which is how to better let users know that there are extensions that can expand functionality for certain Slicer core modules.</p>

---

## Post #11 by @lassoan (2021-09-20 19:03 UTC)

<p>Agreed. We could add an effect with a “+” icon that would show a button that would open up the extension manager that would list all the extensions that contain segment editor effects. I’ve added a ticket to keep track of this feature request:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5880">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5880" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5880" target="_blank" rel="noopener">Make additional segment editor effects more discoverable</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-09-20" data-time="18:59:26" data-timezone="UTC">06:59PM - 20 Sep 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Is your feature request related to a problem? Please describe.

There are s<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">everal extensions that provide additional effects for Segment Editor. They are all listed in the Extensions Manager in Segmentation category and have the Segment Editor icon in their logo. Still this does not make them discoverable for new users.

## Describe the solution you'd like

We could add an effect with a "+" icon that would show a button that would open up the extension manager that would list all the extensions that contain segment editor effects.

## Describe alternatives you've considered

Moving all effects into the Slicer core would work for some effects, but not all.

## Additional context

Discussed in https://discourse.slicer.org/t/move-effects-from-segmenteditorextraeffects-into-slicer-core/19768</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>As always, add a “thumbs-up” reaction to the <a href="https://github.com/Slicer/Slicer/issues/5880">first post of the issue</a> to indicate that this feature would be important for you. <a href="https://github.com/Slicer/Slicer/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions-%2B1-desc">Issues that have a large number of reactions</a> will more likely to get attention sooner.</p>

---
