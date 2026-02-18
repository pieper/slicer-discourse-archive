# Markup annotations in Open Anatomy Export

**Topic ID**: 26366
**Date**: 2022-11-21
**URL**: https://discourse.slicer.org/t/markup-annotations-in-open-anatomy-export/26366

---

## Post #1 by @muratmaga (2022-11-21 21:43 UTC)

<p>Is conceivable that glTF export functionality of Open Anatomy can support Markups?</p>
<p>Embedding models/segmentations in <a href="http://3Dviewer.net" rel="noopener nofollow ugc">3Dviewer.net</a> is great, but occasionally one needs annotations (landmarks, labels etc) as well. Are there any alternative solutions for that?</p>

---

## Post #2 by @pieper (2022-11-21 22:22 UTC)

<p>They could be exported as static geometry.  Maybe the easiest and most general would be to have an option in Slicer to convert Markups to Models and then they would export automatically to glTF.</p>

---

## Post #3 by @muratmaga (2022-11-22 00:51 UTC)

<p>İ tried markups to models extension, but unfortunately text labels are not converted. Also essentially all you can do curves or lines, which can be acceptable for callouts, but lack of labels is a concern.</p>

---

## Post #4 by @pieper (2022-11-22 03:36 UTC)

<p>Can you do labels well in that 3D viewer?  We could export polygon text but I believe they won’t orient towards the camera (“billboard” mode) like they do in Slicer.</p>

---

## Post #5 by @muratmaga (2022-11-22 04:31 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="26366">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Can you do labels well in that 3D viewer?</p>
</blockquote>
</aside>
<p>No idea, haven’t gone that far. Know other free viewers that handles text?</p>

---

## Post #6 by @pieper (2022-11-22 05:36 UTC)

<p>It would be doable with vtkjs.  I haven’t seen it done exactly, but it should be pretty straightforward…  Now that OHIF-v3 has really nice vtkjs-based slice rendering it could be a good time to consider what it would take to build on it make a web viewer that has more Slicer-like functionality.</p>

---

## Post #7 by @muratmaga (2022-11-22 06:06 UTC)

<p>The important trick (for me at least) is being able to run this without requiring a dedicated website. I really love <a href="http://3Dviewer.net" rel="noopener nofollow ugc">3Dviewer.net</a>’s  passthrough URL functionality. For example I cannot maintain a publicly accessible website, but I can post data somewhere on the cloud with a sharable URL…</p>
<p>Would it be possible to do that with vtkjs?</p>

---

## Post #8 by @pieper (2022-11-22 06:10 UTC)

<p>Yes, all that can be done with vtk.js and with ohif.</p>
<p>There’s definitely programming required to make it just the way we want it.</p>

---

## Post #9 by @rbumm (2022-11-22 11:27 UTC)

<p>Could you post such a link and what input would you use?</p>

---

## Post #10 by @pieper (2022-11-22 18:19 UTC)

<p>We might be able to build on this: <a href="https://kitware.github.io/glance/app/" class="inline-onebox">Kitware Glance</a></p>

---

## Post #11 by @muratmaga (2022-11-22 19:11 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="9" data-topic="26366" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Could you post such a link and what input would you use?</p>
</blockquote>
</aside>
<p>Sample data from SlicerMorph <a href="https://github.com/SlicerMorph/SampleData/blob/master/baboon.gltf">https://github.com/SlicerMorph/SampleData/blob/master/baboon.gltf</a></p>
<p>You just turn into a link like this:</p>
<p><code>https://3dviewer.net/index.html#model=https://github.com/SlicerMorph/SampleData/blob/master/baboon.gltf</code></p>
<p>this is from the open anatomy extension tutorial by the way.</p>

---

## Post #12 by @muratmaga (2022-11-22 19:15 UTC)

<aside class="quote no-group" data-username="pieper" data-post="10" data-topic="26366" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>We might be able to build on this: <a href="https://kitware.github.io/glance/app/">Kitware Glance</a></p>
</blockquote>
</aside>
<p>It looks promising, but when I tried to load MRHead.nrrd I didn’t get anything, and I couldn’t figure out how to turn on 3D rendering… Not sure if it is a browser thing (firefox).</p>

---

## Post #13 by @lassoan (2022-11-22 21:39 UTC)

<p><a href="http://3dviewer.net">3dviewer.net</a> supports picking: if you click on a part then its name is highlighted in the mesh tree. Therefore, additional labels may not be necessary.</p>
<p>If you want to add labeled points then the OpenAnatomy exporter could be very easily enhanced to export each markup point as a separate small sphere. If you click on the small sphere then you can see its label in the mesh tree.</p>

---

## Post #14 by @muratmaga (2022-11-22 22:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="26366">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you want to add labeled points then the OpenAnatomy exporter could be very easily enhanced to export each markup point as a separate small sphere. If you click on the small sphere then you can see its label in the mesh tree.</p>
</blockquote>
</aside>
<p>Thank you! I will try that. Do we currently have UI driven method to export markups to spheres? (I don’t think Markups to Models module do that).</p>

---

## Post #15 by @lassoan (2022-11-23 00:23 UTC)

<p>I don’t think there is a function to export each markup point to a separate sphere model node, but it should be easy to write a short script for it (using a vtkSphereSource, similarly to this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#define-edit-a-circular-region-of-interest-in-a-slice-viewer">example</a>).</p>

---
