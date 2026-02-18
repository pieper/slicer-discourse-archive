# Flickering when using segmentation effects

**Topic ID**: 10380
**Date**: 2020-02-21
**URL**: https://discourse.slicer.org/t/flickering-when-using-segmentation-effects/10380

---

## Post #1 by @Alex_Vergara (2020-02-21 13:14 UTC)

<p>While the use of segmentation effects in python scripts in slicer works really well, it creates flickering in the Slicer GUI when using full screen mode in mac. Using windowed mode makes no flickering, only full screen mode is the problematic.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6aed616532bdf27e40040cc84a131fee9379ecb2.gif" data-download-href="/uploads/short-url/ffVcdNh6vcV3pg4Q7qh0jHb9EOK.gif?dl=1" title="capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6aed616532bdf27e40040cc84a131fee9379ecb2_2_689x387.gif" alt="capture" data-base62-sha1="ffVcdNh6vcV3pg4Q7qh0jHb9EOK" width="689" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6aed616532bdf27e40040cc84a131fee9379ecb2_2_689x387.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6aed616532bdf27e40040cc84a131fee9379ecb2_2_1033x580.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6aed616532bdf27e40040cc84a131fee9379ecb2_2_1378x774.gif 2x"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture</span><span class="informations">2558×1436 3.99 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-02-21 13:43 UTC)

<p>It sounds interesting, but I don’t see anything on this “video”. Could you please upload a higher-quality screen capture video,upload it somewhere (dropbox, onedrive, youtube, …), and post the link?</p>

---

## Post #3 by @Alex_Vergara (2020-02-21 14:00 UTC)

<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1MegCJzS2fSXPQFSZMOamos5dv4vsYKtW/view?usp=drive_open" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
    
<img src="https://lh4.googleusercontent.com/2AurLSeAe1ZMRTBKrlRl1cxj0ATTD16RaX6wnZaAWm4pd3Ieb6GXxXuTvZtHJ84=w1200-h630-p" class="thumbnail" width="" height="">

<h3><a href="https://drive.google.com/file/d/1MegCJzS2fSXPQFSZMOamos5dv4vsYKtW/view?usp=drive_open" target="_blank" rel="nofollow noopener">capture.gif</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Alex_Vergara (2020-02-21 14:04 UTC)

<p>It is difficult to make the video because the “bug” only happens in full screen mode in MAC.</p>

---

## Post #5 by @hherhold (2020-02-21 14:20 UTC)

<p>Maybe a quick phone video? Flickering artifacts can be hard to capture on the device they’re happening on.</p>

---

## Post #6 by @Alex_Vergara (2020-02-21 14:23 UTC)

<p>I just recorded it with quickTime, then reprocess it to gif with ffmpeg. It was nasty but it worked out of the box.</p>

---

## Post #7 by @lassoan (2020-02-21 14:31 UTC)

<p>Still very bad quality recording. I don’t see any flickering, but just that the image quality of the recording is very bad. Maybe recording with your phone would be better. Replay of animated gifs is also very bad, as it is not easy to navigate the timeline (at least in the viewers that I have). It would also help if you did more things in different modules, just to see if the issue is specific to a particular module or mode.</p>

---

## Post #8 by @Alex_Vergara (2020-02-21 14:47 UTC)

<p>May you recommend me any other module that uses segment editor in python script. The video just shows that the Slicer starts creating things on the fly and then returns to original state. That does not happen in windowed mode.</p>

---

## Post #9 by @lassoan (2020-02-21 14:52 UTC)

<p>I’m not sure what you mean but Segment Editor module is a typical example of using segment editor widget in a scripted module.</p>
<p>Just wander around Slicer and use other modules (that behave normally) so that I can see what is normal (and just image compression artifact or bad image quality) and what is something else (a problem that you can only see in a specific module).</p>

---

## Post #10 by @Alex_Vergara (2020-02-21 14:54 UTC)

<p>Here is my code anyways, Ill try to upload a better video<br>
<a href="https://gitlab.com/opendose/opendose4d/-/blob/calibration/Dosimetry4D/Calibration.py#L317" rel="nofollow noopener">https://gitlab.com/opendose/opendose4d/-/blob/calibration/Dosimetry4D/Calibration.py#L317</a></p>

---

## Post #11 by @Alex_Vergara (2020-02-21 15:00 UTC)

<p>here it is <a href="https://drive.google.com/open?id=1uOnVNJFSrp0JG0W2HSpjV_CjrEgRxXm2" rel="nofollow noopener">https://drive.google.com/open?id=1uOnVNJFSrp0JG0W2HSpjV_CjrEgRxXm2</a></p>

---

## Post #12 by @lassoan (2020-02-21 15:12 UTC)

<p>By “flickering” you mean that a window is shown for a second at 0:05, 0:15, and 0:30? I would comment out things first in the Python module then in the segment editor widget to see what exact step causes this.</p>

---

## Post #13 by @Alex_Vergara (2020-02-21 15:17 UTC)

<p>I have bisected the code and the specific line that causes the flickering is this one</p>
<pre><code class="lang-auto">segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
</code></pre>

---

## Post #14 by @lassoan (2020-02-21 15:21 UTC)

<p>OK, this is useful information. You need to continue commenting out code parts within the segment editor widget. It is more tedious, but it should lead us to the call that triggers this and then we should be able to fix it.</p>

---

## Post #15 by @Alex_Vergara (2020-02-21 15:31 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="13" data-topic="10380">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>qMRMLSegmentEditorWidget</p>
</blockquote>
</aside>
<p>I have created this routine<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42e039c28b938c2f6114dc689a830fd06bb2b17d.png" alt="image" data-base62-sha1="9xBUGjPt37U2vMFh3epioBXV38V" width="445" height="58"><br>
Thats everything I need to replicate the flickering. Again in windowed mode the bug does not show.</p>

---

## Post #16 by @lassoan (2020-02-21 15:43 UTC)

<p>OK. Now you need to continue commenting out code parts within the segment editor widget (in C++) to see what exactly triggers the behavior.</p>

---

## Post #17 by @Alex_Vergara (2020-02-21 15:53 UTC)

<p>OK, that call just do this</p>
<pre><code class="lang-auto">qMRMLSegmentEditorWidget::qMRMLSegmentEditorWidget(QWidget* _parent)
  : qMRMLWidget(_parent)
  , d_ptr(new qMRMLSegmentEditorWidgetPrivate(*this))
{
  Q_D(qMRMLSegmentEditorWidget);
  d-&gt;init();
}
</code></pre>
<p>and the init call do this</p>
<pre><code class="lang-auto">void qMRMLSegmentEditorWidgetPrivate::init()
{
  Q_Q(qMRMLSegmentEditorWidget);
  this-&gt;setupUi(q);
..........
</code></pre>
<p>So the UI is always generated even in the case we don’t need it at all. My nose tells me this is the thing but I can’t confirm without a build. I have left c++ because of this, I hate to build!</p>

---

## Post #18 by @lassoan (2020-02-25 00:21 UTC)

<p>Instantiating a couple of widgets in <code>setupUi()</code> should be no problem.</p>
<p>We were debating when we designed segment editor if we should separate GUI and logic. Since an “editor” is inherently an interactive component, instantiating GUI classes has practically zero cost, segment editor effect classes are usually very small, and splitting classes would have resulted in many more classes, we chose not to split. That is why you always instantiate GUI widgets, even if you don’t need it.</p>
<p>Let us know what you find. You might even get some information without rebuilding, buy XCode Instrument, but probably you cannot avoid building Slicer if you want to experiment.</p>

---
