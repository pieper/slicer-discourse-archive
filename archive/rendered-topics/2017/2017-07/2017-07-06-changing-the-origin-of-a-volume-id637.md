# Changing the origin of a volume

**Topic ID**: 637
**Date**: 2017-07-06
**URL**: https://discourse.slicer.org/t/changing-the-origin-of-a-volume/637

---

## Post #1 by @lpott005 (2017-07-06 15:59 UTC)

<p>Hey everyone!</p>
<p>I’m having a spot of trouble with a DICOM volume. I used the resample module to change its spacing, but now I’m trying to place the origin of the whole volume so all the coordinates are positive.</p>
<p>I’m currently trying to use the reformat module &lt; <a href="https://www.slicer.org/wiki/Documentation/4.0/Modules/Reformat" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.0/Modules/Reformat</a> &gt; to change the origin, but the documentation says I can only do that slice by slice. So do I have to change every slice manually? Or is there a way to effect the change on the volume all at once?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2017-07-06 16:00 UTC)

<p>You can use Transforms module to translate a volume.</p>
<p>Why would you like to have positive coordinate values?</p>

---

## Post #3 by @lpott005 (2017-07-06 16:59 UTC)

<p>I need to generate landmarks for another bit of code I’m working with, and it’s throwing some strange errors about spacing when I use negative landmarks (I’ve already converting the volume to isotropic spacing, so it’s not that). And I’m not sure if transforms is the right thing to use- not that I don’t trust your judgement. I’d just like to shift the coordinate system, not move the volume around within it. Can I do that with the transforms module?</p>

---

## Post #4 by @lassoan (2017-07-06 17:22 UTC)

<p>Maybe what you need is landmark coordinates in voxel space (IJK) and you are wondering how to get that from landmark coordinates in physical (RAS) space?</p>
<p>See this discussion for information about RAS-&gt;IJK conversion: <a href="https://discourse.slicer.org/t/relationship-between-pixels-and-mm-from-matlab/427/2">Relationship between pixels and mm from Matlab</a></p>

---

## Post #5 by @lpott005 (2017-07-06 17:23 UTC)

<p>This looks helpful, thanks! Will update if it works.</p>

---

## Post #6 by @lpott005 (2017-07-06 18:08 UTC)

<p>Quick side question- If I have a landmark file in one set of coordinates, does slicer support converting it to another coordinate system, or will I have to go through the registration process?</p>

---

## Post #7 by @lassoan (2017-07-06 18:11 UTC)

<p>You can easily convert between coordinates defined in any coordinate system, but of course you need to know the transformation between these coordinate systems.</p>

---

## Post #8 by @JoostJM (2017-07-07 07:41 UTC)

<p>You can read the volumeNode as a SimpleITK image object (<code>image = sitkUtils.GetSlicerITKReadWriteAddress(&lt;volumeNodeName&gt;</code>), after which you can access the transformation matrix by calling <code>GetDirection()</code> on the image object.</p>
<p>Alternatively, you can use <code>image.TransformContinuousIndexToPhysicalPoint(&lt;INDEX&gt;)</code> and <code>TransformPhysicalPointToContinuousIndex(&lt;POINT&gt;)</code> to calculate coordinates in the different coordinate systems.</p>

---
