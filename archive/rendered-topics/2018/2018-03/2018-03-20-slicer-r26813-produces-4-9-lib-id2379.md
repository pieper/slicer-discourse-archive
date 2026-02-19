---
topic_id: 2379
title: "Slicer R26813 Produces 4 9 Lib"
date: 2018-03-20
url: https://discourse.slicer.org/t/2379
---

# Slicer -r26813 produces 4.9 lib

**Topic ID**: 2379
**Date**: 2018-03-20
**URL**: https://discourse.slicer.org/t/slicer-r26813-produces-4-9-lib/2379

---

## Post #1 by @brhoom (2018-03-20 18:22 UTC)

<p>Operating system:Ubuntu<br>
Slicer version:4.8.1<br>
Expected behavior: it should produce 4.8<br>
Actual behavior: 4.9 is produced</p>
<p>I used 26813 which is the source of the stable version 4.8.1</p>
<pre><code>   Checked out revision 26813.
</code></pre>
<p>I just noticed that my Slicer-build/lib  has a folder Slicer-4.9 instead of Slicer-4.8</p>
<p>Did I do something wrong or this is normal?</p>

---

## Post #2 by @lassoan (2018-03-20 19:13 UTC)

<p>SVN revision does not identify the branch (trunk or 4.8). To get source code of Slicer-4.8, switch to <a href="http://svn.slicer.org/Slicer4/branches/Slicer-4-8">http://svn.slicer.org/Slicer4/branches/Slicer-4-8</a>.</p>

---

## Post #3 by @brhoom (2018-03-20 19:29 UTC)

<p>thanks, i was following the instructions <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">here</a> so probably it needs an update?</p>
<pre><code> svn co http://svn.slicer.org/Slicer4/branches/Slicer-4-8 src
 Checked out revision 27089.
</code></pre>
<p>Notice that the revision is not the same as in the link above</p>

---

## Post #4 by @jcfr (2018-03-20 19:54 UTC)

<p>Thanks for the feedback. The page has been updated to clarify:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/CheckoutSourceCode#CHECKOUT_slicer_source_files" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/CheckoutSourceCode#CHECKOUT_slicer_source_files</a></p>
<p>Let us know what you think</p>

---

## Post #5 by @brhoom (2018-03-20 20:17 UTC)

<p>I am still confused.  Which one is correct for the 4.8.1 option a or option b? or they are the same?</p>
<p>option a:</p>
<pre><code>   svn co http://svn.slicer.org/Slicer4/trunk src -r 26813
   Checked out revision 26813.
</code></pre>
<p>option b:</p>
<pre><code>  svn co http://svn.slicer.org/Slicer4/branches/Slicer-4-8 src
  Checked out revision 27089.
</code></pre>
<p>I tried option a but the lib was 4.9 after build. Option b produces the correct lib 4.8 but I see the revision is different.</p>

---

## Post #6 by @jcfr (2018-03-20 20:44 UTC)

<p>Thanks for your patience.</p>
<p>The page has been updated to describe both the <em>marker</em> and the <em>svn revision</em>. Now it should make more sense.</p>
<pre><code class="lang-nohighlight">svn co http://svn.slicer.org/Slicer4/&lt;MARKER&gt; Slicer-r&lt;SVNREVISION&gt; -r &lt;SVNREVISION&gt;
</code></pre>

---

## Post #7 by @brhoom (2018-03-22 11:49 UTC)

<p>Thanks for the effort.  I used</p>
<pre><code>svn co http://svn.slicer.org/Slicer4/branches/Slicer-4-8 Slicer-r26813 -r 26813
</code></pre>
<p>After build using this source I found</p>
<pre><code>Slicer-build/lib/Slicer-4.9
</code></pre>
<p>Why I don’t get theSlicer-4.8?</p>

---

## Post #8 by @jcfr (2018-03-22 11:56 UTC)

<p>You have to make sure to do a clean build or explicitly set the version variables:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master-48/CMakeLists.txt#L45-L54" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master-48/CMakeLists.txt#L45-L54" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master-48/CMakeLists.txt#L45-L54</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="45" style="counter-reset: li-counter 44 ;">
<li>if(NOT DEFINED Slicer_VERSION_MAJOR)</li>
<li>set(Slicer_VERSION_MAJOR "4")</li>
<li>endif()</li>
<li>if(NOT DEFINED Slicer_VERSION_MINOR)</li>
<li>set(Slicer_VERSION_MINOR "8")</li>
<li>endif()</li>
<li>if(NOT DEFINED Slicer_VERSION_PATCH)</li>
<li>set(Slicer_VERSION_PATCH "1")</li>
<li>endif()</li>
<li>project(Slicer VERSION "${Slicer_VERSION_MAJOR}.${Slicer_VERSION_MINOR}.${Slicer_VERSION_PATCH}")</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Failing to do so, the module would be  generated in <code>lib/Slicer-4.9</code>.</p>
<p>Now, in the context of your local build, may be it doesn’t really matter.</p>

---

## Post #9 by @brhoom (2018-03-22 14:19 UTC)

<p>it works now, thanks again.</p>

---
