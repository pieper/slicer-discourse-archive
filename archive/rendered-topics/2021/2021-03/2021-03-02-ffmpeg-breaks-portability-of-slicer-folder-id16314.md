---
topic_id: 16314
title: "Ffmpeg Breaks Portability Of Slicer Folder"
date: 2021-03-02
url: https://discourse.slicer.org/t/16314
---

# Ffmpeg breaks portability of Slicer folder

**Topic ID**: 16314
**Date**: 2021-03-02
**URL**: https://discourse.slicer.org/t/ffmpeg-breaks-portability-of-slicer-folder/16314

---

## Post #1 by @muratmaga (2021-03-02 19:32 UTC)

<p>ffmpeg is still installed under appdata/roaming/NA-MIC/ffmpeg in the latest stable, breaking the portability of the Slicer folder.<br>
Can this be changed to the Slicer folder like the rest of the extensions?</p>
<pre><code>Export to video...

Start ffmpeg:

C:\Users\amaga\AppData\Roaming\NA-MIC\ffmpeg\ffmpeg-3.2.4-win64-static\bin\ffmpeg.exe -nostdin -y -r 6.2 -start_number 0 -i C:\Users\amaga\Documents\SlicerCapture\tmp-P7XSU-%05d.png -codec libx264 -preset slower -pix_fmt yuv420p C:\Users\amaga\Documents\SlicerCapture\SlicerCapture.mp4

Video export succeeded to file: C:\Users\amaga\Documents\SlicerCapture\SlicerCapture.mp4</code></pre>

---

## Post #2 by @lassoan (2021-03-02 19:51 UTC)

<p>ScreenCapture module is fully prepared for both portable and shared Slicer.ini and if it does not find ffmpeg then it downloads it to the proper location (same folder as Slicer.ini).</p>
<p>Make sure that if you don’t want a shared Slicer.ini then copy/create a new one in the same location as the revisionUserSettings ini file is. You can get that folder by calling <code>qt.QFileInfo(slicer.app.slicerRevisionUserSettingsFilePath).absoluteDir().path()</code>. If you previously specified ffmpeg path with an absolute path then remove that path (or replace with a relative path).</p>

---

## Post #3 by @muratmaga (2021-03-02 20:08 UTC)

<p>Here is what I did:</p>
<ul>
<li>uninstalled all previous slicers</li>
<li>Deleted everything in c:\users\murat\appdata\local\na-mic</li>
<li>Deleted everything in c:\users\murat\appdata\roaming\na-mic (including slicer.ini)<br>
(I am assuming this equivalent to installed Slicer to a brand new computer. If not, let me know what else I should do).</li>
</ul>
<p>Installed the new slicer stable <strong>c:\users\murat\desktop</strong><br>
went to screen capture and choose video output. Said yes to download ffmpeg, it downloaded and installed at<br>
<strong>c:\users\murat\appdata\roaming\na-mic</strong> (it also created slicer.ini in that location too).</p>
<p>We have bunch of offline computers that I want to carry slicer in its entirety (including ffmpeg).</p>

---

## Post #4 by @lassoan (2021-03-02 20:36 UTC)

<p>Slicer creates a shared Slicer.ini by default. Make sure that if you don’t want a shared Slicer.ini then have a Slicer.ini in the same folder as the revisionUserSettings ini file is.</p>

---

## Post #5 by @muratmaga (2021-03-02 20:49 UTC)

<p>This worked, thank you!</p>
<p>It is a bit obscure. Would it be possible to make this as an install time option (if they choose to install for everyone there is a shared Slicer.ini, if not it is saved into the correct place).</p>

---

## Post #6 by @lassoan (2021-03-02 21:17 UTC)

<p>Main reason why creating a fully portable application is not made very easy or widely advertised is that it would require a little effort, and most users don’t need it (it is better if Slicer instances use same DICOM database, reuse downloaded ffmpeg, etc.).</p>
<p>I agree that we should have a module that makes it easy to create a portable package. Probably the main use case would be to bundle a portable data viewer with data sets (similarly to viewers supplied with DICOM DVDs), but it could be useful for training courses, and other use cases, too. I’ve submitted a feature request to keep track of this:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/5500" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5500" target="_blank" rel="noopener">Make it easy to create portable Slicer installations</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-03-02" data-time="21:10:59" data-timezone="UTC">09:10PM - 02 Mar 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">Is your feature request related to a problem? Please describe.
Recent Slicer versions can be made fully portable by having Slicer.ini file...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:enhancement</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
