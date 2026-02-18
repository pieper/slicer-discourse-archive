# Exporting a segmentation paired to a custom colortable

**Topic ID**: 35719
**Date**: 2024-04-24
**URL**: https://discourse.slicer.org/t/exporting-a-segmentation-paired-to-a-custom-colortable/35719

---

## Post #1 by @jhlegarreta (2024-04-24 21:33 UTC)

<p>Hi,<br>
I’ve been reading the threads about naming/numbering and the colormaps for segmentations:<br>
<a href="https://discourse.slicer.org/t/export-segmentation-as-labeled-labelmap/26468" class="inline-onebox">Export Segmentation as Labeled LabelMap</a><br>
<a href="https://discourse.slicer.org/t/copying-segment-names-colors-from-one-segmentation-to-another/21204" class="inline-onebox">Copying segment names/colors from one segmentation to another</a></p>
<p>I am not sure to be able to export the labels according to the colortable properly: similar to <a class="mention" href="/u/apparrilla">@apparrilla</a>, I have a colortable that has e.g. 37 (0, 36) consecutive labels. I am manually segmenting structures e.g. 29 and 35. When exporting them, if I pick the colortable that I am using, they are numbered as 37, 38 (besides the background, 0), which I would say is not expected already.</p>
<p>Additionally, if I try to load the exported NIfTI file into Slicer and choose the colortable at issue, they get colored with the RGBA values corresponding to label IDs 1 and 2 in the original colortable.</p>
<p>If I load a segmentation file (automatically generated with another tool) that contains 35 labels (0, 34), and if I load my 37 consecutive label table and set it as the color node for the segmentation to be loaded, they are colored and named following the colortable, as expected.</p>
<p>I’m wondering what step I am missing in all this to be unable to export labels properly.</p>
<p>Thanks.</p>

---

## Post #2 by @muratmaga (2024-04-24 22:36 UTC)

<p>Sharing the color table and a labelmap/segmentation would probably help. Without those it is hard to tell what you might be doing wrong or missing.</p>

---

## Post #3 by @muratmaga (2024-04-24 22:46 UTC)

<aside class="quote no-group" data-username="jhlegarreta" data-post="1" data-topic="35719">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>I am manually segmenting structures e.g. 29 and 35. When exporting them, if I pick the colortable that I am using, they are numbered as 37, 38 (besides the background, 0), which I would say is not expected already.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I can replicate this behavior on latest stable.</p>
<ol>
<li>I created two segments on MRHead called <strong>left_ventricle_chamber</strong> and <strong>right_cerebellar_primordium</strong></li>
<li>Used this color table during the export: <a href="https://github.com/SlicerMorph/MD_E15/blob/main/KOMP2.ctbl" class="inline-onebox">MD_E15/KOMP2.ctbl at main · SlicerMorph/MD_E15 · GitHub</a></li>
</ol>
<p>As opposed to being assigned to indices 44 and 49 as expected, they were assigned 51 and 52.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe1674d669c98532164f62a557a24972e2429b3e.jpeg" data-download-href="/uploads/short-url/AfLobyfddjeEwsjLLGU5R2OeoMe.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe1674d669c98532164f62a557a24972e2429b3e_2_595x500.jpeg" alt="image" data-base62-sha1="AfLobyfddjeEwsjLLGU5R2OeoMe" width="595" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe1674d669c98532164f62a557a24972e2429b3e_2_595x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe1674d669c98532164f62a557a24972e2429b3e_2_892x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe1674d669c98532164f62a557a24972e2429b3e_2_1190x1000.jpeg 2x" data-dominant-color="949598"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1613 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @jhlegarreta (2024-04-24 23:00 UTC)

<p>Thanks for the quick reply <a class="mention" href="/u/muratmaga">@muratmaga</a>.</p>
<blockquote>
<p>Sharing the color table and a labelmap/segmentation would probably help. Without those it is hard to tell what you might be doing wrong or missing.</p>
</blockquote>
<p>You’re right. Not ideal to try to guess without data, but I chose not upload the data somewhere due to various constraints. Apologies.</p>
<blockquote>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I can replicate this behavior on latest stable.<br>
As opposed to being assigned to indices 44 and 49 as expected, they were assigned 51 and 52.</p>
</blockquote>
<p>OK. So looks like an undesired/unexpected behavior was introduced at some point. Forgot to tell that I am using version 5.2.2.</p>

