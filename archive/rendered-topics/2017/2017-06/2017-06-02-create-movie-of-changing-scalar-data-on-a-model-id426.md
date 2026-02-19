---
topic_id: 426
title: "Create Movie Of Changing Scalar Data On A Model"
date: 2017-06-02
url: https://discourse.slicer.org/t/426
---

# Create movie of changing scalar data on a model

**Topic ID**: 426
**Date**: 2017-06-02
**URL**: https://discourse.slicer.org/t/create-movie-of-changing-scalar-data-on-a-model/426

---

## Post #1 by @lassoan (2017-06-02 15:48 UTC)

<p>Following up on this question posted in another topic:</p>
<aside class="quote no-group" data-username="mrjeffs" data-post="14" data-topic="382">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mrjeffs/48/1185_2.png" class="avatar"><a href="https://discourse.slicer.org/t/freesurfer-annotation-file-crashes-model-module/382/14">Freesurfer annotation file crashes model module</a></div>
<blockquote>
<p>is there a method to cycle thru an overlay in movie mode?</p>
</blockquote>
</aside>
<p>Is there a way to create an animation of a model displayed with different scalar overlay (coloring), changing in time?</p>

---

## Post #2 by @lassoan (2017-06-02 15:53 UTC)

<p>You can cycle through manually (step-by-step or slider) or automatically (play/pause) and create videos of any changing properties of any nodes - using the Sequences extension.</p>
<ul>
<li>Load all scalar overlays</li>
<li>In <code>Sequence browser</code> module, create a new Sequence (by clicking on the green <code>+</code> icon in the Synchronized nodes section)</li>
<li>Choose <code>ModelDisplay</code> as proxy node (the node that changes are recorded/replayed of)</li>
<li>Click sequence record button (red circle)</li>
<li>Go to Models module, open Display / Scalars section</li>
<li>Select <code>Active scalar</code>, one by one, for each scalar value that you would like to include in the animation</li>
<li>Click sequence record button to stop recording</li>
<li>You can browse the scalars using the Sequence browser module, or you can show the Sequence browser toolbar (menu: View / Toolbars / Sequence browser) while you are in any module</li>
</ul>
<p>Use Screen capture module with Animation mode = sequence to create a video file from the animation.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/e673cabe764ff681e2dd8ac20f680513df195bf4.gif" width="394" height="346"></p>

---

## Post #3 by @mrjeffs (2017-06-02 17:43 UTC)

<p>interesting,  i will explore that further. the idea was to visualize .stc meg files with morph data structure for coordinates  and time-course dspm data for intensity. these are output by mne-python. it would be more intuitive to load the .stc file in one gulp as there can be 1200 time points for a regular data set.<br>
as another aside can this be done with fiber bundles. i am interested in embedding that same data in dti data. creating an overlay would be one step. seeing if vtk can hold time-course data as well as static FA and NODDI type data.<br>
any thoughts on either of those possibilities.</p>

---

## Post #4 by @lassoan (2017-06-02 17:49 UTC)

<p>You can show time course of any data: changing surface geometry, scalar overlays, linear or warping transforms, rendering parameters, camera positions, etc.</p>
<p>Time course data is stored in VTK files as one timepoint per file. One option is to load all timepoints into Slicer and use the Sequences module to create a Sequence from them. You can then browse/replay them using Sequence browser. You can do synchronized browsing of any number of sequences using Sequence browser module.</p>
<p>Sequences modules are not always that simple to figure out, so if you have any questions about how to create or import time sequences then let me know.</p>

---

## Post #5 by @mrjeffs (2017-06-05 18:26 UTC)

<p>thanks andras, what i would like to do is generate copies of the same DTI fiberbundle with different time course data in each one. then use the Sequence module to link them together. so 25-40 vtk files with one of the specific scalar values<br>
replaced with our data then loop though each of them in time order. can this be done?<br>
jeff</p>

---

## Post #6 by @lassoan (2017-06-06 00:23 UTC)

