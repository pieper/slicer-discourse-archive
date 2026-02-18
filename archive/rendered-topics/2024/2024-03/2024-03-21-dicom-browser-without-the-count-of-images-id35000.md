# DICOM browser without the count of images

**Topic ID**: 35000
**Date**: 2024-03-21
**URL**: https://discourse.slicer.org/t/dicom-browser-without-the-count-of-images/35000

---

## Post #1 by @slicer365 (2024-03-21 08:07 UTC)

<p>In the new version,DICOM browser does not show the count of images in a series.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b4cbae4e2bf7056570098da2db8c9e46cb3ec39.png" data-download-href="/uploads/short-url/jSiLegOIKzqKPA6CFPMwgRqIPIB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b4cbae4e2bf7056570098da2db8c9e46cb3ec39_2_517x261.png" alt="image" data-base62-sha1="jSiLegOIKzqKPA6CFPMwgRqIPIB" width="517" height="261" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b4cbae4e2bf7056570098da2db8c9e46cb3ec39_2_517x261.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b4cbae4e2bf7056570098da2db8c9e46cb3ec39_2_775x391.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b4cbae4e2bf7056570098da2db8c9e46cb3ec39_2_1034x522.png 2x" data-dominant-color="E7EFF4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2006×1012 252 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2024-04-01 11:23 UTC)

<p>This might be due to the recent database update regarding the visual DICOM browser. What happens if you remove all the data from the database (or start a clean database) and import the patients again?</p>

---

## Post #3 by @chir.set (2024-04-01 11:29 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="1" data-topic="35000">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>does not show the count of images in a series</p>
</blockquote>
</aside>
<p>It’s quite <a href="https://discourse.slicer.org/t/dicom-browser-does-not-show-the-count-of-images-in-a-series/33506">old</a>, I guess it’s in the ‘unexplained’ category of event. But it’s good you have highlighted it again.</p>
<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="35000">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>start a clean database</p>
</blockquote>
</aside>
<p>It does not help unfortunately.</p>

---

## Post #4 by @cpinter (2024-04-01 12:08 UTC)

<p>OK thanks! I will try to debug into this when I have a minute (I’m very busy nowadays but will try).</p>

---

## Post #5 by @cpinter (2024-04-02 12:54 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="35000">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>It’s quite <a href="https://discourse.slicer.org/t/dicom-browser-does-not-show-the-count-of-images-in-a-series/33506">old</a></p>
</blockquote>
</aside>
<p>If you take a good look at that thread you’ll see at the bottom that it turned out to be working. Unfortunately I noticed this after wasting a lot of time with looking at older versions. So far my investigation shows that it still worked on Dec 12, 2023 (5.6.1), and it did not work on Jan 15, 2024 (the new visual DICOM browser that I suspected was introduced just after, so it’s not the culprit apparently).</p>
<p>For the attention of developers: I also did some debugging, which shows that the <code>currentSeriesInstanceUid</code> variable (element in <code>this-&gt;UpdatedSeriesInstanceUIDs</code>) is empty string.</p><aside class="onebox githubblob" data-onebox-src="https://github.com/commontk/CTK/blob/fb72e1aa2b143bb942e6c7cdc5603a676884a80a/Libs/DICOM/Core/ctkDICOMDisplayedFieldGeneratorSeriesImageCountRule.cpp#L89">
  <header class="source">

      <a href="https://github.com/commontk/CTK/blob/fb72e1aa2b143bb942e6c7cdc5603a676884a80a/Libs/DICOM/Core/ctkDICOMDisplayedFieldGeneratorSeriesImageCountRule.cpp#L89" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/fb72e1aa2b143bb942e6c7cdc5603a676884a80a/Libs/DICOM/Core/ctkDICOMDisplayedFieldGeneratorSeriesImageCountRule.cpp#L89" target="_blank" rel="noopener">commontk/CTK/blob/fb72e1aa2b143bb942e6c7cdc5603a676884a80a/Libs/DICOM/Core/ctkDICOMDisplayedFieldGeneratorSeriesImageCountRule.cpp#L89</a></h4>



    <pre class="onebox"><code class="lang-cpp">
      <ol class="start lines" start="79" style="counter-reset: li-counter 78 ;">
          <li>  QMap&lt;QString, QMap&lt;QString, QString&gt; &gt; &amp;displayedFieldsMapStudy,</li>
          <li>  QMap&lt;QString, QMap&lt;QString, QString&gt; &gt; &amp;displayedFieldsMapPatient)</li>
          <li>{</li>
          <li>  Q_UNUSED(displayedFieldsMapStudy);</li>
          <li>  Q_UNUSED(displayedFieldsMapPatient);</li>
          <li>  // Update image count for each updated series</li>
          <li>  foreach (QString currentSeriesInstanceUid, this-&gt;UpdatedSeriesInstanceUIDs)</li>
          <li>  {</li>
          <li>    QSqlQuery countQuery(this-&gt;DICOMDatabase-&gt;database());</li>
          <li>    countQuery.prepare("SELECT COUNT(*) FROM Images WHERE SeriesInstanceUID = ? ;");</li>
          <li class="selected">    countQuery.addBindValue(currentSeriesInstanceUid);</li>
          <li>    if (!countQuery.exec())</li>
          <li>    {</li>
          <li>      qCritical() &lt;&lt; Q_FUNC_INFO &lt;&lt; "SQLITE ERROR: " &lt;&lt; countQuery.lastError().driverText();</li>
          <li>      continue;</li>
          <li>    }</li>
          <li></li>
          <li>    countQuery.first();</li>
          <li>    int currentCount = countQuery.value(0).toInt();</li>
          <li></li>
          <li>    QMap&lt;QString, QString&gt; displayedFieldsForCurrentSeries = displayedFieldsMapSeries[currentSeriesInstanceUid];</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
By the way it is not just the image count that is broken, but also the series count on the study level. So it is possible that the display field rules do not get access any more to the updated instance UIDs.</p>
<p>I don’t have more time to work on this, but wanted to disclose my findings so far. I think if we find whick commit broke this instance UID access then we have a good chance of fixing this.</p>

---
