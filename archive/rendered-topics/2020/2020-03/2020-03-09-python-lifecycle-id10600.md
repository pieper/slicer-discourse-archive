---
topic_id: 10600
title: "Python Lifecycle"
date: 2020-03-09
url: https://discourse.slicer.org/t/10600
---

# Python Lifecycle

**Topic ID**: 10600
**Date**: 2020-03-09
**URL**: https://discourse.slicer.org/t/python-lifecycle/10600

---

## Post #1 by @Alex_Vergara (2020-03-09 13:57 UTC)

<p>Since Slicer is heavily dependent of python, it must aknowledge the end of life of each python version it uses. The releases can be seen <a href="https://devguide.python.org/#status-of-python-branches" rel="nofollow noopener">here</a>. As you can see, current python 3.6 will end its life in december 2021. Therefore there shall be a planned schedule of replacing the python version accordingly. Not now, not tomorrow, but a schedule saying this period will be taken for changing python version. The best would be to use a python installer instead of building python itself, but for this, Slicer shall be built as python packages. This is far to be done, therefore the path, at least for now, is to watch python releases.</p>

---

## Post #2 by @lassoan (2020-03-09 14:33 UTC)

<p>Thanks for the note. It means that we are in very good shape and we have lots of time till end of life of the Python version that we use. Do you expect any specific incompatibilities when switching to Python 3.7 or 3.8?</p>
<aside class="quote no-group" data-username="Alex_Vergara" data-post="1" data-topic="10600">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>The best would be to use a python installer instead of building python itself</p>
</blockquote>
</aside>
<p>A slight advantage would be to have somewhat shorter build time, but we would give up control of an important component of the Slicer package. If we cannot build Python locally then it would be hard to create debug-mode builds and investigate/patch problems locally. We would have less freedom in choosing build environment (although if we want to be compatible with binary packages available in the package index then we need to match the official Python build environment, so in official Slicer binaries we plan to remain compatible). Importing a large third-party binary may also be concerning for some companies who distribute Slicer-based software.</p>
<p>What advantages do you see in relying on a third-party Python binaries?</p>
<aside class="quote no-group" data-username="Alex_Vergara" data-post="1" data-topic="10600">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>for this, Slicer shall be built as python packages</p>
</blockquote>
</aside>
<p>I don’t see how it is related to how Python is built. It would be certainly useful to build some Slicer core features as Python packages, but this is still not a common practice among software with embedded Python interpreter and no widely used robust solutions exist (see some information <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Usage_options">here</a>).</p>

---

## Post #3 by @jamesobutler (2020-03-09 14:37 UTC)

<p>Updates to <a class="mention" href="/u/jcfr">@jcfr</a> ‘s python-cmake-buildsystem would be greatly appreciated for adding support for Python 3.7 and 3.8. There are currently PRs with some progress. See <a href="https://github.com/python-cmake-buildsystem/python-cmake-buildsystem/pull/257" rel="nofollow noopener">https://github.com/python-cmake-buildsystem/python-cmake-buildsystem/pull/257</a> and <a href="https://github.com/python-cmake-buildsystem/python-cmake-buildsystem/pull/264" rel="nofollow noopener">https://github.com/python-cmake-buildsystem/python-cmake-buildsystem/pull/264</a>.</p>

---

## Post #4 by @Alex_Vergara (2020-03-09 15:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="10600">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you expect any specific incompatibilities when switching to Python 3.7 or 3.8?</p>
</blockquote>
</aside>
<p>As both 3.7 and 3.8 are the current LTS, being 3.6 the old LTS, and both belong to the same 3.6 family there are not great forward incompatibilities. Although there are lots of back compatibilities. Moving from 3.6 to 3.8 shall be painless, but the other way round is very painful.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="10600">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What advantages do you see in relying on a third-party Python binaries?</p>
</blockquote>
</aside>
<p>Not third party, but official python installers. The main advantage is that the user may have already installed it. In any case you don’t need to build it.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="10600">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Updates to <a class="mention" href="/u/jcfr">@jcfr</a> ‘s python-cmake-buildsystem would be greatly appreciated for adding support for Python 3.7 and 3.8</p>
</blockquote>
</aside>
<p>This is really good, so there is already a work on this direction</p>

---

## Post #5 by @lassoan (2020-03-09 16:35 UTC)

<aside class="quote no-group quote-modified" data-username="Alex_Vergara" data-post="2" data-topic="10600">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="10600">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What advantages do you see in relying on a third-party Python binaries?</p>
</blockquote>
</aside>
<p>Not third party, but official python installers. The main advantage is that the user may have already installed it. In any case you don’t need to build it.</p>
</blockquote>
</aside>
<p>An installed Python is not usable for much (you need headers, libraries, etc.). I know that on Linux it is common to install libraries at system level and have associated dev packages, but it is uncommon on Windows, so it would not simplify the build process. Even on Linux I’m not sure how this can work, as you normally have many Python environments (even if you had some system Python, it is unlikely that it would be the one that you would want to use with Slicer).</p>
<aside class="quote no-group" data-username="Alex_Vergara" data-post="4" data-topic="10600">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Not third party, but official python installers.</p>
</blockquote>
</aside>
<p>I would consider third-party that is not our group or direct collaborators. We have limited knowledge and influence on what gets into official python installers.</p>
<p>It is probably a more interesting discussion is if we should build additional packages that are bundled with Slicer (such as numpy), or just install them from wheels. Since there are several packages, different versions, different tricks in how to build them, etc. and they are only used from Python (so libraries and headers are not needed), it is more tempting to just use the binaries downloaded from PyPI. In fact, as far as I know, this is what we already do in recent Slicer-4.11 versions for numpy.</p>

---

## Post #6 by @jamesobutler (2020-03-09 17:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="10600">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>it is more tempting to just use the binaries downloaded from PyPI. In fact, as far as I know, this is what we already do in recent Slicer-4.11 versions for numpy.</p>
</blockquote>
</aside>
<p>Indeed that is the case. The only one that we don’t is SimpleITK which relies on compatibility with the specific version of ITK that we use. The current stable version of SimpleITK uses ITK 4.13, but there is at least recently a “latest development binaries” option that uses a more recent ITK git hash. Though we generally don’t let SimpleITK dictate which version of ITK to use in Slicer.</p>

---

## Post #7 by @pieper (2020-03-09 17:52 UTC)

<p>I think it’s great that we can use PyPi packages in Slicer, but I still want us to be able to build everything we use so that we have the option of customizing anything we need to.  In the bad old days the “standard” python build systems were so ad hoc that we needed to control every piece and only build the subset that worked across platforms.  Things seem to be better now, but it would be bad to get in the habit of relying on just one source of all binaries.</p>
<p>A lot of the same arguments apply to Qt, but there it’s been harder to break free of the binaries.</p>

---

## Post #8 by @jcfr (2020-03-18 18:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="10600">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>A slight advantage would be to have somewhat shorter build time</p>
</blockquote>
</aside>
<p>Building the python library takes less than a minutes. I don’t think this should motivate any transition.</p>

---
