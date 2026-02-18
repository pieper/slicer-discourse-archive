# Filtering vessels in 3D volume

**Topic ID**: 11855
**Date**: 2020-06-04
**URL**: https://discourse.slicer.org/t/filtering-vessels-in-3d-volume/11855

---

## Post #1 by @Deepa (2020-06-04 03:04 UTC)

<p>Hello Everyone,<br>
I’ve a 3D volume and I am using the <code>Margin</code> effect in Segment editor to filter vessels that have<br>
a thickness less than say 10 microns</p>
<ol>
<li>10 micron is set in Margin tab</li>
<li>select shrink and hit apply</li>
<li>select grow and hit apply</li>
</ol>
<p>I’d like to ask for suggestion on how to use Margin effect to filter vessels that fall in a certain range<br>
e.g. 5 - 10 microns.</p>
<p>Here, I would like to know if it’s possible to do the above by directly specifying the range (5-10).<br>
If not, I think I should be following the same steps mentioned above to filter out 5 microns from the above segment and subtract using logical operators.</p>
<p>Many thanks</p>

---

## Post #2 by @muratmaga (2020-06-04 15:58 UTC)

<p>Deepa, if the method you described would retain vessels with a diameter 10 microns or larger.<br>
Because if you shrink 10 micron, and the segment is only 7 micron, it will disappear. Because it has disappeared, grow operation cannot bring it back. Let’s say this is your segment_1</p>
<p>If you repeat this operation on a new segment (Segment_2) with 5 micron, then that will retain vessels that 5 or larger micron. If you subtract the Segment_1 from Segment_2 (logical operations0, you will get what you want (vessels that are larger than 5 but less than 10 micron in diameter).  For this to work, you should allow for overlap under the Masking section when doing both segmentations.</p>
<p>However, due to the smoothing there might be some left of over from Segment_1. Remove small islands might work on the resultant segment, or others might have better suggestions.</p>

---

## Post #3 by @Deepa (2020-06-04 16:36 UTC)

<p>Thanks a lot.</p>
<p>I could do the above. I would like to check the thickness of the final segment that I have.</p>
<p>Could you please suggest if I can use any plugin that is already available in Slicer to check the distribution of vessel thickness in <a href="https://drive.google.com/file/d/17C1J5qdYf_sRBQkf3Ta88rasW2_w5fua/view?usp=sharing" rel="nofollow noopener">Segment_final</a>?<br>
This would help me in cross-checking what I have done.</p>

---
