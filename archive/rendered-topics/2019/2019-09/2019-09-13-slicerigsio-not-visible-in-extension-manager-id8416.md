# SlicerIGSIO not visible in Extension Manager

**Topic ID**: 8416
**Date**: 2019-09-13
**URL**: https://discourse.slicer.org/t/slicerigsio-not-visible-in-extension-manager/8416

---

## Post #1 by @David_Asgar-Deen (2019-09-13 17:16 UTC)

<p>Hello,</p>
<p>I have noticed that the SlicerIGT tutorials have been updated recently (specifically Lesson U-01). In this tutorial, it states that one of the extensions to download is SlicerIGSIO. When searching in the extension manager I was unable to find this extension. I was wondering if we have to directly download it from github, or if there is another work around. Anyway I would like to thank you for taking the time to read this and I look forward to your response.</p>

---

## Post #2 by @Sunderlandkyl (2019-09-13 17:29 UTC)

<p>What version of Slicer are you using?</p>
<p>SlicerIGSIO appears to have built successfully on the latest nightly release (4.11), but not the stable (4.10.2).</p>

---

## Post #3 by @David_Asgar-Deen (2019-09-13 17:35 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="2" data-topic="8416">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>licerIGSIO appears to have built successfully on the latest nightly release (4.11), but not the stable (4.10.2).</p>
</blockquote>
</aside>
<p>Hello Kyle,</p>
<p>I am currently using the stable release (4.10.2) which would explain why it is not showing up. Thanks for the reply!</p>

---

## Post #4 by @Sunderlandkyl (2019-09-13 17:36 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> Do you have an idea of why the stable version of SlicerIGSIO is failing?</p>
<p>The build seems to be running into issues while checking out one of the projects:<br>
<a href="http://slicer.cdash.org/viewBuildError.php?buildid=1692908" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/viewBuildError.php?buildid=1692908</a></p>

---

## Post #5 by @Sam_Horvath (2019-09-13 17:41 UTC)

<p>Yeah, I have been looking at it.  This git-submodule issue seems to appear randomly on Windows and I haven’t found a consistent solution for it.  I am going to try to force / hack around this on the stable build so we can get at least one working upload for IGSIO.</p>

---

## Post #6 by @Sam_Horvath (2019-09-13 19:16 UTC)

<p>So, I have forced a build/package/upload for SlicerIGSIO on stable, vs the current SlicerIGSIO master.  I will continue to look into the actual build issue, but it is not something I have had any luck in fixing in the past.</p>

---
