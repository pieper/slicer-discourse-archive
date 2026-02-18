# 2018.09.13: Only nightly Slicer packages - do not expect extensions this morning

**Topic ID**: 4097
**Date**: 2018-09-13
**URL**: https://discourse.slicer.org/t/2018-09-13-only-nightly-slicer-packages-do-not-expect-extensions-this-morning/4097

---

## Post #1 by @jcfr (2018-09-13 11:28 UTC)

<p>Dear Slicers,</p>
<p>Exceptionally, we need to use the Slicer build infrastructure for supporting an other project. (Usually, we rely on the spare cycle of the infrastructure to support other projects)</p>
<p>This means:</p>
<ul>
<li>you should <strong>only expect the nightly Slicer packages</strong> for Linux, macOS and Windows
<ul>
<li>it is also normal if no test results are available on the dashboard, we disabled them on purpose</li>
<li>these packages are built against the latest VTK and most (if not all) of Volume Rendering issues are addressed</li>
</ul>
</li>
<li>extensions will either be skipped or build later today</li>
</ul>
<p>Thanks for your patience,</p>

---

## Post #2 by @lassoan (2018-09-14 13:13 UTC)

<p><strong>Until the build infrastructure is restored, Slicer nightly version (with extensions) can be downloaded from here: <a href="https://download.slicer.org/?date=2018-09-10">https://download.slicer.org/?date=2018-09-10</a>.</strong></p>

---

## Post #3 by @lassoan (2018-09-14 13:13 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Next time in similar situation it is better to disable Slicer package builds as well. For users, it is better if they download a version that is built from a few-day-old code than getting a version built from latest master but without extensions.</p>

---

## Post #4 by @jcfr (2018-09-14 13:53 UTC)

<p>Sounds good and that makes sense.</p>
<p>In that specific case, the goal was still to have packages to test the volume rendering using the latest VTK …</p>
<p>I guess having a way to customize <a href="http://download.slicer.org">download.slicer.org</a> and allow to “pin” the nightly version offered for download would address this.</p>

---

## Post #5 by @lassoan (2018-09-14 14:07 UTC)

<p>It would be great to have pinning but just the ability to temporarily add an alternative download link with some explanation would be enough.</p>
<p>We should also rename “nightly” to “preview” on the download page as we planned before (since extensions for both stable and master versions are rebuilt nightly).</p>
<p><a class="mention" href="/u/mhalle">@mhalle</a></p>

---

## Post #6 by @jcfr (2018-09-14 14:11 UTC)

<blockquote>
<p>temporarily add an alternative download link with some explanation would be enough.</p>
</blockquote>
<p>Simple approach that would definitively work</p>
<p>The repository is here: <a href="https://github.com/mhalle/slicer4-download" class="inline-onebox">GitHub - mhalle/slicer4-download_deprecated</a></p>
<p><a class="mention" href="/u/mhalle">@mhalle</a> Moving forward, would it be possible to add <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a> and I (<a class="mention" href="/u/jcfr">@jcfr</a>) as collaborator ?</p>
<p>An other option would be transfer the project to <a href="https://github.com/Slicer" class="inline-onebox">Slicer · GitHub</a> or we could fork it into the Slicer organization (and rename it to <code>download.slicer.org</code>)</p>

---
