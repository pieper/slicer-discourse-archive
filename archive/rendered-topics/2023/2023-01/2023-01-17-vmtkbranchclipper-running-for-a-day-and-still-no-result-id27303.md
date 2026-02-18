# vmtkbranchclipper running for a day and still no result.

**Topic ID**: 27303
**Date**: 2023-01-17
**URL**: https://discourse.slicer.org/t/vmtkbranchclipper-running-for-a-day-and-still-no-result/27303

---

## Post #1 by @Fotos_Stylianou (2023-01-17 15:01 UTC)

<p>Hi all,<br>
I am new here!<br>
As the title says, I have been using the vmtkbranchclipper on a tracheobronchial tree to generate the branches but the command is running forever.</p>
<p>The command I am using is this<br>
“~/vmtk_Py36/vmtk/bin/vmtkbranchclipper -ifile TB.stl -centerlinesfile TB_cl_sm_sp.vtp -ofile TB_branch_cl_sm_sp.vtp”</p>
<p>here is a look of the input files:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/594d7210aae1fac7e2dc2325a3367e74d5eebf96.jpeg" data-download-href="/uploads/short-url/cK0q7dil3zMZqwB6gh51TSFsuVw.jpeg?dl=1" title="TB" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/594d7210aae1fac7e2dc2325a3367e74d5eebf96_2_690x495.jpeg" alt="TB" data-base62-sha1="cK0q7dil3zMZqwB6gh51TSFsuVw" width="690" height="495" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/594d7210aae1fac7e2dc2325a3367e74d5eebf96_2_690x495.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/594d7210aae1fac7e2dc2325a3367e74d5eebf96_2_1035x742.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/594d7210aae1fac7e2dc2325a3367e74d5eebf96_2_1380x990.jpeg 2x" data-dominant-color="43464D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">TB</span><span class="informations">1568×1126 235 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If I run the same command on a subset of the geometry the command gives an output. For example see the image below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e30e3b8bf922f652cf6ab09e5580843f01bf4d94.jpeg" data-download-href="/uploads/short-url/woCSuTSO7mtZHffWbQRMn28ID9G.jpeg?dl=1" title="LLL" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e30e3b8bf922f652cf6ab09e5580843f01bf4d94_2_690x494.jpeg" alt="LLL" data-base62-sha1="woCSuTSO7mtZHffWbQRMn28ID9G" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e30e3b8bf922f652cf6ab09e5580843f01bf4d94_2_690x494.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e30e3b8bf922f652cf6ab09e5580843f01bf4d94_2_1035x741.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e30e3b8bf922f652cf6ab09e5580843f01bf4d94_2_1380x988.jpeg 2x" data-dominant-color="3F414A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">LLL</span><span class="informations">1570×1126 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In fact I can run the command for the other 4 subsets (lobes) and again I get an output.<br>
It takes about 30mins if I remember well to run each subsets. But the full tree was running for a day and I stopped it.</p>
<p>What seems to be the issue?<br>
I believe some form of optimisation is needed. Somewhere it gets trapped.</p>
<p>You can access my files here</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/sh/660ev16iocohivt/AADDnlyngCsBitqvWQJ47wc4a?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/sh/660ev16iocohivt/AADDnlyngCsBitqvWQJ47wc4a?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/sh/660ev16iocohivt/AADDnlyngCsBitqvWQJ47wc4a?dl=0" target="_blank" rel="noopener nofollow ugc">VMTK_question</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @chir.set (2023-01-18 10:37 UTC)

<p>It could be that your TB.stl file is corrupted, just a conclusion.</p>
<p>Try these in SLicer :</p>
<ul>
<li>load TB.stl</li>
<li>in Data module, create a segmentation from the TB node</li>
<li>in Segment editor module, hide 3D and show 3D again</li>
</ul>
<p>This is the result :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f6d8fd8c20202923d4e4d61fcb9c6358471a97c.png" data-download-href="/uploads/short-url/ibhnbNG3cRqlfa6j5Wn8M53DGPy.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f6d8fd8c20202923d4e4d61fcb9c6358471a97c_2_546x500.png" alt="Screenshot" data-base62-sha1="ibhnbNG3cRqlfa6j5Wn8M53DGPy" width="546" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f6d8fd8c20202923d4e4d61fcb9c6358471a97c_2_546x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f6d8fd8c20202923d4e4d61fcb9c6358471a97c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f6d8fd8c20202923d4e4d61fcb9c6358471a97c.png 2x" data-dominant-color="201F0C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">684×626 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>No such glitches were found with <a href="https://www.allevi3d.com/sample-files/" rel="noopener nofollow ugc">sample</a> STL files.</p>
<p>I can’t explain any of these unexpected behaviours,  you may try regenerating your surface.</p>

