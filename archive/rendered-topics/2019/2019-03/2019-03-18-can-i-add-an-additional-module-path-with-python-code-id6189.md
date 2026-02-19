---
topic_id: 6189
title: "Can I Add An Additional Module Path With Python Code"
date: 2019-03-18
url: https://discourse.slicer.org/t/6189
---

# Can I add an "additional module path" with python code

**Topic ID**: 6189
**Date**: 2019-03-18
**URL**: https://discourse.slicer.org/t/can-i-add-an-additional-module-path-with-python-code/6189

---

## Post #1 by @timeanddoctor (2019-03-18 12:24 UTC)

<p>Can I restart 3d slicer and add an “additional module path” with python code.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d71f31be2421ec74e907383111b1b6c121f1ecc.jpeg" alt="360%E6%88%AA%E5%9B%BE-997969" data-base62-sha1="dkExwB8L53xq9X3bf5TJkwA0GGU" width="630" height="186"></p>

---

## Post #2 by @lassoan (2019-03-18 12:44 UTC)

<p>Yes, sure. You don’t even need to restart to load additional Python modules. See source code of extension wizard for details.</p>

---

## Post #3 by @pieper (2019-03-18 12:52 UTC)

<p>Also, you can have a look at how the <a href="https://github.com/Slicer/Slicer/search?q=Additional+module+paths&amp;unscoped_q=Additional+module+paths" rel="nofollow noopener">modules panel</a> handles <a href="https://github.com/Slicer/Slicer/blob/9a1c335d8b6896f3deabc550721a5deca07247b6/Base/QTGUI/qSlicerDirectoryListView.h#L34" rel="nofollow noopener">directory paths.</a>.  And <code>slicer.util.restart()</code>.</p>

---

## Post #4 by @derekcbr (2023-12-15 08:50 UTC)

<p>Can not find the source code. Can you help with it?</p>

---
