# Custom Slicer distributions

**Topic ID**: 559
**Date**: 2017-06-23
**URL**: https://discourse.slicer.org/t/custom-slicer-distributions/559

---

## Post #1 by @lassoan (2017-06-23 14:13 UTC)

<p>Goal of “SlicerVerse” (“Slicer universe”) is to offer custom Slicer distributions built on the same Slicer core but pre-configuret for specific applications (<a href="https://discourse.slicer.org/t/communities-slicerverse/40/22">Communities / “SlicerVerse”</a>).</p>
<p>It is important to decide how much these custom distributions should be separated from the vanilla Slicer distribution.</p>
<ol>
<li>Should the application name be still “Slicer”?</li>
</ol>
<p>It has many implications.</p>
<p>Application name is used in the install package name, start menu shortcut, title bar of the application. It is easier to find/distinguish a custom distribution if it has a custom name.</p>
<p>Application name is also used for storing application settings (.ini files). If the application name is not “Slicer” then all user and version-specific settings are separate from the vanilla Slicer distribution settings. This can be useful, as you can set up custom startup module and other application settings separately for each distribution.</p>
<p>Only one application of a specific name and version may be installed at a time.</p>
<ol start="2">
<li>Should custom distributions be able to download additional extensions from the Slicer appstore?</li>
</ol>
<p>If yes, then these custom distributions should be built on official factory machines so that ABI compatibility can be guaranteed.<br>
Theoretically it could be possible to set up identical build environments, but it would be hard to ensure they are kept in sync (OS, compiler updates, environment variables, etc. may all affect the binaries). Also, application signing would be easier to set up at one place (we still have not managed to set it up for current Slicer).</p>
<p><a class="mention" href="/u/bpaniagua">@bpaniagua</a>, <a class="mention" href="/u/ihnorton">@ihnorton</a> <a class="mention" href="/u/ljod">@ljod</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> - What do you think?</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Do you think Kitware build machines could cope with a couple of more Slicer core nightly builds? Dependencies (VTK, ITK, CTK, DCMTK, …) could be built once and used for building all custom distributions. Extensions would be probably also shared between all.</p>

---

## Post #2 by @ihnorton (2017-06-23 15:05 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Should custom distributions be able to download additional extensions from the Slicer appstore?<br>
If yes, then these custom distributions should be built on official factory machines so that ABI compatibility can be guaranteed.</p>
</blockquote>
</aside>
<p>My $.02 is that it would be ideal to package these distributions from a single official nightly. Even ignoring build machine load, multiple separate builds could add a lot of confusion, maintenance overhead, etc.</p>
<p>If we wanted to keep it really simple and don’t mind trading some package size, we could even bundle everything (the extensions aren’t <em>that big</em>, are they?), and do something clever with the installer to make it activate only some bundles by default, perhaps based on the download name or a prompt (the others would still be available from the extension manager).</p>
<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Theoretically it could be possible to set up identical build environments, but it would be hard to ensure they are kept in sync</p>
</blockquote>
</aside>
<p>Now that docker is natively available on all platforms, we might be able to have standardized build images for all platforms, which would also (somewhat) resolve the long-standing SDK request. (modulo license restrictions for MSVC, not sure how that works, but I have seen docker-windows build images…)</p>

---

## Post #3 by @lassoan (2017-06-23 15:31 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="2" data-topic="559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>My $.02 is that it would be ideal to package these distributions from a single official nightly</p>
</blockquote>
</aside>
<p>If we customize the application name then it has to be a rebuild (at least of the application components) not just a repackaging, but we can reuse all the pre-built dependencies, so it wouldn’t be a big burden.</p>
<aside class="quote no-group" data-username="ihnorton" data-post="2" data-topic="559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>the extensions aren’t that big, are they?</p>
</blockquote>
</aside>
<p>Total size of all zipped nightly extension packages on Windows is 217MB.</p>
<p>Current Slicer installer is 188MB, and when EMSegmenter will be spun out to a separate extension then Slicer core installer will be only about 120MB. Bundling all the extensions would increase the package size to about 400MB, so bundling all extensions would result in a 3x larger install package.</p>
<p>Overall, bundling all extension is an interesting idea but I’m not sure if it is the best solution and it would not scale very well as more extensions are added.</p>
<aside class="quote no-group" data-username="ihnorton" data-post="2" data-topic="559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>Now that docker is natively available on all platforms, we might be able to have standardized build images for all platforms</p>
</blockquote>
</aside>
<p>Good point. I don’t know how easy it is to have Windows docker images. Docker for Windows runs Linux images, but maybe some recent Windows server versions can now run Windows images, too? Visual Studio Community license is free, but Windows OS license is not - I don’t know how that is handled.</p>

