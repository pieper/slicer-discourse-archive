---
topic_id: 14999
title: "Influence Of Spacing On Quality"
date: 2020-12-10
url: https://discourse.slicer.org/t/14999
---

# Influence of spacing on quality

**Topic ID**: 14999
**Date**: 2020-12-10
**URL**: https://discourse.slicer.org/t/influence-of-spacing-on-quality/14999

---

## Post #1 by @Andreas (2020-12-10 22:34 UTC)

<p>Hello everyone,</p>
<p>I’m trying to reduce the spacing using cropped volume in order to create very thin walls with a uniform thickness, but the spacing of the cropped volume is again at 0.2826 mm. So it makes no difference whether I use cropped volume or not.<br>
With a required wall thickness of 0.2 mm, the spacing of ± 0.2826mm is much too high.</p>
<p>I can adjust the oversampling factor, but I ask myself, why wasn’t the spacing already reduced with Cropped Volume?</p>
<p>My main problem is the high loss of quality and that everything runs very jerkily. The program often crashes completely despite 64 GB of RAM. When I try to smooth it out with Smoothing / Median the process takes infinitely and unacceptably long.</p>
<p>Many thanks for your help</p>
<p>Yours sincerely</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99eb81bae2fa5c7d1b5e96ad4976e397bf98a887.jpeg" data-download-href="/uploads/short-url/lXDCGcbAdEMVcsVaT6Nak1fn8X5.jpeg?dl=1" title="cropped volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/99eb81bae2fa5c7d1b5e96ad4976e397bf98a887_2_446x500.jpeg" alt="cropped volume" data-base62-sha1="lXDCGcbAdEMVcsVaT6Nak1fn8X5" width="446" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/99eb81bae2fa5c7d1b5e96ad4976e397bf98a887_2_446x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/99eb81bae2fa5c7d1b5e96ad4976e397bf98a887_2_669x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99eb81bae2fa5c7d1b5e96ad4976e397bf98a887.jpeg 2x" data-dominant-color="F4F5F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cropped volume</span><span class="informations">734×822 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd1b281b1a92f97cf5fb4fd8f2b4038f9c5fad0b.jpeg" alt="spacing still high" data-base62-sha1="vxZHDBMAMFxgt0Npd5cl4YkcrnJ" width="482" height="373"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c11ed8be14f54131533ed8b8f5d039db47fc7cf.jpeg" alt="oversampling" data-base62-sha1="1IM8GgtKC04kYhZ3AXME6qxENcj" width="494" height="373"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17582d096f39f52d83dbacf9ec72a9fcd4c3292e.jpeg" data-download-href="/uploads/short-url/3kvTFphjxSUEqxqiXJL9IWFyrNA.jpeg?dl=1" title="oversampling example" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/17582d096f39f52d83dbacf9ec72a9fcd4c3292e_2_689x258.jpeg" alt="oversampling example" data-base62-sha1="3kvTFphjxSUEqxqiXJL9IWFyrNA" width="689" height="258" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/17582d096f39f52d83dbacf9ec72a9fcd4c3292e_2_689x258.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/17582d096f39f52d83dbacf9ec72a9fcd4c3292e_2_1033x387.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/17582d096f39f52d83dbacf9ec72a9fcd4c3292e_2_1378x516.jpeg 2x" data-dominant-color="A39FCC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">oversampling example</span><span class="informations">2392×896 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-12-11 04:41 UTC)

<p>Once the segmentation geometry is established, changing the master volume does not make any difference (it was just used to determine the geometry at the beginning).</p>
<p>You have many options, I think I described a n previous posts already, but let’s summarize them again:</p>
<p>A. Not use so thin vessel walls. You cannot print a vessel with 0.2mm wall thickness, as it will crumble. Usually you either need accurate inner <em>or</em> outer diameter, but not both, so you can use a thicker wall. Patient-specific material properties are never known, therefore there it is not a problem that you don’t reproduce the wall thickness accurately. Thin vessel walls and leaflets are commonly reproduced by painting thin silicon layer on solid parts, as current 3D printing materials are still very far from properties of real vessels and soft tissues. FEM analysis if thib structures is often  more robust if you use shell elements instead of volumetric elements. So, overall, there is a very high chance ghat you don’t actually need extremely thin walls.</p>
<p>B. Use binary labelmap representation. Use just small enough voxels and crop the volume to minimum size. You can do the vessel segmentation at coarser resolution and oversample only for the final hollowing operation. Buy lots of RAM to keep things fast or just be patient, as all operations are slow on extremely large volumes.</p>
<p>C. Create hollow model in closed surface representation. You can represent arbitrarily thin walls in a surface mesh, without significant memory increase (just need about 2x more cells to have a double walls). The difficulty is of course how to make a mesh hollow. A common technique is to create an offset surface using the mesh normal. This typically generates invalid (self-intersecting) meshes, but if the wall is very thin then these errors may be negligible or relatively easily fixable</p>

