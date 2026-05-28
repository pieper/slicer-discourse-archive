---
topic_id: 47155
title: "Why aren't we building the extensions in parallel?"
date: 2026-05-27
url: https://discourse.slicer.org/t/47155
last_bumped: 2026-05-28T00:14:14.146Z
---

# Why aren't we building the extensions in parallel?

**Topic ID**: 47155
**Date**: 2026-05-27
**URL**: https://discourse.slicer.org/t/why-arent-we-building-the-extensions-in-parallel/47155

---

## Post #1 by @muratmaga (2026-05-27 18:10 UTC)

<p>When I look at the dashboard for extension and sort them by time, there is a clear pattern. Extensions are build sequentially by the operating system.</p>
<p>Is there are reason we are doing that? Can’t they be parallelized? Like Linux is uploaded over 12h ago and Mac extension builds hasn’t even finished, and already half of the workday is gone.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b831e35d9da2cea15ed9e759b26313c070147a0.jpeg" data-download-href="/uploads/short-url/1DQaC96AFDQWUeUlDQfXfiTqCTm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b831e35d9da2cea15ed9e759b26313c070147a0_2_497x500.jpeg" alt="image" data-base62-sha1="1DQaC96AFDQWUeUlDQfXfiTqCTm" width="497" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b831e35d9da2cea15ed9e759b26313c070147a0_2_497x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b831e35d9da2cea15ed9e759b26313c070147a0_2_745x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b831e35d9da2cea15ed9e759b26313c070147a0_2_994x1000.jpeg 2x" data-dominant-color="D1D8D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1505×1513 568 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Sam_Horvath (2026-05-27 18:39 UTC)

<p>Are you asking why aren’t we building them in parallel per os - we should probably work on this.</p>
<p>Are you asking if we are finishing the Linux and Windows extensions and only then building macos extensions? - that is not what is happening. The macos build/test process is just taking forever, for macos reasons, mainly that a single crash tested can trigger the crash reporter, causing tests to go to the timeout.</p>
<p>In general, the linux app build finishes first, then Windows and later macos, just based on their own build times</p>

---

## Post #3 by @muratmaga (2026-05-27 18:43 UTC)

<p>The former, why aren’t we parallelazing the build per os. They are independent anyways.</p>
<p>I understand macos builds takes longer. But from my reading of the time line, the Macos extension build starts after the windows and Linux is done, hence my suggestion of making them go in parallel.</p>

---

## Post #4 by @Sam_Horvath (2026-05-27 18:48 UTC)

<ol>
<li>
<p>They are not independent, (extensions can have dependencies on other extensions).  We would need to redo the extension build system to addresss this.</p>
</li>
<li>
<p>They are already in parallel.  They are running on three separate machines with no timing interaction with each other.  The macos extension build starts once the macos app build/test is done, the same as the other two platforms.  The reason why macos  starts “after” the other two is because the mac build takes so much longer</p>
</li>
</ol>

---

## Post #5 by @Sam_Horvath (2026-05-27 18:55 UTC)

<p>Looking at this thread, I am wondering if we are misunderstanding each other on what (1) and (2) are.</p>
<p>1 - Building SlicerIGT and SlicerRt (for example) in parallel on one OS - we would need to work on the build system a bit for this</p>
<p>2 - MacOS, Linux, and Windows  app/extension builds are already running completely independently from each other.</p>

---

## Post #6 by @muratmaga (2026-05-27 19:08 UTC)

<p>So the just mac build itself takes about 11h+ then? (Dashboard shows started 16h ago, and uploaded 5h ago). And then another 5h for the MacOS extensions to build?</p>

---

## Post #7 by @lassoan (2026-05-27 22:58 UTC)

