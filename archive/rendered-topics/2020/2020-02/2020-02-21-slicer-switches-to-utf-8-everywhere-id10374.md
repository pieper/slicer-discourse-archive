# Slicer switches to UTF-8 everywhere

**Topic ID**: 10374
**Date**: 2020-02-21
**URL**: https://discourse.slicer.org/t/slicer-switches-to-utf-8-everywhere/10374

---

## Post #1 by @lassoan (2020-02-21 04:05 UTC)

<p>Following VTK, ITK, and most other software, with <a href="https://github.com/Slicer/Slicer/commit/1d64077ab32488e4ef83273ea4f4bf3f24175101">this commit</a>, Slicer switches to <a href="https://utf8everywhere.org/">“UTF-8 everywhere”</a>. This will make it possible to load files that have special character in their names, use special characters in node names or any other text.</p>
<p>This also opens up the possibility for full and correct translation of the application to any language, but there is still significant work needed to get there (e…g, consistent usage of <code>tr</code> in C++ code, introduction of translation macro in Python code, design solution for translation of CLI modules).</p>
<p>Coding conventions: <code>std::string</code>  and  <code>char*</code> variables always store string with UTF-8 encoding and text in files are always expected to use UTF-8 encoding. See coding examples and more background information in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Style_Guide#String_encoding%3A_UTF-8_everywhere">style guide</a>.</p>

---

## Post #2 by @jcfr (2020-03-27 18:48 UTC)

<p>4 posts were split to a new topic: <a href="/t/update-of-discourse-posts-to-reference-correct-https-github-com-slicer-slicer-sha-url/10878">Update of Discourse posts to reference correct https://github.com/Slicer/Slicer/ URL</a></p>

---
