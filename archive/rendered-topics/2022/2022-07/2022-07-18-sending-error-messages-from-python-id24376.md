---
topic_id: 24376
title: "Sending Error Messages From Python"
date: 2022-07-18
url: https://discourse.slicer.org/t/24376
---

# Sending error messages from python

**Topic ID**: 24376
**Date**: 2022-07-18
**URL**: https://discourse.slicer.org/t/sending-error-messages-from-python/24376

---

## Post #1 by @keri (2022-07-18 18:09 UTC)

<p>Hi,</p>
<p>As I can see there are at least two ways of sending errors from scripted modules:</p>
<ul>
<li>logging.error()</li>
<li>qt.qCritical()</li>
</ul>
<p>Which is the preferred one?</p>
<p>Also does Slicer write logs somewhere in the text file? For example if my app crash I would like to see the logs.</p>

---

## Post #2 by @jcfr (2022-07-18 19:20 UTC)

<p>From python, you should use the <code>logging</code> module.</p>
<p>Consider reading these sections:</p>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/style_guide.html?highlight=logging#logging">Style Guide / Logging</a></li>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/style_guide.html#error-and-warning-messages">Style Guide / Error and warning messages</a></li>
</ul>

---

## Post #3 by @keri (2022-07-18 20:35 UTC)

<p>Just to clarify, does Slicer somehow write logs to file?</p>

---

## Post #4 by @jcfr (2022-07-18 20:56 UTC)

<aside class="quote no-group" data-username="keri" data-post="3" data-topic="24376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>somehow write logs to file?</p>
</blockquote>
</aside>
<p>It does, see <code>Log outputs</code> link referenced in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#id1">User Guide</a></p>

---

## Post #5 by @keri (2022-07-18 21:01 UTC)

<p>Thank you very much!</p>

---
