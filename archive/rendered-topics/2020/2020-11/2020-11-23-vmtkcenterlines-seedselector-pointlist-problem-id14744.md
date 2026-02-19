---
topic_id: 14744
title: "Vmtkcenterlines Seedselector Pointlist Problem"
date: 2020-11-23
url: https://discourse.slicer.org/t/14744
---

# Vmtkcenterlines -seedselector pointlist problem

**Topic ID**: 14744
**Date**: 2020-11-23
**URL**: https://discourse.slicer.org/t/vmtkcenterlines-seedselector-pointlist-problem/14744

---

## Post #1 by @Haim_Ezer (2020-11-23 18:08 UTC)

<p>Hello, Luca, Everyone,<br>
vmtkcenterlines.py -ifile “Case1.vtk” -seedselector pointlist -sourcepoints 0.00571137 -0.01748690 -0.02422070 -targetpoints 0.00571797 -0.00042939 -0.02172360<br>
But what I get is this:<br>
Traceback (most recent call last):<br>
File “C:\ProgramData\VMTK\lib\site-packages\vmtk\pypeserver.py”, line 46, in RunPypeProcess<br>
pipe.Execute()<br>
File “C:\ProgramData\VMTK\lib\site-packages\vmtk\pype.py”, line 324, in Execute<br>
scriptObject.Execute()<br>
File “C:\ProgramData\VMTK\lib\site-packages\vmtk\vmtkcenterlines.py”, line 595, in Execute<br>
self.SeedSelector.Execute()<br>
File “C:\ProgramData\VMTK\lib\site-packages\vmtk\vmtkcenterlines.py”, line 128, in Execute<br>
for i in range(len(self.SourcePoints)/3):<br>
TypeError: ‘float’ object cannot be interpreted as an integer<br>
ANY IDEAS?<br>
Thanks<br>
Haim</p>

---

## Post #2 by @lantiga (2020-11-24 07:45 UTC)

<p>Hi <a class="mention" href="/u/haim_ezer">@Haim_Ezer</a>,<br>
you bumped into an issue related to the Python 3 port.</p>
<pre><code class="lang-python">for i in range(len(self.SourcePoints)/3):
</code></pre>
<p>should instead be</p>
<pre><code class="lang-python">for i in range(len(self.SourcePoints)//3):
</code></pre>
<p>Bottomline: in Python 2 division of an integer by an integer yields an integer, while the result of <code>/</code> between two numbers in Python 3 yields a float irrespective of the type of the operands. For that you need integer division <code>//</code>, which returns an integer irrespective of the type of the operands.</p>
<p>Anyhow, the change is came right after the last release (one more good reason to organize a new release). To patch it in the meantime, you can open your <code>C:\ProgramData\VMTK\lib\site-packages\vmtk\vmtkcenterlines.py</code> file with an editor and fix lines 128 and 133 by replacing <code>/3</code> with <code>//3</code>.</p>
<p>This should solve it in the meantime.</p>
<p>Luca</p>

---

## Post #3 by @Haim_Ezer (2020-11-26 05:47 UTC)

<p>Thx Luca,<br>
This solved my problem!</p>
<p>Just wanted to share an observation:<br>
It turns that when I scale may surface, the results are amazing!<br>
I use vmtksurfacescaling - scale 5, and this solves most of the unexpected<br>
problems.</p>
<p>Thanks again,<br>
Haim</p>

---
