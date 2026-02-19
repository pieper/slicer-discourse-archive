---
topic_id: 12906
title: "Can I Save The Scene As A Html"
date: 2020-08-08
url: https://discourse.slicer.org/t/12906
---

# Can I save the scene as a html?

**Topic ID**: 12906
**Date**: 2020-08-08
**URL**: https://discourse.slicer.org/t/can-i-save-the-scene-as-a-html/12906

---

## Post #1 by @timeanddoctor (2020-08-08 07:24 UTC)

<p>I tend to share some “dicom” files as the “html” file. So it could be opened in Chrome.<br>
Can I save the scene as a html file(not include the 3d view)? Or, is there any python lib could deal with it?</p>

---

## Post #2 by @lassoan (2020-08-08 13:16 UTC)

<p>There are many options. You can export contact sheets (lightbox views), videos, and image sequences of views that you can view in a web browser using Screen Capture module.</p>
<p>You could put together a simple html+Javascript page to browse slices and rotate 3D view with sliders - it would be a fun project! If you come up with a solution then we would integrate it into the Screen Capture module.</p>
<p>You can also run full Slicer in a docker container and access it via a web browser. You can try it yourself in your browser now:</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://mybinder.org/static/favicon.ico?v=7102bb857703a0fece6d039a6777fc3f" class="site-icon" width="16" height="16">
      <a href="https://mybinder.org/v2/gh/Slicer/SlicerNotebooks/master?filepath=SlicerWeb.ipynb" target="_blank" rel="noopener">mybinder.org</a>
  </header>
  <article class="onebox-body">
    <img src="https://mybinder.org/static/images/logo_square.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://mybinder.org/v2/gh/Slicer/SlicerNotebooks/master?filepath=SlicerWeb.ipynb" target="_blank" rel="noopener">GitHub: Slicer/SlicerNotebooks/master</a></h3>

<p>Click to run this interactive environment. From the Binder Project: Reproducible, sharable, interactive computing environments.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2020-08-08 15:31 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> what do you think about a html export feature in Screen Capture module that would use cornerstone.js?</p>
<p>If you could point me an example that displays a series of pngs (zstack browsing with zoom) then I could easily add it as an export option to Screen Capture.</p>

---

## Post #4 by @timeanddoctor (2020-08-09 14:19 UTC)

<p>Thanks.<br>
I used to create the web files through the manu of Mango, another free and open source software. But I donot how to call it in slicer’s python.<br>
<a href="http://ric.uthscsa.edu/mango/index.html" class="onebox" target="_blank" rel="nofollow noopener">http://ric.uthscsa.edu/mango/index.html</a></p>
<p>I think the html file could be more convenient than png especially in mobile phone.</p>

---

## Post #5 by @lassoan (2020-08-09 15:31 UTC)

<p>Mango/Papaya web viewer looks nice, has BSD-type license, and seems to be very easy to export data to it from Slicer. However, it seems like a one-man-project, which is not developed anymore (there are barely any commits made over the last year), and did not work on a mobile browser that I tried.</p>
<p>Cornerstone viewer is a larger community effort, with lots of ties to the Slicer ecosystem, so it would be better to use that. But it seems a bit more complicated to set it up. I would need at least a fully configured demo deployment. <a class="mention" href="/u/pieper">@pieper</a> could you help with this (or it would not be that simple to set this up with Cornerstone/OHIF)?</p>

---

## Post #6 by @pieper (2020-08-10 14:16 UTC)

<p>I’d suggest trying <a href="https://slicedrop.com">https://slicedrop.com</a>, the original Slicer-in-a-browser project by Daniel Haehn, for simple viewing.  It handles most file formats used by Slicer (including DICOM if they form a volume stack) and does orthogonal reslice and window/level natively.  It’s a few years old now but still very slick.</p>

---

## Post #7 by @lassoan (2020-08-10 14:58 UTC)

<p>Thanks for the suggestion <a class="mention" href="/u/pieper">@pieper</a>, I’ve tried slicedrop and it works nicely.</p>
<p>I’ve just realized that you can also use <a href="http://kheops.online/">Kheops</a> for this, which has a built-in OHIF viewer and takes care of storage and authentication, too.</p>

---

## Post #8 by @timeanddoctor (2020-08-10 16:02 UTC)

<p>Thank you very much!<br>
Really cool !</p>

---

## Post #9 by @timeanddoctor (2020-08-12 05:41 UTC)

