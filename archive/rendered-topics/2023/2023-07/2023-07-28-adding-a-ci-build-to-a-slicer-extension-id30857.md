---
topic_id: 30857
title: "Adding A Ci Build To A Slicer Extension"
date: 2023-07-28
url: https://discourse.slicer.org/t/30857
---

# Adding a CI build to a Slicer extension

**Topic ID**: 30857
**Date**: 2023-07-28
**URL**: https://discourse.slicer.org/t/adding-a-ci-build-to-a-slicer-extension/30857

---

## Post #1 by @jhlegarreta (2023-07-28 14:52 UTC)

<p>Hi,<br>
I am trying to set up a GHA workflow for CI of the SlicerdMRI module:<br>
<a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/172" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add GitHub actions build, test workflow file for CI by jhlegarreta · Pull Request #172 · SlicerDMRI/SlicerDMRI · GitHub</a></p>
<p>The CI is timing out due to Slicer taking beyond 6 hours to build, and not finishing:<br>
<a href="https://github.com/jhlegarreta/SlicerDMRI/actions/runs/5685962029/job/15411909622#step:6:50076" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add GitHub actions build, test workflow file for CI · jhlegarreta/SlicerDMRI@8844bab · GitHub</a></p>
<p>Maybe I’m missing many things, but I realize that:</p>
<ul>
<li>It compiles a number of extensions, or at least Slicer-dMRI, whose <code>HEAD</code> I am trying to build against Slicer, and thus it does not make sense to compile any default Slicer-dMRI extension. If all extensions being considered are using their <code>SuperBuild</code>, they will all be (re-)compiling all of Slicer and its dependencies. Is there a way to deactivate all extensions?<br>
e.g.<br>
<a href="https://github.com/jhlegarreta/SlicerDMRI/actions/runs/5685962029/job/15411909622#step:6:294" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add GitHub actions build, test workflow file for CI · jhlegarreta/SlicerDMRI@8844bab · GitHub</a></li>
<li>It compiles both ITK and SimpleITK. Are both necessary for a minimal Slicer build?</li>
<li>It builds the Python extensions. Is there a way to skip building Python extensions?</li>
<li>Would using ninja instead of GNU be faster?</li>
</ul>
<p>So, in general, what is the setting of flags for a minimal Slicer build within a reasonable time?</p>
<p>Thanks.</p>

---

## Post #2 by @pieper (2023-07-28 15:09 UTC)

<p>Yes, this issue is why we haven’t enable github actions for nightly builds or other testing.  One idea is to build some of the prerequisites in their own github action repos and then store the build trees to share between stages, but it’s not really been investigated.</p>
<p>If you think you can make a simple Slicer build, you can turn off SimpleITK since it’s probably not used in SlicerDMRI.  ITK is definitely needed, and it’s fairly fast.  That may be enough, but probably not.  Be sure to turn off BUILD_TESTING too.  You /might/ be able to turn off DICOM and SlicerDMRI might still work, but I’m not sure.  You can probably turn off CLI modules for Slicer but that might carry over in to SlicerDMRI - not sure you can re-enable that in the extension build if it’s off in Slicer.</p>

---

## Post #3 by @jhlegarreta (2023-07-28 15:16 UTC)

<p>Thanks for the answer Steve.</p>
<blockquote>
<p>you can turn off SimpleITK</p>
</blockquote>
<blockquote>
<p>You /might/ be able to turn off DICOM</p>
</blockquote>
<blockquote>
<p>You can probably turn off CLI modules</p>
</blockquote>
<p>Where are the CMake flags documented so that I can do that?</p>

---

## Post #4 by @pieper (2023-07-28 15:25 UTC)

<p>You’ll just need to look in the main CMakeLists.txt.</p>

---

## Post #5 by @lassoan (2023-07-30 14:19 UTC)

<p>Note that for building an extension you don’t need to build Slicer, but you can start from a docker image that already has the complete Slicer build tree.</p>
<p>We already use CI for building Slicer for all pull requests, which starts from an image that has all the dependencies pre-built. Slicer build from that image fits in the time limit.</p>
<p>The plan was to set up an image that contains the fully built Slicer build tree (updated nightly), which could cut down time requirements even further. <a class="mention" href="/u/jcfr">@jcfr</a> had this been set up already?</p>

