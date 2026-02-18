# Semi-automatic segmentation tools-PET image-Head and Neck cancer

**Topic ID**: 21074
**Date**: 2021-12-15
**URL**: https://discourse.slicer.org/t/semi-automatic-segmentation-tools-pet-image-head-and-neck-cancer/21074

---

## Post #1 by @MPhilip (2021-12-15 10:23 UTC)

<p>Operating system: Windows 10 enterprise<br>
Slicer version:4.13.0-2021-12-02<br>
Hi</p>
<p>I would like to know which are the semi-automatic segmentation tools available in 3D Slicer which could be used for segmenting tumour in head and neck cancer patients on PET images.<br>
I came across watershed, grow from seeds and thresholding(including automatic methods). Are there any other methods that I am not aware of, including extensions?<br>
I have seen that grow from seeds is equivalent to grow cut algorithm.<br>
I had gone through this link too :<a>https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html</a></p>
<p>Would appreciate any suggestions.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @chribaue (2021-12-15 14:53 UTC)

<p>There is a “PETTumorSegmentation” extension developed by the University of Iowa, as part of their PET Analysis tools: <a href="https://qin.iibi.uiowa.edu/" rel="noopener nofollow ugc">https://qin.iibi.uiowa.edu/</a></p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/PETTumorSegmentation" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/PETTumorSegmentation</a></p>
<p>It’s a semi-automated tool that’s available as Slicer Editor Effect and Segment Editor Effect.<br>
The video on the documentation website uses the “Legacy Editor”, which was available in 3D Slicer until the most recent stable release.<br>
It was replaced in favor of the Segment Editor, which has a slightly different user interface.</p>
<p>You can use the PET Tumor Segment Editor Effect either in the most recent stable release of Slicer or in the most recent nightly version. In the Slicer version:4.13.0-2021-12-02 mentioned by you, it was broke.</p>
<p>Best,<br>
Christian</p>

---

## Post #3 by @MPhilip (2021-12-15 15:15 UTC)

<p>Thanks for the reply. The tool looks promising and the video provided on the documentation  is very easy to follow.</p>
<p>Would it be possible to calculate other textural features from the segmented region using the radiomics extension on 3Dslicer ?<br>
What is the algorithm called-is it graph cut algorithm or JCI ?</p>
<p>Would like to know.</p>
<p>Thanks</p>

---

## Post #4 by @MPhilip (2021-12-15 15:15 UTC)

<p>It would be very helpful if links to any tutorials(preferably videos) on how to implement Otsu thresholding and watershed segmentation on PET images could be provided.<br>
I came across these links:<br>
Watershed-<a>https://discourse.slicer.org/t/watershed-fast-marching-and-flood-filling-effects-in-segment-editor/104</a><br>
Otsu-<a>https://www.slicer.org/wiki/Modules:OtsuThresholdSegmentation-Documentation-3.6</a></p>
<p>Thanks</p>

---

## Post #5 by @chribaue (2021-12-15 15:23 UTC)

<blockquote>
<p>What is the algorithm called-is it graph cut algorithm or JCI ?</p>
</blockquote>
<p>You can find details of the algorithm and an evaluation in Beichel et al. (2016): “Semiautomated Segmentation of Head and Neck Cancers in 18F-FDG PET Scans: A Just-Enough-Interaction Approach”, in Medical Physics. <a href="http://dx.doi.org/10.1118/1.4948679" rel="noopener nofollow ugc">http://dx.doi.org/10.1118/1.4948679</a><br>
JEI stands for Just-Enough-Interactions; i.e. as few clicks as needed to get the job done.</p>
<blockquote>
<p>Would it be possible to calculate other textural features from the segmented region using the radiomics extension on 3Dslicer ?</p>
</blockquote>
<p>Certainly. The PET Tumor Segment Editor Effect works on “Segmentations” like any other Segment Editor Effect .</p>

---

## Post #6 by @MPhilip (2021-12-15 15:55 UTC)