<p>How can I change my code to open my volume just giving a path of nrrd file in the index.html?<br>
I tend to share a volume with my team by slicedrop, and I hope they can access the data just click the index file, which means that each one do not need to click the file button to reselect the path in the index.html?<br>
However, I am not good at java. Could you help me?<br>
And my path is “D:/slicerdrop”<br>
Thank you very much!</p>
<p>I forked the index in my github:<br>
</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/neurosurgerydoctor/slicedrop.github.com/blob/aee20fc73d6855f9c64610f6b8de397c6fc94714/index.html#L159" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/neurosurgerydoctor/slicedrop.github.com/blob/aee20fc73d6855f9c64610f6b8de397c6fc94714/index.html#L159" target="_blank" rel="nofollow noopener">neurosurgerydoctor/slicedrop.github.com/blob/aee20fc73d6855f9c64610f6b8de397c6fc94714/index.html#L159</a></h4>
<pre class="onebox"><code class="lang-html"><ol class="start lines" start="149" style="counter-reset: li-counter 148 ;">
<li>				&lt;/div&gt;</li>
<li>				&lt;div id='brainstem' style='display: none'&gt;</li>
<li>					A region of the brainstem of a human adult including an</li>
<li>					automatically generated segmentation as a label map colorized using</li>
<li>					an anatomical color table. &lt;b&gt;Loading time: +&lt;/b&gt; &lt;span</li>
<li>						class='label label-info viewexample' id='brainstemlink'&gt;View</li>
<li>						Example&lt;/span&gt;</li>
<li>				&lt;/div&gt;</li>
<li>			&lt;/div&gt;</li>
<li>
</li><li class="selected">			&lt;div class='dropzone'&gt;</li>
<li>				&lt;span&gt;Drop files here or &lt;/span&gt;&lt;input id='filebutton' type='file'</li>
<li>					multiple onchange='selectfiles(this.files)' style='display: none;'&gt;&lt;/input&gt;&lt;a</li>
<li>					class='btn btn-inverse btn-large' style='vertical-align: super;'</li>
<li>					onclick='javascript:document.getElementById("filebutton").click();'&gt;Select</li>
<li>					files&lt;/a&gt;&lt;br /&gt;</li>
<li>				&lt;span style='font-size: 10px'&gt; Your data stays on your</li>
<li>					computer. No upload required!&lt;/span&gt;&lt;br /&gt;</li>
<li>				&lt;br /&gt;</li>
<li>				&lt;ul class='thumbnails'&gt;</li>
<li>					&lt;li&gt;</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #10 by @pieper (2020-08-12 14:16 UTC)

<p>I haven’t tried myself, but you should be able to do something like Daniel’s examples.  If you host the slicedrop web app code and the data on the same server (to avoid CORS issues) then you can configure a json file like ones in the examples and embed the path to it as a URL parameter like in this example.</p>
<p><a href="http://x.babymri.org/example4/?scene=http://x.babymri.org/example4/scene.json" class="onebox" target="_blank">http://x.babymri.org/example4/?scene=http://x.babymri.org/example4/scene.json</a></p>
<p>In addition to volumes, you should be able to share segmentations, models, and even tractography this way.</p>

---

## Post #11 by @lassoan (2020-08-12 15:02 UTC)

<p><a class="mention" href="/u/timeanddoctor">@timeanddoctor</a> Slicer How do you use this viewer? Copy it to a USB stick and then view it on a computer? Or do you upload it to a web server and access from a tablet/phone? Is there a preference for the data to remain on a remote server (not downloaded to the user’s computer)? Or, is the data already on the user’s computer (and you prefer not to upload it to a remote server)?</p>
<p>Slicer is already a fully portable, zero-install viewer (<a href="https://github.com/Slicer/Slicer/pull/5029">soon</a> it will be distributable with any extensions, Python packages, and settings), which can be launched with a shortcut to load a set of images. Could this be useful? We could also customize the appearance to only show features and module that you would like your users to see.</p>
<p>Slicer can also be used in a web browser, without the need to download any images to the user’s computer/tablet/phone (by running it in a docker container, as shown in the <a href="https://mybinder.org/v2/gh/Slicer/SlicerNotebooks/master?filepath=SlicerWeb.ipynb">SlicerJupyter example</a>).</p>

---

## Post #12 by @timeanddoctor (2020-08-12 16:24 UTC)

<p>Thanks.<br>
Slicer is powerfull and we use it for preoperation plan regularly.<br>
I tend share a dicom image by chrome for my friends who can read it in mobile phone. We used to do this by the png file.<br>
I still do not  deal with the dropslice problem for the index code is difficult for me. And I dont want to apply a host server as well. I think it is a tremedous task for me to do.</p>

---

## Post #13 by @pieper (2020-08-12 16:36 UTC)

<p>You wouldn’t need to run your own server.  I believe it would work fine with a cloud storage hosting service, like dropbox, AWS S3 or similar.  That way you could also selectively share access with strong security.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> we could probably set up the glTF exporter to also create a simple web app wrapper that could be easily shared out of dropbox.</p>

---
