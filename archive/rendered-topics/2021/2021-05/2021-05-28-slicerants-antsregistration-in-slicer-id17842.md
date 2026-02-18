# SlicerANTs antsRegistration in Slicer

**Topic ID**: 17842
**Date**: 2021-05-28
**URL**: https://discourse.slicer.org/t/slicerants-antsregistration-in-slicer/17842

---

## Post #1 by @simonoxen (2021-05-28 14:19 UTC)

<p>Hi,</p>
<p>Just made a PR to ExtensionsIndex to add <a href="https://github.com/simonoxen/SlicerANTs" rel="noopener nofollow ugc">SlicerANTs</a> extension, which implements antsRegistration.</p>
<p>Probably needs some fixes, but it’s currently functional.</p>
<p>This effort is based on the following:</p>
<ul>
<li><a href="https://github.com/ANTsX/ANTs" rel="noopener nofollow ugc">ANTs has publications supporting it’s accuracy</a></li>
<li>Allows for using multiple metrics. (For example using multiple MRI sequences to normalise to MNI).</li>
<li>Highly customisable (I guess this is pro and con depending on the user level)</li>
</ul>
<p>I tried to keep it understandable despite the vast amount of parameters it has. Any feedback is welcome!</p>
<p>I used a json string as a parameter in the parameter node to keep up with this amount of settings. Also, I stored presets as json files so loading them is straightforward. Is this a good practice?</p>
<p>It was mostly based on the <a href="https://github.com/lassoan/SlicerElastix" rel="noopener nofollow ugc">SlicerElastix</a> implementation, from which I copied parts of code.</p>
<p>Best</p>

---

## Post #2 by @muratmaga (2021-05-28 16:53 UTC)

<p>This is great. Do you have it for windows platform too?</p>

---

## Post #3 by @simonoxen (2021-05-31 06:31 UTC)

<p>yes, it builds, but there’s still work needed to integrate with Slicer ITK</p>

---

## Post #4 by @simonoxen (2021-06-18 10:37 UTC)

<p>Hi, just tested with latest nightly in win, mac and ubuntu and is working! Thanks <a class="mention" href="/u/lassoan">@lassoan</a> for the contributions during the PR!</p>
<p>Further work includes:</p>
<ul>
<li>Merging compilation modifications back to ants repo so as to checkout from there.</li>
<li>Making the Advanced section more robust (currently could run to some errors with some settings if not familiarised).</li>
<li>Adding more presets.</li>
</ul>
<p>Hope this is helpful</p>

---

## Post #5 by @slicer365 (2021-06-18 12:53 UTC)

<p>Failed!  A problem with my software.</p>
<p>win 64</p>
<h1><a name="p-61508-h-1" class="anchor" href="#p-61508-h-1" aria-label="Heading link"></a></h1>
<p>antsCommand standard error:</p>
<p>Traceback (most recent call last):<br>
File “E:/Slicer/Slicer41120210226/OpenExtentions/SlicerANTs-master/antsCommand/antsCommand.py”, line 131, in<br>
process = runAntsCommand(antsExecutable, antsCommand, outputLogPath)<br>
File “E:/Slicer/Slicer41120210226/OpenExtentions/SlicerANTs-master/antsCommand/antsCommand.py”, line 12, in runAntsCommand<br>
executableFilePath = os.path.join(getAntsBinDir(), executableFileName)<br>
File “E:/Slicer/Slicer41120210226/OpenExtentions/SlicerANTs-master/antsCommand/antsCommand.py”, line 55, in getAntsBinDir<br>
raise ValueError(‘ANTs not found’)<br>
ValueError: ANTs not found</p>
<h1><a name="p-61508-h-2" class="anchor" href="#p-61508-h-2" aria-label="Heading link"></a></h1>

---

## Post #6 by @simonoxen (2021-06-18 13:15 UTC)

<p>hi, doesn’t seem you installed via Extension Manager in latest nightly</p>
<p>Best</p>

---

## Post #7 by @slicer365 (2021-06-18 13:18 UTC)

<p>I downloaded it from Github，then installed it via developer Tools.</p>

---

## Post #8 by @simonoxen (2021-06-18 13:20 UTC)

<p>You need to install via Extension Manager from a nightly build (starting today)</p>

---

## Post #9 by @muratmaga (2021-06-20 00:30 UTC)

<p><a class="mention" href="/u/simonoxen">@simonoxen</a> I tried with the latest build and it seems to work fine, thank you this nice work. It is great to be able to explore the parameters and visualize the outcome in the same place.</p>
<p>Can you consider saving/outputting the actual antsRegistration call somewhere, so that we can use that parameter set directly on with ANTs or ANTsR when we are running a large number of samples programmatically?</p>

