---
topic_id: 24449
title: "Why Is Slicerradiomics Only Partly Functional"
date: 2022-07-22
url: https://discourse.slicer.org/t/24449
---

# Why is SlicerRadiomics only partly functional?

**Topic ID**: 24449
**Date**: 2022-07-22
**URL**: https://discourse.slicer.org/t/why-is-slicerradiomics-only-partly-functional/24449

---

## Post #1 by @harad (2022-07-22 10:45 UTC)

<p>Hi everyone, I wonder why the GUI of Slicer radiomics has a massively trimmed functionality in comparison to the standalone Pyradiomics. Thereby, only LoG, Wavelet and Original image types can be activated. That leaves seven other image transformations unavailable, such as exponential,  logarithm, square etc… I know that a full array of image modifications can be achieved by using a Parameters file but such a file in YAML is extremely user-unfriendly for anyone who is not seasoned code developer. Besides, the SlicerRadiomics is devoid of a BATCH function. My question is then whether the functionality of the SlicerRadiomics could be expanded to include all functions of the standalone version, as this would be a miracle for scientists with limited coding skills. Cheers, Marko</p>

---

## Post #2 by @jamesobutler (2022-07-22 12:59 UTC)

<p>My inclination is to say probably a lack of funding or lack of developer time or both. It appears that SlicerRadiomics has been in maintenance mode since about 2018 without many new enhancements made on the Slicer module side. See <a href="https://github.com/AIM-Harvard/SlicerRadiomics/graphs/code-frequency" class="inline-onebox" rel="noopener nofollow ugc">Code frequency · AIM-Harvard/SlicerRadiomics · GitHub</a></p>
<p>Cc: SlicerRadiomics developers <a class="mention" href="/u/joostjm">@JoostJM</a> <a class="mention" href="/u/fedorov">@fedorov</a> for the actual specifics about how the SlicerRadiomics module might get future improvements.</p>

---

## Post #3 by @fedorov (2022-07-22 13:46 UTC)

<p><a class="mention" href="/u/harad">@harad</a> that’s a fair question, and <a class="mention" href="/u/jamesobutler">@jamesobutler</a> thanks for heads up.</p>
<p>Yes, the situation is that both pyradiomics and SlicerRadiomics development was covered by a grant that by now is long finished. There is no personnel funded to maintain those tools, and all maintenance is done by Joost and me on our spare time, or time taken away from other funded projects (and I would say at least 95% of what was done in the past years in terms of maintaining those is Joost who continued to work on pyradiomics after the grant was over!).</p>
<p>But another part of it has been lack of feedback from the users. For example, I never thought that anyone actually needs those other transformations. I will look into this, it may not be hard to add those. About BATCH mode, I personally never thought of Slicer or SlicerRadiomics as a tool to support batch processing. Joost was working on <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerCaseIterator">CaseIterator</a>, which may help with this, but I personally never used it. But again, now that you mention it, it creates at least the motivation to add this feature. Although, I can’t tell when anyone might look into implementing it.</p>

---

## Post #4 by @fedorov (2022-07-22 13:54 UTC)

<p>I submitted two issues to at least keep track of this request:</p>
<ul>
<li><a href="https://github.com/AIM-Harvard/SlicerRadiomics/issues/74" class="inline-onebox">Add support for additional image transformations in pyradiomics · Issue #74 · AIM-Harvard/SlicerRadiomics · GitHub</a></li>
<li><a href="https://github.com/AIM-Harvard/SlicerRadiomics/issues/75" class="inline-onebox">Add support for BATCH mode · Issue #75 · AIM-Harvard/SlicerRadiomics · GitHub</a></li>
</ul>

---
