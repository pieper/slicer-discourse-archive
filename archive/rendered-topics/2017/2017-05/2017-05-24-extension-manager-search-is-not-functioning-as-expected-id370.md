# Extension Manager search is not functioning as expected

**Topic ID**: 370
**Date**: 2017-05-24
**URL**: https://discourse.slicer.org/t/extension-manager-search-is-not-functioning-as-expected/370

---

## Post #1 by @fedorov (2017-05-24 13:18 UTC)

<p>Search results do not make sense to me.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0bd404e5844a373e6502087f5d1898a6d9f7ed6.png" data-download-href="/uploads/short-url/rv38SeR5Sa1YGvwFC5Gzedu2Btc.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0bd404e5844a373e6502087f5d1898a6d9f7ed6_2_641x500.png" alt="image" data-base62-sha1="rv38SeR5Sa1YGvwFC5Gzedu2Btc" width="641" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0bd404e5844a373e6502087f5d1898a6d9f7ed6_2_641x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0bd404e5844a373e6502087f5d1898a6d9f7ed6_2_961x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0bd404e5844a373e6502087f5d1898a6d9f7ed6.png 2x" data-dominant-color="D8DAD9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1006×784 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @tdiprima (2017-05-24 14:07 UTC)

<p>Agreed.  When I go to install the SlicerPathology extension, and bring up the extension wizard, there are 3 slicer pathologies.  And 3 ChangeTrackers.</p>
<p>Prior to re-install, I deleted the NA-MIC folder inside of AppData/Roaming.  So there was no cached copy there to cause the triplicates.</p>
<p>The fix was – I had to reboot the machine TWICE.  The second time I did a hard reboot.  So maybe a full shutdown and restart was the answer.</p>
<p>So far we’ve seen this behavior on multiple Windows machines.  (And <a class="mention" href="/u/fedorov">@fedorov</a>  it looks like you’re using Mac, right?)</p>
<p>Thanks.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/310ac0feb24a52dc5f1c52930f698233be4fcc04.png" data-download-href="/uploads/short-url/6ZQr2y6AsX31P5yfbUOtvbHTbZW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/310ac0feb24a52dc5f1c52930f698233be4fcc04_2_690x388.png" alt="image" data-base62-sha1="6ZQr2y6AsX31P5yfbUOtvbHTbZW" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/310ac0feb24a52dc5f1c52930f698233be4fcc04_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/310ac0feb24a52dc5f1c52930f698233be4fcc04_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/310ac0feb24a52dc5f1c52930f698233be4fcc04.png 2x" data-dominant-color="EDEEF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1056×594 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2017-05-24 14:28 UTC)

<p>I’ve experienced random slowdowns non-responses, too (progress stuck at 10%, no extensions come up; after restarting Slicer and the extension manager everything worked).</p>
<p>Probably not related to Slicer, as <a href="http://slicer.kitware.com/midas3/slicerappstore">loading the extension manager directly from a browser</a> has similar issues, too.</p>

---

## Post #4 by @fedorov (2017-05-24 15:52 UTC)

<aside class="quote no-group" data-username="tdiprima" data-post="2" data-topic="370">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tdiprima/48/9469_2.png" class="avatar"> tdiprima:</div>
<blockquote>
<p><a class="mention" href="/u/fedorov">@fedorov</a>  it looks like you’re using Mac, right?</p>
</blockquote>
</aside>
<p>correct, I am using mac</p>

---

## Post #5 by @ihnorton (2017-05-25 15:40 UTC)

<p>I’m also seeing severe hangs in the extension manager and the online view.</p>

---

## Post #6 by @pieper (2017-05-25 16:04 UTC)

<p>earlier today for me it hung for quite a while but finally succeeded.</p>

---

## Post #7 by @fedorov (2017-05-25 16:57 UTC)

<p>I think there could be 2 separate (or related?) issue:</p>
<ol>
<li>Search succeeds, but search results are incorrect (this is what I initially reported).</li>
<li>Extension browser hangs or takes very long time to load.</li>
</ol>

