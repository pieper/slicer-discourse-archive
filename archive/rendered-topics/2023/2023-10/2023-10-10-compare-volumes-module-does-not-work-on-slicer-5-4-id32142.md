---
topic_id: 32142
title: "Compare Volumes Module Does Not Work On Slicer 5 4"
date: 2023-10-10
url: https://discourse.slicer.org/t/32142
---

# Compare Volumes module does not work on Slicer-5.4

**Topic ID**: 32142
**Date**: 2023-10-10
**URL**: https://discourse.slicer.org/t/compare-volumes-module-does-not-work-on-slicer-5-4/32142

---

## Post #1 by @Michele_Bailo (2023-10-10 12:45 UTC)

<p>Hi there,<br>
I recently downloaded the latest stable version of Slicer (5.4.0) for Windows and the module compare volumes doesn’t seem to work any more (the module appears empty when I select it). Is it just me? Do you now if it works properly in subsequent nightly built versions?</p>
<p>thank you very much</p>
<p>MB</p>

---

## Post #2 by @moraleda (2023-10-10 13:15 UTC)

<p>Hi Michele,<br>
I was just about to create a new topic on this problem. Yes, I have Slicer 5.4 on MacOS and Linux and on both it does not work.</p>
<p>It seems to me that the UI file was deleted. This is the error I am getting:</p>
<pre><code class="lang-auto">self.reloadAndTestButton.toolTip = "Reload this module and then run the %s self test." % scenario
AttributeError: 'CompareVolumesWidget' object has no attribute 'reloadAndTestButton'
</code></pre>

---

## Post #3 by @pieper (2023-10-10 13:36 UTC)

<p>Yes, this was a regression in 5.4.  You can use the latest preview or older release for now.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/8c92a12d6acecde092439981af70b1a27b6d2cf1">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/8c92a12d6acecde092439981af70b1a27b6d2cf1" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/8c92a12d6acecde092439981af70b1a27b6d2cf1" target="_blank" rel="noopener">COMP: Update CompareVolumes to fix tooltip of testing scenario buttons (#7183)</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-08-21" data-time="19:23:29" data-timezone="UTC">07:23PM - 21 Aug 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>

      <div class="lines" title="changed 1 files with 1 additions and 1 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/8c92a12d6acecde092439981af70b1a27b6d2cf1" target="_blank" rel="noopener">
          <span class="added">+1</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Ensure that a tooltip is associated with each "scenario" button displayed when e<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/8c92a12d6acecde092439981af70b1a27b6d2cf1" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">nabling developer mode.

https://github.com/pieper/CompareVolumes/commit/cb755dda78f726cf9262aa4e1f75122c72a0df2f</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Or if you need to use 5.4,  you could make this one-word fix to the file /Applications/Slicer-5.4.0.app/Contents/lib/Slicer-5.4/qt-scripted-modules/CompareVolumes.py</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/pieper/CompareVolumes/commit/cb755dda78f726cf9262aa4e1f75122c72a0df2f">
  <header class="source">

      <a href="https://github.com/pieper/CompareVolumes/commit/cb755dda78f726cf9262aa4e1f75122c72a0df2f" target="_blank" rel="noopener">github.com/pieper/CompareVolumes</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/pieper/CompareVolumes/commit/cb755dda78f726cf9262aa4e1f75122c72a0df2f" target="_blank" rel="noopener">Fix developer mode issue with tooltip button</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-08-21" data-time="17:52:19" data-timezone="UTC">05:52PM - 21 Aug 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>

      <div class="lines" title="changed 1 files with 1 additions and 1 deletions">
        <a href="https://github.com/pieper/CompareVolumes/commit/cb755dda78f726cf9262aa4e1f75122c72a0df2f" target="_blank" rel="noopener">
          <span class="added">+1</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This was a bug where the tooltip for test cases was being set on the wrong butto<span class="show-more-container"><a href="https://github.com/pieper/CompareVolumes/commit/cb755dda78f726cf9262aa4e1f75122c72a0df2f" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">n.  When that button got renamed the module would not load in developer mode because the superclass button implementation was changed.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Michele_Bailo (2023-10-12 11:36 UTC)

<p>thanks, I tried with the fix of the stable version at it works properly.</p>
<p>MB</p>

---
