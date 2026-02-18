# Building Slicer offline for inclusion in Fedora

**Topic ID**: 1838
**Date**: 2018-01-14
**URL**: https://discourse.slicer.org/t/building-slicer-offline-for-inclusion-in-fedora/1838

---

## Post #1 by @sanjayankur31 (2018-01-14 17:54 UTC)

<p>Hi!</p>
<p>I’m trying to package Slicer up for inclusion in Fedora. Here’s the <a href="https://github.com/sanjayankur31/rpm-specs/blob/slicer/Slicer.spec" rel="nofollow noopener">WIP spec</a>.</p>
<p>I haven’t managed to build it completely just yet. I notice that the build requires both Git and SVN (the CMakeLists file checks for them), and it seems that the build fetches other bits from the internet too. Most distributions do not permit internet access during builds for security reasons, so that unvetted software cannot be included during builds (and thus compromise the software set).</p>
<p>For Fedora (and other distributions too, I’d think), the build dependencies must be packaged first. So, one starts from the leaves of the dependency tree and packages each node until one gets to the root, in this case Slicer. Would someone have an idea of the list of dependencies, and the order in which they must be built individually, and of course, can one force the Slicer build to use their local system builds instead of fetching them from internet sources without having to hack around the build configuration files too much?</p>
<p>Thanks!<br>
Ankur</p>
<p><a href="https://fedoraproject.org/wiki/User:Ankursinha" class="onebox" target="_blank" rel="nofollow noopener">https://fedoraproject.org/wiki/User:Ankursinha</a></p>

---

## Post #2 by @jcfr (2018-01-14 18:01 UTC)

<p>Hi <a class="mention" href="/u/sanjayankur31">@sanjayankur31</a></p>
<p>Thanks for reaching out.</p>
<blockquote>
<p>do not permit internet access during builds for security reasons</p>
</blockquote>
<p>Makes sense. To support this use case, the build system supports using system version and/or passing local version of most of the dependencies.</p>
<p>For example, to support building against system python, you could configure with <code>-DSlicer_USE_SYSTEM_python:BOOL=ON</code>.</p>
<p>And for using a local build of VTK, you could pass <code>-DVTK_DIR:PATH=/path/to/VTK-build</code>.</p>
<p>Looking at the different <code>External_*</code> files found in <a href="https://github.com/Slicer/Slicer/tree/master/SuperBuild">Slicer/SuperBuild</a> directory should give some hint.</p>
<p>To address and discuss remaining issues, you could also join our weekly hangout. It will be advertised in this topic: <a href="https://discourse.slicer.org/t/weekly-hangout-for-slicer-user-and-developer/53/50" class="inline-onebox">Weekly Hangout for Slicer user and developer - #50</a></p>

---

## Post #3 by @sanjayankur31 (2018-01-14 18:28 UTC)

<p>Hi! Thank you for the quick reply.</p>
<blockquote>
<p>Makes sense. To support this use case, the build system supports using system version and/or passing local version of most of the dependencies.<br>
For example, to support building against system python, you could configure with - DSlicer_USE_SYSTEM_python:BOOL=ON.<br>
And for using a local build of VTK, you could pass -DVTK_DIR:PATH=/path/to/VTK-build.<br>
Looking at the different External_* files found in Slicer/SuperBuild directory should give some hint.</p>
</blockquote>
<p>Lovely. I’ll get started there then. Most of the deps there seem to be in Fedora, but I do see one or two that I’ll have to package first.</p>
<blockquote>
<p>To address and discuss remaining issues, you could also join our weekly hangout. It will be advertised in this topic: Weekly Hangout for Slicer user and developer</p>
</blockquote>
<p>I’ll keep an eye on that and turn up if I run into trouble.</p>
<p>Thanks again!</p>

---

## Post #4 by @sanjayankur31 (2018-01-14 19:13 UTC)

