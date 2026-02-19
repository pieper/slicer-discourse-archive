---
topic_id: 13870
title: "Open3D Worked Within Slicer Until Revision 29392"
date: 2020-10-05
url: https://discourse.slicer.org/t/13870
---

# Open3d worked within slicer until revision 29392

**Topic ID**: 13870
**Date**: 2020-10-05
**URL**: https://discourse.slicer.org/t/open3d-worked-within-slicer-until-revision-29392/13870

---

## Post #1 by @agporto (2020-10-05 18:29 UTC)

<p>SlicerMorph has the open3d==0.9.0 dependency, which was working well within Slicer (Linux) until revision 29392 came along. The last revision in which it worked was 29389.<br>
Now, it throws out the following error:</p>
<p>Traceback (most recent call last):<br>
File “/home/maga/.config/NA-MIC/Extensions-29402/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/ALPACA.py”, line 51, in <strong>init</strong><br>
import open3d as o3d<br>
ModuleNotFoundError: No module named ‘open3d’<br>
During handling of the above exception, another exception occurred:<br>
Traceback (most recent call last):<br>
File “/home/maga/.config/NA-MIC/Extensions-29402/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/ALPACA.py”, line 57, in <strong>init</strong><br>
import open3d as o3d<br>
File “/home/maga/Downloads/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/site-packages/open3d/<strong>init</strong>.py”, line 35, in <br>
from .open3d import * # py2 py3 compatible<br>
ImportError: /lib64/libstdc++.so.6: version `CXXABI_1.3.8’ not found (required by /home/maga/Downloads/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/site-packages/open3d/open3d.cpython-36m-x86_64-linux-gnu.so)<br>
qSlicerPythonCppAPI::instantiateClass  - [ “ALPACAWidget” ] - Failed to instantiate scripted pythonqt class “ALPACAWidget” 0x25e32f8<br>
Warning, the module  “ALPACA” has no widget representation<br>
Warning, there is no UI for the module “ALPACA”</p>
<p>The key problem seems to be associated with this line:<br>
ImportError: /lib64/libstdc++.so.6: version `CXXABI_1.3.8’ not found</p>
<p>I looked at the commits around that time and couldn’t see anything that would justify this error. Any ideas?</p>

---

## Post #2 by @pieper (2020-10-05 18:33 UTC)

<p>Sounds like that’s related to a change in the open3d binary version itself.  Did you try pip_installing it on an earlier version of Slicer?</p>

---

## Post #3 by @agporto (2020-10-05 18:35 UTC)

<p>Yeah…it works fine on Slicer revision 29389</p>

---

## Post #4 by @agporto (2020-10-05 18:43 UTC)

<p>Since I am using pip archived versions (from late 2019), shouldn’t the source of the issue be change within Slicer itself ? If I can pip install the same open3d version on Slicer revision 29389, but not on Slicer revision 29392, wouldn’t that suggest that some change within Slicer caused the break?</p>

---

## Post #5 by @lassoan (2020-10-05 19:37 UTC)

<p>There does not seem to be any commits that could cause the ABI incompatibility issue. It is more likely to be caused by build toolset or configuration update on the Linux factory machine.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> was there any update or configuration change on the Linux factory machine around September 28?</p>
<p>Updating to a more recent version of open3d or building open3d locally might solve the problem.</p>

---

## Post #6 by @Sam_Horvath (2020-10-05 19:59 UTC)

