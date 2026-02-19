---
topic_id: 11174
title: "Can I Convert This Arrays In Slicer"
date: 2020-04-18
url: https://discourse.slicer.org/t/11174
---

# Can I convert this arrays in slicer?

**Topic ID**: 11174
**Date**: 2020-04-18
**URL**: https://discourse.slicer.org/t/can-i-convert-this-arrays-in-slicer/11174

---

## Post #1 by @timeanddoctor (2020-04-18 13:02 UTC)

<h2><a name="p-38784-i-want-to-creat-a-volume-by-and-i-need-convert-the-data-of-bb-to-a-in-slicer-quickly-1" class="anchor" href="#p-38784-i-want-to-creat-a-volume-by-and-i-need-convert-the-data-of-bb-to-a-in-slicer-quickly-1" aria-label="Heading link"></a>I want to creat a volume by and I need convert the data of ‘bb’ to ‘a’ in slicer quickly.</h2>
<p>bb</p>
<blockquote>
<p>array([[[[ 70,  95, 109],<br>
[ 72,  97, 112],<br>
[ 71,  96, 110],<br>
…,<br>
[ 30,  35,  42],<br>
[ 28,  36,  40],<br>
[ 27,  35,  39]]]], dtype=uint8)</p>
</blockquote>
<p>bb.shape</p>
<blockquote>
<p>(1L, 480L, 640L, 3L)</p>
</blockquote>
<p>this is my finally data ‘a’</p>
<p>a.shape</p>
<blockquote>
<p>(1L, 480L, 640L, 3L)</p>
</blockquote>
<p>a</p>
<blockquote>
<p>array([[[[109,  95,  70],<br>
[112,  97,  72],<br>
[110,  96,  71],<br>
…,<br>
[ 42,  35,  30],<br>
[ 40,  36,  28],<br>
[ 39,  35,  27]]]], dtype=uint8</p>
</blockquote>

---

## Post #3 by @lassoan (2020-04-18 14:01 UTC)

<p>You can set content of a numpy array into a volume node by calling <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.updateVolumeFromArray"><code>slicer.util.updateVolumeFromArray</code></a>. See complete example in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Combine_multiple_volumes_into_one">script repository</a>.</p>

---
