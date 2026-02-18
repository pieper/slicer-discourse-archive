# Scissor operation in Segmentation Editor

**Topic ID**: 19249
**Date**: 2021-08-18
**URL**: https://discourse.slicer.org/t/scissor-operation-in-segmentation-editor/19249

---

## Post #1 by @Manav_Kothari (2021-08-18 11:18 UTC)

<p>I would like to generate a complex domain from a DICOM file by specifying the software of the domain in each and every slide/image. However, the scissor tool operates through the entire segmentation. Is there any way to change this setting according to my requirement?</p>
<p>Basically, I would like to change the highlighted setting mentioned in the attached image<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/503dcecdbacd0a38c5ff03dcd73cb5dda34f938e.png" alt="image" data-base62-sha1="brQCspoFLOcLHbyq0Q1x4kPKW7Q" width="666" height="391"></p>

---

## Post #2 by @jamesobutler (2021-08-18 11:35 UTC)

<aside class="quote no-group" data-username="Manav_Kothari" data-post="1" data-topic="19249">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/manav_kothari/48/11104_2.png" class="avatar"> Manav_Kothari:</div>
<blockquote>
<p>However, the scissor tool operates through the entire segmentation.</p>
</blockquote>
</aside>
<p>It can work only on a specific slice if you choose “Symmetric” instead of “Unlimited”.</p>

---