<p>Thanks for the answers.</p>
<p>I had a quick look at the paper which was shown in the video before posting the previous questions, but I think I am not sure about the name of the algorithm. Can it be called JCI algorithm (I could see it as JCI principle in the paper) or a modified graph cut algorithm?</p>
<p>Thank you</p>

---

## Post #7 by @chribaue (2021-12-15 16:10 UTC)

<p>In the paper we use the acronym JEI (Just-Enough-Interaction) to refer to the overall principle of the segmentation approach. (not JCI)</p>
<p>The algorithm uses an optimal surface segmentation (OSS) approach, which is a variant of the LOGISMOS (layered optimal graph image segmentation of multiple objects and surfaces) segmentation framework:</p>
<blockquote>
<p>Y. Yin, X. Zhang, R. Williams, X. Wu, D. D. Anderson, and M. Sonka, “LOGISMOS–layered optimal graph image segmentation of multiple objects and surfaces: Cartilage segmentation in the knee joint,” <em>IEEE Trans. Med. Imaging</em> 29, 2023– 2037 (2010).<a href="https://doi.org/10.1109/TMI.2010.2058861" rel="noopener nofollow ugc">10.1109/TMI.2010.2058861</a></p>
</blockquote>
<p>It’s not a modified graph-cut. You may call it a LOGISMOS-based approach, if you really have to label it.</p>

---

## Post #8 by @MPhilip (2021-12-15 16:21 UTC)

<p>Thank you very much for your response and for the link to the paper. Now it is clear, which approach is used.</p>
<p>Yes, it is JEI and not JCI. Sorry about that.</p>

---

## Post #10 by @MPhilip (2022-01-26 10:05 UTC)

<p>Hi <a class="mention" href="/u/chribaue">@chribaue</a><br>
I have a PET image as below(image 1-manually segmented tumour and 3D view).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d44be12ea804cbcaed0f036c6675816b75e8c336.png" data-download-href="/uploads/short-url/ui3NieOnSm3if39EhGt6YWT3wj4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d44be12ea804cbcaed0f036c6675816b75e8c336_2_690x373.png" alt="image" data-base62-sha1="ui3NieOnSm3if39EhGt6YWT3wj4" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d44be12ea804cbcaed0f036c6675816b75e8c336_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d44be12ea804cbcaed0f036c6675816b75e8c336_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d44be12ea804cbcaed0f036c6675816b75e8c336.png 2x" data-dominant-color="C0C1CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1084×587 46.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But on this image when I use JEI tool on 3DSlicer only one among those regions can be selected(Image 2). May I know how can I select both regions? Do I need to move through different slices? Do I need to use ‘create new’ option?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4482e3ca0584150ed7f268291de44c7e207f584.png" data-download-href="/uploads/short-url/s0oehSpQGdgHR6lJrQGm38Pr25K.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4482e3ca0584150ed7f268291de44c7e207f584_2_690x306.png" alt="image" data-base62-sha1="s0oehSpQGdgHR6lJrQGm38Pr25K" width="690" height="306" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4482e3ca0584150ed7f268291de44c7e207f584_2_690x306.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4482e3ca0584150ed7f268291de44c7e207f584_2_1035x459.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4482e3ca0584150ed7f268291de44c7e207f584_2_1380x612.png 2x" data-dominant-color="A7A7A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1705×757 49.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
When I click on the other yellow region it becomes like this.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1ffd1ffcb7c9c6d61935814bebfe670ebcc3465.png" data-download-href="/uploads/short-url/rGcf91aJ9dUF4YnDJfNoN1RZ6rX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1ffd1ffcb7c9c6d61935814bebfe670ebcc3465_2_690x316.png" alt="image" data-base62-sha1="rGcf91aJ9dUF4YnDJfNoN1RZ6rX" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1ffd1ffcb7c9c6d61935814bebfe670ebcc3465_2_690x316.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1ffd1ffcb7c9c6d61935814bebfe670ebcc3465_2_1035x474.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1ffd1ffcb7c9c6d61935814bebfe670ebcc3465_2_1380x632.png 2x" data-dominant-color="ADAEAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1660×762 50.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
when I move through different slices, I can’t see the JEI segmented regions on those slices, I can see only the manual one(yellow region) as shown below. Am I doing it correct?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95343af94553cce39e5ac0a25968b6d36d34e430.png" data-download-href="/uploads/short-url/lhV2RmtYxal2EWpHL1IRv6tp8mQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95343af94553cce39e5ac0a25968b6d36d34e430.png" alt="image" data-base62-sha1="lhV2RmtYxal2EWpHL1IRv6tp8mQ" width="690" height="461" data-dominant-color="EEEEED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">815×545 8.22 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The below is another image. When I clicked(JEI tool) on the manually segmented tumour(yellow) only a small portion of the tumour is selected(red colour) which does not include the entire tumour. Do I need to click multiple times? Or do I need to make changes in the interaction style, and select from various options and advanced options?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/031e04eb12ee4550f1fd961035d88ac4c1566018.png" data-download-href="/uploads/short-url/rzKoncfI2fwUSNqVlagQLy47EI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/031e04eb12ee4550f1fd961035d88ac4c1566018_2_690x304.png" alt="image" data-base62-sha1="rzKoncfI2fwUSNqVlagQLy47EI" width="690" height="304" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/031e04eb12ee4550f1fd961035d88ac4c1566018_2_690x304.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/031e04eb12ee4550f1fd961035d88ac4c1566018_2_1035x456.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/031e04eb12ee4550f1fd961035d88ac4c1566018_2_1380x608.png 2x" data-dominant-color="A7A7A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1743×768 53.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hope you would be able to help.</p>
<p>Thanks</p>

