# Recent improvements in window/level management

**Topic ID**: 7284
**Date**: 2019-06-23
**URL**: https://discourse.slicer.org/t/recent-improvements-in-window-level-management/7284

---

## Post #1 by @lassoan (2019-06-23 13:48 UTC)

<p>This is a quick summary of image window/level (brightness/contrast) adjustment changes introduced in recent Slicer Preview (formerly known as “Nightly”) releases.</p>
<ol>
<li>Improved automatic window/level algorithm</li>
</ol>
<p>Images that do not contain preferred window/level information are displayed with automatically computed values. The complex automatic computation algorithm that had been used in Slicer worked marginally better for some images, but sometimes generated too bright images and overall the results were somewhat unpredictable.</p>
<p>The algorithm is replaced by a simpler one, which adjust the window to display intensity values between 0.1 and 99.9 percentiles.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f49ecd148e343b274b506e69cf3a305e0a939c0f.jpeg" data-download-href="/uploads/short-url/yU0JpZ3opY3lEVuyJol2biGgtoH.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f49ecd148e343b274b506e69cf3a305e0a939c0f_2_690x285.jpeg" alt="image" data-base62-sha1="yU0JpZ3opY3lEVuyJol2biGgtoH" width="690" height="285" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f49ecd148e343b274b506e69cf3a305e0a939c0f_2_690x285.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f49ecd148e343b274b506e69cf3a305e0a939c0f_2_1035x427.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f49ecd148e343b274b506e69cf3a305e0a939c0f_2_1380x570.jpeg 2x" data-dominant-color="424141"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1471×608 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>Improved manual window/level adjustment</li>
</ol>
<p>New mouse mode is added for window/level adjustment. This prevents accidental modification of window/level when interacting in slice views and allows new window/level adjustment methods. Click on the corresponding icon on the toolbar to activate the new mode. The icon consists of color and grayscale gradients and a mouse pointer:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb0efdef9970062e2f46839e8477554354ad1b11.png" alt="image" data-base62-sha1="sYl2T2YCAe7nbjZcn0Ay7MRRX7b" width="133" height="49"></p>
<p>Window/level setting options:</p>
<ul>
<li>Click-and-drag adjusts window/level (same as before)</li>
<li>Ctrl + left-click-and-drag sets optimal window/level for the selected region. Pressing Escape or right-click during the drag cancels the operation.</li>
<li>Double-click resets window/level (using automatic window/level algorithm, for the entire image)</li>
</ul>
<p>Region-based auto window/level example:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf742af441a06e4c27815d5340b9571a7037101c.jpeg" data-download-href="/uploads/short-url/tBdIVQ4xFtJdKFh79RPPTKAHnCA.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf742af441a06e4c27815d5340b9571a7037101c_2_690x322.jpeg" alt="image" data-base62-sha1="tBdIVQ4xFtJdKFh79RPPTKAHnCA" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf742af441a06e4c27815d5340b9571a7037101c_2_690x322.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf742af441a06e4c27815d5340b9571a7037101c_2_1035x483.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf742af441a06e4c27815d5340b9571a7037101c.jpeg 2x" data-dominant-color="54504E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1306×610 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Demo video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="u1B0F1KcVsk" data-video-title="3D Slicer - new mouse mode for window/level" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=u1B0F1KcVsk" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/u1B0F1KcVsk/maxresdefault.jpg" title="3D Slicer - new mouse mode for window/level" width="" height="">
  </a>
</div>


---

## Post #2 by @Amine (2019-07-18 02:44 UTC)

<p>Could there be an option in settings to enable windowing using the normal mouse cursor as well? working with multiple series and needing to change windows on the go is awkward, i guess for people who are familiar with slicer this will be a bigger bother than of the window accidentally changing, unless there is a planned better use of the regular left click.</p>

---

## Post #3 by @lassoan (2019-07-18 04:43 UTC)

