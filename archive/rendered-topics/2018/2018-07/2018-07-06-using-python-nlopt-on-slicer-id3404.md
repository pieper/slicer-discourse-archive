# Using Python nlopt on Slicer

**Topic ID**: 3404
**Date**: 2018-07-06
**URL**: https://discourse.slicer.org/t/using-python-nlopt-on-slicer/3404

---

## Post #1 by @chaddy1004 (2018-07-06 15:32 UTC)

<p>Hello</p>
<p>I am trying to use a library called <a href="https://nlopt.readthedocs.io/en/latest/" rel="noopener nofollow ugc">NLopt</a> in Slicer for module development, but I am having a very difficult time getting it to work.</p>
<p>What I did was to download the .whl file of NLopt provided by the authors found <a href="https://www.lfd.uci.edu/~gohlke/pythonlibs/#nlopt" rel="noopener nofollow ugc">here</a> and ran</p>
<pre><code>pip.main(["install", "C:\Users\Stewart\Downloads\NLopt-2.4.2-cp27-cp27m-win_amd64.whl"]) 
</code></pre>
<p>It prompted that the install was successful, but when I try to import the module, I get the following error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5eabd1e673d2aecdb5d6e6d21e203080f6d4fe3.png" data-download-href="/uploads/short-url/uwoCQPGZDWooMwpgtpdiUCvIuDF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5eabd1e673d2aecdb5d6e6d21e203080f6d4fe3.png" alt="image" data-base62-sha1="uwoCQPGZDWooMwpgtpdiUCvIuDF" width="690" height="112" data-dominant-color="FFF0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">831×135 4.14 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then I built the source code of NLopt, then proceeded to place the .dll file in the Slicer Python’s site packages like so:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f6b1e9375fd756897a393550921bd571fc86e83.png" alt="image" data-base62-sha1="bkzdNisGTgQSVi1PBROmH4u2jpp" width="582" height="58"><br>
but it still gives me the same errors.</p>
<p>When I pip install the .whl file through my command prompt and import it, it works fine.</p>
<p>I realize that this is a very specific question, but does anyone have any good suggestions on what to do, or got Python NLopt to work with Slicer?</p>
<p>Thank you!</p>
<p>Chad Paik</p>

---

## Post #2 by @lassoan (2018-07-07 05:04 UTC)

<p>Slicer uses Python 2.7, built using Visual Studio 2015. You need to build NLopt with Slicer’s Python, using Visual Studio 2015, similarly to how numpy is built. After we release Slicer-4.10, we’ll start migrating to Python3 and then it’ll be possible to pip install any packages.</p>

---