---

## Post #6 by @jhlegarreta (2023-07-30 17:15 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="30857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Note that for building an extension you don’t need to build Slicer, but you can start from a docker image that already has the complete Slicer build tree.</p>
</blockquote>
</aside>
<p>Yes, that would be very helpful.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="30857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We already use CI for building Slicer for all pull requests, which starts from an image that has all the dependencies pre-built. Slicer build from that image fits in the time limit.</p>
</blockquote>
</aside>
<p>Yes, prior to submitting my PR to build SlicerDMRI I had a look at the Slicer CI folder, but found the workflow not straightforward to understand.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="30857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The plan was to set up an image that contains the fully built Slicer build tree (updated nightly), which could cut down time requirements even further.</p>
</blockquote>
</aside>
<p>Let me know when this is ready. Otherwise, I would still be interested in pulling an image that has all dependencies built. If an extension’s CI can do this easily, I could potentially use it.</p>

---

## Post #7 by @lassoan (2023-07-30 19:11 UTC)

<aside class="quote no-group" data-username="jhlegarreta" data-post="6" data-topic="30857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>Yes, prior to submitting my PR to build SlicerDMRI I had a look at the Slicer CI folder, but found the workflow not straightforward to understand.</p>
</blockquote>
</aside>
<p>The base image that comes with all Slicer depencies is this (updated nightly): <a href="https://hub.docker.com/r/slicer/slicer-base/">https://hub.docker.com/r/slicer/slicer-base/</a></p>
<aside class="quote no-group" data-username="jhlegarreta" data-post="6" data-topic="30857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>Let me know when this is ready. Otherwise, I would still be interested in pulling an image that has all dependencies built. If an extension’s CI can do this easily, I could potentially use it.</p>
</blockquote>
</aside>
<p>We would enable this for our extensions, too. Hopefully we’ll hear from <a class="mention" href="/u/jcfr">@jcfr</a> about this.</p>

---

## Post #8 by @jhlegarreta (2023-07-30 19:34 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="7" data-topic="30857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The base image that comes with all Slicer depencies is this (updated nightly): <a href="https://hub.docker.com/r/slicer/slicer-base/" class="inline-onebox" rel="noopener nofollow ugc">Docker</a></p>
</blockquote>
</aside>
<p>Yes, that I had seen. Thanks.</p>

---

## Post #9 by @jhlegarreta (2023-07-30 23:20 UTC)

<p>The build at issue is warning about an extension/CLI module that is missing:</p>
<pre><code class="lang-auto"> Dependent extension UKFTractography cannot be found by CMake
</code></pre>
<p>Not sure if it is clear by the rest of the warning how the extension can be included/built: what is the appropriate CMake option to tell the Slicer build to download and compile a given extension/CLI module?</p>

---

## Post #10 by @lassoan (2023-07-30 23:36 UTC)

<p>If an extension depends on another extensions then you need to pass the build folder of each dependency in <code>&lt;DependentExtensionName&gt;_DIR</code> CMake variable.</p>
<p>Alternatively, you can put all s4ext files of the extensions you want to build into a folder and build this list of extensions as described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-list-of-extensions-manually">here</a>.</p>

---

## Post #11 by @lassoan (2023-07-30 23:41 UTC)

<p>FYI, I’ve built Slicer from <code>slicer/slicer-base</code> and pushed it to <a href="https://hub.docker.com/layers/lassoan/slicer-built/20230730/images/sha256-d33f9a9b8aedabfe83c1ffb2c5f7a698eb309a2a9269080e2fdd36666f5576e2?context=explore"><code>lassoan/slicer-built:20230730</code></a>. It contains the full Slicer build tree, so it can be used for building any extension right away. It is quite big, though, so it may take a while for CI to download it. If it works then we could set up a repeating task to create a new image from latest Slicer source every night.</p>

---

