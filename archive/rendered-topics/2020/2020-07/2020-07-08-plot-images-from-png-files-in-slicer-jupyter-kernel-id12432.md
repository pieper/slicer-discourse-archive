# Plot images from PNG files in slicer jupyter kernel

**Topic ID**: 12432
**Date**: 2020-07-08
**URL**: https://discourse.slicer.org/t/plot-images-from-png-files-in-slicer-jupyter-kernel/12432

---

## Post #1 by @BennetMontgomery (2020-07-08 01:50 UTC)

<p>I have a Jupyter Notebook that uses a Slicer kernel and I would like to plot a variable number of captures of the 3D view in the notebook, each view captured from different scenes loaded sequentially. The way I have it set up now is the notebook takes shots of the 3D view and writes them to png files, and I would like to load the png files into the notebook and plot them in a table.</p>
<p>I’ve tried matplotlib and ipyplot, but they don’t work with a slicer kernel in jupyter notebooks. The most potentially useful resource I’ve found is the <a href="https://github.com/Slicer/SlicerJupyter/" rel="nofollow noopener">Slicer Jupyter</a> library, but I don’t see any way to use it to load and plot png files. Is anyone aware of a way to plot png files in jupyter notebooks using a slicer kernel?</p>

---

## Post #2 by @lassoan (2020-07-08 13:00 UTC)

<aside class="quote no-group" data-username="BennetMontgomery" data-post="1" data-topic="12432">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/c2a13f/48.png" class="avatar"> BennetMontgomery:</div>
<blockquote>
<p>The way I have it set up now is the notebook takes shots of the 3D view and writes them to png files, and I would like to load the png files into the notebook and plot them in a table.</p>
</blockquote>
</aside>
<p>This is already implemented with a one-liner for slice views:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ebd0806a2c45e8d24622965cfbfd8855bdde06d.jpeg" data-download-href="/uploads/short-url/beyeUteiRgWZS9iWU8G4uovic1v.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ebd0806a2c45e8d24622965cfbfd8855bdde06d_2_690x358.jpeg" alt="image" data-base62-sha1="beyeUteiRgWZS9iWU8G4uovic1v" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ebd0806a2c45e8d24622965cfbfd8855bdde06d_2_690x358.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ebd0806a2c45e8d24622965cfbfd8855bdde06d_2_1035x537.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ebd0806a2c45e8d24622965cfbfd8855bdde06d_2_1380x716.jpeg 2x" data-dominant-color="2E2E2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1463×760 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>By changing a few lines in <a href="https://github.com/Slicer/SlicerJupyter/blob/beafcb192bc44ccc88e0c2c478df89fefcd43537/JupyterNotebooks/JupyterNotebooksLib/display.py#L236-L283">ViewLightboxDisplay script</a> (essentially, replace <code>screenCaptureLogic.captureSliceSweep</code> by <a href="https://github.com/Slicer/Slicer/blob/0bc7cb16bd6cb9cdad7e589f44442e9bf7d0ee79/Modules/Scripted/ScreenCapture/ScreenCapture.py#L1214-L1215"><code>screenCaptureLogic.capture3dViewRotation</code></a>, you can create a table showing 3D view in different orientations. I’ve created this using Screen Capture module GUI, you can play a bit with the GUI, too to get to know a bit better what the module can do:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/443f476b175b5dd20cfc4bec01878f6563d4f4a1.jpeg" data-download-href="/uploads/short-url/9JK2DESCDopbk82riVuCFY3002R.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/443f476b175b5dd20cfc4bec01878f6563d4f4a1_2_690x427.jpeg" alt="image" data-base62-sha1="9JK2DESCDopbk82riVuCFY3002R" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/443f476b175b5dd20cfc4bec01878f6563d4f4a1_2_690x427.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/443f476b175b5dd20cfc4bec01878f6563d4f4a1.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/443f476b175b5dd20cfc4bec01878f6563d4f4a1.jpeg 2x" data-dominant-color="412819"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">800×496 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Finally, here is an example of a script creating some data augmentation for training data and generation of an overview image of all data sets:</p>
<aside class="quote quote-modified" data-post="8" data-topic="11810">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/generating-augmented-training-data-from-nrrd-file-using-random-translations-rotations-and-deformations/11810/8">Generating augmented training data from nrrd file using random translations, rotations, and deformations</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I’ve updated the volume augmentation script to apply random translations and rotations in addition to the random deformations, and to also take screenshots so that you can get a quick overview of how the augmented data looks like. 
Gallery of example output: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/997a93c14e8d46858b371c0bb1ce5d88c278940b.jpeg" data-download-href="/uploads/short-url/lTJFKml7VlX5O7UgDfcVrHSJzaX.jpeg?dl=1" title="image">[image]</a> 
Script that generated it:
  </blockquote>