---

## Post #11 by @chribaue (2022-01-26 15:09 UTC)

<p>The PETTumorSegmentationTool is semi-automatic. It needs the user to decide what high-uptake parts should get included and it offers the user options to achieve their desired results with only few clicks.</p>
<p>This means that the user has to be familiar with the tool’s options and it takes some training/experience to know how to best approach more complex cases.</p>
<p>Start with the documentation: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/PETTumorSegmentEditorEffect" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Modules/PETTumorSegmentEditorEffect - Slicer Wiki</a><br>
and read the paper: Semi-automated Segmentation of Head and Neck Cancers in 18F-FDG PET Scans: A Just-Enough-Interaction Approach", in Medical Physics, 2016.<br>
again. Then you should be able to understand the different options and that the tool is designed to segment blob-like structures.</p>
<p>To segment multiple disconnected blobs or an elongated lesion that seems to consist of multiple parts as part of one “Slicer Segment” , it’s best to segment those parts individually using “Create new”.</p>
<p>For the first example you showed above, you want to segment two different uptake areas and combine them into one mask. After segmenting the first lesion, you have to switch to “Create new” and segment the second one. From the image it seems you used the “Global refinement” which is certainly not what you wanted.</p>
<p>For the second example you showed, it is also unclear to the algorithm if the neighboring high uptake regions are also part of same lesion or e.g. inflammation or another lesion/lymph node. The user needs to make that decision. In your case, you want all these parts included. Probably the best approach to achieve this is to use “Create new” for the additional regions.</p>
<p>Hope that helps.</p>

---

## Post #12 by @MPhilip (2022-01-26 15:22 UTC)

<p>Thank you very much. It was helpful indeed.</p>

---

## Post #13 by @MPhilip (2022-01-27 09:29 UTC)

<p><a class="mention" href="/u/chribaue">@chribaue</a><br>
I have a follow-up question.<br>
In the case of JEI or any other semi-automatic segmentation tools, is it necessary that the lesion to be segmented is identified from all those disconnected parts of the tumour individually by moving through different slices(say, in the sagittal view) in order for the algorithm to segment the tumour correctly,  for an image like example 1? I have seen that if I locate the tumour on just one or two slices in a particular view, after applying the segmentation, in the 3D view of the segmented tumour I could see that the entire tumour was not segmented including disconnected blobs or elongated lesions and the volume of the semi-automatically segmented tumour is far too small compared to the manually segmented volume.<br>
I could read in the paper that one of the limitations of the algorithm is: in some cases more than ten user actions are necessary to produce a segmentation of a lesion. Is this the case with the PET image in example 1?</p>
<p>Hope you would be able to help.</p>
<p>Thank you</p>

