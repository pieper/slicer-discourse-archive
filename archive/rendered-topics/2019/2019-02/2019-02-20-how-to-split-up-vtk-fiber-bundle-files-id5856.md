---
topic_id: 5856
title: "How To Split Up Vtk Fiber Bundle Files"
date: 2019-02-20
url: https://discourse.slicer.org/t/5856
---

# How to Split Up VTK Fiber Bundle Files

**Topic ID**: 5856
**Date**: 2019-02-20
**URL**: https://discourse.slicer.org/t/how-to-split-up-vtk-fiber-bundle-files/5856

---

## Post #1 by @rpl6 (2019-02-20 21:53 UTC)

<p>Hello everyone,</p>
<p>I was wondering if there was a way to split up a VTK fiber bundle file into smaller parts (or multiple smaller files) for more manageable processing. I am currently working with Slicer Python, but I would be open to solutions outside of the Slicer environment also. I would greatly appreciate any help and insight anyone can provide!</p>
<p>Thanks,<br>
Rick</p>

---

## Post #2 by @ljod (2019-02-20 23:23 UTC)

<p>Hi there are many ways to do this.</p>
<p>One way is to select parts of the fiber bundle using regions of interest (tutorial here) <a href="http://dmri.slicer.org/docs/" rel="nofollow noopener">http://dmri.slicer.org/docs/</a></p>
<p>If you want to automatically segment whole brain tractography into anatomically curated fiber tracts, you can use our atlas and accompanying python code described here:<br>
<a href="http://dmri.slicer.org/atlases/" class="onebox" target="_blank" rel="nofollow noopener">http://dmri.slicer.org/atlases/</a></p>
<p>Programmatically you can loop over the lines in the polydata and do something with each line. For example keep those within a “mask” as in our code here:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/06270b072d44f4b087b0f92288a9083d0f4d7090/whitematteranalysis/filter.py#L296" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/06270b072d44f4b087b0f92288a9083d0f4d7090/whitematteranalysis/filter.py#L296" target="_blank" rel="nofollow noopener">SlicerDMRI/whitematteranalysis/blob/06270b072d44f4b087b0f92288a9083d0f4d7090/whitematteranalysis/filter.py#L296</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="286" style="counter-reset: li-counter 285 ;">
<li># final line count</li>
<li>#print "&lt;filter.py&gt; Number of lines selected:", outpd.GetNumberOfLines()</li>
<li>if return_indices:</li>
<li>    # return sorted indices, this is the line ordering of output</li>
<li>    # polydata (because we mask rather than changing input line order)</li>
<li>    return outpd, numpy.sort(line_indices)</li>
<li>else:</li>
<li>    return outpd</li>
<li>
</li>
<li>
</li>
<li class="selected">def mask(inpd, fiber_mask, color=None, preserve_point_data=False, preserve_cell_data=True, verbose=True):</li>
<li>""" Keep lines and their points where fiber_mask == 1.</li>
<li>
</li>
<li> Unlike vtkMaskPolyData that samples every nth cell, this function</li>
<li> uses an actual mask, and also gets rid of points that</li>
<li> are not used by any cell, reducing the size of the polydata file.</li>
<li>
</li>
<li> This code also sets scalar cell data to input color data.  This</li>
<li> input data is expected to be 1 or 3 components.</li>
<li>
</li>
<li> If there is no input cell scalar color data, existing cell</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Hope this helps. Let us know if one of these directions works for you.<br>
Lauren</p>

---

## Post #3 by @rpl6 (2019-02-21 13:54 UTC)

<p>Hi Lauren,</p>
<p>Thank you so much for your time and reply, it was very helpful and enlightening!   I realize now that I may have been imprecise with my statement of my original question. I mean to downsample the tracts to maintain a representitive subsample of the original track set. Looking through your whitematteranalysis code was extremely enlightening!</p>
<p>I used your DMRI Tractography Downsample module to achieve what I needed in most cases. However, I fear that I may have stumbled upon another roadblock. Loading large files (&gt;50GB) seems to crash using Tractography Downsample.</p>
<p>The data loads in fine, but as soon as I call the code, Slicer crashes and exits. I don’t imagine it is a RAM issue, because the machine I am working on has 768 GB of RAM and the RAM Utilization doesn’t approach the limit.</p>
<p>Perhaps there way to fix this or to perform this operation outside of Slicer, on disk, or to process the data piecewise? I am also hoping that there is a solution that I am not currently considering. As always, I appreciate any help you (or anyone) can provide.</p>
<p>Thanks,<br>
Rick</p>

---

## Post #4 by @ljod (2019-02-21 14:16 UTC)

<p>Hi I recommend you install whitematteranalysis and use the wm_preprocess_all command. It downsamples all polydata fiber files in the input directory. There’s another command to create a mrml file, which is useful if you want to read several polydata into slicer as  fiber bundles.</p>

---

## Post #5 by @rpl6 (2019-02-21 20:56 UTC)

<p>Hello again Lauren,</p>
<p>Thank you for the advice! wm_preprocess_all seems like what I would like to do. I tried running wm_preprocess_all.py on the large file, and it fails with an error. The script works fine with smaller tract files, but for some reason, it fails on the larger ones. I have attached the command I used and the stdout below, I hope it will help. I truly appreciate how much you have helped me, and I hope I can learn to correctly use your software.</p>
<pre><code>[rpl6@civmcluster1 large_files_TO_DELETE]$ python2 ~/python_lib/bin/wm_preprocess_all.py -f 349084 -j 1 . ./out
Importing whitematteranalysis package.
wm_laterality. Starting white matter laterality computation.

=====input directory======
.
=====output directory=====
./out
==========================
fibers to retain per subject:  349084
minimum length of fibers to retain (in mm): 0
CPUs detected: 16
Using N jobs: 1
==========================
&lt;wm_preprocess.py&gt; Input number of files:  4
('&lt;wm_preprocess.py&gt; ', 1, '/', 4, '**Starting subject:', 'roi_106_tracks')
('&lt;wm_preprocess.py&gt; ', 1, '/', 4, '**Reading input:', 'roi_106_tracks')
('&lt;wm_preprocess.py&gt; ', 1, '/', 4, '**Downsampling input:', 'roi_106_tracks', ' number of fibers: ', 349084)
Traceback (most recent call last):
  File "/home/rpl6/python_lib/bin/wm_preprocess_all.py", line 162, in &lt;module&gt;
for sidx in range(0, len(inputPolyDatas)))
  File "/home/rpl6/python_lib/lib/python2.7/site-packages/joblib/parallel.py", line 921, in __call__
if self.dispatch_one_batch(iterator):
  File "/home/rpl6/python_lib/lib/python2.7/site-packages/joblib/parallel.py", line 759, in dispatch_one_batch
self._dispatch(tasks)
  File "/home/rpl6/python_lib/lib/python2.7/site-packages/joblib/parallel.py", line 716, in _dispatch
job = self._backend.apply_async(batch, callback=cb)
  File "/home/rpl6/python_lib/lib/python2.7/site-packages/joblib/_parallel_backends.py", line 182, in apply_async
result = ImmediateResult(func)
  File "/home/rpl6/python_lib/lib/python2.7/site-packages/joblib/_parallel_backends.py", line 549, in __init__
self.results = batch()
  File "/home/rpl6/python_lib/lib/python2.7/site-packages/joblib/parallel.py", line 225, in __call__
for func, args, kwargs in self.items]
  File "/home/rpl6/python_lib/bin/wm_preprocess_all.py", line 136, in pipeline
wm3 = wma.filter.downsample(wm2, args.numberOfFibers, verbose=False)
  File "/home/rpl6/python_lib/lib/python2.7/site-packages/whitematteranalysis/filter.py", line 284, in downsample
outpd = mask(inpd, fiber_mask, preserve_point_data=preserve_point_data, preserve_cell_data=preserve_cell_data, verbose=verbose)
  File "/home/rpl6/python_lib/lib/python2.7/site-packages/whitematteranalysis/filter.py", line 435, in mask
point = inpoints.GetPoint(ptids.GetId(pidx))
ValueError: expects 0 &lt;= id &amp;&amp; id &lt; GetNumberOfPoints()`Preformatted text`</code></pre>

---

## Post #6 by @ljod (2019-02-21 21:26 UTC)

<p>Try two things:</p>
<ol>
<li>Use -f to specify a low number of fibers to keep (like 10000) and -l to keep only above a length threshold.</li>
<li>Make sure your file is properly formatted vtk. One thing to try is reading it into Slicer as a model.</li>
</ol>

---

## Post #7 by @rpl6 (2019-02-22 21:29 UTC)

<p>Thank you for the suggestions, I have tried both:</p>
<p>For 1. It seems to have failed again with the same error, I have placed the stdout below.</p>
<p>For  2. I am able to load the file into Slicer in the sense that it shows up in the Data module. However, as soon as I enable 3D view and try to display the model it crashes. I believe that may have something to do with the graphics capabilities of this workstation, and I am hoping it is not due to data formatting.</p>
<p>Once again, thank you for your time and help!</p>
<pre><code>[rpl6@civmcluster1 large_files_TO_DELETE]$ python2 ~/python_lib/bin/wm_preprocess_all.py -f 10000 -l 10 -j 1 . ./out
Importing whitematteranalysis package.
wm_laterality. Starting white matter laterality computation.

=====input directory======
.
=====output directory=====
./out
==========================
fibers to retain per subject:  10000
minimum length of fibers to retain (in mm):  10
CPUs detected: 16
Using N jobs: 1
==========================
&lt;wm_preprocess.py&gt; Input number of files:  4
('&lt;wm_preprocess.py&gt; ', 1, '/', 4, '**Starting subject:', 'roi_106_tracks')
('&lt;wm_preprocess.py&gt; ', 1, '/', 4, '**Reading input:', 'roi_106_tracks')
('&lt;wm_preprocess.py&gt; ', 1, '/', 4, '**Preprocessing:', 'roi_106_tracks')
Traceback (most recent call last):
  File "/home/rpl6/python_lib/bin/wm_preprocess_all.py", line 162, in &lt;module&gt;
    for sidx in range(0, len(inputPolyDatas)))
  File "/home/rpl6/python_lib/lib/python2.7/site-packages/joblib/parallel.py", line 921, in __call__
    if self.dispatch_one_batch(iterator):
  File "/home/rpl6/python_lib/lib/python2.7/site-packages/joblib/parallel.py", line 759, in dispatch_one_batch
    self._dispatch(tasks)
  File "/home/rpl6/python_lib/lib/python2.7/site-packages/joblib/parallel.py", line 716, in _dispatch
    job = self._backend.apply_async(batch, callback=cb)
  File "/home/rpl6/python_lib/lib/python2.7/site-packages/joblib/_parallel_backends.py", line 182, in apply_async
    result = ImmediateResult(func)
  File "/home/rpl6/python_lib/lib/python2.7/site-packages/joblib/_parallel_backends.py", line 549, in __init__
    self.results = batch()
  File "/home/rpl6/python_lib/lib/python2.7/site-packages/joblib/parallel.py", line 225, in __call__
    for func, args, kwargs in self.items]
  File "/home/rpl6/python_lib/bin/wm_preprocess_all.py", line 120, in pipeline
    wm2 = wma.filter.preprocess(wm, args.fiberLength, verbose=False)
  File "/home/rpl6/python_lib/lib/python2.7/site-packages/whitematteranalysis/filter.py", line 241, in preprocess
    outpd = mask(inpd, fiber_mask, preserve_point_data=preserve_point_data, preserve_cell_data=preserve_cell_data, verbose=verbose)
  File "/home/rpl6/python_lib/lib/python2.7/site-packages/whitematteranalysis/filter.py", line 435, in mask
    point = inpoints.GetPoint(ptids.GetId(pidx))
ValueError: expects 0 &lt;= id &amp;&amp; id &lt; GetNumberOfPoints()</code></pre>

---

## Post #8 by @ljod (2019-02-22 23:46 UTC)

<p>This looks to be a corrupt file, most likely. The WMA code fails to loop through the data structure, and even simple loading as a model crashes slicer. This sort of strange error issue happens to us sometimes if there is a disk access issue when the tractography algorithm is writing a very large file. This can fail silently on our compute cluster.</p>
<p>What is the provenance of this vtk file? How was it generated?</p>

---

## Post #9 by @rpl6 (2019-02-25 14:10 UTC)

<blockquote>
<p>This looks to be a corrupt file, most likely. The WMA code fails to loop through the data structure, and even simple loading as a model crashes slicer. This sort of strange error issue happens to us sometimes if there is a disk access issue when the tractography algorithm is writing a very large file. This can fail silently on our compute cluster.</p>
</blockquote>
<p>I see, that would make sense because the files that are generating the error are particularly large. I am not sure if it makes a difference, but Slicer does not crash upon loading the VTK, but rather upon trying to display it.</p>
<blockquote>
<p>What is the provenance of this vtk file? How was it generated?</p>
</blockquote>
<p>The tracts originated in DSI Studio as .trk files. I used this tool to convert them to VTKs: <a href="https://github.com/MarcCote/tractconverter" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MarcCote/tractconverter: Converter for different neuro-imaging file formats.</a><br>
It seems very feasible that they are corrupt because that software has been marked depreciated. However, there were 282 other (yet smaller) track sets of the same provenance that were able to be converted, processed with WMA, and loaded without error.</p>
<p>I hope this information helps. The time you have given is greatly appreciated!</p>
<p>Thank you,<br>
Rick</p>

---

## Post #10 by @ljod (2019-02-25 15:26 UTC)

<p>I think the reader can get data from the file but the data structure is not internally consistent and code accessing it that assumes a valid polydata fails. This seems consistent with the evidence. I suggest testing if the original trk file is ok by reading it into another program then saving it to vtk in another way. I think trackvis supports vtk export for example. I seem to remember Isaiah worked on a converter also that might be part of slicer or posted in this forum. Let me know what you learn from these tests and I’ll try to provide more suggestions.</p>

---

## Post #11 by @rpl6 (2019-02-26 20:23 UTC)

<p>Thank you for providing those tests! It seems that the original TRK file loads into Trackvis fine, and as long as I skip most of the tracts or disable displaying them, Trackvis does not crash. From having the file loaded in Trackvis, I did 2 things:</p>
<ol>
<li>I skipped 99.5% of the tracks and saved them to a VTK file via Trackvis. This yielded a track file that could successfully load and display in Slicer as a model</li>
<li>I disabled viewing and included all of the tracks (skipped 0% of the tracks) and exported those. Slicer never seemed to even try to load these (I would click “Ok” on the load window and nothing would happen at all).</li>
</ol>
<p>I am currently getting Isaiah’s converter to work. I also believe that I may be able to use Trackvis to do one round of track reduction (as per test 1) before putting those into WMA for the final reduction. I will update you on how those go.</p>

---

## Post #12 by @ljod (2019-02-27 15:47 UTC)

<p>I’m glad this is working!</p>

---
