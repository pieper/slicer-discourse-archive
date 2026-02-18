# Loading Colour Table alongside 3D Models

**Topic ID**: 16020
**Date**: 2021-02-17
**URL**: https://discourse.slicer.org/t/loading-colour-table-alongside-3d-models/16020

---

## Post #1 by @karinak (2021-02-17 00:29 UTC)

<p>Hello,</p>
<p>I am currently trying to load 3D models of individual segments (liver, left kidney, right kidney etc) into Slicer but I am losing their original colour attributes. I see that there is an option to load a colour table under the Model module but I cannot currently access it. Is there any other way that I can manually load a colour table into Slicer while my models are loading or is this something I would possibly need to script?</p>

---

## Post #2 by @lassoan (2021-02-17 00:54 UTC)

<aside class="quote no-group" data-username="karinak" data-post="1" data-topic="16020">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/9d8465/48.png" class="avatar"> karinak:</div>
<blockquote>
<p>Is there any other way that I can manually load a colour table into Slicer while my models are loading or is this something I would possibly need to script?</p>
</blockquote>
</aside>
<p>Color table is for coloring scalars (data associated with mesh points or cells). If you want to change the overall color of a model then you don’t need color files - the color is stored in the display node associated with the model node. You can set color of a model after loading (<code>modelNode.GetDisplayNode().SetColor(1,0,0)</code>) but if you want to preserve colors then the simplest is to save the scene file and load the models using that scene file.</p>
<p>You can also save segmentations along with colors (and standard DICOM terminology to identify segment content) in private fields by setting master representation in Segmentations module to “Closed surface”.</p>
<p>What is the overall goal of your project? What is your current processing workflow? Why are you considering loading individual segments manually instead of loading via a scene file?</p>

---

## Post #3 by @karinak (2021-02-17 19:34 UTC)

<p>Hi Andras,</p>
<p>I followed your advice and saved it as a scene file and loaded that back into Slicer and it worked. The colours were maintained and we’re able to select which segmented parts we want to view. Thank you again for your help!</p>

---
