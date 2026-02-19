---
topic_id: 12832
title: "2020 08 04 Hangout W Project Week Discussion"
date: 2020-08-03
url: https://discourse.slicer.org/t/12832
---

# 2020.08.04 Hangout w/ Project Week Discussion

**Topic ID**: 12832
**Date**: 2020-08-03
**URL**: https://discourse.slicer.org/t/2020-08-04-hangout-w-project-week-discussion/12832

---

## Post #1 by @Sam_Horvath (2020-08-03 15:12 UTC)

<p>Hi all:</p>
<p>We will be having the developer hangout tomorrow at 10:00 AM EST until 11 AM EST.</p>
<p>We will be brainstorming ideas for what a fully virtual January project week could look like.</p>
<p>Anyone is welcome to join to ask questions at <a href="https://bit.ly/slicer-googlemeet-hosted-by-kitware" rel="nofollow noopener">https://bit.ly/slicer-googlemeet-hosted-by-kitware </a></p>
<p>Agenda:</p>
<ul>
<li>Slicer 5 progress check-in</li>
<li>Slicer updated website review
<ul>
<li>Discuss the content of the “What is Slicer” section. See <a href="https://github.com/Slicer/slicer.org/issues/35" rel="nofollow noopener">https://github.com/Slicer/slicer.org/issues/35</a>
</li>
<li>Revisit integration of a fixed nav bar at the top of the main page. See <a href="https://github.com/Slicer/slicer.org/issues/17" rel="nofollow noopener">https://github.com/Slicer/slicer.org/issues/17</a>
</li>
<li>Discuss the content of the “Features” section. Should it be less verbose ? See <a href="https://github.com/Slicer/slicer.org/issues/19" rel="nofollow noopener">https://github.com/Slicer/slicer.org/issues/19</a>
</li>
<li>Agree on an initial set of images to associated the image carousel</li>
<li>Finalize items listed in the footer. See <a href="https://github.com/Slicer/slicer.org/issues/36" rel="nofollow noopener">https://github.com/Slicer/slicer.org/issues/36</a>
</li>
</ul>
</li>
<li>Project Week Brainstorming from 10:30 on !!</li>
</ul>
<p>Feel free to post to this thread to request/suggest a topic!</p>
<p>Thanks<br>
Sam and J-Christophe</p>

---

## Post #2 by @Sam_Horvath (2020-08-04 14:02 UTC)

<ul>
<li>Mac build issues: <a href="https://github.com/Slicer/Slicer/issues/5079" rel="nofollow noopener">https://github.com/Slicer/Slicer/issues/5079</a>
</li>
</ul>

---

## Post #3 by @jcfr (2020-08-04 16:06 UTC)

<p><em>Notes are also available in this <a href="https://docs.google.com/document/d/1pDJ6hh2QrjD7gygO68nyAK3NZy8TNzZ5M2PuUwxSiSY/edit#">Google document</a></em></p>
<p>Discussed:</p>
<ul>
<li>Website redesign issues</li>
<li>Testing failure on mac - could not see any commits that were likely to have caused regression so maybe something about the build machine</li>
<li>Looked at multiplex microscopy example data and discussed threading performance issues (Steve shared images like the one pasted below). Pan/zoom with hotlinked slice viewers is not optimized currently (effectively single threaded)</li>
<li>Discussed plans for a project week focused on collaborations with Africa. Planning on the week of 14th of December. In two weeks we want to have several projects to discuss. Tina will invite participants. Likely themes are anatomy education, neurosurgery, and nephrostomy.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://lh4.googleusercontent.com/GmToZSTzQ2rDf9Z0AYWC0gJPOFn9NSorhfwRfEDsQ4G7Ck0lpSjKwByRhZPbq1VtH-cH2qipY7PnKlKR8O74pf7k5UaGppQJu9JnxGMcK5L_faSoaTNLVRW8GDgct6W0ChzMUDhK" title=""><img src="https://lh4.googleusercontent.com/GmToZSTzQ2rDf9Z0AYWC0gJPOFn9NSorhfwRfEDsQ4G7Ck0lpSjKwByRhZPbq1VtH-cH2qipY7PnKlKR8O74pf7k5UaGppQJu9JnxGMcK5L_faSoaTNLVRW8GDgct6W0ChzMUDhK" alt="" width="662" height="483"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use xlink:href="#far-image"></use></svg><span class="filename"></span><span class="informations">1504×1095</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use xlink:href="#discourse-expand"></use></svg></div></a></div></p>
<p>Example multiplex microscopy image. 36 channels of data mapped to RGB slices. Original data is 83GB uncompressed (~ 30k x 30k pixels). More info about the data <a href="https://www.cycif.org/">https://www.cycif.org/</a></p>

---