---

## Post #3 by @Fotos_Stylianou (2023-01-18 16:44 UTC)

<p>Hi and thank you for your reply.<br>
The stl file is not corrupted. It is an open surface meaning that the inlet and outlets are open. So your visualisation software is tying to close them and it fails.<br>
I have updated the dropbox folder and I provide also closed stl files.<br>
Try again if you like to see what is going on.</p>
<p>cheers<br>
Fotos</p>

---

## Post #4 by @chir.set (2023-01-18 17:14 UTC)

<p>Yep, the closed surface does not get altered in Slicer, I mean, the segmentation derived from your original file.</p>
<p>Now I made other processing today with a segmentation containing only 19 branches, i.e., much fewer than in your model. I took 12 mins. Too much. And it uses only one CPU core throughout. Only VMTK folks can say if this processing can be multi-threaded.</p>
<p>Debranching your model would probable end up with success in a few days, that’s obviously not a pragmatic workflow. As for ‘How will so many branches help you in practice ?’, well, …</p>
<p>We learn that less is better here.</p>

---

## Post #5 by @Fotos_Stylianou (2023-01-19 09:24 UTC)

<p>any other ideas are welcome from the VMTK folks…</p>

---

## Post #6 by @rbumm (2023-01-19 13:59 UTC)

<p>This is a great airway segmentation, would be interested in how you generated it.</p>
<p>Are you running vmtkbranchclipper from an extension in 3d Slicer, from the Python console, or from the command line?</p>

---

## Post #7 by @chir.set (2023-01-19 17:04 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="6" data-topic="27303">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Are you running vmtkbranchclipper from an extension in 3d Slicer, from the Python console, or from the command line?</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="Fotos_Stylianou" data-post="1" data-topic="27303">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fotos_stylianou/48/18053_2.png" class="avatar"> Fotos_Stylianou:</div>
<blockquote>
<p>The command I am using is this<br>
“~/vmtk_Py36/vmtk/bin/vmtkbranchclipper</p>
</blockquote>
</aside>
<p>It seems <a class="mention" href="/u/fotos_stylianou">@Fotos_Stylianou</a> is using the command line, and I am using a newly available module in SlicerVMTK, based on vmtkbranchclipper.py.</p>
<p>But the bottleneck is <a href="https://github.com/vmtk/vmtk/blob/a0ed7931c458bf43795b895370fbe16f729e24f4/vtkVmtk/ComputationalGeometry/vtkvmtkPolyDataCenterlineGroupsClipper.cxx#L290" rel="noopener nofollow ugc">here</a>. Too many points in the surface, and too many branches will definitely be very long to process on one single CPU core.</p>

---

## Post #8 by @rbumm (2023-01-19 18:58 UTC)

<p>Maybe trivial, but you may see on a CPU / GPU monitoring tool (I currently use and recommend <a href="https://www.cpuid.com/softwares/hwmonitor.html">CPUid HWMonitor classic</a> on Windows) where the hardware performance bottlenecks really are at certain points of a script.</p>

---

## Post #9 by @Fotos_Stylianou (2023-01-20 11:54 UTC)

