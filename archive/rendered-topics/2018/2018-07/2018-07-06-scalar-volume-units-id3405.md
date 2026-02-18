# Scalar Volume Units?

**Topic ID**: 3405
**Date**: 2018-07-06
**URL**: https://discourse.slicer.org/t/scalar-volume-units/3405

---

## Post #1 by @Masteling (2018-07-06 16:52 UTC)

<p>Hi all,<br>
When using the segment statistics module, besides the volume we get the minimum, maximum, mean and standard deviation of the segmentation.<br>
What are the units of the latest (min, max, means, std)?</p>
<p>In the case of MRI, can you compare scans made in the same scanner using the same sequences, using only those values?</p>

---

## Post #2 by @fedorov (2018-07-06 17:53 UTC)

<p>MRI images are not normalized and have no units. In general, you cannot compare non-normalized MRI intensity statistics across scans.</p>
<p>For some of the MRI-derived images, such as Apparent Diffusion Coefficient derived from DWI MRI, or pharmacokinetic maps derived from DCE MRI, quantities and units are generally known at the time those maps are generated, but may not be well-exposed to the user.</p>
<p>If you have specific questions about specific types of MRI images you want to compare, please let us know more details.</p>

---

## Post #3 by @Masteling (2018-07-06 20:00 UTC)

<p>Hi Andrey,<br>
Thanks for your answer.</p>
<p>I understand it’s an arbitrary unit and I need to normalize it (we have already been doing that). My questions is more, if there is no “unit”, what do they represent or are measuring: are they proportional to water content? or proportional to some other content/characteristic?</p>
<p>Thank you</p>

---

## Post #4 by @fedorov (2018-07-06 20:17 UTC)

<p>What the signal is proportional to will depend on the sequence, and I will defer to MR physics experts to provide a concise and correct answer. In some sequence, for example, the signal can be proportional to the water content, or fat content. And you will never get a signal where you do not have protons to excite… There are many resources with the introductions:</p>
<ul>
<li>a long time ago, I worked through part of this book (an earlier edition), and I found it very approachable: <a href="https://www.amazon.com/MRI-Ray-H-Hashemi-PhD/dp/1496384326">https://www.amazon.com/MRI-Ray-H-Hashemi-PhD/dp/1496384326</a>
</li>
<li>Wikipedia is always an option: <a href="https://en.wikipedia.org/wiki/MRI_sequence">https://en.wikipedia.org/wiki/MRI_sequence</a>
</li>
</ul>

---