---

## Post #3 by @Andreas (2020-12-14 21:45 UTC)

<p>Hello Mr. Lasso,</p>
<p>I understood your explanation of point C as shown in the attached video.<br>
However, I do not know whether spacing was used here and whether the wall thickness is the same everywhere.</p>
<p>          </p><div class="onebox video-onebox">
            <video width="100%" height="100%" controls="">
              <source src="https://dl.dropboxusercontent.com/s/v46xzcgk83bodhd/closed%20surface%20representation.mp4?dl=0">
              <a href="https://dl.dropboxusercontent.com/s/v46xzcgk83bodhd/closed%20surface%20representation.mp4?dl=0" rel="noopener nofollow ugc">https://dl.dropboxusercontent.com/s/v46xzcgk83bodhd/closed%20surface%20representation.mp4?dl=0</a>
            </video>
          </div>


---

## Post #4 by @lassoan (2020-12-14 21:57 UTC)

<p>The video above shows option B.</p>
<p>Option C can be implemented in a few lines of Python code using VTK filters.</p>

---

## Post #5 by @Andreas (2020-12-14 23:15 UTC)

<p>Hello Mr. Lasso,</p>
<p>Thank you for putting so much effort into my questions. However, I have to admit that I do not currently have an overview of the individual processes and their specific properties / differences.</p>
<ol>
<li>
<p>In the posted video I had inserted the STL file and created the wall. ---- &gt; Binary label map.</p>
</li>
<li>
<p>Another method I know is the Crop Volume. This reduces the size of the image.</p>
</li>
<li>
<p>From the third method, I don’t know the name, but only the symbol <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/877ed58f105134fcdc7452a7036135383c6c6c33.png" alt="image" data-base62-sha1="jkEcn73AV3H9WrBIdft8td6AQLx" width="25" height="23"> , which looks like a cube. With this method I can increase the oversampling factor and thus adjust the spacing.</p>
</li>
</ol>
<p>I would like to know which of the three methods mentioned above is the best way to solve my problem.</p>
<p>Problem:</p>
<p>spacing<br>
even wall<br>
Quality of surface properties</p>
<p>I’m sure you have a suitable solution for me.</p>

---

## Post #6 by @lassoan (2020-12-15 02:01 UTC)

<p>In most cases <strong>option A or B</strong> works best, as it is robust and allows easy editing of the shell.</p>
<p>If you need extremely thin walls then <strong>option C</strong> may be the best because option B would require too much memory and while option C is generally unreliable, it works acceptably well for thin shells. You can get a shell model of a segment as shown in this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_hollow_model_from_boundary_of_solid_segment">example</a>. You need to then cut off the caps, for example using “Plane cut” tool of Dynamic modeler module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad9317a30b8a3dfb156d4bd9197b968d5b7f6b4a.jpeg" data-download-href="/uploads/short-url/oLvKgBp08HpE4BPJQG21q7ELX0S.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad9317a30b8a3dfb156d4bd9197b968d5b7f6b4a_2_690x418.jpeg" alt="image" data-base62-sha1="oLvKgBp08HpE4BPJQG21q7ELX0S" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad9317a30b8a3dfb156d4bd9197b968d5b7f6b4a_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad9317a30b8a3dfb156d4bd9197b968d5b7f6b4a_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad9317a30b8a3dfb156d4bd9197b968d5b7f6b4a_2_1380x836.jpeg 2x" data-dominant-color="ADAEAE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1369 474 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Based on what you describe, option C seems to be the most suitable solution for your particular use case.</p>

---

## Post #7 by @Andreas (2020-12-15 15:51 UTC)

<p>Dear Mr. Lasso,</p>
<p>I really like the Dynamic Modeler module for displaying the cutting planes.</p>
<p>I assume that by option C you mean creating a hollow model in a closed surface representation.</p>
<p>This option C is unfortunately not known to me.</p>
<p>You said it can be done with VTK filters and a few lines of phyton.</p>
<p>Unfortunately, I have no experience with programming languages and have not yet worked with the VTK filter.</p>
<p>My work now hangs only on this problem, which is why I would be very grateful for a detailed explanation.</p>

---

