# Label Selection

**Topic ID**: 591
**Date**: 2017-06-28
**URL**: https://discourse.slicer.org/t/label-selection/591

---

## Post #1 by @LGG (2017-06-28 15:37 UTC)

<p>Hi everyone,</p>
<p>in Slicer 4.6.2 I can not find Fiber bundle label select in the Module-list. Since I want to do tractography between two labels or a label and a model I wanted to ask how I know the number of the label I want to use? (to type in in when Using Tractography ROI Selection in “inclusion labels”) So far I wasn’t able to visualize fibers between two labels that are not in drawn in the same MRI-image.</p>
<p>Thanks!</p>
<p>Operating system: MacOs Sierra 10.12.5<br>
Slicer version: 4.6.2</p>

---

## Post #2 by @ihnorton (2017-06-28 15:43 UTC)

<p>Please use the Slicer nightly build, and install SlicerDMRI: <a href="http://dmri.slicer.org/download/">http://dmri.slicer.org/download/</a></p>

---

## Post #3 by @ihnorton (2017-06-28 18:47 UTC)

<p>Also, I should add (thanks <a class="mention" href="/u/ljod">@ljod</a>), that the module can be found as below after SlicerDMRI is installed:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be477510e81b131cd0d72e985b327c9ed2013753.png" data-download-href="/uploads/short-url/r9hOAoUVjBVEqAIyLjPsXSl6x6X.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be477510e81b131cd0d72e985b327c9ed2013753_2_690x158.png" alt="image" data-base62-sha1="r9hOAoUVjBVEqAIyLjPsXSl6x6X" width="690" height="158" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be477510e81b131cd0d72e985b327c9ed2013753_2_690x158.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be477510e81b131cd0d72e985b327c9ed2013753.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be477510e81b131cd0d72e985b327c9ed2013753.png 2x" data-dominant-color="9FA1A3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">708×163 27.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @LGG (2017-06-30 11:29 UTC)

<p>Thanks Isaiah!</p>
<p>I wasn’t aware that Tractography ROI Selection is the same as Fiber bundle label select…<br>
Now I am still not sure which numbers to give the software (in “inclusion labels”) to be sure that it takes the labels I want it to track in between - it is a number refering to a certain labelmap, not an amount of labels, right? And does it only work with labelmaps or also with models?</p>
<p>Sorry for the many questions!</p>
<p>Lioba</p>

---

## Post #5 by @ihnorton (2017-06-30 13:27 UTC)

<aside class="quote no-group" data-username="LGG" data-post="4" data-topic="591">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/ea666f/48.png" class="avatar"> LGG:</div>
<blockquote>
<p>it is a number refering to a certain labelmap</p>
</blockquote>
</aside>
<p>It’s referring to the highlighted value in the given labelmap.</p>
<aside class="quote no-group" data-username="LGG" data-post="4" data-topic="591">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/ea666f/48.png" class="avatar"> LGG:</div>
<blockquote>
<p>And does it only work with labelmaps or also with models?</p>
</blockquote>
</aside>
<p>Only labelmaps, but you can create one from a model with “Model to Label Map” module.</p>

---

## Post #6 by @LGG (2017-08-23 14:04 UTC)

<p>Hi Isaiah,</p>
<p>sorry, I still don’t understand where to find the number or given value of a labelmap. I thought it to be the number behind the “node_ _” when opening the node inspector because I can’t find any highlighted value.</p>
<p>What I would like to do is to extract trackts from a whole brain tractography through a model or labelmap I created using module Tractography ROI selection. But whatever number I try, no fiber is being tracked.</p>
<p>Also what confuses me - the “selection region label map” is the labelmap I would like to track through, no? Why do I still have to select inclusion labels?</p>
<p>And my last question concerns the “model to labelmap” module: This won’t work with the model I created. In the Slicer module explanation I read it would only work for surface models, may this be the reason?</p>
<p>Thanks!<br>
Lioba</p>

---
