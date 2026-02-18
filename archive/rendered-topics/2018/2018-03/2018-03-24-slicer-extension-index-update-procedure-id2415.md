# Slicer extension index update procedure

**Topic ID**: 2415
**Date**: 2018-03-24
**URL**: https://discourse.slicer.org/t/slicer-extension-index-update-procedure/2415

---

## Post #1 by @lassoan (2018-03-24 14:06 UTC)

<p>Different approaches are used for updating extension index. One is to specify git hashes, another is to define a branch name. We started an interesting discussion around a <a href="https://github.com/Slicer/ExtensionsIndex/pull/1542">pull request</a>. I copy it here so that the discussion can be joined by more developers.</p>
<p>From <a class="mention" href="/u/lassoan">@lassoan</a>:</p>
<blockquote>
<p>Manual updates of git hashes takes time and error-prone. You can make copy-paste errors, update the wrong s4ext file or the wrong branch of the ExtensionIndex, etc. It should be avoided.<br>
If for some reason you feel safer with having specific git hashes in the s4ext file then the update should be fully automatic. You can use <a class="mention" href="/u/jcfr">@jcfr</a>’s extension wizard scripts.<br>
However, a much cleaner and better controllable workflow is to use protected release branches and set the release branch name in the s4ext file instead of a specific hash. The release branch can be master or any other name. Protected branches can be configured to require reviews and be writeable only by certain users. Therefore, instead of enforcing Slicer core developers to click blindly on merging a new git hash, you can control what gets into the release in your own repository by defining your own rules that you set for the protected branch.</p>
</blockquote>
<p>From <a class="mention" href="/u/ihnorton">@ihnorton</a>:</p>
<blockquote>
<p>The protected branch is nice, simple, and almost zero-effort, so I think that would be great to encourage for all extensions where people don’t want to build off master in the short-term. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"><br>
Another potential approach is a release bot. There are a few around, but the one I’m most familiar with is “attobot” for Julia packages. It is a travis hook that runs on AWS Lambda; essentially watches any release-tags on a repository, and automatically makes a validated PR to the central index when a new release is created. Automated update was imperative for Julia with close to 2000 packages, because full manual review of every update PR by only 3-4 people was starting to be a big time-sink and blocker. It’s not so much an issue for ~100 extensions, but clean, validated automation is always nice in any case. The code is quite short and MIT licensed, so it wouldn’t be too crazy to just adapt it (if/when we have full continuous integration for extensions).</p>
</blockquote>

---

## Post #2 by @lassoan (2018-03-24 14:09 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a>, this is very interesting. Do you know how Julia packages are managed?</p>
<ul>
<li>What is the acceptance criteria for new revisions of a package? All tests defined in the package should pass?</li>
<li>What happens if there are test failures? What happens if tests fail due to Julia core changes?</li>
<li>Is there a dashboard where results can be monitored? Who keeps an eye on the dashboard?  What happens if problems are found with some packages?</li>
</ul>

---