## Post #8 by @lassoan (2020-12-15 16:20 UTC)

<aside class="quote no-group" data-username="Andreas" data-post="7" data-topic="14999">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>Unfortunately, I have no experience with programming languages and have not yet worked with the VTK filter.</p>
</blockquote>
</aside>
<p>I gave a complete solution in my post above. You just need to copy those few lines of code into the Python console and you are done.</p>
<p>I also created a GUI for this (as a new “Hollow” tool in Dynamic modeler), which will be available in the Slicer Preview Release tomorrow.</p>

---

## Post #9 by @Andreas (2020-12-15 17:27 UTC)

<p>Dear Mr. Lasso,</p>
<p>I have inserted the codes from the above post one by one into the “Phyton Interactive”, however, nothing has changed in my segmented vessel model. I only used Scissors and Smoothing and wanted to do the Hollow with the help of the Phyton codes.</p>
<p>The following codes were added:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/988e8e800c3c132d3b7f50a74a22b95ef6045d7e.jpeg" data-download-href="/uploads/short-url/lLA06y38zbrFGe3fgEcgCeMmfOm.jpeg?dl=1" title="Create hollow" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/988e8e800c3c132d3b7f50a74a22b95ef6045d7e_2_690x240.jpeg" alt="Create hollow" data-base62-sha1="lLA06y38zbrFGe3fgEcgCeMmfOm" width="690" height="240" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/988e8e800c3c132d3b7f50a74a22b95ef6045d7e_2_690x240.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/988e8e800c3c132d3b7f50a74a22b95ef6045d7e_2_1035x360.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/988e8e800c3c132d3b7f50a74a22b95ef6045d7e_2_1380x480.jpeg 2x" data-dominant-color="F2F3F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Create hollow</span><span class="informations">1454×506 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Will it be possible to use the new GUI in the stable 3D slicer version? In my work I only want to include functions that can be used in the stable version.</p>
<p>I also tried to reproduce their illustration/screenshot from the Dynamic modeler module with plane cut on a simplified model, unfortunately I was not able to create a cut plane.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac933f5b3a20174b16163929f8b9c318a0cbdad5.jpeg" data-download-href="/uploads/short-url/oCFBh0UYFjhmrh70qLsilLlx7W5.jpeg?dl=1" title="Plane cut" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac933f5b3a20174b16163929f8b9c318a0cbdad5_2_690x400.jpeg" alt="Plane cut" data-base62-sha1="oCFBh0UYFjhmrh70qLsilLlx7W5" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac933f5b3a20174b16163929f8b9c318a0cbdad5_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac933f5b3a20174b16163929f8b9c318a0cbdad5_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac933f5b3a20174b16163929f8b9c318a0cbdad5_2_1380x800.jpeg 2x" data-dominant-color="7C7C82"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Plane cut</span><span class="informations">1678×974 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @lassoan (2020-12-15 20:25 UTC)

<p>To use the code snippet, you need to replace the example node name (<code>Segmentation</code>) and segment ID (<code>Segment_1</code>) with you actual node name and segment ID.</p>
<p>New features are not added to stable releases, so you’ll need to use a preview release. You can pick any preview release and keep using that, thereby it can serve as your own “stable release”.</p>

---

## Post #11 by @Andreas (2020-12-15 22:10 UTC)

<p>Hello Mr. Lasso,</p>
<p>In the attachment I send you a photo of the attempt to apply the Phyton code, but nothing changes. The example node name and segment ID would actually have to match the template. ( see photo)</p>
<p>What’s the mistake?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71dfa735208624893aacf3f530e0250c6a92a542.jpeg" alt="shellthickness" data-base62-sha1="gfn7ZeMjmlt2lh2xk1brpkB6ydQ" width="668" height="461"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a41f616e262b8942c4a15c73ca2908e0df487a3.jpeg" alt="node" data-base62-sha1="f9ZVRuYUEzunASLoFC4dP97mrdN" width="617" height="158"></p>

---

## Post #12 by @lassoan (2020-12-15 22:16 UTC)

<p>It looks good except you missed the last two lines of the script.</p>

---

## Post #13 by @Andreas (2020-12-15 22:41 UTC)

