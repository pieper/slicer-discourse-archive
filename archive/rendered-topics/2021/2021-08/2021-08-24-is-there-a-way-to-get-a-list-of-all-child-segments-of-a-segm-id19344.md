---
topic_id: 19344
title: "Is There A Way To Get A List Of All Child Segments Of A Segm"
date: 2021-08-24
url: https://discourse.slicer.org/t/19344
---

# Is there a way to get a list of all child segments of a segmentation programmatically?

**Topic ID**: 19344
**Date**: 2021-08-24
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-get-a-list-of-all-child-segments-of-a-segmentation-programmatically/19344

---

## Post #1 by @akshay_pillai (2021-08-24 17:11 UTC)

<p>How can I get a list of all the segments in a segmentation. For example I have 10 segments in my segmentation. I want a list of these 10 segments so I can use them in my code later on. Is this possible? Is so, how?</p>

---

## Post #2 by @Sunderlandkyl (2021-08-24 17:16 UTC)

<p>If you want a list of segment IDs, you can get them using vtkSegmentation::GetSegmentIDs:</p>
<pre><code class="lang-auto">segmentationNode.GetSegmentation().GetSegmentIDs()
</code></pre>

---

## Post #3 by @akshay_pillai (2021-08-24 17:19 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>  when I enter this in the python interactor in slicer, I get this:<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
TypeError: no overloads of GetSegmentIDs() take 0 arguments</p>

---

## Post #4 by @akshay_pillai (2021-08-24 17:19 UTC)

<p>Also , is there a way to get the names of these segments instead of IDs?</p>

---

## Post #5 by @Sunderlandkyl (2021-08-24 17:33 UTC)

<aside class="quote no-group" data-username="akshay_pillai" data-post="3" data-topic="19344" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akshay_pillai/48/8301_2.png" class="avatar"> akshay_pillai:</div>
<blockquote>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> when I enter this in the python interactor in slicer, I get this:<br>
Traceback (most recent call last):<br>
File “”, line 1, in<br>
TypeError: no overloads of GetSegmentIDs() take 0 arguments</p>
</blockquote>
</aside>
<p>What version of Slicer are you using? This works in latest version (as of 20 days ago). Othewise, you can pass a vtkStringArray as an argument.</p>
<aside class="quote no-group" data-username="akshay_pillai" data-post="4" data-topic="19344" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akshay_pillai/48/8301_2.png" class="avatar"> akshay_pillai:</div>
<blockquote>
<p>Also , is there a way to get the names of these segments instead of IDs?</p>
</blockquote>
</aside>
<p>If you are tracking the list of segments for later use, it is better to use segment IDs as the IDs shouldn’t change.</p>
<p>You can get the name of a segment using vtkSegment::GetName():</p>
<pre><code class="lang-auto">for segmentID in segmentIDs:
  segmentationNode.GetSegmentation().GetSegment(segmentID).GetName()
</code></pre>
<p>or</p>
<pre><code class="lang-auto">for i in range(segmentationNode.GetSegmentation().GetNumberOfSegments()):
  segmentationNode.GetSegmentation().GetNthSegment(i).GetName()
</code></pre>

---

## Post #6 by @akshay_pillai (2021-08-24 17:45 UTC)

<p>I’m using slicer 4.11.20200930</p>

---

## Post #7 by @apparrilla (2021-09-02 20:36 UTC)

<p>Hi <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> .<br>
I have same problem. I´ve passed and vtkStringArray as argument but it shouldn´t looks to be iterable</p>
<p>Error msg:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a111edeebd5a357bd3ad3cc65be4324f242ed80f.png" data-download-href="/uploads/short-url/mYThKKJlM6oLjLwgoHNconTyykL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a111edeebd5a357bd3ad3cc65be4324f242ed80f.png" alt="image" data-base62-sha1="mYThKKJlM6oLjLwgoHNconTyykL" width="690" height="42" data-dominant-color="282020"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1193×74 3.48 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Maybe I´m doing something wrong…</p>
<p>Thanks on advance!</p>

---

## Post #8 by @Sunderlandkyl (2021-09-03 00:00 UTC)

<p>You can iterate through a vtkStringArray like this:</p>
<pre><code class="lang-auto">for i in range(segmentIDs.GetNumberOfValues()):
  segmentID = segmentIDs.GetValue(i)
</code></pre>

---
