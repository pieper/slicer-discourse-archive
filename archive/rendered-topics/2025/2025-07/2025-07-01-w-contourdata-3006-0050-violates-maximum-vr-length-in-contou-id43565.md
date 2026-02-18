# W: ContourData (3006,0050) violates maximum VR length in ContourSequence

**Topic ID**: 43565
**Date**: 2025-07-01
**URL**: https://discourse.slicer.org/t/w-contourdata-3006-0050-violates-maximum-vr-length-in-contoursequence/43565

---

## Post #1 by @ferhue (2025-07-01 18:03 UTC)

<p>Hello,</p>
<p>When loading in Slicer, I get the following warning printed many times:<br>
<code>W: ContourData (3006,0050) violates maximum VR length in ContourSequence</code></p>
<p>I do not fully understand this, since the largest sequence contains about 32000 characters, and I thought that it would support until 65000 bytes.</p>
<p>I am generating these RTstruct using pydicom.<br>
Is there a trick to tell pydicom to remove decimal places in the floating points to make it fit into the maximum VR length? Or is this rather a bug in dcmtk? I set ExplicitVRLittleEndian, not sure if that is relevant.</p>
<p>Note that Slicer seems to load the file and visualize it correctly, the only problem are the warnings in the log (of severity critical)</p>
<p>CT Files and RTstruct are here: <a href="https://consigna.uv.es/?recoge:ca:5266_8206_2288_7250" class="inline-onebox" rel="noopener nofollow ugc">Consigna UV - Arreplegant fitxer</a></p>
<p>I am using 3DSlicer 5.8.1</p>
<p>fyi <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @issakomi (2025-07-03 02:10 UTC)

<blockquote>
<p><code>W: ContourData (3006,0050) violates maximum VR length in ContourSequence</code></p>
</blockquote>
<p><code>dciodvfy</code> also complains about it, e.g.</p>
<p><code>Error - Value invalid for this VR - (0x3006,0x0050) DS Contour Data  DS [3] = &lt;-1087.5608163265306&gt; - Length invalid for this VR = 19, expected &lt;= 16</code></p>
<p>There are very many such warnings.<br>
But it is related to individual DS entries, DS should be max. 16 bytes. BTW, with most programs this is usually not a problem.</p>
<blockquote>
<p>I set ExplicitVRLittleEndian, not sure if that is relevant.</p>
</blockquote>
<p>It may be relevant for large contours, but it is not relevant in this particular case. S. <a href="https://dicom.nema.org/medical/dicom/current/output/chtml/part05/chapter_7.html#table_7.1-1" rel="noopener nofollow ugc">Tables 7.1-1, 7.1-2 and 7.1-3</a>. For explicit TS + VR::DS the value length field of the data element is <em>uint16</em>. For implicit it is always <em>uint32</em>. It is also mentioned here s. DS in the <a href="https://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_6.2.html#table_6.2-1" rel="noopener nofollow ugc">Table 6.2-1</a></p>

---

## Post #3 by @ferhue (2025-07-03 05:47 UTC)

<aside class="quote no-group" data-username="issakomi" data-post="2" data-topic="43565">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/b9e5f3/48.png" class="avatar"> issakomi:</div>
<blockquote>
<p>DS should be max. 16 bytes.</p>
</blockquote>
</aside>
<p>Thanks a lot for the reply. So this issue might surely come from <a href="https://github.com/pydicom/pydicom/issues/1264" class="inline-onebox" rel="noopener nofollow ugc">Strings with Value Representation DS are too long · Issue #1264 · pydicom/pydicom · GitHub</a> and it seems easy to change.</p>

---
