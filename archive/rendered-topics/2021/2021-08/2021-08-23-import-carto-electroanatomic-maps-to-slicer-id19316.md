---
topic_id: 19316
title: "Import Carto Electroanatomic Maps To Slicer"
date: 2021-08-23
url: https://discourse.slicer.org/t/19316
---

# Import Carto electroanatomic maps to slicer

**Topic ID**: 19316
**Date**: 2021-08-23
**URL**: https://discourse.slicer.org/t/import-carto-electroanatomic-maps-to-slicer/19316

---

## Post #1 by @mk.kassai (2021-08-23 13:09 UTC)

<p>I would like to ask for a little help with cardiac electroanatomic map importing.<br>
There was a similar <a href="https://discourse.slicer.org/t/is-there-interest-in-a-reader-for-cardiac-electrophysiology-electronanatomic-maps/6356/3">issue</a> a while ago, where eventually a <a href="https://github.com/stephan1312/SlicerEAMapReader" rel="noopener nofollow ugc">new module</a> was born, however it looks like it won’t work with CARTO files.<br>
I have the .txt files and a really nice explanation of the values, however I lack the skills to recreate a script that builds the models from the coordinates.<br>
The attached screenshot shows what the different values refer to, and I’d like to create a model with the exact shape of the atrium and also the bipolar value (Which we will compare to segmentations).<br>
As far as I know, that means I need the the E, F, G, and L columns to build the model.<br>
Does someone have any idea where I could start to build a script, or if there is a module already published?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2c389f2ce7548f6e107e2524606943f01def670.png" data-download-href="/uploads/short-url/pvpVEdDtWG7OVLbVrsBqbSC7r7G.png?dl=1" title="Screenshot 2021-08-23 at 15.01.17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2c389f2ce7548f6e107e2524606943f01def670.png" alt="Screenshot 2021-08-23 at 15.01.17" data-base62-sha1="pvpVEdDtWG7OVLbVrsBqbSC7r7G" width="690" height="413" data-dominant-color="323232"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-08-23 at 15.01.17</span><span class="informations">763×457 47.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-08-23 13:42 UTC)

<p>Probably the existing Carto file reader can be fixed up to work with your file variant. Can you share a complete study that we can test with? (anonymized or phantom data set)</p>

---

## Post #3 by @mk.kassai (2021-08-24 08:29 UTC)

<p>Thank you!<br>
Here is the <a href="https://www.dropbox.com/s/l13qn9e8ps410iz/EA_map.txt?dl=0" rel="noopener nofollow ugc">file</a><br>
And the full table about the values<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4b9a3de0981ac09bfcb3428b42df853e77dffc2.png" data-download-href="/uploads/short-url/ulQXgcXKsH3b65tRRHRgl03gEtI.png?dl=1" title="Screenshot 2021-08-23 at 9.38.02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4b9a3de0981ac09bfcb3428b42df853e77dffc2_2_543x500.png" alt="Screenshot 2021-08-23 at 9.38.02" data-base62-sha1="ulQXgcXKsH3b65tRRHRgl03gEtI" width="543" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4b9a3de0981ac09bfcb3428b42df853e77dffc2_2_543x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4b9a3de0981ac09bfcb3428b42df853e77dffc2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4b9a3de0981ac09bfcb3428b42df853e77dffc2.png 2x" data-dominant-color="323232"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-08-23 at 9.38.02</span><span class="informations">622×572 58.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-08-25 05:54 UTC)

<p>Can you also get a mesh file (.vtk or .stl or other format) from Carto? The points could be used to reconstruct a mesh, but it is not completely trivial</p>
<p>The EA Map Reader expects a zip file from Carto, with the point list text file named as <code>..._car.txt</code>, mesh file named as <code>....mesh</code>, and ablation sites file named as <code>VisiTagExport/Sites.txt</code>. Do you get such zip file from your Carto system?</p>
<p>I could load your text file if I renamed as the extension expected it and could create a left atrium mesh using Markups to Model extension:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7e82d68abc73fc1ed3453f6b098ec927deaa160.jpeg" data-download-href="/uploads/short-url/x5xJteNYtGG0OFV19WryK4KuSU8.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7e82d68abc73fc1ed3453f6b098ec927deaa160_2_690x419.jpeg" alt="image" data-base62-sha1="x5xJteNYtGG0OFV19WryK4KuSU8" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7e82d68abc73fc1ed3453f6b098ec927deaa160_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7e82d68abc73fc1ed3453f6b098ec927deaa160_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7e82d68abc73fc1ed3453f6b098ec927deaa160_2_1380x838.jpeg 2x" data-dominant-color="C7BDD7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1166 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>But it would be better to use the mesh the Carto creates, to be consistent. Also, we would need to find a VTK filter that can nicely map the bipolar or other values from the measurement points to the mesh - while this mapping is probably already available in the mesh file that Carto exported.</p>

