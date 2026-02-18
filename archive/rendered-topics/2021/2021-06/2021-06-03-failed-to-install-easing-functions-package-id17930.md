# Failed to install easing-functions package

**Topic ID**: 17930
**Date**: 2021-06-03
**URL**: https://discourse.slicer.org/t/failed-to-install-easing-functions-package/17930

---

## Post #1 by @slicer365 (2021-06-03 04:23 UTC)

<p>I want to use the explode models function in the animationSlicerMorph,but I need to install the easing-functions package. this picuture means no response！Is there any other way to install the package?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68673f4a5a8a9a493663647fa18277040b5302c3.png" alt="无标题" data-base62-sha1="eTARvJgb3nqPmvYPLm4drqvSQIb" width="522" height="315"></p>

---

## Post #2 by @muratmaga (2021-06-03 08:50 UTC)

<p>Normally it should install automatically. What do you get when you type</p>
<blockquote>
<p>import easing_functions</p>
</blockquote>
<p>into the python console.<br>
Did you try</p>
<blockquote>
<p>pip_install(‘easing_functions’)</p>
</blockquote>

---

## Post #3 by @slicer365 (2021-06-03 10:38 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b540a761c80e0e909d79631561cf4d660695eec6.jpeg" alt="捕获" data-base62-sha1="pRqWqpII0jy6nrhT7lVYAnGVZwq" width="546" height="224"></p>
<p>Thank you  for your answer,yeah,it should install automatically.however，when I click OK，the  whole software will pause，no responce for long time.The other ways don’t work.</p>

---

## Post #4 by @muratmaga (2021-06-03 10:49 UTC)

<p>Seems like auto-formatting changed the closing (’) apostrophe, it is not the same character as the opening one (hence the syntax error). Please try again with quotation mark ("")<br>
pip_install(“easing-functions”)</p>

---

## Post #5 by @muratmaga (2021-06-03 10:51 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, actually I think the discourse is the culprit here. I type double quotes appear correct as I type here “” (i.e., both identical). But in preview they change to different characters (an opening and a closing one).<br>
I find this behavior very annoying where we exchange code snippets. Can it be disabled? I don’t recall this before…</p>

---

## Post #6 by @slicer365 (2021-06-03 10:56 UTC)

<p>Oh,my God，yes,your are right!<br>
thank you very much！ <img src="https://emoji.discourse-cdn.com/twitter/100.png?v=12" title=":100:" class="emoji" alt=":100:" loading="lazy" width="20" height="20"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4fdde43fb301d5e0b6818bb3167c07a478f1660.jpeg" alt="捕获" data-base62-sha1="wFKLX2XRB9NwIWQ5JOQKvZYErT2" width="594" height="85"></p>

---

## Post #7 by @lassoan (2021-06-03 12:31 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="17930">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>actually I think the discourse is the culprit here. I type double quotes appear correct as I type here “” (i.e., both identical). But in preview they change to different characters (an opening and a closing one).</p>
</blockquote>
</aside>
<p>It is not discourse’s fault. Outlook, word, latex, etc. will all convert your quotes if you don’t indicate that it is preformatted/code/verbatim text. You just need to learn the syntax. Fortunately, discourse uses markdown, which is now the standard that is used everywhere to specify formatting in plan text. You only need to learn this once and then can include code snippets correctly almost everywhere.</p>
<h2><a name="p-60531-code-text-inline-1" class="anchor" href="#p-60531-code-text-inline-1" aria-label="Heading link"></a>Code text inline</h2>
<p><strong>Plain text input:</strong></p>
<p><code>Use backtick for entering `code (note the "quotes") text`. These are "quotes" outside.</code></p>
<p><strong>Rendering:</strong></p>
<p>Use backtick for entering <code>code (note the "quotes") text</code>. These are “quotes” outside.</p>
<h2><a name="p-60531-code-block-2" class="anchor" href="#p-60531-code-block-2" aria-label="Heading link"></a>Code block</h2>
<p><strong>Plain text input:</strong></p>
<pre><code class="lang-plaintext">Use triple-backtick for code blocks:

```python
# Specify the language (Python, console, cpp,...) for syntax highlighting.
pip_install('easing_functions')
```
</code></pre>
<p><strong>Rendering:</strong></p>
<p>Use triple-backtick for code blocks:</p>
<pre data-code-wrap="python"><code class="lang-python"># Specify the language (Python, console, cpp,...) for syntax highlighting.
pip_install('easing_functions')
</code></pre>
<hr>
<p>Note that blockquote (that is used for quoting formatted text by prepending <code>&gt;</code>) has similar gray shading behind the text, but it is not for verbatim formatting.</p>

---
