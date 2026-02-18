# Linux build issues

**Topic ID**: 1284
**Date**: 2017-10-25
**URL**: https://discourse.slicer.org/t/linux-build-issues/1284

---

## Post #1 by @dcantor (2017-10-25 03:12 UTC)

<p>That makes sense, it could be the case. I am downloading the Slicer linux build. How can I tell if what you mention is happening?</p>
<p>D.</p>

---

## Post #2 by @jcfr (2017-10-25 03:28 UTC)

<blockquote>
<p>I am downloading the Slicer linux build</p>
</blockquote>
<p>To clarify, no “build” (as in build tree or sdk) is available for download. Only the sources or the pre-built binaries can be downloaded .</p>
<p>That said, you can check if the Qt libraries (dll) that you downloaded (or built) are 32-bit or 64-bit using dumpbin executable</p>
<aside class="onebox stackexchange" data-onebox-src="https://superuser.com/questions/358434/how-to-check-if-a-binary-is-32-or-64-bit-on-windows">
  <header class="source">

      <a href="https://superuser.com/questions/358434/how-to-check-if-a-binary-is-32-or-64-bit-on-windows" target="_blank" rel="noopener">superuser.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://superuser.com/users/60605/septagram" target="_blank" rel="noopener">
    <img alt="Septagram" src="https://www.gravatar.com/avatar/2a3c94bbf645e76c0f8a727abae35b7a?s=256&amp;d=identicon&amp;r=PG" class="thumbnail onebox-avatar" width="" height="">
  </a>

<h4>
  <a href="https://superuser.com/questions/358434/how-to-check-if-a-binary-is-32-or-64-bit-on-windows" target="_blank" rel="noopener">How to check if a binary is 32 or 64 bit on Windows?</a>
</h4>

<div class="tags">
  <strong>windows, binary-files, 32-vs-64-bit</strong>
</div>

<div class="date">
  asked by
  
  <a href="https://superuser.com/users/60605/septagram" target="_blank" rel="noopener">
    Septagram
  </a>
  on <a href="https://superuser.com/questions/358434/how-to-check-if-a-binary-is-32-or-64-bit-on-windows" target="_blank" rel="noopener">10:29AM - 17 Nov 11 UTC</a>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @dcantor (2017-10-25 03:52 UTC)

<p>Hi Jean,</p>
<p>dumpbin is exclusive for Windows (?)</p>
<p>I used ldd (as the reported problem is on linux) and this is what I got:</p>
<p>I don’t see any Qt dependency.</p>
<p>D.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c71978ee5f85f787a619368f3f3f161bc87b08d.png" data-download-href="/uploads/short-url/hKSzICKxKhnXe09HI5k7ytZMEpL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c71978ee5f85f787a619368f3f3f161bc87b08d_2_690x323.png" alt="image" data-base62-sha1="hKSzICKxKhnXe09HI5k7ytZMEpL" width="690" height="323" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c71978ee5f85f787a619368f3f3f161bc87b08d_2_690x323.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c71978ee5f85f787a619368f3f3f161bc87b08d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c71978ee5f85f787a619368f3f3f161bc87b08d.png 2x" data-dominant-color="8F9090"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">729×342 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @jcfr (2017-10-25 15:39 UTC)

<p><a class="mention" href="/u/dcantor">@dcantor</a> Apologize for the confusion, It looks like windows release question where asked on the same thread. See  <a href="https://discourse.slicer.org/t/cant-build-slicer/1280">Can't build Slicer</a> <a class="mention" href="/u/ihnorton">@ihnorton</a> just split the topic.</p>

---

## Post #5 by @jcfr (2017-10-25 15:41 UTC)

<aside class="quote no-group" data-username="dcantor" data-post="1" data-topic="1284">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dcantor/48/782_2.png" class="avatar"> dcantor:</div>
<blockquote>
<p>That makes sense, it could be the case. I am downloading the Slicer linux build. How can I tell if what you mention is happening?</p>
</blockquote>
</aside>
<p>Also would it be possible to provide the original context of your question ?</p>

---
