---
topic_id: 7166
title: "Python Interactor Disconnecting"
date: 2019-06-13
url: https://discourse.slicer.org/t/7166
---

# Python interactor disconnecting

**Topic ID**: 7166
**Date**: 2019-06-13
**URL**: https://discourse.slicer.org/t/python-interactor-disconnecting/7166

---

## Post #1 by @pieper (2019-06-13 21:19 UTC)

<p>I’ve noticed that sometimes lately the python interactor will stop processing new commands.  This is something new in the past few weeks.  It seems to happen when there’s a background exception.  <a class="mention" href="/u/lassoan">@lassoan</a> the other day on the developer hangout it sounded like you’d seen this before too, but we didn’t have time to talk.  Do you know why it’s happening?</p>

---

## Post #2 by @lassoan (2019-06-13 21:48 UTC)

<p>I don’t remember ever experiencing this.</p>

---

## Post #3 by @jcfr (2019-06-13 23:22 UTC)

<p>I confirm I experienced similar problem. I will report an issue with exact step.</p>

---

## Post #4 by @pieper (2019-06-13 23:50 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a> - I’ve had it happen a couple times.  In case it helps, today I was able to track it down to an exception being thrown in an imported library.  Nothing showed up on the Slicer console, but when I ran the same code in an external python process the exception showed up.</p>

---

## Post #5 by @jamesobutler (2019-06-28 16:41 UTC)

<p>I was also able to make the python interactor stop processing events correctly in Slicer nightly. Was there ever a bug/fix issued regarding the previous cases of the interactor not processing?</p>
<p>Typed into interactor: a= “Ì”<br>
Ì = windows alt code 0204</p>
<p><strong>Slicer 4.10.2</strong></p>
<pre><code class="lang-auto">Python console user input: a="?"
Python console user input: a
'\xec'
Python console user input: print("Hello")
Hello
</code></pre>
<p><strong>Slicer 4.11 nightly</strong></p>
<pre><code class="lang-auto">Python console user input: a="?"
Python console user input: a
Python console user input: print("Hello")
Python console user input: slicer.app.settingsDialog().show()
  File "&lt;console&gt;", line 1
    a
    ^
SyntaxError: multiple statements found while compiling a single statement
</code></pre>

---

## Post #6 by @lassoan (2019-06-30 02:52 UTC)

<p>This special character problem is caused by an incorrect Latin1 encoding of the user input in this line:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/CTK/blob/a18ece7db314a6f638db747ca8d05cc6f5c41bb3/Libs/Scripting/Python/Widgets/ctkPythonConsole.cpp#L506" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/a18ece7db314a6f638db747ca8d05cc6f5c41bb3/Libs/Scripting/Python/Widgets/ctkPythonConsole.cpp#L506" target="_blank" rel="nofollow noopener">commontk/CTK/blob/a18ece7db314a6f638db747ca8d05cc6f5c41bb3/Libs/Scripting/Python/Widgets/ctkPythonConsole.cpp#L506</a></h4>
<pre class="onebox"><code class="lang-cpp"><ol class="start lines" start="496" style="counter-reset: li-counter 495 ;">
<li>bool ret_value = false;</li>
<li>
</li>
<li>QString buffer = code;</li>
<li>// The embedded python interpreter cannot handle DOS line-endings, see</li>
<li>// http://sourceforge.net/tracker/?group_id=5470&amp;atid=105470&amp;func=detail&amp;aid=1167922</li>
<li>buffer.remove('\r');</li>
<li>
</li>
<li>PyObject *res = PyObject_CallMethod(this-&gt;InteractiveConsole,</li>
<li>                                    const_cast&lt;char*&gt;("push"),</li>
<li>                                    const_cast&lt;char*&gt;("z"),</li>
<li class="selected">                                    buffer.toLatin1().data());</li>
<li>if (res)</li>
<li>  {</li>
<li>  int status = 0;</li>
<li>  if (PyArg_Parse(res, "i", &amp;status))</li>
<li>    {</li>
<li>    ret_value = (status &gt; 0);</li>
<li>    }</li>
<li>  Py_DECREF(res);</li>
<li>  }</li>
<li>return ret_value;</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Changing <code>buffer.toLatin1().data()</code> to <code>buffer.toUtf8().data()</code> fixes the issue.</p>
<p>This change would need to be tested with Python2 and other <code>toLatin1</code> calls would need to be reviewed and potentially changed to <code>toUtf8</code> in the CTK Python console.</p>
<p>I won’t be able to investigate this any further. <a class="mention" href="/u/jamesobutler">@jamesobutler</a> would you have time to look into this?</p>

---

## Post #7 by @jamesobutler (2019-06-30 20:38 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I can confirm the change to <code>buffer.toUtf8().data()</code> does fix the issue for the Slicer nightly:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; a="Ì"
&gt;&gt;&gt; a
'Ì'
&gt;&gt;&gt; print(a)
Ì
</code></pre>
<p>The same change for Slicer 4.10 which uses Python2 unfortunately results in a different output compared to what it currently shows. So this code change doesn’t seem to be appropriate for both python 2 and 3:<br>
<strong>Unmodified Slicer 4.10:</strong></p>
<pre><code class="lang-auto">&gt;&gt;&gt; a="Ì"
&gt;&gt;&gt; a
'\xcc'
&gt;&gt;&gt; print(a)
Ì
</code></pre>
<p><strong>Modified Slicer 4.10:</strong></p>
<pre><code class="lang-auto">&gt;&gt;&gt; a="Ì"
&gt;&gt;&gt; a
'\xc3\x8c'
&gt;&gt;&gt; print(a)
Ã
</code></pre>

---

## Post #8 by @jcfr (2019-07-01 17:28 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a>  Thanks for testing.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="7166">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>ever a bug/fix issued regarding the previous cases of the interactor not processing?</p>
</blockquote>
</aside>
<p>I didn’t get to report an issue. That said, based on the recent updates discussed here, the following PR will be integrated to CTK and Slicer will be updated accordingly: <a href="https://github.com/commontk/CTK/pull/872" class="inline-onebox">BUG: Update ctkPythonConsole to support auto-completion including unicode characters by jcfr · Pull Request #872 · commontk/CTK · GitHub</a></p>

---

## Post #9 by @jcfr (2019-07-01 17:41 UTC)

<p>Corresponding changes have been integrated in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28353" rel="nofollow noopener">r28353</a></p>

---