## Post #12 by @jhlegarreta (2023-07-30 23:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="30857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If an extension depends on another extensions then you need to pass the build folder of each dependency in <code>&lt;DependentExtensionName&gt;_DIR</code> CMake variable.</p>
</blockquote>
</aside>
<p>OK, but this applies to the <code>SlicerDMRI</code> extension: how do I tell the Slicer build to download and build the <code>UKFTractography</code> extension? Do I need to proceed the exact same way as with <code>SlicerDMRI</code> by first cloning <code>UKFTractography</code>, then configuring, building? Luckily, it looks like the latter does not depend on other extensions.</p>
<blockquote>
<p>Alternatively, you can put all s4ext files of the extensions you want to build into a folder and build this list of extensions as described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-list-of-extensions-manually" rel="noopener nofollow ugc">here</a>.</p>
</blockquote>
<p>Not sure if I follow this, or how the linked page responds to the question above.</p>

---

## Post #13 by @jhlegarreta (2023-07-30 23:47 UTC)

<p>Thanks for the effort. Will consider it at some point. For now, building Slicer from scratch is uncovering things that may need some attention, documenting, etc., so I would prefer to try to build it that way for now.</p>

---

## Post #14 by @lassoan (2023-07-30 23:48 UTC)

<aside class="quote no-group quote-modified" data-username="jhlegarreta" data-post="12" data-topic="30857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>Do I proceed the exact same way as with <code>SlicerDMRI</code> by first cloning <code>UKFTractography</code>, the configuring, building?</p>
</blockquote>
</aside>
<p>Exactly. The inconvenience is that you need to run check out source code and build multiple extensions in the right order. If you simply <a href="https://github.com/Slicer/ExtensionsIndex/">download the list of s4ext files</a> that you want to build and put it in a folder and run the single CMake command described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-list-of-extensions-manually">here</a> then it downloads and builds all the extensions automatically (in the correct order, taking into account dependencies between them).</p>

---

## Post #15 by @lassoan (2023-07-31 00:32 UTC)

<aside class="quote no-group" data-username="jhlegarreta" data-post="13" data-topic="30857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>For now, building Slicer from scratch is uncovering things that may need some attention, documenting, etc</p>
</blockquote>
</aside>
<p>To get started, it may be simpler to follow the provided instructions and defaults. If you change defaults then you will get to non-well-documented territory and may discover problems, which may not be the best use of your time. We attempt to fix all issues, but it is not necessary (and not possible) to test and fix <em>all</em> the billions of combinations of build options.</p>

---

## Post #16 by @jhlegarreta (2023-07-31 13:26 UTC)

<p>Andras, I am turning off modules or options that are available as options in CMake: if they are necessary to build Slicer, I am fine, but then they should not be made available as options in CMake.</p>

---

## Post #17 by @lassoan (2023-07-31 13:44 UTC)

<p>There are dozens of flags and of course not all combinations are tested and not all makes sense. Since it would be impractical to document (and maintain documentation) of all possible interplays between all options, we do not even attempt or plan to do this.</p>
<p>For example, turning off a Slicer core module is a very invasive action with unforeseeable consequences. There may be compile-time or runtime dependencies, there may be hard dependencies that would prevent some other modules from working at all, or absence of a module may just disable certain features in other modules. Some dependencies may be changed or removed by investing some work, if there is a good reason to do so. Even if we could explore and document some of the side effects of disabling a module in Slicer core, it is practically impossible to evaluate all the effects in all extensions continuously; or ask extension developers to perform this kind of impact analysis, document the results, and keep it up-to-date continuously.</p>
<p>Therefore, I would recommend to keep all options at the default value unless you have a strong reason to change one. Reducing build time or package size by changing default options may worth the effort for a well-funded commercial project, but probably not worth it for automated testing of an open-source extension.</p>

---

## Post #18 by @pieper (2023-07-31 13:59 UTC)

<p>It’s also worth noting, not just for Slicer but for any software, that configuration options that are not regularly tested should be considered experimental and/or expected not to work until proven.  I’m sure that’s true for ITK and VTK for example, and I’m sure we’ve all encountered that.  For Slicer this means that the configuration used on the factory machines with the documented build systems is the starting point for any experiments.</p>
<p>Perhaps we should make this statement explicit in the build documentation.  We could even generate a cmake warning whenever a configuration is changed such that the build is going down and untested pathway.</p>
<p>If there are configurations that are important for key use cases then we should set up CI to keep them tested and working.</p>

