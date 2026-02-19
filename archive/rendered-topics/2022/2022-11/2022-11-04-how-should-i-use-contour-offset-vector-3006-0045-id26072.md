---
topic_id: 26072
title: "How Should I Use Contour Offset Vector 3006 0045"
date: 2022-11-04
url: https://discourse.slicer.org/t/26072
---

# How should I use Contour Offset Vector (3006,0045)?

**Topic ID**: 26072
**Date**: 2022-11-04
**URL**: https://discourse.slicer.org/t/how-should-i-use-contour-offset-vector-3006-0045/26072

---

## Post #1 by @Alexandre_Huat (2022-11-04 14:24 UTC)

<p>Hi, my colleague and I have read the doc of DICOM Data Element Contour Offset Vector but we don’t understand how we should exactly use it to correct the Contour Data of an RT Structure Set. The doc is ambiguous, it says:</p>
<blockquote>
<h5><a href="https://dicom.nema.org/medical/dicom/2020b/output/chtml/part03/sect_C.8.8.6.html" rel="noopener nofollow ugc">C.8.8.6 ROI Contour Module</a></h5>
<h6>Contour Offset Vector (3006,0045)</h6>
<p>Vector (x,y,z) in the Patient-Based Coordinate System described in <a href="https://dicom.nema.org/medical/dicom/2020b/output/chtml/part03/sect_C.7.6.2.html#sect_C.7.6.2.1.1" rel="noopener nofollow ugc">Section C.7.6.2.1.1</a> that is normal to plane of Contour Data (3006,0050), <strong>describing direction and magnitude of the offset (in mm) of each point of the central plane of a contour slab from the corresponding original point of Contour Data</strong> (3006,0050). See <a href="https://dicom.nema.org/medical/dicom/2020b/output/chtml/part03/sect_C.8.8.6.2.html" rel="noopener nofollow ugc">Section C.8.8.6.2</a>.</p>
</blockquote>
<p>with</p>
<blockquote>
<h5><a href="https://dicom.nema.org/medical/dicom/2020b/output/chtml/part03/sect_C.8.8.6.2.html" rel="noopener nofollow ugc">C.8.8.6.2 Contour Slab Thickness</a></h5>
<p>A set of Contour slabs may define a multi-slab Volume of Interest. Contour Slab Thickness (3006,0044) shall specify the thickness of <strong>a slab, the central plane of which shall be defined by the set of points offset from Contour Data (3006,0050) by the value of Contour Offset Vector (3006,0045)</strong>. […]</p>
</blockquote>
<p>We see two possible understandings. Consider a contour offset vector <em>u = (a, b, c)</em> and a contour point with contour data <em>p = (x, y, z)</em>. What are the actual coordinates <em>q</em> of that point?</p>
<ol>
<li><em>q = p - u = (x - a, y - b, z - c)</em></li>
<li><em>q = p + u = (x + a, y + b, z + c)</em></li>
</ol>
<p>Thank you for your help.</p>

---

## Post #2 by @lassoan (2022-11-04 14:47 UTC)

<p>Probably nobody knows (except maybe David Clunie), because these field are not used in practice. See for example <a href="https://github.com/search?q=ContourSlabThickness&amp;type=Code">usages of this field in all projects on github</a> - they all seem to be just about defining and copying the value, they are not used in any computation.</p>
<p>Have you ever seen a DICOM RTSTRUCT with these fields present? If you haven’t seen such data sets, but you are not comfortable simply ignoring these fields then you can display a warning to the user or reject loading the series if the fields are present.</p>

---

## Post #3 by @Alexandre_Huat (2022-11-04 15:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="26072">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Have you ever seen a DICOM RTSTRUCT with these fields present?</p>
</blockquote>
</aside>
<p>Yes, that’s why I’m asking. I know that Contour Offset Vector was removed from DICOM in 2021 but some files that date back to the 2010s use it.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="26072">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>you can display a warning to the user or reject loading the series if the fields are present.</p>
</blockquote>
</aside>
<p>That’s our current “fix” indeed.</p>

---

## Post #4 by @Alexandre_Huat (2022-11-17 13:30 UTC)

<p>Some updates: I had a short mail exchange with David Clunie (thank you <a class="mention" href="/u/lassoan">@lassoan</a>) and Christof Schadt who is a member of the DICOM WG-07 and removed the Contour slab mechanism as part of the Change Proposal (CP) 2006.</p>
<p>About Contour Offset Vector, Christof said:</p>
<blockquote>
<p>As it is proposed by the definition of the Contour Slab Thickness, it is used to define multiple contour slabs out of a single contour. But <strong>I have to admit I also do not fully understand how this is to be used</strong>.</p>
<p>And that is also one of the main reasons why <strong>the DICOM WG-07 (Radiotherapy) decided to retire this concept, as there is no known application that has implemented this feature</strong>. As a result, in case you want to achieve interoperability, I would not recommend implementing this attribute.</p>
<p>(…)</p>
<p>We are currently at the IHE-RO Connectathon (…) and basically all the major vendors are present (Accuray, Brainlab, Elekta, IBA, Mevion, RaySearch, Varian/Siemens). And regarding the RT Structure Set, there is <strong>the <a href="https://www.ihe.net/resources/technical_frameworks/#radiationoncology" rel="noopener nofollow ugc">Basic RT Objects Profile</a></strong> that <strong>is tested this week</strong> and there, <strong>the usage of slabs is not included</strong>.</p>
<p><strong>I talked to one of the individuals who was present when the DICOM RT Structure Set was originally defined and also he cannot remember the reason why it is there (and also cannot reconstruct it from the DICOM Standard).</strong></p>
</blockquote>
<p>So my colleague and I will definitely not try to do anything with this Contour Offset Vector and Contour Slab Thickness attributes.</p>

---