<p>A quick grep tells me that using system libraries for a few of the dependencies is not supported:</p>
<pre><code>[asinha@ankur  SuperBuild]$ grep "SYSTEM.* not supported" *
External_CTKAPPLAUNCHER.cmake:    message(FATAL_ERROR "Enabling ${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj} is not supported !")
External_CTKAppLauncherLib.cmake:  message(FATAL_ERROR "Enabling ${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj} is not supported !")
External_CTK.cmake:  message(FATAL_ERROR "Enabling ${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj} is not supported !")
External_CTKResEdit.cmake:  message(FATAL_ERROR "Enabling ${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj} is not supported !")
External_JsonCpp.cmake:  message(FATAL_ERROR "Enabling ${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj} is not supported !")
External_LibArchive.cmake:  message(FATAL_ERROR "Enabling ${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj} is not supported !")
External_ParameterSerializer.cmake:  message(FATAL_ERROR "Enabling ${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj} is not supported !")
External_PCRE.cmake:  message(FATAL_ERROR "Enabling ${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj} is not supported !")
External_qRestAPI.cmake:  message(FATAL_ERROR "Enabling ${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj} is not supported !")
External_SciPy.cmake:  message(FATAL_ERROR "Enabling ${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj} is not supported !")
External_SimpleITK.cmake:  message(FATAL_ERROR "Enabling ${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj} is not supported !")
External_SlicerExecutionModel.cmake:  message(FATAL_ERROR "Enabling ${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj} is not supported !")
External_Swig.cmake:  message(FATAL_ERROR "Enabling ${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj} is not supported !")
</code></pre>
<p>Is this because modified versions of these are needed? If it is so, I’m afraid I’ll have to wait until these modifications have been merged upstream and entered Fedora as updates. For the time being, I’ll modify the cmake files to remove these constraints and see how that goes.</p>
<p>It is possible to use bundled versions, but it is strongly suggested to use upstream versions:<br>
<a href="https://fedoraproject.org/wiki/Bundled_Libraries?rd=Packaging:Bundled_Libraries" class="onebox" target="_blank" rel="nofollow noopener">https://fedoraproject.org/wiki/Bundled_Libraries?rd=Packaging:Bundled_Libraries</a><br>
<a href="https://fedoraproject.org/wiki/Packaging:Guidelines#Bundling_and_Duplication_of_system_libraries" class="onebox" target="_blank" rel="nofollow noopener">https://fedoraproject.org/wiki/Packaging:Guidelines#Bundling_and_Duplication_of_system_libraries</a></p>
<p>Thanks!</p>

---

## Post #5 by @ihnorton (2018-01-16 15:49 UTC)

<p>I very much appreciate the spirit of this initiative, but I have to ask whether:</p>
<ul>
<li>it will be maintained</li>
<li>what the support channels would be</li>
<li>what is the advantage over generic linux binaries from <a href="http://download.slicer.org">download.slicer.org</a>?</li>
</ul>
<p>I ask this because Slicer has been included in Debian in the past, but the port was not maintained, which leads to user confusion when they install that way and then find they are versions behind.</p>
<p>In fact, it is not unusual to recommend that a user downloads a nightly build only a few weeks after a “stable release” (releases are done for various important reasons – but they aren’t more stable than a typical nightly).</p>
<p>Slicer maintainers are effectively the upstream for all of CTK*, ParameterSerializer, SlicerExecutionModel; and work very closely with VTK, ITK, and SimpleITK maintainers – for this reason, Slicer often tracks pinned commits and backports, rather than upstream releases.</p>
<p>All of which makes this policy:</p>
<aside class="quote no-group" data-username="sanjayankur31" data-post="4" data-topic="1838">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sanjayankur31/48/1075_2.png" class="avatar"> sanjayankur31:</div>
<blockquote>
<p>It is possible to use bundled versions, but it is strongly suggested to use upstream versions</p>
</blockquote>
</aside>
<p>difficult to follow…</p>

---

## Post #6 by @sanjayankur31 (2018-02-04 17:34 UTC)

<p>Well, Fedora follows the standard Linux distribution eco-system pretty much. As the update policy I had linked to earlier gives details about the updates policy, but this relies on major releases being more stable than nightliies in general, so that does not apply. I cannot see maintainers updating packages at each commit, for example. The packages go through a QA process, and that building each commit does not lend itself well to it.</p>
<p><a href="https://fedoraproject.org/wiki/QA:Updates_Testing" class="onebox" target="_blank" rel="nofollow noopener">https://fedoraproject.org/wiki/QA:Updates_Testing</a></p>
<p>Linux distributions provide support at the first level where the community aims to diagnose the issue, and provide the user with enough information to help decide if it was a package/distribution specific error (which may be caused due to dependent packages or other distribution specific mechanisms) or if it’s an upstream error, in which case users will be redirected to the forum here.</p>
<p>The biggest advantage is that instead of users having to install the various tools individually from individual upstreams, they can install them all from the distribution’s repositories. The maintenance responsibility is taken over by the maintainer who updates the packages regularly and provides these updates to users. I cannot see most users regularly checking for updates. I also cannot see most users regularly using nightlies unless asked to do so either - especially if the user is not trained in computer science, as is regularly the case in research.</p>
<p>Fedora does include VTK and the others, but since I do not maintain them, I am not well versed with the developement cycle they follow. It is perfectly alright to follow commits and backports, but unless these are of extremely high priority, I generally see that these changes are collected into a minor release or a major one even.</p>
<p>I do agree that the current upstream development method may not lend itself to distribution based packaging. Maybe Flakpacks/snappy etc would be a better way, or maybe even a COPR repository that can be quicker moving but does not see any testing.</p>
<p><a href="https://copr.fedorainfracloud.org/" class="onebox" target="_blank" rel="nofollow noopener">https://copr.fedorainfracloud.org/</a></p>

---
