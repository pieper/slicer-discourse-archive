# I want to know how to colour the exported models

**Topic ID**: 24476
**Date**: 2022-07-25
**URL**: https://discourse.slicer.org/t/i-want-to-know-how-to-colour-the-exported-models/24476

---

## Post #1 by @Luckypig (2022-07-25 09:18 UTC)

<p>Hello everyone,<br>
I find that the exported models have no color（STL format）.How can I make exported models have colors,because I find many people can make colorful models.<br>
Thanks to you all.</p>

---

## Post #2 by @Sam_Horvath (2022-07-25 14:06 UTC)

<p>So, the STL standard format does not support colors.  If you want to preserve color information when exporting, try exporting in another format such as OBJ.</p>

---

## Post #3 by @Luckypig (2022-07-25 14:34 UTC)

<p>Thank you for your answer,but when I export obj format, it still has no color.What is wrong  with my operation?</p>

---

## Post #4 by @Sam_Horvath (2022-07-25 14:39 UTC)

<p>Perhaps something like this will work: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-model-to-blender-including-color-by-scalar" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>

---

## Post #5 by @mikebind (2022-07-26 16:50 UTC)

<p>When you export to OBJ, you get two files, a .obj file which has the mesh information, and a .mtl file with the same base name which has the “material” information, which includes color.  When you want to load into another program which can handle OBJ files, you need to load both the .obj and .mtl files. Depending on the program, the color may automatically be applied to the mesh in this case, or you may need to apply the loaded material to the loaded object.</p>

---

## Post #6 by @lassoan (2022-07-26 19:33 UTC)

<p>I would recommend the <a href="https://github.com/PerkLab/SlicerOpenAnatomy#sliceropenanatomy">SlicerOpenAnatomy extension</a> for this. It can export models with color, transparency, hierarchy, and names preserved, to OBJ and glTF format.</p>

---

## Post #7 by @Luckypig (2022-07-26 23:37 UTC)

<p>Thank you, I have downloaded the extension, but I can’t click “export” after choosing model and format.</p>

---

## Post #8 by @lassoan (2022-07-27 09:49 UTC)

<p>You need to select a segmentation or a folder that contains model(s).</p>
<p>Exporting a single model is not really meaningful (you can then simply save it instead of using OpenAnatomy exporter module), but if you want to do that anyway then go to Data module, create a folder, and drag-and-drop your model into that.</p>

---

## Post #9 by @Luckypig (2022-07-27 12:50 UTC)

<p>THANK YOU! I have spent a lot of time on this <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=12" title=":sob:" class="emoji" alt=":sob:" loading="lazy" width="20" height="20"></p>

---

## Post #10 by @Luckypig (2022-07-27 14:33 UTC)

<p>But I still have a small question, when the Tr in MTL is 1, I can’t see my model.Only when I manually change Tr to 0 can the color be displayed normally.Is there a solution to this problem?</p>

---

## Post #11 by @mikebind (2022-07-28 21:06 UTC)

<p>Just a guess, but it would not be surprising if Tr stood for transparency, with 1.0 fully transparent (invisible), and 0.0 fully opaque.   In that case, it would be the correct behavior if objects with Tr 1.0 were not visible at all.</p>

---

## Post #12 by @Kamil.Kadyrov (2023-08-05 09:37 UTC)

<p>Hello everyone,<br>
I have a question regarding to this topic.<br>
I would like to export coloured model into the MSOffice software (Word, PP). How can i do that?<br>
I have got that STL cannot carry any colors. But my OBJ exports are also colorless in PP.<br>
If I’m using an online 3D viewer, there are no any problems with colors both for GLTF and OBJ.</p>
<p>And one more question on axes of exported files. If I’m using an STL in PP, model is shown in coronal plane (I mean antero-posterior view) and that’s OK. But if I’m using an OBJ, it is shown in axial plane (superio-infeior view) and this disturbs all the rotations of the model. Maybe I can export an OBJ file with coronal plane in default?</p>
<p>Thanks!</p>

---

## Post #13 by @lassoan (2023-08-05 10:46 UTC)

<p>I would recommend the <a href="https://github.com/PerkLab/SlicerOpenAnatomy">SlicerOpenAnatomy extension</a> this. It can export colors d segmentation to OBJ or glTF.</p>

---

## Post #14 by @Kamil.Kadyrov (2023-08-05 11:07 UTC)

<p>Dear Andras,</p>
<p>I have used this extension already, but OBJ export is colorless all the same. It’s colorless only in the MS Office soft.</p>

---

## Post #15 by @Kamil.Kadyrov (2023-08-05 11:40 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c485a7dca98796632eb44544e0719e38659e46d6.jpeg" data-download-href="/uploads/short-url/s2vWijmd8S7o2bJloFvQBG2DdA2.jpeg?dl=1" title="Screenshot_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c485a7dca98796632eb44544e0719e38659e46d6_2_682x500.jpeg" alt="Screenshot_2" data-base62-sha1="s2vWijmd8S7o2bJloFvQBG2DdA2" width="682" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c485a7dca98796632eb44544e0719e38659e46d6_2_682x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c485a7dca98796632eb44544e0719e38659e46d6.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c485a7dca98796632eb44544e0719e38659e46d6.jpeg 2x" data-dominant-color="5C7EBB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2</span><span class="informations">726×532 24.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is how it looks like.</p>

---

## Post #16 by @klc (2023-11-14 17:09 UTC)

