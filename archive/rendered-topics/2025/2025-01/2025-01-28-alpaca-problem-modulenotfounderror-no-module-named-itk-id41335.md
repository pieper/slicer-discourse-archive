---
topic_id: 41335
title: "Alpaca Problem Modulenotfounderror No Module Named Itk"
date: 2025-01-28
url: https://discourse.slicer.org/t/41335
---

# ALPACA problem: ModuleNotFoundError: No module named 'itk'

**Topic ID**: 41335
**Date**: 2025-01-28
**URL**: https://discourse.slicer.org/t/alpaca-problem-modulenotfounderror-no-module-named-itk/41335

---

## Post #1 by @nightmare (2025-01-28 12:41 UTC)

<p>Hi, how can I solve this problem?<br>
alpaca does not descend and does not open.</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/İhsanBeratKILIÇLI/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/ALPACA.py”, line 126, in setup<br>
import itk<br>
ModuleNotFoundError: No module named ‘itk’</p>

---

## Post #2 by @muratmaga (2025-01-28 14:24 UTC)

<aside class="quote no-group" data-username="nightmare" data-post="1" data-topic="41335">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nightmare/48/79252_2.png" class="avatar"> nightmare:</div>
<blockquote>
<p>File “C:/Users/İhsanBeratKILIÇLI/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/ALPACA.py”, line 126, in setup</p>
</blockquote>
</aside>
<p>This should work, as we routinely use ALPACA on windows with v5.6.2. Can you try to install Slicer in a path that doesn’t have Turkish characters? Something like <code>C:/Slicer-5.6.2</code> and then try installing SlicerMorph and running ALPACA?</p>

---

## Post #3 by @muratmaga (2025-01-28 15:06 UTC)

<p>actually I am seeing an issue with itk libraries missing on Mac too.</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/Extensions-33216/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/ALPACA.py", line 105, in setup
    from itk import Fpfh
ImportError: cannot import name 'Fpfh' from 'itk' (/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/itk/__init__.py)
</code></pre>
<p><a class="mention" href="/u/dzenanz">@dzenanz</a> do you have thoughts on this?</p>

---

## Post #4 by @dzenanz (2025-01-28 15:10 UTC)

<p>We probably need <code>pip install itk-fpfh</code> somewhere.</p>

---

## Post #5 by @muratmaga (2025-01-28 15:32 UTC)

<aside class="quote no-group" data-username="dzenanz" data-post="4" data-topic="41335">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/dzenanz/48/1992_2.png" class="avatar"> dzenanz:</div>
<blockquote>
<p>itk-fpfh</p>
</blockquote>
</aside>
<p>It is supposed to be installed:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/17bae274129a763f41951512fece68b413d6e076/ALPACA/ALPACA.py#L120">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/17bae274129a763f41951512fece68b413d6e076/ALPACA/ALPACA.py#L120" target="_blank" rel="noopener nofollow ugc">github.com/SlicerMorph/SlicerMorph</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/17bae274129a763f41951512fece68b413d6e076/ALPACA/ALPACA.py#L120" target="_blank" rel="noopener nofollow ugc">ALPACA/ALPACA.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerMorph/SlicerMorph/blob/17bae274129a763f41951512fece68b413d6e076/ALPACA/ALPACA.py#L120" rel="noopener nofollow ugc"><code>17bae2741</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="110" style="counter-reset: li-counter 109 ;">
          <li>if needInstall:</li>
          <li>    progressDialog = slicer.util.createProgressDialog(</li>
          <li>        windowTitle="Installing...",</li>
          <li>        labelText="Installing ALPACA Python packages. This may take a minute...",</li>
          <li>        maximum=0,</li>
          <li>    )</li>
          <li>    slicer.app.processEvents()</li>
          <li>    try:</li>
          <li>        slicer.util.pip_install(["itk~=5.4.0"])</li>
          <li>        slicer.util.pip_install(["scikit-learn"])</li>
          <li class="selected">        slicer.util.pip_install(["itk-fpfh~=0.2.0"])</li>
          <li>        slicer.util.pip_install(["itk-ransac~=0.2.1"])</li>
          <li>        slicer.util.pip_install(f"cpdalp")</li>
          <li>    except:</li>
          <li>        slicer.util.infoDisplay("Issue while installing the ITK Python packages")</li>
          <li>        progressDialog.close()</li>
          <li>    import itk</li>
          <li></li>
          <li>    fpfh = itk.Fpfh.PointFeature.MF3MF3.New()</li>
          <li>    progressDialog.close()</li>
          <li></li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Likewise on Windows 5.6.2 the error is missing the ITK library, which was never an issue before.</p>

---

## Post #6 by @nightmare (2025-02-07 13:46 UTC)

<p>I’m sorry, I was on vacation and couldn’t check your answers. The problem was solved when I installed it without Turkish characters. <a class="mention" href="/u/dzenanz">@dzenanz</a><br>
I would also like to give additional information: Version of Windows users must also be active.</p>

---