---

## Post #14 by @chribaue (2022-01-27 14:15 UTC)

<p><a class="mention" href="/u/mphilip">@MPhilip</a><br>
I hope I understand your questions correctly.</p>
<blockquote>
<p>…semi-automatic segmentation tools, is it necessary that the lesion to be segmented is identified from all those disconnected parts of the tumour individually…</p>
</blockquote>
<p>I think with any semi-automated tool you would have to click into each disconnected part at least once.<br>
If the algorithm would be able by itself to identify other regions and classify which of them are part of the tumor you have in mind, it would be basically a fully-automated algorithm.</p>
<p>The doctors at our hospital specify a lesion to always be one connected region. And each lymph node in a lymph node chain or adjacent to the primary tumor is considered a separate lesion. Thus, your example 1 would be considered as 4 separate lesions.<br>
Lymph nodes are typically small and roundish, they can often get segmented with only one click (and the right setting: “splitting on”). More complex lesions might need more than one click.</p>
<blockquote>
<p>I locate the tumour on just one or two slices in a particular view, after applying the segmentation…</p>
</blockquote>
<p>You have to click roughly at the 3D center of the lesion that you want to segment.<br>
Once you identify a lesion, you have to move the view/slice roughly to the 3D center of the lesion and select a center point there, otherwise you might specify a point at the periphery of the lesion and the algorithm is not designed for that.</p>
<p>It’s best to first get a mental impression of the lesion in the CT scan before you start segmenting it. Turning “Slice intersections” on and pressing the “shift key” while moving over one of the 3D views to position the other 2 views helps me a lot to select proper axial, coronal, and sagittal views around the lesion’s center, before I start segmenting.</p>

---

## Post #15 by @MPhilip (2022-01-28 11:33 UTC)

<p>Hi <a class="mention" href="/u/chribaue">@chribaue</a></p>
<p>Thank you for your time in replying to my query in detail.<br>
I’m not quite sure whether I got this right:</p>
<blockquote>
<p>‘You have to click roughly at the 3D center of the lesion that you want to segment.<br>
Once you identify a lesion, you have to move the view/slice roughly to the 3D center of the lesion and select a center point there’</p>
</blockquote>
<p>In the case of a disconnected blob or elongated lesion, I felt that it is taking some time to locate  the tumour on different slices/views. Is it right to locate the tumour on different views rather than on different slices?<br>
Was this the 3D view(shown below) that will give an overall picture of the tumour before using any semi-automatic segmentation tools?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c90bf3daa01508152abdf223cd807c5d13f6bfa9.png" data-download-href="/uploads/short-url/sGxzWIkXOw9oSx5Ns6wxCAa5rGp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c90bf3daa01508152abdf223cd807c5d13f6bfa9_2_690x476.png" alt="image" data-base62-sha1="sGxzWIkXOw9oSx5Ns6wxCAa5rGp" width="690" height="476" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c90bf3daa01508152abdf223cd807c5d13f6bfa9_2_690x476.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c90bf3daa01508152abdf223cd807c5d13f6bfa9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c90bf3daa01508152abdf223cd807c5d13f6bfa9.png 2x" data-dominant-color="B1B3DB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">691×477 50.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I have done a semi-automatic segmentation using the JEI tool on this image and it is segmented as below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9db6980259a2e27c036ca8beab0249acb975dfd9.png" data-download-href="/uploads/short-url/mvcaqITwejU93HY80uZZCdwpqZj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9db6980259a2e27c036ca8beab0249acb975dfd9_2_690x272.png" alt="image" data-base62-sha1="mvcaqITwejU93HY80uZZCdwpqZj" width="690" height="272" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9db6980259a2e27c036ca8beab0249acb975dfd9_2_690x272.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9db6980259a2e27c036ca8beab0249acb975dfd9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9db6980259a2e27c036ca8beab0249acb975dfd9.png 2x" data-dominant-color="C1C1C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">866×342 75.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
the 3d view is as below<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a4a077e18f7a379a787b1ac3f808f8ff902cdfd.png" alt="image" data-base62-sha1="3Kz1jw73ZxEieMevBPAmxO8j2W1" width="688" height="465"><br>
The volume appears smaller than the manually segmented tumour.<br>
Can it be improved or is this just right?<br>
I had experimented with other options available, but could not find any improvement.<br>
Hope you would be kind enough to comment on this.</p>
<p>Thanks in advance.</p>