<p>Hi, did you solve this problem ?<br>
Thanks</p>

---

## Post #17 by @mikebind (2023-11-14 19:38 UTC)

<p>OBJ files contain only geometrical information, not color information directly.  However, they can be saved with associated <code>.mtl</code> files which describe a material texture or color to apply to the object. Slicer saves these .mtl files when you export to OBJ.  Many applications that load OBJ files automatically look for an associated .mtl file in the same folder with the same name and, if present, apply that material automatically.  Other applications may require you to separately load the material file and apply it to the loaded object.</p>

---

## Post #18 by @klc (2023-11-15 04:22 UTC)

<p>Thank you for your reply.<br>
I am trying to import the mtl file in Unity but still no luck.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12527c56bf1bd578f0420afad167fa3133fb7159.jpeg" data-download-href="/uploads/short-url/2C5jNfajsG9UkZVTcL5q25U324h.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12527c56bf1bd578f0420afad167fa3133fb7159_2_690x348.jpeg" alt="image" data-base62-sha1="2C5jNfajsG9UkZVTcL5q25U324h" width="690" height="348" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12527c56bf1bd578f0420afad167fa3133fb7159_2_690x348.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12527c56bf1bd578f0420afad167fa3133fb7159_2_1035x522.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12527c56bf1bd578f0420afad167fa3133fb7159_2_1380x696.jpeg 2x" data-dominant-color="51504E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1936×978 226 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have put the mtl file in the assets folder and configured the materials accordingly but the color just wont show.</p>

---

## Post #19 by @lassoan (2023-11-15 04:59 UTC)

<p>I don’t think Unity can import material for obj file from mtl file. You may be able to convert to fbx and import that; or you can export to glTF from Slicer (using OpenAnatomy extension) and try if you can import it into Unity.</p>

---

## Post #20 by @klc (2023-11-15 07:12 UTC)

<p>Thank you for your reply. Exporting to glTF did work.<br>
For anyone wondering, glTF requires an extra step to be imported in unity</p><div class="youtube-onebox lazy-video-container" data-video-id="FbwZAyzo6Kc" data-video-title="GlTF or GLB import to Unity - glTF format" data-video-start-time="130s" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=FbwZAyzo6Kc&amp;t=130s" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/FbwZAyzo6Kc/maxresdefault.jpg" title="GlTF or GLB import to Unity - glTF format" width="" height="">
  </a>
</div>


---

## Post #21 by @Kamil.Kadyrov (2023-11-15 07:24 UTC)

<p>Hello!<br>
Firstly I export the segmentation to glTF using a <a href="https://github.com/PerkLab/SlicerOpenAnatomy" rel="noopener nofollow ugc">SlicerOpenAnatomy</a> extension. Then I uploaded this file to <a href="https://3dviewer.net/" rel="noopener nofollow ugc">3dviewer.net</a> website. After that i again export the file to glTF Binary (file extension .glb) using that website. That model in .GLB preserves colors while showing it via MS Office soft.<br>
I’m not sure will it wors for Unity or not, but you can try anyway.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c70013bd9d77c2710ee49b42d37a4ee5747c756.jpeg" data-download-href="/uploads/short-url/hKPaSPBQr6ijkeC4g8kSEnAsxq6.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c70013bd9d77c2710ee49b42d37a4ee5747c756_2_690x432.jpeg" alt="1" data-base62-sha1="hKPaSPBQr6ijkeC4g8kSEnAsxq6" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c70013bd9d77c2710ee49b42d37a4ee5747c756_2_690x432.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c70013bd9d77c2710ee49b42d37a4ee5747c756_2_1035x648.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c70013bd9d77c2710ee49b42d37a4ee5747c756.jpeg 2x" data-dominant-color="6F7172"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1275×800 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/413c2f27bf7d62e86d3ead61a0bdfb1597f0a86d.jpeg" data-download-href="/uploads/short-url/9j5YJI6ypOyTIugae3cCeRnjm1v.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/413c2f27bf7d62e86d3ead61a0bdfb1597f0a86d_2_690x432.jpeg" alt="2" data-base62-sha1="9j5YJI6ypOyTIugae3cCeRnjm1v" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/413c2f27bf7d62e86d3ead61a0bdfb1597f0a86d_2_690x432.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/413c2f27bf7d62e86d3ead61a0bdfb1597f0a86d_2_1035x648.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/413c2f27bf7d62e86d3ead61a0bdfb1597f0a86d.jpeg 2x" data-dominant-color="6C6F71"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1277×800 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7682f9bec1b3335f2e83f05842a8769db7a97e7.jpeg" data-download-href="/uploads/short-url/x17vOk1773Glu9Rlo8F7yrkRspN.jpeg?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7682f9bec1b3335f2e83f05842a8769db7a97e7_2_690x432.jpeg" alt="3" data-base62-sha1="x17vOk1773Glu9Rlo8F7yrkRspN" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7682f9bec1b3335f2e83f05842a8769db7a97e7_2_690x432.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7682f9bec1b3335f2e83f05842a8769db7a97e7_2_1035x648.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7682f9bec1b3335f2e83f05842a8769db7a97e7.jpeg 2x" data-dominant-color="A3B7DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1277×800 93.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #22 by @eNable_Polska (2024-08-03 17:25 UTC)

<p>Thank you for your solution, this is the answer to my question how to show segmentation in Oculus<br>
Simple and works fine</p>

---