---

## Post #4 by @ihnorton (2017-06-23 15:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If we customize the application name then it has to be a rebuild (at least of the application components) not just a repackaging, but we can reuse all the pre-built dependencies, so it wouldn’t be a big burden.</p>
</blockquote>
</aside>
<p>I was basically envisioning a customized launcher name only (maybe icon too), possibly at install time. But maybe I’m underestimating the work/complication there, or overestimating feasibility with CMake and CPack.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Docker for Windows runs Linux images, but maybe some recent Windows server versions can now run Windows images, too?</p>
</blockquote>
</aside>
<p>Yes, exactly.</p>

---

## Post #5 by @pieper (2017-06-23 16:38 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="4" data-topic="559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>If we customize the application name then it has to be a rebuild (at least of the application components) not just a repackaging, but we can reuse all the pre-built dependencies, so it wouldn’t be a big burden.</p>
<p>I was basically envisioning a customized launcher name only (maybe icon too), possibly at install time. But maybe I’m underestimating the work/complication there, or overestimating feasibility with CMake and CPack.</p>
</blockquote>
</aside>
<p>You can change the application name and settings without recompiling.  I added that for the <a href="https://github.com/pieper/CustomSlicerGenerator">CustomSlicerGenerator</a>.  I don’t think we change the app icon right now, but that’s also possible to do without recompiling.</p>
<p>OTOH I do like the idea of using containers to build extensions on-the-fly for all the different platforms.  This would allow anyone to build a ‘mini factory’ to update extensions against particular slicer builds.</p>

---

## Post #6 by @ljod (2017-06-23 17:31 UTC)

<p>Currently we have an extension and that works well. I’m not sure why all SlicerVerse packages need a custom full Slicer installation (distribution). If the name becomes distribution, this is implied, but I don’t think it has to be a requirement for everything. It seems like more to maintain. Thoughts?</p>

---

## Post #7 by @lassoan (2017-06-23 17:35 UTC)

<p>I’ve checked the code and indeed application name is not hardcoded anywhere but it is determined from the application executable name at startup. So, you can get quite close to a usable solution using CustomSlicerGenerator. However, there are two limitations:</p>
<ol>
<li>CustomSlicerGenerator does not give you an installer package. We cannot just dump a zip file on the user (at least on Windows it doesn’t work).</li>
<li>Another issue is replacing resources. CTKResEdit can replace standard windows resources (such as the application icon). However, Qt resources (referenced by the qrc file) are compressed, converted to C++ code, and compiled into the Qt C++ program. These cannot be changed after the application is built.</li>
</ol>

---

## Post #8 by @ihnorton (2017-06-23 17:41 UTC)

<p>Agree. I’m happy with SlicerDMRI as an extension for now too.</p>

---

## Post #9 by @bpaniagua (2017-06-23 17:44 UTC)

<p>I agree with Lauren. We should not force our users to create custom distributions of Slicer. Extensions are fine.<br>
However, all extensions cant be considered Slicer Distributions. This falls along a definition of what constitutes a SlicerDistribution.</p>
<p>We talked about the fact it needs to be customized to the needs of a certain biomedical community and be self-sufficient by itself (no matter if it is an extension or a Slicer package)</p>
<p>The reason why I decided going through the hassle of creating SlicerCMF and Salt as their own packages is because our specific communities struggled installing extensions (they did). Also, because you can create a snapshot of your program/extension in time to avoid having to keep the extension current with Slicer.</p>
<p>Nothing that anybody with an extension cant do with the SlicerCustomGenerator.</p>

