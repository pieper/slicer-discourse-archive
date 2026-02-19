---
topic_id: 466
title: "Proposed New Executable Tag In Slicerexecutionmodel"
date: 2017-06-06
url: https://discourse.slicer.org/t/466
---

# Proposed new "executable" tag in SlicerExecutionModel

**Topic ID**: 466
**Date**: 2017-06-06
**URL**: https://discourse.slicer.org/t/proposed-new-executable-tag-in-slicerexecutionmodel/466

---

## Post #1 by @lassoan (2017-06-06 21:22 UTC)

<aside class="quote no-group quote-modified" data-username="jcfr" data-post="19" data-topic="53">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"><a href="https://discourse.slicer.org/t/weekly-hangout-for-slicer-user-and-developer/53/19">Weekly Hangout for Slicer user and developer</a></div>
<blockquote>
<p>update of executable tag to support  executable path=“&lt;name&gt;” type=“python|cpp”</p>
</blockquote>
</aside>
<p>What this executables tag refers to and what would it be used for?<br>
It seems that the value specify what language the module is implemented in, but that should not matter much - you can compile python code to be an exe file, you can also create executables by bash scripting, you can run .bat files on Windows…</p>
<p>Do you want to specify what software you need to use to launch it? Then the options should be system, python, bash, etc. and the tag name could be “launcher”, “interpreter” or something similar.</p>

---

## Post #2 by @fedorov (2017-06-09 13:59 UTC)

<p>I agree with Andras - would be great to know more details about this new tag. It is quite confusing. I could not make the call, is there some place with more details?</p>

---

## Post #3 by @jcfr (2017-06-21 14:28 UTC)

<p>Here is a link to bring some context … <a href="https://github.com/commontk/ctk-cli/pull/17">https://github.com/commontk/ctk-cli/pull/17</a></p>
<p>(i will follow up next week when I am back from travelling)</p>

---
