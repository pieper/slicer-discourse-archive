# Improving usage of when to use Stable vs Nightly release

**Topic ID**: 4049
**Date**: 2018-09-10
**URL**: https://discourse.slicer.org/t/improving-usage-of-when-to-use-stable-vs-nightly-release/4049

---

## Post #1 by @jamesobutler (2018-09-10 18:09 UTC)

<h2><a name="p-15312-background-info-1" class="anchor" href="#p-15312-background-info-1" aria-label="Heading link"></a>Background info</h2>
<p>Out of a discussion that started <a href="https://discourse.slicer.org/t/after-saving-and-re-opening-files-i-cannot-re-edit-the-labels-using-editor/4048/5">here</a> I’m thinking there might be some improvement to encourage users when it is best to use the Stable versus the current Nightly release. I frequently see users on the forum asking for help related to things in 4.8.1 and often a good response is to encourage them to the latest nightly. The Nightly release becomes the preferred version to use especially when the Stable is quite old as it is now. It’s been ~8 months since Slicer 4.8.1 was released and ~11 months since Slicer 4.8.0 was released.</p>
<p>Based on information from <a class="mention" href="/u/lassoan">@lassoan</a>:</p>
<blockquote>
<p>Creating a stable Slicer release still requires a lot of manual effort, so unfortunately there is often a rather long time period when a nightly version is ready to be released as stable, yet it is still only labelled as nightly version.</p>
<p>Except a few very specific issues (which should only affect few users), the current nightly version works well, so the potential issues of nightly version are outweighed by those many fixes and improvements that it contains.<br>
[<a href="https://discourse.slicer.org/t/after-saving-and-re-opening-files-i-cannot-re-edit-the-labels-using-editor/4048/7">source</a>]</p>
</blockquote>
<blockquote>
<p>If the stable build is older than a few months, I would recommend to use a nightly build. If you download a nightly and have no problems with it, keep using that for a few months (until there are some fixes or improvements in the nightly builds that you need).<br>
[<a href="https://discourse.slicer.org/t/new-release-nightlies-stability/263/2">source</a>]</p>
</blockquote>
<p>and another reason from <a class="mention" href="/u/cpinter">@cpinter</a> to sometimes encourage the Nightly as the preferred option</p>
<blockquote>
<p>4.8.1 can now be considered ancient in terms of segmentation features<br>
[<a href="https://discourse.slicer.org/t/after-saving-and-re-opening-files-i-cannot-re-edit-the-labels-using-editor/4048/6">source</a>]</p>
</blockquote>
<h2><a name="p-15312-potential-improvements-2" class="anchor" href="#p-15312-potential-improvements-2" aria-label="Heading link"></a>Potential Improvements:</h2>
<ul>
<li>On the public facing download page <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a>, add text that indicates if the currently Nightly is 3(?) months newer than the current Stable that it should be the preferred download.</li>
<li>Or text indicating that the Nightly is the preferred download could be added to the page in an automated way once it has been a certain number of days after the Stable release.</li>
<li>Or if the revision number/number of git commits since the Stable has reached a threshold to then make the nightly download the preferred download.  This is different than indicating “preferred” based on number of days that have passed since the Stable release.</li>
<li>Increase the prominence of the Nightly download over the stable? List it above the stable?</li>
<li>More granular indication on the download page that if you are using specific features(ie Segmentation) that you should use the Nightly.</li>
</ul>
<h2><a name="p-15312-other-ideas-3" class="anchor" href="#p-15312-other-ideas-3" aria-label="Heading link"></a>Other Ideas?</h2>
<p>Does anyone have any ideas about how else to improve the download page to encourage the use of Stable vs Nightly that can be an improvement given the current state of Slicer stable releases is on a slower yearly release schedule?</p>

---

## Post #2 by @muratmaga (2018-09-10 18:33 UTC)

<p>Currently for us volume rendering in 4.9 versions is a big road block. See my post at <a href="https://discourse.slicer.org/t/volume-rendering-issues-with-high-resolution-data-in-4-9-nightlies-continues-with-new-hardware/4051">Volume rendering issues with high-resolution data in 4.9 nightlies continues with new hardware</a></p>
<p>If this can’t be fixed, there should be an indication about this on the website.</p>
<p>M</p>

---

## Post #3 by @cpinter (2018-09-10 18:47 UTC)

