---
topic_id: 19952
title: "Delays In Paint Function Using Wacom Cintiq22"
date: 2021-10-01
url: https://discourse.slicer.org/t/19952
---

# Delays in 'Paint' function using Wacom Cintiq22

**Topic ID**: 19952
**Date**: 2021-10-01
**URL**: https://discourse.slicer.org/t/delays-in-paint-function-using-wacom-cintiq22/19952

---

## Post #1 by @softdent (2021-10-01 14:17 UTC)

<p>We’are using a Wacom Cintiq 22. and 3D slicer for 3D segmentation job for our research.<br>
Thank your for your great effort for the great software.</p>
<p>In your 3D slicer version 4.11.20210226, if we use the ‘Paint’ function with a Wacom pen in the Segmentation Editor, delay occurs like the attached picture.<br>
In 3D slicer 4.10.2, this delay of the ‘paint’ function does not occur when using a same Wacom pen.</p>
<p>Could it be solved in the next versions?</p>
<p>Thank you.</p>

---

## Post #2 by @softdent (2021-10-01 14:17 UTC)

<p>We’are using a Wacom Cintiq 22. and 3D slicer for 3D segmentation job for our research.<br>
Thank your for your great effort for the great software.</p>
<p>In your 3D slicer version 4.11.20210226, if we use the ‘Paint’ function with a Wacom pen in the Segmentation Editor, delay occurs like the attached picture.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c7d3cb772f6e6f0a4e8ef11d21b447263370571.jpeg" alt="image" data-base62-sha1="1Mu32yRlYlmgZJdfLxrWgyiWO6B" width="541" height="306"></p>
<p>In 3D slicer 4.10.2, this delay of the ‘paint’ function does not occur when using a same Wacom pen.</p>
<p>Could it be solved in the next versions?</p>
<p>Thank you.</p>

---

## Post #3 by @lassoan (2021-10-01 19:08 UTC)

<p>I cannot reproduce any delay using a Surface Pen:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="vNuvI9socTw" data-video-title="Image segmentation using pen and touchscreen" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=vNuvI9socTw" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/vNuvI9socTw/maxresdefault.jpg" title="Image segmentation using pen and touchscreen" width="" height="">
  </a>
</div>

<p>Current Surface Pens are excellent and you can also use a <a href="https://www.windowscentral.com/bamboo-ink-review">Wacom Bamboo Ink</a>. They cost less than $100 and allow you to draw on compatible screens similarly to the expensive Wacom Cintiq (the Cintiq costs 15x more).</p>
<p>If you want to stick to the Wacom Cintiq then there are a few things to try.</p>
<p>You can try to adjust your Wacom settings or follow tutorials on the web on how to reduce Wacom pen lag (such as <a href="https://fixthephoto.com/wacom-tablet-lagging.html">this page</a>).</p>
<p>Try the latest Slicer Preview Release, there have been many fixes and improvements since 4.11.20210226.</p>
<p>You can also try if adjusting event processing settings make a difference. Copy-paste this code snippet into the Python console (Ctrl+3) in Slicer and see if Paint effect performance is improved in the Red slice view:</p>
<pre><code class="lang-python">paint=slicer.modules.segmenteditor.widgetRepresentation().self().editor.effectByName("Paint")
paint.delayedPaint=True
paint.minimumPaintPointDistance=20
</code></pre>
<p>Enabling event compression for tablet events (Qt::AA_CompressHighFrequencyEvents, Qt::AA_CompressTabletEvents - see <a href="https://doc.qt.io/qt-5/qt.html#ApplicationAttribute-enum">here</a>) <a href="https://github.com/Slicer/Slicer/blob/7a532d54df88a5ac034966e8e04d4b4b23a0362c/Libs/MRML/Widgets/qMRMLWidget.cxx#L144">in Slicer source code</a> might help with this issue, too, but you would need to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html">build Slicer from source code</a> to try this.</p>
<p>This has been reported by another user some time ago, but then the correspondence stopped, so we closed the issue:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5063">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5063" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5063" target="_blank" rel="noopener">Segmentation editor regression: uneven or interrupted paint strokes -- especially with pen</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-07-27" data-time="22:45:08" data-timezone="UTC">10:45PM - 27 Jul 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2021-09-14" data-time="01:41:34" data-timezone="UTC">01:41AM - 14 Sep 21 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/fusentasticus" target="_blank" rel="noopener">
          <img alt="fusentasticus" src="https://avatars.githubusercontent.com/u/11786553?v=4" class="onebox-avatar-inline" width="20" height="20">
          fusentasticus
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">In 4.11.0-2020-07-20, I get the results below when trying to paint: the first is<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> with a pen on a Wacom tablet, the second with mouse. Both result from undersampled mouse tracking apparently, but it's especially bad with the pen! 

![with pen](https://user-images.githubusercontent.com/11786553/88598339-1a39dd80-d037-11ea-97fc-cfc7f897ef49.jpg)
![image](https://user-images.githubusercontent.com/11786553/88598550-86b4dc80-d037-11ea-9051-0aa255252085.png)

## Steps to reproduce

Start Slicer [with all extensions disabled just in case], load the sample CT chest volume, go to Segment Editor, create Segment, choose chest volume, choose paint, and the use pen or mouse.

## Expected behavior

Smooth strokes from gazilions of circle imprints. Paint effect produced smooth strokes in 4.11.0.2020-01-08. 

## Environment
- Slicer version: Slicer-4.11.0-2020-07-20
- Operating system: Windows</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2021-10-08 01:33 UTC)

<p>I’ve now tested a recent Slicer Preview Release (Slicer-4.13-2021-10-05) With a Wacom Intuos BT M tablet on Windows 10 and everything worked perfectly. The only thing that did not work with the default configuration was right-click zoom in views - for that I had to disable “Windows Ink” mode.</p>

---
