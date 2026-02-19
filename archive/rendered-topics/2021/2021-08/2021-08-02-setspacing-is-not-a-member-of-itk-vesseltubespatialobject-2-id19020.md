---
topic_id: 19020
title: "Setspacing Is Not A Member Of Itk Vesseltubespatialobject 2"
date: 2021-08-02
url: https://discourse.slicer.org/t/19020
---

# ‘SetSpacing’: is not a member of ‘itk::VesselTubeSpatialObject<2>’

**Topic ID**: 19020
**Date**: 2021-08-02
**URL**: https://discourse.slicer.org/t/setspacing-is-not-a-member-of-itk-vesseltubespatialobject-2/19020

---

## Post #1 by @Mahesh_Timmanagoudar (2021-08-02 07:04 UTC)

<p>Error C2039 ‘SetSpacing’: is not a member of ‘itk::VesselTubeSpatialObject&lt;2&gt;’ [D:\W4-rel\S-bld\Slicer-build\E\TubeTK\Applications\SegmentTubeUsingMinimalPath\SegmentTubeUsingMinimalPathLib.vcxproj] Slicer D:\W4\S-rel\S-bld\TubeTK\Base\Segmentation\itktubeSegmentTubesUsingMinimalPathFilter.hxx 364</p>
<p>Hello I am upgrading ITK4.4 to latest ITK version. While building I got above error.<br>
In latest version of ITK, SetSpacing and GetSpacing methods are deprecated. May I know how can i solve the above error.</p>
<p>Actually the method is called at itktubeSegmentTubesUsingMinimalPathFilter.hxx line number 364</p>
<p>typename TubeType::Pointer pTube = TubeType::New(); //line number 361<br>
pTube-&gt;SetPoints(tubePointList); //line number 362<br>
pTube-&gt;ComputeTangentAndNormals(); //line number 363<br>
pTube-&gt;SetSpacing(tubeSpacing); //line number 364<br>
pTube-&gt;SetId(i); //line number 365</p>
<p>Please let me know how to solve this issue.</p>

---

## Post #2 by @lassoan (2021-08-02 11:59 UTC)

<p>Your can reach developers of ITK at <a href="https://discourse.itk.org">https://discourse.itk.org</a>. Please ask the question there and post the link of your question here (to allow people who are interested in this topic to join the discussing there).</p>

---
