# Extract Centerline computational troubleshooting

**Topic ID**: 45322
**Date**: 2025-12-02
**URL**: https://discourse.slicer.org/t/extract-centerline-computational-troubleshooting/45322

---

## Post #1 by @Stephanie_Baumgart (2025-12-02 14:51 UTC)

<p>I was trying to use Extract Centerline to generate a centerline tree of what I think is a relatively simple shape (compared to what I want to input later). I’ve got 128gb RAM, 8GB NVIDIA card, 2TB SSD, and Intel i7-14700HX processor, which I would think would be enough to process at least this.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/scl/fo/6avpncksx1dg0ex7vf6pn/ABLxyLXTrRmDcGauzTXJL_8?rlkey=pliyhrqs1loqqiqdaod92rpzf&amp;st=hkv7ip67&amp;dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon.ico" class="site-icon" alt="" width="32" height="32">

      <a href="https://www.dropbox.com/scl/fo/6avpncksx1dg0ex7vf6pn/ABLxyLXTrRmDcGauzTXJL_8?rlkey=pliyhrqs1loqqiqdaod92rpzf&amp;st=hkv7ip67&amp;dl=0" target="_blank" rel="noopener nofollow ugc">dropbox.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://www.dropbox.com/scl/fo/6avpncksx1dg0ex7vf6pn/ABLxyLXTrRmDcGauzTXJL_8?rlkey=pliyhrqs1loqqiqdaod92rpzf&amp;st=hkv7ip67&amp;dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The model was imported as a .ply from an Avizo export because the lab I’m in segments in Avizo (and not going to change). It was about 42k points, I used decimate set at 0.9 and it output a 23k-point mesh.</p>
<p>If I did not run pre-processing, the network outputs rendered very quickly, though missing a couple branching points I had marked with endpoints, and the centerline outputs haven’t finished after 30min. If I did run pre-processing, Slicer stays pre-processing for over 30min. I’ve tried changing curve sampling distance to 0.001mm because the scan resolution is 0.006mm; I saw that was an issue in a previous post. I’ve also tried increasing target point count. It pre-processes fast when set to 23k (basically no more decimating), then spends tens of min on the centerline curve and table generation. When I set target point count for 15k, then it takes a very long time to pre-process again, I haven’t seen it finish either step yet.</p>
<p>If this was the most complicated tree structure I wanted a centerline tree of, then I’d be more patient. But I have much more complex structures that I will need trees from too, so I was wondering if there was anything else I could do to optimize computation time or if I was missing something obvious. Avizo has a similar module, but it finishes the computation in a minute or two, though the line isn’t always in the center and it’s harder to edit/refine (talking with them about that too), so I was hoping to use Slicer’s.</p>
<p>Thank you for any ideas!</p>

---

## Post #2 by @chir.set (2025-12-02 17:32 UTC)

<p>Your data has a <code>tree_smooth</code> and a <code>decimate tree</code> models.</p>
<p>With multiple combinations of <code>Preprocess input surface</code>, <code>Target point count</code> and <code>Subdivide</code>, a centerline model only (Tree) is generated in a few seconds with either input model.</p>
<p>Trouble starts while generating centerline curves, it runs and runs and there’s no console output hinting at anything.</p>
<p>If the bifurcated centerline (11K+ points) is processed with <code>vtkCleanPolyData</code> and a new model is created from its output (4K+ points), and the clean centerline model is processed in <code>Centerline disassembly</code>, its components as models are created in a few mins. But it keeps running when curve components are requested. <code>Centerline disassembly</code> relies on <code>Extract centerline</code> to generate curves.</p>
<p>If the bifurcated centerline itself is processed in <code>Centerline disassembly</code> (without cleaning), the same observations can be made.</p>
<p>So the lengthy computation happens with centerline curve generation in <code>Extract centerline</code> for unknown reasons. I’m afraid you’ll have to work with centerline models for now.</p>
<p>Someone else may have a better idea.</p>

---
