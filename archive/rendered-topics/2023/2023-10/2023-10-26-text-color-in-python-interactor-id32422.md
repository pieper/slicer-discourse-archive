---
topic_id: 32422
title: "Text Color In Python Interactor"
date: 2023-10-26
url: https://discourse.slicer.org/t/32422
---

# Text color in python interactor

**Topic ID**: 32422
**Date**: 2023-10-26
**URL**: https://discourse.slicer.org/t/text-color-in-python-interactor/32422

---

## Post #1 by @bserrano (2023-10-26 08:15 UTC)

<p>Hi all,</p>
<p>How can I print text in the python interactor in different colors?</p>

---

## Post #2 by @lassoan (2023-10-26 12:30 UTC)

<p>Colors are reserved for distinguishing different types of messages (info, warning, error, console input/output). What would you like to achieve?</p>

---

## Post #3 by @bserrano (2023-10-26 14:18 UTC)

<p>That’s exactly what I want. When running the code, I want to notify the user or print error messages, but I would like to do so in a different color.</p>

---

## Post #4 by @cpinter (2023-10-26 14:32 UTC)

<p>You can use</p>
<pre><code class="lang-auto">import logging
logging.info('All OK')
logging.warning('Something is wrong')
logging.error('Even worse')
</code></pre>

---

## Post #5 by @bserrano (2023-10-27 06:52 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="32422">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<pre><code class="lang-auto">import logging
logging.info('All OK')
logging.warning('Something is wrong')
logging.error('Even worse')
</code></pre>
</blockquote>
</aside>
<p>Thanks. Still not working as expected:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2ddcc11c13b1d8e72b60ccfe35c0a0f33ac93458.png" alt="imagen" data-base62-sha1="6xIrUnzHTLEHf5iSUFdCoD5Vqu4" width="334" height="136"></p>
<p>So I guess that it is not possible to print text in a random color.</p>

---
