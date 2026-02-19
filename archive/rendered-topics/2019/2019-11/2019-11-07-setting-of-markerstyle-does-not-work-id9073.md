---
topic_id: 9073
title: "Setting Of Markerstyle Does Not Work"
date: 2019-11-07
url: https://discourse.slicer.org/t/9073
---

# Setting of MarkerStyle does NOT work!

**Topic ID**: 9073
**Date**: 2019-11-07
**URL**: https://discourse.slicer.org/t/setting-of-markerstyle-does-not-work/9073

---

## Post #1 by @aiden.zhu (2019-11-07 23:07 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11.0-2009-06.23<br>
Expected behavior: vtkMRMLPlotSeriesNode → Marker-Style<br>
Actual behavior: Only square works with the selection of Marker-style</p>
<p>Hi I am using 4.11.0 nightly version and it found that the plotting lines canNOT be set in a right way with the options of Markers Styles.</p>
<p>MarkerStyleCross → shows square-shape<br>
MarkerStylePlus → not working<br>
MarkerStyleSquare–&gt; the one working only<br>
MarkerStyleCircle → not working<br>
MarkerStyleDiamond → not working</p>
<p>Anyone has the same issue? or a new version has fixed such problems?</p>
<p>Screenshots to show the issue:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9938ad8e225102311d752b081e70b9d023aadad.png" alt="image" data-base62-sha1="v2LIAshgDxIKcoHhqXnsfS4GYfH" width="539" height="239"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d412338329ab092b4145d3ba3757549b604aa560.png" data-download-href="/uploads/short-url/ug4dCpocY53PSb5dMQ3MPPDmR1K.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d412338329ab092b4145d3ba3757549b604aa560.png" alt="image" data-base62-sha1="ug4dCpocY53PSb5dMQ3MPPDmR1K" width="631" height="500" data-dominant-color="FCFCF6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1545×1223 11.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks a lot.</p>

---

## Post #2 by @lassoan (2019-11-08 00:00 UTC)

<p>I’ve tested this now and it works well. You don’t see the marker because you have set the marker size to a small value line thickness to a large value.</p>

---

## Post #3 by @aiden.zhu (2019-11-08 00:07 UTC)

<p>Thanks a lot for your quick reply, Andras.</p>
<p>I did as you mentioned the values settings. But it’s not working. Which version are you using? maybe I need think about trying to update it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dbd76829b29b8a5cb74186e6ebf831eca2e07a3.png" data-download-href="/uploads/short-url/8Ob2Z6mFxrDdHzeu9spKKzrSgOD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dbd76829b29b8a5cb74186e6ebf831eca2e07a3.png" alt="image" data-base62-sha1="8Ob2Z6mFxrDdHzeu9spKKzrSgOD" width="690" height="198" data-dominant-color="F5F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">933×269 5.49 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cf449f38004276403fbb06342f69bc3d2e66daf.png" data-download-href="/uploads/short-url/hPoAKPTuqxoKkAXQhBrC8s7KKD5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cf449f38004276403fbb06342f69bc3d2e66daf.png" alt="image" data-base62-sha1="hPoAKPTuqxoKkAXQhBrC8s7KKD5" width="597" height="499" data-dominant-color="FEFBF5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1435×1201 14.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To get a comparison:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ac4a69a94161f2e6918c26b0f56eb16b7ff0cd1.png" alt="image" data-base62-sha1="66lnjUfVBTwdQhhaWxTxCHILaMx" width="629" height="265"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c8e6d8b3fab835e78b83188505710667ea46435.png" data-download-href="/uploads/short-url/mkXDpU79zSq5XffOpj8yc2fqmgt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c8e6d8b3fab835e78b83188505710667ea46435.png" alt="image" data-base62-sha1="mkXDpU79zSq5XffOpj8yc2fqmgt" width="483" height="500" data-dominant-color="FEF9F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1201×1243 12 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best,<br>
Aiden</p>

---

## Post #4 by @lassoan (2019-11-08 00:28 UTC)

