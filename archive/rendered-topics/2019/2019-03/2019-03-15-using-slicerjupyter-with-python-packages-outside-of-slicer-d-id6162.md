# Using SlicerJupyter with python packages outside of Slicer distribution

**Topic ID**: 6162
**Date**: 2019-03-15
**URL**: https://discourse.slicer.org/t/using-slicerjupyter-with-python-packages-outside-of-slicer-distribution/6162

---

## Post #1 by @fedorov (2019-03-15 21:27 UTC)

<p>I guess it is obvious in retrospect, but it took me by surprise that I can only use python packages available within Slicer when I use Slicer Jupyter kernel. What is the recommended approach for installing extra python packages to use with Slicer kernel?</p>
<p>In my specific case, for example, I would like to have pandas and pylidc in my Slicer kernel notebook. I did find the post with instructions here how to install external packages: <a href="https://discourse.slicer.org/t/error-when-installing-scikit-image-via-python-interactor/2253" class="inline-onebox">Error when installing scikit-image via Python Interactor</a>, but I wanted to confirm before I do it. Is this what I should be doing?</p>
<p>Now that I think about it, it might be easier and more flexible to use a standard python kernel, generate a python initialization script to import+load data and initialize the viewers “on the fly”, and then launch a Slicer instance with that script. This way there is lower burden on the user of the notebook to get it ready to run.</p>

---

## Post #2 by @lassoan (2019-03-15 21:46 UTC)

<p>Slicer will switch to Python 3 within days. Then you can install any Python package using pip. Each Slicer installation will act as yet another Python environment.</p>
<p>The huge advantage of using Slicer’s embedded Python kernel is that you can continuously use both the desktop and Jupyter interface. For example, you can load all data in Jupyter and inspect interactively in the desktop application; or the other way, you load your data using the desktop interface and launch processing implemented as a notebook. There is need to launch Slicer instances manually or implement inter-process communication between the notebook’s kernel and Slicer.</p>

---

## Post #3 by @fedorov (2019-03-15 21:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="6162">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer will switch to Python 3 within days. Then you can install any Python package using pip.</p>
</blockquote>
</aside>
<p>I see. I will revisit it then.</p>
<p>How reliable is the “within days” estimate? I can wait days, but if I need to wait weeks, then I would rather implement the other solution with the startup script, due to project deadlines.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="6162">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The huge advantage of using Slicer’s embedded Python kernel is that you can continuously use both the desktop and Jupyter interface.</p>
</blockquote>
</aside>
<p>Oh yes, I can’t agree more. But it depends on the requirements (for example, sometime it is important to keep instructions to the minimum, and maybe the only need is to quickly view something in Slicer), and requires that packages not available within Slicer can be installed easily.</p>
<p>Another issue is that Slicer kernel based notebooks cannot be used without Slicer kernel. I may want to have a notebook sections of which do not require Slicer, and I want those cells to be runnable if/when the user does not have Slicer, or doesn’t want to bother with the functionality that does not require Slicer.</p>

---

## Post #4 by @lassoan (2019-03-15 22:07 UTC)

<p>What we end up doing is that instead of having large notebooks that call out to various Python environments, in a project we use a couple of notebooks, and a few environments. Data pre-processing and feature extraction uses Slicer flnotebook, exported data is used for machine learning training using Anaconda-based notebooks. Trained models are used in Slicer by communicating with an Anaconda-based server via pyIGTLink and/or files (and there are a couple of other variants).</p>
<p>If for a particular project you don’t need Slicer functions in the notebook then you can delete the unnecessary cells from your notebook and choose another kernel.</p>

---

## Post #5 by @fedorov (2019-03-15 22:10 UTC)

<p>Yes, that is exactly what I was planning to do, but I need those other python packages for interacting with the metadata that I want to use in conjunction with image visualization in Slicer.</p>

---

## Post #6 by @ungi (2019-03-16 20:33 UTC)

<p>When I run into similar issues, I use numpy files or csv files to communicate data between Slicer notebooks and Python 3 notebooks. With standard paths and file names, it is not as painful as it sounds. But I’m also looking forward to trying Slicer with Python 3. In a few days, we won’t have these problems anymore.</p>

---

## Post #7 by @lassoan (2019-03-18 05:29 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="3" data-topic="6162">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>How reliable is the “within days” estimate?</p>
</blockquote>
</aside>
<p>You can find an update from <a class="mention" href="/u/jcfr">@jcfr</a> here in this topic: <a href="https://discourse.slicer.org/t/updating-slicer-to-work-with-python-3/4662/3" class="inline-onebox">Updating slicer to work with python 3 - #3 by jcfr</a></p>

---
