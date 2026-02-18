# Slicer elatix cannot be installed

**Topic ID**: 5865
**Date**: 2019-02-21
**URL**: https://discourse.slicer.org/t/slicer-elatix-cannot-be-installed/5865

---

## Post #1 by @Jainey (2019-02-21 07:45 UTC)

<p>Hi</p>
<p>I downloaded the latest nightly version of slicer. I cannot get the sequence registration to work. I ve installed the sequences plug in and 4D elatix.</p>
<p>I am getting an error message saying I need slicer elastix module which cannot be found<br>
Could you pls help</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2019-02-21 13:24 UTC)

<p>What platform (OS) and slicer version are you using?  I installed sequence registration yesterday on nightlies of mac and linux and it worked fine.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a>: the dashboards do indicate a lot of extension issues on the factory machines.</p>

---

## Post #3 by @cpinter (2019-02-21 15:01 UTC)

<p>Probably Mac, see</p><aside class="quote" data-post="14" data-topic="4531">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicerelastix-extension-not-available-on-mac/4531/14">SlicerElastix extension not available on Mac</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I’ve updated SlicerElastix to use a specific Elastix hash.
  </blockquote>
</aside>

<p>We haven’t had a SlicerElastix on Mac for at least a year. We should at least upload a package for the stable if we cannot fix the factory build.</p>
<p>After a quick search there were unanswered inquiries about the same thing from others, such as</p><aside class="quote" data-post="1" data-topic="5434">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/da6949/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-elastix-on-mac/5434">Slicer elastix on Mac</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi 
I cannot get sequence registration module to work on MAc. I am using slicer 4.10 and installed elastix separately and tried specifying the path on general registration. Could you please help. Thanks
  </blockquote>
</aside>

<p>I did my best to investigate then to push the issue, but it’s not resolved as of now.</p>

---

## Post #4 by @cpinter (2019-02-21 15:13 UTC)

<p>Hm we actually do have a SlicerElastix package for today’s nightly:<br>
<a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercombine=or&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=SlicerElastix" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercombine=or&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=SlicerElastix</a></p>
<p>But we seem to have a Windows issue now <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Update: <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2019-02-11&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=SlicerElastix" rel="nofollow noopener">this</a> is the last day it worked, 10 days ago.</p>

---

## Post #5 by @jcfr (2019-02-21 15:22 UTC)

<blockquote>
<p>the dashboards do indicate a lot of extension issues on the factory machines.</p>
</blockquote>
<p>Most of them are compilation errors that could easily be fixed.</p>
<p>Regarding SlicerElastix issues:</p>
<ul>
<li>On windows it is a regression caused by <a href="https://github.com/lassoan/SlicerElastix/commit/9ef96648402bd60e50c62cd511e886d5a2a04a98" class="inline-onebox">COMP: turn off override warnings · lassoan/SlicerElastix@9ef9664 · GitHub</a></li>
</ul>
<pre><code class="lang-auto">cl : Command line error D8021: invalid numeric argument '/Wno-inconsistent-missing-override' [D:\D\P\S-0-E-b\
SlicerElastix-build\elastix-build\CMakeFiles\CMakeTmp\cmTC_381f5.vcxproj] [D:\D\P\S-0-E-b\SlicerElastix-build
\elastix.vcxproj]

          0 Warning(s)
          1 Error(s)

</code></pre>
<ul>
<li>On linux, the following warning is reported <code>warning: unrecognized command line option ‘-Wno-inconsistent-missing-override’</code>, and extension failed to upload last night  [1], I manually re-did the upload and it is available now. See <a href="http://slicer.kitware.com/midas3/slicerappstore?os=linux&amp;arch=amd64&amp;revision=27968&amp;category=&amp;search=SlicerElastix&amp;layout=layout" class="inline-onebox">@KitwareMedical/slicer-extensions-webapp</a></li>
</ul>
<p>[1] it failed because of server issue. This a known problem and we have path forward, we need resources (aka financial support) to finalize the transition.</p>
<ul>
<li>On macOS, it uploaded without trouble. See <a href="http://slicer.kitware.com/midas3/slicerappstore?os=macosx&amp;arch=amd64&amp;revision=27968&amp;category=&amp;search=SlicerElastix&amp;layout=layout" class="inline-onebox">@KitwareMedical/slicer-extensions-webapp</a></li>
</ul>

---

## Post #6 by @jcfr (2019-02-21 15:24 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="3" data-topic="5865">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>We haven’t had a SlicerElastix on Mac for at least a year</p>
</blockquote>
</aside>
<p>SlicerElastix is available on macOS for both the <a href="http://slicer.kitware.com/midas3/slicerappstore?os=macosx&amp;arch=amd64&amp;revision=27931&amp;category=&amp;search=SlicerElastix&amp;layout=layout">latest release</a> as well as the nightly build (see above).</p>

---

## Post #7 by @cpinter (2019-02-21 15:27 UTC)

<p>Yes I have seen that since then. It’s great news and good to know.</p>

---

## Post #8 by @pieper (2019-02-21 15:40 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="5" data-topic="5865">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>On windows it is a regression caused by <a href="https://github.com/lassoan/SlicerElastix/commit/9ef96648402bd60e50c62cd511e886d5a2a04a98">https://github.com/lassoan/SlicerElastix/commit/9ef96648402bd60e50c62cd511e886d5a2a04a98 </a></p>
</blockquote>
</aside>
<p>Thanks for catching that Jc - after the commit I was wondering if I needed to make that flag conditional to be mac-only but I couldn’t get any error message from the dashboard.  The <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1519245">windows</a> and <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1518941">linux</a> build messages were cryptic and I thought they were unrelated since so many other things were breaking.  I guess this is the server issue you refer to?</p>
<p>In any case I can add a check so that the flag is only added on mac.</p>

---

## Post #9 by @pieper (2019-02-21 16:16 UTC)

<p>I think this will fix it.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/lassoan/SlicerElastix/pull/13">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerElastix/pull/13" target="_blank" rel="noopener">github.com/lassoan/SlicerElastix</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/lassoan/SlicerElastix/pull/13" target="_blank" rel="noopener">only add warning suppression for apple</a>
      </h4>

    <div class="branches">
      <code>lassoan:master</code> ← <code>pieper:suppress-on-apple</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2019-02-21" data-time="16:09:37" data-timezone="UTC">04:09PM - 21 Feb 19 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/pieper" target="_blank" rel="noopener">
            <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
            pieper
          </a>
        </div>

        <div class="lines" title="3 commits changed 1 files with 3 additions and 1 deletions">
          <a href="https://github.com/lassoan/SlicerElastix/pull/13/files" target="_blank" rel="noopener">
            <span class="added">+3</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Addresses https://discourse.slicer.org/t/slicer-elatix-cannot-be-installed/5865/<span class="show-more-container"><a href="https://github.com/lassoan/SlicerElastix/pull/13" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">5</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
