---
topic_id: 3125
title: "No 4 8 1 Windows Builds Since March 14"
date: 2018-06-08
url: https://discourse.slicer.org/t/3125
---

# No 4.8.1 windows builds since March 14

**Topic ID**: 3125
**Date**: 2018-06-08
**URL**: https://discourse.slicer.org/t/no-4-8-1-windows-builds-since-march-14/3125

---

## Post #1 by @cpinter (2018-06-08 13:45 UTC)

<p>I have been checking the stable builds for a while because I didn’t see windows builds. As the problem does not seem to go away I’d like to bring it up here.</p>
<p>On May 3rd, there were still builds for Windows:<br>
<a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-05-03" class="onebox" target="_blank">http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-05-03</a><br>
It stopped the next day:<br>
<a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-05-04" class="onebox" target="_blank">http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-05-04</a><br>
And it’s still the same today:<br>
<a href="http://slicer.cdash.org/index.php?project=Slicer4" class="onebox" target="_blank">http://slicer.cdash.org/index.php?project=Slicer4</a></p>
<p>Can someone with access to the factories check what’s going on? Thanks!</p>
<p>Update: Sorry my bad, those windows builds were from our build servers. The official Windows factory for stable release is down for even longer, possible since March 14<br>
<a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-03-14" class="onebox" target="_blank">http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-03-14</a><br>
vs<br>
<a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-03-13" class="onebox" target="_blank">http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-03-13</a></p>

---

## Post #2 by @cpinter (2018-06-11 18:51 UTC)

<p>Also no extensions built since Friday. This is the first dashboard with no extensions:<br>
<a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-06-09" class="onebox" target="_blank">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-06-09</a></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Can you please take a look at the 4.8.1 issue and the nightly extensions issue? Or give others access to the factory. Thanks!</p>

---

## Post #3 by @Sam_Horvath (2018-06-11 20:27 UTC)

<p>Working on this!</p>
<p>For the extensions issue, the culprit appears to be: <a href="https://github.com/Slicer/ExtensionsIndex/commit/3f19331f9dac74b6873fccbb043f73a5820171b7" rel="nofollow noopener">https://github.com/Slicer/ExtensionsIndex/commit/3f19331f9dac74b6873fccbb043f73a5820171b7</a></p>
<p>The SlicerZFrameRegistration dependency is actually just named ZFrameRegistration.  This is creating a dependency on a non-existent .s4ext file that is breaking the configuration step.  We should fix the dependency, but we should also look into how to not have this type of thing jam up the whole process.</p>

---

## Post #4 by @Sam_Horvath (2018-06-11 22:16 UTC)

<p>Update:  the 4.8.1 windows extension error seems to have been caused during the refactoring of the factories during the Preview/Stable setup.  Hopefully will be fixed for tonight’s extensions.</p>

---

## Post #5 by @cpinter (2018-06-12 13:50 UTC)

<p>Thank you very much, Sam, for the prompt response and action <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #6 by @cpinter (2018-06-13 19:23 UTC)

<p>Today there are again no 4.8.1 windows extension builds. Not sure if it’s a one-time problem, or that somehow the applied fix only worked for the yesterday build, but I think it’s worth checking.</p>
<p>Another issue is that some superbuild extensions don’t seem to build on Mac for 4.8.1, due to inability to download the dependencies. The two examples I could find where connection error is the cause of failure:<br>
<a href="http://slicer.cdash.org/viewBuildError.php?buildid=1292866" class="onebox" target="_blank">http://slicer.cdash.org/viewBuildError.php?buildid=1292866</a><br>
<a href="http://slicer.cdash.org/viewBuildError.php?buildid=1292803" class="onebox" target="_blank">http://slicer.cdash.org/viewBuildError.php?buildid=1292803</a><br>
These may be related.</p>
<p>I’d appreciate if you could look into these! Thanks a lot!</p>

---

## Post #7 by @Sam_Horvath (2018-06-13 19:40 UTC)

<p>The windows factory rebooted during the build process last night (updates <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=5" title=":frowning:" class="emoji" alt=":frowning:">).  The nightly package did not get uploaded and both the stable and nightly extensions are missing entirely.</p>
<p>Will look into the Mac issue.</p>

---

## Post #8 by @lassoan (2018-06-14 03:04 UTC)

<aside class="quote no-group" data-username="Sam_Horvath" data-post="7" data-topic="3125">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<p>The windows factory rebooted during the build process last night (updates <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20">).</p>
</blockquote>
</aside>
<p>You can set “Active hours” in Windows update settings to something like 10pm to 11am to make sure updates don’t interfere with nightly builds.</p>

---