---

## Post #5 by @lassoan (2024-04-25 02:12 UTC)

<p>I’ve tested Slicer-5.6.2 and everything works well: if a segment name matches a color name in the chosen table, then the label value in the exported labelmap volume is the color index.</p>
<p>What confused <a class="mention" href="/u/muratmaga">@muratmaga</a> was that internally in color table files, space character is stored as underscore (probably for easier parsing). In Colors module you can see the actual color names that must match the segment names:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53d1803246397090f99c4f24db26a30427236ef5.png" data-download-href="/uploads/short-url/bXutY4MA0x5M6QmK6TokjngHjJX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53d1803246397090f99c4f24db26a30427236ef5_2_463x499.png" alt="image" data-base62-sha1="bXutY4MA0x5M6QmK6TokjngHjJX" width="463" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53d1803246397090f99c4f24db26a30427236ef5_2_463x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53d1803246397090f99c4f24db26a30427236ef5_2_694x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53d1803246397090f99c4f24db26a30427236ef5.png 2x" data-dominant-color="3B3A3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">904×976 50.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>We know that this ctbl file format is inadequate and we should phase it out - see <a href="https://github.com/Slicer/Slicer/issues/7593" class="inline-onebox">Improve color table node format · Issue #7593 · Slicer/Slicer · GitHub</a></p>
<aside class="quote no-group" data-username="jhlegarreta" data-post="1" data-topic="35719">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>I am manually segmenting structures e.g. 29 and 35. When exporting them, if I pick the colortable that I am using, they are numbered as 37, 38 (besides the background, 0), which I would say is not expected already.</p>
</blockquote>
</aside>
<p>It all works well in the Latest Slicer Stable Release, so please use that. I don’t think it was broken in Slicer-5.2.1, too, but I have not tested it now. Most likely your segment names don’t match the color names that you selected for exporting to labelmap. But if you think something else is going on then please provide instructions and data. You can use any of the Slicer sample data sets.</p>
<hr>
<p>All this color table based matching is very fragile, even a single character mistyping may cause segments not to pair up with labels. Also, label values cannot be standardized between multiple projects. Therefore, I would recommend to move towards identifying segment content using standard terminology codes. They are global identifiers that can be shared between projects and they allow using different name variants and spelling for segment names.</p>

---

## Post #6 by @jhlegarreta (2024-04-25 16:55 UTC)

<p>Thanks for giving this a try <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>I made sure that I am using exactly the names in my colortable, and have simplified it to the following:</p>
<pre><code class="lang-auto"># Color table file my_colortable.txt
# 4 values
0 Background 0 0 0 0
1 Left 231 255 0 255
2 Right 111 231 0 255
3 New_I_name 0 230 92 255
4 Another_I_New_Name 30 30 102 255
</code></pre>
<p>As shown in the screenshots below, I am choosing the colortable at issue (have loaded different versions, thus the name <code>my_colortable_2</code> displayed), and I am getting the same result as yesterday.</p>
<p>Drawing:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/413cd39e107f88970172351fd7baf885f9369121.png" data-download-href="/uploads/short-url/9j7m4AVVb6qrPPmjqLluhI0Ofjr.png?dl=1" title="segmentation_labelling_issue_segmentation_draw_half" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/413cd39e107f88970172351fd7baf885f9369121_2_345x195.png" alt="segmentation_labelling_issue_segmentation_draw_half" data-base62-sha1="9j7m4AVVb6qrPPmjqLluhI0Ofjr" width="345" height="195" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/413cd39e107f88970172351fd7baf885f9369121_2_345x195.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/413cd39e107f88970172351fd7baf885f9369121_2_517x292.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/413cd39e107f88970172351fd7baf885f9369121_2_690x390.png 2x" data-dominant-color="888A90"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmentation_labelling_issue_segmentation_draw_half</span><span class="informations">929×527 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Exportation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df9a605e151fd291de79c3e5669bafee7c7a9f2c.png" data-download-href="/uploads/short-url/vU5e0lOq1ODP6MVBDcVK7IonFuY.png?dl=1" title="segmentation_labelling_issue_segmentation_export_half" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df9a605e151fd291de79c3e5669bafee7c7a9f2c_2_345x195.png" alt="segmentation_labelling_issue_segmentation_export_half" data-base62-sha1="vU5e0lOq1ODP6MVBDcVK7IonFuY" width="345" height="195" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df9a605e151fd291de79c3e5669bafee7c7a9f2c_2_345x195.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df9a605e151fd291de79c3e5669bafee7c7a9f2c_2_517x292.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df9a605e151fd291de79c3e5669bafee7c7a9f2c_2_690x390.png 2x" data-dominant-color="88898F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmentation_labelling_issue_segmentation_export_half</span><span class="informations">929×527 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Loading the exported file:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14f3dbb3980b636cf2c41aca1ad255f840d27dbe.png" data-download-href="/uploads/short-url/2Zm0OMU0fBega3O2WJIQtAPrSjQ.png?dl=1" title="segmentation_labelling_issue_load_exported_half" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14f3dbb3980b636cf2c41aca1ad255f840d27dbe_2_345x195.png" alt="segmentation_labelling_issue_load_exported_half" data-base62-sha1="2Zm0OMU0fBega3O2WJIQtAPrSjQ" width="345" height="195" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14f3dbb3980b636cf2c41aca1ad255f840d27dbe_2_345x195.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14f3dbb3980b636cf2c41aca1ad255f840d27dbe_2_517x292.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14f3dbb3980b636cf2c41aca1ad255f840d27dbe_2_690x390.png 2x" data-dominant-color="99999F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmentation_labelling_issue_load_exported_half</span><span class="informations">929×527 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any testing image will serve to demonstrate this.</p>
<p>Upgrading to a newer Slicer version is unfortunately not an option at this time for me (an extension I use has been reported to have issues in more recent versions).</p>

