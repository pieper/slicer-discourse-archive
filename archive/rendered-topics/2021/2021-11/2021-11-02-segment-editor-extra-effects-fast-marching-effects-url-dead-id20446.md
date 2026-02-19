---
topic_id: 20446
title: "Segment Editor Extra Effects Fast Marching Effects Url Dead"
date: 2021-11-02
url: https://discourse.slicer.org/t/20446
---

# Segment Editor : Extra Effects — Fast Marching effect's URL dead

**Topic ID**: 20446
**Date**: 2021-11-02
**URL**: https://discourse.slicer.org/t/segment-editor-extra-effects-fast-marching-effects-url-dead/20446

---

## Post #1 by @DIV (2021-11-02 01:55 UTC)

<p>The <em>Fast Marching</em> (extra) effect in the <strong>Segment Editor</strong> module has a link to<br>
<code>http://www.spl.harvard.edu/publications/item/view/193</code><br>
embedded as “The effect uses <a href="http://www.spl.harvard.edu/publications/item/view/193" rel="noopener nofollow ugc">fast marching method</a>”, but the link seems to be dead.<br>
Browsing<br>
<a href="https://web.archive.org/web/20160731173233/http://www.spl.harvard.edu/publications/pages/display/?entriesPerPage=50&amp;collection=1" class="onebox" target="_blank" rel="noopener nofollow ugc">https://web.archive.org/web/20160731173233/http://www.spl.harvard.edu/publications/pages/display/?entriesPerPage=50&amp;collection=1</a><br>
I couldn’t figure out where it was supposed to link to.<br>
—DIV</p>

---

## Post #2 by @jamesobutler (2021-11-02 03:47 UTC)

<aside class="quote" data-post="10" data-topic="12848">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/issues-with-website-links-and-webmaster-email-address/12848/10">Issues with website links and webmaster email address</a> <a class="badge-category__wrapper " href="/c/forum-feedback/10"><span data-category-id="10" style="--category-badge-color: #B3B5B4; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="Discussion about this site, its organization, how it works, and how we can improve it."><span class="badge-category__name">Forum and website feedback</span></span></a>
  </div>
  <blockquote>
    I heard we’re still stuck waiting for physical presence on site before the publication server can come back. 
I think google scholar would be a good option.
  </blockquote>
</aside>

<p><a class="mention" href="/u/pieper">@pieper</a> Is the publication server at spl going to come online again? If not, I suppose we replace all links to it including those that might be in Slicer extensions.</p>
<p>Dead link in question is located at:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/e540feb6f01049a0a4311ca1da73e9a09017c804/SegmentEditorFastMarching/SegmentEditorFastMarchingLib/SegmentEditorEffect.py#L36">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/e540feb6f01049a0a4311ca1da73e9a09017c804/SegmentEditorFastMarching/SegmentEditorFastMarchingLib/SegmentEditorEffect.py#L36" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/e540feb6f01049a0a4311ca1da73e9a09017c804/SegmentEditorFastMarching/SegmentEditorFastMarchingLib/SegmentEditorEffect.py#L36" target="_blank" rel="noopener nofollow ugc">lassoan/SlicerSegmentEditorExtraEffects/blob/e540feb6f01049a0a4311ca1da73e9a09017c804/SegmentEditorFastMarching/SegmentEditorFastMarchingLib/SegmentEditorEffect.py#L36</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="26" style="counter-reset: li-counter 25 ;">
          <li>  def icon(self):
</li>
          <li>    # It should not be necessary to modify this method
</li>
          <li>    iconPath = os.path.join(os.path.dirname(__file__), 'SegmentEditorEffect.png')
</li>
          <li>    if os.path.exists(iconPath):
</li>
          <li>      return qt.QIcon(iconPath)
</li>
          <li>    return qt.QIcon()
</li>
          <li>
</li>
          <li>  def helpText(self):
</li>
          <li>    return """&lt;html&gt;Expand the selected segment&lt;br&gt; to regions that have similar intensity.&lt;p&gt;
</li>
          <li>Only the selected segment is expanded. No background segment is needed.
</li>
          <li class="selected">The effect uses &lt;a href="http://www.spl.harvard.edu/publications/item/view/193"&gt;fast marching method&lt;/a&gt;.
</li>
          <li>&lt;p&gt;&lt;/html&gt;"""
</li>
          <li>
</li>
          <li>  def setupOptionsFrame(self):
</li>
          <li>
</li>
          <li>    self.percentMax = ctk.ctkSliderWidget()
</li>
          <li>    self.percentMax.minimum = 0
</li>
          <li>    self.percentMax.maximum = 100
</li>
          <li>    self.percentMax.singleStep = 1
</li>
          <li>    self.percentMax.value = 10
</li>
          <li>    self.percentMax.suffix = '%'
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @pieper (2021-11-02 13:59 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="20446">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> Is the publication server at spl going to come online again?</p>
</blockquote>
</aside>
<p>At this point it’s probably better to assume it’s not coming back and we should make other plans.</p>

---

## Post #4 by @lassoan (2021-11-02 20:31 UTC)

<p>Could we upload all the papers in a github repository as release assets?</p>

---

## Post #5 by @pieper (2021-11-02 21:54 UTC)

<p>I’m checking.  I don’t know if the machine died with no backup or if it’s just not set up.</p>

---
