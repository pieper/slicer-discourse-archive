# Virtual extraction (dental)

**Topic ID**: 5929
**Date**: 2019-02-26
**URL**: https://discourse.slicer.org/t/virtual-extraction-dental/5929

---

## Post #1 by @Jmarcs (2019-02-26 12:37 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:<br>
how is the best way to get a virtual extraction   best regards</p>

---

## Post #2 by @Andinet_Enquobahrie (2019-03-01 12:29 UTC)

<p>Hi,</p>
<p>You can do something like what is shown in the following movie using Slicer Segment Editor Modules</p>
<div class="lazyYT" data-youtube-id="U3eG78ogpkk" data-youtube-title="Virtual tooth extraction and ovate pontic site creation using Autodesk MeshMixer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>A good starting point is to review the segmentation tutorials</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation</a></p>
<p>Let us know if you have specific questions after you review the tutorials and try out the Segment Editor Module to do the extraction</p>
<p>Best,<br>
-Andinet</p>

---

## Post #3 by @Jmarcs (2019-07-14 08:09 UTC)

<p>thanks but the question was about extraction with 3D SLICER and not with Meshmixer</p>
<p>best regards</p>

---

## Post #4 by @lassoan (2019-07-14 12:49 UTC)

<p>As <a class="mention" href="/u/andinet_enquobahrie">@Andinet_Enquobahrie</a> suggested above, you can use Segment Editor module in Slicer to do this. For example, segment a tooth using “Grow from seeds” effect then remove it (replace it with voxel value corresponding to air) using “Mask volume” effect.</p>

---

## Post #5 by @Jmarcs (2019-07-14 13:27 UTC)

<p>3d slicer is great app. Thanks to all the team Thanks a lot  i think it is the best flow to get it</p>

---
