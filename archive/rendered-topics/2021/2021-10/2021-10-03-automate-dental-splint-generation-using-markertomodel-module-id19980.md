---
topic_id: 19980
title: "Automate Dental Splint Generation Using Markertomodel Module"
date: 2021-10-03
url: https://discourse.slicer.org/t/19980
---

# Automate Dental Splint Generation using MarkerToModel Module

**Topic ID**: 19980
**Date**: 2021-10-03
**URL**: https://discourse.slicer.org/t/automate-dental-splint-generation-using-markertomodel-module/19980

---

## Post #1 by @Fluvio_Lobo (2021-10-03 22:50 UTC)

<p>Hello,</p>
<p>I am using <strong>Fiducials</strong> and the <strong>MarkupToModel</strong> module to generate an orthognathic splint from the position of the upper and lower dental landmarks in both the intermediate and final occlusions. I am getting pretty good results and would like to explore automating the process through Python scripting.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3c6e8c8971ec9b5c70b5d3a2055fb500efe616c.jpeg" data-download-href="/uploads/short-url/udsUgq5U2wYnvQSLvhfBdUhlbFG.jpeg?dl=1" title="slicer_splint_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3c6e8c8971ec9b5c70b5d3a2055fb500efe616c_2_345x237.jpeg" alt="slicer_splint_2" data-base62-sha1="udsUgq5U2wYnvQSLvhfBdUhlbFG" width="345" height="237" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3c6e8c8971ec9b5c70b5d3a2055fb500efe616c_2_345x237.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3c6e8c8971ec9b5c70b5d3a2055fb500efe616c_2_517x355.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3c6e8c8971ec9b5c70b5d3a2055fb500efe616c_2_690x474.jpeg 2x" data-dominant-color="262421"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_splint_2</span><span class="informations">1297×894 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Currently, <em>I start by combining upper and lower dental landmarks</em> in a single <strong>Fiducial List</strong>;<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9ce2a8aea07fbe321c5193f8180ce2ccebe1d57.jpeg" data-download-href="/uploads/short-url/zDSB98d4B0N0JTqw4K0U61zF0NN.jpeg?dl=1" title="dental_landmarks" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9ce2a8aea07fbe321c5193f8180ce2ccebe1d57_2_345x237.jpeg" alt="dental_landmarks" data-base62-sha1="zDSB98d4B0N0JTqw4K0U61zF0NN" width="345" height="237" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9ce2a8aea07fbe321c5193f8180ce2ccebe1d57_2_345x237.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9ce2a8aea07fbe321c5193f8180ce2ccebe1d57_2_517x355.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9ce2a8aea07fbe321c5193f8180ce2ccebe1d57_2_690x474.jpeg 2x" data-dominant-color="2A2619"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dental_landmarks</span><span class="informations">1297×894 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<em>Figure: Dental landmarks in green, only the lower teeth are shown</em></p>
<p>Using the <strong>Fiducial List</strong> as an Input to the <strong>MarkupToModel</strong> module, I create a “tube” using the parameters shown on the screenshot below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/202c611f1638119ed4f874b379b14b22079f397c.jpeg" data-download-href="/uploads/short-url/4ACmpmYTYyf1kUP5iwoyA2OwGAY.jpeg?dl=1" title="markup_to_model_screenshot.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/202c611f1638119ed4f874b379b14b22079f397c_2_690x373.jpeg" alt="markup_to_model_screenshot.PNG" data-base62-sha1="4ACmpmYTYyf1kUP5iwoyA2OwGAY" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/202c611f1638119ed4f874b379b14b22079f397c_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/202c611f1638119ed4f874b379b14b22079f397c_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/202c611f1638119ed4f874b379b14b22079f397c_2_1380x746.jpeg 2x" data-dominant-color="35312E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">markup_to_model_screenshot.PNG</span><span class="informations">1920×1040 321 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><strong>Is there a way to interact with the MarkupToModel module programmatically using Python?</strong> I briefly scanned the GitHub repo. and only found C++ code… Essentially, I just want to apply the parameters to every case.</p>

---

## Post #2 by @Fluvio_Lobo (2021-10-04 03:14 UTC)

<p>I did not know how to interact with <code>loadable modules</code> until I found <a href="https://discourse.slicer.org/t/create-axes-model-using-createmodels-cli/674/2">this post</a>.<br>
To replicate the parameters above, I just need to use the logic;</p>
<pre><code class="lang-auto">logic = slicer.modules.markerstomodel.logic()
logic.UpdateOutputCurveModel(fidNode,modelNode,3,False,4,8,5,True,1,1,slicer.vtkCurveGenerator(),1,0.5,3)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cfa4c2276ed6cf729baebd9ab75d902f17dc72e.jpeg" data-download-href="/uploads/short-url/k796xOxxfGRSe9UjWYgPYcVTDbg.jpeg?dl=1" title="automated_splint" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8cfa4c2276ed6cf729baebd9ab75d902f17dc72e_2_517x282.jpeg" alt="automated_splint" data-base62-sha1="k796xOxxfGRSe9UjWYgPYcVTDbg" width="517" height="282" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8cfa4c2276ed6cf729baebd9ab75d902f17dc72e_2_517x282.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8cfa4c2276ed6cf729baebd9ab75d902f17dc72e_2_775x423.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8cfa4c2276ed6cf729baebd9ab75d902f17dc72e_2_1034x564.jpeg 2x" data-dominant-color="261E1B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">automated_splint</span><span class="informations">1216×665 94.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @manjula (2023-09-14 15:03 UTC)

<p>Hi <a class="mention" href="/u/fluvio_lobo">@Fluvio_Lobo</a> ,</p>
<p>Can you please explain how you do this ? how do you make the thickness and how do you substract the occlusion ? do you use the model to substract the teeth from the tube or ?</p>
<p>if you can let me know your work flow it would be great.</p>
<p>thank you</p>

---