---

## Post #8 by @lassoan (2017-05-25 17:14 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="7" data-topic="370">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Search succeeds, but search results are incorrect (this is what I initially reported</p>
</blockquote>
</aside>
<p>First of all, the filtering was correct. ChangeTracker extension has “pathology” word in its description.<br>
Duplicate listings has been popping up randomly in the last few years (with or without any filtering applied). It’s not nice and it should be fixed, but otherwise harmless.</p>
<aside class="quote no-group" data-username="fedorov" data-post="7" data-topic="370">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Extension browser hangs or takes very long time to load.</p>
</blockquote>
</aside>
<p>That’s a new issue and it’s severe. The wait is long enough so that people don’t wait for the result and conclude that Slicer is broken. It should be fixed ASAP. Probably the simplest solution would be to not spend time with determining the latest available version when a specific version is already supplied (or never try to determine latest version but just display a meaningful error message to let the user know what is missing and how to get that information).</p>

---

## Post #9 by @fedorov (2017-05-25 18:14 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="370">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>First of all, the filtering was correct.</p>
</blockquote>
</aside>
<p>Can you explain the presence of CMFreg? Perhaps there is an explanation, but I don’t see any mentioning of “pathology” in the extension metadata. But I don’t know what other sources Extensions Manager is searching. It’s confusing.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/blob/master/CMFreg.s4ext">
  <header class="source">

      <a href="https://github.com/Slicer/ExtensionsIndex/blob/master/CMFreg.s4ext" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/ExtensionsIndex/blob/master/CMFreg.s4ext" target="_blank" rel="noopener">Slicer/ExtensionsIndex/blob/master/CMFreg.s4ext</a></h4>


      <pre><code class="lang-s4ext">#
# First token of each non-comment line is the keyword and the rest of the line
# (including spaces) is the value.
# - the value can be blank
#

# This is source code manager (i.e. svn)
scm git
scmurl https://github.com/DCBIA-OrthoLab/CMFreg.git
scmrevision master

# list dependencies
# - These should be names of other modules that have .s4ext files
# - The dependencies will be built first
depends NA

# Inner build directory (default is ".")
build_subdirectory .

# homepage
</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/ExtensionsIndex/blob/master/CMFreg.s4ext" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @lassoan (2017-05-25 21:10 UTC)

<p>Good point. Most likely CMFreg (and all other extensions than ChangeTracker and SlicerPathology) are duplicate items left over from the time when the filtering criteria was still just “pa”.</p>

---

## Post #11 by @lassoan (2017-05-26 14:26 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> This extension manager hang is very confusing for users. If it’s too difficult to properly fix it then maybe just temporarily revert the latest developments and enable them again once the performance issue is sorted out.</p>

---

## Post #12 by @jcfr (2017-05-29 21:55 UTC)

<p>Behavior should now be back to normal when used  within Slicer. Generally speaking, the slow lookup is performed only if needed.</p>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/midasplatform/slicerappstore/commit/71d41e938cb7021a7d7659834bd5c55112d39479" target="_blank">github.com/midasplatform/slicerappstore</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/midasplatform/slicerappstore/commit/71d41e938cb7021a7d7659834bd5c55112d39479" target="_blank">ENH: Get most recent revision only if revision parameter is not specified</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2017-05-29" data-time="21:53:32" data-timezone="UTC">09:53PM - 29 May 17 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank">
          <img alt="jcfr" src="https://avatars0.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
        
      </div>

      <div class="lines" title="changed 1 files with 7 additions and 3 deletions">
        <a href="https://github.com/midasplatform/slicerappstore/commit/71d41e938cb7021a7d7659834bd5c55112d39479" target="_blank">
          <span class="added">+7</span>
          <span class="removed">-3</span>
        </a>
      </div>
    </div>

  </div>
</div>


  <div class="github-row">
    <pre class="github-content" style="white-space: normal;">See https://discourse.slicer.org/t/extension-manager-search-is-not-functioning-as-expected/370/11</pre>
  </div>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
