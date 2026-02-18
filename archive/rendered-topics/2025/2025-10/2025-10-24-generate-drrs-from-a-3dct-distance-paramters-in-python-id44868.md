# Generate DRRs from a 3DCT. Distance paramters in Python

**Topic ID**: 44868
**Date**: 2025-10-24
**URL**: https://discourse.slicer.org/t/generate-drrs-from-a-3dct-distance-paramters-in-python/44868

---

## Post #1 by @ruju (2025-10-24 12:54 UTC)

<p>Hi,</p>
<p>I have another question about the computation of DRRs in 3D slicer. In the GUI of the DRR Image Computation module I can change the isocenter to imager distance. Is it also possible to modify this parameter in a Python script? I haven’t found any command that works in 3D Slicer 5.8.1 so far.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @Mik (2025-10-24 14:22 UTC)

<p>That`s the DrrImageCompulationNode  parameter:</p>
<p>Examples:</p>
<pre><code class="lang-auto"># DRR image in isocenter plan
# Set isocenter imager distance == 0 mm
rtImageParameters.SetIsocenterImagerDistance(0)
</code></pre>
<pre><code class="lang-auto"># Set isocenter imager distance == 350 mm
rtImageParameters.SetIsocenterImagerDistance(350)
</code></pre>
<p>You should see how images markups change their position as well.</p>

---

## Post #3 by @lassoan (2025-10-25 14:00 UTC)

<p>Note that if you work with C-arms (not with the EPID of a linear accelerator) then there is a new “Virtual Cath Lab” module in SlicerHeart extension that provides lots of features, including realistic 3D model of the C-arm (mono or biplane), fluoro image simulation, virtual contrast filling, device simulation, time sequences, etc.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.linkedin.com/posts/jolleylab_congratulations-yuval-barak-corren-matt-activity-7376724043884023808-2Cxa?utm_source=social_share_send&amp;utm_medium=android_app&amp;rcm=ACoAAANbVMYBr7veNR93l1nczCWzGqteluxucc8&amp;utm_campaign=copy_link">
  <header class="source">
      <img src="https://static.licdn.com/aero-v1/sc/h/al2o9zrvru7aqj8e1x2rzsrca" class="site-icon" alt="" width="64" height="64">

      <a href="https://www.linkedin.com/posts/jolleylab_congratulations-yuval-barak-corren-matt-activity-7376724043884023808-2Cxa?utm_source=social_share_send&amp;utm_medium=android_app&amp;rcm=ACoAAANbVMYBr7veNR93l1nczCWzGqteluxucc8&amp;utm_campaign=copy_link" target="_blank" rel="noopener">linkedin.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/388;"><img src="https://dms.licdn.com/playlist/vid/v2/D4E05AQG-gBqOIt32jg/thumbnail-with-play-button-overlay-high/B4EZl9jWcSKUDk-/0/1758748049506?e=2147483647&amp;v=beta&amp;t=hFXYaqosut_iuU5zfJcsN4r8m4M1KkS5kHljsQL0DdU" class="thumbnail" alt="" width="690" height="388"></div>

<h3><a href="https://www.linkedin.com/posts/jolleylab_congratulations-yuval-barak-corren-matt-activity-7376724043884023808-2Cxa?utm_source=social_share_send&amp;utm_medium=android_app&amp;rcm=ACoAAANbVMYBr7veNR93l1nczCWzGqteluxucc8&amp;utm_campaign=copy_link" target="_blank" rel="noopener">SlicerHeart Virtual Cath Lab: A New Tool for Cardiology Training | Jolley Lab...</a></h3>

  <p>Congratulations Yuval Barak-Corren, Matt Daemer, Andras Lasso, Kyle Sunderland and team on the their publication in the Journal for the Society for Cardiovascular Angiography &amp; Interventions describing the SlicerHeart Virtual Cath...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
