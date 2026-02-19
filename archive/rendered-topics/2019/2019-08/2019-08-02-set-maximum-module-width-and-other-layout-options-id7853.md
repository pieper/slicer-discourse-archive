---
topic_id: 7853
title: "Set Maximum Module Width And Other Layout Options"
date: 2019-08-02
url: https://discourse.slicer.org/t/7853
---

# Set maximum module width and other layout options

**Topic ID**: 7853
**Date**: 2019-08-02
**URL**: https://discourse.slicer.org/t/set-maximum-module-width-and-other-layout-options/7853

---

## Post #1 by @Prashant_Pandey (2019-08-02 19:55 UTC)

<p>Slicer 4.10.2</p>
<p>I’m writing a scriptable module, and by default the width of the module is too large and it takes up too much of the screen on my laptop. Is there a way to set the overall maximum layout for the complete module, or at least the default width when the module is first initialized?</p>
<p>Also, where can I look up other layout options for the module (for example vertical/horizontal white spacing, centering widgets, etc) ? Thanks</p>

---

## Post #2 by @lassoan (2019-08-02 20:13 UTC)

<p>There is no Slicer-specific API for size management, everything is controlled by Qt size policies that you set on your widgets.</p>

---

## Post #3 by @Prashant_Pandey (2019-08-04 16:07 UTC)

<p>Could you point me to the Qt widget documentation? For example, how do I set white space in the slicer module, etc?</p>

---

## Post #4 by @lassoan (2019-08-05 00:02 UTC)

<p>See <a href="https://doc.qt.io/qt-5/qwidget.html#sizePolicy-prop" rel="nofollow noopener">qWidget::size Policy</a>. White space may be added by changing margins or adding spacer widgets.</p>

---
