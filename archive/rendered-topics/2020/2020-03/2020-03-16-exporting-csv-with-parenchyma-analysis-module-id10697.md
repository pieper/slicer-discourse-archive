# Exporting CSV with parenchyma analysis module

**Topic ID**: 10697
**Date**: 2020-03-16
**URL**: https://discourse.slicer.org/t/exporting-csv-with-parenchyma-analysis-module/10697

---

## Post #1 by @Ezio_Lanza (2020-03-16 11:07 UTC)

<p>Hello everyone,<br>
I’m having troubles exporting results from the parenchyma analysis module in CSV. It only exports the first row without the resulting values. Also, I cannot copy and paste to excel which instead is possible when using the scalar volume module</p>
<p>Any clue? I’m using slicer 4 on MAC</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-03-18 04:09 UTC)

<p>I’m not sure if CIP developers monitor the Slicer forum. Could you try to contact them directly and let us know if they respond?</p>
<p><a class="mention" href="/u/raul">@raul</a></p>

---

## Post #3 by @Ezio_Lanza (2020-03-18 13:43 UTC)

<p>Thanks for answering<br>
I couldn’t find any email address to contact them</p>

---

## Post #4 by @raul (2020-03-18 14:21 UTC)

<p>Hi Ezio,</p>
<p>Thank you for your email and sorry for the trouble.</p>
<p>Can you provide more info about the Slicer version that you are using to try to reproduce the results?</p>
<p>Are you able to see the results in the module table before exporting the values? A screenshot of a test case might be helpful</p>
<p>Thanks</p>
<p>Raul</p>

---

## Post #5 by @chuawm (2021-08-08 12:50 UTC)

<p>Hi there,</p>
<p>Sorry, I am new to this and I am also having trouble.</p>
<ol>
<li>I am not able to export the data in parenchyma analysis in CSV format.</li>
<li>I can only export one parameter each time. Is there a way to export all the results at one go?</li>
<li>I tried using my own segmentation label map volume (using segment editor). My histogram does not look correct. My left lung histogram is flat. I am not sure what I am doing wrong.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5785fc77967126424c24d4d4b939296fe2db534.jpeg" data-download-href="/uploads/short-url/nBOGlxNxQvjWqiq0jBjzxWbMSry.jpeg?dl=1" title="segmentation histogram" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5785fc77967126424c24d4d4b939296fe2db534_2_690x364.jpeg" alt="segmentation histogram" data-base62-sha1="nBOGlxNxQvjWqiq0jBjzxWbMSry" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5785fc77967126424c24d4d4b939296fe2db534_2_690x364.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5785fc77967126424c24d4d4b939296fe2db534_2_1035x546.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5785fc77967126424c24d4d4b939296fe2db534_2_1380x728.jpeg 2x" data-dominant-color="C0C2C5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmentation histogram</span><span class="informations">1920×1013 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2021-08-08 14:00 UTC)

<p>How did you segment the lungs? Using Segment Editor module? Have you clicked “Apply” in “Grow from seeds” effect after the preview looked good?</p>
<p>You could also consider using the LungCTAnalyzer extension. If you miss some features (e.g., want to compute histogram) then probably <a class="mention" href="/u/rbumm">@rbumm</a> could easily add it.</p>

---

## Post #7 by @chuawm (2021-08-08 14:35 UTC)

<p>Thanks for your reply!</p>
<p>I used this youtube video as a guide: <a href="https://www.youtube.com/watch?v=v1-L_niLZxQ" rel="noopener nofollow ugc">COVID-19 lung CT segmentation using 3D Slicer - YouTube</a></p>
<ol>
<li>Set threshold as mask (HU -1024 to -200)</li>
<li>using paint to draw general outlines for right lung, left lung and trachea</li>
<li>Click on grow from seeds and initialize</li>
<li>Add additional areas of paint for regions that need correction</li>
<li>Click on apply under grow from seeds to finalize</li>
<li>Export as new label map volume</li>
<li>Go to parenchyma analysis and select input CT volume and the newly created label map volume</li>
<li>Click on apply</li>
</ol>
<p>I tried the lung CT segmenter extension as well (using landmarks for right lung, left lung and trachea). I still get the same flat histogram for left lung</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b01af79143bc1fce43cc044f233c93ab07ed6ad.jpeg" data-download-href="/uploads/short-url/68s8OT3OXPBb0lmD77nQRs6O5Fr.jpeg?dl=1" title="threshold" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b01af79143bc1fce43cc044f233c93ab07ed6ad_2_690x286.jpeg" alt="threshold" data-base62-sha1="68s8OT3OXPBb0lmD77nQRs6O5Fr" width="690" height="286" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b01af79143bc1fce43cc044f233c93ab07ed6ad_2_690x286.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b01af79143bc1fce43cc044f233c93ab07ed6ad_2_1035x429.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b01af79143bc1fce43cc044f233c93ab07ed6ad_2_1380x572.jpeg 2x" data-dominant-color="C1BDC4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">threshold</span><span class="informations">1920×798 91.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfdc0ee7eca906d7c50fc664b547ae176244e3f3.jpeg" data-download-href="/uploads/short-url/tEOj9DtLs7oI2ug819yd0RBTfGj.jpeg?dl=1" title="applied after grow from seed" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfdc0ee7eca906d7c50fc664b547ae176244e3f3_2_690x288.jpeg" alt="applied after grow from seed" data-base62-sha1="tEOj9DtLs7oI2ug819yd0RBTfGj" width="690" height="288" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfdc0ee7eca906d7c50fc664b547ae176244e3f3_2_690x288.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfdc0ee7eca906d7c50fc664b547ae176244e3f3_2_1035x432.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfdc0ee7eca906d7c50fc664b547ae176244e3f3_2_1380x576.jpeg 2x" data-dominant-color="B6B7BE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">applied after grow from seed</span><span class="informations">1920×804 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8247e39c1ecfc26a68c807dddfb24015f0ded132.jpeg" data-download-href="/uploads/short-url/iAw5KU04Lun6l28j4zT3TsFa5O2.jpeg?dl=1" title="lung ct segmenter" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8247e39c1ecfc26a68c807dddfb24015f0ded132_2_690x314.jpeg" alt="lung ct segmenter" data-base62-sha1="iAw5KU04Lun6l28j4zT3TsFa5O2" width="690" height="314" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8247e39c1ecfc26a68c807dddfb24015f0ded132_2_690x314.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8247e39c1ecfc26a68c807dddfb24015f0ded132_2_1035x471.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8247e39c1ecfc26a68c807dddfb24015f0ded132_2_1380x628.jpeg 2x" data-dominant-color="B7B9BB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">lung ct segmenter</span><span class="informations">1920×875 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I am trying to use other parameters (such as perc 85%) to analyze lung fibrosis.</p>

---

## Post #8 by @rbumm (2021-08-08 15:14 UTC)

