# Internal error : Bad array new length

**Topic ID**: 10179
**Date**: 2020-02-10
**URL**: https://discourse.slicer.org/t/internal-error-bad-array-new-length/10179

---

## Post #1 by @prorai (2020-02-10 07:21 UTC)

<p>Hello Slicer Team,<br>
Today I run into the issue ‘Slicer has caught an internal error.’</p>
<blockquote>
<p>The message detail is:</p>
<p>Exception thrown in event: bad array new length</p>
</blockquote>
<p>i was running a batch script to generate a 3d model using seed grow segmentation, first i got this issue i’m attaching a log file here , so i rerun  the program and it worked as usual normal and created the output .</p>
<p>My Question is , is there any setting to avoid the internal errors and give slicer whatever the memory or source it requires and use it at its full potential?</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://filebin.net/ehx1iicfhm4on7um">
  <header class="source">
      <img src="https://filebin.net/static/img/favicon.png" class="site-icon" width="" height="">

      <a href="https://filebin.net/ehx1iicfhm4on7um" target="_blank" rel="noopener nofollow ugc">filebin.net</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://filebin.net/ehx1iicfhm4on7um" target="_blank" rel="noopener nofollow ugc">Filebin | ehx1iicfhm4on7um</a></h3>

  <p>Convenient file sharing. Think of it as Pastebin for files. Registration is not required. Large files are supported.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @lassoan (2020-02-10 19:59 UTC)

<p><code>MemoryError: std::bad_alloc: bad allocation</code> is the first serious error and it typically means that you run out of memory. How large the image is that you are trying to load?</p>
<p>There are lots of OpenGL errors in the log. What CPU and graphics card does this computer has?</p>
<p>Hundreds of issues have been fixed and improved since your Slicer version was released. Could you try if the most recent Slicer Preview Release works well?</p>

---

## Post #3 by @prorai (2020-02-12 07:17 UTC)

<p>Sounds Good, i’ll try to update the slicer version, and get back to you.</p>
<p>I’m using Xeon E5-2690.</p>
<p>thanks</p>

---

## Post #4 by @lassoan (2020-02-13 01:34 UTC)

<aside class="quote no-group" data-username="prorai" data-post="3" data-topic="10179">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/e8c25b/48.png" class="avatar"> prorai:</div>
<blockquote>
<p>I’m using Xeon E5-2690.</p>
</blockquote>
</aside>
<p>Sandy bridge processors were released almost 10 years ago. Slicer requires computers that are not older than about 6 years.</p>

---
