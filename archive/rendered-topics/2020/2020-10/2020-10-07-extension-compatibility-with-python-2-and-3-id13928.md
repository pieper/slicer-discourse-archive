---
topic_id: 13928
title: "Extension Compatibility With Python 2 And 3"
date: 2020-10-07
url: https://discourse.slicer.org/t/13928
---

# Extension compatibility with Python 2 and 3

**Topic ID**: 13928
**Date**: 2020-10-07
**URL**: https://discourse.slicer.org/t/extension-compatibility-with-python-2-and-3/13928

---

## Post #1 by @mehrtash (2020-10-07 20:36 UTC)

<p>DeepInfer and probably some other modules do not work in Slicer 4.11 due to python 3 incompatibility. [1]</p>
<p>I have made some changes to the code to make it compatible with python 3 but the problem is that it would not work in the previous Slicer versions including 4.10.</p>
<p>Is there any way to specify a specific git id in the s4ext file for Slicer v &lt;=4.10 to support backward compatibility and master for v&gt;=4.11?</p>
<p>[1] <a href="https://github.com/DeepInfer/Slicer-DeepInfer/issues/13" rel="noopener nofollow ugc">https://github.com/DeepInfer/Slicer-DeepInfer/issues/13</a></p>

---

## Post #2 by @jamesobutler (2020-10-07 20:47 UTC)

<p>The factory build machines are no longer building Slicer 4.10 extensions so updates to <a href="https://github.com/Slicer/ExtensionsIndex/tree/4.10" rel="noopener nofollow ugc">https://github.com/Slicer/ExtensionsIndex/tree/4.10</a> won’t result in any changes. The current stable is the Slicer 4.11.20200930 snapshot.  Updates for this new stable for the factory to build would be made to the s4ext in <a href="https://github.com/Slicer/ExtensionsIndex/tree/4.11" rel="noopener nofollow ugc">https://github.com/Slicer/ExtensionsIndex/tree/4.11</a>.</p>
<p>If you want to support building the extension on your own for compatibility with Slicer 4.10 you can update your code checking slicer version such as <code>slicer.app.majorVersion</code>, <code>slicer.app.minorVersion</code>, and <code>slicer.app.patchVersion</code>.</p>

---

## Post #3 by @lassoan (2020-10-07 21:07 UTC)

<p>If you don’t want to pollute your code with version checks then:</p>
<ul>
<li>in your repository create a new <code>4.10</code> branch from current master</li>
<li>send a pull request to <a href="https://github.com/Slicer/ExtensionsIndex/tree/4.10">https://github.com/Slicer/ExtensionsIndex/tree/4.10</a> to use <code>4.10</code> branch of your extension instead of master (just in case someone builds a Slicer-4.10 version)</li>
</ul>

---