<p>Build time on macOS is very long due to packaging, which includes updating shared library paths in thousands of binary files.</p>
<p>Extension builds could be probably made somewhat faster by building them in parallel, but we should really move towards building each extension immediately in github actions. That would allow developers to create and test packages any time in a few minutes and publish them on the extensions index without waiting for the next day. It would also mean less load on Kitware build servers and less worrying about security issues associated with building constantly changing third-party code.</p>
<p>Packaging of Python-only extensions already works, you only need to <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/pull/105/changes">add a very small (8 lines) script file to your extension</a>. See more details here: <a href="https://github.com/Slicer/Slicer/pull/9118" class="inline-onebox">ENH: Add script to package native Python extensions by lassoan · Pull Request #9118 · Slicer/Slicer · GitHub</a></p>
<p>There seems to be a shortage of intel macOS github runners, so macOS packages may be delayed, but this will be solved when we switch to native ARM builds.</p>
<p>The next step will be streamlining of extensions submission/update process. We can get the list of all the available extensions on github (via the <a href="https://github.com/topics/3d-slicer-extension"><code>3d-slicer-extension</code> github topic</a>) and we could use that to populate an index dynamically. But it still makes sense to have a central repository of extension packages for archiving and performance reasons; and the tier system (1=experimental; 3=stable; 5=supported by Slicer core team) also needs centralized curation process.</p>

---

## Post #8 by @muratmaga (2026-05-27 23:37 UTC)

<p>This looks interesting and useful. But I guess unless we switch to pure ARM build for maOS, it is not going to be much of help shortening the build time. Will the next stable 5.12 be native macos application or still use Rosetta?</p>

---

## Post #9 by @jamesobutler (2026-05-27 23:48 UTC)

<p>Per most recent Slicer hangout meeting notes, the next stable 5.12 will still require Rosetta for Apple Silicon Macs. There are likely additional build dependencies and build updates to make native arm builds possible. An Apple Silicon Mac will also need to be identified that will do the Slicer factory building, packaging and testing. Of course part of this work is making sure various parts extensions (primarily the compiled ones) are also still working on arm architecture. There are arm systems running Windows, Linux and macOS so it could be for all platforms.</p>
<aside class="quote quote-modified" data-post="4" data-topic="47103">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ebrahim/48/13403_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/2026-05-26-weekly-meeting/47103/4">2026.05.26 Weekly Meeting</a> <a class="badge-category__wrapper " href="/c/community/hangout/20"><span data-category-id="20" style="--category-badge-color: #12A89D; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #F7941D;" data-parent-category-id="12" data-drop-close="true" class="badge-category --style-square --has-parent" title="This category is used to announce hangouts and organize associated notes."><span class="badge-category__name">Weekly meetings</span></span></a>
    </div>
  </div>
  <blockquote>
    Meeting notes: 
<a name="p-133977-slicer-512-everyone-1" class="anchor" href="#p-133977-slicer-512-everyone-1" aria-label="Heading link"></a>Slicer 5.12 (Everyone)
Slicer 5.12 release issue now exists: <a href="https://github.com/Slicer/Slicer/issues/9180" class="inline-onebox" rel="noopener nofollow ugc">Release Slicer v5.12 · Issue #9180 · Slicer/Slicer · GitHub</a> 
It is a good time to release 5.12 soon because we have a fairly clean dashboard and we are about tackle two problems that will create a broken nightly for a while: transtion to Qt6 and support mac arm64. 
<a name="p-133977-imported-symbols-in-python-console-steve-ebrahim-2" class="anchor" href="#p-133977-imported-symbols-in-python-console-steve-ebrahim-2" aria-label="Heading link"></a>Imported symbols in python console (Steve, Ebrahim)
We should restore the legacy behavior in terms of things in slicer.util that were previously automaticall…
  </blockquote>
</aside>


---

## Post #10 by @rkikinis (2026-05-27 23:55 UTC)

<p>Apple will discontinue support for Rosetta 2 sometime in 2027, if I understand it correctly.</p>
<p>This email is intended for non-work related messages</p>

---

## Post #11 by @jamesobutler (2026-05-28 00:14 UTC)

<p>Yes Rosetta 2 is planned to not be present in macOS 28 expected release in October 2027, so we technically have some time where using Rosetta builds is still possible for the most recent version of macOS. Apple supports 3 given versions at any one time so macOS 27 with Rosetta 2 will still be receiving security updates likely up until macOS 30 (fall of 2029). Of course we will aim to provide native arm builds sooner especially with certain Python packages no longer providing pre-built whls for Intel Mac.</p>

---