---

## Post #16 by @chribaue (2022-01-31 19:32 UTC)

<p>Hi <a class="mention" href="/u/mphilip">@MPhilip</a></p>
<p>Our training material/tutorials were mostly designed to teach our tools to medical professionals who are familiar with tracing lesions using standard clinical tools/viewers and who have the medical expertise identifying lesions. I’m not sure if I can teach you all of that, but I’ll try my best helping you with your questions:</p>
<blockquote>
<p>In the case of a disconnected blob or elongated lesion…</p>
</blockquote>
<p>You have to split such a case into regions that you segment separately.</p>
<blockquote>
<p>I felt that it is taking some time to locate the tumour on different slices/views</p>
</blockquote>
<p>Once I find the lesion in any of the 3 (red/green/yellow) slice views, it takes me just a few seconds to find axial/coronal/saggital slices close to a lesion center. Using the “Slicer Intersection” is really very helpful in this process:</p>
<p>Turn it on via the Slicer main tool bar:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/248fa7eda37ba6cb98ef63b99c35555ef60b7465.png" alt="image" data-base62-sha1="5dqYal80nOrfPz3dZ2UF8YaN40Z" width="180" height="201"></p>
<p>Example: Initial view of PET scan with a lesion and slice intersections turned on:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6ab47b0c565872c2efc53824a89f6fe0e594aae0.jpeg" data-download-href="/uploads/short-url/fdXhYllV3noYlRNfuUqchTMIX84.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ab47b0c565872c2efc53824a89f6fe0e594aae0_2_340x250.jpeg" alt="image" data-base62-sha1="fdXhYllV3noYlRNfuUqchTMIX84" width="340" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ab47b0c565872c2efc53824a89f6fe0e594aae0_2_340x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ab47b0c565872c2efc53824a89f6fe0e594aae0_2_510x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ab47b0c565872c2efc53824a89f6fe0e594aae0_2_680x500.jpeg 2x" data-dominant-color="979897"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1776×1309 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Find lesion in one of the views; e.g. the yellow one in this case. Then move mouse cursor there while holding the shift-key down. When you’re there, release the shift-key. This will get the red and green slice to show the lesion as well.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/6050466d729f3457a514449b515ee41003e132ef.jpeg" data-download-href="/uploads/short-url/dK1Pckm9toIWQz9e61j9VThu6Zh.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6050466d729f3457a514449b515ee41003e132ef_2_340x250.jpeg" alt="image" data-base62-sha1="dK1Pckm9toIWQz9e61j9VThu6Zh" width="340" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6050466d729f3457a514449b515ee41003e132ef_2_340x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6050466d729f3457a514449b515ee41003e132ef_2_510x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6050466d729f3457a514449b515ee41003e132ef_2_680x500.jpeg 2x" data-dominant-color="9A9B9A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1444×1073 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In the red/green slices you can see that the yellow slice is not close to the lesion center. Move it closer to the center by again holding down the shift-key and moving the mouse cursor to the center of the structure in the red or green slice. Now we have all views close to the lesion center:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53fcb08c72d3eac92b3b7ffc99381d7db45ec108.jpeg" data-download-href="/uploads/short-url/bYZ0W5j2MutBNGa4VdNSn2vQXCo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53fcb08c72d3eac92b3b7ffc99381d7db45ec108_2_340x250.jpeg" alt="image" data-base62-sha1="bYZ0W5j2MutBNGa4VdNSn2vQXCo" width="340" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53fcb08c72d3eac92b3b7ffc99381d7db45ec108_2_340x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53fcb08c72d3eac92b3b7ffc99381d7db45ec108_2_510x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53fcb08c72d3eac92b3b7ffc99381d7db45ec108_2_680x500.jpeg 2x" data-dominant-color="9A9A99"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1430×1061 95.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<blockquote>
<p>Was this the 3D view(shown below) that will give an overall picture of the tumour before using any semi-automatic segmentation tools?</p>
</blockquote>
<p>I think to get a complete picture of the lesion and segmentation you need to move through all the slices it intersects, preferably in all 3 anatomic planes.</p>
<blockquote>
<p>The volume appears smaller than the manually segmented tumour. Can it be improved or is this just right?</p>
</blockquote>
<p>When we designed the algorithm, we adjusted it to reflect the tracing behavior of our most experienced radiation oncologist (where he would set the boundary based on properties of the lesion and its surrounding area). But different medical experts have different preferences; some draw the contours slightly larger or smaller than others.</p>
<p>If based on your medical experience you think that after the initial segmentation the overall contour is too small, you can use the “global refinement” option to adjust the gray-value level obtained by the algorithm. Switch to this option and click in the PET scan on a location for the surface that reflects the gray-level you think is right. The whole surface will adjust to this gray-level.</p>