<p>Does it work well if you create a plot using this script?</p>
<pre><code class="lang-auto"># Get a volume from SampleData and compute its histogram
import SampleData
import numpy as np
volumeNode = SampleData.SampleDataLogic().downloadMRHead()
histogram = np.histogram(arrayFromVolume(volumeNode), bins=50)

chartNode = slicer.util.plot(histogram, xColumnIndex = 1)
chartNode.SetYAxisRangeAuto(False)
chartNode.SetYAxisRange(0, 4e5)
</code></pre>
<p>Always use latest stable or latest preview release.</p>

---

## Post #5 by @aiden.zhu (2019-11-08 00:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="9073">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>import SampleData import numpy as np volumeNode = SampleData.SampleDataLogic().downloadMRHead() histogram = np.histogram(arrayFromVolume(volumeNode), bins=50) chartNode = slicer.util.plot(histogram, xColumnIndex = 1) chartNode.SetYAxisRangeAuto(False) chartNode.SetYAxisRange(0, 4e5)</p>
</blockquote>
</aside>
<p>Yes, but no circles as markers there,  Andras.</p>
<p>Here is the screenshot:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c87535bdb0980775e78417025e4b842223d82625.png" data-download-href="/uploads/short-url/sBkC8OM1Xm9Ls5GOmg15OHGOTLT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c87535bdb0980775e78417025e4b842223d82625_2_603x500.png" alt="image" data-base62-sha1="sBkC8OM1Xm9Ls5GOmg15OHGOTLT" width="603" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c87535bdb0980775e78417025e4b842223d82625_2_603x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c87535bdb0980775e78417025e4b842223d82625_2_904x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c87535bdb0980775e78417025e4b842223d82625_2_1206x1000.png 2x" data-dominant-color="FBFBF4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1531×1269 25.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thanks,<br>
Aiden</p>
<p>PS: I just did a quick check with the newly version of 4.11.0-2019-11-05 (nightly). I got exactly the same results as mentioned in the beginning.</p>
<p>Does that mean something wrong (or not that right) with my computer?<br>
Here is some basic info of my desktop:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11dc8cbdd7fe2abb818179c088274f7fea35c9f1.png" alt="image" data-base62-sha1="2y0DQysrhXzgsvoCeDdntMJFzJT" width="606" height="317"></p>

---

## Post #6 by @lassoan (2019-11-08 01:30 UTC)

<p>I was able to reproduce the problem on one computer while it works well on another.</p>
<p>Can you try if it works well if you</p>
<ul>
<li>open a terminal window where <code>Slicer.exe</code> is located</li>
<li>type <code>set SLICER_OPENGL_PROFILE=core</code>
</li>
<li>type <code>Slicer.exe</code> to start the application</li>
</ul>
<p>Copy-paste this to the Python console:</p>
<pre><code class="lang-python">import SampleData
import numpy as np
volumeNode = SampleData.SampleDataLogic().downloadMRHead()
histogram = np.histogram(arrayFromVolume(volumeNode), bins=50)

chartNode = slicer.util.plot(histogram, xColumnIndex = 1)
chartNode.SetYAxisRangeAuto(False)
chartNode.SetYAxisRange(0, 4e5)

chartNode.GetNthPlotSeriesNode(0).SetMarkerStyle(slicer.vtkMRMLPlotSeriesNode.MarkerStyleCircle)
chartNode.GetNthPlotSeriesNode(0).SetMarkerSize(15)
</code></pre>
<p>You may also try updating your graphics card drivers. What graphics card and driver version do you use?</p>

---

## Post #7 by @aiden.zhu (2019-11-08 13:37 UTC)

<p>Super!!! It works after setting Slicer_OpenGL_Profile=core! Thanks a lot, Andras.</p>
<p>How to check or make sure of SLICER_OPENGL_PROFILE=core if I run by python?</p>
<p>Best,<br>
Aiden</p>

---

## Post #8 by @aiden.zhu (2019-11-08 13:49 UTC)

<p>Solution-1:<br>
Start Slicer.exe from a terminal after “set SLICER_OPENGL_PROFILE=core”</p>
<p>Solution-2:<br>
Go to system’s “Advanced System Settings”–&gt; “Environment Variables”–&gt;Make a new variable as “SLICER_OPENGL_PROFILE” and set its value as “core”; then run Slicer as normal.</p>

