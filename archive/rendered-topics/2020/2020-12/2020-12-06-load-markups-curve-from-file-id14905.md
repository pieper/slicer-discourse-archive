# Load markups curve from file

**Topic ID**: 14905
**Date**: 2020-12-06
**URL**: https://discourse.slicer.org/t/load-markups-curve-from-file/14905

---

## Post #1 by @yee (2020-12-06 04:20 UTC)

<p>Hi! When I input " <code>curveNode = slicer.util.loadMarkupsCurve('some/folder/MarkupsCurve.fcsv')</code>", I just get makups node. How can I get the markupcurve?  Thank you in advance !<br>
And if i use Edoscopy ,I  just got this.<br>
<a href="/404" data-orig-href="upload://awmrWMoJNXgeUTs34OWyk3sSNpL.png">{E54W@1HD5FZ~OJ6$KX74P7|690x359</a></p>

---

## Post #2 by @yee (2020-12-06 04:16 UTC)

<p>Hi! When I input " <code>curveNode = slicer.util.loadMarkupsCurve('some/folder/MarkupsCurve.fcsv')</code>", I just get makups node. How can I get the markupcurve? Thank you in advance.</p>

---

## Post #3 by @lassoan (2020-12-06 04:22 UTC)

<p>Legacy fcsv file format is only for landmark points. You can use the new json-based file format for other markup node types.</p>

---

## Post #4 by @lassoan (2020-12-06 05:49 UTC)

<p>A post was merged into an existing topic: <a href="/t/markupscurve-with-endoscopy-error-message/14862/8">MarkupsCurve with Endoscopy error message</a></p>

---

## Post #5 by @yee (2020-12-06 06:58 UTC)

<p>Hello ! How can I convert the markupfiducial which I imported from the txt file to the open markups curve?<br>
The code which I convert txt file to the markupfiducial is "markupNode.AddFiducial(*out[:3]) ". Thank you in advance!</p>

---