---

## Post #5 by @mk.kassai (2021-08-25 08:25 UTC)

<p>Unfortunately I only have these .txt files.<br>
When I try to import the .zip file as you suggested, the EA Map Reader module starts to extract it, but stops at 10%.</p>

---

## Post #6 by @lassoan (2021-08-25 15:30 UTC)

<p>Import of this file worked for me:<br>
<a href="https://1drv.ms/u/s!Arm_AFxB9yqHxf4bPBvcr9SQKhzj8w?e=xm6aYW" class="onebox" target="_blank" rel="noopener">https://1drv.ms/u/s!Arm_AFxB9yqHxf4bPBvcr9SQKhzj8w?e=xm6aYW</a></p>
<p>You need to wait several minutes, because the module does block updates while placing points one by one. I’ve submitted a <a href="https://github.com/stephan1312/SlicerEAMapReader/pull/7">pull request</a> that makes the import faster (still a few ten seconds).</p>
<aside class="quote no-group" data-username="mk.kassai" data-post="5" data-topic="19316">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mk.kassai/48/9631_2.png" class="avatar"> mk.kassai:</div>
<blockquote>
<p>Unfortunately I only have these .txt files.</p>
</blockquote>
</aside>
<p>Did you acquire the files yourself? Can you describe the steps of how you exported the data from Carto?</p>
<p>There is lots of room for improvements in the module. It should be possible to speed up the import, store all the values as measurements, maybe add an option to load the points as colored glyphs (can be generated from the fiducials), and of course it could be made a proper extension that can be installed from the Extensions manager by a few clicks.</p>
<p><a class="mention" href="/u/stephan">@stephan</a> are you still around? Would you be interested in making some improvements and submitting the extension to the Extensions index so that EA Map Reader shows up in the Extensions manager?</p>

---

## Post #7 by @mk.kassai (2021-08-27 13:42 UTC)

<p>We don’t create them, we just receive them for further analysis.<br>
The one you sent me works well, it imports as markup points in a few seconds.</p>
<p>However, the ones I have seem to crash Slicer at 10%.<br>
I left it running for hours, but the whole program stopped responding.</p>

---

## Post #8 by @lassoan (2021-08-27 22:12 UTC)

<p>I’ve just renamed the file that I got from you and zipped it.</p>
<aside class="quote no-group" data-username="mk.kassai" data-post="7" data-topic="19316">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mk.kassai/48/9631_2.png" class="avatar"> mk.kassai:</div>
<blockquote>
<p>We don’t create them, we just receive them for further analysis.</p>
</blockquote>
</aside>
<p>Could you please ask the clinicians to describe how they export the files (what software version they use, what export options does the software offers and what they choose, what files are exported, what files they choose to share with you,…)? There is a good chance they can have the mesh files, too, they just might think that you don’t need it.</p>

---

## Post #9 by @stephan (2021-08-30 05:17 UTC)

