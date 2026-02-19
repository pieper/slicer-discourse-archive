---
topic_id: 2765
title: "Access Slicer Modules And Libraries In Pycharm"
date: 2018-05-06
url: https://discourse.slicer.org/t/2765
---

# Access slicer modules and libraries in pycharm

**Topic ID**: 2765
**Date**: 2018-05-06
**URL**: https://discourse.slicer.org/t/access-slicer-modules-and-libraries-in-pycharm/2765

---

## Post #1 by @hadasara (2018-05-06 20:27 UTC)

<p>Hi,<br>
I’d like to know why when I try to call slicer modules\libraries (vtk, numpy), they are not recognized, unless I’m in the remote-debug mode, and run some loadable module, while there is a breakpoint somewhere in the code:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5aee56f6a3bde3425b9987ec1381f0d8b0653b39.png" alt="image" data-base62-sha1="cYpBZA6Mr0Z2zPMti8xsv1E4IDn" width="614" height="294"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5579590acf8383dae2823cd5052e3438c09b8fbb.png" alt="image" data-base62-sha1="cc8zqPvNOGL7QA08F3oRvN4PNtF" width="611" height="351"></p>
<p>What path should I add to the python search path? and how it is different in the different modes?</p>
<p>Thanks!!</p>

---

## Post #2 by @lassoan (2018-05-07 13:58 UTC)

<p>Slicer is not a Python interpreter extended by Python libraries, but an application that embeds Python. The difference is explained here: <a href="https://docs.python.org/2/extending/embedding.html">https://docs.python.org/2/extending/embedding.html</a></p>
<p>The consequence is that you cannot run Slicer from any generic Python interpreter, such as the one started by the PyCharm IDE. You can only load some of the libraries, such as VTK or SimpleITK into any Python interpreter (and it should not be too difficult to make the core MRML library and some other parts loadable as well). However, in general, to access all Slicer classes, you always need to start Slicer application and then connect to Slicer’s built-in Python interpreter.</p>

---

## Post #3 by @ihnorton (2018-05-15 19:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2765">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>it should not be too difficult to make the core MRML library and some other parts loadable as well</p>
</blockquote>
</aside>
<p>There may still be some other modules we need to exclude, but the following PR allows to safely <code>import slicer</code> in the regular python(.exe) binary included with Slicer:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/945">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/945" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/945" target="_blank" rel="noopener">Nightlies hang on linux / ubuntu 10.04 and others</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:34:56" data-timezone="UTC">10:34PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:34:56" data-timezone="UTC">10:34PM - 12 Mar 20 UTC</span>
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
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=945). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>However, note that the <code>python</code> binary must either be started from the launcher or from a shell with with the <a href="https://discourse.slicer.org/t/python-real-different-from-python-interpreter/2496/5">necessary environment variables</a>.</p>

---

## Post #4 by @lassoan (2018-05-15 19:38 UTC)

<p>Thanks for the information <a class="mention" href="/u/ihnorton">@ihnorton</a>, this will be very useful.</p>
<p>I see that some Slicer Qt widget modules had to be excluded. Do you know why they caused crash?</p>
<p>Can we still access MRML widgets and various custom Qt widgets defined in Slicer modules?</p>

---

## Post #5 by @ihnorton (2018-05-15 19:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="2765">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I see that some Slicer Qt widget modules had to be excluded. Do you know why they caused crash?</p>
</blockquote>
</aside>
<p>PythonQt shared libraries try to access <code>PythonQt::self</code> singleton (or something with a similar name) during shared library loading, but it is not initialized.</p>
<blockquote>
<p>Can we still access MRML widgets and various custom Qt widgets defined in Slicer modules?</p>
</blockquote>
<p>No, right now anything Qt has to be excluded. There is a <a href="https://sourceforge.net/p/pythonqt/discussion/631393/thread/ec93fba5/">discussion</a> on the PythonQt forum about what would be required to use PythonQt that way – we would need a wrapper shim that initializes PythonQt and sets up the event loop. For now my use-case is Python-based CLI.</p>

---
