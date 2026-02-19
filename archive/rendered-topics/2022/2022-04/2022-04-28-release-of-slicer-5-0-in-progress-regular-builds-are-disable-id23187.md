---
topic_id: 23187
title: "Release Of Slicer 5 0 In Progress Regular Builds Are Disable"
date: 2022-04-28
url: https://discourse.slicer.org/t/23187
---

# Release of Slicer 5.0 in progress: Regular builds are disabled

**Topic ID**: 23187
**Date**: 2022-04-28
**URL**: https://discourse.slicer.org/t/release-of-slicer-5-0-in-progress-regular-builds-are-disabled/23187

---

## Post #1 by @jcfr (2022-04-28 20:37 UTC)

<p>This evening, regular preview and stable builds of Slicer and associated extensions will be disabled in favor of a new stable release.</p>
<p>To track the progress, see <a href="https://github.com/Slicer/Slicer/issues/6337" class="inline-onebox">Release Slicer v5.0 · Issue #6337 · Slicer/Slicer · GitHub</a></p>

---

## Post #2 by @jcfr (2022-04-30 05:51 UTC)

<p>Updates:</p>
<ul>
<li>Release has been tagged and packages are being generated. See dashboard <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=">here</a>
</li>
<li>Regular will be resumed tomorrow</li>
</ul>

---

## Post #3 by @jcfr (2022-04-30 20:18 UTC)

