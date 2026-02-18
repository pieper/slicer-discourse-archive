# Shape variation analyzer

**Topic ID**: 23836
**Date**: 2022-06-12
**URL**: https://discourse.slicer.org/t/shape-variation-analyzer/23836

---

## Post #1 by @lili-yu22 (2022-06-12 01:42 UTC)

<p>Systerm：win10，slicer5.1.0<br>
l have installed the extension shape variation analyzer，but it shows not loaded，the python interactor shows module not found error：no module named joblib，can you give me some guidelines?</p>

---

## Post #2 by @mau_igna_06 (2022-06-12 09:47 UTC)

<p>maybe you could try pip_install(‘joblib’)</p>
<p>hopw it helps</p>

---

## Post #3 by @lili-yu22 (2022-06-12 11:34 UTC)

<p>thank you，but follow your advice，it shows “no module named threadpoolctl”，then l install the“threadpoolctl”it still failed. l uninstall the extension，want to install again，now l even can’t install the extension，how can i do</p>

---

## Post #4 by @mau_igna_06 (2022-06-12 12:03 UTC)

<p>Try reinstalling slicer latest version and trying again</p>

---

## Post #5 by @jamesobutler (2022-06-12 18:11 UTC)

<p><a class="mention" href="/u/lili-yu22">@lili-yu22</a> I installed Shape Variation Analyzer using Slicer 5.0.2 through the Extensions Manager on Windows and it included joblib and threadpoolctl. How did you install the extension? Through the Extensions Manager? Installing from file? Cloning from GitHub and building from source?</p>

---

## Post #6 by @lili-yu22 (2022-06-13 00:55 UTC)

<p>through the extension manager，now I can’t download it</p>

---

## Post #7 by @lili-yu22 (2022-06-13 01:56 UTC)

<p>now，according your advice after install threadpoolctl，it success，i found at night it always failed，at day time，it success，l don’t know why it happen</p>

---

## Post #8 by @SlicerBP (2022-11-27 15:34 UTC)

<p>I have the same problem. Shape variation analyzer does not work! Slicer 5.0.2</p>
<p>Python 3.9.10 (main, May  6 2022, 03:14:57) [MSC v.1930 64 bit (AMD64)] on win32</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>C:\Users\bp\AppData\Local\NA-MIC\Slicer 5.0.2\NA-MIC\Extensions-30822\ShapeVariationAnalyzer\lib\Slicer-5.0\qt-scripted-modules\shapepcalib.py:811: SyntaxWarning: “is” with a literal. Did you mean “==”?<br>
if (len(y_design) is 0):<br>
C:\Users\bp\AppData\Local\NA-MIC\Slicer 5.0.2\NA-MIC\Extensions-30822\ShapeVariationAnalyzer\lib\Slicer-5.0\qt-scripted-modules\shapepcalib.py:820: SyntaxWarning: “is not” with a literal. Did you mean “!=”?<br>
if len(y_design) is not 0:<br>
C:\Users\bp\AppData\Local\NA-MIC\Slicer 5.0.2\NA-MIC\Extensions-30822\ShapeVariationAnalyzer\lib\Slicer-5.0\qt-scripted-modules\cpns\cpns.py:57: SyntaxWarning: “is” with a literal. Did you mean “==”?<br>
if len(self.fileList) is 0:</p>

---

## Post #9 by @lassoan (2022-11-27 16:12 UTC)

<aside class="quote no-group" data-username="SlicerBP" data-post="8" data-topic="23836">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/848f3c/48.png" class="avatar"> SlicerBP:</div>
<blockquote>
<p>I have the same problem. Shape variation analyzer does not work! Slicer 5.0.2</p>
</blockquote>
</aside>
<p>Please use the latest Slicer Stable Release (currently 5.0.3, in a few days 5.2.x) or the latest Slicer Preview Release (currently 5.3.x).</p>

---

## Post #10 by @SlicerBP (2022-12-03 20:11 UTC)

<p>Hi, thank you for your reply! However, I have still the same problem:</p>
<blockquote>
<p>C:\Usersbp\AppData\Local\NA-MIC\Slicer 5.2.1\NA-MIC\Extensions-31317\ShapeVariationAnalyzer\lib\Slicer-5.2\qt-scripted-modules\cpns\cpns.py:57: SyntaxWarning: “is” with a literal. Did you mean “==”?<br>
if len(self.fileList) is 0:<br>
File “”, line 1<br>
==<br>
^<br>
SyntaxError: invalid syntax</p>
</blockquote>
<p>ShapeVariationAnalyzer does not work!</p>

---