---

## Post #10 by @lassoan (2017-06-23 17:45 UTC)

<aside class="quote no-group" data-username="ljod" data-post="6" data-topic="559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ljod/48/652_2.png" class="avatar"> ljod:</div>
<blockquote>
<p>I’m not sure why all SlicerVerse packages need a custom full Slicer installation (distribution).</p>
</blockquote>
</aside>
<p>What do you mean by a “SlicerVerse package”?</p>
<p>Options existing today:</p>
<ol>
<li>User downloads standard Slicer installer and installs extensions manually.</li>
<li>Custom installers (have custom application name, some additional extensions are bundled, some modules are excluded) - this can be built without modifying anything in Slicer source code, just by tuning CMake options (except resources, which currently cannot be customized through CMake). No extension manager access.</li>
<li>CustomSlicerGenerator: It kind of works but currently has two serious limitations (no installer; resources are not customizable).</li>
</ol>
<p>We are happy with Option 1 for most cases. For some use cases (commercial applications, clinical installations) we use Option 2.</p>

---

## Post #11 by @lassoan (2017-06-23 17:47 UTC)

<aside class="quote no-group" data-username="bpaniagua" data-post="9" data-topic="559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bpaniagua/48/20_2.png" class="avatar"> bpaniagua:</div>
<blockquote>
<p>SlicerCMF and Salt as their own packages</p>
</blockquote>
</aside>
<p>What is a SlicerCMF and Salt package? A custom installer? Does it use a custom application name (custom settings, etc)?<br>
How you distribute it? How do you update it?<br>
Does it have access to the extension manager?</p>

---

## Post #12 by @bpaniagua (2017-06-23 17:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>CustomSlicerGenerator does not give you an installer package. We cannot just dump a zip file on the user (at least on Windows it doesn’t work).</p>
</blockquote>
</aside>
<p>What do you mean we cant dump a zip file on the user? We have done that in the past, and people has had no problem using the unzipped package. SlicerCustomGenerator fixes the paths during the first time you run the program.</p>

---

## Post #13 by @bpaniagua (2017-06-23 17:54 UTC)

<blockquote>
<p>What is a SlicerCMF and Salt package? A custom installer? Does it use a custom application name (custom settings, etc)?</p>
</blockquote>
<p>They are generated differently. SlicerCMF uses SlicerCustomGenerator, with the idiosyncrasie that we are discussing.   SlicerSALT uses a different library that does create installers and allows customizing the application name, the colors etc.</p>
<blockquote>
<p>How you distribute it?</p>
</blockquote>
<p>Distribution is where I see the biggest problem. You have to use your own resources, hosting, etc.</p>
<blockquote>
<p>How do you update it?</p>
</blockquote>
<p>SlicerCMF - download a new Slicer package for the customization<br>
SlicerSALT - update Slicer git tag as part of the build</p>
<blockquote>
<p>Does it have access to the extension manager?</p>
</blockquote>
<p>It can, it is configurable. I have decided to hide the extension manager in both packages, just because I am trying to remove cluter from the packages. Both SlicerCMF and SlicerSALT modules are distributed initially as part of the Slicer proper extension mechanism (in that way we give back to the community). So if a user wants to use any of the CMF or SALT extensions in conjunction with other tools, that can be done through Slicer proper.</p>

---

## Post #14 by @ljod (2017-06-23 18:16 UTC)

<p>For this reason I disagree with the name “Distribution.” Our original idea was to advertise the communities and dedicated application-specific software packages that have grown up with Slicer. I prefer the name Communities to Distributions, for example, though I don’t know what is the perfect name.</p>

---

## Post #15 by @lassoan (2017-06-23 18:27 UTC)

<p>Yes, there are <em>communities</em> who use/develop different <em>distributions</em>. I would use the “distribution” word instead of “package”. Now we just have to figure out what a “package” should mean.</p>

---

