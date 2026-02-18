# CommonTK website broken when going to URLs with www prefix

**Topic ID**: 11422
**Date**: 2020-05-05
**URL**: https://discourse.slicer.org/t/commontk-website-broken-when-going-to-urls-with-www-prefix/11422

---

## Post #1 by @jamesobutler (2020-05-05 18:53 UTC)

<p>Posting this here because Slicer uses CTK and generally maintained by the same people:</p>
<p><a href="http://www.commontk.org/" rel="nofollow noopener">http://www.commontk.org/</a> doesn’t work as a link, though the site is accessible through <a href="http://commontk.org/" rel="nofollow noopener">http://commontk.org/</a>.  The www hyperlink version is posted at <a href="https://github.com/commontk/CTK" rel="nofollow noopener">https://github.com/commontk/CTK</a>.</p>
<p>From <a href="http://commontk.org/" rel="nofollow noopener">http://commontk.org/</a> there is a link to the API documentation which is <a href="http://www.commontk.org/docs/html/classes.html" rel="nofollow noopener">http://www.commontk.org/docs/html/classes.html</a>, but that doesn’t work however the non-www hyperlink works such as <a href="http://commontk.org/docs/html/classes.html" rel="nofollow noopener">http://commontk.org/docs/html/classes.html</a>.</p>
<p>There must be something wrong with the redirect of www links to the non-www link for this domain.  There’s a bunch of links on commontk’s website that have the broken www version.</p>

---

## Post #2 by @pieper (2020-05-05 19:22 UTC)

<p>Thanks for the heads up <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>I don’t own the <a href="http://commontk.org">commontk.org</a> domain, and I don’t remember for sure who does.  Maybe Kitware?  (<a class="mention" href="/u/jcfr">@jcfr</a> do you know?) However I went ahead and fixed the repository homepage link and also the CTK code so most things won’t break.  Would be good to fix the redirect to fix any lingering links.</p>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/commontk/CTK/commit/96d40511f46e12ff78e590ab24ac2d89668e4abe" target="_blank">github.com/commontk/CTK</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/commit/96d40511f46e12ff78e590ab24ac2d89668e4abe" target="_blank">DOC: remove www. from commontk.org urls</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2020-05-05" data-time="19:17:48" data-timezone="UTC">07:17PM - 05 May 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank">
          <img alt="pieper" src="https://avatars0.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
        
      </div>

      <div class="lines" title="changed 57 files with 68 additions and 68 deletions">
        <a href="https://github.com/commontk/CTK/commit/96d40511f46e12ff78e590ab24ac2d89668e4abe" target="_blank">
          <span class="added">+68</span>
          <span class="removed">-68</span>
        </a>
      </div>
    </div>

  </div>
</div>


  <div class="github-row">
    <pre class="github-content" style="white-space: normal;">See https://discourse.slicer.org/t/commontk-website-broken-when-going-to-urls-with-www-prefix/11422</pre>
  </div>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jcfr (2020-05-05 19:44 UTC)

<p>I just asked our sysadmin to enable https and also add redirect for www domain.</p>
<p>I will  update this thread when I hear back.</p>

---

## Post #4 by @jcfr (2020-05-12 04:28 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="3" data-topic="11422">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>I will update this thread when I hear back.</p>
</blockquote>
</aside>
<p>This has been addressed.</p>
<p></p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1327b58a8699ad95d11041490caa2fd79ed7f737.png" data-download-href="/uploads/short-url/2Js9cpk5v2JXbzie0OeEAyIZWnB.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/1327b58a8699ad95d11041490caa2fd79ed7f737_2_690x232.png" alt="image" data-base62-sha1="2Js9cpk5v2JXbzie0OeEAyIZWnB" width="690" height="232" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/1327b58a8699ad95d11041490caa2fd79ed7f737_2_690x232.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1327b58a8699ad95d11041490caa2fd79ed7f737.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1327b58a8699ad95d11041490caa2fd79ed7f737.png 2x" data-dominant-color="F0F0EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">716×241 48.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><p></p>

---
