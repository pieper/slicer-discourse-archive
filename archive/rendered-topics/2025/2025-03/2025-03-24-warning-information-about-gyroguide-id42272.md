# Warning information about “Gyroguide“

**Topic ID**: 42272
**Date**: 2025-03-24
**URL**: https://discourse.slicer.org/t/warning-information-about-gyroguide/42272

---

## Post #1 by @doc-xie (2025-03-24 01:52 UTC)

<p>Hi everyone,<br>
In module “Gyroguide”, after the markers setting, click “calculate”, the warning information showed as below:Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-32448/GyroGuide/lib/Slicer-5.6/qt-scripted-modules/GyroGuide.py”, line 367, in onCalculateButtonClicked<br>
result = PuncturePlannerCalculator(markersFiducialsNode, targetFiducialNode, entryFiducialNode)<br>
File “/Applications/Slicer.app/Contents/Extensions-32448/GyroGuide/lib/Slicer-5.6/qt-scripted-modules/GyroGuide.py”, line 577, in <strong>init</strong><br>
for j in xrange(n):<br>
NameError: name ‘xrange’ is not defined<br>
What the reason about this problem and how to fix the issue?<br>
Best wishes,<br>
Xie</p>

---

## Post #2 by @pieper (2025-03-24 12:58 UTC)

<p>Hi <a class="mention" href="/u/doc-xie">@doc-xie</a>  - <code>xrange</code> was available in older Slicer versions that used Python2, but it’s not in Python3, so it should be <code>range</code> instead.  There’s some background on the transition here: <a href="https://discourse.slicer.org/t/updating-slicer-to-work-with-python-3/4662" class="inline-onebox">Updating slicer to work with python 3</a></p>

---

## Post #3 by @doc-xie (2025-03-25 02:58 UTC)

<p>Thanks Steve Pieper,<br>
I agree with you that the reason is the -xrange was not compatible with Python3. But I was confused with the transition. I want to know is there a easy way to solve the problem? The version of Python in my 3D Slicer is "3.9.10 (main, Apr  5 2024, 00:33:09) "<br>
Best wishes,<br>
Xie</p>

---

## Post #4 by @jamesobutler (2025-03-25 05:20 UTC)

<p>Hi Xie, it is definitely a developer task to make the code python 3 compatible. The easiest way for a developer to do this would be to utilize the pre-commit framework with a hook to run pyupgrade. That will then automatically apply fixes to upgrade the code syntax to a specific python version such as 3.9 as used by latest Slicer.</p>
<p>See for example this specification of pyupgrade in a pre-commit configuration file.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/6527a2660220a3beae41ad0f812e8e7cc25b4284/.pre-commit-config.yaml#L26">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/6527a2660220a3beae41ad0f812e8e7cc25b4284/.pre-commit-config.yaml#L26" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/6527a2660220a3beae41ad0f812e8e7cc25b4284/.pre-commit-config.yaml#L26" target="_blank" rel="noopener nofollow ugc">.pre-commit-config.yaml</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/6527a2660220a3beae41ad0f812e8e7cc25b4284/.pre-commit-config.yaml#L26" rel="noopener nofollow ugc"><code>6527a2660</code></a>
</div>



    <pre class="onebox"><code class="lang-yaml">
      <ol class="start lines" start="16" style="counter-reset: li-counter 15 ;">
          <li>      exclude: "\\.(svg|vtk|vtp)$"</li>
          <li>    - id: trailing-whitespace</li>
          <li>      exclude: "\\.(svg|vtk|vtp)$"</li>
          <li></li>
          <li>- repo: https://github.com/astral-sh/ruff-pre-commit</li>
          <li>  rev: v0.11.2</li>
          <li>  hooks:</li>
          <li>    - id: ruff</li>
          <li>      args: ["--fix", "--show-fixes"]</li>
          <li></li>
          <li class="selected">- repo: https://github.com/asottile/pyupgrade</li>
          <li>  rev: v3.19.1</li>
          <li>  hooks:</li>
          <li>    - id: pyupgrade</li>
          <li>      args: [--py39-plus]</li>
          <li></li>
          <li>- repo: https://github.com/pre-commit/mirrors-prettier</li>
          <li>  rev: "v4.0.0-alpha.8"</li>
          <li>  hooks:</li>
          <li>    - id: prettier</li>
          <li>      types_or: [yaml]</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Note that the GyroGuide extension hasn’t significantly been updated since 2015 which is a very long time. Do you know Luping Fang who appears to be the main developer of that extension?</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/lpfang/GyroGuide/commits/master/">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">

      <a href="https://github.com/lpfang/GyroGuide/commits/master/" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/f01fa09ea9581ed8cd2b86510c84ba155c1a9204736b713f80624c5a32d471f6/lpfang/GyroGuide" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/lpfang/GyroGuide/commits/master/" target="_blank" rel="noopener nofollow ugc">Commits · lpfang/GyroGuide</a></h3>

  <p>An python extension of 3D Slicer helps surgeons implement puncture orientation. - Commits · lpfang/GyroGuide</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @doc-xie (2025-03-27 02:49 UTC)

<p>Hi James Butler，<br>
I do not know LP Fang, but I will try to contact with him about this issue. Hope this problem can be solved in no time.<br>
Best wishes,<br>
Xie</p>

---
