---
topic_id: 3333
title: "Export Volume Rendering As Stack Of Pngs Not Stls"
date: 2018-06-29
url: https://discourse.slicer.org/t/3333
---

# Export Volume Rendering as stack of PNG's. NOT stl's

**Topic ID**: 3333
**Date**: 2018-06-29
**URL**: https://discourse.slicer.org/t/export-volume-rendering-as-stack-of-pngs-not-stls/3333

---

## Post #1 by @JoeCrozier (2018-06-29 11:21 UTC)

<p>Operating system:Windows 10 Pro<br>
Slicer version:4.9.0</p>
<p>Hello.  I did a quick google search but nothing showed up so I was wondering if you could help me.</p>
<p>I am very familiar with thresholding/segmenting/exporting as stl’s, etc…  I work as a 3d Printing Lab Coordinator at a hospital.</p>
<p>However I’m fortunate enough to have a printer that can print voxel by voxel and theoretically have MUCH more detail than traditional 3d printers (in 500,000+ colors).  In order to print at the voxel level I need to provide a stack of .png’s to the software.  Obviously my first thought was to take the dicom images and convert to png in batch and provide that, but I’d rather not just have black and white prints.  So I thought it’d be cool if the volume rendering options in 3d slicer that provide color volumes could then be exported (with their colors) as a stack of png’s.   Possible?  How do I do it?</p>
<p>Thank you for any help!</p>

---

## Post #2 by @chir.set (2018-06-29 13:31 UTC)

<aside class="quote no-group" data-username="JoeCrozier" data-post="1" data-topic="3333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/c4cdca/48.png" class="avatar"> JoeCrozier:</div>
<blockquote>
<p>as a stack of png’s</p>
</blockquote>
</aside>
<p>You may record a video from your VR model using Screen Capture module, then export each frame to PNG images. It should be possible to modify the ffmpeg video creation options so that the source PNG files are not deleted during video creation, but I don’t know what other option to pass to ffmpeg. Or I completely missed your point.</p>

---

## Post #3 by @JoeCrozier (2018-06-29 13:43 UTC)

<p>I’d have to try it but I’m not 100% sure thats it.  What I’m looking for is really just like a png that is a colorized version of each dicom image.  I know there are dicom-&gt; png converters (which i’ve used) but then I’m left with black and white png’s.  I want pngs that have color and transparency added in a similar manner to what the volume render did.   I can then send that stack of png’s to my printer.</p>
<p>I’m assuming pngs from the video would be more like a frame by frame screenshot from one viewpoint?  Right?</p>

---

## Post #4 by @ihnorton (2018-06-29 13:48 UTC)

<aside class="quote no-group" data-username="JoeCrozier" data-post="1" data-topic="3333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/c4cdca/48.png" class="avatar"> JoeCrozier:</div>
<blockquote>
<p>I thought it’d be cool if the volume rendering options in 3d slicer that provide color volumes could then be exported (with their colors) as a stack of png’s. Possible? How do I do it?</p>
</blockquote>
</aside>
<p>This is still an area of active research, <s>and I don’t believe there is any turnkey solution implemented in Slicer right now</s> [edit: see <a href="https://discourse.slicer.org/t/export-volume-rendering-as-stack-of-pngs-not-stls/3333/7">link below</a>] . See the paper linked in the post below:</p>
<aside class="quote quote-modified" data-post="1" data-topic="3017">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/printing-volume-renderings-in-plastic/3017">Printing volume renderings in plastic</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    A question that comes up on this forum from time to time is why we can’t <a href="https://discourse.slicer.org/t/save-volume-rendering-as-stl-file/524">just 3D print the volume rendered view</a>.  We explain that most printers today expect STL surface models and we go into the difference between volume rendering and surface segmentation. 
I wanted to point out some just published research about new printing techniques that are much closer to directly printing out a volume rendering. 
These are photographs of 3D prints made using this technique: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a496d030927d0e4275076c12a22a39b048e7a5b0.jpeg" data-download-href="/uploads/short-url/nu1q6rRtxvFEDEQE9YPpsTP0S4g.jpg?dl=1" title="image">[image]</a> 
Here’s our paper that…
  </blockquote>
</aside>


---

## Post #5 by @JoeCrozier (2018-06-29 14:02 UTC)

<p>Thank you.  I had kind of assumed it wasn’t in slicer yet but I wanted to double check.  I know just enough programming in R to be dangerous and I think I’ll tinker with creating my own converter for dicom-&gt; png with added color.  We’ll see if I’m in over my head.</p>

---

## Post #6 by @lassoan (2018-06-29 14:37 UTC)

<p>What is the input to your printer? A 3D array of RGB voxels?</p>

---

## Post #7 by @pieper (2018-06-29 14:38 UTC)

<p>Hi Joe -</p>
<p>Actually there’s a working prototype we started a while back.  I just tested it and it works with Slicer 4.8 and may be just what you are looking for.  Hope it works for your purposes.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerFab/SlicerFab">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerFab/SlicerFab" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <img src="https://opengraph.githubassets.com/2bee2e005e3e239fdafac41aacc0b86d2421d6e132b6384796c7636cd5ae4e59/SlicerFab/SlicerFab" class="thumbnail" width="" height="">

<h3><a href="https://github.com/SlicerFab/SlicerFab" target="_blank" rel="noopener">GitHub - SlicerFab/SlicerFab: A 3D Slicer Extension for fabrication of...</a></h3>

  <p>A 3D Slicer Extension for fabrication of physical objects - GitHub - SlicerFab/SlicerFab: A 3D Slicer Extension for fabrication of physical objects</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>-Steve</p>

---

## Post #8 by @JoeCrozier (2018-06-29 14:44 UTC)

<p>Woohooo!! That’s awesome thank you!</p>

---

## Post #9 by @lassoan (2018-06-29 14:53 UTC)

<p>Steve, what kind of data your printer takes as input? 3D volume of dithered binary voxels, or RGB voxels?</p>

---

## Post #10 by @pieper (2018-06-29 15:11 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> it’s the one described in the paper - it acts just like an inkjet printer where you can choose what to deposit at each point (mix of primitive colors CMYK plus clear and maybe others like something to control the stiffness of the material).  There’s dithering in the driver to map the continuous tone of the input images to essentially bitmap (on/off) at high resolution of the printer.  So these sliced PNGs essentially go right into the printer driver.  That’s why the main module is called the BitmapGenerator.</p>
<p>By the way, it would be great if anyone wants to enhance this SlicerFab code.  There are more parameters like slab thickness and spacing, output image resolution, and other things that could easily be added to the interface if needed.</p>

