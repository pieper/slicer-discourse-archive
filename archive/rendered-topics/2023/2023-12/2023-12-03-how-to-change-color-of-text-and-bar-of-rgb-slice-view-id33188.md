---
topic_id: 33188
title: "How To Change Color Of Text And Bar Of Rgb Slice View"
date: 2023-12-03
url: https://discourse.slicer.org/t/33188
---

# How to change color of text and Bar of RGB slice view?

**Topic ID**: 33188
**Date**: 2023-12-03
**URL**: https://discourse.slicer.org/t/how-to-change-color-of-text-and-bar-of-rgb-slice-view/33188

---

## Post #1 by @1116 (2023-12-03 13:55 UTC)

<p>I want to change color of text and bar in the RGB slice view.<br>
Is it possible to change the part I circled by python script?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/919acbd190d19b0b88f745b343d22df7bc1520f7.png" alt="스크린샷 2023-12-03 225450" data-base62-sha1="kM4SIdQ3Ypb5t75D6uWjj7Jv7Qb" width="380" height="336"><br>
Thank you!</p>

---

## Post #2 by @lassoan (2023-12-03 22:20 UTC)

<p>Color of the slice view is stored in the slice view node and you can change it like this:</p>
<pre><code class="lang-auto">slicer.util.getFirstNodeByClassByName('vtkMRMLSliceNode', 'Red').SetLayoutColor(1,0,1)
</code></pre>

---

## Post #3 by @1116 (2023-12-03 23:31 UTC)

<p>Thank you! It works well</p>
<p>I have one more question.<br>
Is it possible to approach the top bar of slicer by QT &amp; Python script?<br>
<code>slicer.app.styleSheet="QWidget{color:#F0F6FC;background-color: #464646;}"</code><br>
This command changed all the widget color except the top bar.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33d6da73eedf80c5aefa69c98de7628370eabc53.png" alt="image" data-base62-sha1="7oAFFG20EVtNw1ve7izPRpcWWAz" width="175" height="23"></p>

---

## Post #4 by @lassoan (2023-12-04 12:42 UTC)

<p>It might be possible that some parts of the application window are drawn by the operating system, but most likely you can customize everything. The issue in the code snippet above might be that you only set custom style for QWidget instances and not for the main window class.</p>

---
