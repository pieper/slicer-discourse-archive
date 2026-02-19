---
topic_id: 32506
title: "Testing Without Launching Graphical Components"
date: 2023-10-31
url: https://discourse.slicer.org/t/32506
---

# Testing without launching graphical components

**Topic ID**: 32506
**Date**: 2023-10-31
**URL**: https://discourse.slicer.org/t/testing-without-launching-graphical-components/32506

---

## Post #1 by @jhlegarreta (2023-10-31 14:19 UTC)

<p>Hi,<br>
I am trying to set up a GHA workflow to test the SlicerDMRI extension. <code>ctest</code> is effectively finding and triggering the tests so far:<br>
<a href="https://github.com/SlicerDMRI/SlicerDMRI/actions/runs/6699507556/job/18203755131?pr=191#step:8:1519" class="inline-onebox" rel="noopener nofollow ugc">ENH: Test build · SlicerDMRI/SlicerDMRI@576ae7c · GitHub</a></p>
<p>However, as I’ve realized locally, some of those tests launch Slicer’s GUI components, and thus fail in the GitHub headless testing environment. I’ve seen that the test command contains a number of flags, e.g.<br>
<a href="https://github.com/SlicerDMRI/SlicerDMRI/actions/runs/6699507556/job/18203755131?pr=191#step:8:1505" class="inline-onebox" rel="noopener nofollow ugc">ENH: Test build · SlicerDMRI/SlicerDMRI@576ae7c · GitHub</a></p>
<p>Including e.g. a <code>--no-splash</code>.</p>
<p>I am wondering whether tests we can completely avoid launching Slicer’s GUI parts, or whether this is the case already, and if tests fail, it is because they genuinely launch GUI parts (within the context of the extension, maybe due to some design choices). I am asking this to save installing <code>xfvb</code> (and spending time interacting with GHA to see if the steps work) if possible.</p>
<p>Even when a display is available, I’d say that it is not desirable to launch GUI parts.</p>
<p>Thanks.</p>

---

## Post #2 by @pieper (2023-10-31 15:55 UTC)

<p>The first failing test seems to be due to this error:</p>
<blockquote>
<p>This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.</p>
</blockquote>
<p>You might need to install these:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#debian-ubuntu" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#debian-ubuntu</a></p>
<aside class="quote no-group" data-username="jhlegarreta" data-post="1" data-topic="32506">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>Even when a display is available, I’d say that it is not desirable to launch GUI parts.</p>
</blockquote>
</aside>
<p>It’s fine t have both kinds of tests, with and without the GUI, but as a general rule the tests that involve the GUI are more comprehensive and detect a wider variety of regressions, so explicitly running them as part of any CI is preferred.  Using xvfb or docker are options to make this seamless.</p>

---

## Post #3 by @jhlegarreta (2023-10-31 20:34 UTC)

<p>Thanks for answering, Steve.</p>
<aside class="quote no-group quote-modified" data-username="pieper" data-post="2" data-topic="32506">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>You might need to install these:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#debian-ubuntu" class="inline-onebox" rel="noopener nofollow ugc">Getting Started — 3D Slicer documentation</a></p>
</blockquote>
</aside>
<p><code>libxcb</code> is being installed: <a href="https://github.com/SlicerDMRI/SlicerDMRI/actions/runs/6707883768/job/18227432404#step:4:75" class="inline-onebox" rel="noopener nofollow ugc">ENH: Test build · SlicerDMRI/SlicerDMRI@d841568 · GitHub</a></p>
<p>and there is a symlink already:<br>
<a href="https://github.com/SlicerDMRI/SlicerDMRI/actions/runs/6711676171/job/18239570693#step:5:13" class="inline-onebox" rel="noopener nofollow ugc">ENH: Test build · SlicerDMRI/SlicerDMRI@9c6c873 · GitHub</a></p>
<p>So the only chances seems to use <code>xvfb</code>. Hoping that solves the issue:<br>
<a href="https://github.com/SlicerDMRI/SlicerDMRI/actions/runs/6711729063/job/18239746275?pr=191" class="inline-onebox" rel="noopener nofollow ugc">ENH: Test build · SlicerDMRI/SlicerDMRI@5e56b79 · GitHub</a></p>

---
