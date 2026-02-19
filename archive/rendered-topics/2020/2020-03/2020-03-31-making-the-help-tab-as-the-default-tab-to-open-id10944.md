---
topic_id: 10944
title: "Making The Help Tab As The Default Tab To Open"
date: 2020-03-31
url: https://discourse.slicer.org/t/10944
---

# Making the 'Help' tab as the default tab to open

**Topic ID**: 10944
**Date**: 2020-03-31
**URL**: https://discourse.slicer.org/t/making-the-help-tab-as-the-default-tab-to-open/10944

---

## Post #1 by @muratmaga (2020-03-31 20:03 UTC)

<p>I have this strange issue. I need the Help section of the ‘Help and Acknowledgement’ tab to be the default tab to show.  I can manually click the help, but when I open a new slicer, this always goes back displaying Acknowledgement tab.</p>
<p>Is there a persistent setting to modify this behavior?</p>

---

## Post #2 by @pieper (2020-03-31 20:25 UTC)

<p>There’s no current persistent setting for this, at least not that I know of.  But it would be easy enough to set in a .slicerrc.py.</p>
<p>This should do it:</p>
<pre><code class="lang-auto">findChildren(name="HelpAcknowledgementTabWidget")[0].currentIndex = 0
</code></pre>

---

## Post #3 by @lassoan (2020-03-31 20:53 UTC)

<p>I think it would be better to always make the Help tab the default. Acknowledgement information is much less frequently needed. Probably it was the original intent, too, because Help is the first tab and Acknowledgement is the second tab.</p>

---

## Post #4 by @muratmaga (2020-03-31 21:03 UTC)

<p>I agree that this should be default behavior.</p>

---

## Post #5 by @pieper (2020-04-01 00:42 UTC)

<p>Yes, that would be an easy change.</p>
<p>It’s here if anyone wants to take it on:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/47deb76d7556e40de4e25e585c4b24a63a153da5/Base/QTGUI/Resources/UI/qSlicerModulePanel.ui#L89" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/47deb76d7556e40de4e25e585c4b24a63a153da5/Base/QTGUI/Resources/UI/qSlicerModulePanel.ui#L89" target="_blank">Slicer/Slicer/blob/47deb76d7556e40de4e25e585c4b24a63a153da5/Base/QTGUI/Resources/UI/qSlicerModulePanel.ui#L89</a></h4>
<pre class="onebox"><code class="lang-ui"><ol class="start lines" start="79" style="counter-reset: li-counter 78 ;">
<li>&lt;property name="collapsed"&gt;</li>
<li> &lt;bool&gt;true&lt;/bool&gt;</li>
<li>&lt;/property&gt;</li>
<li>&lt;property name="contentsFrameShape"&gt;</li>
<li> &lt;enum&gt;QFrame::StyledPanel&lt;/enum&gt;</li>
<li>&lt;/property&gt;</li>
<li>&lt;layout class="QVBoxLayout" name="verticalLayout_3"&gt;</li>
<li> &lt;item&gt;</li>
<li>  &lt;widget class="QTabWidget" name="HelpAcknowledgementTabWidget"&gt;</li>
<li>   &lt;property name="currentIndex"&gt;</li>
<li class="selected">    &lt;number&gt;1&lt;/number&gt;</li>
<li>   &lt;/property&gt;</li>
<li>   &lt;widget class="QWidget" name="HelpTab"&gt;</li>
<li>    &lt;attribute name="title"&gt;</li>
<li>     &lt;string&gt;Help&lt;/string&gt;</li>
<li>    &lt;/attribute&gt;</li>
<li>    &lt;layout class="QVBoxLayout" name="verticalLayout"&gt;</li>
<li>     &lt;property name="margin"&gt;</li>
<li>      &lt;number&gt;0&lt;/number&gt;</li>
<li>     &lt;/property&gt;</li>
<li>     &lt;item&gt;</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @jamesobutler (2020-04-03 05:10 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="10944">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>It’s here if anyone wants to take it on:</p>
</blockquote>
</aside>
<p>Here you go <a href="https://github.com/Slicer/Slicer/pull/4804" class="inline-onebox" rel="noopener nofollow ugc">ENH: Set Help tab as the default instead of Acknowledgement by jamesobutler · Pull Request #4804 · Slicer/Slicer · GitHub</a>. I co-authored you <a class="mention" href="/u/pieper">@pieper</a>!</p>

---