---

## Post #9 by @lassoan (2019-11-08 14:33 UTC)

<aside class="quote no-group" data-username="aiden.zhu" data-post="7" data-topic="9073">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f19dbf/48.png" class="avatar"> aiden.zhu:</div>
<blockquote>
<p>How to check or make sure of SLICER_OPENGL_PROFILE=core if I run by python?</p>
</blockquote>
</aside>
<p>This is a system environment variable, so you can query its value from Python easily.</p>
<p>It is probably a bug in VTK library. Using OpenGL core profile causes rendering errors (e.g., render window update is delayed) on some computers with Intel graphics cards, so we had to force using OpenGL compatibility profile. However, apparently, this causes this issue on some high-end NVidia graphics cards.</p>
<p>Hopefully this problem will go away if we <a href="https://discourse.slicer.org/t/building-slicer-with-latest-vtk/9083">update to latest VTK version</a>. Until then you may use this workaround of explicitly setting OpenGL profile.</p>

---

## Post #10 by @aiden.zhu (2019-11-08 15:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="9073">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>import SampleData import numpy as np volumeNode = SampleData.SampleDataLogic().downloadMRHead() histogram = np.histogram(arrayFromVolume(volumeNode), bins=50) chartNode = slicer.util.plot(histogram, xColumnIndex = 1) chartNode.SetYAxisRangeAuto(False) chartNode.SetYAxisRange(0, 4e5) chartNode.GetNthPlotSeriesNode(0).SetMarkerStyle(slicer.vtkMRMLPlotSeriesNode.MarkerStyleCircle) chartNode.GetNthPlotSeriesNode(0).SetMarkerSize(15)</p>
</blockquote>
</aside>
<p>Yeah, just feel that render window update is really delayed too much due to this re-setting for OpenGL core profile. Thanks a lot, and looking forward to a new version after newly-updates with VTK.</p>
<p>Aiden</p>

---

## Post #11 by @lassoan (2019-11-08 15:53 UTC)

<p>The delayed update bug only affects certain Intel graphics cards and driver versions (but those don’t have the MarkerStyle issue). If yours is not among those graphics cards then you can safely use a core profile without any adverse affects.</p>
<p>What graphics card do you have? Do you see any problems when you enable OpenGL core profile?</p>

---

## Post #12 by @aiden.zhu (2019-11-08 16:05 UTC)

<p>I do have a NVIDIA Quadro P5000.<br>
It seems no problem for re-setting SLICER_OPENGL_PROFILE as core.</p>
<p>I was mis-led by a pixel-spacing setting, which I was trying to figure out what happens but failed.<br>
You see, now I have an image which has a pixel-spacing 15nm (that means, 1.5e-5mm). I load this image to Slicer and it seems fine. But the mouse-scroll to change slices along views does not work (slower than usual, the slice-bar on the top of each view work fine though). So I try to put a fake pixel-spacing value as 1.5mm or even 0.015mm, it works fine to middle-mouse-button-scroll to browse slices along views.<br>
This is what I was trying to ask you expertise to figure out in my next question. This issue may be reproduced by yourself , trying to use that famous MRHead image, if you set image pixel spacing as 0.001mm, it’s fine. but if you set image pixel spacing as 0.0001 mm, then you try mouse-scrolling where you may see my issue.</p>
<p>Thanks a lot again.</p>
<p>PS: I guess it’s better for me to open a new topic here: <a href="https://discourse.slicer.org/t/view-displays-lag-if-pixel-spacing-is-small/9087" class="inline-onebox">View displays lag if pixel-spacing is small</a>.</p>

---

## Post #13 by @lassoan (2019-11-08 17:48 UTC)

<aside class="quote no-group" data-username="aiden.zhu" data-post="12" data-topic="9073">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f19dbf/48.png" class="avatar"> aiden.zhu:</div>
<blockquote>
<p>I do have a NVIDIA Quadro P5000.</p>
</blockquote>
</aside>
<p>Yes, using OpenGL core profile has not been an issue for NVidia graphics cards, so there should be no drawback for you to use it.</p>

---
