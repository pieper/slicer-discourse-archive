---
topic_id: 33865
title: "Qt Warning Message When I Use Python Console"
date: 2024-01-19
url: https://discourse.slicer.org/t/33865
---

# Qt warning message when I use python console

**Topic ID**: 33865
**Date**: 2024-01-19
**URL**: https://discourse.slicer.org/t/qt-warning-message-when-i-use-python-console/33865

---

## Post #1 by @park (2024-01-19 07:28 UTC)

<p>Hi all</p>
<p>I built Slicer 5.7 as a debug version and loaded a script extension modules using the extension wizard. Since then, I have been consistently getting the following warning messages. Due to this I cannot use the Python console.</p>
<p><code>"Using QCharRef with an index pointing outside the valid range of a QString. The corresponding behavior is deprecated, and will be changed in a future version of Qt."</code></p>
<p>These warning messages only appear in the build version and not in the Slicer binary. Any idea what might be causing this?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88362e7af293c801d91743f95a65c935f068fe5e.png" alt="캡처" data-base62-sha1="jqZ1cKqcG4U42fFHUGIIye4nXK6" width="516" height="349"></p>

---

## Post #2 by @pieper (2024-01-19 13:44 UTC)

<p>I’ve never seen that particular message.  Since you built from source you should be able to set a breakpoint where the warning is printed and inspect the stack trace to see if this comes from specific c++ code.</p>

---

## Post #3 by @jcfr (2024-01-20 11:04 UTC)

<p>Warning seems to reported by  code in <code>QByteArray</code>… See <a href="https://github.com/qt/qtbase/blob/v5.15.2/src/corelib/text/qbytearray.cpp#L5134-L5142" class="inline-onebox">qtbase/src/corelib/text/qbytearray.cpp at v5.15.2 · qt/qtbase · GitHub</a></p>
<p><a class="mention" href="/u/park">@park</a> Would it be possible to share the exact steps leading to these warning messages ?  Does it happen without the generated script extension loaded ?</p>

---

## Post #4 by @park (2024-01-22 02:15 UTC)

<p>Ironically, this warning message appeared because of “Grammarly”. It seems that Grammarly’s spelling check feature keeps activating the python interactor.</p>
<p>Thank you for your consideration !</p>

---

## Post #5 by @jcfr (2024-01-22 18:16 UTC)

<p>This seems consistent with these Grammarly related comments<sup class="footnote-ref"><a href="#footnote-105830-1" id="footnote-ref-105830-1">[1]</a></sup> I found:</p>
<blockquote>
<blockquote>
<p>Is the grammarly desktop app interacting with browser elements without using the extension? (IIRC the grammarly app uses some accessibility privileges to inject into textareas across all apps)</p>
</blockquote>
<p>It seems like that must be the case. If we have the details right about desktop app only (which seemed pretty clear).</p>
</blockquote>
<p>I am wondering if there is way to “hint” Grammarly and avoid this.</p>
<p>What about having someone from our community  with a paid account reach out and ask the  Grammarly support team ?</p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-105830-1" class="footnote-item"><p><a href="https://news.ycombinator.com/item?id=38477100" class="inline-onebox">The weirdest bug I've seen yet | Hacker News</a> <a href="#footnote-ref-105830-1" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---