<p>If you find that you need to modify window/level of multiple volumes then you can keep the mouse mode in window/level mode. You can still pan, zoom, browse slices, etc. and adjust window/level with left-click-and-drag the same way as before.</p>
<p>Also, we plan to make it easier to switch between mouse modes (using right-click context menu and keyboard shortcuts).</p>

---

## Post #4 by @Amine (2019-07-18 17:07 UTC)

<p>Thanks, keyboard shortcuts would be fine, the issue was more prominent when using segment editor as clicking “none” tool or Esc key disables the windowing mouse, and there is a need to switch back and forth when tweaking the window multiple times</p>

---

## Post #5 by @lassoan (2019-11-06 13:33 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-change-window-level-programmatically/9043">How to change window/level programmatically</a></p>

---

## Post #6 by @Vinny (2020-06-27 16:46 UTC)

<p>works great, thank you</p>

---

## Post #7 by @ButuiHu (2020-08-24 01:59 UTC)

<p>Hi, when I load DICOM series, 3D slicer uses the Window/level found in DICOM tags. However, DICOM series come with a lot of files, it seems 3D slicer uses the DICOM tag found in the first slice. While ITK-SNAP uses the last slice’s DICOM tag. ITK-SNAP usually gives me a better display result. Not sure the window level found in DICOM tags is set by doctor or the machine?</p>

---

## Post #8 by @lassoan (2020-08-24 04:24 UTC)

<aside class="quote no-group" data-username="ButuiHu" data-post="7" data-topic="7284">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/butuihu/48/2386_2.png" class="avatar"> ButuiHu:</div>
<blockquote>
<p>While ITK-SNAP uses the last slice’s DICOM tag. ITK-SNAP usually gives me a better display result.</p>
</blockquote>
</aside>
<p>Have you found any reference in ITK-Snap source code that it uses window center&amp;width stored in the DICOM file at all? (I have not, but I’m not that familiar with its source code) Maybe it just applies histogram-based auto-brightness/contrast.</p>
<p>Can you check if ITK-Snap’s brightness/contrast for DICOM files is the same (or similar to) Slicer’s auto brightness/contrast (that you get when you double-click on the image when the mouse mode is Window/level adjustment mode)?</p>
<p>It’s true that choosing to use the first slice’s window center/width is arbitrary, but I would expect that the last slice’s window would be just as bad. Maybe we could consider using a slice near the center of the image, as it may be more representative of content clinicians are most interested in.</p>

---

## Post #9 by @ButuiHu (2020-08-26 08:10 UTC)

<p>Check these screenshots:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a41dcef2ba51378f11a6ffe3b1b60103f4e59b4f.jpeg" alt="image" data-base62-sha1="npQauVP9SX4VPnYFsdZvmqvTgxp" width="451" height="468"><br>
ITK-SNAP</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91bc63781f04d21c95fae42fb95135976af6a696.jpeg" alt="image" data-base62-sha1="kNeQW6xf6n1IiowRNrjTnfoCjDE" width="451" height="470"><br>
3D Slicer with auto brightness/contrast</p>
<p>Maybe you’re right, we could consider using the middle slice’s DICOM tag.</p>

---

## Post #10 by @lassoan (2020-08-26 22:44 UTC)

<p>I haven’t encountered a case when window/level was drastically different in first/middle slice. If this is the case for this data set then it would be great to have it for testing.</p>
<p>Is this from a public image database? If not, could you anonymize and share it? (you can send me the download link in a private message)</p>
<p>I’ve added an issue to keep track of this issue and potential fix:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/5140" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5140" target="_blank" rel="noopener">Use more representative slice's window/level when loading DICOM image</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-08-26" data-time="22:58:54" data-timezone="UTC">10:58PM - 26 Aug 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">When loading a DICOM series, default window/level is taken from the first slice. In some cases, window/level is different for each...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #11 by @ButuiHu (2020-08-31 05:19 UTC)

<p>I’m so sorry. The data is from a hospital. We have no permission to share it even after anonymize it.</p>

---