---

## Post #19 by @jhlegarreta (2023-07-31 14:03 UTC)

<p>Agreed Steve: to me, the point is that if a module is part of the core, not sure why they should be optional. An intermediate step would be maybe to mark them as <code>Advanced</code> variables or grouped under a <code>Core</code> category.</p>
<p>Above all, I am grateful for all the work that you and the community has put and puts into this, and I am more than happy to continue helping, needless to say this. I have good reasons to set up a CI on GitHub for the extension at issue. We can discuss this on a call if necessary.</p>

---

## Post #20 by @jhlegarreta (2023-07-31 14:07 UTC)

<p>Thanks for the pointers. Had a look at this.</p>
<p>According to the extension index, <code>SlicerDMRI</code> seems not to depend on any other extension/module according to its extension index file:<br>
<a href="https://github.com/Slicer/ExtensionsIndex/blob/main/SlicerDMRI.s4ext#L5" rel="noopener nofollow ugc">https://github.com/Slicer/ExtensionsIndex/blob/main/SlicerDMRI.s4ext#L5</a></p>
<p>I now see that the configuration process, a few lines later,<br>
<a href="https://github.com/jhlegarreta/SlicerDMRI/actions/runs/5707614346/job/15464465415#step:7:186" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add GitHub actions build, test workflow file for CI · jhlegarreta/SlicerDMRI@67e378d · GitHub</a></p>
<p>says:</p>
<pre><code class="lang-auto">-- Setting EXTENSION_DEPENDS ...................: UKFTractography
</code></pre>
<p>Which I assume stems from the extension’s <code>CMakeLists.txt</code>: <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/610533480896d2884cb9ab0671c88874d237247d/CMakeLists.txt#L14" rel="noopener nofollow ugc">https://github.com/SlicerDMRI/SlicerDMRI/blob/610533480896d2884cb9ab0671c88874d237247d/CMakeLists.txt#L14</a></p>
<p>So there seems to be mismatch between what the extension states as its dependencies in its <code>CMakeLists.txt</code> file and the extension index <code>s4ext</code> file recipe.</p>
<p>Is there an automated way to keep these in sync?</p>

---

## Post #21 by @lassoan (2023-07-31 14:10 UTC)

<aside class="quote no-group" data-username="jhlegarreta" data-post="20" data-topic="30857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>Is there an automated way to keep these in sync?</p>
</blockquote>
</aside>
<p>Unfortunately not. The information in the CMakeLists.txt file and the s4ext file are redundant and may not be in sync - see more details <a href="https://github.com/Slicer/Slicer/issues/6434">here</a>.</p>

---

## Post #22 by @pieper (2023-07-31 14:11 UTC)

<aside class="quote no-group" data-username="jhlegarreta" data-post="19" data-topic="30857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>An intermediate step would be maybe to mark them as <code>Advanced</code> variables or grouped under a <code>Core</code> category</p>
</blockquote>
</aside>
<p>I like this idea <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #23 by @jamesobutler (2023-07-31 15:45 UTC)

<aside class="quote no-group" data-username="jhlegarreta" data-post="19" data-topic="30857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>I have good reasons to set up a CI on GitHub for the extension at issue.</p>
</blockquote>
</aside>
<p>Just curious, does the <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerDMRI" rel="noopener nofollow ugc">nightly build of the SlicerDMRI extension</a> across all platforms using the Slicer factory machines not suffice for the work that you are doing? Are you trying to avoid self-building the extension against a local build tree? Or are you also avoiding committing a change and then having to wait until the next day to see if the build is successful on the Slicer factory machines? Just wondering what development procedures others are using and how to improve things for development of other extensions</p>

---

## Post #24 by @lassoan (2023-07-31 16:50 UTC)

<p>The standard for CI today is immediate build for pull requests. It would be nice to achieve this for Slicer, too. Currently, most extension developers rely on local builds and the nightly automatic build. The only exception is OpenDose3D, which has <a href="https://gitlab.com/opendose/opendose3d/-/pipelines">CI pipeline</a> set up on gitlab.</p>

---