---

## Post #11 by @JoeCrozier (2018-06-29 15:17 UTC)

<p>I just installed it and used it to generate png’s.  Prior to sending to the printer I should double check layer height.  The j750 I use has a 0.027mm thickness between layers, and I know the one in your paper was listed at 0.030.   Does the BitmapGenerator module automatically reslice to create this 0.030 thickness?</p>

---

## Post #12 by @pieper (2018-06-29 15:50 UTC)

<p>The parameters are here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerFab/SlicerFab/blob/master/BitmapGenerator/BitmapGenerator.py#L97-L103" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerFab/SlicerFab/blob/master/BitmapGenerator/BitmapGenerator.py#L97-L103" target="_blank">SlicerFab/SlicerFab/blob/master/BitmapGenerator/BitmapGenerator.py#L97-L103</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="97" style="counter-reset: li-counter 96 ;">
<li>def __init__(self):</li>
<li>  self.width = 1024</li>
<li>  self.height = 1024</li>
<li>  self.buildDirection = "SI" # TODO: allow other build directions</li>
<li>  self.slabSpacing = 0.03 # in mm, # DONE</li>
<li>  self.slabSpacing = 0.5</li>
<li>  self.slabThickness = 1 # in mm, TODO: confirm this is good - Not sure what this refers to</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>If you know the values you want, I’d suggest changing them in the code and then restarting slicer.  If you find yourself experimenting, you can enable Developer Mode in Slicer (se Edit-&gt;Application Settings -&gt; Developer) and you’ll get a Reload button so you can change the code on the fly.</p>
<p>Longer term, as I mentioned, it would be good to expose these in the user interface, possibly with presets for any commonly used printers.</p>

---

## Post #13 by @pieper (2018-06-29 15:52 UTC)

<p>I should mention too that this isn’t exactly the code used in the paper - some of the authors worked on this as a way to generalize the scripts used for the paper.</p>
<p>At this point there haven’t been a lot of prints made, so the best mapping between volume rendering and printer files is a bit of an open question (input welcome).</p>

---

## Post #14 by @Hamburgerfinger (2018-06-29 15:52 UTC)

<p>This looks awesome!  I tried to install it as an extension via Slicer’s Application Settings–&gt;Extension Wizard but it seems to not be working…  All that I have to do is add the path to the BitmapGenerator folder (in the SlicerFab-master folder cloned from GitHub) to the “Additional template paths for modules” section?  It should then show up as a module in Slicer, yes?</p>

---

## Post #15 by @pieper (2018-06-29 15:58 UTC)

<aside class="quote no-group" data-username="Hamburgerfinger" data-post="14" data-topic="3333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/eb9ed0/48.png" class="avatar"> Hamburgerfinger:</div>
<blockquote>
<p>This looks awesome!</p>
</blockquote>
</aside>
<p>Thanks!</p>
<p>Right - this is not in the Extension manager yet, but the structure is compatible, so if we confirm it works well and maybe add some tweaks to the UI it would be easy to migrate it (this would make it easier to install).</p>
<aside class="quote no-group" data-username="Hamburgerfinger" data-post="14" data-topic="3333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/eb9ed0/48.png" class="avatar"> Hamburgerfinger:</div>
<blockquote>
<p>to the “Additional template paths for modules” section? It should then show up as a module in Slicer, yes?</p>
</blockquote>
</aside>
<p>You can either put the path on the command line as in the README of the repository or you can add it to the Edit-&gt;Application Settings dialog by clicking the Add button shown below and browsing to the BitmapGenerator folder and then restarting.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/1138ab893c20a3526270684b1ea6797cbf46aad9.png" data-download-href="/uploads/short-url/2slwZbK9iifDZptM0mdybvytulP.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/1138ab893c20a3526270684b1ea6797cbf46aad9_2_690x308.png" alt="image" data-base62-sha1="2slwZbK9iifDZptM0mdybvytulP" width="690" height="308" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/1138ab893c20a3526270684b1ea6797cbf46aad9_2_690x308.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/1138ab893c20a3526270684b1ea6797cbf46aad9_2_1035x462.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/1138ab893c20a3526270684b1ea6797cbf46aad9_2_1380x616.png 2x" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1676×750 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @JoeCrozier (2018-07-05 14:43 UTC)

<p>Again, thank you for pointing out these modules.  Being close by I’d love to come up and talk to you about this in person.</p>
<p>My question now pertains to using this module to export png’s in color for the j750.  My contact at grabcad sent me this in response to the png’s SlicerFab created:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9e7b9a180b943947d5b489d17a20297e32a10c0.png" data-download-href="/uploads/short-url/xndIBma2qlCobuGvgbcRfr3nhle.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9e7b9a180b943947d5b489d17a20297e32a10c0_2_628x500.png" alt="Capture" data-base62-sha1="xndIBma2qlCobuGvgbcRfr3nhle" width="628" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9e7b9a180b943947d5b489d17a20297e32a10c0_2_628x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9e7b9a180b943947d5b489d17a20297e32a10c0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9e7b9a180b943947d5b489d17a20297e32a10c0.png 2x" data-dominant-color="DFDAD8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">878×699 68.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In your experience is there a way to control the number of colors exported?  Either in the volume rendering itself or in the code of slicerfab?</p>
<p>Thank you!</p>

---

## Post #17 by @pieper (2018-07-05 22:28 UTC)

<p>Right - the SlicerFab module just puts out the continuous tone color files, but they need to be further process for the printer using the <a href="https://www.liebertpub.com/doi/pdf/10.1089/3dp.2017.0140">dithering technique described in the paper.</a></p>
<p>The script for dithering is in <a href="https://github.com/SlicerFab/SlicerFab/blob/master/workflow/150209_bmpWorkflow.ipynb">this ipython notebook file</a> but doesn’t run automatically.  This allows you to get full color in the print even with a small number of colors in the printer (just like an ink just printer can print color images with only 4 ink cartridges).</p>
<p>Integrating the dithering step into the module directly is another task we haven’t had a chance to do yet, which is another reason SlicerFab is not a regular Slicer extension yet.</p>

---

## Post #18 by @JoeCrozier (2018-07-06 12:26 UTC)

<p>Guess I should have “read the manual”.  Thank you!</p>