<p>I’ve added the last two lines from the script and it also forms a gold-colored vessel wall, but it still doesn’t work.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/475046645055fe10685dd1e6a9610c5097a1f6df.jpeg" alt="shellthickness2" data-base62-sha1="aaRT6gLeMeyrK6fgL6KhT88FU6j" width="677" height="480"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a149867c45f7fe0318a376aae32bf4cd5116bdd.jpeg" data-download-href="/uploads/short-url/jHw10lIY5DwewUuecCb2ZAA4ebr.jpeg?dl=1" title="model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a149867c45f7fe0318a376aae32bf4cd5116bdd_2_690x302.jpeg" alt="model" data-base62-sha1="jHw10lIY5DwewUuecCb2ZAA4ebr" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a149867c45f7fe0318a376aae32bf4cd5116bdd_2_690x302.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a149867c45f7fe0318a376aae32bf4cd5116bdd_2_1035x453.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a149867c45f7fe0318a376aae32bf4cd5116bdd_2_1380x604.jpeg 2x" data-dominant-color="C2BCBF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">model</span><span class="informations">1680×737 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #14 by @lassoan (2020-12-15 23:15 UTC)

<p>That’s it, that yellow model is the result. If you clip it or enable 2D visibility then you will see that it is a thin shell.</p>

---

## Post #15 by @Andreas (2020-12-15 23:47 UTC)

<p>In the 2D visibility the shell of 3. 0mm is not shown to me. Hiding out the internal segmentation does not help either.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/339148cb082561eee5b068aa6aa2f6e3b1dfbcca.jpeg" data-download-href="/uploads/short-url/7mbCwaKacEljpE09oNsbp0bCFAK.jpeg?dl=1" title="no hollow" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/339148cb082561eee5b068aa6aa2f6e3b1dfbcca_2_690x402.jpeg" alt="no hollow" data-base62-sha1="7mbCwaKacEljpE09oNsbp0bCFAK" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/339148cb082561eee5b068aa6aa2f6e3b1dfbcca_2_690x402.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/339148cb082561eee5b068aa6aa2f6e3b1dfbcca_2_1035x603.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/339148cb082561eee5b068aa6aa2f6e3b1dfbcca_2_1380x804.jpeg 2x" data-dominant-color="7C7C81"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">no hollow</span><span class="informations">1678×978 272 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #16 by @lassoan (2020-12-15 23:57 UTC)

<p>You need to enable 2D visibility for the model (the yellow object) that you created. You can show it by right-clicking on the model node’s eye icon in Data module (and you have access to many more visibility options in the Models module).</p>

---

## Post #17 by @Andreas (2020-12-16 00:09 UTC)

<p>I have right-clicked on Model and clicked on Convert model to segmentation node, but I can’t cut with the scissors</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92cd7dc05d54019866c5ce57a7c56767b8aecb83.jpeg" data-download-href="/uploads/short-url/kWFYmsUp79kGwTh7GAJZWrcjK8j.jpeg?dl=1" title="model segmentation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92cd7dc05d54019866c5ce57a7c56767b8aecb83_2_690x401.jpeg" alt="model segmentation" data-base62-sha1="kWFYmsUp79kGwTh7GAJZWrcjK8j" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92cd7dc05d54019866c5ce57a7c56767b8aecb83_2_690x401.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92cd7dc05d54019866c5ce57a7c56767b8aecb83_2_1035x601.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92cd7dc05d54019866c5ce57a7c56767b8aecb83_2_1380x802.jpeg 2x" data-dominant-color="848586"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">model segmentation</span><span class="informations">1680×978 260 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #18 by @lassoan (2020-12-16 02:04 UTC)

<p>Yo don’t convert this thin-shell model to segmentation node. You cannot represent this thin smooth shell as a binary labelmap. If you could, then you would have chosen option B. Instead, you need to do the conversion to shell as a very last step of the segment editing. After that, you can only edit the model, using Dynamic modeler, Surface toolbox, and other modules that operate on surface meshes. You can also edit meshes in external software, such as MeshMixer (easy to learn) or Blender (it is the 3D Slicer equivalent of 3D modeling - very powerful and very hard to learn).</p>

---

## Post #19 by @Andreas (2020-12-16 14:02 UTC)

