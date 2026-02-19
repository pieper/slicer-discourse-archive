---
topic_id: 30571
title: "How To Hide Or Delete The Help Acknowledgement Bar"
date: 2023-07-13
url: https://discourse.slicer.org/t/30571
---

# How to hide or delete the Help&Acknowledgement bar

**Topic ID**: 30571
**Date**: 2023-07-13
**URL**: https://discourse.slicer.org/t/how-to-hide-or-delete-the-help-acknowledgement-bar/30571

---

## Post #1 by @slicer365 (2023-07-13 00:07 UTC)

<p>In slicer,every module has a Help bar, as is shown in this pic.</p>
<p>I wonder hide or delete it ,is there any way ?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23b989fd98a7b6d13159075b67c7e3a4770fae7a.png" alt="17" data-base62-sha1="562e4zjDyVftmwVzyk2IDBm7D6y" width="387" height="81"></p>

---

## Post #2 by @lassoan (2023-07-13 01:02 UTC)

<p>You can hide it using this command:</p>
<pre><code>slicer.util.setModuleHelpSectionVisible(False)
</code></pre>
<p>Why would you like to hide it? To save space?</p>

---

## Post #3 by @slicer365 (2023-07-13 01:19 UTC)

<p>Thank you!<br>
Because I want to embed other module into my current module, but then there will be two same help columns，so I want to hide the embed module’s help bar.</p>

---

## Post #4 by @slicer365 (2023-07-13 01:22 UTC)

<p>Another problem is that the command will hide all modules’ Help bar.<br>
Actually I just want to hide the embed module’s bar</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5e60b722f704a79ef49d7653d085f1c00982ac2.png" alt="image" data-base62-sha1="uwezk1FytvqfmrLQ0RBRT0g8v9o" width="450" height="255"></p>

---

## Post #5 by @lassoan (2023-07-13 01:34 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="3" data-topic="30571">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>Because I want to embed other module into my current module</p>
</blockquote>
</aside>
<p>I would not recommend doing this. Module GUI is not intended to be reused or duplicated and you may run into issues if you do it anyway. It is also not a good idea because module GUI always has input/output node selectors that you typically don’t need when you want to show some widgets embedded in another module’s GUI.</p>
<p>The proper solution is to build your module GUI from reusable widgets. These widgets can be instantiated any number of times, in any module, and have a number of properties to customize their appearance and behavior. A well-designed module builds its GUI from these reusable widgets (and maybe a few node selectors and buttons).</p>

---