## Post #11 by @jamesobutler (2022-12-03 20:55 UTC)

<p>That is just a warning and not an error. I issued a PR to fix these warnings in ShapeVariationAnalyzer back in June, but the developers of that extension haven’t responded to integrate the change.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/DCBIA-OrthoLab/ShapeVariationAnalyzer/pull/65">
  <header class="source">

      <a href="https://github.com/DCBIA-OrthoLab/ShapeVariationAnalyzer/pull/65" target="_blank" rel="noopener nofollow ugc">github.com/DCBIA-OrthoLab/ShapeVariationAnalyzer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/DCBIA-OrthoLab/ShapeVariationAnalyzer/pull/65" target="_blank" rel="noopener nofollow ugc">Add pre_commit framework checking and upgrade python syntax to latest</a>
      </h4>

    <div class="branches">
      <code>DCBIA-OrthoLab:master</code> ← <code>jamesobutler:syntax-upgrade</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2022-06-12" data-time="18:36:07" data-timezone="UTC">06:36PM - 12 Jun 22 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
            <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
            jamesobutler
          </a>
        </div>

        <div class="lines" title="4 commits changed 25 files with 41 additions and 70 deletions">
          <a href="https://github.com/DCBIA-OrthoLab/ShapeVariationAnalyzer/pull/65/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+41</span>
            <span class="removed">-70</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">I observed these syntax warnings in https://slicer.cdash.org/test/22434929 where<span class="show-more-container"><a href="https://github.com/DCBIA-OrthoLab/ShapeVariationAnalyzer/pull/65" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden"> Slicer is using Python 3.9 now.

```
/Volumes/D/P/S-0-E-b/ShapeVariationAnalyzer-build/inner-build/lib/Slicer-5.1/qt-scripted-modules/shapepcalib.py:811: SyntaxWarning: "is" with a literal. Did you mean "=="?
  if (len(y_design) is 0):
/Volumes/D/P/S-0-E-b/ShapeVariationAnalyzer-build/inner-build/lib/Slicer-5.1/qt-scripted-modules/shapepcalib.py:820: SyntaxWarning: "is not" with a literal. Did you mean "!="?
  if len(y_design) is not 0:
/Volumes/D/P/S-0-E-b/ShapeVariationAnalyzer-build/inner-build/lib/Slicer-5.1/qt-scripted-modules/cpns/cpns.py:57: SyntaxWarning: "is" with a literal. Did you mean "=="?
  if len(self.fileList) is 0:
```

The syntax warning in question started as of Python 3.8.
https://docs.python.org/3.8/whatsnew/3.8.html#changes-in-python-behavior

&gt; The compiler now produces a [SyntaxWarning](https://docs.python.org/3.8/library/exceptions.html#SyntaxWarning) when identity checks (is and is not) are used with certain types of literals (e.g. strings, numbers). These can often work by accident in CPython, but are not guaranteed by the language spec. The warning advises users to use equality tests (== and !=) instead. (Contributed by Serhiy Storchaka in [bpo-34850](https://bugs.python.org/issue34850).)

cc: @jcfr</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Is there something with your usage of ShapeVariationAnalyzer that is not working?</p>

---

## Post #12 by @jamesobutler (2022-12-03 20:58 UTC)

<p>Xref</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/DCBIA-OrthoLab/ShapeVariationAnalyzer/issues/67">
  <header class="source">

      <a href="https://github.com/DCBIA-OrthoLab/ShapeVariationAnalyzer/issues/67" target="_blank" rel="noopener nofollow ugc">github.com/DCBIA-OrthoLab/ShapeVariationAnalyzer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/DCBIA-OrthoLab/ShapeVariationAnalyzer/issues/67" target="_blank" rel="noopener nofollow ugc">ShapeVariationAnalyzer does not work under Slicer 5.2.1</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-12-03" data-time="20:25:12" data-timezone="UTC">08:25PM - 03 Dec 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/bpuladi" target="_blank" rel="noopener nofollow ugc">
          <img alt="bpuladi" src="https://avatars.githubusercontent.com/u/44176896?v=4" class="onebox-avatar-inline" width="20" height="20">
          bpuladi
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">ShapeVariationAnalyzer does not work under Slicer 5.2.1
```

[Qt] Switch to m<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">odule:  "shapepcalib"
[Qt] Warning, there is no UI for the module "shapepcalib"
```</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #13 by @Shivi23 (2023-04-09 18:20 UTC)

<p>Hi, I am using Slicer 5.2.2 and I have installed Shape Variation Analyzer by adding it as an extension. However, I do not see it as a module in the module list. Please help.</p>

---
