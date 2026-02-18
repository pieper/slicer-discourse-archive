# Restore visual properties of models when registered as Sample Data

**Topic ID**: 21654
**Date**: 2022-01-27
**URL**: https://discourse.slicer.org/t/restore-visual-properties-of-models-when-registered-as-sample-data/21654

---

## Post #1 by @RafaelPalomar (2022-01-27 14:44 UTC)

<p>I’m using <code>SampleData</code> to register sample data to be used in Slicer-Liver. Part of that data is 3D models, which don’t preserve the visual properties when saved as <code>.vtk</code> models. Is there anyway to set up the visual properties of these models automatically when they are loaded again? Thanks!</p>

---

## Post #2 by @lassoan (2022-01-27 14:48 UTC)

<p>You can use an .mrb file as sample data, which contains the VTK models and all the display properties. If you want you can keep only the model, storage, and display node in the .mrml file (in the mrb zip file) and remove everything else (such as layout node, slice nodes, etc. that would update a bunch of other things when the mrb file is loaded).</p>

---

## Post #3 by @RafaelPalomar (2022-01-27 14:51 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>. I wonder if it would be an option to add a new parameter in <code>SampleData.SampleDataLogic.registerCustomSampleDataSource</code> with a list of setup functions to be called after the data is loaded.</p>

---

## Post #4 by @lassoan (2022-01-27 14:55 UTC)

<p>See example in SampleData.py:</p>
<pre><code class="lang-auto">    filePaths = logic.downloadFromSource(SampleDataSource(
      uris=TESTING_DATA_URL + 'SHA256/5a1c78c3347f77970b1a29e718bfa10e5376214692d55a7320af94b9d8d592b8',
      loadFiles=True, fileNames='slicer4minute.mrb'))
</code></pre>
<p>You need to set <code>loadFiles=True</code> to load the .mrb file (by default it is only downloaded).</p>
<aside class="quote no-group" data-username="RafaelPalomar" data-post="3" data-topic="21654">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>I wonder if it would be an option to add a new parameter in <code>SampleData.SampleDataLogic.registerCustomSampleDataSource</code> with a list of setup functions to be called after the data is loaded.</p>
</blockquote>
</aside>
<p>You can do this by specifying a custom loader function. I would not recommend to use it for modifying the loaded data, setting display properties, etc., as it would make the result hard to reproduce. The outcome would depend on both the data on the server and the loading script: two different locations, two different ways of specifying data.</p>

---

## Post #5 by @RafaelPalomar (2022-01-27 14:56 UTC)

<p>I see. Thanks a lot <a class="mention" href="/u/lassoan">@lassoan</a>!</p>

---
