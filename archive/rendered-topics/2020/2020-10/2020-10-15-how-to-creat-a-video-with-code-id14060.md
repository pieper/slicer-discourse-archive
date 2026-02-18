# How to creat a video with code

**Topic ID**: 14060
**Date**: 2020-10-15
**URL**: https://discourse.slicer.org/t/how-to-creat-a-video-with-code/14060

---

## Post #1 by @aldoSanchez (2020-10-15 18:57 UTC)

<p>Hi, today I was trying to make a video or gif.<br>
but the thing is that I couldn’t I don’t really now why but here’s the code I got:</p>
<p>cap = ScreenCapture.ScreenCaptureLogic().createVideo(30,‘extra’,‘C:\Program Files\Slicer 4.10.2’,‘image_%05d.mp4’,‘vid.mp4’)</p>
<p><span class="hashtag">#what</span> it’s in the repository is :<br>
def createVideo(self, frameRate, extraOptions, outputDir, imageFileNamePattern, videoFileName)</p>
<p>it gives me the next error:</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/ScreenCapture.py”, line 1100, in createVideo<br>
raise ValueError("Video creation failed: ffmpeg executable path is invalid: "+ffmpegPath)<br>
ValueError: Video creation failed: ffmpeg executable path is invalid: C:\Program Files\Slicer 4.10.2</p>
<p>if someone could give me an example of how to use it, that would help a lot.</p>

---

## Post #2 by @lassoan (2020-10-15 19:10 UTC)

<p>You need to install ffmpeg (it cannot be bundled with Slicer due to video codec licensing issues) and tell the module where to find it. The easiest is to export a video using the Screen Capture module GUI first, which will offer automatic download and install of ffmpeg.</p>

---

## Post #3 by @aldoSanchez (2020-10-15 19:35 UTC)

<p>ScreenCapture.ScreenCaptureLogic().ffmpegDownload()<br>
<span class="hashtag">#that</span> gives me this but it dose not open<br>
Requesting download ffmpeg from <a href="http://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-3.2.4-win64-static.zip" rel="noopener nofollow ugc">http://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-3.2.4-win64-static.zip</a>…</p>
<p><span class="hashtag">#so</span> i went to :<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://ffmpeg.org/download.html/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://ffmpeg.org/download.html" target="_blank" rel="noopener nofollow ugc">ffmpeg.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://ffmpeg.org/download.html" target="_blank" rel="noopener nofollow ugc">Download FFmpeg</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>i don’t really undertand how to install this</p>

---

## Post #4 by @lassoan (2020-10-15 19:56 UTC)

<p>You can download and unzip any of the ffmpeg packages and set the path to ffmpeg.exe in the Screen Capture module GUI.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e8da3f85b8e3012fc8f5aae5d3cbbf42c813d7e.png" data-download-href="/uploads/short-url/24K9aOOjIN7Hf0ys6rFNCPilfK6.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e8da3f85b8e3012fc8f5aae5d3cbbf42c813d7e_2_481x500.png" alt="image" data-base62-sha1="24K9aOOjIN7Hf0ys6rFNCPilfK6" width="481" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e8da3f85b8e3012fc8f5aae5d3cbbf42c813d7e_2_481x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e8da3f85b8e3012fc8f5aae5d3cbbf42c813d7e_2_721x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e8da3f85b8e3012fc8f5aae5d3cbbf42c813d7e_2_962x1000.png 2x" data-dominant-color="5E5646"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1300×1351 86 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2020-10-15 20:07 UTC)

<p>Alternatively, you can update the download URL in ScreenCapture.py file in your installed Slicer:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/403902710ce34505795044485881efdf915722a1/Modules/Scripted/ScreenCapture/ScreenCapture.py#L888" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/403902710ce34505795044485881efdf915722a1/Modules/Scripted/ScreenCapture/ScreenCapture.py#L888" target="_blank" rel="noopener">Slicer/Slicer/blob/403902710ce34505795044485881efdf915722a1/Modules/Scripted/ScreenCapture/ScreenCapture.py#L888</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="878" style="counter-reset: li-counter 877 ;">
<li>ffmpegTargetDirectory = self.getDownloadedFfmpegDirectory()</li>
<li>filePath = slicer.app.temporaryPath + '/ffmpeg-package.zip'</li>
<li>success = self.unzipFfmpeg(filePath, ffmpegTargetDirectory)</li>
<li>if success:</li>
<li>  # there was a valid downloaded package already</li>
<li>  return True</li>
<li>
</li><li># List of mirror sites to attempt download ffmpeg pre-built binaries from</li>
<li>urls = []</li>
<li>if os.name == 'nt':</li>
<li class="selected">  urls.append('https://github.com/Slicer/SlicerBinaryDependencies/releases/download/ffmpeg/ffmpeg-3.2.4-win64-static.zip')</li>
<li>else:</li>
<li>  # TODO: implement downloading for Linux/MacOS?</li>
<li>  pass</li>
<li>
</li><li>success = False</li>
<li>qt.QApplication.setOverrideCursor(qt.Qt.WaitCursor)</li>
<li>
</li><li>for url in urls:</li>
<li>
</li><li>  success = True</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #7 by @aldoSanchez (2020-10-15 20:29 UTC)

<p>i got it, thanks for the information it was really helpfull<br>
i leave the code:<br>
cap = ScreenCapture.ScreenCaptureLogic().createVideo(30,’-codec mpeg4 -qscale 3’,‘C:/Users/aldot/Desktop/ICBM/python/img’,‘image_%05d.png’,‘vid.mp4’)</p>

---
