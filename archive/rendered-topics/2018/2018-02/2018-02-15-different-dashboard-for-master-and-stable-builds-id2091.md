# Different dashboard for master and stable builds

**Topic ID**: 2091
**Date**: 2018-02-15
**URL**: https://discourse.slicer.org/t/different-dashboard-for-master-and-stable-builds/2091

---

## Post #1 by @jcfr (2018-02-15 14:15 UTC)

<p>Hi Slicers,</p>
<p>Following last week <a href="https://discourse.slicer.org/t/weekly-hangout-for-slicer-user-and-developer/53/57">hangout</a>, we decided to improve the developer experience by submitting build results associated with the stable and master version of Slicer to different dashboards.</p>
<h3>Which cdash URL for what ?</h3>
<p>Practically speaking, this means the following:</p>
<ul>
<li>daily build of Slicer <strong>extensions</strong> associated with the latest stable release of Slicer will be submitted to
<ul>
<li><a href="http://slicer.cdash.org/index.php?project=Slicer4">http://slicer.cdash.org/index.php?project=Slicer4</a></li>
</ul>
</li>
<li>daily build of Slicer <strong>extensions</strong> and <strong>applications</strong> associated with the latest revision of the source code will be be submitted to
<ul>
<li><a href="http://slicer.cdash.org/index.php?project=SlicerMaster">http://slicer.cdash.org/index.php?project=SlicerMaster</a></li>
</ul>
</li>
</ul>
<h3>Timeline</h3>
<ul>
<li>
<strong>Before the end of the week</strong>: Project <a href="http://slicer.cdash.org/index.php?project=SlicerMaster">SlicerMaster</a> was just created on CDash, starting tonight or tomorrow Slicer source code will be updated to submit results to that project</li>
<li>
<strong>Just before the next Slicer stable release</strong>: Project <a href="http://slicer.cdash.org/index.php?project=Slicer4">Slicer4</a> will be renamed to <code>SlicerStable</code>
</li>
</ul>

---

## Post #2 by @pieper (2018-02-15 14:32 UTC)

<p>Excellent!</p>
<p>When this is available let’s also remember to update the links in the CDash section of the developer wiki pages:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Developers" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Developers</a><br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers</a></p>

---

## Post #3 by @jcfr (2018-02-15 14:46 UTC)

<h3>Updates</h3>
<ul>
<li>
<a href="https://github.com/Slicer/Slicer/pull/892">PR Slicer/Slicer#892</a> updating the CDash project from <code>Slicer4</code> to <code>SlicerMaster</code> is being reviewed.</li>
<li>Wiki pages have been updated (see <a href="https://www.slicer.org/w/index.php?title=Documentation%2F4.8%2FDevelopers&amp;type=revision&amp;diff=58613&amp;oldid=55523">here</a> and <a href="https://www.slicer.org/w/index.php?title=Documentation%2FNightly%2FDevelopers&amp;type=revision&amp;diff=58610&amp;oldid=54941">here</a>). Thanks <a class="mention" href="/u/pieper">@pieper</a> for pointing this out.</li>
<li>
<a href="https://github.com/mhalle/slicer4-download/pull/12">PR mhalle/slicer4-download#12</a> updating the links available on <a href="http://download.slicer.org/">http://download.slicer.org/</a> was just submitted</li>
</ul>
<h3>Questions</h3>
<p>We initially chose the pair</p>
<pre><code>SlicerStable / SlicerMaster
</code></pre>
<p>because using</p>
<pre><code>SlicerStable / SlicerNightly
</code></pre>
<p>would be confusing due to the fact both CDash project would host build results performed “nightly”.</p>
<p>That said, for years, we have been calling the different release <strong>Nightly</strong> and <strong>Stable</strong>.  For this reason, I wonder if the following pair will be more consistent:</p>
<pre><code>  SlicerStableRelease / SlicerNightlyRelease
</code></pre>
<p>This would also be consistent with the naming used on <a href="http://download.slicer.org/">http://download.slicer.org/</a> and also the release type option introduced in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26420">r26420</a>.</p>
<p>What do you think ?</p>

---

## Post #4 by @lassoan (2018-02-15 15:23 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="3" data-topic="2091">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>SlicerStableRelease / SlicerNightlyRelease</p>
</blockquote>
</aside>
<p>I like the SlicerStableRelease / SlicerNightlyRelease separation because it is more clear. However, it is a bit long: two words instead of one - so, we’ll probably often drop one word for brevity and then it’ll not be clear anymore. Also, it is still not fully clear. For example, how do I tell a user to download the latest nightly version of an extension for the latest stable release?</p>
<p>I think we need to avoid the word “nightly” as it comes from the times when we did not rebuild extensions for stable versions every night.</p>
<p>Stable version is a very good word, we just need to find a similar name for the master/trunk version. What about these?</p>
<ul>
<li>development</li>
<li>preview</li>
<li>experimental</li>
<li>beta</li>
<li>master</li>
<li>snapshot</li>
</ul>

---

## Post #5 by @jcfr (2018-02-15 19:03 UTC)

