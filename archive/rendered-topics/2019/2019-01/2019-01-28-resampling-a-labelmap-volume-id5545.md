---
topic_id: 5545
title: "Resampling A Labelmap Volume"
date: 2019-01-28
url: https://discourse.slicer.org/t/5545
---

# Resampling a Labelmap Volume

**Topic ID**: 5545
**Date**: 2019-01-28
**URL**: https://discourse.slicer.org/t/resampling-a-labelmap-volume/5545

---

## Post #1 by @stevenagl12 (2019-01-28 17:14 UTC)

<p>How can I resample a binary labelmap volume to an image origin of [0,0,0] and an image spacing of [1,1,1] that preserves the labelmap classes in the volume output? Is there a way to do this programmatically?</p>

---

## Post #2 by @lassoan (2019-01-29 01:03 UTC)

<p>You can use any of the resample modules. The simplest way to preserve label values is to use nearest neighbor “interpolation”.</p>

---

## Post #3 by @jcfr (2019-01-29 01:48 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="1" data-topic="5545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>Is there a way to do this programmatically?</p>
</blockquote>
</aside>
<p>To invoke the resample volume programmatically, you could look into:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_run_CLI_module_from_Python.3F">How to run CLI module from Python?</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_call_a_CLI_module_from_a_C.2B.2B_loadable_module.3F">How to call a CLI module from a C++ loadable module?</a></li>
</ul>

---