---

## Post #17 by @MPhilip (2022-02-02 09:20 UTC)

<p>Hi <a class="mention" href="/u/chribaue">@chribaue</a></p>
<p>Thank you very much for explaining everything in detail. This is very easy to follow and the ‘slice intersections’ option is a time saver. Thanks for introducing this to me as I am not a medical professional and have no medical expertise in tracing lesions. I am using 3D slicer for my research for the first time.</p>
<p>In the below image I was unable to segment all the disconnected blob using the ‘<strong>PET tumour segmentation</strong>’ tool even after turning ON the ‘<strong>slice intersections</strong>’ option. As you can see in the <strong>3D view</strong> entire tumour is not identified(the 3D view in <em>green</em> which is segmented using the tool as compared to the <em>yellow</em> 3D view of the tumour which was segmented manually).<br>
The 3D view of tumour segmented using ‘PET segmentation tool’ appears as below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8902242992b32b1145704a055a7a1c4aa067db83.png" data-download-href="/uploads/short-url/jy20492HQkGOL55jZAjAcryYa1Z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8902242992b32b1145704a055a7a1c4aa067db83_2_690x285.png" alt="image" data-base62-sha1="jy20492HQkGOL55jZAjAcryYa1Z" width="690" height="285" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8902242992b32b1145704a055a7a1c4aa067db83_2_690x285.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8902242992b32b1145704a055a7a1c4aa067db83_2_1035x427.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8902242992b32b1145704a055a7a1c4aa067db83_2_1380x570.png 2x" data-dominant-color="BFBFC5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1913×792 91.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The 3D view of the tumour segmented manually appears different and it is clear that there are some unidentified regions that are visible only if I scroll through any of these slice views(sagittal/axial/coronal) as shown below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dacfbc4bf3381a967f86a5a3f1c85d58e222b954.png" data-download-href="/uploads/short-url/vdH9UBsIOhj5n5dcviT4XI0NCsY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dacfbc4bf3381a967f86a5a3f1c85d58e222b954_2_690x261.png" alt="image" data-base62-sha1="vdH9UBsIOhj5n5dcviT4XI0NCsY" width="690" height="261" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dacfbc4bf3381a967f86a5a3f1c85d58e222b954_2_690x261.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dacfbc4bf3381a967f86a5a3f1c85d58e222b954_2_1035x391.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dacfbc4bf3381a967f86a5a3f1c85d58e222b954_2_1380x522.png 2x" data-dominant-color="BABAC0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1912×726 93.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2e46979eb8907734593e0c475042b11ff15368e.png" data-download-href="/uploads/short-url/nf0IGnjwrnJPvdaY6OfiwlK2BZ4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2e46979eb8907734593e0c475042b11ff15368e_2_690x259.png" alt="image" data-base62-sha1="nf0IGnjwrnJPvdaY6OfiwlK2BZ4" width="690" height="259" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2e46979eb8907734593e0c475042b11ff15368e_2_690x259.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2e46979eb8907734593e0c475042b11ff15368e_2_1035x388.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2e46979eb8907734593e0c475042b11ff15368e_2_1380x518.png 2x" data-dominant-color="B8B8BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1911×719 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also in the below image, I find it a bit difficult to identify the lesion centre.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/4157ceb0c3642da0f46564de7d11f9b5f57c8261.png" data-download-href="/uploads/short-url/9k3a2R3WAk6wEVGlEFtymzKM7Ad.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4157ceb0c3642da0f46564de7d11f9b5f57c8261_2_690x303.png" alt="image" data-base62-sha1="9k3a2R3WAk6wEVGlEFtymzKM7Ad" width="690" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4157ceb0c3642da0f46564de7d11f9b5f57c8261_2_690x303.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/4157ceb0c3642da0f46564de7d11f9b5f57c8261_2_1035x454.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/4157ceb0c3642da0f46564de7d11f9b5f57c8261.png 2x" data-dominant-color="91929C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1275×561 39.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hope you would be able to guide me again.</p>
<p>Thanks in advance.</p>