<p>Yes, that should work, that’s exactly what’s Sequences modules are developed for.</p>
<p>Sequence module does not have an specific “sequencer” for DTI fiberbundles, so a generic sequencer will be used. If you experience slow replay speed or any other issue then let me know and I’ll add an optimized sequencer (I’ll just need sample data from you).</p>

---

## Post #7 by @mrjeffs (2017-06-06 00:26 UTC)

<p>thanks, not sure how to get started here, i have added and selected each of 6 individual linear fiber bundles but it seems none of the other buttons are active. not sure of the work flow here. any docs or tutorials?<br>
jeff</p>

---

## Post #8 by @lassoan (2017-06-06 01:13 UTC)

<p>How to set it up:</p>
<ul>
<li>Load all data in the scene.</li>
<li>In Sequences module, at the top <code>Active node</code> selector create a new Sequence node.</li>
<li>In Add/remove data nodes section, add all your nodes that you would like to replay (by clicking the green left-arrow button)</li>
<li>Go to Sequence browser module</li>
<li>At the top of <code>Synchronized nodes</code> section, select your sequence and click the green <code>+</code> icon =&gt; this will add a new “proxy node” to the scene (that will always contain the selected timepoint of the sequence).</li>
<li>Click <code>Rename</code> checkbox to rename the proxy node to contain the time point in the node name (this is optional, just makes it a bit easier to find your proxy node)</li>
<li>Use the play/pause, prev/next buttons to replay the time sequence (you can also show the Sequence browser toolbar to access replay controls while you are in another module)</li>
</ul>

---

## Post #9 by @mrjeffs (2017-06-06 05:24 UTC)

<p>ok andras, will try tomorrow. i think most of the problem is i have 40 x 500+MB fibertracts.vtk to load into memory.<br>
more than 20gig. so the response was real slow. if there is a way to load the vtks into slicer memory directly without the hang ups (paging perhaps, memory limits? idk) then it might work better??<br>
jeff</p>

---

## Post #10 by @lassoan (2017-06-06 11:25 UTC)

<p>It is very rare that you actually need all the details of a 500MB model to display on a regular screen. Usually you can decimate large meshes so that you have 90-99% size reduction without visible difference. In Slicer, you can experiment with decimation settings by using Surface toolbox module.</p>
<p>Or, you can change how the tracts are generated: If you use tube filter then you can reduce number of sides, don’t use tube filter at all (have just lines), and/or fit a spline to the tract lines and resample with a larger spacing.</p>
<p>If you can load all data in memory then even if loading and browsing is slow, you can create fluid animations using Screen Capture module (rendering may take a long time, but the generated video will be fast and smooth). You just have to make sure that you allocate enough virtual memory in your operating system.</p>

---

## Post #11 by @mrjeffs (2017-06-07 03:10 UTC)

<p>hi andras, the Surface toolbox module shows empty with no selectable fiber bundles.<br>
thinking of appending our data to the end of the original vtk file in ascii. we would have 40 scalar values to  toggle through but would that work? how is the hash calculated at the top of the file? wouldn’t we need to adjust that? anything other considerations?<br>
jeff</p>

---

## Post #12 by @mrjeffs (2017-06-09 01:08 UTC)

<p>looks like the selectable scalar values are hard coded. adding more value types yields nothing. i’ve run out of time.<br>
if you can think of any other way to loop over values in a fiber bundle, please let me know.<br>
jeff<br>
ps do you think this concept is popular enough that it should be a feature request for the future?</p>

---

## Post #13 by @lassoan (2017-06-09 11:15 UTC)

<aside class="quote no-group" data-username="mrjeffs" data-post="12" data-topic="426">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mrjeffs/48/1185_2.png" class="avatar"> mrjeffs:</div>
<blockquote>
<p>looks like the selectable scalar values are hard coded</p>
</blockquote>
</aside>
<p>Do you mean that you can save scalars with arbitrary names but only certain names are recognized? Are the names completely custom (you can compute any value and save it with any name you want) or there is a list of valid names?</p>
<p>It should be easy to change the data reader to load all scalars, I just need more information and some sample data sets.</p>

---