## Post #3 by @ihnorton (2018-03-25 01:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2415">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What is the acceptance criteria for new revisions of a package?</p>
</blockquote>
</aside>
<p>Current requirements to register a package are <a href="https://github.com/JuliaLang/METADATA.jl/blob/metadata-v2/README.md">listed here</a>. Essentially: OSI license, and must list supported julia and dependency versions. For new revisions, attobot/testing is mostly to ensure that a package and all dependencies can be installed and loaded.</p>
<blockquote>
<p>All tests defined in the package should pass?</p>
</blockquote>
<p>As far as I know, there is no official requirement of tests right now, but when a registration PR is made, I think the author may be kindly asked to add some tests. Most do – there are <a href="https://docs.julialang.org/en/stable/stdlib/test/">very nice tools</a> possible in a language with <a href="https://docs.julialang.org/en/stable/manual/metaprogramming/">full AST macros</a>. The compiler also supports tracking coverage by line, and a <a href="https://github.com/JuliaCI/Coverage.jl">package provides integration</a> with a coverage reporting service (notifies if a PR changes coverage more than X %).</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2415">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What happens if there are test failures?</p>
</blockquote>
</aside>
<p>Responsibility of the authors. Package development is currently more <a href="https://en.wikipedia.org/wiki/The_Cathedral_and_the_Bazaar">bazaar than cathedral</a>. (at first of course everyone was just happy to have people contributing packages, but the criteria has become a little more stringent over time. Some scaling and curation needs were identified, so there is currently a transition in progress to a new package manager for Julia 1.0).</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2415">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is there a dashboard where results can be monitored?</p>
</blockquote>
</aside>
<p>Sort of, see <a href="https://pkg.julialang.org/pulse.html">https://pkg.julialang.org/pulse.html</a> — shows packages which pass their tests by core release version, and also passing-&gt;failing status changes (at the bottom).</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2415">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Who keeps an eye on the dashboard?</p>
</blockquote>
</aside>
<p>Everyone uses Travis and Appveyor to run tests, so most mature packages run tests on each PR. Like most open source, there is a range of maintenance commitment/availability by package developers, and varying contributor bases. There are companies maintaining various packages, which can indicate higher maintenance commitment in some cases.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2415">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What happens if problems are found with some packages?</p>
</blockquote>
</aside>
<p>If the original author/maintainer is unavailable to merge PRs and no one else has access, then the index can relatively easily be switched to point to a more maintained fork.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2415">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What happens if tests fail due to Julia core changes?</p>
</blockquote>
</aside>
<p>The language is stabilizing for 1.0 release this year, but of course there have been a number of core changes over time as the language was developed. Several strategies and tools have emerged:</p>
<ul>
<li>the language has a deprecation system which allows to support old syntax and many non-syntax feature deprecations during the deprecation period, and users get (opt-out) warnings when loading code.</li>
<li>there is a <a href="https://github.com/JuliaLang/Compat.jl">compatibility package</a>, which provides backward (and sometimes forward) compatible macros across versions (often as simple as putting <code>@compat</code> in front of some deprecated construct, and the macro figures out what code should be generated for the running version).</li>
<li>a bot is available which can automatically upgrade most syntax changes: <a href="https://github.com/JuliaComputing/FemtoCleaner.jl" class="inline-onebox">GitHub - JuliaComputing/FemtoCleaner.jl: The code behind femtocleaner</a> (it makes automatic pull-requests against registered packages)</li>
<li>there is a tool to automatically run all tests in all registered packages against a commit or PR: <a href="https://github.com/JuliaCI/PackageEvaluator.jl" class="inline-onebox">GitHub - JuliaCI/PackageEvaluator.jl: A tool to evaluate the quality of Julia packages.</a>. This is run for most major core changes, and many regressions are caught ahead of time with the system. It can help to identify which constructs are heavily used, to give a sense what new rules need to be added to FemtoCleaner prior to a release.</li>
</ul>
<p>—</p>
<p>[1] The main issues with the current system are: need for namespaced packages; need to support multiple, independent, federated indexes so that different groups can curate for their own needs (including companies with proprietary internal code); and need to stop using git to manage the extension index: the number of files and revisions in METADATA.jl scales very poorly at the current size, especially on Windows and NFS fileshares.</p>

---

## Post #4 by @jcfr (2018-03-25 02:04 UTC)

<blockquote>
<p>federated indexes so that different groups can curate for their own needs (including companies with proprietary internal code</p>
</blockquote>
<p>While the new implementation of the <a href="https://github.com/girder/slicer_package_manager#readme">Slicer extension mamnager</a> already support different application (Slicer, CustomSlicer1, …), we are currently discussing the <a href="https://github.com/girder/slicer_package_manager/issues/52">concept of channel</a> that would allow Slicer user to select “official extension” channel, or channel from a specific lab, …</p>

---

## Post #5 by @fedorov (2018-03-25 21:13 UTC)

<p>What we found to be a practical approach to work around the limitations of the current Slicer testing infrastructure and other Slicer-related issues is designing new functionality in modular fashion, and developing CLI modules in such a way that they can be built both as part of Slicer, but also as standalone projects using cmake superbuild. The advantages of this approach are numerous:</p>
<ul>
<li>we can use standard continuous integration tools for testing (a lot more intuitive interface, notifications, integration with GitHub, orders of magnitude faster test execution, 0 maintenance of the server, ability to ssh to the server VM using GitHub credentials to troubleshoot failures if needed)</li>
<li>we can use CI for generating standalone packages of the tools that can then be used independently of Slicer</li>
<li>developers can build extensions without having to build the whole Slicer app</li>
<li>CLI functionality is accessible without the baggage of Slicer dependencies, if users want to use just the CLI tools</li>
<li>no launcher for the standalone packages, which makes them a lot more intuitive to use from command line on Windows as compared to the Slicer-packaged CLIs</li>
<li>size of a docker image containerizing the tool is a lot smaller</li>
</ul>
<p>We applied this approach to <a href="https://github.com/qiicr/dcmqi">dcmqi</a>, and more recently to <a href="https://github.com/QIICR/PkModeling">PkModeling</a>, and I really like it. The initial effort was significant, with <a class="mention" href="/u/jcfr">@jcfr</a> doing all the heavy lifting for dcmqi, but we were able to do the same thing for PkModeling without much problems.</p>
<p>Going forward, I think it would be quite helpful to have a CLI extension skeleton generator that incorporates cmake superbuild to allow Slicer-independent extensions.</p>

---

## Post #6 by @dzenanz (2018-03-26 15:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="2415">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>a much cleaner and better controllable workflow is to use protected release branches and set the release branch name in the s4ext file instead of a specific hash</p>
</blockquote>
</aside>
<p>I like this approach more, because of its simplicity. Using buildbots and more complicated configurations increase “barrier to entry” for the Slicer ecosystem.</p>

---

## Post #7 by @lassoan (2018-03-26 17:16 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a> Thank you for the answers. It is interesting to see how an extension system can scale. I’ve learned a lot.</p>

---
