# Could I edit qMRML~Widget in Qt designer?

**Topic ID**: 35684
**Date**: 2024-04-23
**URL**: https://discourse.slicer.org/t/could-i-edit-qmrml-widget-in-qt-designer/35684

---

## Post #1 by @park (2024-04-23 15:45 UTC)

<p>Hello everyone,</p>
<p>I’m interested in creating a custom widget using the qMRML~Widget in Qt Designer, particularly the qMRMLMarksupROIWidget.</p>
<p>For the qMRMLMarksupROIWidget, I only require a slider to adjust the size of the ROI. Specifically, I want to remove all other elements and reposition the slider.</p>
<p>Is this achievable in Qt Designer?<br>
If so, which approach would be more efficient: rebuilding the functionality from scratch or utilizing the qMRML Widget?</p>

---

## Post #2 by @lassoan (2024-04-24 01:34 UTC)

<p>If you only need a single slider then probably you don’t need to create a new widget for it, you can just use a Qt or CTK slider widget.</p>

---

## Post #3 by @park (2024-04-24 02:26 UTC)

<p>Thank you for your response.</p>
<p>I created a slider using ctkRangeSlider as you advised, but there is an issue.<br>
The style of the selected range doesn’t change as I want it to.</p>
<p>I’ve tried changing the color somewhat using the following code:</p>
<pre data-code-wrap="css"><code class="lang-css">ctkRangeSlider, QSlider {
    selection-background-color: #427d7a;
}
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b01d10f399ffda5193de5e636ce966ddb3331421.png" alt="캡처" data-base62-sha1="p7Yj9lcAmxNgtUrFdrqBDtNQ6Rz" width="273" height="141"></p>
<p>But as you can see in the image, the gradient and border colors are still present.</p>
<p>How can I resolve this?</p>

---
