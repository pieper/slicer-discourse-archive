# Slicer doesn't open after installing SlicerWMA extension

**Topic ID**: 42356
**Date**: 2025-03-29
**URL**: https://discourse.slicer.org/t/slicer-doesnt-open-after-installing-slicerwma-extension/42356

---

## Post #1 by @Dmytro_Shyshlov (2025-03-29 03:40 UTC)

<p>Hello!</p>
<p>I’m trying to run Slicer 5.8.1 on CentOS 7.9 server with 3 extensions: SlicerDMRI, SlicerWMA, UKFTractography. Everything works fine with DMRI and UKFT, but every time I try to install SlicerWMA the program doesn’t reopen after I click on the restart button. Any subsequent attempt to launch Slicer again result in the splash screen followed by this error:<br>
$ ./Slicer<br>
error: [/apps/lib/3dslicer/5.8.1/bin/SlicerApp-real] exit abnormally - Report the problem.</p>
<p>I tried ./Slicer --disable-settings and ./Slicer --disable-modules with the same result.</p>
<p>Anyone know how to further troubleshoot this issue? Thank you!</p>

---

## Post #2 by @pieper (2025-04-01 12:38 UTC)

<p>Thanks for the report.</p>
<p>We are working on this here: <a href="https://github.com/SlicerDMRI/whitematteranalysis/pull/244" class="inline-onebox">Update requirements.txt to accept more python/vtk versions by pieper · Pull Request #244 · SlicerDMRI/whitematteranalysis · GitHub</a></p>

---

## Post #3 by @pieper (2025-04-02 18:45 UTC)

<p>Hi <a class="mention" href="/u/dmytro_shyshlov">@Dmytro_Shyshlov</a> -</p>
<p>We checked today’s Slicer Preview build (5.9.0) on linux and the SlicerWMA extension no longer prevents Slicer from starting up and SlicerDMRI and UKFTractography work as expected.</p>
<p>For the current release, SlicerWMA is still the older version that prevents Slicer from starting, so if you need to use 5.8.1 don’t install SlicerWMA.</p>
<p>It turns out SlicerWMA is actually just a stub for a module in development that didn’t add the expected functionality, so if you want to try tract parcellation you can use the whitematteranalysis python approach directly and the results should still be compatible with SlicerDMRI.</p>
<p>Thanks again for reporting!</p>

---

## Post #4 by @jamesobutler (2025-04-02 23:25 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="42356">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>We checked today’s Slicer Preview build (5.9.0) on linux and the SlicerWMA extension no longer prevents Slicer from starting up</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/pieper">@pieper</a> I see that you have removed the SlicerWMA extension from being available for the Slicer Preview release with the below commit. Is that intended? Is that how you intend to fix the slicer startup issue by removing the extension from the index?</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/commit/74a83cbefe15d8cf53de5a5bf30f26030d51ad9a">
  <header class="source">

      <a href="https://github.com/Slicer/ExtensionsIndex/commit/74a83cbefe15d8cf53de5a5bf30f26030d51ad9a" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/ExtensionsIndex</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/ExtensionsIndex/commit/74a83cbefe15d8cf53de5a5bf30f26030d51ad9a" target="_blank" rel="noopener nofollow ugc">Remove SlicerWMA which points to the wrong repository</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2025-04-02" data-time="17:24:13" data-timezone="UTC">05:24PM - 02 Apr 25 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>

      <div class="lines" title="changed 1 files with 0 additions and 9 deletions">
        <a href="https://github.com/Slicer/ExtensionsIndex/commit/74a83cbefe15d8cf53de5a5bf30f26030d51ad9a" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+0</span>
          <span class="removed">-9</span>
        </a>
      </div>
    </div>
  </div>
</div>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @pieper (2025-04-03 00:07 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> the underlying problem was actually fixed in <a href="https://github.com/SlicerDMRI/whitematteranalysis/pull/244">whitematteranalysis</a> but then we realized that the SlicerWMA module didn’t do anything particularly useful (it was an unfinished stub from an earlier developer) so we didn’t want to leave a boobytrap that installed the wrong VTK.</p>
<p>I made PRs to remove WMA from Neuro.</p>
<p>We were planning to ask to have the existing extension removed from the 5.8.1 release extensions so that people would not get bit by this.  <a class="mention" href="/u/jcfr">@jcfr</a> or <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> do you have access to remove SlicerWMA builds from the release server?</p>
<p>This whole exercise makes me look forward to getting <a href="https://github.com/Slicer/Slicer/pull/8181">this functionality</a> in place.</p>

---

## Post #6 by @jcfr (2025-04-03 00:44 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="42356">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>do you have access to remove SlicerWMA builds from the release server ?</p>
</blockquote>
</aside>
<p>We will work on removing the extension builds so that is it not available in 5.8.1.</p>

---
