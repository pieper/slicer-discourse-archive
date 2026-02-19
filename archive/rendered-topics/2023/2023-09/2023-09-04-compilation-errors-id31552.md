---
topic_id: 31552
title: "Compilation Errors"
date: 2023-09-04
url: https://discourse.slicer.org/t/31552
---

# Compilation errors

**Topic ID**: 31552
**Date**: 2023-09-04
**URL**: https://discourse.slicer.org/t/compilation-errors/31552

---

## Post #1 by @iwangwangwang (2023-09-04 15:46 UTC)

<p>After going through countless hardships, I have finally solved most of the compilation problems, but there are still some problems that are difficult for me. I would like to ask how to solve these problems?</p>
<ol>
<li>
<p>in ITK project<br>
itkAffineTransform.hxx(294): error C2244: “slicer_itk::AffineTransform&lt;TParametersValueType,VDimension&gt;::Metric”: Cannot match function definition with existing declaration<br>
… a lot of C2244 error</p>
</li>
<li>
<p>in ITK project<br>
itkInterpolateImageFunction.h(79): error C2653: “InputImageType”: Not a class or namespace name<br>
…a lot of C2653 error</p>
</li>
<li>
<p>in ITK project<br>
itkCenteredSimilarity2DTransform.h(99): error C2146: Syntax error: Missing ‘;’<br>
…a lot of C2146 error</p>
</li>
<li>
<p>in ITK project<br>
itkCenteredSimilarity2DTransform.h(99): error C4430: Missing type descriptor - assumed to be int. Note: C++does not support default ints</p>
</li>
</ol>
<p>there were many errors<br>
sincerely for help</p>

---

## Post #2 by @jamesobutler (2023-09-04 16:08 UTC)

<p>Can you provide information on the following?</p>
<ul>
<li>
<p>What OS version are you using? e.g. Windows 11 Pro 22H2</p>
</li>
<li>
<p>What version of the application are you using to compile Slicer? e.g. Visual Studio 2022 17.7.3 Community edition</p>
</li>
<li>
<p>What version of CMake are you using? e.g. CMake 3.27.4</p>
</li>
<li>
<p>What version of Slicer are you trying to build? Latest <code>main</code> or a git tag like <code>v5.4.0</code>?</p>
</li>
</ul>
<p>Any other non-standard build options that you are using?</p>

---

## Post #4 by @iwangwangwang (2023-09-05 00:54 UTC)

<p>Here are some information you mentioned：<br>
OS: windows11 professional 22H2<br>
compiler: visual studio 2017 enterprise edition 15.9.56<br>
CMake: 3.26.0<br>
Slicer: latest main unknown version<br>
Qt: 5.15.2<br>
git: 2.42.0 windows.2<br>
python: 3.9<br>
A key point： set _LINKER_FLAGS_DEBUG /INCREMENT:NO</p>
<p>Hope the above information can help you understand my problem</p>

---

## Post #5 by @lassoan (2023-09-05 16:47 UTC)

<aside class="quote no-group" data-username="iwangwangwang" data-post="4" data-topic="31552">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/f1d935/48.png" class="avatar"> iwangwangwang:</div>
<blockquote>
<p>visual studio 2017 enterprise edition 15.9.56</p>
</blockquote>
</aside>
<p>VS2017 may be too old for building ITK.</p>

---

## Post #6 by @jamesobutler (2023-09-05 16:54 UTC)

<p>Visual Studio 2017 is not tested anymore as mentioned in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#install-prerequisites" class="inline-onebox" rel="noopener nofollow ugc">Windows — 3D Slicer documentation</a>. Maybe something has changed in the dependency tree and we will need to update that note in the build instructions. The Slicer ITK version says that Visual Studio 15.7 with the v141 toolset or later should work as it conformed to the C++11/14/17 standard.</p>
<p>Would you be able to download and install Visual Studio 2022 and use its default v143 toolset instead?</p>

---

## Post #7 by @jamesobutler (2023-09-05 16:57 UTC)

<p>Also note that ITK has removed support for Visual Studio 2017 in <code>v5.4rc01</code>. Slicer updates the ITK version that it uses every so often, so Visual Studio 2017 will likely be dropped in Slicer soon as well.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/InsightSoftwareConsortium/ITK/commit/140f3c249fbb20c4f4a1607e563e19ee9a9cbd78">
  <header class="source">

      <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/140f3c249fbb20c4f4a1607e563e19ee9a9cbd78" target="_blank" rel="noopener nofollow ugc">github.com/InsightSoftwareConsortium/ITK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/140f3c249fbb20c4f4a1607e563e19ee9a9cbd78" target="_blank" rel="noopener nofollow ugc">ENH: Drop support for MSVC toolset v141 aka Visual Studio 2017</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-05-02" data-time="15:01:45" data-timezone="UTC">03:01PM - 02 May 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/dzenanz" target="_blank" rel="noopener nofollow ugc">
          <img alt="dzenanz" src="https://avatars.githubusercontent.com/u/1792121?v=4" class="onebox-avatar-inline" width="20" height="20">
          dzenanz
        </a>
      </div>

      <div class="lines" title="changed 3 files with 6 additions and 10 deletions">
        <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/140f3c249fbb20c4f4a1607e563e19ee9a9cbd78" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+6</span>
          <span class="removed">-10</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Enabling C++17 broke VS2017 due to its numerous bugs. See discussion:
https://di<span class="show-more-container"><a href="https://github.com/InsightSoftwareConsortium/ITK/commit/140f3c249fbb20c4f4a1607e563e19ee9a9cbd78" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">scourse.itk.org/t/c-17-breaks-visual-studio-2017-drop-support/5884</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @iwangwangwang (2023-09-05 18:33 UTC)

<p>Roger that, by the way，Slicer 5.4 or lower version has the same requirements?<br>
maybe I want to compile a lower version which is more convenience.</p>

---

## Post #9 by @iwangwangwang (2023-09-05 18:36 UTC)

<p>Is the version of ITK associated with the version of Slicer？ what about compiling a lower version of Slicer with VS2017</p>

---

## Post #10 by @pieper (2023-09-05 18:46 UTC)

<p>We suggest you try to stick as close to the latest releases of everything as possible and not rely on older versions or compilers or you are likely to get stuck and not get any new fixes or features.  Of course we don’t break things on purpose but often there are good reasons why people drop support for old compilers.</p>

---

## Post #11 by @jamesobutler (2023-09-05 18:47 UTC)

<p>Yes the ITK version is associated with the Slicer version. Slicer has required C++17 starting with Slicer 5.2.0 so you would have to go all the way back to the Slicer 5.0.x series of code to likely compile successfully using Visual Studio 2017. I would highly discourage this if you’re able to download and install Visual Studio 2022.</p>
<p>Slicer 5.0.x was released 1.5 years ago and you won’t get all the improvements and bug fixes since then unless you spend time trying to backport small changes. Since Slicer developers have limited resources generally we can only support efforts for the latest Slicer Stable (currently 5.4.0) or the latest Slicer preview.</p>

---

## Post #12 by @iwangwangwang (2023-09-05 19:01 UTC)

<p>Okay, I will follow your suggestions, thanks^-^</p>

---

## Post #13 by @iwangwangwang (2023-09-05 19:03 UTC)

<p>Okay, I understand. Thank you for your help <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>

---
