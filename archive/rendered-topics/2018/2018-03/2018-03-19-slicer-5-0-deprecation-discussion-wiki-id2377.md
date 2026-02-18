# Slicer 5.0 deprecation discussion/wiki

**Topic ID**: 2377
**Date**: 2018-03-19
**URL**: https://discourse.slicer.org/t/slicer-5-0-deprecation-discussion-wiki/2377

---

## Post #1 by @cpinter (2018-03-19 19:42 UTC)

<p>Hi all,</p>
<p>Not sure how to propose topics in the agenda, as the <a href="https://www.slicer.org/wiki/Developer_Meetings">developer hangouts page</a> seems not to be used anymore.</p>
<p>In any case, I’d like to propose that we talk about non-backward-compatible changes regarding the upcoming 5.0 release, especially removing obsolete features, and other big changes that are best done with this major version upgrade.</p>
<p>Thanks!</p>
<hr>
<p>[edit: after checking with <code>@cpinter</code>, I moved this to a new topic in Development to give more visibility and space for discussion – <code>@ihnorton</code>]</p>

---

## Post #2 by @pieper (2018-03-19 20:13 UTC)

<p>Hi Csaba -</p>
<p>Yes, this thread has effectively taken over for the wiki, so this is the right place to post. (I guess we could discuss if there’s a better way to organize things).</p>
<p>I’m not able to join this Tuesday, but it sounds like a good topic.  Last week we briefly discussed that 5.0 is as big a step as the name might imply, but we had made the naming decision a few months or so ago and the plan at least so far is to keep it, even if there are no big API changes (mostly just updated versions of VTK, ITK, Qt).</p>
<p>-Steve</p>

---

## Post #3 by @jcfr (2018-03-19 20:35 UTC)

<aside class="quote no-group quote-modified" data-username="cpinter" data-post="78" data-topic="53">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"><a href="https://discourse.slicer.org/t/weekly-hangout-for-slicer-user-and-developer/53/78">Weekly Hangout for Slicer user and developer</a></div>
<blockquote>
<p>seems not to be used anymore.</p>
</blockquote>
</aside>
<p>Indeed, I updated the page accordingly.</p>
<aside class="quote no-group quote-modified" data-username="cpinter" data-post="78" data-topic="53">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"><a href="https://discourse.slicer.org/t/weekly-hangout-for-slicer-user-and-developer/53/78">Weekly Hangout for Slicer user and developer</a></div>
<blockquote>
<p>we talk about non-backward-compatible changes regarding the upcoming 5.0 release</p>
</blockquote>
</aside>
<p>So far incompatible changes have been documented here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide" class="inline-onebox">Documentation/Nightly/Developers/Tutorials/MigrationGuide - Slicer Wiki</a></p>
<p>I suggest you create a wiki page here: <a href="https://www.slicer.org/wiki/Documentation/Labs#Internals" class="inline-onebox">Documentation/Labs - Slicer Wiki</a> where we could start document functionality to remove etc …</p>

---

## Post #4 by @cpinter (2018-03-19 21:04 UTC)

<p>Thanks Steve and Jc!</p>
<p>I created <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer50">this page</a> and added a list of things that could be done in terms of the major version upgrade. Feel free to add/comment/etc.</p>
<p>I’m happy to help with the changes we agree on before the release of 5.0.</p>

---

## Post #5 by @pieper (2018-03-19 21:48 UTC)

<p>Thanks for making the page <a class="mention" href="/u/cpinter">@cpinter</a>! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=5" title=":+1:" class="emoji" alt=":+1:">  The items on the page seem very well thought out.</p>

---

## Post #6 by @cpinter (2018-03-20 15:33 UTC)

<p>A major decision was made at the hangout:</p>
<ul>
<li>Upcoming release: 4.10 or 5.0?
<ul>
<li>The question is whether to consider the user perspective (5.0: Qt5, no Editor on GUI, etc) or the developer perspective (4.10: no Qt4, no Editor as API, node copying, etc.)</li>
</ul>
</li>
</ul>
<p>So we decided that the best would be to release 4.10 this time, so that we have time to make the non-backwards-compatible changes for 5.0 (the wiki list will be extended), because major version number bumps happen only every several years.</p>

---

## Post #7 by @jcfr (2018-03-20 17:38 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> Thanks for the update</p>
<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="2377">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>the wiki list will be extended</p>
</blockquote>
</aside>
<p>See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer50">Work-in-progress: Transition plans for Slicer 4.10, and major changes in Slicer 5.0</a></p>

---

## Post #8 by @jcfr (2018-03-22 23:13 UTC)

<p>I realized that the code associated with these two CLI modules <a href="https://github.com/Slicer/Slicer/tree/master/Modules/CLI/BlobDetection">BlobDetection</a> and <a href="https://github.com/Slicer/Slicer/tree/master/Modules/CLI/ConnectedComponent">ConnectedComponent</a> have <strong>NOT</strong> been compiled since <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=20744">r20744</a> (from August 2010).</p>
<p>The commit message indicates:</p>
<pre><code class="lang-plaintext">ENH: remove BlobDetection and other CLI modules as requested
</code></pre>
<p>Associated issue was:</p>
<ul>
<li><a href="https://issues.slicer.org/view.php?id=2809">#2809</a>: Create extensions for BlobDetection and ConnectedComponent module</li>
</ul>
<p>And a excerpt from <a class="mention" href="/u/pieper">@pieper</a> reply from on the <a href="http://slicer-devel-archive.65872.n3.nabble.com/Adding-new-modules-to-Slicer-core-tp4025907p4026923.html">slicer-devel</a> mailing list thread entitled <code>Re: Adding new modules to Slicer core? </code>:</p>
<aside class="quote no-group">
<blockquote>
<p>I haven’t looked at this in detail, but I think the module has the <strong>potential for wide utility</strong>, but since it’s <strong>currently disabled</strong> it’s not yet widely used. It also seems that it <strong>doesn’t have documentation</strong>, which is probably why it is currently disabled.  So yes, for now I think BlobDetection and the related module ConnectedComponent <strong>should move to an extension</strong> (as should a few other specialized modules).  We should probably make this a group project at some point, but as we discussed on yesterday’s call performance optimization and ITKv4 are higher priorities right now <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
</blockquote>
</aside>
<p>Based on the information I found, I will submit a PR removing the modules today and plan on integrating it tomorrow.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/923">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/923" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/923" target="_blank" rel="noopener">Color picker window layout issue</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:34:32" data-timezone="UTC">10:34PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:34:32" data-timezone="UTC">10:34PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=923). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @jcfr (2018-03-25 07:55 UTC)

<p>Based on feedback posted on <a href="https://github.com/Slicer/Slicer/pull/923">Slicer/Slicer#923</a>, we created a dedicated extension to bundle Slicer legacy modules:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Slicer/SlicerLegacyModules">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/SlicerLegacyModules" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <img src="https://opengraph.githubassets.com/e39413c83e00edf0065db63cea01ddd4fa62e42f2a792c6ba633b2d2a0c9fb3f/Slicer/SlicerLegacyModules" class="thumbnail" width="" height="">

<h3><a href="https://github.com/Slicer/SlicerLegacyModules" target="_blank" rel="noopener">GitHub - Slicer/SlicerLegacyModules: Collection of legacy Slicer modules</a></h3>

  <p>Collection of legacy Slicer modules. Contribute to Slicer/SlicerLegacyModules development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>There is also a <a href="https://github.com/Slicer/SlicerLegacyModules#how-to-extract-module-history-from-slicer-and-include-it-in-this-extension-">step-by-step guide</a> explaining how to extract history.</p>

---