<p>Hi everybody,<br>
sorry for not responding earlier.<br>
<a class="mention" href="/u/lassoan">@lassoan</a> : In general, I am still around, but since I am not longer on the research fellowship I was on 2 years ago (when I wrote the extension an learned Python in  the process) I do not really have the time for maintenance and improvements. The fact that the extension was my first encounter with Python might also explain the huge room for improvement in efficiency and coding style. Please feel free <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=10" title=":wink:" class="emoji" alt=":wink:"><br>
I’ve tried to figure out how to package the extension so that it can be submitted to the extension index, but I never really understood is (it seems you need a full-blown IDE with CMAKE and other version control stuff to package it, not to mention all the unit testing). Anyone wanting to adopt the project is very welcome.</p>
<p><a class="mention" href="/u/mk.kassai">@mk.kassai</a> : Carto v7 exports should still be importable as anatomy only (without voltage and activation time data). You might want to point your clinicians to the following step-by-step export tutorial:</p>
<ol>
<li>
<p>On the start-up screen, select “Review Study”. Open study for review</p>
</li>
<li>
<p>Select Study → Export Study Data… from the menu</p>
</li>
<li>
<p>Close study review</p>
</li>
<li>
<p>Back in the start-up screen, select “System”</p>
</li>
<li>
<p>In the “System tools” menu, select the Export Data… button</p>
</li>
<li>
<p>Select the correct patient. After the prior export (step 3), there should be a file called “Export_Study_[some numbers].zip” with today’s date and “RawData” in the “Type” column</p>
</li>
<li>
<p>Select this file for export (by clicking the arrow to the right of the file list), select the export target at the bottom of the screen, and hit export. You have to chose a password for the export.</p>
</li>
<li>
<p>The actual study data .zip file is exported inside another (encrypted) .zip file which needs to be unpacked first. So open the .zip file with any zip extractor using the password you chose in step 8. Inside this password-protected “container” zip file there should be the actual study zip (named “Export_Study_[some numbers].zip”). Extract this file out of the container, using the password you chose.</p>
</li>
<li>
<p>This (unencrypted) .zip file which you just took out of the export container is ready for import using EAMapReader</p>
</li>
</ol>
<p>The interpolated electric data which previously was part of the .mesh file is no longer exported in v7. However, electric data per point (NOT per anatomy vertex, but per catheter-acquired point in space) is available in the *_car.txt files. For more detail see here: <a href="https://github.com/stephan1312/SlicerEAMapReader/issues/4" class="inline-onebox" rel="noopener nofollow ugc">Change in exported data in Carto3 v7 · Issue #4 · stephan1312/SlicerEAMapReader · GitHub</a><br>
Thus, one could re-create interpolated electric (bipolar, unipolar voltage and LAT) data for each model vertex and add this as a scalar overlay, but this needs to be done in the plugin, since the interpolation is no longer available in the export (I think this is due to the so-called HD coloring feature which became available first in v6 and broke the export when active. In v7 this can no longer be turned off.)</p>
<p>The file you shared in post <span class="hashtag">#3</span> is actually the _car.txt file (and I am pretty sure it was named 1-OG_car.txt when it was first exported). It should have come inside a .zip file, accompanied by (among others) a file named 1-OG.mesh. This entire zip file could be read by EAMapReader.</p>
<p>Let me know if there is anything else I could do</p>
<p>Stephan</p>

---

## Post #10 by @mk.kassai (2021-09-01 14:38 UTC)

<p>Dear Stephen and Andras,</p>
<p>Thank you for your replies.<br>
So it seems that currently the only file that contains the electric values is the .txt file.<br>
I’m still a beginner in python, but do you have some tips about where I could start to improve the module as Stephan explained, to re-create the interpolated electric data?</p>

---

## Post #11 by @stephan (2021-09-01 15:51 UTC)

<p>This is correct.<br>
Depending on your use case, you might not even need the interpolation. The .txt file gives you “raw” electric and spatial data. If you need anatomy as well(e.g. for registration purposes), the .mesh file contains a triangulated mesh (same coordinate space as the txt file).<br>
However, if you need to recreate the look of the map as seen on the CARTO workstation, the projection/interpolation needs to be calculated.</p>

---

## Post #12 by @mk.kassai (2021-09-02 09:41 UTC)

<p>I found <a href="https://www.dropbox.com/s/wol6daj26fd61ui/1-OG.mesh.zip?dl=0" rel="noopener nofollow ugc">the .mesh file</a> for the same patient, however for me it seems like its the newer version, that only contains the anatomic data as coordinates, but not the voltage, as <a class="mention" href="/u/stephan">@stephan</a> explained.</p>

---

## Post #13 by @lassoan (2021-09-02 14:23 UTC)

<p>The EA mapper can nicely read this mesh file. The mesh that “Markups to model” generated looks quite similar:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc74985baf135ca90c744007aafc6fc57e6d41de.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc74985baf135ca90c744007aafc6fc57e6d41de.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc74985baf135ca90c744007aafc6fc57e6d41de.mp4</a>
    </source></video>
  </div><p></p>