---

## Post #19 by @pieper (2018-07-06 12:41 UTC)

<p>It’s definitely a work-in-progress so let us know how it goes for you!</p>

---

## Post #20 by @willyci (2018-08-10 14:32 UTC)

<p>Just want to say thanks to you guys, this module help me a lot, easy to use.</p>
<p>I am new to slicer, if anyone like me having problem using it, here is what I did<br>
I am on V4.8.1<br>
goto edit → app setting<br>
in modules, add the folder where the py code it. restart the app, it should show up in the modules drop down<br>
once you got the volume rendering setup, open the BitmapGenerator, setup where the folder is, click on “Apply”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3ba9068b4efc55a78f7d70ef124204a3726402f0.png" data-download-href="/uploads/short-url/8vMiZD58wWNIrvfN9sSjqKM8P4I.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3ba9068b4efc55a78f7d70ef124204a3726402f0_2_432x500.png" alt="Capture" data-base62-sha1="8vMiZD58wWNIrvfN9sSjqKM8P4I" width="432" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3ba9068b4efc55a78f7d70ef124204a3726402f0_2_432x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3ba9068b4efc55a78f7d70ef124204a3726402f0_2_648x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3ba9068b4efc55a78f7d70ef124204a3726402f0_2_864x1000.png 2x" data-dominant-color="CCCBCE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">872×1007 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<hr>
<p>I need the image to to be transparent , but I don’t know much about  python,<br>
so here is my python code to remove the white background.<br>
( maybe someone can update the module’s scode. )</p>
<pre><code class="lang-auto">import os
rootdir = '/temp/'
extensions = ('.png')
from PIL import Image


for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		ext = os.path.splitext(file)[-1].lower()
		if ext in extensions:
			print (os.path.join(subdir, file))
			img = Image.open(file)
			img = img.convert("RGBA")
			datas = img.getdata()
			
			newData = []
			for item in datas:
				if item[0] == 255 and item[1] == 255 and item[2] == 255:
					newData.append((255, 255, 255, 0))
				else:
					newData.append(item)

			img.putdata(newData)
			img.save("t_"+file, "PNG")
			continue
		else:
			continue
</code></pre>
<hr>

---

## Post #23 by @lassoan (2018-08-28 00:15 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Should we add this extension to the extension manager? Even if the module is imperfect, it fulfills a need.</p>

---

## Post #24 by @pieper (2018-08-28 17:09 UTC)

<p>Good point <a class="mention" href="/u/lassoan">@lassoan</a>, I <a href="https://github.com/Slicer/ExtensionsIndex/commit/1f6c8d1b83b1f2830b0613319adfddee73c12b02">added this</a> as an extension.  The extension was generated a while ago but the format should still be good (it builds for me).  We can see what it looks like in the morning.</p>
<p>People should feel free to track issues on the <a href="https://github.com/SlicerFab/SlicerFab">github repository</a>.  I don’t have easy access to the right printer, so it would be great of people who do could help improve the code.</p>

---

## Post #25 by @pieper (2018-08-29 21:32 UTC)

<p>The SlicerFab extension needed a couple tweaks, but a working extension should be available tomorrow in the extension manager.  It could still use work exposing some of the slicing parameters to the in the GUI but it should be workable.</p>

---

## Post #26 by @Nicholas.jacobson (2018-10-09 04:47 UTC)

<p>Does anyone have experience getting the png’s from slicerfab to print at the proper resolutions for a J750? Typically the y -res is 600 the x-res is 300. Currently I do not see an option in the python to modify the resolutions…</p>

---

## Post #27 by @Nicholas.jacobson (2018-10-09 05:04 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> . Are there any parameters for specifying the x and y resolutions? This is needed to be modified for the printer.</p>

---

## Post #28 by @lassoan (2018-10-09 05:31 UTC)

<p>I don’t think <a href="https://github.com/SlicerFab/SlicerFab/blob/master/BitmapGenerator/BitmapGenerator.py#L180">vtkPNGWriter</a> has an API to set DPI, but you can use Qt’s PNG writer instead:</p>
<pre><code># Grab image from view widget (just to have a complete working example)
lm = slicer.app.layoutManager()
threeDView = lm.threeDWidget(0).threeDView()
renderWindow = threeDView.renderWindow()
threeDView.forceRender()
windowToImage = vtk.vtkWindowToImageFilter()
windowToImage.SetInput(renderWindow)

# Write to file with custom DPI
dpi = 420.0
filename = "c:/tmp/test.png"
windowToImage.Update()
vtkImage = windowToImage.GetOutput()
qImage = qt.QImage()
slicer.qMRMLUtils().vtkImageDataToQImage(vtkImage, qImage)
inchesPerMeter = 39.3700787
qImage.setDotsPerMeterX(dpi*inchesPerMeter)
qImage.setDotsPerMeterY(dpi*inchesPerMeter)
imagePixmap = qt.QPixmap.fromImage(qImage)
imagePixmap.save(filename)</code></pre>

---

## Post #29 by @pieper (2018-10-09 12:30 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>If anyone wants to give this a try, it should be simple to switch to the Qt writer in the code below.  Then if it works it would be great to expose this in the GUI.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerFab/SlicerFab/blob/master/BitmapGenerator/BitmapGenerator.py#L175-L188" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerFab/SlicerFab/blob/master/BitmapGenerator/BitmapGenerator.py#L175-L188" target="_blank">SlicerFab/SlicerFab/blob/master/BitmapGenerator/BitmapGenerator.py#L175-L188</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="175" style="counter-reset: li-counter 174 ;">
<li>while slabCenter[2] &lt;= slabTop:</li>
<li>  roi.SetXYZ(slabCenter)</li>
<li>  threeDView.forceRender()</li>
<li>  windowToImage = vtk.vtkWindowToImageFilter()</li>
<li>  windowToImage.SetInput(renderWindow)</li>
<li>  writer = vtk.vtkPNGWriter()</li>
<li>  writer.SetInputConnection(windowToImage.GetOutputPort())</li>
<li>  filePath = filePattern % slabCounter</li>
<li>  windowToImage.Update()</li>
<li>  writer.SetFileName(filePath)</li>
<li>  writer.Write()</li>
<li>  slabCounter += 1</li>
<li>  slabCenter[2] = slabCenter[2] + self.slabSpacing</li>
<li>  self.delayDisplay("Saved to " + filePath, 30)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #30 by @ahmedhosny (2018-10-11 13:20 UTC)