---

## Post #18 by @chribaue (2022-02-02 14:50 UTC)

<p>I’ve watched medical professionals annotating image data/segmenting lesions in PET.</p>
<p>They typically start at the brain and go down the datasets through all axial slices using the mouse wheel. When they identify something they think might be a lesion, they might go up and down a couple slices around that structure and use the slice intersection to look at it in the coronal and sagittal views, maybe also going forward and backward a few slices there to get a good idea about the shape of structure and if it’s really tumor or some other high uptake structure that should not be segmented. To make this decision they might also look at the subject’s medical records, other scan modalities, or literature.</p>
<p>Once they decide that it actually is a lesion, they start the segmentation. They pick a point close to the center to start the segmentation. For an oddly shaped lesion this is not the center of the bounding box, but somewhere well inside the high uptake structure. After the initial segmentation they inspect the result carefully in at least 2 of the 3 planes, inspecting all slices that the structure intersects. If they are not satisfied with the segmentation, they use JEI to refine it. Once they approve the segmentation of that lesion, they keep going though the remaining dataset in a systematic manner. After they went trough the whole dataset, they might double-check everything one more time to make sure they didn’t miss anything.</p>
<p>In your case, you will have to do that too and you will still have to go through all slices of the image stack that contains the structures you are interested in. You will have to identify and segment all the 4 disjoint parts separately and use “global/local refinement”, “create new” or “splitting” to improve the segmentation if you think it is needed.</p>
<p>Our tool does not solve the high level tasks of identifying lesions and what parts to include in the segmentation. It helps the user segmenting the structures they decide to segment in a much more efficient and consistent way, compared to manual tracing, or other semi-automated tools that e.g. require adjusting thresholds etc.</p>

---

## Post #19 by @MPhilip (2022-02-02 15:01 UTC)

<p>Thank you very much <a class="mention" href="/u/chribaue">@chribaue</a> for the explanation. Thanks for your time.</p>

---

## Post #21 by @MPhilip (2022-08-04 11:32 UTC)

<p>Hi <a class="mention" href="/u/chribaue">@chribaue</a> . Could you please suggest a name which I can use for this tool while describing about it? In 3d slicer I can see when I hover over the icon the name ‘PET tumour segmentation’. Is it ideal to use that name? can I use the name ‘tool based on JEI principle’  I am looking for something like watershed, grow from seeds,42% SUVmax threshold etc.<br>
I would like to know whether this algorithm is based on JEI principle or LOGISMOS? You said in one of the above replies that it is based on LOGISMOS principle.<br>
I would like to know.<br>
Many thanks</p>

---