</aside>


---

## Post #3 by @BennetMontgomery (2020-07-08 23:02 UTC)

<p>Thanks for the help but unfortunately, this doesn’t solve my problem. Let me just clarify what I’m trying to accomplish:</p>
<p>I’m loading mrb scenes into the jupyter managed slicer, constructing a volume, rendering the volume, and then capturing a screenshot of the 3D view for display. The number of scenes is variable and I would like for the user of the notebook to load as many scenes as they like. At present, I have a cell that allows the user to input paths to mrb scenes to load into the notebook:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfc512ff2eb3a2d6e413a253f639bdc74bc461be.png" data-download-href="/uploads/short-url/tE145pcqCYgEq9DfGQk64dNB55I.png?dl=1" title="Screenshot_20200708_165321" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfc512ff2eb3a2d6e413a253f639bdc74bc461be_2_690x190.png" alt="Screenshot_20200708_165321" data-base62-sha1="tE145pcqCYgEq9DfGQk64dNB55I" width="690" height="190" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfc512ff2eb3a2d6e413a253f639bdc74bc461be_2_690x190.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfc512ff2eb3a2d6e413a253f639bdc74bc461be.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfc512ff2eb3a2d6e413a253f639bdc74bc461be.png 2x" data-dominant-color="F2F0EE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20200708_165321</span><span class="informations">954×264 68.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Later on, I use a for loop to load one of the scenes, do the processing, capture the 3d view, and repeat until all scenes have been processed:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d9bb93c09d58c0efa88f652e616e439f465d7d7.png" data-download-href="/uploads/short-url/1WnQhLmVrBRQEg4Smn6bXXdSGG3.png?dl=1" title="Screenshot_20200708_172201" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d9bb93c09d58c0efa88f652e616e439f465d7d7_2_690x302.png" alt="Screenshot_20200708_172201" data-base62-sha1="1WnQhLmVrBRQEg4Smn6bXXdSGG3" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d9bb93c09d58c0efa88f652e616e439f465d7d7_2_690x302.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d9bb93c09d58c0efa88f652e616e439f465d7d7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d9bb93c09d58c0efa88f652e616e439f465d7d7.png 2x" data-dominant-color="F0F2EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20200708_172201</span><span class="informations">952×417 56.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In that cell I try using the lightbox display, but neither it nor the view3ddisplay() method seem to work when embedded in for loops as both give an identical result:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a4bb4861c9ac69d413a87be744698aed55f6114.png" data-download-href="/uploads/short-url/jJq5ucT4qmLD2etwDK8NywTrQji.png?dl=1" title="Screenshot_20200708_172314" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a4bb4861c9ac69d413a87be744698aed55f6114_2_690x191.png" alt="Screenshot_20200708_172314" data-base62-sha1="jJq5ucT4qmLD2etwDK8NywTrQji" width="690" height="191" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a4bb4861c9ac69d413a87be744698aed55f6114_2_690x191.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a4bb4861c9ac69d413a87be744698aed55f6114.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a4bb4861c9ac69d413a87be744698aed55f6114.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20200708_172314</span><span class="informations">870×242 65.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Everything works fine but no images are displayed in the notebook. The view3ddisplay() method works when not embedded in a for loop but I don’t see a way to retain a theoretically limitless number of scenes to test on without it. As I see it, my only option is to get rid of the for loop and abandon being able to load a limitless number of scenes but I would really like to avoid that if at all possible.</p>
<p>Thanks!</p>

---

## Post #4 by @lassoan (2020-07-09 00:49 UTC)

<p>Jupyter notebook shows only the last result. If you want to show multiple results then you need to put each result that you want to display as input argument of <code>display()</code> function.</p>
<p>For example, if you want to display 3 slice views in a for loop:</p>
<p>This only displays the last one:</p>
<pre><code class="lang-python">for layout in ["OneUpRedSlice", "OneUpYellowSlice", "OneUpGreenSlice"]:
    slicernb.ViewDisplay(layout) # wrong!
</code></pre>
<p>This shows all 3 views:</p>
<pre><code class="lang-python">for layout in ["OneUpRedSlice", "OneUpYellowSlice", "OneUpGreenSlice"]:
    display(slicernb.ViewDisplay(layout))
</code></pre>

---

## Post #5 by @BennetMontgomery (2020-07-09 02:50 UTC)

<p>Thanks, that works perfectly!</p>

---
