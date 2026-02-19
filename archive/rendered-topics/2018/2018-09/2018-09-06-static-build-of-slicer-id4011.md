---
topic_id: 4011
title: "Static Build Of Slicer"
date: 2018-09-06
url: https://discourse.slicer.org/t/4011
---

# Static build of Slicer

**Topic ID**: 4011
**Date**: 2018-09-06
**URL**: https://discourse.slicer.org/t/static-build-of-slicer/4011

---

## Post #1 by @cpinter (2018-09-06 23:57 UTC)

<p>Does anyone know if there is a way to statically build Slicer so that there is only one Slicer.exe and no vtkSlicer*.dll, qSlicer*.dll, vtkMRML*.dll or qMRML*.dll etc?</p>
<p>I tried configuring with BUILD_SHARED_LIBS=OFF, but it had no effect.</p>
<p>Thanks!</p>

---

## Post #2 by @jcfr (2018-09-07 05:09 UTC)

<p>While this has been on my wish list, it is currently not supported.</p>
<p>To make progress, I suggest to start with python disabled, and only the minimum number of external  projects.</p>
<p>To support loading the loadable modules, I anticipate that some header/cpp files would have to be generated to ensure the corresponding code is built in. On other hand, the CLI may be more complex … at first, they should probably be supported only when built as executable only.</p>

---

## Post #3 by @ihnorton (2018-09-07 13:54 UTC)

<p>If the use-case is improved start-up time, we could probably get a long way by reducing the total number of libraries (e.g. have libVTK, libITK, etc. rather than all the tiny constituents). When I’ve profiled start-up on mac, there is a huge amount of time spent in symbol coalescing (has to coalesce many external references, especially in ITK libraries, every time a CLI is pre-loaded).</p>
<p>Start-up time did seem to improve noticeably over the last months, though, so thanks to whoever (…<a class="mention" href="/u/jcfr">@jcfr</a>) did that <img src="https://emoji.discourse-cdn.com/twitter/sparkles.png?v=6" title=":sparkles:" class="emoji" alt=":sparkles:"></p>

---

## Post #4 by @cpinter (2018-09-07 14:07 UTC)

<p>Thanks Isaiah but it’s not about startup time. A client would like to make it harder to identify Slicer from the installed application files. I personally don’t think this would help a lot because you can look into the executable for the symbols, but still want to give this a try if I can.</p>

---

## Post #5 by @ihnorton (2018-09-07 14:26 UTC)

<p>You could strip or symbol-obfuscate a fully static build (which would presume a solution for dlopen’d libraries), but Python files would still be strongly identifying. There are tools like <a href="https://en.wikipedia.org/wiki/UPX">UPX</a> which could essentially do whole-program obfuscation in a way that is simple and transparent enough that it might not break Slicer’s assumptions (basically decompresses at startup) but it would add startup overhead, and might be hard to justify in regulated situations.</p>

---

## Post #6 by @pieper (2018-09-07 14:34 UTC)

<p>If you just want to change the appearance of the program to the casual user, you could probably use something like <a href="http://www.py2exe.org/index.cgi/Py2Exe">py2exe</a> that would unpack and run behind the scenes and then cleans up afterwards (assuming startup time really isn’t an issue).</p>

---

## Post #7 by @cpinter (2018-09-07 20:10 UTC)

<p>Thanks for the ideas. Any tips for the original question though about how to statically build Slicer.exe? I need to use the installer too. If this is not considered enough then I’ll consider other methods later (to be honest I don’t think any amount of effort will be enough if a tech savvy person starts digging, but I’d like to fulfill the actual requests).</p>

---

## Post #8 by @tbillah (2021-01-13 22:39 UTC)

<p>It’s been two years since this post. Is dynamic linking of libraries still the only option?</p>
<p>In the current way, I build some executables e.g. <code>FiberTractMeasurements</code> from <code>SlicerDMRI</code> and if I move <code>Slicer</code> build tree or the executables elsewhere, my executables can’t find libraries like:</p>
<blockquote>
<p>/cli/FiberTractMeasurements: error while loading shared libraries: libSlicerBaseLogic.so: cannot open shared object file: No such file or directory</p>
</blockquote>

---

## Post #9 by @jcfr (2021-01-13 22:54 UTC)

<p>We currently do not actively support building Slicer main application statically.</p>
<p>If you would like to support using CLIs independently of Slicer, it should be possible to build them statically.</p>
<p>That said, since <code>FiberTractMeasurements</code> depends on Slicer libraries like <code>MRMLCore</code> (see <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/366d232d8406479fe2ec9fbd391d55978c2dfc11/Modules/CLI/FiberTractMeasurements/CMakeLists.txt#L15-L16">here</a> and <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/366d232d8406479fe2ec9fbd391d55978c2dfc11/Modules/CLI/FiberTractMeasurements/FiberTractMeasurements.cxx#L29-L41">here</a>), ensuring the <code>PATH</code> and <code>LD_LIBRARY_PATH</code> env. variable are set will be the easiest.</p>
<p>To support this, you could for example install the SlicerDMRI extension, and then run the following command:</p>
<pre><code class="lang-auto">Slicer --launch FiberTractMeasurements
</code></pre>

---

## Post #10 by @tbillah (2021-01-13 22:56 UTC)

<p>Right, I know the last way. I shall try to see if <code>SlicerDMRI</code> can be built independently of Slicer. If nothing works, I shall probably write a Python version of <code>FiberTractMeasurements</code> <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"></p>

---

## Post #11 by @jcfr (2021-01-13 23:01 UTC)

<blockquote>
<p>I shall probably write a Python version of <code>FiberTractMeasurements</code></p>
</blockquote>
<p>While possible, I think this would be counter productive.</p>
<p>I think we should better understand your use case and find way to support it. That way, we could work on improving the current infrastructure.</p>
<p>For example, we have been talking about factoring our MRML library so that they can be built independently and statically, and this could be prioritized.</p>
<p>Could you provide more details related to your use case?  Which modules are you trying to use independently, in which environment, … ?</p>

---

## Post #12 by @lassoan (2021-01-14 00:56 UTC)

<aside class="quote no-group" data-username="tbillah" data-post="10" data-topic="4011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tbillah/48/4139_2.png" class="avatar"> tbillah:</div>
<blockquote>
<p>Right, I know the last way</p>
</blockquote>
</aside>
<p>What is the problem with starting the module by running <code>Slicer --launch</code>?</p>
<aside class="quote no-group" data-username="tbillah" data-post="10" data-topic="4011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tbillah/48/4139_2.png" class="avatar"> tbillah:</div>
<blockquote>
<p>I shall probably write a Python version of <code>FiberTractMeasurements</code></p>
</blockquote>
</aside>
<p>Technical problems, such as static/dynamic linking are issues that can be solved with small one-time efforts and so should not be significant factors in strategic decisions.</p>
<p>To decide if you want to reimplement some SlicerDMRI feature you may consider how much effort you and SlicerDMRI developers spend with adding new features, fixing bugs, importance of using exactly the same methods/getting exactly the same results, how much your long-term goals are aligned with goals and interests of SlicerDMRI developers. It may be also important what other current and future Slicer features you might use, etc.</p>

---