<p>The factory image was updated to support Qt. 5.15.1  This is all that changed in our Dockerfile, but would have pulled the latest upstream images:<br>
</p><aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/SlicerBuildEnvironment/commit/806cba73d276fe9f4bc1ceb4f287d1b53bac3214" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/SlicerBuildEnvironment</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/SlicerBuildEnvironment/commit/806cba73d276fe9f4bc1ceb4f287d1b53bac3214" target="_blank" rel="noopener nofollow ugc">Merge pull request #17 from Slicer/update-to-qt-5.15.1</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2020-09-29" data-time="02:28:13" data-timezone="UTC">02:28AM - 29 Sep 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener nofollow ugc">
          <img alt="jcfr" src="https://avatars0.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
        
      </div>

      <div class="lines" title="changed 3 files with 13 additions and 13 deletions">
        <a href="https://github.com/Slicer/SlicerBuildEnvironment/commit/806cba73d276fe9f4bc1ceb4f287d1b53bac3214" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+13</span>
          <span class="removed">-13</span>
        </a>
      </div>
    </div>

  </div>
</div>


  <div class="github-row">
    <pre class="github-content" style="white-space: normal;">qt5-centos7: Update from Qt 5.15.0 to 5.15.1</pre>
  </div>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Notable changes in upstream:<br>
</p><aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/dockbuild/dockbuild/commit/8858cab34da5076e4fcc7870a8666cbc1f9c8bad#diff-9ad1c378c7531a28355e167d166e0271" target="_blank" rel="noopener nofollow ugc">github.com/dockbuild/dockbuild</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/dockbuild/dockbuild/commit/8858cab34da5076e4fcc7870a8666cbc1f9c8bad" target="_blank" rel="noopener nofollow ugc">centos7-devtoolset4-gcc5: Fix devtoolset-4 install using vault.centos.org</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2020-05-07" data-time="06:09:22" data-timezone="UTC">06:09AM - 07 May 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener nofollow ugc">
          <img alt="jcfr" src="https://avatars0.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
        
      </div>

      <div class="lines" title="changed 1 files with 10 additions and 0 deletions">
        <a href="https://github.com/dockbuild/dockbuild/commit/8858cab34da5076e4fcc7870a8666cbc1f9c8bad" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+10</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>

  </div>
</div>


  <div class="github-row">
    <pre class="github-content" style="white-space: normal;">Use "7.6.1810" because it is the most recent directory including "devtoolset-4/",
the newer "7.7.1908" and "7.8.2003" didn't seem to have the packages....</pre>
  </div>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Nothing should have changed about the toolset however, just the package source.</p>

---

## Post #7 by @agporto (2020-10-05 21:06 UTC)

<p>Dear Sam and Andras,<br>
Thanks for checking it out. We haven’t figure out yet what is the source of the problem, but these links will give us a good starting point.<br>
Thanks again,<br>
Arthur</p>

---

## Post #8 by @lassoan (2020-10-06 19:45 UTC)

<p>It seems that Open3D developers deliberately choose an old C++ ABI. This page may contain useful information: <a href="http://www.open3d.org/docs/release/compilation.html#jupyter-visualization-widgets-support-experimental">http://www.open3d.org/docs/release/compilation.html#jupyter-visualization-widgets-support-experimental</a></p>

---

## Post #9 by @agporto (2020-10-06 19:54 UTC)

<p>Yeah, that is where I am as well. I was trying to build a manylinux wheel with a different ABI that would work across a broad range of linux flavors, but it still doesn’t seem to solve the problem (or I messed up somewhere). The error I shared yesterday was captured by Murat on a CentOs machine. But on my ubuntu laptop I don’t actually get any error in the error log. Slicer simply crashes and the last entry in the error log is the ‘Welcome’ screen entry. Interestingly, if I open SlicerPython (ie., without a GUI), I can  import open3d with no problems. It seems that the source of the problem only occurs when loading the UI. Which again might indicate that something about the Qt upgrade was really the source of the issue.</p>

---

## Post #10 by @agporto (2020-10-06 19:57 UTC)

<p>The “good” news is that it doesn’t seem to impact Mac OSX and Windows. It is a linux-specifc problem.</p>

---

## Post #11 by @lassoan (2020-10-06 20:06 UTC)

<p>Yes, Windows is using Universal C Runtime since 2015, which preserves ABI compatibility across all versions. One less thing that can break.</p>

---
