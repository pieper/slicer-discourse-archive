# Basic PyCharm Importation Analysis for Slicer Development

**Topic ID**: 8509
**Date**: 2019-09-20
**URL**: https://discourse.slicer.org/t/basic-pycharm-importation-analysis-for-slicer-development/8509

---

## Post #1 by @evan (2019-09-20 17:34 UTC)

<p>After searching the web, I found that it is not currently possible to gain full IDE code-completion/analysis for Slicer python development as some packages are added at run-time.</p>
<p>I was able to gain some package importation analysis (resulting in the removal of many false errors and warnings) by the following:</p>
<ol>
<li>In PyCharm open your Slicer project of choice</li>
<li>In the menu-bar, open <strong>File</strong> &gt; <strong>Settings</strong></li>
<li>In Settings, click <strong>Project: ____</strong> &gt; <strong>Project Interpreter</strong></li>
<li>Next to Project Interpreter click  <img src="https://emoji.discourse-cdn.com/twitter/gear.png?v=12" title=":gear:" class="emoji" alt=":gear:" loading="lazy" width="20" height="20"> &gt; <strong>Add</strong></li>
<li>Navigate to and select <strong>Slicer installation directory</strong> \ <strong>bin</strong> \ <strong>PythonSlicer.exe</strong></li>
</ol>
<p>The following should appear:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c395f6ee0f78b303382cd820174707aa0aea450e.png" data-download-href="/uploads/short-url/rUep4jdiOwu4gry5loZZ59hIgHk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c395f6ee0f78b303382cd820174707aa0aea450e.png" alt="image" data-base62-sha1="rUep4jdiOwu4gry5loZZ59hIgHk" width="690" height="308" data-dominant-color="404446"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">990×443 14.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
PyCharm will now interpret using Slicer’s included python binary. I would not recommend updating or adding packages. However, I did find it useful to add the Python 2.7 PyQt package as a reference module, as it offers full PyQt code-completion. Remembering to remove this manually added package and point to Slicer’s PyQt (import qt) before deployment.</p>

---

## Post #2 by @jamesobutler (2019-09-20 20:25 UTC)

<p>As a clarification, Slicer uses <a href="https://mevislab.github.io/pythonqt/" rel="nofollow noopener">PythonQt</a> and not <a href="https://riverbankcomputing.com/software/pyqt/intro" rel="nofollow noopener">PyQt</a>. They are similar, but if you run into python related Qt issues make sure to look into the correct source. Slicer uses PythonQt as included in CTK <a href="https://github.com/commontk/PythonQt" rel="nofollow noopener">https://github.com/commontk/PythonQt</a>.</p>

---
