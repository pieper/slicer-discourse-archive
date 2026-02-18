# Create axis trough cylinder model

**Topic ID**: 18543
**Date**: 2021-07-06
**URL**: https://discourse.slicer.org/t/create-axis-trough-cylinder-model/18543

---

## Post #1 by @sfglio (2021-07-06 20:13 UTC)

<p>I would like to create (by calculation) an axis in the middle of a cylinder (as seen in the attached file).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b4f8157503d2e7f231d99c8979044a53c08a75e.png" data-download-href="/uploads/short-url/1C3AFclmTnt3H7mtip21kmqJkFE.png?dl=1" title="axis" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b4f8157503d2e7f231d99c8979044a53c08a75e_2_144x500.png" alt="axis" data-base62-sha1="1C3AFclmTnt3H7mtip21kmqJkFE" width="144" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b4f8157503d2e7f231d99c8979044a53c08a75e_2_144x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b4f8157503d2e7f231d99c8979044a53c08a75e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b4f8157503d2e7f231d99c8979044a53c08a75e.png 2x" data-dominant-color="D2D0D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">axis</span><span class="informations">166×576 32.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is this something which could be achieved in Slicer?<br>
I thought of performing hole filling in advance and maybe cut the cylinder at the bottom, yet I would like to know if it would be possible to create this axis as I would like to calculate the angle between multiple scans of the same specimen…</p>

---

## Post #2 by @lassoan (2021-07-09 05:30 UTC)

<p>Filling the cylinder in Segment Editor is a good idea. You can then use Segment Statistics module to get the position and direction of the cylinder’s long axis.</p>

---

## Post #3 by @sfglio (2021-07-10 08:21 UTC)

<p>Thank you!<br>
Can I just choose use any random image data (e.g. from the example data) just to provide  RAS coordinates to Segment editor (otherwise it does not work without providing a scalar volume)?<br>
I loaded the MRI head example as scalar volume.</p>
<p>How can I calculate now the angle between the z-axis (this should be the long-axis through the cylinder  between those two segments)? (I assume the axes are vectors and represented by the coordinates x y z)</p>
<p>I assume that only the cylinder needs to be depicted without any other structure to make this workflow work?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfee840ffb0302a9960c13f6fa43de606f3e3cff.png" data-download-href="/uploads/short-url/vWZuCaVnZTQmYWtHguGeRA3Z1AX.png?dl=1" title="Bildschirmfoto 2021-07-10 um 10.15.14" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfee840ffb0302a9960c13f6fa43de606f3e3cff_2_690x97.png" alt="Bildschirmfoto 2021-07-10 um 10.15.14" data-base62-sha1="vWZuCaVnZTQmYWtHguGeRA3Z1AX" width="690" height="97" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfee840ffb0302a9960c13f6fa43de606f3e3cff_2_690x97.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfee840ffb0302a9960c13f6fa43de606f3e3cff_2_1035x145.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfee840ffb0302a9960c13f6fa43de606f3e3cff_2_1380x194.png 2x" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2021-07-10 um 10.15.14</span><span class="informations">1868×264 14.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-07-13 03:06 UTC)

<p>If you use the GUI then you can use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#panels-and-their-use">Specify geometry button</a> to create an empty labelmap volume automatically. Alternatively, you can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-a-new-volume">create a volume from scratch</a>.</p>

---
