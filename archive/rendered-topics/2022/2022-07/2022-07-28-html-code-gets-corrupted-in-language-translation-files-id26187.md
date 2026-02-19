---
topic_id: 26187
title: "Html Code Gets Corrupted In Language Translation Files"
date: 2022-07-28
url: https://discourse.slicer.org/t/26187
---

# HTML code gets corrupted in language translation files

**Topic ID**: 26187
**Date**: 2022-07-28
**URL**: https://discourse.slicer.org/t/html-code-gets-corrupted-in-language-translation-files/26187

---

## Post #1 by @Aki (2022-07-28 11:51 UTC)

<p>hello, lassoan,</p>
<p>I have completed the translation of the strings for Japanese.<br>
But, I found that some HTML tags disappear after saving the translation.<br>
Some strings including HTML tags, and the tags and parameter values in tags disappear, in particular,</p>
<pre><code class="lang-auto">&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name="qrichtext" content="1" /&gt;&lt;style type="text/css"&gt;
</code></pre>
<p>is changed to</p>
<pre><code class="lang-auto">
&amp;lt;html&amp;gt;&lt;meta name="qrichtext" content="1"&gt;&lt;style type="text/css"&gt;
</code></pre>
<p>Also, some style strings are changed, like</p>
<pre><code class="lang-auto">&lt;/span&gt;&lt;span style=" font-size:8pt; font-weight:600;"&gt;
</code></pre>
<p>to</p>
<pre><code class="lang-auto">&lt;/span&gt;&lt;span style=""&gt;
</code></pre>
<p>If you have a solution for this, please let me know.<br>
Thanks.</p>

---

## Post #2 by @DDinghoya (2022-09-07 02:30 UTC)

<p>I agree. The same is true for Korean.</p>
<p>In my opinion, it seems to occur only for characters using a 2-byte character set.</p>
<p>Also, in the case of Korean, 100% translation was performed on Weblate, but translation was not applied in some surrenders.</p>

---

## Post #3 by @lassoan (2022-11-10 18:27 UTC)

<p>We enabled in Weblate to have HTML code in translation files, so text corruption should not occur anymore. The existing messages should be fixed up as explained in <a href="https://github.com/Slicer/SlicerLanguagePacks/issues/14" class="inline-onebox">HTML tags and special characters get corrupted · Issue #14 · Slicer/SlicerLanguagePacks · GitHub</a>.</p>
<p>Going forward, we’ll try to avoid using HTML formatting in translatable text, by adding formatting outside the translatable strings wherever it is possible.</p>

---

## Post #4 by @Aki (2022-11-15 09:46 UTC)

<p>Thanks, Lassoan</p>
<p>I checked the Japanese translation on Weblate.  I have done the replacement of the &lt; &gt; and so on to the original charactors and copying the html tags which are included in the origianl English strings to the translated strings.</p>
<p>Aki</p>

---