## Post #16 by @lassoan (2017-06-23 18:39 UTC)

<aside class="quote no-group" data-username="bpaniagua" data-post="13" data-topic="559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bpaniagua/48/20_2.png" class="avatar"> bpaniagua:</div>
<blockquote>
<p>They are generated differently.</p>
</blockquote>
</aside>
<p>I think we should agree in one method that is acceptable for all needs. It is enough work to specify, implement, and maintain one new mechanism.</p>
<aside class="quote no-group" data-username="bpaniagua" data-post="13" data-topic="559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bpaniagua/48/20_2.png" class="avatar"> bpaniagua:</div>
<blockquote>
<p>SlicerCMF uses SlicerCustomGenerator, with the idiosyncrasie that we are discussing.   SlicerSALT uses a different library that does create installers and allows customizing the application name, the colors etc.</p>
</blockquote>
</aside>
<p>SlicerCMF = Option 3: I don’t think SlicerCustomGenerator’s lack of installer and resource customization are acceptable and the main problem is that I don’t know about any possible fix (that would work without rebuilding the application).</p>
<p>SlicerSALT = Option 2: I think this could be usable. We just have to make sure that no Slicer core source code has to be modified (for maintainability, binary compatibility, etc). As far as I know, <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Customizing_application_build">all necessary parameters can be customized via CMake variables</a>. The only current limitation is that changing resources requires changing Slicer core files - but this should be fixable.</p>
<p>In SlicerSALT repository do you change anything else than resource files to customize your application?</p>

---

## Post #17 by @ihnorton (2017-06-23 20:32 UTC)

<p>3 posts were split to a new topic: <a href="/t/customized-application-launchers/564">Customized application launchers</a></p>

---

## Post #19 by @ihnorton (2017-06-23 20:37 UTC)

<p>There are at least three conversations here.</p>
<p>One is the question about what to call the thing at the top of the landing page, for linking/advertising “topical <s>groups</s> <em>Communities</em> with a website and funding” -&gt; I suggest taking this conversation back to the other thread:  <a href="https://discourse.slicer.org/t/communities-slicerverse/40">Communities / “SlicerVerse”</a></p>
<p>Then there is a technical, logistical, and maintenance question of:</p>
<ul>
<li>improving capabilities to create customized bundles</li>
<li>creating such bundles on a regular basis (perhaps on behalf of a <s>team</s> <em>Community</em> as defined above – but by no means are they required to do so)</li>
</ul>
<p>-&gt; <strong>this thread!?!</strong></p>
<p>And the related question of: including custom launchers in a bundle, installer, and/or extension. -&gt; I suggest moving to a new thread: <a href="https://discourse.slicer.org/t/customized-application-launchers/564">Customized application launchers</a></p>

---

## Post #20 by @fedorov (2017-06-23 22:44 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a> now I am double lost, since I get an impression individual messages are being moved across the threads that are being split and merged again …</p>
<p>I have to say that I really don’t like the feature of Discourse of moving messages around. It is super confusing to me, and in fact discourages to contribute to the discussion.</p>

---

## Post #21 by @lassoan (2017-06-23 23:03 UTC)

<p>I love the possibility to have clear discussion threads, but the discussion was so complex already that I agree that splitting just made it much harder to follow. We can still merge it back to one thread again - but I’m not sure if it would help or make things even worse.</p>
<p>Anyway, I think we are talking about several things and we don’t even have a common agreement about what we are talking about.</p>
<p>Should we try to keep discussing this in writing or set up a teleconference instead?</p>

---

## Post #22 by @ihnorton (2017-06-23 23:42 UTC)

<p>Ok, sorry. I can see how splitting made it even more confusing. The feature is very nice when there is a more clear break to follow.</p>

---

## Post #23 by @fedorov (2017-06-24 01:26 UTC)

<p>Having learned from my own mistakes, I made a new thread to discuss the topic of splitting threads <a href="https://discourse.slicer.org/t/splitting-of-the-discussions/566">Splitting of the discussions</a></p>
<p>I don’t have a good idea how to salvage this one though!</p>

---