<p>Updates:</p>
<ul>
<li>
<p>Last night build all complete along with the built of all extensions, that said a glitch related to toggling memory leaks that is specific to Stable build was identified (See issue <a href="https://github.com/Slicer/Slicer/issues/6344">#6344</a>).</p>
</li>
<li>
<p>This means that a maintenance branch will be created and <strong>new tag called <code>v5.0.1</code></strong> will be published and associated release build will be <strong>triggered tonight</strong> (in place of our usual preview build).</p>
</li>
</ul>
<h3><a name="p-77452-what-about-revisions-1" class="anchor" href="#p-77452-what-about-revisions-1" aria-label="Heading link"></a>What about revisions</h3>
<p>To ensure revision of potential patch release and on-going development associated with <code>5.1.0</code> would compare nicely, we pre-allocated 100 revisions (See <a href="https://github.com/Slicer/Slicer/pull/6343">PR #6343</a>)</p>

---

## Post #4 by @jcfr (2022-05-01 12:15 UTC)

<p>Updates:</p>
<ul>
<li>Slicer v5.0.1 has been tagged and packages are being generated.  See dashboard <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2022-05-01&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=">here</a>
</li>
</ul>
<p>Details:</p>
<ul>
<li>Issue <a href="https://github.com/Slicer/Slicer/issues/6344">#6344</a> has been addressed</li>
<li>Dashboard scripts have been tweaked to also backup the <code>site-packages</code> directory before building the extensions. See details <a href="https://github.com/Slicer/DashboardScripts/commit/b3f057d1fbf65efb01bb2c586aada5acfcb57434">here</a>.</li>
</ul>
<p>Next steps</p>
<ul>
<li>The download <a href="https://download.slicer.org/">site</a> displays <code>None</code> instead of the package version</li>
<li>Finalize part 2 of the release checklist available at <a href="https://github.com/Slicer/Slicer/issues/6337" class="inline-onebox">Release Slicer v5.0 · Issue #6337 · Slicer/Slicer · GitHub</a>
</li>
</ul>

---

## Post #5 by @jcfr (2022-05-02 03:45 UTC)

<p>Updates:</p>
<ul>
<li>Build of applications and extensions completed for both macOS and Windows <img src="https://emoji.discourse-cdn.com/twitter/ok_hand.png?v=12" title=":ok_hand:" class="emoji" alt=":ok_hand:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20">
</li>
<li>Due to a network failure related to download of some test datasets (See <a href="https://slicer.cdash.org/viewBuildError.php?buildid=2677780">here</a>),  the <strong>Linux build has been re-started and is in progress</strong> <img src="https://emoji.discourse-cdn.com/twitter/hourglass_flowing_sand.png?v=12" title=":hourglass_flowing_sand:" class="emoji" alt=":hourglass_flowing_sand:" loading="lazy" width="20" height="20">  See dashboard <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2022-05-02&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex">here</a>.</li>
</ul>

---

## Post #6 by @jcfr (2022-05-02 19:27 UTC)

<p>A post was split to a new topic: <a href="/t/availability-of-slicer-5-0-on-archlinux/23245">Availability of Slicer 5.0 on ArchLinux</a></p>

---

## Post #7 by @jcfr (2022-05-06 06:56 UTC)

<p>Updates:</p>
<ul>
<li>Slicer <code>v5.0.2</code> has been tagged and packages are being generated. See dashboard <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2022-05-06&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=">here</a>
</li>
<li>Regular will be resumed tomorrow</li>
</ul>
<p>Notes:</p>
<ul>
<li>For list of backported commits. See <a href="https://github.com/Slicer/Slicer/compare/v5.0.1...maintenance/5.0" class="inline-onebox">Comparing v5.0.1...maintenance/5.0 · Slicer/Slicer · GitHub</a>
</li>
</ul>

---

## Post #8 by @jcfr (2022-05-20 07:59 UTC)

<p>Updates:</p>
<ul>
<li>Slicer <code>v5.0.2</code> packages are now available for download at <a href="https://download.slicer.org">https://download.slicer.org</a> <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=12" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20">
</li>
</ul>
<p>Known issues:</p>
<ul>
<li>Endoscopy module issue. Fixed in <a href="https://github.com/Slicer/Slicer/commit/3d66964c524a58b2583aac051e1310a5019d0039">Slicer@3d66964c5</a> and candidate for backport targeting <code>v5.0.3</code>
</li>
</ul>
<p>Next:</p>
<ul>
<li>Finalize announcements</li>
</ul>

---

## Post #9 by @Alex_Vergara (2022-05-25 09:11 UTC)

<p>The module updates are not integrated in the stable release, they do upgrade normally in the nightly package. Is there any plans to backport the updates to the stable branch? When shall we expect this feature?</p>

---

## Post #10 by @cpinter (2022-05-26 09:00 UTC)

<p>When you say “module updates” what do you refer to? Extension updates? If so, you can update your extension repo hash in the s4ext in the branch of the stable version in ExtensionIndex:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b17eba364ea05426919f6d660668c1414199f1e8.png" data-download-href="/uploads/short-url/pkc1vZNrsTvtcj9z0TxSEC1Q5tu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b17eba364ea05426919f6d660668c1414199f1e8_2_494x500.png" alt="image" data-base62-sha1="pkc1vZNrsTvtcj9z0TxSEC1Q5tu" width="494" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b17eba364ea05426919f6d660668c1414199f1e8_2_494x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b17eba364ea05426919f6d660668c1414199f1e8_2_741x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b17eba364ea05426919f6d660668c1414199f1e8.png 2x" data-dominant-color="E4E7E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">879×889 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @Alex_Vergara (2022-05-26 13:10 UTC)

<p>it is there <a href="https://github.com/Slicer/ExtensionsIndex/blob/5.0/OpenDose3D.s4ext" class="inline-onebox" rel="noopener nofollow ugc">ExtensionsIndex/OpenDose3D.s4ext at 5.0 · Slicer/ExtensionsIndex · GitHub</a></p>
<p>So I don’t know why the latest changes are not integrated</p>

---

## Post #12 by @jamesobutler (2022-05-26 13:51 UTC)

<p><a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2022-05-25" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2022-05-25</a></p>
<p>^ May 25th 2022 shows the following:</p>
<ul>
<li>Windows: OpenDose started building at 10:53 UTC</li>
<li>Linux: OpenDose extension started building at 8:56 UTC</li>
<li>macOS: OpenDose extension started building at 23:14 UTC</li>
</ul>
<p>These all were of OpenDose hash 324ebe4 which matches the current latest at <a href="https://gitlab.com/opendose/opendose3d/-/commits/master-stable/" class="inline-onebox" rel="noopener nofollow ugc">Commits · master-stable · OpenDose / SlicerOpenDose3D · GitLab</a>.</p>
<p><a class="mention" href="/u/alex_vergara">@Alex_Vergara</a> your post yesterday was at 9:11 UTC. It appears you had posted before the extensions builds had fully completed for that day.</p>
<p>The runs from the previous day on May 24th (<a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2022-05-24" class="inline-onebox" rel="noopener nofollow ugc">CDash</a>) had varying git hashes of OpenDose being used because you had committed to <a href="https://gitlab.com/opendose/opendose3d/-/commits/master-stable/" class="inline-onebox" rel="noopener nofollow ugc">Commits · master-stable · OpenDose / SlicerOpenDose3D · GitLab</a> during the middle of the extension builds. The Windows build of OpenDose that day started at 12:08 UTC, but OpenDose hash 324ebe4 wasn’t committed until 13:19 UTC. While the macOS build of OpenDose did have hash 324ebe4  because it started at 21:42 UTC.</p>

---

## Post #13 by @Alex_Vergara (2022-05-26 17:15 UTC)

<p>it is working today, thanks for the explanation</p>

---

## Post #14 by @jcfr (2022-07-07 22:32 UTC)

<p>Updates:</p>
<ul>
<li>Slicer <code>v5.0.3</code> will be tagged shortly and packages will be generated this evening <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=12" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20">
</li>
<li>Regular preview and nightly builds will be <strong>disabled</strong> and resumed tomorrow</li>
</ul>
<p>Notes:</p>
<ul>
<li>Most of the commits added to <code>main</code> have been backported commits. See <a href="https://github.com/Slicer/Slicer/pull/6398/commits">https://github.com/Slicer/Slicer/pull/6398/commits</a>
</li>
<li>The changes related to the rename of <code>master</code> to <code>main</code> have <strong>not</strong> been backported</li>
<li>Since only 100 commits were <a href="https://github.com/Slicer/Slicer/blob/df1116d7685d8e9ea903aab47141224a14db62cf/CMakeLists.txt#L315-L316">allocated</a> for the patch releases:
<ul>
<li>some of the commit have been squashed together and started with <code>Backport ...</code> (for example see <a href="https://github.com/Slicer/Slicer/pull/6398/commits/82a8e54b4eaece3952639e579f371fd6900a7199">82a8e54b4</a>)</li>
<li>there are now 82 commits on top of <code>v5.0.0</code>
</li>
</ul>
</li>
</ul>

---

## Post #15 by @jcfr (2022-07-08 06:27 UTC)

<p>Updates:</p>
<ul>
<li>Slicer <code>v5.0.3</code> has been tagged and packages are being generated. See dashboard <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2022-07-08">here</a>
</li>
<li>Regular will be resumed tomorrow</li>
</ul>

---

## Post #16 by @jcfr (2022-07-08 22:45 UTC)

<p>Update:</p>
<ul>
<li>Package have been generated and will be signed on Monday</li>
<li>Regular nightly build will resume this evening</li>
</ul>

---
