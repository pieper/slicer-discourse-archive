---
topic_id: 42958
title: "Input Method Cannot Be Activated In Packaged Slicer On Ubunt"
date: 2025-05-16
url: https://discourse.slicer.org/t/42958
---

# Input Method Cannot Be Activated in Packaged Slicer on Ubuntu

**Topic ID**: 42958
**Date**: 2025-05-16
**URL**: https://discourse.slicer.org/t/input-method-cannot-be-activated-in-packaged-slicer-on-ubuntu/42958

---

## Post #1 by @herryliq (2025-05-16 06:28 UTC)

<p>We encountered an input method issue during custom development based on <strong>3D Slicer 5.6.2</strong>.</p>
<ul>
<li>
<p><strong>Operating System</strong>: Ubuntu 22.04.4 LTS</p>
</li>
<li>
<p><strong>Slicer Version</strong>: 5.6.2 (custom build)</p>
</li>
</ul>
<h4><a name="p-125179-problem-description-1" class="anchor" href="#p-125179-problem-description-1" aria-label="Heading link"></a>Problem Description:</h4>
<ul>
<li>
<p>When running Slicer directly from the <strong>build environment</strong> (compiled from source), the <strong>system input method (e.g., ibus, fcitx)</strong> works correctly in text fields.</p>
</li>
<li>
<p>However, when running <strong>Slicer from the packaged version</strong> (generated using <code>cpack</code>), it becomes <strong>impossible to activate the system input method</strong> in any text input field.</p>
</li>
<li>
<p>This issue only occurs on <strong>Ubuntu</strong>. On <strong>Windows 11</strong>, the packaged Slicer can activate and use the input method without any problems.</p>
</li>
</ul>
<h4><a name="p-125179-initial-thoughts-2" class="anchor" href="#p-125179-initial-thoughts-2" aria-label="Heading link"></a>Initial Thoughts:</h4>
<p>This might be caused by:</p>
<ul>
<li>
<p>Missing Qt platform input context plugins in the packaged environment (e.g., <code>libqt5gui5-plugins</code>, <code>qtvirtualkeyboard</code>, or <code>platforminputcontexts</code>).</p>
</li>
<li>
<p>Environment variables such as <code>QT_IM_MODULE</code>, <code>QT_PLUGIN_PATH</code>, or others not being set correctly in the packaged runtime.</p>
</li>
<li>
<p>Differences in runtime plugin loading between build and installed environments.</p>
</li>
</ul>
<hr>
<p>We’d appreciate any guidance or suggestions from the Slicer developer community on how to resolve this issue.</p>
<p>Is there a recommended way to ensure that input method support (e.g., ibus) is preserved in the packaged Slicer on Linux?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2025-05-16 12:06 UTC)

<p>Thanks for reporting this. Since you already have a way to reproduce this problem, the best would be if you could investigage this a bit further. First of all, test how Slicer behaves when you build it but not run it from the build tree, but create a package and use that. If your packaged/installed Slicer has the same issues with system input method switches then you can test all your theories (missing Qt plugins is the most likely).</p>

---

## Post #3 by @herryliq (2025-05-20 04:21 UTC)

<p>Thank you for your feedback. I would like to ask whether anyone has reported a similar issue and if there is already a solution in the community.<br>
If no one has reported this issue yet, I will complete the final investigation and confirmation, and provide the modification plan here.</p>

---

## Post #4 by @lassoan (2025-05-20 05:09 UTC)

<aside class="quote no-group" data-username="herryliq" data-post="3" data-topic="42958">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/3bc359/48.png" class="avatar"> herryliq:</div>
<blockquote>
<p>would like to ask whether anyone has reported a similar issue and if there is already a solution in the community</p>
</blockquote>
</aside>
<p>I don’t recall anybody reporting related problems but you have a look at the list of known issues in the <a href="https://github.com/Slicer/Slicer/issues">issue tracker</a>.</p>
<aside class="quote no-group" data-username="herryliq" data-post="3" data-topic="42958">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/3bc359/48.png" class="avatar"> herryliq:</div>
<blockquote>
<p>If no one has reported this issue yet, I will complete the final investigation and confirmation</p>
</blockquote>
</aside>
<p>Probaly right now you are more interested in this topic than anyone else, so I would encourage you to investigate and try to fix issues that you find.</p>

---