---

## Post #10 by @lassoan (2021-06-20 19:52 UTC)

<p><a class="mention" href="/u/simonoxen">@simonoxen</a> The module is intuitive and fast and works very robustly. Thanks a lot for your contribution! It would be great if you could create a short YouTube video that shows a few basic and maybe some more advanced use cases in 1-2 minutes.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> you can find the command line argument list that is passed to ants in the application log.</p>

---

## Post #11 by @muratmaga (2021-06-20 19:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="17842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> you can find the command line argument list that is passed to ants in the application log.</p>
</blockquote>
</aside>
<p>I know but it is always better to write them explicitly to disk (in json or whatever) for posterity. If I close the application, I may loose the parameters (I know the logs exists for a while, but still…)</p>

---

## Post #12 by @lassoan (2021-06-20 21:13 UTC)

<p>If you created one or a few files at each execution of ANTS, when those file would be deleted? (you don’t want to end up with potentially hundreds of temporary files if you perform registration many times)</p>
<p>Saving the parameters into the log is nice because the last 10-15 log files are preserved but older ones are cleaned up automatically. You would normally get the parameters right after the successful registration anyway, so it should not be even necessary to dig into the archived log files.</p>

---

## Post #13 by @simonoxen (2021-06-21 06:41 UTC)

<p>Thanks!</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="17842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would be great if you could create a short YouTube video that shows a few basic and maybe some more advanced use cases in 1-2 minutes.</p>
</blockquote>
</aside>
<p>I’ll add this to my to-do.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I didn’t think about it, but the log files seem to be a good solution.</p>

---

## Post #14 by @simonoxen (2021-11-08 16:36 UTC)

<p>Hi, I made some changes in the implementation of this extension.</p>
<ul>
<li>I made a <a href="https://github.com/ANTsX/ANTs/pull/1260" rel="noopener nofollow ugc">small contribution</a> to the ANTs project and now I checkout from there.</li>
<li>ANTs is built with shared libraries and linked to a new <a href="https://github.com/netstim/SlicerANTs/tree/master/antsRegistrationCLI" rel="noopener nofollow ugc">antsRegistrationCLI module</a>.</li>
<li>ANTs is <a href="https://github.com/netstim/SlicerANTs/blob/master/SuperBuild/ants_patch.cmake" rel="noopener nofollow ugc">patched</a> to communicate CLI progress with Slicer.</li>
<li>The CLI modules manages all the I/O making the implementation much cleaner.</li>
<li>I also migrated the repo to the <a href="https://github.com/netstim" rel="noopener nofollow ugc">netstim</a> organization and made a <a href="https://github.com/Slicer/ExtensionsIndex/pull/1797" rel="noopener nofollow ugc">PR</a> to update this is in the Extension Index.</li>
</ul>
<p>One question I had is wether shared or static libraries is preferred to build an external project (ANTs in this case). Any comments on this?</p>
<p>Thanks</p>

---

## Post #15 by @lassoan (2021-11-08 17:01 UTC)

<aside class="quote no-group" data-username="simonoxen" data-post="14" data-topic="17842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/simonoxen/48/66398_2.png" class="avatar"> simonoxen:</div>
<blockquote>
<p>One question I had is wether shared or static libraries is preferred to build an external project (ANTs in this case). Any comments on this?</p>
</blockquote>
</aside>
<p>Often the maintainers of a library has a preference (they mainly test with statically-linked or shared libraries) and if that’s the case then we follow that. If there is no preference then the decision factors include expected binary compatibility issues (if the library is widely used as a shared library in different projects and no name mangling is supported then it is safer to link statically) and binary size (if the library size is big and the project provides many executables then shared libraries can cut down the size very significantly).</p>
<p>Since we only use a single executable and binary compatibility might come up as an issue when Slicer is used in a workflow that already uses ANTs, it might make sense to link statically.</p>
<aside class="quote no-group quote-modified" data-username="simonoxen" data-post="13" data-topic="17842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/simonoxen/48/66398_2.png" class="avatar"> simonoxen:</div>
<blockquote>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="17842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would be great if you could create a short YouTube video that shows a few basic and maybe some more advanced use cases in 1-2 minutes.</p>
</blockquote>
</aside>
<p>I’ll add this to my to-do.</p>
</blockquote>
</aside>
<p>This would be really nice if you could do this. If you wrote a short post about the module (in “Support” category, with “feature” tag added) and included a short video demo/tutorial then we could advertise this further on twitter etc. and the impact of your work would be increased a lot. Thanks again for your contribution!</p>

---