<p>You do not have to do lung masks in “Parenchyma Analysis”. Just set the input volume to the lung CT dataset and leave the  “Label map volume” set to “None”, then press “Apply”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a979d05bc9f979a1029b4563da82f30408a4645b.jpeg" data-download-href="/uploads/short-url/obfG0DiycRkW08tCjdxLoRV8Cvh.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a979d05bc9f979a1029b4563da82f30408a4645b_2_690x403.jpeg" alt="image" data-base62-sha1="obfG0DiycRkW08tCjdxLoRV8Cvh" width="690" height="403" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a979d05bc9f979a1029b4563da82f30408a4645b_2_690x403.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a979d05bc9f979a1029b4563da82f30408a4645b_2_1035x604.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a979d05bc9f979a1029b4563da82f30408a4645b.jpeg 2x" data-dominant-color="A7A6B0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1319×771 77.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98ee3b4289ecf540b4829a2c74886416219ccb71.jpeg" data-download-href="/uploads/short-url/lOSZ0UH7v746Ad89ETUp3Yezkvn.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98ee3b4289ecf540b4829a2c74886416219ccb71_2_690x290.jpeg" alt="image" data-base62-sha1="lOSZ0UH7v746Ad89ETUp3Yezkvn" width="690" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98ee3b4289ecf540b4829a2c74886416219ccb71_2_690x290.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98ee3b4289ecf540b4829a2c74886416219ccb71_2_1035x435.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98ee3b4289ecf540b4829a2c74886416219ccb71_2_1380x580.jpeg 2x" data-dominant-color="BCBBC3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×808 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @rbumm (2021-08-08 15:22 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Having a histogram in the LungCTAnalyzer is probably good idea !</p>

---

## Post #10 by @chuawm (2021-08-08 16:05 UTC)

<p>I see, thanks! I will try to use the native label map volume from “Parenchyma Analysis” as much as possible.</p>
<p>My only concern is if there are some studies where the automated segmentation by the “Parenchyma Analysis” is not optimal and I have to manually edit some areas. In that case, I am worried that this issue will again recur.</p>
<p>I would also like to ask if there is any way to export the data in “Parenchyma Analysis” as a CSV file?</p>

---

## Post #11 by @rbumm (2021-08-08 17:23 UTC)

<p>I am not the developer of this extension but - yes, after “Parenchyma analysis” and if you go into the “Data” extension, you see, that the results of the analysis are stored in table nodes.</p>
<p>When saving your scene select the CSV format:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1e4d496a5cb9a6ebf19a83ab936b037ac8a0bda.png" alt="image" data-base62-sha1="yvTkUA0QQHlImxALOCeoIMgwy9A" width="685" height="381"></p>

---

## Post #12 by @lassoan (2021-08-08 21:33 UTC)

<p>The flat histogram looks good, it belongs the trachea (or “other”) segment, which is very small and dark compared to the two lung segments.</p>
<p>The Parenchyma Analysis module probably uses hardcoded label values, which are not the same as the values that are used when you export the segmentation that was created in Lung CT segmentation module. The module should be modernized so that it can use segmentation as input (so that we don’t need to rely on hardcoded label values anymore). The module should also modernized so that for plotting it does not use Charts (that will be removed soon from Slicer) but Plots.</p>
<p>You can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region">compute the histogram of a segmented region by a few lines of Python code</a>, so it would be easy to add it to Lung CT analyzer module. But it is probably better to not create modules with overlapping features but fix/modernize the existing module instead.</p>

---

## Post #13 by @chuawm (2021-08-09 07:45 UTC)

<p>Thanks alot!</p>
<p>That is very helpful</p>

---

## Post #14 by @chuawm (2021-08-09 07:47 UTC)

<p>I see!</p>
<p>I am not very experienced with Python coding but I will play around with it. Does that mean I can possibly add in my own parameters for analysis (such as other percentile densities instead of the ones provided)?</p>

---

## Post #15 by @chuawm (2021-08-09 12:15 UTC)

<p>I realized that if I were to switch the order around in “segment editor”, where “left lung” comes before “right lung”, I will get the histogram for the “left lung” but it will be labelled as “right lung” in “parenchymal analysis”. Essentially, “parenchymal analysis” will create the histogram for the first segmentation accurately but not the others.</p>
<p>This is the original histogram with “right lung” on 1st in order by default:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af9656f5b66d4ab3d64b9daa369b1558fd183091.jpeg" data-download-href="/uploads/short-url/p3jEPK3NoWxoBj2tTSZsWe5Eb2p.jpeg?dl=1" title="original parenchymal analysis" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af9656f5b66d4ab3d64b9daa369b1558fd183091_2_690x313.jpeg" alt="original parenchymal analysis" data-base62-sha1="p3jEPK3NoWxoBj2tTSZsWe5Eb2p" width="690" height="313" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af9656f5b66d4ab3d64b9daa369b1558fd183091_2_690x313.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af9656f5b66d4ab3d64b9daa369b1558fd183091_2_1035x469.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af9656f5b66d4ab3d64b9daa369b1558fd183091_2_1380x626.jpeg 2x" data-dominant-color="B4B5BB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">original parenchymal analysis</span><span class="informations">1920×871 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After I switch the order, putting “left lung” 1st in order as follows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/869fe9e3e18c0d8269c734632a5ea73b3dcc0d39.jpeg" data-download-href="/uploads/short-url/jcWAQWRcSMgkU5PPzESvMhSIFtL.jpeg?dl=1" title="left lung segment" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/869fe9e3e18c0d8269c734632a5ea73b3dcc0d39_2_690x311.jpeg" alt="left lung segment" data-base62-sha1="jcWAQWRcSMgkU5PPzESvMhSIFtL" width="690" height="311" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/869fe9e3e18c0d8269c734632a5ea73b3dcc0d39_2_690x311.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/869fe9e3e18c0d8269c734632a5ea73b3dcc0d39_2_1035x466.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/869fe9e3e18c0d8269c734632a5ea73b3dcc0d39_2_1380x622.jpeg 2x" data-dominant-color="B0B2B9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">left lung segment</span><span class="informations">1920×866 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I get the histogram for the “left lung” but it is labelled as the “right lung” in “parenchymal analysis”<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fefd469efacd2d073e8e791075b1cecb2eb9799c.jpeg" data-download-href="/uploads/short-url/AnJUWP5C0mEHu0z6Io7Q6s5f5YE.jpeg?dl=1" title="new parenchymal analysis" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fefd469efacd2d073e8e791075b1cecb2eb9799c_2_690x313.jpeg" alt="new parenchymal analysis" data-base62-sha1="AnJUWP5C0mEHu0z6Io7Q6s5f5YE" width="690" height="313" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fefd469efacd2d073e8e791075b1cecb2eb9799c_2_690x313.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fefd469efacd2d073e8e791075b1cecb2eb9799c_2_1035x469.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fefd469efacd2d073e8e791075b1cecb2eb9799c_2_1380x626.jpeg 2x" data-dominant-color="B4B5BC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">new parenchymal analysis</span><span class="informations">1920×871 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #16 by @rbumm (2021-08-09 13:33 UTC)

<p>Yes you could do that, the python code is exposed in that extension.<br>
You would need to switch Slicer to “Enable developer mode” under “Application Settings” &gt; “Developer”, then you would be able to “Edit” and “Reload” the extension code (with great care)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81301677183f7cb8d613ebe1440bda417af36d9f.png" alt="image" data-base62-sha1="iqQCvZRmkungl7x1TcvgN42abN5" width="613" height="66"></p>

---

## Post #17 by @lassoan (2021-08-09 15:12 UTC)

<aside class="quote no-group" data-username="chuawm" data-post="15" data-topic="10697">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chuawm/48/11915_2.png" class="avatar"> chuawm:</div>
<blockquote>
<p>I realized that if I were to switch the order around in “segment editor”, where “left lung” comes before “right lung”, I will get the histogram for the “left lung” but it will be labelled as “right lung” in “parenchymal analysis”. Essentially, “parenchymal analysis” will create the histogram for the first segmentation accurately but not the others.</p>
</blockquote>
</aside>
<p>This is the expected behavior if you export the segmentation to labelmap without specifying a mapping from segment names to label values.</p>
<p>You could change the label values quite easily manually, using numpy, but it is more elegant to specify a color mapping from segment names to label values using a color table node. You can create a color node that matches label values of <a href="https://github.com/acil-bwh/ChestImagingPlatform/blob/8a9d9cf831c9f670518730c4e74365f34008f025/Common/cipChestConventions.cxx#L646-L714">CIP conventions</a> for a few labels like this:</p>
<pre data-code-wrap="python"><code class="lang-python">segmentToLabelValueMapping = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLColorTableNode", "CIP colors")
segmentToLabelValueMapping.SetTypeToUser()
segmentToLabelValueMapping.HideFromEditorsOff()
segmentToLabelValueMapping.SetNumberOfColors(69)
segmentToLabelValueMapping.SetColor( 0, "background", 0.0, 0.0, 0.0, 0.0)
segmentToLabelValueMapping.SetColor( 1, "whole lung", 0.42, 0.38, 0.75, 1.0)
segmentToLabelValueMapping.SetColor( 2, "right lung", 0.26, 0.64, 0.10, 1.0)
segmentToLabelValueMapping.SetColor( 3, "left lung",  0.80, 0.11, 0.36, 1.0)
segmentToLabelValueMapping.SetColor(58, "trachea",    0.49, 0.49, 0.79, 1.0)
segmentToLabelValueMapping.NamesInitialisedOn()
</code></pre>
<p>You can then specify this color table when you export the segmentation to labelmap to get the desired label values.</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a> if you want to make it easier to use LungCTAnalyzer segmentations with CIP then you could create a color node like this in the segmentation module and set it in the segmentation node. I think it would be used by default when you export the segmentation to labelmap.</p>

---

## Post #18 by @rbumm (2021-08-09 19:51 UTC)

<p>Done and working (created in 4.13, CIP tested vs 4.11).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6a4c1c5dd70ca9b3977ceba83160441f972f320.png" alt="image" data-base62-sha1="nMcfvGJsHLSQ30B9JnkGWbnOeRi" width="643" height="368"></p>

---

## Post #19 by @rbumm (2021-08-10 08:09 UTC)

<p>That success message was too early.<br>
I will create an issue in LungCTAnalyzer to prevent pushing this up all the time in discourse.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/rbumm/SlicerLungCTAnalyzer/issues/27">
  <header class="source">

      <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/issues/27" target="_blank" rel="noopener nofollow ugc">github.com/rbumm/SlicerLungCTAnalyzer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/issues/27" target="_blank" rel="noopener nofollow ugc">Create compatibility between LungCTSegmenter and CIP</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-08-10" data-time="08:33:38" data-timezone="UTC">08:33AM - 10 Aug 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/rbumm" target="_blank" rel="noopener nofollow ugc">
          <img alt="rbumm" src="https://avatars.githubusercontent.com/u/18140094?v=4" class="onebox-avatar-inline" width="20" height="20">
          rbumm
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">I implemented the code in LungCTSegmenter  mentioned here

[https://discourse.<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">slicer.org/t/exporting-csv-with-parenchyma-analysis-module/10697/17?u=rbumm](https://discourse.slicer.org/t/exporting-csv-with-parenchyma-analysis-module/10697/17?u=rbumm)

but this

![image](https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/a/a4bcef1500c54fa3c4fa175c37c7d85e79b4471e.png)

was produced leaving the labelmap input to "None". 

If I do a LungCTSegmenter run with the latest code and do this

![](https://user-images.githubusercontent.com/18140094/128834443-38f0520a-d77f-415c-8d20-f59b1d45439d.png)

I get this (Lung segmentation-label. 

![](https://user-images.githubusercontent.com/18140094/128834627-4e273f23-31a8-4eb7-9784-5473368a9bc6.png)

Feeding this to CIP and "Parenchyma Analysis" 

![](https://user-images.githubusercontent.com/18140094/128835036-6f4a6995-cb9b-4784-bb97-8e92a58ece95.png)

still results in

![](https://user-images.githubusercontent.com/18140094/128834904-0a9c5304-2cc2-47a4-9ee9-ae2a88453b2b.png)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #20 by @chuawm (2021-08-21 17:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="17" data-topic="10697">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>segmentToLabelValueMapping.NamesInitialisedOn()</code></p>
</blockquote>
</aside>
<p>Sorry Lassoan,</p>
<p>I tried changing the label values to match those of CIP conventions as per your suggestion. I used the exact labels which you kindly provided.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1e70e9927ba6a7a5fd35864325e45303efe8cba.jpeg" data-download-href="/uploads/short-url/rFlbJeUHGtQ1cGPBQKsvfXBYEs2.jpeg?dl=1" title="labelvaluemapping" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1e70e9927ba6a7a5fd35864325e45303efe8cba_2_690x365.jpeg" alt="labelvaluemapping" data-base62-sha1="rFlbJeUHGtQ1cGPBQKsvfXBYEs2" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1e70e9927ba6a7a5fd35864325e45303efe8cba_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1e70e9927ba6a7a5fd35864325e45303efe8cba_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1e70e9927ba6a7a5fd35864325e45303efe8cba_2_1380x730.jpeg 2x" data-dominant-color="B3B3BA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">labelvaluemapping</span><span class="informations">1920×1018 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
However, my histogram still looks flat for the left lung.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e30ad1ba43454b65dce3ee5bffc259255e66debb.jpeg" data-download-href="/uploads/short-url/wovz5pHJiFXaJHXzTLIfJvRbqXN.jpeg?dl=1" title="new parenchymal analysis" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e30ad1ba43454b65dce3ee5bffc259255e66debb_2_690x367.jpeg" alt="new parenchymal analysis" data-base62-sha1="wovz5pHJiFXaJHXzTLIfJvRbqXN" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e30ad1ba43454b65dce3ee5bffc259255e66debb_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e30ad1ba43454b65dce3ee5bffc259255e66debb_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e30ad1ba43454b65dce3ee5bffc259255e66debb_2_1380x734.jpeg 2x" data-dominant-color="BFBFBE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">new parenchymal analysis</span><span class="informations">1920×1023 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you know where did I go wrong?</p>

---

## Post #21 by @rbumm (2021-08-22 19:32 UTC)

<p>Just to let you know, <a class="mention" href="/u/chuawm">@chuawm</a> :<br>
I have literally spent 6 hours on that problem, tried every possible way to make this work in 4.11, but had no success. The problem seems to be, that the “Parenchyma analysis” of CIP (which I am not the author of) is outdated and probably not fully compatible with 4.11. Whatever values I put into the “CIP colors” color table node, and use it during export of the “Lung CT Segmenter” segmentation and as an input into “Parenchyma analysis”, it is not associated with “right lung” and “left lung” and “left lung” histogram remains flat.</p>
<p>Just an example: segmentToLabelValueMapping.SetTypeToUser() is not in the vtkMRMLColorTableNode documentation. Am I / are we missing anything here ?</p>
<p>I could easily implement a histogram function into “LungCTSegmenter”, but as <a class="mention" href="/u/lassoan">@lassoan</a> said - this is probably not the right way to go because the specialized modules should be modernized.</p>

---

## Post #22 by @chuawm (2021-08-23 15:39 UTC)

<p>Firstly, thank you <a class="mention" href="/u/rbumm">@rbumm</a> for helping! I really appreciate it!</p>
<p>I will probably have to make do with using the alternative you suggested for the time being, which is to use a histogram function for “LungCTSegmenter”.</p>
<p>Apologies as I am still new to this and I have a question about inserting the histogram function. How do I get the individual histograms for each segments  (i.e. right lung, left lung)?</p>
<p>The script repository here that I’m using is likely generating a single histogram (I’m assuming its the whole lung).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a8eff21e58fc372f9e9b590989212ee47f1c76a.jpeg" data-download-href="/uploads/short-url/3MWMy4A59OpJ0tP1kADjrViunbk.jpeg?dl=1" title="histogram whole lung script" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a8eff21e58fc372f9e9b590989212ee47f1c76a_2_690x248.jpeg" alt="histogram whole lung script" data-base62-sha1="3MWMy4A59OpJ0tP1kADjrViunbk" width="690" height="248" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a8eff21e58fc372f9e9b590989212ee47f1c76a_2_690x248.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a8eff21e58fc372f9e9b590989212ee47f1c76a_2_1035x372.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a8eff21e58fc372f9e9b590989212ee47f1c76a_2_1380x496.jpeg 2x" data-dominant-color="EDFDCB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">histogram whole lung script</span><span class="informations">3220×1159 283 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42287f86bef6c3778313c96a7541e331f515def1.jpeg" data-download-href="/uploads/short-url/9rghm4s8k96eXdATLzLYYVxVJS1.jpeg?dl=1" title="histogram whole lung result" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42287f86bef6c3778313c96a7541e331f515def1_2_690x313.jpeg" alt="histogram whole lung result" data-base62-sha1="9rghm4s8k96eXdATLzLYYVxVJS1" width="690" height="313" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42287f86bef6c3778313c96a7541e331f515def1_2_690x313.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42287f86bef6c3778313c96a7541e331f515def1_2_1035x469.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42287f86bef6c3778313c96a7541e331f515def1_2_1380x626.jpeg 2x" data-dominant-color="B7B9B3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">histogram whole lung result</span><span class="informations">1920×873 99.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Additionally, the count frequency and graph seem to be different when generated by CIP “Parenchyma Analysis” compared with the generic script I am using.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e48c66251bedeee3539a9c5873a88943d2830bd2.jpeg" data-download-href="/uploads/short-url/wBPFkWXdEsSdMYlsAUBuvut2MCu.jpeg?dl=1" title="comparing histogram" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e48c66251bedeee3539a9c5873a88943d2830bd2_2_551x500.jpeg" alt="comparing histogram" data-base62-sha1="wBPFkWXdEsSdMYlsAUBuvut2MCu" width="551" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e48c66251bedeee3539a9c5873a88943d2830bd2_2_551x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e48c66251bedeee3539a9c5873a88943d2830bd2_2_826x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e48c66251bedeee3539a9c5873a88943d2830bd2_2_1102x1000.jpeg 2x" data-dominant-color="F1F7F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">comparing histogram</span><span class="informations">1274×1154 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #23 by @rbumm (2021-08-23 17:14 UTC)

<p>Did you copy that code into the python interactor or modify it before? You would need to.<br>
The code you mention is an example of loading a brain tumor dataset and plotting a histogram …</p>
<p>I will add a histogram function, which will be helpful anyway, to LungCTAnalyzer during the next few days.  Please check back.</p>

---

## Post #24 by @lassoan (2021-08-24 00:50 UTC)

<p>I’m fixing CIP for the Slicer Preview Release (4.13) and also investigating this histogram computation issue.</p>

---

## Post #25 by @lassoan (2021-08-24 03:22 UTC)

<p>I’ve <a href="https://github.com/acil-bwh/ChestImagingPlatform/pull/41">fixed Chest Imaging Platform build for Slicer-4.13</a>. It’ll probably take a few days to get the pull request merged.</p>
<p>I’ve also fixed <a href="https://github.com/Slicer/Slicer/commit/9492059b0bee65be40fc81bc1f527d2bb62abe0a">the bug that cause the color map not applied during labelmap export</a> (and therefore broke the histogram computation). This will be available in the Slicer Preview Release from Wednesday.</p>

---

## Post #26 by @lassoan (2021-08-24 21:04 UTC)

<p>Chest Imaging Platform fix has been merged today. So, in tomorrow’s Slicer Preview Release CIP should be available and it should work well with LungCTSegmenter output.</p>

---

## Post #27 by @rbumm (2021-08-26 11:48 UTC)

<p>I can confirm that in 4.13.0-2021-08-24 → CIP is available. The “Parenchyma analysis” extension of CIP now correctly detects and analyzes a labelmap generated from a segmentation created by “LungCTSegmenter” using CIP-colors. As far as I see  - good histograms:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62eef7db74253f775448ec6298aadb088faf6041.jpeg" data-download-href="/uploads/short-url/e7cMiQ7kkVYkRagJunTYvdARHod.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62eef7db74253f775448ec6298aadb088faf6041_2_690x328.jpeg" alt="image" data-base62-sha1="e7cMiQ7kkVYkRagJunTYvdARHod" width="690" height="328" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62eef7db74253f775448ec6298aadb088faf6041_2_690x328.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62eef7db74253f775448ec6298aadb088faf6041_2_1035x492.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62eef7db74253f775448ec6298aadb088faf6041_2_1380x656.jpeg 2x" data-dominant-color="AFB0B3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×913 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a><br>
<a class="mention" href="/u/ezio_lanza">@Ezio_Lanza</a>  , <a class="mention" href="/u/chuawm">@chuawm</a> go for it <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #28 by @chuawm (2021-08-27 07:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="17" data-topic="10697">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>segmentToLabelValueMapping = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLColorTableNode", "CIP colors")</code></p>
</blockquote>
</aside>
<p>Hello <a class="mention" href="/u/rbumm">@rbumm</a> and <a class="mention" href="/u/lassoan">@lassoan</a> ,</p>
<p>Thank you again for helping! I am really excited to try this out. However, I am again encountering the same issues.</p>
<p>I upgraded the 3D slicer version to 4.13.0-2021-08-24 and installed CIP. I then used “LungCTSegmenter” to segment the lungs as shown.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf55a4d574aa9fa8546b81cadd395a8878d6cc0d.jpeg" data-download-href="/uploads/short-url/tAakj7iGWnqwyzfqXPOpsaYbXyZ.jpeg?dl=1" title="newsegmentation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf55a4d574aa9fa8546b81cadd395a8878d6cc0d_2_690x364.jpeg" alt="newsegmentation" data-base62-sha1="tAakj7iGWnqwyzfqXPOpsaYbXyZ" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf55a4d574aa9fa8546b81cadd395a8878d6cc0d_2_690x364.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf55a4d574aa9fa8546b81cadd395a8878d6cc0d_2_1035x546.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf55a4d574aa9fa8546b81cadd395a8878d6cc0d_2_1380x728.jpeg 2x" data-dominant-color="98999B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">newsegmentation</span><span class="informations">1920×1015 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I then proceeded to go to “segment editor” to change the label values of the segments to match CIP conventions and export it as a lablelmap (mentioned by <a class="mention" href="/u/lassoan">@lassoan</a> here<br>
<a href="https://discourse.slicer.org/t/exporting-csv-with-parenchyma-analysis-module/10697/17" class="inline-onebox">Exporting CSV with parenchyma analysis module - #17 by lassoan</a>)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8a0a694644b27855f74f7b765976435db3f02ae.jpeg" data-download-href="/uploads/short-url/qli2V49orrUOpt2vM0U0i43kAY6.jpeg?dl=1" title="cip colours" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8a0a694644b27855f74f7b765976435db3f02ae_2_690x364.jpeg" alt="cip colours" data-base62-sha1="qli2V49orrUOpt2vM0U0i43kAY6" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8a0a694644b27855f74f7b765976435db3f02ae_2_690x364.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8a0a694644b27855f74f7b765976435db3f02ae_2_1035x546.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8a0a694644b27855f74f7b765976435db3f02ae_2_1380x728.jpeg 2x" data-dominant-color="959496"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cip colours</span><span class="informations">1920×1013 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then I went to “Parenchyma Analysis” to use the generate the histogram using the segmentation labelmap I created. But I still get a flat histogram<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/6218b2edb0020807d32affbed05ffb64ee60c621.jpeg" data-download-href="/uploads/short-url/dZNHYGYBiuBo396YmnaEtnS5EJ3.jpeg?dl=1" title="histogram" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6218b2edb0020807d32affbed05ffb64ee60c621_2_690x365.jpeg" alt="histogram" data-base62-sha1="dZNHYGYBiuBo396YmnaEtnS5EJ3" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6218b2edb0020807d32affbed05ffb64ee60c621_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6218b2edb0020807d32affbed05ffb64ee60c621_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6218b2edb0020807d32affbed05ffb64ee60c621_2_1380x730.jpeg 2x" data-dominant-color="B8B7B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">histogram</span><span class="informations">1920×1016 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I noticed that your segmentation colours are the default ones generated by “LungCTSegmenter” (i.e. green and yellow). I also tried using the default colours but the same flat histogram is still present.</p>
<p>Did I do something wrong?</p>

---

## Post #29 by @rbumm (2021-08-27 08:14 UTC)

<p>This is still a bit complicated, we will make this easier soon.</p>
<p>You need to right-click on the newly created lung segmentation, then go → “Edit properties”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ece5755706eeafe9345366311485df8d0e354d9.png" data-download-href="/uploads/short-url/bf9kfjtKy1XGD77iBcZXEXrLFVf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ece5755706eeafe9345366311485df8d0e354d9_2_468x500.png" alt="image" data-base62-sha1="bf9kfjtKy1XGD77iBcZXEXrLFVf" width="468" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ece5755706eeafe9345366311485df8d0e354d9_2_468x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ece5755706eeafe9345366311485df8d0e354d9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ece5755706eeafe9345366311485df8d0e354d9.png 2x" data-dominant-color="E7EBE7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">548×585 30.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This will open the segmentations extension<br>
 → go “Export/Import models and labelmaps”<br>
 → click "Advanced</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d654080d9a02a68dacc9b6f89ebacf5d8ac3e28.png" data-download-href="/uploads/short-url/4c2Meyow4DL0gCiKfl4NQqxLfxm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d654080d9a02a68dacc9b6f89ebacf5d8ac3e28_2_403x500.png" alt="image" data-base62-sha1="4c2Meyow4DL0gCiKfl4NQqxLfxm" width="403" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d654080d9a02a68dacc9b6f89ebacf5d8ac3e28_2_403x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d654080d9a02a68dacc9b6f89ebacf5d8ac3e28_2_604x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d654080d9a02a68dacc9b6f89ebacf5d8ac3e28.png 2x" data-dominant-color="DDDDDE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">608×753 35 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p> → Check the checkbox “Use color table values”<br>
 → Press “Export” button</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26306441032547664370bb56da935d15cd07d159.jpeg" data-download-href="/uploads/short-url/5rPOZs5k5tA7wMvKtKo8St9oguB.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26306441032547664370bb56da935d15cd07d159_2_348x500.jpeg" alt="image" data-base62-sha1="5rPOZs5k5tA7wMvKtKo8St9oguB" width="348" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26306441032547664370bb56da935d15cd07d159_2_348x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26306441032547664370bb56da935d15cd07d159_2_522x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26306441032547664370bb56da935d15cd07d159.jpeg 2x" data-dominant-color="EDEDEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">551×791 76.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and you are done.</p>
<p>Under “Data” you will find a new labelmap “Lung segmentation-label”  with correct label specifications for CIP</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66f219a10ae16773c6985e83b8a06bdbe35c8c11.png" alt="image" data-base62-sha1="eGHoK5Afdu37hWeDcBwqZzfkJOh" width="546" height="436"></p>
<p>“Parenchyma analysis” with an input of the new labelmap will produce:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6dd166240e335f34623b9540e58efd4367b23023.png" data-download-href="/uploads/short-url/fFuG89D7lW95lSUeqTaar5mOGHx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6dd166240e335f34623b9540e58efd4367b23023_2_690x462.png" alt="image" data-base62-sha1="fFuG89D7lW95lSUeqTaar5mOGHx" width="690" height="462" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6dd166240e335f34623b9540e58efd4367b23023_2_690x462.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6dd166240e335f34623b9540e58efd4367b23023.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6dd166240e335f34623b9540e58efd4367b23023.png 2x" data-dominant-color="E7EBE8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">744×499 40.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> will probably know how to transform segmentations to labelmaps using a color table via script.</p>

---

## Post #30 by @chuawm (2021-08-27 08:33 UTC)

<p>Thank you so much!!! It works now <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"><br>
Your steps were clear so it was not that complicated</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/585967b437a6922abe8b4bc119e42bf8b78d08be.jpeg" data-download-href="/uploads/short-url/cBzz9h6YMm5YYnkgV26fCSXJLPw.jpeg?dl=1" title="histogram" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/585967b437a6922abe8b4bc119e42bf8b78d08be_2_690x362.jpeg" alt="histogram" data-base62-sha1="cBzz9h6YMm5YYnkgV26fCSXJLPw" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/585967b437a6922abe8b4bc119e42bf8b78d08be_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/585967b437a6922abe8b4bc119e42bf8b78d08be_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/585967b437a6922abe8b4bc119e42bf8b78d08be_2_1380x724.jpeg 2x" data-dominant-color="ACADB1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">histogram</span><span class="informations">1920×1008 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #31 by @lassoan (2021-08-27 22:30 UTC)

<p>CIP modules should be updated to take segmentations directly instead of requiring labelmap conversion.</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a> it would be awesome if you could review and modernize CIP modules. They contain excellent algorithms but they don’t seem to be actively maintained.</p>

---

## Post #32 by @rbumm (2021-08-28 20:15 UTC)

<p>Quite a difficult task, no promises concerning a time frame, but I will dig into this <a class="mention" href="/u/lassoan">@lassoan</a>.</p>

---

## Post #33 by @lassoan (2021-08-28 21:55 UTC)

<p>Allowing selfecting segmentation or labelmap volume as input should be straightforward. You can list multiple node types in the input selector combobox and if you receive a segmentation node then you can convert to labelmap node with the appropriate color table.</p>
<p>But I fully agree that overall the modernization of the CIP extension is significant effort. Any amount of work that you can put into it (and other extensions) are greatly appreciated.</p>

---

## Post #34 by @pieper (2021-08-29 12:57 UTC)

<p>It could help to look at how it’s done in SlicerRadiomics.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/AIM-Harvard/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L788-L793">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L788-L793" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/AIM-Harvard/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L788-L793" target="_blank" rel="noopener">AIM-Harvard/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L788-L793</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="788" style="counter-reset: li-counter 787 ;">
          <li>self._labelGenerators = []</li>
          <li>if maskNode.IsA('vtkMRMLVolumeNode'):</li>
          <li>  self._labelGenerators = chain(self._labelGenerators, self._getLabelGeneratorFromLabelMap(maskNode, imageNode))</li>
          <li>elif maskNode.IsA('vtkMRMLSegmentationNode'):</li>
          <li>  self._labelGenerators = chain(self._labelGenerators,</li>
          <li>                                self._getLabelGeneratorFromSegmentationNode(maskNode, imageNode))</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/AIM-Harvard/SlicerRadiomics/blob/e599755f305792619536ef5d324a69638673435e/SlicerRadiomics/SlicerRadiomics.py#L526-L555">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/SlicerRadiomics/blob/e599755f305792619536ef5d324a69638673435e/SlicerRadiomics/SlicerRadiomics.py#L526-L555" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/AIM-Harvard/SlicerRadiomics/blob/e599755f305792619536ef5d324a69638673435e/SlicerRadiomics/SlicerRadiomics.py#L526-L555" target="_blank" rel="noopener">AIM-Harvard/SlicerRadiomics/blob/e599755f305792619536ef5d324a69638673435e/SlicerRadiomics/SlicerRadiomics.py#L526-L555</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="526" style="counter-reset: li-counter 525 ;">
          <li>def _getLabelGeneratorFromSegmentationNode(self, segmentationNode, imageNode):</li>
          <li>  import vtkSegmentationCorePython as vtkSegmentationCore</li>
          <li>  segLogic = slicer.modules.segmentations.logic()</li>
          <li>
          </li>
<li>  segmentation = segmentationNode.GetSegmentation()</li>
          <li>  binaryRepresentationDef = \</li>
          <li>      vtkSegmentationCore.vtkSegmentationConverter.GetSegmentationBinaryLabelmapRepresentationName()</li>
          <li>  if not segmentation.ContainsRepresentation(binaryRepresentationDef):</li>
          <li>    segmentation.CreateRepresentation(binaryRepresentationDef)</li>
          <li>
          </li>
<li>  segmentLabelmapNode = slicer.vtkMRMLLabelMapVolumeNode()</li>
          <li>  slicer.mrmlScene.AddNode(segmentLabelmapNode)</li>
          <li>
          </li>
<li>  for segmentID in range(segmentation.GetNumberOfSegments()):</li>
          <li>    segment = segmentation.GetNthSegment(segmentID)</li>
          <li>    segmentNames = vtk.vtkStringArray()</li>
          <li>    segmentNames.InsertNextValue(segment.GetName())</li>
          <li>
          </li>
<li>    if not slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsToLabelmapNode(segmentationNode, segmentNames, segmentLabelmapNode, imageNode):</li>
          <li>      self.logger.error("Failed to convert label map")</li>
      </ol>
    </code>
  </pre>

  This file has been truncated. <a href="https://github.com/AIM-Harvard/SlicerRadiomics/blob/e599755f305792619536ef5d324a69638673435e/SlicerRadiomics/SlicerRadiomics.py#L526-L555" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #35 by @rbumm (2021-08-30 10:51 UTC)

<p>How Do I use ExportSegmentsToLabelmapNode correctly with a color node ?</p>
<pre><code class="lang-auto">        # to create labelmap compatibility with Chest Imaging Platform
 
        segmentToLabelValueMapping = slicer.util.getFirstNodeByClassByName("vtkMRMLColorTableNode", "CIP colors")
        if not segmentToLabelValueMapping:
            segmentToLabelValueMapping = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLColorTableNode", "CIP colors")
            segmentToLabelValueMapping.SetTypeToUser()
            segmentToLabelValueMapping.HideFromEditorsOff()
            segmentToLabelValueMapping.SetNumberOfColors(69)
            segmentToLabelValueMapping.SetColor( 0, "background", 0.0, 0.0, 0.0, 0.0)
            segmentToLabelValueMapping.SetColor( 1, "whole lung", 0.42, 0.38, 0.75, 1.0)
            segmentToLabelValueMapping.SetColor( 2, "right lung", 0.26, 0.64, 0.10, 1.0)
            segmentToLabelValueMapping.SetColor( 3, "left lung",  0.80, 0.11, 0.36, 1.0)
            segmentToLabelValueMapping.SetColor(58, "trachea",    0.49, 0.49, 0.79, 1.0)
            segmentToLabelValueMapping.NamesInitialisedOn()
        
        segmentIds = [self.rightLungSegmentId, self.leftLungSegmentId, self.tracheaSegmentId]
        labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
        slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(self.outputSegmentation, segmentIds, labelmapVolumeNode, self.inputVolume, slicer.vtkSegmentation.EXTENT_REFERENCE_GEOMETRY, segmentToLabelValueMapping)

        # end for compatibility with CIP 
</code></pre>
<p>Running this results in:<br>
Failed to compute results: “arguments do not match any overloaded methods”</p>

---

## Post #36 by @lassoan (2021-08-31 04:28 UTC)

<p><a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#a672694808d71487ebcb59bb65155d448">vtkSlicerSegmentationsModuleLogic::ExportSegmentsToLabelmapNode methods expect segment IDs as a string vector reference or as a vtkStringArray</a>. A list of Python strings can only be used when the argument is a string vector (not a reference). Therefore right now, you need to copy your strings into a vtkStringArray and use that as input to the method:</p>
<pre><code class="lang-python">segmentIds = vtk.vtkStringArray()
for segmentId in segmentIdList:
  segmentIds.InsertNextValue(segmentId)
slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(..., segmentIds, ...)
</code></pre>

---

## Post #37 by @lassoan (2021-09-01 18:08 UTC)

<p>I investigated this more and it turns out that VTK is supposed to support string vector references, there was just a bug in VTK that broke this for cases when there were multiple overloads for a method. I’ve <a href="https://discourse.vtk.org/t/python-wrapping-of-std-vector-std-string-does-not-work-when-there-are-multiple-overloads/6517/3">reported the error to VTK developers</a>, they fixed it, now we just need to backport these fixes in to Slicer’s VTK. Once that is done, you will not need to create a vtkStringArray but you can directly pass a Python string array to the ExportSegmentsToLabelmapNode method.</p>

---

## Post #38 by @rbumm (2021-09-07 09:42 UTC)

<p>Could you notify me when the backport is finished?</p>

---

## Post #39 by @lassoan (2021-09-08 17:41 UTC)

<p>The fixes will be available in the Slicer Preview Release from tomorrow.</p>

---

## Post #40 by @chuawm (2021-12-10 14:37 UTC)

<p>Dear all,</p>
<p>I realized that the Parenchymal Analysis Module is no longer available on the later versions of Slicer Preview Release (4.13.0-2021-12-09). Is this permanent or temporary? If permanent, is there another module that can analyze and create histogram of lung density similar to Parenchymal Analysis Module?</p>
<p>Thank you.</p>

---

## Post #41 by @lassoan (2021-12-10 16:48 UTC)

<p>This is a temporary issue, we are just waiting for <a class="mention" href="/u/raul">@raul</a> to approve this pull request that contains the fix:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/acil-bwh/SlicerCIP/pull/34">
  <header class="source">

      <a href="https://github.com/acil-bwh/SlicerCIP/pull/34" target="_blank" rel="noopener">github.com/acil-bwh/SlicerCIP</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/acil-bwh/SlicerCIP/pull/34" target="_blank" rel="noopener">Parenchyma analysis segmentation support</a>
    </h4>

    <div class="branches">
      <code>acil-bwh:develop</code> ← <code>lassoan:parenchyma-analysis-segmentation-support</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-09-30" data-time="13:57:33" data-timezone="UTC">01:57PM - 30 Sep 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="4 commits changed 4 files with 337 additions and 257 deletions">
        <a href="https://github.com/acil-bwh/SlicerCIP/pull/34/files" target="_blank" rel="noopener">
          <span class="added">+337</span>
          <span class="removed">-257</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This pull request includes https://github.com/acil-bwh/SlicerCIP/pull/32 and add<span class="show-more-container"><a href="https://github.com/acil-bwh/SlicerCIP/pull/34" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">s further fixes (such as report generation), design improvements and code refactoring.

@rbumm please test if everything works as expected. I've changed the API of the logic class, so you may need to adjust Lung CT Segmenter module accordingly.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #42 by @chuawm (2021-12-10 17:54 UTC)

<p>Ok thank you <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>On another note, I have been trying to create histograms for my own CT chest studies in Parenchymal Analysis Module using the steps laid out by <a class="mention" href="/u/rbumm">@rbumm</a> .</p>
<p>However, there always seems to be a spike in frequency at HU -1024. I have tried a few different CT studies</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29cdc8c430a84e6546baa062faec7dbedd7633ca.jpeg" data-download-href="/uploads/short-url/5XOsX8sGAp27XBR3DuiHyaSePlU.jpeg?dl=1" title="ct chest spike" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29cdc8c430a84e6546baa062faec7dbedd7633ca_2_690x415.jpeg" alt="ct chest spike" data-base62-sha1="5XOsX8sGAp27XBR3DuiHyaSePlU" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29cdc8c430a84e6546baa062faec7dbedd7633ca_2_690x415.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29cdc8c430a84e6546baa062faec7dbedd7633ca_2_1035x622.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29cdc8c430a84e6546baa062faec7dbedd7633ca_2_1380x830.jpeg 2x" data-dominant-color="BAB9BB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ct chest spike</span><span class="informations">1920×1156 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This does not appear to be an issue for the DemoCTChest sample data. Is there a reason for it?</p>

---

## Post #43 by @lassoan (2021-12-10 17:58 UTC)

<p>-1000 HU corresponds to air, if you are interested in soft tissue density then you can ignore that peak.</p>

---

## Post #44 by @chuawm (2021-12-10 18:17 UTC)

<p>In that case, shouldn’t the CTchest sample data also have the same peak to correspond to air? But as you can see in the image below, the sample data does not have the peak at -1024 HU. Instead, the peak is at ~HU-900. Also, the peak is smooth and not as sharp as mine.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f2bde0691aa390746c2f40ac8d71383935d71d9.jpeg" data-download-href="/uploads/short-url/6JiqqR945HXPWmv2CPRTwFNdcDL.jpeg?dl=1" title="histogram (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f2bde0691aa390746c2f40ac8d71383935d71d9_2_689x500.jpeg" alt="histogram (1)" data-base62-sha1="6JiqqR945HXPWmv2CPRTwFNdcDL" width="689" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f2bde0691aa390746c2f40ac8d71383935d71d9_2_689x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f2bde0691aa390746c2f40ac8d71383935d71d9_2_1033x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f2bde0691aa390746c2f40ac8d71383935d71d9_2_1378x1000.jpeg 2x" data-dominant-color="85868F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">histogram (1)</span><span class="informations">2405×1743 382 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I am all for ignoring it but I am worried that there might actually be erroneous data being generated.</p>

---

## Post #45 by @lassoan (2021-12-10 19:41 UTC)

<p>Probably all voxels below -1024 is lumped into the that -1024 bin. As you can see, the peak does not go down all the way to 0 at that density value (either the image is darker or more of the air voxels are included in the segmentation), you see one large value. Probably you could eliminate this by reducing the lower range from -1024 to -1200 or so, or by adjusting the segmentation to include less “air” voxels.</p>

---

## Post #46 by @chuawm (2021-12-11 14:47 UTC)

<p>Ok thanks for helping <a class="mention" href="/u/lassoan">@lassoan</a>. I tried using a wider threshold as you suggested (i.e. HU -1200) and also ensuring that the segmentation is as accurate as possible to exclude air that is not lungs but it still does not work.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3db93df41d5a47f1f3cc86b37c815c788d606f1e.jpeg" data-download-href="/uploads/short-url/8O20iHvmURIj2h6jildLZsKCDHE.jpeg?dl=1" title="ct chest spike" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3db93df41d5a47f1f3cc86b37c815c788d606f1e_2_690x283.jpeg" alt="ct chest spike" data-base62-sha1="8O20iHvmURIj2h6jildLZsKCDHE" width="690" height="283" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3db93df41d5a47f1f3cc86b37c815c788d606f1e_2_690x283.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3db93df41d5a47f1f3cc86b37c815c788d606f1e_2_1035x424.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3db93df41d5a47f1f3cc86b37c815c788d606f1e_2_1380x566.jpeg 2x" data-dominant-color="B0B0B7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ct chest spike</span><span class="informations">1920×789 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I think ideally it should have looked like the histogram in the 3D slicer sample data as this is what normal lung histogram looks like as seen below (peaking at about ~HU -900 without any spurious spike). I think the main issue is whether the other calculations (e.g. mean, skewness, kurtosis, perc) will be significantly affected by this spike.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd76c3ce6c68844e66353fa633a8c33dc6f331fe.jpeg" data-download-href="/uploads/short-url/AaffEV6c46UJagAL15qJhPbolum.jpeg?dl=1" title="normal densitogram" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fd76c3ce6c68844e66353fa633a8c33dc6f331fe_2_503x500.jpeg" alt="normal densitogram" data-base62-sha1="AaffEV6c46UJagAL15qJhPbolum" width="503" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fd76c3ce6c68844e66353fa633a8c33dc6f331fe_2_503x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fd76c3ce6c68844e66353fa633a8c33dc6f331fe_2_754x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fd76c3ce6c68844e66353fa633a8c33dc6f331fe_2_1006x1000.jpeg 2x" data-dominant-color="F7F7F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">normal densitogram</span><span class="informations">1025×1018 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I will try on more studies but so far I am not getting it to work.</p>
<p>On another note, would you happen to know when <a class="mention" href="/u/raul">@raul</a> will be approving the pull request?</p>
<p>Thanks alot!</p>

---

## Post #47 by @lassoan (2021-12-11 14:59 UTC)

<p>You haven’t changed the histogram bin lower range from -1024. Changing the plot view’s zoom does not change the histogram bins. If adjusting the histogram bin range is not exposed on the GUI then you need to edit the Python script of the module.</p>

---

## Post #48 by @chuawm (2021-12-11 15:50 UTC)

<p>Oh yes, I just realized that as well. I had a look at the script. It seems that there is no lower limit for the histogram. Is this correct?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d28dec0a5453f918a10fd13161ed209dee77d838.jpeg" data-download-href="/uploads/short-url/u2EkN4xxFsfz5VNa11xxk2j1czC.jpeg?dl=1" title="cip script" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d28dec0a5453f918a10fd13161ed209dee77d838_2_318x500.jpeg" alt="cip script" data-base62-sha1="u2EkN4xxFsfz5VNa11xxk2j1czC" width="318" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d28dec0a5453f918a10fd13161ed209dee77d838_2_318x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d28dec0a5453f918a10fd13161ed209dee77d838_2_477x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d28dec0a5453f918a10fd13161ed209dee77d838_2_636x1000.jpeg 2x" data-dominant-color="343841"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cip script</span><span class="informations">1690×2656 460 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Anyway, it still does not make sense as I feel that lungs should not have any density at or lower than HU -1024 if they are normal. We can see from the sample data that the range of densities does not come close to HU -1000.</p>

---

## Post #49 by @lassoan (2021-12-11 16:29 UTC)

<p>It all looks good to me. Probably the WholeLung segment includes the trachea, which is all air. The intensity barely goes below -1024, maybe by 5 bins, which can be due to noise and slight miscalibration of the CT.</p>
<p>It is also interesting to note that the shape of the intensity histogram may depend on the resolution of the CT due to the partial volume effect. A higher-resolution scan will contain more voxels that are completely filled with air, therefore the histogram will have a thicker tail (more voxels with approximately -1000 HU).</p>

---

## Post #50 by @rbumm (2021-12-12 09:57 UTC)

<p>I get the same vertical histogram bar at -1024 … obviously, the voxel intensities at and below -1024 seem to be pooled at this value.</p>
<p>Threshold segmentation (range -1024 to -1024):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6e9e153ea38d6e6657a1f933445aecada4a6668.jpeg" alt="image" data-base62-sha1="nOAlsloI9pKJDIXCT1oNU5GGl3G" width="330" height="386"></p>

---

## Post #51 by @chuawm (2021-12-14 14:34 UTC)

<p>Thanks <a class="mention" href="/u/rbumm">@rbumm</a> and <a class="mention" href="/u/lassoan">@lassoan</a> ! Yes I tried a few more cases and even used another program to test. All of them return a spike and it is likely due to the smaller airways or air pockets that we cannot exclude. I might have to adjust the threshold higher if I want to remove the spike.</p>
<p>Thanks again!</p>

---

## Post #52 by @rbumm (2021-12-19 17:43 UTC)

<p>Checked this out a little further and - sorry to say - I can not reproduce the disturbing vertical spike at -1024 when implementing my own histogram chart with scatterbars in the LungCTAnalyzer:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc47ca0bb688e75dacb889bd633796bbe16f904f.jpeg" data-download-href="/uploads/short-url/qRBzttyTmcCnX1CVN1XFTjRgGsL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc47ca0bb688e75dacb889bd633796bbe16f904f_2_690x244.jpeg" alt="image" data-base62-sha1="qRBzttyTmcCnX1CVN1XFTjRgGsL" width="690" height="244" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc47ca0bb688e75dacb889bd633796bbe16f904f_2_690x244.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc47ca0bb688e75dacb889bd633796bbe16f904f_2_1035x366.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc47ca0bb688e75dacb889bd633796bbe16f904f.jpeg 2x" data-dominant-color="777E81"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1379×488 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Tested several CTs with the new function not showing a spike. Unfortunately, I can not check this against Parenchyma Analysis of CIP because although CIP can be loaded with yesterday’s Slicer preview (4.13.0-2021-12-17 r30503 / fff83f9) it results in all kinds of error messages, and Parenchyma Analysis is not initialized.</p>
<p>So if you all agree I will probably include a histogram table and chart production as an additional output in LungCTAnalyzer.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23fb1f3893b83b4b9eed257021777db5ad8c68a8.png" alt="image" data-base62-sha1="58iJK0ZRc5Zi4rOfjvBuUh5iWxy" width="492" height="413"></p>

---

## Post #53 by @lassoan (2021-12-19 22:23 UTC)

<p>It is better to fix the existing Parenchyma analyzer module than duplicating the feature in Lung CT analyzer: it keeps lung CT analyzer module slightly sinpler and significantly reduces maintenance workload (no need to maintain the same feature in two places).</p>

---

## Post #55 by @rbumm (2022-01-03 13:01 UTC)

<p>Happy new year, <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<blockquote>
<blockquote>
<p>It is better to fix the existing Parenchyma analyzer module</p>
</blockquote>
</blockquote>
<p>Although I was a bit reluctant (possible delays of getting CIP PR’s accepted) I was able to fork and locally build Slicer_CIP, as far as I see without errors. Now I am stuck on how to locally install this extension build in my recently compiled Slicer from disk. How would you recommend doing so? Use the Developer Tools → Extension Wizard or is there a command-line option?</p>

---

## Post #56 by @lassoan (2022-01-03 13:34 UTC)

<p>I usually just add the module folders to “additional module paths” in application settings. See some more details here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#run-slicer-with-your-custom-modules" class="inline-onebox">Extensions — 3D Slicer documentation</a></p>

---

## Post #57 by @rbumm (2022-01-03 14:00 UTC)

<p>Great, works.</p>
<p>It turns out that loading the current Slicer_CIP in two recent Slicer previews throws seven “No module named Editor” exceptions like this:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "C:\D\S4R\python-install\Lib\imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "C:/D_CIP/SlicerCIP/SlicerCIP-build/inner-build/lib/Slicer-4.13/qt-scripted-modules/CIP_RVLVRatio.py", line 10, in &lt;module&gt;
    from CIP.ui import CaseReportsWidget
  File "C:\D_CIP\SlicerCIP\SlicerCIP-build\inner-build\lib\Slicer-4.13\qt-scripted-modules\CIP\ui\__init__.py", line 1, in &lt;module&gt;
    from .CIP_EditorWidget import CIP_EditorWidget
  File "C:\D_CIP\SlicerCIP\SlicerCIP-build\inner-build\lib\Slicer-4.13\qt-scripted-modules\CIP\ui\CIP_EditorWidget.py", line 7, in &lt;module&gt;
    from Editor import EditorWidget
ModuleNotFoundError: No module named 'Editor'  
</code></pre>
<p>Probably easy to solve ?</p>

---

## Post #58 by @lassoan (2022-01-03 14:54 UTC)

<p>The Editor module has been removed from Slicer. The replacement may not be trivial, but should improve the extension. This may be a good task for the upcoming project week.</p>

---

## Post #59 by @chuawm (2022-04-13 10:19 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> For the spike, I realized it depends on what kernel the images were acquired in. If I used images reconstructed with smooth kernel (soft tissue window), the spikes will not be there. But if I used images reconstructed with lung kernel (lung window), then the spikes will be there.</p>
<p>Lung Kernel example:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdb5d3092e135a707016c91d1ec72a398138ab99.png" data-download-href="/uploads/short-url/tlNraXjKleM6RIDkhRI9GNiLZ4B.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdb5d3092e135a707016c91d1ec72a398138ab99_2_690x426.png" alt="image" data-base62-sha1="tlNraXjKleM6RIDkhRI9GNiLZ4B" width="690" height="426" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdb5d3092e135a707016c91d1ec72a398138ab99_2_690x426.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdb5d3092e135a707016c91d1ec72a398138ab99_2_1035x639.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdb5d3092e135a707016c91d1ec72a398138ab99.png 2x" data-dominant-color="FBF9F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1230×761 49 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14340ae451bf6c81fb25cd3113d980d267566da0.jpeg" data-download-href="/uploads/short-url/2SJ36ooTs5bMQh4O9gKaXewAmic.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14340ae451bf6c81fb25cd3113d980d267566da0_2_576x500.jpeg" alt="image" data-base62-sha1="2SJ36ooTs5bMQh4O9gKaXewAmic" width="576" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14340ae451bf6c81fb25cd3113d980d267566da0_2_576x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14340ae451bf6c81fb25cd3113d980d267566da0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14340ae451bf6c81fb25cd3113d980d267566da0.jpeg 2x" data-dominant-color="77736D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">743×644 93.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Smooth kernel example of same patient:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/9679bb7a60d0d0657ead435c6f316137c92d76c1.png" data-download-href="/uploads/short-url/ltaqImfhvPMCl3o0VCMeO9ZY95n.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9679bb7a60d0d0657ead435c6f316137c92d76c1_2_690x429.png" alt="image" data-base62-sha1="ltaqImfhvPMCl3o0VCMeO9ZY95n" width="690" height="429" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9679bb7a60d0d0657ead435c6f316137c92d76c1_2_690x429.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9679bb7a60d0d0657ead435c6f316137c92d76c1_2_1035x643.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/9679bb7a60d0d0657ead435c6f316137c92d76c1.png 2x" data-dominant-color="FBF9F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1219×759 51 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d28275d31cba509c9441bf0872517272362a690.jpeg" data-download-href="/uploads/short-url/fzE4xRusl51sM6MzcRumjBMTNL2.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d28275d31cba509c9441bf0872517272362a690_2_606x500.jpeg" alt="image" data-base62-sha1="fzE4xRusl51sM6MzcRumjBMTNL2" width="606" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d28275d31cba509c9441bf0872517272362a690_2_606x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d28275d31cba509c9441bf0872517272362a690.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d28275d31cba509c9441bf0872517272362a690.jpeg 2x" data-dominant-color="423D36"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">790×651 67.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Not sure if that helps.</p>
<p>By the way, <a class="mention" href="/u/lassoan">@lassoan</a> do you know if the parenchyma analysis module has been fixed?</p>

---

## Post #60 by @lassoan (2022-04-13 20:18 UTC)

<p>Forget about that peak. You can safely ignore that. The segment have thousands of voxels and the peak is just a few dozens voxels.</p>
<aside class="quote no-group" data-username="chuawm" data-post="59" data-topic="10697">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chuawm/48/11915_2.png" class="avatar"> chuawm:</div>
<blockquote>
<p>By the way, <a class="mention" href="/u/lassoan">@lassoan</a> do you know if the parenchyma analysis module has been fixed?</p>
</blockquote>
</aside>
<p>It was a long time ago, but I think it works well in current Slicer Preview Release.</p>

---