---

## Post #7 by @lassoan (2024-04-25 18:29 UTC)

<aside class="quote no-group" data-username="jhlegarreta" data-post="6" data-topic="35719">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>I made sure that I am using exactly the names in my colortable, and have simplified it t</p>
</blockquote>
</aside>
<p>As I wrote above, you need to use the color names that show up in Colors module, which is not exactly what is stored internally in the color table file (due to spaces are replaced by underscores). Your screenshots show that you use underscore in the segment names, so the names don’t match. We’ll <a href="https://github.com/Slicer/Slicer/issues/7593">switch to a new color table file format soon</a>, which does not have this confusing behavior.</p>
<p>It is extremely important to keep up your extensions working with latest Slicer version. Which extensions users having problems with?</p>

---

## Post #8 by @muratmaga (2024-04-25 19:15 UTC)

<aside class="quote no-group" data-username="jhlegarreta" data-post="6" data-topic="35719">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>I made sure that I am using exactly the names in my colortable, and have simplified it to the following:</p>
</blockquote>
</aside>
<p>I confirm that everything works as expected (i.e., labelmaps are exported with correct indices) when you replace underscore (_) with space. I tested it 5.6.2. If 5.2.2 doesn’t export it correctly for you (with the replacement), you can install 5.6.2 and export in there.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="35719">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>They are global identifiers that can be shared between projects and they allow using different name variants and spelling for segment names.</p>
</blockquote>
</aside>
<p>I am not sure how this will fix the conversion to the labelmap though. Labelmaps are what goes into the ML training, and they need to have indices. So we will always need some sort of lookup between segment labels and labelmap indices, regardless if the segment labels comes from a standardized terminology. Or am I overlooking something?</p>

---

## Post #9 by @lassoan (2024-04-29 13:55 UTC)

<p>10 posts were split to a new topic: <a href="/t/create-standard-terminology-for-new-segmentation-project/35798">Create standard terminology for new segmentation project</a></p>

---

## Post #19 by @jhlegarreta (2024-04-27 22:20 UTC)

<p>OK, thanks Andrass. Thanks Murat as well for the valuable input.</p>
<blockquote>
<p>you need to use the color names that show up in Colors module, which is not exactly what is stored internally in the color table file (due to spaces are replaced by underscores).</p>
</blockquote>
<p>Indeed, underscores are replaced by whitespaces, and using such names solves the issue. Have just tested.</p>
<blockquote>
<p>It is extremely important to keep up your extensions working with latest Slicer version. Which extensions users having problems with?</p>
</blockquote>
<p>I am aware of this. Some SlicerDMRI features were reported as having issues with the most recent Slicer versions towards the end of 2023.</p>
<p>BTW, you may want to transfer the exchange about the best possibilities going forward about color tables to a dedicated thread so that you can consolidate the discussion.</p>

---