<p>You need to be at 600dpi in the X and 300dpi in the Y for the connex500 printer. Z resolution is at 30um or 0.03mm. Essentially you need the X to be stretched twice as much as the Y. Make sure to do the stretching before the dither, otherwise your bits are not square anymore. Also make sure the X pixels are divisible by 16. crop slightly if needed. Y can be anything. <a href="https://www.dropbox.com/s/lvdjrb2a1q6giql/DOC-08407-A_Voxel-Printing%2B.pdf?dl=0" rel="nofollow noopener">Here</a> is a document from Stratasys that explains this further.</p>

---

## Post #31 by @Nicholas.jacobson (2018-11-09 06:22 UTC)

<p>Hey. There seems to be some bugs with the latest SlicerFab. I keep getting a stack of the same image repeated. Its not actually slicing the model anymore. The image is a top down view. How can I fix this?</p>

---

## Post #32 by @avarghes23 (2018-11-09 15:32 UTC)

<p>I was able to use the BitmapGenerator yesterday to create a .PNG image stack from a rendered volume by just simply hitting “Apply”. I’m using 3D Slicer 4.11.0 (Nightly Build).</p>

---

## Post #33 by @pieper (2018-11-09 18:20 UTC)

<p>Yes, it worked for me recently too and the code hasn’t changed.  Maybe different data or rendering settings?</p>

---

## Post #34 by @lassoan (2018-11-10 05:24 UTC)

<p>I’ve tried today with Slicer-4.10 and it works well for me, too.</p>
<p>Do you see the image changing on your screen?<br>
How large is your volume? (slab spacing is set to 0.5mm; if your volume is very large or very small then you might not see much change in the exported images)<br>
Is the voxel spacing set in mm? (it is, if you imported from DICOM)</p>

---

## Post #35 by @Nicholas.jacobson (2018-11-12 16:06 UTC)

<p>This has been resolved. The issue come about when cropping out the model to a much smaller size. The original bounding box can get messed up. It seems like the best practice is to save out just the volume and then run the bitmap generator on that one volume.</p>
<p>nick</p>

---

## Post #36 by @lassoan (2018-11-12 17:53 UTC)

<p>Yes, I would recommend to crop the volume to the desired size using Crop volume module. You can also apply arbitrarily shaped mask using Segment Editor’s Mask volume effect (available in SegmentEditorExtraEffects extension).</p>

---

## Post #37 by @Nicholas.jacobson (2018-12-13 22:52 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/ahmedhosny">@ahmedhosny</a> . I’m exporting a stack from an infant heart that is about 3" tall and only getting 146 png’s. Its coming in to the printer as .157" tall. Is there a setting in the Python for slicerfab that is off? What can I do to modify this correctly.</p>

---

## Post #38 by @lassoan (2018-12-13 23:17 UTC)

<p>You may need to adjust <code>slabSpacing</code> value in <a href="https://github.com/SlicerFab/SlicerFab/blob/master/BitmapGenerator/BitmapGenerator.py" rel="nofollow noopener">BitmapGenerator.py</a> to match your printer’s layer thickness.</p>

---

## Post #39 by @Nicholas.jacobson (2018-12-14 00:02 UTC)

<p>Ah yes there was an extra piece of code in there overriding the typical .027 spacing to .5. I have deleted it on my end and it is working well.</p>

---

## Post #42 by @Nicholas.jacobson (2018-12-24 18:59 UTC)

<p><a class="mention" href="/u/willyci">@willyci</a> where in the code did you place this block to take our the while background? Or has anyone else worked on creating a transparent background?</p>

---

## Post #43 by @lassoan (2018-12-27 04:33 UTC)

<p>I’ve sent a pull request that adds transparency (alpha channel) to the exported images - see <a href="https://github.com/SlicerFab/SlicerFab/pull/8" rel="nofollow noopener">https://github.com/SlicerFab/SlicerFab/pull/8</a></p>

---

## Post #44 by @Nicholas.jacobson (2018-12-27 21:15 UTC)

