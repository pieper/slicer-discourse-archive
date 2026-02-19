---
topic_id: 4531
title: "Slicerelastix Extension Not Available On Mac"
date: 2018-10-25
url: https://discourse.slicer.org/t/4531
---

# SlicerElastix extension not available on Mac

**Topic ID**: 4531
**Date**: 2018-10-25
**URL**: https://discourse.slicer.org/t/slicerelastix-extension-not-available-on-mac/4531

---

## Post #1 by @cpinter (2018-10-25 19:57 UTC)

<p>Hi all,</p>
<p>I wanted to show a Mac user the SlicerElastix extension but it was not there. After a bit of investigation, it turns out that it does not build at least since February.<br>
Here’s the <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=Elastix">latest dashboard</a> and the <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1411238">error</a> (and the <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-02-17&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=Elastix">oldest available dashboard</a>).</p>
<p>Does anyone know what is needed in order to fix this? Can someone who usually develops on Mac check it out? Elastix is a great registration tool, we should have it in 4.10.</p>
<p>Thanks,<br>
csaba</p>

---

## Post #2 by @cpinter (2018-11-05 20:06 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> managed to compile it locally. There were tons of warnings but no errors.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> It seems on the <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1423261">dashboard</a> that the same thing happened as for Kyle, but the warnings are somehow treated as errors. Maybe fixing the wrong parsing of the log would solve the problem?</p>
<p>Thanks!</p>

---

## Post #3 by @lassoan (2018-11-05 22:20 UTC)

<p>I think build log parsing is only used for categorizing messages for dashboard display and does not have an effect on the build process (build error is detected by getting non-zero exit value of compiler and linker process).</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you try to build with latest Elastix version?</p>

---

## Post #4 by @Sunderlandkyl (2018-11-05 23:16 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Compiles fine using the most recent Elastix version in the master branch (once some paths are changed in elastix_patch.cmake).</p>

---

## Post #5 by @lassoan (2018-11-05 23:45 UTC)

<p>Great! Could you please send a pull request with the necessary changes and the git hash you have tested with? Maybe build will succeed with this new version. Thank you!</p>

---

## Post #6 by @cpinter (2018-11-06 14:32 UTC)

<p>Or we could use the master instead of a hash.</p>

---

## Post #7 by @jcfr (2018-11-07 06:36 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="4" data-topic="4531">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>Compiles fine using the most recent Elastix version in the master branch</p>
</blockquote>
</aside>
<p>Nice work finding out the source of the problem <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=14" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="4531" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Or we could use the master instead of a hash.</p>
</blockquote>
</aside>
<p>That said, I recommend against using the master branch in the actual extension code. This will make integration in custom application difficult as checking the code on day1 and on day2 could lead to different behavior and could make the reproduction of results very challenging, and the tracking of error difficult.</p>

---

## Post #8 by @cpinter (2018-11-07 13:58 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="7" data-topic="4531">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>checking the code on day1 and on day2 could lead to different behavior</p>
</blockquote>
</aside>
<p>Not sure I agree.</p>
<ul>
<li>Fixed hash: You build the custom app on day 1, with extension hash A. Then you build custom app on day 2 with extension hash B. There is a bug related to extension. You need to go to the extension index and see which hash was used on day 1 and 2, and compare the two hashes</li>
<li>Master: You build the custom app on day 1, with extension hash A. Then you build custom app on day 2 with extension hash B. There is a bug related to extension. You need to go to the extension repository and see what was the head each time. Compare the two hashes.</li>
</ul>
<p>To me the two workflows seem to take the same amount of effort, except if there were many commits on day 1 in the second case, but le’s face it it’s very unlikely.<br>
On the other hand when you change anything in an extension that you want to make its way into the release you need to update the hash every single time in extension index, which is significant overhead, not mentioning the fact that it’s easy to forget about.</p>

---

## Post #9 by @Sunderlandkyl (2018-11-07 15:19 UTC)

<p>The build is still failing in the same way as before, so changing the elastix version did not seem to have an effect: <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1425226" rel="nofollow noopener">http://slicer.cdash.org/viewBuildError.php?buildid=1425226</a>.</p>

---

## Post #10 by @fedorov (2018-11-07 15:51 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="8" data-topic="4531">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Master: You build the custom app on day 1, with extension hash A. Then you build custom app on day 2 with extension hash B. There is a bug related to extension. You need to go to the extension repository and see what was the head each time. Compare the two hashes.</p>
</blockquote>
</aside>
<p>I don’t think this will be easy, and sometime it may not be possible. If you have SlicerElastix that depends on elastix “master” branch, it might be challenging to figure out which exact hash was checked out based on the specific time of the build. Imagine the scenario when prolific elastix developers make several commits on the night (morning in Europe) when Slicer dashboards checks out SlicerElastix.</p>
<p>+1 for FixedHash of the elastix repo and “master” for SlicerElastix in SlicerElastix.s4ext.</p>

---

## Post #11 by @cpinter (2018-11-07 15:56 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="10" data-topic="4531">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>+1 for FixedHash of the elastix repo and “master” for SlicerElastix in SlicerElastix.s4ext</p>
</blockquote>
</aside>
<p>I was talking about the ExtensionIndex, not the Elastix external in the superbuild extension. So I agree with this.</p>

---

## Post #12 by @fedorov (2018-11-07 15:58 UTC)

<p>Sorry for my confusion!</p>
<p>ps I thought <a class="mention" href="/u/jcfr">@jcfr</a> was talking about actual hash for elastix, not SlicerElastix.</p>

---

## Post #13 by @cpinter (2018-11-07 16:06 UTC)

<p>Probably he did and I was the one who misunderstood <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>We also use fixed hash for superbuild extension dependencies, and I agree with <a class="mention" href="/u/jcfr">@jcfr</a>’s concerns about that.</p>

---

## Post #14 by @lassoan (2018-11-07 22:25 UTC)

<p>I’ve updated SlicerElastix to use a specific Elastix hash.</p>

---

## Post #18 by @cpinter (2018-11-12 15:01 UTC)

<p>The build still fails. The errors still look like warnings, most of them (all of the ones I read) the type "overrides a member function but is not marked ‘override’ ".</p>
<p>It still seems to me that the problem is only with parsing the output, given that <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> built it successfully.<br>
<a class="mention" href="/u/jcfr">@jcfr</a> could you take a look at this <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1429401">dashboard entry</a> please? You’ll probably see the problem immediately.</p>

---

## Post #19 by @lassoan (2018-11-12 19:42 UTC)

<p>Log parser in CTest may misinterpret messages, but this does not affect the build process. Only return value  of compiler, linker, etc. process execution matters. The easiest would be to restart the build on the factory machine. Then most likely the warnings would not be displayed again and you would immediately see the actual build error message.</p>

---

## Post #20 by @cpinter (2019-02-21 15:29 UTC)

<p>For the record, Mac build of SlicerElastix is available as of February 13.</p>

---