<p>Many thanks for your responses.<br>
<a class="mention" href="/u/rbumm">@rbumm</a> the segmentation mask is processed with meshmixer to reach the level you see at the images. I did some magic also with vmtk for the outlets.<br>
<a class="mention" href="/u/chir.set">@chir.set</a> thank you for pinpointing where the bottleneck is. Hopefully the VMTK team will look into it.<br>
I have to say that even if I reduce (by a lot) the number of cells on the surface mesh still the command does not produce anything. I believe that the number of branches is the problem.<br>
Anyhow, I was not expecting a quick solution.</p>
<p>By the way I found an other way to get something similar to what branchclipper does by using paraview. And it runs like in 1 second. So that is why I say that the vmtk branchclipper needs some rewriting and optimisation.</p>
<p>I summarise my steps in paraview with the images below in case someone might end up in my situation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3ae0caa49f1d93df3809e084bb84749ea49af13.jpeg" data-download-href="/uploads/short-url/yLGVk98u9mkhkZAxopXucfjh3tV.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3ae0caa49f1d93df3809e084bb84749ea49af13_2_673x500.jpeg" alt="1" data-base62-sha1="yLGVk98u9mkhkZAxopXucfjh3tV" width="673" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3ae0caa49f1d93df3809e084bb84749ea49af13_2_673x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3ae0caa49f1d93df3809e084bb84749ea49af13_2_1009x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3ae0caa49f1d93df3809e084bb84749ea49af13_2_1346x1000.jpeg 2x" data-dominant-color="A3A6B1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1705×1265 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d28a03b2d3fed9d677b79405846df3831b8246ae.jpeg" data-download-href="/uploads/short-url/u2vXJfr9fb1La6uo2XhELoeFmFg.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d28a03b2d3fed9d677b79405846df3831b8246ae_2_676x500.jpeg" alt="2" data-base62-sha1="u2vXJfr9fb1La6uo2XhELoeFmFg" width="676" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d28a03b2d3fed9d677b79405846df3831b8246ae_2_676x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d28a03b2d3fed9d677b79405846df3831b8246ae_2_1014x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d28a03b2d3fed9d677b79405846df3831b8246ae_2_1352x1000.jpeg 2x" data-dominant-color="9FA5AE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1707×1262 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96bbb4593bcdb70eb70e301afffc4082ca0f7f8e.jpeg" data-download-href="/uploads/short-url/lvrM5jhlhp8sFEMjIVSVavA5K6G.jpeg?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96bbb4593bcdb70eb70e301afffc4082ca0f7f8e_2_678x500.jpeg" alt="3" data-base62-sha1="lvrM5jhlhp8sFEMjIVSVavA5K6G" width="678" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96bbb4593bcdb70eb70e301afffc4082ca0f7f8e_2_678x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96bbb4593bcdb70eb70e301afffc4082ca0f7f8e_2_1017x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96bbb4593bcdb70eb70e301afffc4082ca0f7f8e_2_1356x1000.jpeg 2x" data-dominant-color="A59EA8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1716×1265 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
the last two steps follow in the next post because I can only add 3 images per post</p>
<p>I will be deleting the dropbox folder next week because I do not want my geometry circulating the internet.</p>
<p>Many Thanks for your responses!</p>

---

## Post #10 by @Fotos_Stylianou (2023-01-20 11:55 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b595f4efaddcca77baec23e2a698420073e5fe6.jpeg" data-download-href="/uploads/short-url/8t1EiGRCP3PiTqunV34mVTYAdMi.jpeg?dl=1" title="4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b595f4efaddcca77baec23e2a698420073e5fe6_2_676x500.jpeg" alt="4" data-base62-sha1="8t1EiGRCP3PiTqunV34mVTYAdMi" width="676" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b595f4efaddcca77baec23e2a698420073e5fe6_2_676x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b595f4efaddcca77baec23e2a698420073e5fe6_2_1014x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b595f4efaddcca77baec23e2a698420073e5fe6_2_1352x1000.jpeg 2x" data-dominant-color="A59FAA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4</span><span class="informations">1703×1258 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/831d44b871e568db0a9247753029d82541ef73c0.jpeg" data-download-href="/uploads/short-url/iHTfRX4eUxJfgsJNnUp5WSFSP3q.jpeg?dl=1" title="5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/831d44b871e568db0a9247753029d82541ef73c0_2_676x500.jpeg" alt="5" data-base62-sha1="iHTfRX4eUxJfgsJNnUp5WSFSP3q" width="676" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/831d44b871e568db0a9247753029d82541ef73c0_2_676x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/831d44b871e568db0a9247753029d82541ef73c0_2_1014x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/831d44b871e568db0a9247753029d82541ef73c0_2_1352x1000.jpeg 2x" data-dominant-color="B7818E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5</span><span class="informations">1707×1261 315 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
