# Showing Arteries

**Topic ID**: 17288
**Date**: 2021-04-24
**URL**: https://discourse.slicer.org/t/showing-arteries/17288

---

## Post #1 by @IzzyRobb (2021-04-24 01:29 UTC)

<p>I’m trying to locate the Circle of Willis within a brain scan (just using sample data for now) but am finding it hard to segment the arteries from the rest of the scan. Is there a specific module or method to use to show this? Am a beginner so any help is appreciated!</p>

---

## Post #2 by @chir.set (2021-04-24 10:51 UTC)

<p>Segmenting the Willis circle is not a satisfactory exercise. Its intensity range overlaps much with those in neighbouring veins and the arteries are very close to the skull bones.</p>
<p>I found Volume Rendering more useful to study the Willis circle with a surgical eye. CT-cardiac3 and Vesselness filters (if VMTK is installed) are the more helpful. You need to play much with the ‘Shift’ slider bar, and a little with ‘Scalar Opacity Mapping’ (as per the filter in use). Much rotation and zooming on targeted zones of interest are required for a good understanding of that particular arterial disposition. The book description is in fact very, very rarely seen.</p>
<p>Once you have identified parts of the Willis circle, it is theoretically possible to segment them using Paint and Masking tools in the Segment Editor. But it is much time consuming, and might be good only for presentations.</p>
<p>As an example, the pictures below show a Willis circle with these peculiars :</p>
<ul>
<li>the anterior communicating artery is well seen, in a nearly ‘bookish’ way</li>
<li>the left posterior communicating artery is well visible, which is not that common</li>
<li>the P2 segment of the left posterior cerebral artery originates from the left posterior communicating artery, because</li>
<li>the P1 segment of the left posterior cerebral artery is missing</li>
<li>the right posterior cerebral artery is normal and complete</li>
<li>the right posterior communicating artery is missing, which is quite common</li>
<li>the A1 segment of the right anterior cerebral artery is patent, but smaller than on the left side</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3c4569ec0af55134157d50f909a06872f971497.jpeg" alt="Willis_0" data-base62-sha1="yMsG3ru6ej2THDfVYhjpefaeEvB" width="644" height="445"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/349b1802bff07490dfe1b391c499951963ba2114.png" alt="Willis_1" data-base62-sha1="7vn79wjzj1Pj7lOwar8MeSMeKJC" width="644" height="445"></p>
<p>If you need to study the Willis circle from a surgical point of view, Slicer is your best friend. Don’t take any surgical decisions right away. You will have to go through the pains of mastering anything new first.</p>
<p>Best of luck.</p>

---

## Post #3 by @lassoan (2021-04-25 14:01 UTC)

<p>It is great to see here questions answered not just from engineering but from clinical perspective. <a class="mention" href="/u/chir.set">@chir.set</a> thank you for your very valuable insight.</p>

---
