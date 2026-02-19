---
topic_id: 21572
title: "Suggestion For An R Interactor"
date: 2022-01-22
url: https://discourse.slicer.org/t/21572
---

# Suggestion for an R interactor

**Topic ID**: 21572
**Date**: 2022-01-22
**URL**: https://discourse.slicer.org/t/suggestion-for-an-r-interactor/21572

---

## Post #1 by @stevenagl12 (2022-01-22 13:53 UTC)

<p>So, I was wondering if it’s possible for us to get an R interactor in addition to the Python Interactor. My reasoning is that, it would be nice to be able to utilize packages such as RvtkStatismo, geomorph, and shiny, etc within 3D Slicer. I understand that geomorph has an equivalent module to SlicerMorph right now, but it does not do any of the real computation, and it would be nice to generate many of these things within the scene itself. RvtkStatismo can mainly be used within linux systems (as the download for windows is really bad), but it would enable statistical shape modelling, and if we can make slicer compatable with h5 transforms on top of an average shape model, then we can create a statistical shape model from data and display it within the 3D viewer, as well as colorize it.</p>

---

## Post #2 by @jamesobutler (2022-01-22 14:35 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> is more knowledgeable on this idea of going between Python and R options, but I think you will have to rely on installing python packages that call R packages where you’re still using a python 3 interactor instead of an R interactor.</p>
<p>Starting from this post linked below in a really old thread you can read some about why development of R within Slicer is likely not going to be implemented. It’s about most R packages having a GPL license instead of LGPL and Slicer is not wanting to distribute any GPL code in Slicer packages or extensions.</p>
<aside class="quote quote-modified" data-post="7" data-topic="4883">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/rpy2-pip-installation-fails/4883/7">Rpy2 pip installation fails</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a>. 
There are many different types of analyses that one can use landmark based shape analyses to investigate different biological questions (phylogenetics, ecology, evolutionary trajectories etc). Most of these are already implemented in R as different packages (and surprisingly almost none in python, AFAIK). We just don’t want to reimplement them in Slicer (and also take the responsibility of maintaining them). Instead our goal is to have a standard way of visualizing results…
  </blockquote>
</aside>


---

## Post #3 by @hherhold (2022-01-22 16:06 UTC)

<p>You can switch between R and Python inside Jupyter notebooks. Would that be useful, along with using SlicerJupyter?</p>

---

## Post #4 by @muratmaga (2022-01-22 16:23 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="1" data-topic="21572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>R interactor in addition to the Python Interactor. M</p>
</blockquote>
</aside>
<p>This cannot happen due to license incompatibilities between these two software.</p>
<p>You can use R through Rpyserve, Rpy2 or various other Integration packages.</p>
<p>But this is not as simple as passing an object between two platforms. For a good integration, you have to consider how you will handle those R objects in Slicer. How you will show the in the scene etc. We will be working towards that in a grant proposal that’s in works.</p>
<p>For the time being the simplest solution is to use SlicermorphR r package to easily import your digitization output into R</p>
<p>As for vtkStatismo, you can either import their pywheel into Slicer (if they have one) or use the VTK functions directly, which are all available directly.</p>

---

## Post #5 by @stevenagl12 (2022-01-25 12:53 UTC)

<p>Ah ok. My apologize, I am unfamiliar with how you set up a python interactor. Unfortunately I am not sure how to utilize the principle component values once exported from SlicerMorph to be useful in R.</p>

---

## Post #6 by @muratmaga (2022-01-25 17:30 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="5" data-topic="21572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>Unfortunately I am not sure how to utilize the principle component values once exported from SlicerMorph to be useful in R</p>
</blockquote>
</aside>
<p>You can use SlicerMorph derived PC scores in the whichever way you are using PC scores derived from the <code>gm.prcomp</code> function of the geomorph. They are equivalent. <a href="https://github.com/SlicerMorph/Tutorials/tree/main/GPA_3#example-r-analysis">This example</a> shows that on sample data.</p>

---

## Post #7 by @stevenagl12 (2022-01-28 21:48 UTC)

<p>Another stupid question for you. Did you have a special package which contained your parser function for your code you sent me to? My system is saying that I don’t have the function parser…</p>

---

## Post #8 by @muratmaga (2022-01-28 22:36 UTC)

<p>in R do<br>
<code>devtools::install_github("SlicerMorph/SlicerMorphR")</code>, then<br>
<code>library(SlicerMorphR)</code></p>

---

## Post #9 by @stevenagl12 (2022-01-29 09:48 UTC)

<p>Ah ok, the code snippet that was on github did not show that you had to use SlicerMorphR as a library, so I was very confused.</p>

---