<p>I like <code>preview</code>, <code>master</code> or even <code>draft</code></p>
<p>For the “master” release, we could then have:</p>
<ul>
<li><code>SlicerPreviewRelease</code></li>
<li><code>SlicerDraftRelease</code></li>
</ul>
<p>Any preference ?</p>
<p>Here is what it would look like on the download site:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d84d5d06ab08fe4b2e3a71c34d0003284f8e431.png" data-download-href="/uploads/short-url/mttyMrfSqONznSP6QrIPTH9e7xn.png?dl=1" title="preview_release_slicer"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d84d5d06ab08fe4b2e3a71c34d0003284f8e431.png" alt="preview_release_slicer" data-base62-sha1="mttyMrfSqONznSP6QrIPTH9e7xn" width="690" height="247" data-dominant-color="F8F8F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">preview_release_slicer</span><span class="informations">899×322 15.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea098b9d874da72b337ad2e1887676b5f7fb3fa5.png" data-download-href="/uploads/short-url/xoob5T5ohddnG5oKGkBrEFgj1sh.png?dl=1" title="draft_release_slicer"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea098b9d874da72b337ad2e1887676b5f7fb3fa5.png" alt="draft_release_slicer" data-base62-sha1="xoob5T5ohddnG5oKGkBrEFgj1sh" width="690" height="206" data-dominant-color="F7F8F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">draft_release_slicer</span><span class="informations">877×263 13.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @ihnorton (2018-02-15 19:33 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="3" data-topic="2091">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>That said, for years, we have been calling the different release Nightly and Stable</p>
</blockquote>
</aside>
<p>I think many people will keep calling the master-branch-build “Nightly” for a long time out of habit. Maybe instead of “Stable” we could just call the release-branch dashboard by version, e.g. “Slicer4.8”, because that is what people do colloquially anyway.  (and update at each release unless it is a lot of effort/risk to change)</p>
<p>Instead of renaming “Nightly” to avoid confusion, we could then call the (nightly-updated) extension section of the “Slicer4.8” dashboard something like “4.8-Continuous”.</p>

---

## Post #7 by @lassoan (2018-02-15 20:05 UTC)

<p>For CMake users, Nightly/Continuous/Experimental have very specific meaning. It would be better to avoid these words referring to different branches (we can have nightly/continuous/experimental builds for master or stable branches).</p>
<p>Using specific version number anywhere means that it has to be updated for each stable release. As we would like to release stable versions more frequently (4 times a year would be great), these updates at various places could require significant effort.</p>
<p>I like <strong>Stable Release / Preview Release</strong>. <em>Preview release</em> is used as a synonym of <em>beta release</em> for a for a couple of software I know, so it would not be a Slicer-only naming convention.</p>

---

## Post #8 by @ihnorton (2018-02-15 20:08 UTC)

<blockquote>
<p>For CMake users, Nightly/Continuous/Experimental have very specific meaning.</p>
</blockquote>
<p>Fair enough. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> to Stable/Preview then.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://martinfowler.com/bliki/TwoHardThings.html">
  <header class="source">

      <a href="https://martinfowler.com/bliki/TwoHardThings.html" target="_blank" rel="noopener">martinfowler.com</a>
  </header>

  <article class="onebox-body">
    <img width="278" height="278" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d92f2ba761e87dcb14c510c0c85619d0e57d6942.png" class="thumbnail onebox-avatar" data-dominant-color="B796B7">

<h3><a href="https://martinfowler.com/bliki/TwoHardThings.html" target="_blank" rel="noopener">bliki: TwoHardThings</a></h3>

  <p>There are only two hard things in Computer Science: cache invalidation and naming things -- Phil Karlton (bonus variations on the page)</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @cpinter (2018-02-15 20:09 UTC)

<p>I like Stable for the release branch too.</p>
<p>For the terms from <a class="mention" href="/u/lassoan">@lassoan</a>’s list I’d prefer <code>Development</code> or <code>Preview</code>. <code>Master</code> is very technical, the users won’t know what it is, and <code>Draft</code> (at least to me) suggests that it’s not ready to use. I think <code>Continuous</code> would be confusing, because it has a different meaning: tests after each commit.</p>
<p><a class="mention" href="/u/ihnorton">@ihnorton</a> is right though, people will say <code>Nightly</code> anyway, so keeping that would make sense. Regardless how that term was originally born, it means the “snapshot for the day”, so I think it would be the least confusing.</p>

---

## Post #10 by @jcfr (2018-02-16 20:37 UTC)

<p>Updates:</p>
<ul>
<li>
<p>Dashboard will be <a href="http://slicer.cdash.org/index.php?project=SlicerPreview">SlicerPreview</a></p>
</li>
<li>
<p>Slicer has been updated accordingly - see <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26928">r26928</a></p>
</li>
<li>
<p>New <a href="https://github.com/mhalle/slicer4-download/pull/13">PR mhalle/slicer4-download#13</a> was just submitted to update <a href="http://download.slicer.org/">http://download.slicer.org/</a> and use the term <code>Preview Release</code> instead of <code>Nightly Build</code></p>
</li>
</ul>

---
