# Connect external appareil to 3D Slicer

**Topic ID**: 24774
**Date**: 2022-08-15
**URL**: https://discourse.slicer.org/t/connect-external-appareil-to-3d-slicer/24774

---

## Post #1 by @abdoullah (2022-08-15 19:18 UTC)

<p>Operating system:Mac OS 12.4<br>
Slicer version:5.0.3<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2022-08-15 19:19 UTC)

<p>3D Slicer can be connected to a wide range of devices. What would you like to achieve?</p>

---

## Post #3 by @abdoullah (2022-08-15 22:19 UTC)

<p>I would like to transform an image of a part of body into a scanner image. So, I thought of two solutions:</p>
<ol>
<li>
<p>either take the photo with a smartphone then import it into 3D slicer</p>
</li>
<li>
<p>connect the smartphone to 3D slider and activate the camera to see the scanner images in real time on 3D slicer like this tutorial <a href="https://www.youtube.com/watch?v=BZ2OsMOnXlk" class="inline-onebox" rel="noopener nofollow ugc">TUSS-guided Nephrostomy - YouTube</a> (in the tutorial he did not connect a smartphone to 3D slicer)</p>
</li>
</ol>
<p>What is the best solution ?</p>
<p>Regards</p>

---

## Post #4 by @lassoan (2022-08-16 13:39 UTC)

<p>You can certainly load a photo (jpg, png, tif, …) into Slicer.</p>
<p>If you want to stream images into Slicer then I would not recommend connecting a phone (it costs at hundreds of $ or more, needs to be recharged, needs network connection configuration, etc). It is much easier to connect a good-quality webcam and stream the image via <a href="https://plustoolkit.github.io/">Plus toolkit</a> and <a href="https://github.com/openigtlink/SlicerOpenIGTLink">SlicerOpenIGTLink extension</a>. You can find lots of detailed tutorials at <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT website</a>.</p>

---

## Post #5 by @abdoullah (2022-08-16 13:52 UTC)

<p>Thank you.</p>
<p>I’ll try that.</p>

---

## Post #6 by @abdoullah (2022-08-18 13:51 UTC)

<p>Hi,</p>
<p>Please, how can I install Plus Toolkit on Mac OS ?</p>
<p>Regards</p>

---

## Post #7 by @lassoan (2022-08-18 17:56 UTC)

<p>We only provide pre-built Plus packages for Windows, as almost all medical device manufacturers (imaging, tracking devices, sensors, etc.) only provide drivers for Windows.</p>
<p>You have a couple of options:</p>
<ul>
<li>You can build Plus on macOS or Linux. Note that only a small number of hardware devices support these operating systems.</li>
<li>You can run the user interface (3D Slicer) on macOS or linux computer, but you do the data acquisition on a separate Windows box. Depending on the connected hardware, it may be a compute stick or mini-PC.</li>
<li>You switch to Windows so that you can have both data acquisition and user interface on one system.</li>
</ul>

---

## Post #8 by @PaoloZaffino (2022-08-18 18:21 UTC)

<p>If it can help, there is also the multi-OS possibility to connect Arduino with Slicer.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://pzaffino.github.io/SlicerArduinoController/">
  <header class="source">

      <a href="https://pzaffino.github.io/SlicerArduinoController/" target="_blank" rel="noopener nofollow ugc">SlicerArduinoController</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://pzaffino.github.io/SlicerArduinoController/" target="_blank" rel="noopener nofollow ugc">Slicer Arduino Controller</a></h3>

  <p>Extension for 3D Slicer that allows connecting and receiving/sending data from/to Arduino boards</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pzaffino/SlicerArduinoController">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pzaffino/SlicerArduinoController" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <img src="https://repository-images.githubusercontent.com/235574013/88cc4b80-af61-11ea-8f85-ed1c3fd2e284" class="thumbnail onebox-avatar" width="128" height="128">

<h3><a href="https://github.com/pzaffino/SlicerArduinoController" target="_blank" rel="noopener nofollow ugc">GitHub - pzaffino/SlicerArduinoController: Extension for 3D Slicer that...</a></h3>

  <p>Extension for 3D Slicer that allows connecting and receiving/sending data from/to Arduino boards - GitHub - pzaffino/SlicerArduinoController: Extension for 3D Slicer that allows connecting and rece...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @abdoullah (2022-08-25 22:40 UTC)

<p>How can I configure a webcam into Slicer 3D ?</p>

---

## Post #10 by @lassoan (2022-08-27 22:05 UTC)

<p>You can connect the webcam via Plus toolkit.</p>
<p>If you don’t want to use Plus then you can acquire an image using some Python package and import the numpy array into a volume node (see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#combine-multiple-volumes-into-one">example</a>).</p>

---

## Post #11 by @abdoullah (2022-09-04 00:59 UTC)

<p>Can I do a realtime 3D volume reconstruction using python and an external webcam ?</p>

---
