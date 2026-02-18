# Is PLUS compatible with Cygnus-PFS a DC magnetic navigate

**Topic ID**: 2123
**Date**: 2018-02-20
**URL**: https://discourse.slicer.org/t/is-plus-compatible-with-cygnus-pfs-a-dc-magnetic-navigate/2123

---

## Post #1 by @timeanddoctor (2018-02-20 13:33 UTC)

<p>Is PLUS compatible with Cygnus-PFS?<br>
Cygnus-PFS:<a href="http://ciimedical.com/RegulusArticle.pdf" rel="nofollow noopener">paper</a><br>
I read this post and there is nothing information like that.<br>
<a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceNDI.html" rel="nofollow noopener">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceNDI.html</a><a href="https://discourse.slicer.org/t/ndi-vega-compatibility/1969">https://discourse.slicer.org/t/ndi-vega-compatibility/1969</a></p>

---

## Post #2 by @lassoan (2018-02-20 13:53 UTC)

<p>I have never heard of Cygnus-PFS but from their website it seems that they use Ascension 3DG tracker, which Plus can connect to. However, only one application can connect to an Ascension tracker at a time, so while you are using the Cygnus software then you cannot connect using Plus at the same time.</p>

---

## Post #3 by @timeanddoctor (2018-02-20 13:53 UTC)

<blockquote>
<p>The Regulus Navigator (RN) utilizes a commercially available 144 Hz pulsed DC<br>
Flock of Birds (Ascension Technology Corporation; Burlington, VT 05402) magnetic<br>
field transmitter as its digitizer which defines its three-dimensional coordinate system.</p>
</blockquote>
<p>I cheaked carefully, find I can use NDI…</p>

---

## Post #4 by @timeanddoctor (2018-02-20 13:54 UTC)

<p>ok, I will try it…<br>
Thanks.</p>

---

## Post #5 by @lassoan (2018-02-20 13:54 UTC)

<p>The paper that was referenced described a 20+ year old variant of the system that used Ascension Flock-of-birds tracker. However, from the <a href="http://ciimedical.com/index.php?p=arm">pictures on their website</a> it is clear that their current system uses Ascension 3DG.</p>

---

## Post #6 by @timeanddoctor (2018-02-20 13:57 UTC)

<p><a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceNDI.html" class="onebox" target="_blank" rel="nofollow noopener">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceNDI.html</a><br>
So I can connect it by PLUS follow the above tutorial?<br>
Thanks!</p>

---

## Post #7 by @lassoan (2018-02-20 13:58 UTC)

<p>It is an Ascension 3DG tracker, so you can find information on this page: <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceAscension3DG.html">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceAscension3DG.html</a></p>

---

## Post #8 by @timeanddoctor (2018-02-20 14:00 UTC)

<p>Ok, Thanks.<br>
I will connect it and do something with 3d slicer.</p>

---
