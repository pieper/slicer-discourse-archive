---
topic_id: 32215
title: "Extension Versioning"
date: 2023-10-13
url: https://discourse.slicer.org/t/32215
---

# Extension versioning

**Topic ID**: 32215
**Date**: 2023-10-13
**URL**: https://discourse.slicer.org/t/extension-versioning/32215

---

## Post #1 by @jhlegarreta (2023-10-13 17:06 UTC)

<p>Hi,<br>
I am using 3D Slicer 5.2.2, and have a number of extensions installed, including SlicerDMRI:<br>
<a href="https://github.com/SlicerDMRI/SlicerDMRI" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerDMRI/SlicerDMRI: Diffusion MRI analysis and visualization in 3D Slicer open source medical imaging platform.</a></p>
<p>According to the ExtensionManager in 3D Slicer, the SlicerDMRI version I have is <a href="https://github.com/SlicerDMRI/SlicerDMRI/tree/6207e526b549a1fc73bcd106704972bc0f9f3fb2" rel="noopener nofollow ugc">6207e52</a> (2023-02-23). The repository at issue only contains an <a href="https://github.com/SlicerDMRI/SlicerDMRI/tags" rel="noopener nofollow ugc">old tag</a>.</p>
<p>As far as I know, for CMake-based projects, the version is usually hosted in a <code>*.cmake</code> (e.g. <a href="https://github.com/Slicer/Slicer/blob/93ee298abb3d091899f2c887b8907009f076e00d/CMake/SlicerVersion.cmake" rel="noopener nofollow ugc"><code>SlicerVersion.cmake</code></a>) file.</p>
<p>I am wondering how stable versions for extensions should be dealt with or are installed or picked by the Extension Manager.</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2023-10-13 18:13 UTC)

<p>The <a href="https://github.com/Slicer/ExtensionsIndex/">ExtensionsIndex repository</a> stores what version of an extension (tag, branch, or hash) should be used for each Slicer version (in scm* fields in the .s4ext files).</p>
<p>For example, version of each extension that should be used with Slicer-5.4 are specified in this branch: <a href="https://github.com/Slicer/ExtensionsIndex/tree/5.4" class="inline-onebox">GitHub - Slicer/ExtensionsIndex at 5.4</a></p>

---

## Post #3 by @jhlegarreta (2023-10-13 18:58 UTC)

<p>OK, thanks for info Andras.</p>

---

## Post #4 by @MyrtleDunlap (2023-11-06 13:56 UTC)

<p>In 3D Slicer, extension versions are managed through the Extension Manager, which ensures you have the latest stable version. The version you mentioned, 6207e52, corresponds to a release or update from the repository.</p>

---

## Post #5 by @jhlegarreta (2023-11-06 14:19 UTC)

<aside class="quote no-group" data-username="MyrtleDunlap" data-post="4" data-topic="32215">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/b5ac83/48.png" class="avatar"> MyrtleDunlap:</div>
<blockquote>
<p>corresponds to a release or update from the repository.</p>
</blockquote>
</aside>
<p>It is a simple commit. If you look at the tags and/or releases of the repository you’ll realize about the relevance of the question.</p>
<aside class="quote no-group" data-username="MyrtleDunlap" data-post="4" data-topic="32215">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/b5ac83/48.png" class="avatar"> MyrtleDunlap:</div>
<blockquote>
<p>In 3D Slicer, extension versions are managed through the Extension Manager, which ensures you have the latest stable version.</p>
</blockquote>
</aside>
<p>I only had a quick look at the extension index repository, and saw that there is a non-negligible amount of extensions that specify a non-tagged version for their <code>scmrevision</code>, which potentially implies that these are not necessarily stable.</p>

---