<p>Thanks Andras,<br>
There is one issue that I am finding. The slab spacing UI create does not allow for 0.027mm it does not allow for anything past 0.00 (two places after the decimal. The code looks good, so I am struggling to find the issue.</p>
<p>nick</p>

---

## Post #45 by @lassoan (2018-12-27 21:31 UTC)

<p>By default, number of decimals was set to 2. I’ve updated the pull request.</p>

---

## Post #46 by @Nicholas.jacobson (2018-12-27 21:37 UTC)

<p>Also now the images default to VTK MultiVolume rendering. For our purposes, we need the GPU RayCasting. It would be nice to be able to control this in the volume rendering. Can this be reset?</p>
<p>nick</p>

---

## Post #47 by @lassoan (2018-12-27 22:09 UTC)

<p>I don’t think it is related. You can set default volume rendering method in application settings.</p>

---

## Post #48 by @Nicholas.jacobson (2018-12-28 01:39 UTC)

<p>Thanks for all the updates. Can you explain what you did to resize the images? The scale is no longer seems to be correct. It seems to be almost filling the image created but not quite. So its not strictly based on ROI. The output that we were getting from the last build created images at the correct scale.</p>

---

## Post #49 by @lassoan (2018-12-28 02:23 UTC)

<aside class="quote no-group" data-username="Nicholas.jacobson" data-post="48" data-topic="3333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/ba8739/48.png" class="avatar"> Nicholas.jacobson:</div>
<blockquote>
<p>seems to be almost filling the image created but not quite</p>
</blockquote>
</aside>
<p>Exactly that. ROI size + a few percent margin, to maximize the details that can be represented in the fixed number of pixels. Resolution was not explicitly set before, so if it was “correct” then it was probably incidental.</p>
<p>Is there a specific pixel size that you would like to have in the output (and image size in pixels would be adjusted accordingly)?<br>
Or, would you prefer specifying image size in pixels and compute the resulting pixel size (DPI) and save it in the png file?</p>

---

## Post #50 by @Nicholas.jacobson (2018-12-28 03:30 UTC)

<p>Yes. Typically I take the images into photoshop to further process. This involves setting the scale to have a resolution of x=300 y=600 DPI for the printer (the images are skewed for printing purposes). Then limit the image to 6 colors because the printers can only handle 6 base colors, then a 50% dither is applied.</p>
<p>If we could get the image to print at 300x600 dpi that would be ideal.</p>
<p><a class="mention" href="/u/ahmedhosny">@ahmedhosny</a> wrote a python for dithering that could be incorporated to finish the process.</p>
<p>It would be nice to have the full process in slicer.</p>

---

## Post #51 by @lassoan (2018-12-28 15:22 UTC)

<aside class="quote no-group" data-username="Nicholas.jacobson" data-post="50" data-topic="3333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/ba8739/48.png" class="avatar"> Nicholas.jacobson:</div>
<blockquote>
<p>If we could get the image to print at 300x600 dpi that would be ideal.</p>
</blockquote>
</aside>
<p>This works now. I’ve implemented proper physical scaling of the exported image slices. You can specify DPI separately for x and y axes. These DPI values are also encoded in the png file, so they appear correctly in image editing programs or when printed. You can also specify object scale, which allows you to print the object smaller or larger than real physical size.</p>
<aside class="quote no-group" data-username="Nicholas.jacobson" data-post="50" data-topic="3333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/ba8739/48.png" class="avatar"> Nicholas.jacobson:</div>
<blockquote>
<p>limit the image to 6 colors because the printers can only handle 6 base colors, then a 50% dither is applied.</p>
</blockquote>
</aside>
<p>Are the 6 colors: CMYK + transparent + support material?<br>
In the described <a href="https://github.com/SlicerFab/SlicerFab/tree/master/workflow">workflow</a>, <strong>I did not find anything about color separation and colored dithering, do you have a code for it already?</strong></p>
<p>If yes, we should be able to use that code directly in Slicer. If you don’t have code for this (e.g., because you’ve done it so far in Photoshop), then we could implement this, potentially quite easily:</p>
<ul>
<li>Color separation: Basic implementation (that does not use ICC profiles based color matching, just generic approximations) is trivial.</li>
<li>Colored dithering: We would need to know if there are any constraints on the generated material images. <strong>Is the sum of pixel values among all materials at a specific position must be a specific number (if yes, what is that number 1, 16, …, 256?) or there is a maximum value?</strong></li>
</ul>

---

## Post #52 by @Nicholas.jacobson (2019-02-12 06:12 UTC)

<p>It appears this Add-in is not loading properly in the new build. I’m just seeing the constructor addin come though on loading. Any thoughts?</p>

---

## Post #53 by @pieper (2019-02-12 13:18 UTC)

<p>Can you look in the error log and post anything that looks related?</p>

---

## Post #54 by @Nicholas.jacobson (2019-02-14 03:56 UTC)

<p>loadSourceAsModule - Failed to load file "C:/Users/njacobson/AppData/Roaming/NA-MIC/Extensions-27931/SlicerFab/lib/Slicer-4.10/qt-scripted-modules/BitmapGenerator.py" as module "BitmapGenerator" !</p>
<p>Fail to instantiate module "BitmapGenerator"</p>

---

## Post #55 by @pieper (2019-02-14 14:50 UTC)

<p>There should be a little more info in the log file, like a python stack trace - do you see anything like that?</p>

---

## Post #56 by @Nicholas.jacobson (2019-02-14 16:02 UTC)

<p>Sure, below are all the errors I am getting, in addition to the previous one sent.</p>
<p>Stream : Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>File “C:/Users/njacobson/AppData/Roaming/NA-MIC/Extensions-27931/SlicerFab/lib/Slicer-4.10/qt-scripted-modules/BitmapGenerator.py”, line 21</p>
<p>self.parent.contributors = [“Steve Pieper (Isomics, Inc.), Steve Keating (MIT), Ahmed Hosny (Harvard), James Weaver (Harvard)”, Andras Lasso (Queens)] # replace with “Firstname Lastname (Organization)”</p>
<p>^</p>
<p>SyntaxError: invalid syntax</p>
<p>Python : Scripted subject hierarchy plugin registered: Annotations</p>
<p>Python : Scripted subject hierarchy plugin registered: SegmentEditor</p>
<p>Scripted subject hierarchy plugin registered: SegmentStatistics</p>
<p>QT : Scripted subject hierarchy plugin registered: SegmentEditor</p>
<p>Scripted subject hierarchy plugin registered: SegmentStatistics</p>

---

## Post #57 by @lassoan (2019-02-14 21:32 UTC)

<p>Probably this simple change will fix it: <a href="https://github.com/SlicerFab/SlicerFab/pull/9/files" rel="nofollow noopener">https://github.com/SlicerFab/SlicerFab/pull/9/files</a></p>

---

## Post #58 by @Nicholas.jacobson (2019-02-14 21:37 UTC)

<p>Thanks. Do I just reload this from the extension manager to try this fix?</p>

---

## Post #59 by @lassoan (2019-02-14 21:40 UTC)

<p>It’ll be in the extension manager tomorrow.</p>
<p>If you don’t want to wait then you can update BitmapGenerator.py locally (just a single-line change).</p>

---

## Post #60 by @Nicholas.jacobson (2019-02-15 15:21 UTC)

<p>That worked! Thank you.</p>

---

## Post #61 by @Chris_Rorden (2019-02-15 21:08 UTC)

<p>As an aside, there are two approaches for color 3D printing. One uses PNGs for a voxel approach. The other uses a mesh with either colored vertices or a texture map. Shapeways supports the latter approach using the archaic X3D or VRML formats. The image below shows how the mesh can incorporate color for both a statistical map as well as emphasizing ambient occlusion using a curvature map.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a40c4e5cb50f46c04a322f4b6520575b3d6533f.png" data-download-href="/uploads/short-url/3KfbfvXYRJQKl8AKFCBPWPGAUlF.png?dl=1" title="shapeways" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a40c4e5cb50f46c04a322f4b6520575b3d6533f_2_690x328.png" alt="shapeways" data-base62-sha1="3KfbfvXYRJQKl8AKFCBPWPGAUlF" width="690" height="328" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a40c4e5cb50f46c04a322f4b6520575b3d6533f_2_690x328.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a40c4e5cb50f46c04a322f4b6520575b3d6533f_2_1035x492.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a40c4e5cb50f46c04a322f4b6520575b3d6533f_2_1380x656.png 2x" data-dominant-color="F0EEF0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">shapeways</span><span class="informations">2220×1058 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #63 by @Nicholas.jacobson (2019-02-26 17:26 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a><br>
Just loaded in a .ply file and activated the scalars to show color like tractography. I see in the Models Module under Display &gt;Visibility &gt; Views there is a view tab that includes ‘bitmap generator’. See attached. However, when I run the bitmap generator script I get 2,000 png’s or a flattened image of the .ply and not slices. Any idea how to slice these .ply bundles? <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7634d07c337ffc2c35ab68ef0fd02244a5063c89.png" data-download-href="/uploads/short-url/gRHuJYPojiQVv5JBpxcSfIFGWlb.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/7634d07c337ffc2c35ab68ef0fd02244a5063c89_2_690x434.png" alt="Capture" data-base62-sha1="gRHuJYPojiQVv5JBpxcSfIFGWlb" width="690" height="434" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/7634d07c337ffc2c35ab68ef0fd02244a5063c89_2_690x434.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/7634d07c337ffc2c35ab68ef0fd02244a5063c89_2_1035x651.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7634d07c337ffc2c35ab68ef0fd02244a5063c89.png 2x" data-dominant-color="919D9D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1301×819 461 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #64 by @pieper (2019-02-26 17:54 UTC)

<p>Hi <span class="mention">@Nick</span> -</p>
<p>Right now the BitmapGenerator code only slices the volume rendering (it iterates through the volume and sets the crop bounds) so models aren’t cropped.</p>
<p>Models have a different cropping infrastructure based on the slice planes.  ou can find it further down in the Models module UI under clipping planes.  It should be possible to extend the BitmapGenerator to control these as well. It’s not on my todo list, but I could make suggestions if you wanted to try.</p>
<p>HTH,<br>
Steve</p>

---

## Post #65 by @Nicholas.jacobson (2019-02-26 18:00 UTC)

<p>Yes. This is a new course of research for us. I’d love to work on it, send any suggestions you have!</p>

---

## Post #66 by @pieper (2019-02-26 18:38 UTC)

<p>You should be able to create a clipping scenario like the one shown in the image below.  I’ve done it through the GUI here, but the same thing in python via the model display nodes, clip model node, and slice nodes using code like what’s pasted below.  This would need to be scripted and integrated with the <a href="https://github.com/SlicerFab/SlicerFab/blob/master/BitmapGenerator/BitmapGenerator.py#L313-L371">corresponding slab generation for the volume rendering</a>.</p>
<p>Cheers,<br>
Steve</p>
<pre><code class="lang-auto">m = getNode('tissue')
dn = m.GetDisplayNode()
dn.SetClipping(0)
dn.SetClipping(1)
c = getNode('*ClipModel*')
c.SetClipType(1)
c.SetClipType(0)
c.SetClipType(1)
c.SetYellowSliceClipState(1)
c.SetYellowSliceClipState(0)
c.SetYellowSliceClipState(1)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad2ae48259f7de863d1efedd08874cc531783b50.jpeg" data-download-href="/uploads/short-url/oHUuXEt5EVUguvnzL5drXZAiWxq.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad2ae48259f7de863d1efedd08874cc531783b50_2_690x480.jpeg" alt="image" data-base62-sha1="oHUuXEt5EVUguvnzL5drXZAiWxq" width="690" height="480" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad2ae48259f7de863d1efedd08874cc531783b50_2_690x480.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad2ae48259f7de863d1efedd08874cc531783b50_2_1035x720.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad2ae48259f7de863d1efedd08874cc531783b50_2_1380x960.jpeg 2x" data-dominant-color="848688"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1685×1174 397 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #67 by @JoeCrozier (2019-05-06 19:53 UTC)

<p>Sorry I hadn’t been paying attention to this thread for a few months, but I’m super happy it got made into an official extension.  To see if I can help with the dithering, I’ll share what I did code wise (in R unfortunately, not Python):</p>
<p><a href="https://drive.google.com/file/d/1Vf9S6lSo4WxeHWMLlpfMGCcPfbDceXmG/view?usp=sharing" rel="nofollow noopener">Text file with R code</a></p>
<p>In summary, it takes all the png’s in the folder, then using software from an old Amiga emulator dithers them all and spits them out as new files.<br>
I don’t remember exactly but at the time I don’t believe they had alpha channels.  I just set everything that was white to be printed in our clear material.  Don’t know if that is different now that I think you said alpha is part of the bitmap generator.</p>
<p>It still ran into the problem nicholas.jacobson mentioned of resolution being squished in the printer back when I did it, but we were able to manually fix that.</p>
<p>On that note, ive uninstalled SlIcerFab, reinstalled it through the extension manager, and i’m running 4.11, and I don’t see any of the options to specify dpi or height or anything.  Is that in the GUI or just the python code?</p>

---

## Post #68 by @pieper (2019-05-06 20:45 UTC)

<p>Hi <a class="mention" href="/u/joecrozier">@JoeCrozier</a> -  I don’t think anyone has worked on the GUI for this yet, but it’s pretty easy to edit the python code directly to match your printer parameters.</p>
<p>The R code looks fine.  Also people could look at Image Magick for dithering and other options.</p>
<p><a href="http://www.imagemagick.org/Usage/quantize/#diy_multi" class="onebox" target="_blank" rel="nofollow noopener">http://www.imagemagick.org/Usage/quantize/#diy_multi</a></p>

---

## Post #69 by @scratcher (2019-12-14 10:32 UTC)

<p>im having issues installing this extension does somebody know what im doing wrong?</p>

---

## Post #70 by @lassoan (2019-12-14 13:55 UTC)

<p>We would be happy to help. Please provide more details about what exact steps you do, what you expect to happen, and what happens instead.</p>

---

## Post #71 by @KTing (2020-03-23 19:18 UTC)

<p>Hi Nick,</p>
<p>I’m currently seeing the same issue you described above: I keep getting a stack of the same image repeated. Can you describe the steps that resolved this? I’m running the bitmap generator on just one volume. I’ve also tried converting the labelmap to a scalar volume, but am still having the same issue.</p>

---

## Post #72 by @pieper (2020-03-24 18:34 UTC)

<p>Hi -</p>
<p>I <a href="https://github.com/SlicerFab/SlicerFab/commit/c090d36f44aa562794feac12338ee8497758397c">fixed the self test</a> so if you reinstall the extension tomorrow you should be able to test it (turn on developer mode and click the reload and test button).  Or if you want to try sooner you can checkout the module and update the code manually.</p>
<p>I tested this with today’s nightly preview version on mac and it worked fine.  One thing to note is that if you are using the default settings the slices are very thin (to match the printer needing thin cuts) so you won’t see much change unless you wait quite a while.</p>

---

## Post #73 by @KTing (2020-03-25 14:04 UTC)

<p>Hi Steve,</p>
<p>Thanks for looking into this.<br>
The test passes, but the PNG’s it outputs still look the same. I’m wondering if there might be any other settings I might have set up incorrectly. I was able to use the extension previously (about a month ago) but I don’t recall doing anything differently.</p>
<p>I have been using 100 DPI, 1mm thickness, and 1.00x scale just for testing.</p>
<p>Attached: Slices 0 and 12 from the test<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/3203c02164193dd628eac88013b5007dea2744f8.jpeg" data-download-href="/uploads/short-url/78rUm0Ik2KI7xFVEDmH2LJItYcE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3203c02164193dd628eac88013b5007dea2744f8_2_689x351.jpeg" alt="image" data-base62-sha1="78rUm0Ik2KI7xFVEDmH2LJItYcE" width="689" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3203c02164193dd628eac88013b5007dea2744f8_2_689x351.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3203c02164193dd628eac88013b5007dea2744f8_2_1033x526.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/3203c02164193dd628eac88013b5007dea2744f8.jpeg 2x" data-dominant-color="B28D77"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1195×609 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #74 by @pieper (2020-03-25 14:27 UTC)

<p>Hi <a class="mention" href="/u/kting">@KTing</a> -</p>
<p>Hmm, not sure what’s different.  I just downloaded today’s Slicer preview, installed SlicerFab, clicked the Reload &amp; Test button, and everything worked.  I tested this on windows and got the images as shown below.  Is it possible you had another volume loaded before running the test?  That might interfere somehow.</p>
<p>-Steve</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6b6223f4a3c496ee0696a7a31eefc2b486254ca.jpeg" data-download-href="/uploads/short-url/uDqoHOOT7gcttnQY7FTvvCuAAZQ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6b6223f4a3c496ee0696a7a31eefc2b486254ca_2_496x500.jpeg" alt="image" data-base62-sha1="uDqoHOOT7gcttnQY7FTvvCuAAZQ" width="496" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6b6223f4a3c496ee0696a7a31eefc2b486254ca_2_496x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6b6223f4a3c496ee0696a7a31eefc2b486254ca_2_744x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6b6223f4a3c496ee0696a7a31eefc2b486254ca_2_992x1000.jpeg 2x" data-dominant-color="F9F7F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1269×1279 378 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #75 by @KTing (2020-03-25 18:11 UTC)

<p>I tried running the test on another machine, and it looks like it’s working- thanks!<br>
Not sure what the issue is on this machine though - I’m also using today’s Slicer preview.</p>
<p>Should this extension work on segmentation files? I’ve first converted them to labelmaps then to scalarVolumes, but haven’t had any luck so far, the PNG’s look like a squashed top-down view of my volume</p>

---

## Post #76 by @pieper (2020-03-25 18:33 UTC)

<aside class="quote no-group" data-username="KTing" data-post="75" data-topic="3333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/ebca7d/48.png" class="avatar"> KTing:</div>
<blockquote>
<p>I tried running the test on another machine, and it looks like it’s working- thanks!</p>
</blockquote>
</aside>
<p>Great!</p>
<aside class="quote no-group" data-username="KTing" data-post="75" data-topic="3333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/ebca7d/48.png" class="avatar"> KTing:</div>
<blockquote>
<p>Not sure what the issue is on this machine though</p>
</blockquote>
</aside>
<p>I’m not sure either.  Are there any other extensions installed?  Is there a <code>.slicerrc.py</code> file or something else that modifies the default behavior?</p>
<aside class="quote no-group" data-username="KTing" data-post="75" data-topic="3333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/ebca7d/48.png" class="avatar"> KTing:</div>
<blockquote>
<p>Should this extension work on segmentation files? I’ve first converted them to labelmaps then to scalarVolumes, but haven’t had any luck so far, the PNG’s look like a squashed top-down view of my volume</p>
</blockquote>
</aside>
<p>That should work, but I haven’t really tried.  Let us know how it goes.</p>

---

## Post #77 by @KTing (2020-03-25 18:38 UTC)

<p>Unfortunately it doesn’t look like it worked, the PNG’s just look like a top-down view of my volume</p>

---

## Post #78 by @lassoan (2020-03-25 18:52 UTC)

<aside class="quote no-group" data-username="KTing" data-post="75" data-topic="3333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/ebca7d/48.png" class="avatar"> KTing:</div>
<blockquote>
<p>Should this extension work on segmentation files?</p>
</blockquote>
</aside>
<p>Segmentations are binary files, you can print them as usual, from an STL file You can “Export to files” section in Segmentations module.</p>

---

## Post #79 by @KTing (2020-03-25 18:56 UTC)

<p>I’m actually using the extension for a different application, (not 3D printing)<br>
The application I’m working on takes a stack of PNG’s to construct a voxel object. My goal is to take my segmentation files of bone, ligament, etc. and export each of them to stacks of PNGs</p>
<p>Would there be another way I can accomplish this?</p>

---

## Post #80 by @lassoan (2020-03-25 21:09 UTC)

<p>You can use Screen Capture module to get an image stack of slice views (choose a slice view as “Master view” and use “slice sweep” animation mode).</p>

---

## Post #81 by @KTing (2020-03-27 20:15 UTC)

<p>Thanks for the suggestion!</p>

---

## Post #82 by @Nicholas.jacobson (2020-06-27 02:39 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> I’m looking for a way to register CT and MRI and use slicerfab to print both volumes at once. For Cranio Facial work we want to get high res bone and soft tissue represented in one print. The problems I’m running into is that Slicer displays multiple volumes in an unpredicatble way. I’d like to specifiy which volume takes precedence and then be able to slicerfab both of these at once. Any thoughts?</p>

---

## Post #83 by @lassoan (2020-06-27 06:10 UTC)

<p>For predictable multi-volume rendering, you need to choose “VTK multi-volume (experimental)” rendering in volume rendering module. It does not support shading (current limitation in VTK), but probably this is not be an issue for you.</p>

---

## Post #84 by @Nicholas.jacobson (2020-06-30 22:55 UTC)

<p>Thanks. When I slice this from SlicerFab I can only get one of the volumes. I see in the code on line  241 something about GetSingletonNode. Thinking this is what I can change to add both active volumes but not seeing what to change this to. Any thoughts?</p>
<p>self.threeDViewNode = slicer.mrmlScene.GetSingletonNode(“BitmapGenerator”,“vtkMRMLViewNode”)</p>

---

## Post #85 by @pieper (2020-07-07 20:53 UTC)

<p>I haven’t looked carefully in a while, but I’m pretty sure the BitmapGenerator is hard coded for just one volume, so some amount of code restructuring would be needed to support the new renderer.</p>

---

## Post #86 by @Nicholas.jacobson (2022-12-19 20:35 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/lassoan">@lassoan</a>. My cs student (gunnar) and I have been returning to the work descibed in this thread earlier.</p><aside class="quote quote-modified" data-post="66" data-topic="3333">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/export-volume-rendering-as-stack-of-pngs-not-stls/3333/66">Export Volume Rendering as stack of PNG's. NOT stl's</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You should be able to create a clipping scenario like the one shown in the image below.  I’ve done it through the GUI here, but the same thing in python via the model display nodes, clip model node, and slice nodes using code like what’s pasted below.  This would need to be scripted and integrated with the <a href="https://github.com/SlicerFab/SlicerFab/blob/master/BitmapGenerator/BitmapGenerator.py#L313-L371" rel="noopener nofollow ugc">corresponding slab generation for the volume rendering</a>. 
Cheers, 
Steve 
m = getNode('tissue')
dn = m.GetDisplayNode()
dn.SetClipping(0)
dn.SetClipping(1)
c = getNode('*ClipModel*')
c.SetClipT…
  </blockquote>
</aside>
<p>
We are working to include multiple volumes and imported models to be sliced through SlicerFab. We’ve made progress and are so close but have a few questions:</p>
<p>-Can we transfer all models into volumes to interact with the volume display node?<br>
-Should we add logic to also slice through models? If so how do we control the clipping plane through the python loadable modules? Your previous advise got use close but then we ran into uncharted territory finding the clipping plan module.<br>
-Is there a display node that can hold both Models and Volumes?</p>
<p>Any thoughts?</p>

---

## Post #87 by @pieper (2022-12-19 21:06 UTC)

<p>Hi <a class="mention" href="/u/nicholas.jacobson">@Nicholas.jacobson</a> -</p>
<aside class="quote no-group" data-username="Nicholas.jacobson" data-post="86" data-topic="3333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/ba8739/48.png" class="avatar"> Nicholas.jacobson:</div>
<blockquote>
<p>-Can we transfer all models into volumes to interact with the volume display node?</p>
</blockquote>
</aside>
<p>I haven’t tried, but I’d say it depends on exactly what kind of models and what you want them to look like.  You can load most models as segmentations, and then export them as labelmaps (Segmentations module) and convert those to scalar volumes (Volumes module).  this would make them uniform slabs at each slice.  If they are made different colors (different transfer functions) they could work with the multivolume renderer with the bitmap generator approach.  This would be a very general solution I think.</p>
<aside class="quote no-group" data-username="Nicholas.jacobson" data-post="86" data-topic="3333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/ba8739/48.png" class="avatar"> Nicholas.jacobson:</div>
<blockquote>
<p>Should we add logic to also slice through models? If so how do we control the clipping plane through the python loadable modules?</p>
</blockquote>
</aside>
<p>As you can see in one of the screenshots above you can clip a slice through a model, but the interior is hollow and this may not be what you want.  Better to do the multivolume approach I think.</p>
<aside class="quote no-group" data-username="Nicholas.jacobson" data-post="86" data-topic="3333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/ba8739/48.png" class="avatar"> Nicholas.jacobson:</div>
<blockquote>
<p>-Is there a display node that can hold both Models and Volumes?</p>
</blockquote>
</aside>
<p>No, these are distinct at the level we are discussing here.</p>
<p>If you have a specific example of a scene you are trying to print maybe we can give other suggestions.</p>

---

## Post #88 by @Gunnar_Enserro (2023-01-12 17:04 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> -<br>
I am Nicks student working on getting this bitmap Generator working. I been hitting my head against the wall trying to figure out the right method for turning a model into a volume, here are the lines of code I have written in an attempt to do so:</p>
<pre><code class="lang-auto">self.delayDisplay('0')
modelNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLModelNode")

referenceVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
# Convert model to labelmap
seg = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
seg.SetReferenceImageGeometryParameterFromVolumeNode(referenceVolumeNode)
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(modelNode, seg)
# seg.CreateBinaryLabelmapRepresentation()
outputLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(seg, outputLabelmapVolumeNode, referenceVolumeNode)

slicer.modules.volumes.logic().CreateScalarVolumeFromVolume(slicer.mrmlScene, referenceVolumeNode, outputLabelmapVolumeNode)

slicer.mrmlScene.RemoveNode(outputLabelmapVolumeNode)
</code></pre>
<p>If you see anything wrong or know of a better way, please let me know.</p>

---

## Post #89 by @pieper (2023-01-12 17:57 UTC)

<aside class="quote no-group" data-username="Gunnar_Enserro" data-post="88" data-topic="3333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gunnar_enserro/48/18000_2.png" class="avatar"> Gunnar_Enserro:</div>
<blockquote>
<pre><code class="lang-auto">referenceVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
</code></pre>
</blockquote>
</aside>
<p>This creates an empty volume node, but what you need is a reference volume that defines the geometry of the grid that you want to use to sample the STL model (e.g. the orientation, spacing, and dimensions of the resulting image data).  You can either load an existing volume, or specify one programmatically <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-a-new-volume">like this</a>.  Otherwise I think the code should work.</p>

---

## Post #90 by @Gunnar_Enserro (2023-01-27 22:34 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>-<br>
I have gone down a few rabbit hole and was looking if you have any advices, I was successfully able to turn a model into a segmentation into a scalar volume. I was wondering with this tool is there a programmatic way to merge all visible volumes into one volume and process that one volume through the bit map generator.</p>
<p>Thank you ahead of time</p>

---

## Post #91 by @pieper (2023-01-28 18:37 UTC)

<p>Yes, if you have the files as vtkImageData and they are the same geometry you can use vtkImageBlend or vtkImageMathematics to generate composite outputs.  If they are different geometry you can make MRML nodes for them and use Slicer’s CLIs either to resample them, or do do math like add, mask, multiply etc.  Hope that’s clear - if not can describe how you envision the result when you merge the volumes and maybe we can give more specific advice.</p>

---
