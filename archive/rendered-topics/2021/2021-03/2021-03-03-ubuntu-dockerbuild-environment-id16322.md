---
topic_id: 16322
title: "Ubuntu Dockerbuild Environment"
date: 2021-03-03
url: https://discourse.slicer.org/t/16322
---

# Ubuntu dockerbuild environment

**Topic ID**: 16322
**Date**: 2021-03-03
**URL**: https://discourse.slicer.org/t/ubuntu-dockerbuild-environment/16322

---

## Post #1 by @RafaelPalomar (2021-03-03 07:28 UTC)

<p>Yesterday in the devs hangout we discussed about making a dockerbuild environment for testing 3D Slicer in newer Ubuntu distributions. I’ve looked at the existing <code>ubuntu-2004-gcc9/Dockerfile</code> and have a few questions:</p>
<ol>
<li>
<p>The existing Ubuntu environments in the current <a href="https://github.com/dockbuild/dockbuild/tree/b35d6d70e2b785d8dd5985422ddfd1fda8800909" rel="noopener nofollow ugc">dockbuild</a> all match <code>xx.04</code> releases.  Did I understand correctly that we want to prepare an <code>ubuntu-2010-gcc10</code> environment?</p>
</li>
<li>
<p>These environments come with a thin layer of core packages provided by the package-manager (e.g., <code>libssl-dev</code> and <code>curl</code>) and scripts to build/install some other packages (e.g., <code>install-cmake-binary.sh</code> and <code>build-and-install-git.sh</code>). Why do some packages rely on the package-manager while others don’t? Should the version of the scripted packages (e…g, <code>ARG CMAKE_VERSION=...</code> correspond to that of the packages in the package-manager?</p>
</li>
<li>
<p>There are some Slicer dependencies that are not considered in <code>dockbuild</code> (e.g., Qt). What to do with these?</p>
</li>
</ol>
<p>Thank you.</p>

---

## Post #2 by @pll_llq (2021-03-03 10:57 UTC)

<p>Hey <img src="https://emoji.discourse-cdn.com/twitter/wave.png?v=9" title=":wave:" class="emoji" alt=":wave:"></p>
<p>20.04 is an LST release and 20.10 will reach end of life in less than 6 months (July 2021 as said <a href="https://wiki.ubuntu.com/Releases" rel="noopener nofollow ugc">here</a>)</p>

---

## Post #3 by @Sam_Horvath (2021-03-03 14:48 UTC)

<p>For 3:</p>
<p>Once we have the dockbuild image set up, we will create an image for Slicer (see <a href="https://github.com/Slicer/SlicerBuildEnvironment" rel="noopener nofollow ugc">SlicerBuildEnvironment</a> ) that takes care of Qt.  The Qt stuff can be non-trivial, so if when you get to that point you find you are having issues, I can help out with that.</p>

---

## Post #4 by @jcfr (2021-03-03 15:46 UTC)

<aside class="quote no-group" data-username="RafaelPalomar" data-post="1" data-topic="16322">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>scripts to build/install some other packages</p>
</blockquote>
</aside>
<p>This scripts are copied from dockcross using <a href="https://github.com/dockbuild/dockbuild/blob/master/imagefiles/UpdateFromUpstream.sh">this script</a>.</p>
<p>There are useful to (for example) ensure we have a specific version of CMake available in all images.</p>
<p>If someone has bandwidth, it would be great to work on these issues as well:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/dockbuild/dockbuild/issues/67">
  <header class="source">

      <a href="https://github.com/dockbuild/dockbuild/issues/67" target="_blank" rel="noopener">github.com/dockbuild/dockbuild</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/dockbuild/dockbuild/issues/67" target="_blank" rel="noopener">Add support for versioning images</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-03-03" data-time="15:31:20" data-timezone="UTC">03:31PM - 03 Mar 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Similarly to dockcross, we should have tagged images with the following name `YY<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">YYMMDD-SHA{7}`

For reference, see https://github.com/dockcross/dockcross/blob/master/Makefile


![image](https://user-images.githubusercontent.com/219043/109829449-89019980-7c0b-11eb-81a6-49bb931a04eb.png)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubissue" data-onebox-src="https://github.com/dockbuild/dockbuild/issues/68">
  <header class="source">

      <a href="https://github.com/dockbuild/dockbuild/issues/68" target="_blank" rel="noopener">github.com/dockbuild/dockbuild</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/dockbuild/dockbuild/issues/68" target="_blank" rel="noopener">Update CMake version to 3.19.6</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-03-03" data-time="15:31:55" data-timezone="UTC">03:31PM - 03 Mar 21 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2022-01-21" data-time="07:56:03" data-timezone="UTC">07:56AM - 21 Jan 22 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubissue" data-onebox-src="https://github.com/dockbuild/dockbuild/issues/69">
  <header class="source">

      <a href="https://github.com/dockbuild/dockbuild/issues/69" target="_blank" rel="noopener">github.com/dockbuild/dockbuild</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/dockbuild/dockbuild/issues/69" target="_blank" rel="noopener">Evaluate transition to GitHub action</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-03-03" data-time="15:36:36" data-timezone="UTC">03:36PM - 03 Mar 21 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2021-03-12" data-time="15:29:49" data-timezone="UTC">03:29PM - 12 Mar 21 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">See https://github.com/dockcross/dockcross/blob/master/.github/workflows/main.ym<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">l</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