<p>However, on one side VTK’s Delaunay triangulator was not able to follow the points as closely  as Carto:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de14f03212bb6b349632c3b4374b4756934e01a5.jpeg" data-download-href="/uploads/short-url/vGCRdVTFJm5A8P5KW0YpcCSfwep.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de14f03212bb6b349632c3b4374b4756934e01a5_2_594x500.jpeg" alt="image" data-base62-sha1="vGCRdVTFJm5A8P5KW0YpcCSfwep" width="594" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de14f03212bb6b349632c3b4374b4756934e01a5_2_594x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de14f03212bb6b349632c3b4374b4756934e01a5_2_891x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de14f03212bb6b349632c3b4374b4756934e01a5_2_1188x1000.jpeg 2x" data-dominant-color="A0999E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1447×1217 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Therefore, for the registration you will benefit from importing the Carto-generated mesh. There are a number of other surface reconstruction filters in VTK that can create a surface from sparse points, but it is not an easy problem because the points are distributed very unevenly.</p>
<p><a class="mention" href="/u/mk.kassai">@mk.kassai</a> What is your end goal with the bipolar value? Just visualization? Would showing the bipolar value as colored spheres (and not interpolated on the surface) be sufficient for you?</p>

---

## Post #14 by @mk.kassai (2021-09-02 15:31 UTC)

<p>Our goal is to compare some segmentations to these points, so showing them as colored spheres (Or being able to threshold them by bipolar voltage value, and compare the segmentations to those) would be perfect for us.</p>

---

## Post #15 by @lassoan (2021-09-02 15:48 UTC)

<p>Sounds very doable then. You can generate a model that contains colored spheres using <a href="https://vtk.org/doc/nightly/html/classvtkGlyph3D.html">vtkGlyph3D filter</a>. You provide a vtkPolyData as input, you use the xyz coordinates as point positions, and you put the bipolar values into a vtkDoubleArray and you add that as point data.</p>

---

## Post #16 by @mk.kassai (2021-09-02 15:57 UTC)

<p>Perfect, thank you!<br>
I really appreciate your help with all of this <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/stephan">@stephan</a>.</p>

---

## Post #17 by @mk.kassai (2021-10-20 15:02 UTC)

<p>Dear Andras,</p>
<p>My python skills are close to zero, so I could not figure out a way to use the suggested solution.<br>
For the analysis part, I’m ok with the thresholded bipolar voltages, but I would like to re-create the carto map in Slicer simply for visualization purposes.<br>
Since all we have are these coordinates with values and the mesh, I’d like to “paint” the mesh the same way it looks like on the original carto map (attached screenshots from Carto).<br>
Could you please show me a way to start, to understand the usage of vtkGlyph3D to re-create something like the carto map?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df46954665225a2cde694ee03ef10589f0d06b66.jpeg" data-download-href="/uploads/short-url/vRbHmWfzzLMfJxrDshxws1q2ECy.jpeg?dl=1" title="AP" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df46954665225a2cde694ee03ef10589f0d06b66_2_431x500.jpeg" alt="AP" data-base62-sha1="vRbHmWfzzLMfJxrDshxws1q2ECy" width="431" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df46954665225a2cde694ee03ef10589f0d06b66_2_431x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df46954665225a2cde694ee03ef10589f0d06b66_2_646x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df46954665225a2cde694ee03ef10589f0d06b66_2_862x1000.jpeg 2x" data-dominant-color="440845"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">AP</span><span class="informations">949×1100 65.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #19 by @Raha_Sep (2022-10-25 14:06 UTC)

<p>Dear Andras,<br>
Could you please let me know the way to import the txt file only? to which extension you renamed the text file?<br>
When I try to import the .zip file as you suggested, the EA Map Reader module starts to extract it but stops at 10% or 30%. Do I need to keep only <code>..._car.txt</code> , mesh file and …_car.txt inside the zip file to be imported by Slicer?<br>
I can’t either import any [EA_map.zip] file as you explained above or find  the Markups to Model extension.</p>
<p>Thank you for your help!<br>
Raha</p>

---

## Post #20 by @Nisal_Udawatta (2023-05-23 09:51 UTC)

<p>Hi,<br>
I can see in some Carto files (.mesh), Group IDs are 0s and -1000000s. Does that mean something affecting for the map?<br>
Cheers.</p>

---

## Post #21 by @Raha_Sep (2023-06-20 14:03 UTC)

<p>Hi,<br>
When Wavefront Annotation is used, a “No valid LAT” points have a value of -10000</p>

---
