# Report: if Slicer's super build dir is in a softly linked dir

**Topic ID**: 9001
**Date**: 2019-11-03
**URL**: https://discourse.slicer.org/t/report-if-slicers-super-build-dir-is-in-a-softly-linked-dir/9001

---

## Post #1 by @gaoyi.cn (2019-11-03 03:42 UTC)

<p>Dear All,</p>
<p>I’m doing a case report on building slicer in a soft-ly linked dir.</p>
<p>I have two hard drives with typical config: one fast and small, one big and slow.<br>
My home dir is on the fast disk, mounted at:<br>
/home/gaoyi</p>
<p>The big disk is mounted at:<br>
/media/gaoyi/data</p>
<p>I have a softlink in my home dir to the big disk:<br>
/home/gaoyi/big  → /media/gaoyi/data/gaoyi/</p>
<p>I put Slicer on the big disk:<br>
/media/gaoyi/data/gaoyi/namic/rls20191103/Slicer<br>
so it’s also:<br>
/home/gaoyi/big/namic/rls20191103/Slicer</p>
<p>I then did all the operation in the soft-ly linked foler, like mkdir for the super-build<br>
/home/gaoyi/big/namic/rls20191103/Slicer-sb</p>
<p>But building gives errors from python, like:</p>
<hr>
<p>CMake Error at /home/pv/usr/work/namic/rls20191103/sb-rls/python-pythonqt-requirements-prefix/src/python-pythonqt-requirements-stamp/python-pythonqt-requirements-install-Release.cmake:49 (message):<br>
Command failed: 1</p>
<p>‘/home/pv/usr/work/namic/rls20191103/sb-rls/python-install/bin/PythonSlicer’ ‘-m’ ‘pip’ ‘install’ ‘–require-hashes’ ‘-r’ ‘/home/pv/usr/work/namic/rls20191103/sb-rls/python-pythonqt-requirements-requirements.txt’</p>
<p>See also</p>
<pre><code>/home/pv/usr/work/namic/rls20191103/sb-rls/python-pythonqt-requirements-prefix/src/python-pythonqt-requirements-stamp/python-pythonqt-requirements-install-*.log
</code></pre>
<p>CMakeFiles/python-pythonqt-requirements.dir/build.make:74: recipe for target ‘python-pythonqt-requirements-prefix/src/python-pythonqt-requirements-stamp/python-pythonqt-requirements-install’ failed<br>
make[2]: *** [python-pythonqt-requirements-prefix/src/python-pythonqt-requirements-stamp/python-pythonqt-requirements-install] Error 1<br>
CMakeFiles/Makefile2:257: recipe for target ‘CMakeFiles/python-pythonqt-requirements.dir/all’ failed<br>
make[1]: *** [CMakeFiles/python-pythonqt-requirements.dir/all] Error 2<br>
make[1]: *** Waiting for unfinished jobs…<br>
CMake Error at /home/pv/usr/work/namic/rls20191103/sb-rls/python-dicom-requirements-prefix/src/python-dicom-requirements-stamp/python-dicom-requirements-install-Release.cmake:49 (message):<br>
Command failed: 1</p>
<hr>
<p>By looking into the log files, and calling the lsb_release file in the Super-build/python-install/bin/lsb_release, I got the error:</p>
<blockquote>
<p>python-install/bin/lsb_release -a<br>
error: Application does NOT exists [/media/pv/data/pv/usr/work/namic/rls20191103/sb-rls/python-install/bin/…/…/…/…/…/…/…/…/…/usr/bin/./lsb_release]</p>
</blockquote>
<p>Looks like it’s trying to find the system’s lsb_release at: /usr/bin/lsb_release<br>
But, the number of  “…/”  is not correct. I believe this is because the soft link.</p>
<p><strong>Solution seems simple: just build in the “real location”.</strong></p>

---

## Post #2 by @gaoyi.cn (2019-11-03 05:12 UTC)

<p>Hi Andras, <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>It seems that the recent commit:<br>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/commit/73f2afcd2f41040749da0e520b35f2841315ac86" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/73f2afcd2f41040749da0e520b35f2841315ac86" target="_blank" rel="nofollow noopener">COMP: Install pip, setuptools, wheel using whl files</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2019-11-01" data-time="05:01:23" data-timezone="UTC">05:01AM - 01 Nov 19 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="nofollow noopener">
          <img alt="jamesobutler" src="https://avatars1.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
        
      </div>

      <div class="lines" title="changed 6 files with 89 additions and 56 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/73f2afcd2f41040749da0e520b35f2841315ac86" target="_blank" rel="nofollow noopener">
          <span class="added">+89</span>
          <span class="removed">-56</span>
        </a>
      </div>
    </div>

  </div>
</div>


  <div class="github-row">
    <pre class="github-content" style="white-space: normal;">svn-url: http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28580
git-svn-id: http://svn.slicer.org/Slicer4/trunk@28580 3bd1e089-480b-0410-8dfb-8563597acbee</pre>
  </div>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>may be caused by a combination of factors of this, and also the openssl, curl  issues.</p>
<p>I tested without that particular commit and Slicer builds well.</p>
<p>Of course, there may be other reasons for that commit and i’m not aware of.</p>

---

## Post #3 by @lassoan (2019-11-04 02:17 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> is still working on this. It looks like that things should clear up within a couple of days (see <a href="https://github.com/Slicer/Slicer/pulls/jamesobutler">these recent pull requests</a>).</p>

---

## Post #4 by @gaoyi.cn (2019-11-14 11:16 UTC)

<p>I tested the master commit today and build Slicer in the absolute path (not soft link dir). It builds. But will give immediate crashing error when launching Slicer. With the change of openssl and curl (in the pull request), I believe the problem is solved (also the soft link problem is also solved. now building in soft link dir is fine too).</p>

---

## Post #5 by @jcfr (2019-11-14 14:22 UTC)

<aside class="quote no-group quote-modified" data-username="gaoyi.cn" data-post="4" data-topic="9001">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gaoyi.cn/48/1422_2.png" class="avatar"> gaoyi.cn:</div>
<blockquote>
<p>With the change of openssl and curl […] I believe the problem is solved</p>
</blockquote>
</aside>
<p>Thanks for the update, we will review and work on integrating the changes associated with <a href="https://github.com/Slicer/Slicer/pull/1260" class="inline-onebox">when adding a second fiducial to the annotationfiducialslist, tractography fiducial seeding works only with the first one. · Issue #1260 · Slicer/Slicer · GitHub</a></p>
<p>In the mean time, do you have issue running the “preview” build available at <a href="https://download.slicer.org">https://download.slicer.org</a></p>

---