<p>Hello Mr. Lasso,</p>
<p>after I had inserted the Python codes from your script, the yellow model got. I have hidden the inside of the model and obtained the desired image in the 2-D representation. Now it’s time to cut the ends. Which module is the best way to do this? I would like to know how to save the hollow body as STL file. In the appendix I have added screenshots to my questions.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1af826c11a3815e90e0dd986759e54843a02708d.jpeg" data-download-href="/uploads/short-url/3QA4IBvsFcujWIy1Kyhwz1hQ4uF.jpeg?dl=1" title="model (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1af826c11a3815e90e0dd986759e54843a02708d_2_690x401.jpeg" alt="model (1)" data-base62-sha1="3QA4IBvsFcujWIy1Kyhwz1hQ4uF" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1af826c11a3815e90e0dd986759e54843a02708d_2_690x401.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1af826c11a3815e90e0dd986759e54843a02708d_2_1035x601.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1af826c11a3815e90e0dd986759e54843a02708d_2_1380x802.jpeg 2x" data-dominant-color="7D7E81"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">model (1)</span><span class="informations">1680×978 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #20 by @lassoan (2020-12-16 14:39 UTC)

<p>Dynamic modeler - see <a href="https://discourse.slicer.org/t/influence-of-spacing-on-quality/14999/6">above</a>.</p>

---

## Post #21 by @Andreas (2020-12-16 15:24 UTC)

<p>Hello Mr. Lasso,</p>
<p>I was looking for a suitable example to explain the Dynamic Modeler a bit more precisely. I came across this video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="F6fNMQTxD-4" data-video-title="3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=F6fNMQTxD-4" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/F6fNMQTxD-4/maxresdefault.jpg" title="3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications" width="" height="">
  </a>
</div>

<p>Do I need to put MarkupsPlane as in this video? In your screenshot you have Plane node [1]: Red.<br>
How exactly does that work?</p>

---

## Post #22 by @lassoan (2020-12-16 15:28 UTC)

<p>Yes, you need to specify a cutting plane to cut the mesh. I would recommend to use a markups plane, defined by clicking 3 points around the vessel tip (you can adjust position/orientation by enabling interaction handles).</p>

---

## Post #23 by @Andreas (2020-12-16 15:59 UTC)

<p>I have now added a markups plane on both ends but only the model can be hidden.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a8cfe70b2c55199af44e74395d68d9c9d23810f.jpeg" data-download-href="/uploads/short-url/1vkQRZXpju6rPfdtGDY3VqdjPav.jpeg?dl=1" title="plane cut (2)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a8cfe70b2c55199af44e74395d68d9c9d23810f_2_690x400.jpeg" alt="plane cut (2)" data-base62-sha1="1vkQRZXpju6rPfdtGDY3VqdjPav" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a8cfe70b2c55199af44e74395d68d9c9d23810f_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a8cfe70b2c55199af44e74395d68d9c9d23810f_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a8cfe70b2c55199af44e74395d68d9c9d23810f_2_1380x800.jpeg 2x" data-dominant-color="7D7D82"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">plane cut (2)</span><span class="informations">1680×974 260 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6eca7723fba69800e75582659e3df1d09d49616.jpeg" data-download-href="/uploads/short-url/zeoub9LY98mpwA4xyMImAHnmyOi.jpeg?dl=1" title="plane cut (3)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6eca7723fba69800e75582659e3df1d09d49616_2_690x400.jpeg" alt="plane cut (3)" data-base62-sha1="zeoub9LY98mpwA4xyMImAHnmyOi" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6eca7723fba69800e75582659e3df1d09d49616_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6eca7723fba69800e75582659e3df1d09d49616_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6eca7723fba69800e75582659e3df1d09d49616_2_1380x800.jpeg 2x" data-dominant-color="7E7C81"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">plane cut (3)</span><span class="informations">1680×974 261 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #24 by @Andreas (2020-12-16 18:34 UTC)

<p>Can you please tell me how to save the new model as STL. Do I need to convert it first?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/452105054e04c52d2d4ecdf9caf22e98c0ce1693.jpeg" data-download-href="/uploads/short-url/9RxGL1OTpvqL6kcApRJzjSweKQP.jpeg?dl=1" title="stl file" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/452105054e04c52d2d4ecdf9caf22e98c0ce1693_2_690x400.jpeg" alt="stl file" data-base62-sha1="9RxGL1OTpvqL6kcApRJzjSweKQP" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/452105054e04c52d2d4ecdf9caf22e98c0ce1693_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/452105054e04c52d2d4ecdf9caf22e98c0ce1693_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/452105054e04c52d2d4ecdf9caf22e98c0ce1693_2_1380x800.jpeg 2x" data-dominant-color="7C7B7F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">stl file</span><span class="informations">1680×974 263 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #25 by @lassoan (2020-12-17 05:12 UTC)

<p>See how to save data in the documentation: <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#non-dicom-data">https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#non-dicom-data</a></p>

---

## Post #26 by @Andreas (2020-12-17 15:07 UTC)

<p>Dear Mr Lasso,</p>
<p>I have tried to apply the principle with the Markup Planes to more complex vessel models with several openings, but I have the problem that the cut plane is not limited to the red field/window, but runs completely through the axis and cuts out other segments I need. ( see figure)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b23059ca5717a68e0afaacd60aa2743ac7c97b4b.jpeg" data-download-href="/uploads/short-url/pqkA0kmhKlvdKR2sSybM18jdSH1.jpeg?dl=1" title="MarkUps Plane Problem" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b23059ca5717a68e0afaacd60aa2743ac7c97b4b_2_690x400.jpeg" alt="MarkUps Plane Problem" data-base62-sha1="pqkA0kmhKlvdKR2sSybM18jdSH1" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b23059ca5717a68e0afaacd60aa2743ac7c97b4b_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b23059ca5717a68e0afaacd60aa2743ac7c97b4b_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b23059ca5717a68e0afaacd60aa2743ac7c97b4b_2_1380x800.jpeg 2x" data-dominant-color="BDBBD4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MarkUps Plane Problem</span><span class="informations">1680×974 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #27 by @lassoan (2020-12-17 15:58 UTC)

<p>You can choose how to combine multiple cutting planes (union/intersect) and thereby limit what is cut by a plane by adding more planes. In this case, you need to use a separate cut plane tool and set of planes for cutting off each tip.</p>
<p>We will add a markups ROI widget within a few months, which will make cutting with a finite plane easier.</p>
<p>You can also use other cutting tools in Dynamic modeler, but they don’t generate a straight cut but instead cut along the mesh edges.</p>

---

## Post #28 by @Andreas (2020-12-17 17:17 UTC)

<p>Dear Mr Lasso,</p>
<p>Unfortunately, the cutting tool “Curve Cut” in the Dynamic Modeler did not work and the “Portal”/Curve can not really be aligned well in three-dimensional space. ( probably a matter of practice). With the “Boundary Cut” cutting tool, the same thing happens as with “Plane Cut”, here too the cut runs along the entire axis and segments are removed. I haven’t tested the functions Mirror and Append yet. (I don’t want to mirror anything)</p>
<p>I would prefer the solution with MarkUp Planes, but I don’t know how to implement your solution proposal. Operation type Union did not help (single problem) and nothing happens with Operation type: Intersection.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6f25b9460ef92feea3bcce8f0876a329d20e134.jpeg" data-download-href="/uploads/short-url/uFvqwaAwRaAk4IQYjb2CJgfK5qk.jpeg?dl=1" title="curve cut" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6f25b9460ef92feea3bcce8f0876a329d20e134_2_690x400.jpeg" alt="curve cut" data-base62-sha1="uFvqwaAwRaAk4IQYjb2CJgfK5qk" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6f25b9460ef92feea3bcce8f0876a329d20e134_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6f25b9460ef92feea3bcce8f0876a329d20e134_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6f25b9460ef92feea3bcce8f0876a329d20e134_2_1380x800.jpeg 2x" data-dominant-color="BFBFD6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">curve cut</span><span class="informations">1680×976 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abd0242f7c2cb7c1352b4a51dd7ac094d5ee0e94.jpeg" alt="create" data-base62-sha1="ovVAta3mVMYvvJavrgXLGRpAezi" width="630" height="38"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/841a0e86d78c39ff8b35cd0a511aa15e12eea2f9.jpeg" alt="union" data-base62-sha1="iQCQQH582M4ZaPfrdal9uQSE11n" width="626" height="213"></p>

---

## Post #29 by @lassoan (2020-12-17 17:37 UTC)

<p>With a single plane, tip of the other vessel segment is clipped:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb9e94e35e8738fc7a8792716a9896b135f603d4.png" data-download-href="/uploads/short-url/xCnXPFw0RsZNL9NOc4MS3Mo33j6.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb9e94e35e8738fc7a8792716a9896b135f603d4_2_690x419.png" alt="image" data-base62-sha1="xCnXPFw0RsZNL9NOc4MS3Mo33j6" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb9e94e35e8738fc7a8792716a9896b135f603d4_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb9e94e35e8738fc7a8792716a9896b135f603d4_2_1035x628.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb9e94e35e8738fc7a8792716a9896b135f603d4_2_1380x838.png 2x" data-dominant-color="B9BDD8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1371 495 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>By adding a second plane and choosing intersection operation, we can prevent second clipping:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91a2f698cfff65c56b64ba4794a04ce529d30e88.png" data-download-href="/uploads/short-url/kMmnAia62SZmAiNsOWTOWoK7BUY.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91a2f698cfff65c56b64ba4794a04ce529d30e88_2_690x419.png" alt="image" data-base62-sha1="kMmnAia62SZmAiNsOWTOWoK7BUY" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91a2f698cfff65c56b64ba4794a04ce529d30e88_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91a2f698cfff65c56b64ba4794a04ce529d30e88_2_1035x628.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91a2f698cfff65c56b64ba4794a04ce529d30e88_2_1380x838.png 2x" data-dominant-color="B9BDD6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1371 545 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #30 by @Andreas (2020-12-17 22:03 UTC)

<p>Dear Mr Lasso,</p>
<p>Thank you very much for the illustration. Adding the second level and selecting the intersection operation worked very well. ( see figure)</p>
<p>My problem is to make several openings. As soon as I make a new plane Cut, the previous opening is closed/deleted again. I have already tried to add the plane Cuts to a folder, but then the program crashes. Another question is, is it possible to fix placed plane markups so that they can’t move accidentally? Even if I have hidden this has happened to me many times and measurements have then not been correct.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f162107eef087d9f690132b63bf2f4477ad42d1c.jpeg" data-download-href="/uploads/short-url/yrnaGXhMNTSJmPxkDvSr0MotI1m.jpeg?dl=1" title="plane cut intersection" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f162107eef087d9f690132b63bf2f4477ad42d1c_2_690x400.jpeg" alt="plane cut intersection" data-base62-sha1="yrnaGXhMNTSJmPxkDvSr0MotI1m" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f162107eef087d9f690132b63bf2f4477ad42d1c_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f162107eef087d9f690132b63bf2f4477ad42d1c_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f162107eef087d9f690132b63bf2f4477ad42d1c_2_1380x800.jpeg 2x" data-dominant-color="C0BED7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">plane cut intersection</span><span class="informations">1680×976 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #31 by @lassoan (2020-12-17 22:27 UTC)

<p>To make multiple cuts, use result of the previous cut as input for the next cut.</p>

---

## Post #32 by @Andreas (2020-12-17 23:26 UTC)

<p>Dear Mr Lasso,</p>
<p>I am very enthusiastic about the result with this thin wall thickness and thank you again for your support and patience.</p>
<p>I have the feeling that with this variant (Option C) the spacing has been removed or is the impression deceiving?</p>
<p>Why is the computing power required when using the graphical user interface (GUI) and why is it not when using a Phyton code? Do you have an explanation for this?</p>

---

## Post #33 by @lassoan (2020-12-20 23:36 UTC)

<p>Model (surface mesh) representation can easily represent thin walls, but it is not robust when the surface is very complex (e.g., result of thresholding a noisy image). Compared to labelmaps, meshes are very hard to edit (we currently only a few different operations, such as cuts, mirroring, appending).</p>
<p>3D printers use surface meshes as inputs.</p>
<p>Finite element solvers use volumetric meshes, which are easier to generate from labelmaps.</p>
<p>Both representations (surface mesh, labelmap) have advantages and disadvantages. You need to use the representation that works the best for the specific task.</p>

---

## Post #34 by @Andreas (2020-12-22 03:39 UTC)

<p>I still have two questions on the subject:</p>
<p>Why does a shadow regularly appear on the cutting planes? I noticed that this shadow does not appear on the last cut plane.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e9c6e555ac45cc984f5629ee37ede80d13d63fe.jpeg" data-download-href="/uploads/short-url/bdqosDaq7kHxGVnuK48KY0EyyVU.jpeg?dl=1" title="Shadow" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e9c6e555ac45cc984f5629ee37ede80d13d63fe_2_690x400.jpeg" alt="Shadow" data-base62-sha1="bdqosDaq7kHxGVnuK48KY0EyyVU" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e9c6e555ac45cc984f5629ee37ede80d13d63fe_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e9c6e555ac45cc984f5629ee37ede80d13d63fe_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e9c6e555ac45cc984f5629ee37ede80d13d63fe_2_1380x800.jpeg 2x" data-dominant-color="CDB3AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Shadow</span><span class="informations">1680×974 185 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h1><a name="p-51964-h-1" class="anchor" href="#p-51964-h-1" aria-label="Heading link"></a></h1>
<p>The second question would be, if I have to create many cutting planes and thus also create many models, it can quickly become confusing. Is there any way to make this a little clearer?</p>
<h1><a name="p-51964-h-2" class="anchor" href="#p-51964-h-2" aria-label="Heading link"></a></h1>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfb556f332c844b32f59e06eb43dcfafa9b484ae.jpeg" data-download-href="/uploads/short-url/tDtlZNSu2OVOUduaGFZ8pALG698.jpeg?dl=1" title="Shadow and many models" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfb556f332c844b32f59e06eb43dcfafa9b484ae_2_690x400.jpeg" alt="Shadow and many models" data-base62-sha1="tDtlZNSu2OVOUduaGFZ8pALG698" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfb556f332c844b32f59e06eb43dcfafa9b484ae_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfb556f332c844b32f59e06eb43dcfafa9b484ae_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfb556f332c844b32f59e06eb43dcfafa9b484ae_2_1380x800.jpeg 2x" data-dominant-color="C0BBBE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Shadow and many models</span><span class="informations">1680×976 209 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h1><a name="p-51964-h-3" class="anchor" href="#p-51964-h-3" aria-label="Heading link"></a></h1>
<p>Thanks for the help</p>

---

## Post #35 by @lassoan (2020-12-22 05:06 UTC)

<aside class="quote no-group" data-username="Andreas" data-post="34" data-topic="14999">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>Why does a shadow regularly appear on the cutting planes? I noticed that this shadow does not appear on the last cut plane.</p>
</blockquote>
</aside>
<p>You don’t need to worry about those shadows, they are just visualization artifacts. If you have very sharp edges in a surface then you may prefer to recompute surface normals with splitting enabled, for example using Surface Toolbox module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7f767945576ac2c88e11bec4e20f74afce496e4.png" data-download-href="/uploads/short-url/znBZOXj83axDjraYHNIhGUBAzd2.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7f767945576ac2c88e11bec4e20f74afce496e4_2_554x500.png" alt="image" data-base62-sha1="znBZOXj83axDjraYHNIhGUBAzd2" width="554" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7f767945576ac2c88e11bec4e20f74afce496e4_2_554x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7f767945576ac2c88e11bec4e20f74afce496e4_2_831x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7f767945576ac2c88e11bec4e20f74afce496e4_2_1108x1000.png 2x" data-dominant-color="C7C8C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1349×1217 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="Andreas" data-post="34" data-topic="14999">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>The second question would be, if I have to create many cutting planes and thus also create many models, it can quickly become confusing. Is there any way to make this a little clearer?</p>
</blockquote>
</aside>
<p>If you are willing to learn some Python scripting then you can implement some helper scripts that automate this. For example, you could create cutting planes automatically from 6 planes of a ROI node. Otherwise you probably need to wait for the new markups ROI widget to be added to Slicer (expected within a few months).</p>

---

## Post #36 by @Andreas (2021-01-01 21:49 UTC)

<p>Hello everybody,</p>
<p>I still have questions about binary labelmap (green color) and closed surface (blue color). ( see pictures)</p>
<ol>
<li>
<p>Is the previously segmented vascular lumen always a binary label map? ( Threshold + Segment Editor)</p>
</li>
<li>
<p>Does the “Hollow” effect in the Segment Editor module always belong to the binary label map and can it only be edited with the scissors?</p>
</li>
<li>
<p>Surface mesh representation (with Python code) for very thin vessel walls (without spacing) always belongs to the closed surface. Can this only be edited with the cutting planes?</p>
</li>
</ol>
<p>I’m all about understanding.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b8204e9ae0b317660523aba1184ca5af9dc6475.jpeg" data-download-href="/uploads/short-url/jU8VRjl1UDzimx3AX4PCoPqH4uV.jpeg?dl=1" title="labelmap -  surface1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b8204e9ae0b317660523aba1184ca5af9dc6475_2_690x343.jpeg" alt="labelmap -  surface1" data-base62-sha1="jU8VRjl1UDzimx3AX4PCoPqH4uV" width="690" height="343" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b8204e9ae0b317660523aba1184ca5af9dc6475_2_690x343.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b8204e9ae0b317660523aba1184ca5af9dc6475_2_1035x514.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b8204e9ae0b317660523aba1184ca5af9dc6475.jpeg 2x" data-dominant-color="EAE0ED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">labelmap -  surface1</span><span class="informations">1274×634 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2dbac34c719d8b7861d7c1d937795e0644e7083.jpeg" data-download-href="/uploads/short-url/neHZNxKS8nwH0wbJ806Z0i5WTRh.jpeg?dl=1" title="segment1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2dbac34c719d8b7861d7c1d937795e0644e7083_2_690x362.jpeg" alt="segment1" data-base62-sha1="neHZNxKS8nwH0wbJ806Z0i5WTRh" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2dbac34c719d8b7861d7c1d937795e0644e7083_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2dbac34c719d8b7861d7c1d937795e0644e7083.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2dbac34c719d8b7861d7c1d937795e0644e7083.jpeg 2x" data-dominant-color="D5E5DD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segment1</span><span class="informations">754×396 68 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
