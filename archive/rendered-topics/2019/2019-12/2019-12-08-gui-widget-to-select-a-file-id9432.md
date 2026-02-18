# GUI widget to select a file

**Topic ID**: 9432
**Date**: 2019-12-08
**URL**: https://discourse.slicer.org/t/gui-widget-to-select-a-file/9432

---

## Post #1 by @Rebecca_Kincaid (2019-12-08 14:38 UTC)

<p>I am creating a module where I need to import an H5 file, process it and then display it to the output node. How do I get the option to view a dialogue box so that I can select a file?</p>
<p>I found an example in the SlicerITKUltrasound, ScanConvertSliceSeries module, But could not understand how to script it in python.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/0739d5ae22cbef62c9617a1df31c3980aed40580.png" alt="Slicer" data-base62-sha1="11VfELHEmATOF7UUWp8ceOcQJCU" width="602" height="339"></p>

---

## Post #2 by @lassoan (2019-12-08 14:56 UTC)

<p>That is the ctkPathLineEdit widget. See a gallery of more CTK widgets <a href="http://www.commontk.org/index.php/Documentation/ImageGallery">here</a>. If you use <code>scripteddesigner</code> template when you create your scripted module then you can use Qt designer to create your GUI. All the available widgets are shown there and you can simply drag-and-drop them to your module GUI:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecdf630cfb982bd59d1145fd0f94332785d42326.png" data-download-href="/uploads/short-url/xNthOkMulXPMveG9TCgocamkaHk.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecdf630cfb982bd59d1145fd0f94332785d42326_2_690x437.png" alt="image" data-base62-sha1="xNthOkMulXPMveG9TCgocamkaHk" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecdf630cfb982bd59d1145fd0f94332785d42326_2_690x437.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecdf630cfb982bd59d1145fd0f94332785d42326_2_1035x655.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecdf630cfb982bd59d1145fd0f94332785d42326_2_1380x874.png 2x" data-dominant-color="E1DDDD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1677×1064 217 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>See step-by-step tutorial <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">here</a>.</p>

---

## Post #3 by @Saima (2020-04-03 06:16 UTC)

<p>Hi Andras,<br>
I am using scripteddesigner. I can drag and drop and create easily the designer but how can i connect the components in the script. for example if I added ctkpathlineedit. how can i add it in the script and how can i use it.<br>
self.ui.pathLineEdit…</p>
<p>I now how to use the other filters the input mrmrl selector and buttons but i am unable to see how to use this one.</p>
<p>Thank you in advance.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #4 by @Saima (2020-04-07 06:51 UTC)

<aside class="quote no-group" data-username="Rebecca_Kincaid" data-post="1" data-topic="9432">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rebecca_kincaid/48/5354_2.png" class="avatar"> Rebecca_Kincaid:</div>
<blockquote>
<p>SlicerITKUltrasound,</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
I added the ctk widgets(collapsible button and pathlineedit)  using qt designer but when I load the example in 3d slicer. it doesnt show me pathlineedit inside the ctk collapsible button. It only shows ctkcollapsible buttons.</p>
<p>If I use below lines it will create new collapsible buttons and pathline edits but I want to use the pathline edit created from the qt designer.<br>
parametersCollapsibleButton = ctk.ctkCollapsibleButton()<br>
parametersCollapsibleButton.text = “Parameters”<br>
self.layout.addWidget(parametersCollapsibleButton)</p>
<pre><code># Layout within the dummy collapsible button
parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)

self.inputDirSelector = ctk.ctkPathLineEdit()
self.inputDirSelector.filters = ctk.ctkPathLineEdit.Dirs
self.inputDirSelector.settingKey = 'DICOMPatcherInputDir'
parametersFormLayout.addRow("Input DICOM directory:", self.inputDirSelector)
</code></pre>
<p>Thank you</p>
<p>Reagrds,<br>
Saima Safdar</p>

---

## Post #5 by @lassoan (2020-04-07 23:51 UTC)

<p>Without seeing your .ui file I can only guess. After you drag-and-drop a widget into a collapsible button, you need to set the layout for the collapsible button. Maybe you have missed that step.</p>
<p>If you can send a link to your module then I can have a look.</p>

---

## Post #6 by @Saima (2020-04-08 06:09 UTC)

<p>Hi Andras,<br>
I am sending the link to the module. I added model collapsible button using qt designer and the checkbox as well when I open module in slicer it doesnt show me the content inside collapsible button.<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cloudstor.aarnet.edu.au/plus/3rdparty-apps/cloudstortheme/core/img/favicon.ico" class="site-icon" width="32" height="32">
      <a href="https://cloudstor.aarnet.edu.au/plus/s/oR4wB04bTM9oTkv" target="_blank" rel="nofollow noopener">CloudStor</a>
  </header>
  <article class="onebox-body">
    <img src="https://cloudstor.aarnet.edu.au/plus/3rdparty-apps/cloudstortheme/core/img/favicon-fb.png" class="thumbnail onebox-avatar" width="128" height="128">

<h3><a href="https://cloudstor.aarnet.edu.au/plus/s/oR4wB04bTM9oTkv" target="_blank" rel="nofollow noopener">CloudStor - CloudStor is powered by AARNet</a></h3>

<p>MTLEDSimulator.zip is publicly shared</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #7 by @lassoan (2020-04-08 21:28 UTC)

<p>Everything looks good to me:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a482a3500814516861d41bc55512be28f9f592c.png" data-download-href="/uploads/short-url/aB7WBSek0AK8xH4FxszZiT3PKjy.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a482a3500814516861d41bc55512be28f9f592c_2_690x441.png" alt="image" data-base62-sha1="aB7WBSek0AK8xH4FxszZiT3PKjy" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a482a3500814516861d41bc55512be28f9f592c_2_690x441.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a482a3500814516861d41bc55512be28f9f592c_2_1035x661.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a482a3500814516861d41bc55512be28f9f592c_2_1380x882.png 2x" data-dominant-color="A8A7AB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 218 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If I drag-and-drop a ctkPathLineEdit widget to the GUI layout in QtDesigner and click Reload in Slicer then the widget shows up correctly in the module GUI in Slicer.</p>
<p>I would recommend to remove code from the .py file that creates widgets and instead add all widgets to the .ui file.</p>

---

## Post #8 by @Saima (2020-04-16 06:36 UTC)

<p>Yes it worked now. Do we need the vertical height of collapsible to be fixed.</p>

---
