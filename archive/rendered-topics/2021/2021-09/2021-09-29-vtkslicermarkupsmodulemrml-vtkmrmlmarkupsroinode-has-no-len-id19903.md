---
topic_id: 19903
title: "Vtkslicermarkupsmodulemrml Vtkmrmlmarkupsroinode Has No Len"
date: 2021-09-29
url: https://discourse.slicer.org/t/19903
---

# 'vtkSlicerMarkupsModuleMRML.vtkMRMLMarkupsROINode' has no len()

**Topic ID**: 19903
**Date**: 2021-09-29
**URL**: https://discourse.slicer.org/t/vtkslicermarkupsmodulemrml-vtkmrmlmarkupsroinode-has-no-len/19903

---

## Post #1 by @jumbojing (2021-09-29 00:02 UTC)

<pre><code class="lang-auto">  File "/Applications/Slice98.app/Contents/bin/Python/slicer/util.py", line 1307, in getNode
    nodes = getNodes(pattern, scene)
  File "/Applications/Slice98.app/Contents/bin/Python/slicer/util.py", line 1290, in getNodes
    if (fnmatch.fnmatchcase(name, pattern) or
  File "/Applications/Slice98.app/Contents/lib/Python/lib/python3.6/fnmatch.py", line 70, in fnmatchcase
    match = _compile_pattern(pat)
TypeError: unhashable type: 'numpy.ndarray'
odec can't decode byte 0xe5 in position 21801: ordinal not in range(128)
 'vtkSlicerMarkupsModuleMRML.vtkMRMLMarkupsROINode' has no len()
</code></pre>
<p>??? what’s wrong???</p>

---

## Post #2 by @lassoan (2021-09-29 03:11 UTC)

<p>Please copy here the command that produced this error.</p>

---

## Post #3 by @chir.set (2021-09-29 08:01 UTC)

<p>I had this once in a script. Your’s has a ‘å’ character somewhere that Python does not like.</p>
<p>Replace the ‘å’ character by chr(0xe5).</p>
<p>As to why Python breaks with special characters in scripts while Slicer libs are compiled with UTF-8 support, I can’t tell.</p>

---

## Post #4 by @jumbojing (2021-09-29 08:34 UTC)

<p>Thanks <a class="mention" href="/u/chir.set">@chir.set</a><br>
嗯, 我想问的是,这个错和’vtkMRMLMarkupsROINode’有啥关系呢? 最近得到这个报错好几次了…</p>
<blockquote>
<p>Well, what I want to ask is, what does this error have to do with’vtkMRMLMarkupsROINode’? I got this error several times recently…</p>
</blockquote>

---

## Post #5 by @jumbojing (2021-09-29 08:44 UTC)

<p>我找到了原因: 是由于我用"slicer.util.getName(modName)"时,modName用了变量而不是字符串的名字…</p>
<blockquote>
<p>I found the reason: when I used “slicer.util.getName(modName)”, <strong>modName</strong> used a variable instead of a string name…</p>
</blockquote>

---

## Post #6 by @lassoan (2021-09-29 18:53 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="19903">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>As to why Python breaks with special characters in scripts while Slicer libs are compiled with UTF-8 support, I can’t tell.</p>
</blockquote>
</aside>
<p>It was a problem specific to how macOS loads files by default. I’ve fixed the issue now (see <a href="https://discourse.slicer.org/t/couldnt-reload-whats-wrong/19893/4" class="inline-onebox">Couldn't Reload, what's wrong - #4 by lassoan</a>).</p>

---