<p>Thanks for bringing this up!</p>
<ol>
<li>
<p>I think encouraging users to use the stable is generally a good idea, as it is the one that corresponds to the documentation the best, and the one with the fewest known issues. For most of the users it is fine. I think we usually refer users to the nightly because of two reasons:<br>
a) When users report bugs, then we refer them to the nightly because basically that’s the only one we maintain (due to limited resources to backport), and if the bug appears there, then we use it, otherwise we fix it in the nightly<br>
b) When users ask questions about issues that we already addressed in the nightly. You also noticed that these mostly happen nowadays about segmentation. The new editor was not yet considered mature enough to replace the old one at the time of 4.8.1, but now we can recommend it as it’s quite stable and its features make it more user friendly and comprehensive than the legacy editor (this is why I referred to it as “ancient in terms of segmentation”). So with this release, this is kind of a special case, because segmentation is one of the most prevalent use cases and it underwent huge changes recently.</p>
</li>
<li>
<p>The shift of preference towards the nightly is not a matter of time or commits, but about two things: major improvements in terms of important features, and stability. Both are matters of human judgement.</p>
</li>
</ol>
<p>For these reasons my vote goes for keeping recommending the stable to the users, and not setting up an automated system for marking the nightly the preferred one.</p>
<p>Instead - as you also suggested, and we totally agree - we should do releases more often. Unfortunately in this case we have been having the same blocking issues in the last half year more or less, otherwise the three-month interval would have been achievable.<br>
With 4.9, we had several months when Slicer could be considered very unstable when the transition to Qt 5 was happening. Those months passed quickly, and I could recommend the nightly relatively risk-free after that. However if you look at the <a href="https://issues.slicer.org/view_all_bug_page.php">issues</a>, you’ll see that we have problems with the Extension Manager (related to QWebEngine in Qt5), and some aspects of the new OpenGL2 backend which came after switching to VTK9. Once these issues are fixed, we can release a new Slicer version (see my first point about minimizing the number and severity of known issues for the stable builds).</p>
<p>It would be great if we could release a Slicer every 3 months or so, and I think it should be generally achievable in the periods where we do incremental work, if the core devs dedicate some time for bugfixes before each release. Updating the documentation is still a hurdle, but there are efforts towards dynamic documentation which would solve this.<br>
So in this specific case (in my understanding) we’ll do a release once those two blocking issues are fixed, and then we can use the new stable. Not sure what is needed in order to make that happen, so the opinions of others (<a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a>) would be appreciated.<br>
I’m looking forward to the release as well!</p>

---

## Post #4 by @jamesobutler (2018-09-10 19:20 UTC)

<blockquote>
<p>The shift of preference towards the nightly is not a matter of time or commits, but about two things: major improvements in terms of important features, and stability. Both are matters of human judgement.</p>
</blockquote>
<p>Ok, true.  I guess you can have a bunch of smaller commits which wouldn’t result in the nightly being necessarily a “preferred” version.  Probably at most an equal.</p>
<blockquote>
<p>Unfortunately in this case we have been having the same blocking issues in the last half year more or less, otherwise the three-month interval would have been achievable.</p>
</blockquote>
<p>It would probably be a good idea to not have a few issues blocking a new release if there are a bunch of improvements that don’t depend on it that could be released as a new slicer release.  The commit that created a regression of some sort could be picked out to allow a new Slicer release.  I haven’t looked at <a class="mention" href="/u/muratmaga">@muratmaga</a> 's issue, but I don’t suspect QWebEngine or OpenGL2 issues should be blocking new features related to the popular Segment Editor module.</p>

---

## Post #5 by @cpinter (2018-09-10 19:35 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="4049">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>It would probably be a good idea to not have a few issues blocking a new release if there are a bunch of improvements that don’t depend on it that could be released as a new slicer release</p>
</blockquote>
</aside>
<p>In an ideal world, indeed <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> Switches to Qt5 and VTK9 were really necessary, and as development is happening on multiple fronts, but there is only one master branch, we cannot prevent one influencing the other.</p>
<p>I’d very much like to see the new release, but as I was always told it’s a matter of a few weeks, I wasn’t concerned about these once I fixed the issues that were assigned to me. Unfortunately, the work related to the release seems to have stalled.<br>
I’d love to hear the current status from those who work on the remaining issues, and I gladly help if I can!</p>

---

## Post #6 by @pieper (2018-09-10 21:21 UTC)

<p>I think this thread is accurate - <a class="mention" href="/u/jamesobutler">@jamesobutler</a> describes where we’d like to be and <a class="mention" href="/u/cpinter">@cpinter</a> describes where we are and why.  Perhaps if nothing else the download page could include a summary of the main points from this thread so that potential users get a sense of what “stable” and “nightly” typically mean in the Slicer world.</p>

---
