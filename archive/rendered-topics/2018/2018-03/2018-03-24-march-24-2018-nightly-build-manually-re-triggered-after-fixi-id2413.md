---
topic_id: 2413
title: "March 24 2018 Nightly Build Manually Re Triggered After Fixi"
date: 2018-03-24
url: https://discourse.slicer.org/t/2413
---

# March 24, 2018: Nightly build manually re-triggered after fixing regression due to rename of vtkNRRDReader, vtkNRRDWriter to vtkTeemNRRD{R,W}

**Topic ID**: 2413
**Date**: 2018-03-24
**URL**: https://discourse.slicer.org/t/march-24-2018-nightly-build-manually-re-triggered-after-fixing-regression-due-to-rename-of-vtknrrdreader-vtknrrdwriter-to-vtkteemnrrd-r-w/2413

---

## Post #1 by @jcfr (2018-03-24 05:45 UTC)

<p>What happen ?</p>
<ul>
<li>
<code>vtkNRRDReader</code>, <code>vtkNRRDWriter</code> classes were renamed to <code>vtkTeemNRRDReader</code> and <code>vtkTeemNRRDWriter</code> in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27102">r27102</a>
</li>
<li>Project impacted by the rename were all updated <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=5" title=":+1:" class="emoji" alt=":+1:">
</li>
<li>but the update of the MultiVolumeExplorer hash was done after commit <code>r27102</code> and the associated reference in <a href="https://github.com/Slicer/Slicer/blob/69a9d7738d37f6cb141e9b1e2f38931bbe57853f/SuperBuild.cmake#L217-L223">Slicer/SuperBuild.cmake</a> had <strong>NOT</strong> been updated as part of commit  <code>r27102</code> <img src="https://emoji.discourse-cdn.com/twitter/-1.png?v=5" title=":-1:" class="emoji" alt=":-1:">
</li>
<li>To fix this, the MultiVolumeExplorer hash was updated in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27105">r27105</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=5" title=":+1:" class="emoji" alt=":+1:">
</li>
</ul>
<p>Next time ?</p>
<ul>
<li>Let’s make sure to update references of impacted <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_system/Remote_Module">Slicer Remote Module</a> or any other external  projects (files <code>Slicer/SuperBuild/External_*.cmake</code>) also impacted in the commit introducing the breaking change.</li>
</ul>
<p>Dashboard ?</p>
<ul>
<li>
<p>existing macOS and Windows entries were manually removed</p>
</li>
<li>
<p>For these reasons, the dashboard will not show anything in the “Update” column.</p>
</li>
</ul>

---

## Post #2 by @ihnorton (2018-03-24 10:40 UTC)

<p>Sorry about that. I’m not sure if it is possible with cmake, but would be nice if there was a way to ensure that out-of-tree code can’t break the build.</p>

---

## Post #3 by @jcfr (2018-03-25 02:08 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="2" data-topic="2413">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>possible with cmake, but would be nice if there was a way to ensure that out-of-tree code can’t break the build</p>
</blockquote>
</aside>
<p>It is already possible to configure Slicer setting a hash of your choice for external project [1][2], would it help to have the same option for Slicer Remote ?</p>
<p>[1] <a href="https://github.com/Slicer/Slicer/blob/69a9d7738d37f6cb141e9b1e2f38931bbe57853f/CMake/ExternalProjectDependency.cmake#L956-L961">ExternalProject_SetIfNotDefined</a><br>
[2]  and <a href="https://github.com/Slicer/Slicer/blob/69a9d7738d37f6cb141e9b1e2f38931bbe57853f/SuperBuild/External_RapidJSON.cmake#L23-L33">example of usage</a></p>

---

## Post #4 by @ihnorton (2018-03-25 10:39 UTC)

<p>I meant more along the lines of <code>make -k</code> (continue after failure excluding failed target dependees). We wouldn’t want to run the whole build like that, but it would be fine for remotes.</p>

---

## Post #5 by @lassoan (2018-03-25 12:01 UTC)

<p>For users, a partially successful package would simply appear to be broken: some features are missing/not working). Missing parts of the core could cause various additional errors in extensions. I would rather not have a package with so many issues at all.</p>

---