## Post #25 by @jhlegarreta (2023-07-31 19:00 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="23" data-topic="30857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Just curious, does the <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerDMRI" rel="noopener nofollow ugc">nightly build of the SlicerDMRI extension</a> across all platforms using the Slicer factory machines not suffice for the work that you are doing? Are you trying to avoid self-building the extension against a local build tree? Or are you also avoiding committing a change and then having to wait until the next day to see if the build is successful on the Slicer factory machines? Just wondering what development procedures others are using and how to improve things for development of other extensions</p>
</blockquote>
</aside>
<p>Andras has already stated the point in <a href="https://discourse.slicer.org/t/adding-a-ci-build-to-a-slicer-extension/30857/24">his answer</a>, but the idea is to be sure that any commit to the code (in this case, an extension) does not get merged unless (at least) tests are passing. The nightly builds are wonderful, and I am grateful for those of you who have set them up and maintain them, but they do not ensure this (and besides some maintainers, contributors rarely have a look at them, in my experience). This can save many hours of work when trying to collaborate with others, find bugs, etc.</p>

---

## Post #26 by @jamesobutler (2023-07-31 20:24 UTC)

<p>Got it. So the desire is to gate keep more to make sure code doesn’t break things prior to integration. This certainly seems more ideal.</p>
<p>For Slicer core and Slicer extensions it has historically been an integrate changes first, then review the build and testing results the following day to see what unexpectedly broke. This primarily being because developers likely test on one platform say Windows, but then their changes break things on macOS or Linux. Are you planning on setting up CI builds for Linux, macOS and Windows?</p>

---

## Post #27 by @jhlegarreta (2023-07-31 20:34 UTC)

<p>Thanks for understanding James.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="26" data-topic="30857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>This primarily being because developers likely test on one platform say Windows, but then their changes break things on macOS or Linux.</p>
</blockquote>
</aside>
<p>A CI running on all three OS, and assuming some essential tests check basic things, this risk would be minimized. A number of things would be discarded at least.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="26" data-topic="30857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Are you planning on setting up CI builds for Linux, macOS and Windows?</p>
</blockquote>
</aside>
<p>Long-term, ideal goal. Making this work on Linux would already be a first step. The rest can come later.</p>

---

## Post #28 by @jhlegarreta (2023-08-01 00:37 UTC)

<p>OK, I understand. Thanks Andras. Have gone through the repository, issue and documentation.</p>
<p>A few thoughts:</p>
<ul>
<li>At first, I thought that adding a parser to generate the <code>s4ext</code> file from the top-level <code>CMakeLists.txt</code> file of each extension would be useful, but I see that this is being done <a href="https://github.com/Slicer/Slicer/blob/079b3432d5e94465b658080cbce0bf077dbd28de/Extensions/CMake/SlicerFunctionExtractExtensionDescription.cmake" rel="noopener nofollow ugc">here</a> if I’m not mistaken using <code>CMake</code>, the issue then being the extension index repository not containing the same/reliable/duplicate information ?</li>
<li>Maybe such parser, e.g. a Python script, could still be useful to keep the information in sync ? It could directly read the extension’s <code>CMakeLists.txt</code> file (so the very same source the above <code>CMake</code> script uses) to populate the <code>s4ext</code> file? Ideally, the script could be executed nightly with a GHA workflow. The caveat would be that two different scripts, within different workflows, would be doing the same job.</li>
<li>Otherwise, a nightly run Slicer could push the generated <code>s4ext</code> files to the <code>ExtensionsIndex</code> repository and automatically open a PR if something has changed in the files ? This is maybe doable with little to reasonable effort ?</li>
</ul>

---

## Post #29 by @jhlegarreta (2023-08-01 12:51 UTC)

<p>Last two builds are passing:<br>
<a href="https://github.com/jhlegarreta/SlicerDMRI/actions" class="inline-onebox" rel="noopener nofollow ugc">Actions · jhlegarreta/SlicerDMRI · GitHub</a></p>
<p>So the PR is ready to be merged:<br>
<a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/172" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add GitHub actions build, test workflow file for CI by jhlegarreta · Pull Request #172 · SlicerDMRI/SlicerDMRI · GitHub</a></p>
<p>Thanks for all the pointers and thoughts.</p>

---
