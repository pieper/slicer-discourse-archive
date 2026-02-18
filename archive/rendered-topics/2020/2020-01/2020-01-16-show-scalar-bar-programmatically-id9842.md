# Show scalar bar programmatically

**Topic ID**: 9842
**Date**: 2020-01-16
**URL**: https://discourse.slicer.org/t/show-scalar-bar-programmatically/9842

---

## Post #1 by @Fernando (2020-01-16 21:03 UTC)

<p>Hi all,</p>
<p>I’d like to show the scalar bar like when I do DataProbe -&gt; ScalarBar -&gt; Enable -&gt; Foreground. Do you know how I can do this? I’ve always had a hard time accessing the DataProbe stuff from Python.</p>
<p>Cheers,<br>
Fernando</p>

---

## Post #2 by @pieper (2020-01-16 21:30 UTC)

<p>Hi <a class="mention" href="/u/fernando">@Fernando</a> - this should work for you (although we might want to think of a better API).</p>
<pre><code class="lang-auto">qt.QSettings().setValue('DataProbe/sliceViewAnnotations.scalarBarEnabled', True)
import DataProbeLib
DataProbeLib.SliceAnnotations().updateSliceViewFromGUI()
</code></pre>

---

## Post #3 by @Fernando (2020-01-16 21:45 UTC)

<p>Thanks, Steve. That worked great to enable the scalar bar. Do you know how I can specifically show the foreground one?</p>

---

## Post #4 by @pieper (2020-01-16 22:04 UTC)

<p>It’ll be a similar pattern - have a look at the various options <a href="https://github.com/Slicer/Slicer/blob/25b804e35bf5ee27e14a318cd44680850825b33b/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L222">in the code</a>…</p>

---

## Post #5 by @Fernando (2020-01-16 22:18 UTC)

<p>I did! But the choice between background and foreground doesn’t seem to be part of those settings…</p>

---

## Post #6 by @pieper (2020-01-17 01:05 UTC)

<p>Right - looks like that setting is not persisted in the settings.  Maybe you want to add code to persist it to be consistent.  Probably the best thing to do would be to expose a proper logic API for these in the DataProbe code.</p>

---

## Post #7 by @lassoan (2020-01-17 13:29 UTC)

<p>Data probe (that includes scalar widget management) would need to be completely rewritten. We’ve been planning to do this but there have been always higher-priority tasks.<br>
<a class="mention" href="/u/fernando">@Fernando</a> If you can achieve what you need with small changes then go on, but if you have some more time then it would be great if you could help with redesign/reimplementation of the feature.</p>

---

## Post #8 by @Fernando (2020-01-17 13:43 UTC)

<p>I’ll let you know if I find a solution. <a class="mention" href="/u/lassoan">@lassoan</a>, that code has always been a bit obscure to me, but I’m happy to help if I can.</p>

---

## Post #9 by @pieper (2020-01-17 19:22 UTC)

<aside class="quote no-group quote-modified" data-username="pieper" data-post="2" data-topic="9842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>qt.QSettings().setValue(‘DataProbe/sliceViewAnnotations.scalarBarEnabled’, True) import DataProbeLib DataProbeLib.SliceAnnotations().updateSliceViewFromGUI()</p>
</blockquote>
</aside>
<p>Update: the argument to <code>setValue</code> here needs to be an int not a boolean in order to be restored correctly:</p>
<pre><code class="lang-auto">qt.QSettings().setValue('DataProbe/sliceViewAnnotations.scalarBarEnabled', 1)
import DataProbeLib
DataProbeLib.SliceAnnotations().updateSliceViewFromGUI()
</code></pre>

---

## Post #10 by @Fernando (2020-03-31 13:24 UTC)

<p>PR here: <a href="https://github.com/Slicer/Slicer/pull/4789" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/4789</a></p>

---
