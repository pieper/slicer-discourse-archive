# Special characters

**Topic ID**: 5398
**Date**: 2019-01-17
**URL**: https://discourse.slicer.org/t/special-characters/5398

---

## Post #1 by @opetne (2019-01-17 14:09 UTC)

<p>It may sound a total stupid ask from a person who shouldn’t use any software:)<br>
Is it possible to develop a warning sign or message in a popping up window if Slicer has a problem with a special character in a folder or file name? I lost 2 days to find where the problem should be when I was not able to load or open any files since I mistyped (I typed a special hungarian characet accidentaly) a name of a complete folder.</p>

---

## Post #2 by @pieper (2019-01-17 15:19 UTC)

<p>I would love to see Slicer have better support for international character sets, and at least detecting errors would be a great start.</p>
<p>As a self-admitted stupid American, I don’t feel qualified to debug this because I don’t understand who things should be done the “right way”.</p>
<p>It would be great if there anyone who routinely uses non-ascii operating systems could implement and test such things.</p>

---

## Post #3 by @opetne (2019-01-17 19:28 UTC)

<p>Dear Steve,</p>
<p>I know <a class="mention" href="/u/lassoan">@lassoan</a> mentioned many times that Slicer is not accepting special characters. I forgot it and there is not sign that: hey you stupid, bad character in a file name! It could help a lot and save a lot of frustration.</p>
<p>Ors</p>
<p>Steve Pieper via 3D Slicer Forum <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> (időpont: 2019. jan. 17., Cs, 16:29) ezt írta:</p>

---

## Post #4 by @jcfr (2019-01-17 21:26 UTC)

<p>That made me thing of the following commit that I stumbled upon while crafting the changelog for Slicer 4.10.1.</p>
<p>See:</p>
<ul>
<li>
<a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27676" rel="nofollow noopener">r27676</a>:  ENH: Added check for non-ASCII characters when drag-and-dropping a DICOM folder</li>
</ul>
<p>The approach implemented by <a class="mention" href="/u/lassoan">@lassoan</a> could probably be generalized so that it is used in both the AddData dialog and the DICOM browser.</p>

---
