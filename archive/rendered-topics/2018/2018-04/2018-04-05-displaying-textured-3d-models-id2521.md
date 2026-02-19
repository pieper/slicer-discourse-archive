---
topic_id: 2521
title: "Displaying Textured 3D Models"
date: 2018-04-05
url: https://discourse.slicer.org/t/2521
---

# Displaying textured 3D models

**Topic ID**: 2521
**Date**: 2018-04-05
**URL**: https://discourse.slicer.org/t/displaying-textured-3d-models/2521

---

## Post #1 by @muratmaga (2018-04-05 16:38 UTC)

<p>I have a PLY made from a stereophotogrammatic scanner. It also has a texture file in jpg format. I tried setting the option for these texture files to “scalar overlay” and asked it to apply to the model I already loaded. When I do that, nothing happens, no error message nor the trace of the texture files as far as I can tell. There is no scalar listed under the “Scalar” tab of the models module.</p>
<p>This is with 4.8.1 on windows.</p>

---

## Post #2 by @lassoan (2018-04-05 16:52 UTC)

<p>If you loaded the ply file as a model and the jpg texture file as a volume, then you can apply the texture to the model by using <code>Texture model</code> module of SlicerIGT extension.</p>
<p>Example:</p>
<div class="lazyYT" data-youtube-id="PeyfyCs2tJg" data-youtube-title="Importing of color surface scans into 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #3 by @muratmaga (2018-04-05 18:38 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
I just installed IGT, I don’t seem to have textured mesh module as seen in video. I do have the <strong>texture model</strong> module, but it doesn’t seem to do anything when I choose the ply as the model, and the jpg as the texture and hit apply. If I check the  “set color information as point data”, then I get these error messages.</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/Murat/AppData/Roaming/NA-MIC/Extensions-26813/SlicerIGT/lib/Slicer-4.8/qt-scripted-modules/TextureModel.py”, line 114, in onApplyButton<br>
logic.applyTexture(self.inputModelSelector.currentNode(), self.inputTextureSelector.currentNode(), self.addColorAsPointAttributeCheckbox.checked)<br>
File “C:/Users/Murat/AppData/Roaming/NA-MIC/Extensions-26813/SlicerIGT/lib/Slicer-4.8/qt-scripted-modules/TextureModel.py”, line 131, in applyTexture<br>
self.convertTextureToPointAttribute(modelNode, textureImageNode)<br>
File “C:/Users/Murat/AppData/Roaming/NA-MIC/Extensions-26813/SlicerIGT/lib/Slicer-4.8/qt-scripted-modules/TextureModel.py”, line 153, in convertTextureToPointAttribute<br>
assert numOfPoints == tcoords.GetNumberOfTuples(), “Number of texture coordinates does not equal number of points”<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetNumberOfTuples’</p>

---

## Post #4 by @lassoan (2018-04-05 18:43 UTC)

<p>Yes, the module has been renamed to <code>Texture model</code>, as I wrote above.</p>
<p>It seems that your PLY does not have texture coordinates, therefore, you cannot apply a texture. It would be nice if you could add a check there in line 153 to display a message box if <code>tcoords is None</code> instead of just logging the error message and send a pull request.</p>
<p>Have you applied any processing to the PLY file that could have removed the texture coordinates?</p>

---

## Post #5 by @muratmaga (2018-04-05 18:45 UTC)

<p>Sorry, I don’t normally work with this data, so I don’t know whether there has been any processing done to it. This is from 3dMD. All I can say texture is visible when I load the same file into the meshlab.</p>

---

## Post #6 by @lassoan (2018-04-05 18:54 UTC)

<p>Can you share a data set?</p>

---

## Post #7 by @muratmaga (2018-04-05 19:07 UTC)

<p>Sure the 131015103819.jpg and 131015103819.ply in<br>
<a href="https://app.box.com/s/dp728p8q39mh0cytrv591ahne2veakr2" class="onebox" target="_blank" rel="nofollow noopener">https://app.box.com/s/dp728p8q39mh0cytrv591ahne2veakr2</a></p>

---

## Post #8 by @lassoan (2018-04-05 20:46 UTC)

<p>Thank you for the sample data. It seems that VTK cannot load texture coordinates from this .ply file. The simplest workaround is to load the data set in MeshLab and save as .obj file and load the .obj file into Slicer. Texture coordinates seems to be stored in a more standardized way in .obj files and VTK can find it there. If it is important for you to load .ply files directly then it should be possible to fix it quite easily.</p>

---

## Post #9 by @tsehrhardt (2018-04-08 14:01 UTC)

<p>Does the texture need to be an overlay? If you import the file into Meshlab, you can apply the filter: Transfer texture to vertex color, then transfer the vertex color to face color and export as a new ply mesh with only face color. Then open in 3D Slicer, go to Models and check the “Scalars Visible” box, select RGB from the dropdown and it will load. I also got it to work with an obj as long as the color is “face color.” For some reason, it would not read the color correctly if it was saved in the vertex.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/934b46e845ce5f451309b5525543b97f3b18e18b.jpeg" data-download-href="/uploads/short-url/l11t2jQgOPwo24sbEXNkQsP6FGX.jpg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/934b46e845ce5f451309b5525543b97f3b18e18b_2_665x500.jpg" alt="Screenshot" data-base62-sha1="l11t2jQgOPwo24sbEXNkQsP6FGX" width="665" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/934b46e845ce5f451309b5525543b97f3b18e18b_2_665x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/934b46e845ce5f451309b5525543b97f3b18e18b_2_997x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/934b46e845ce5f451309b5525543b97f3b18e18b.jpeg 2x" data-dominant-color="9A92A9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1196×898 250 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @stevenagl12 (2022-01-21 18:00 UTC)

<p>How can we generate texture that is in RGB values that are next to the vertices in an OBJ file?</p>

---

## Post #11 by @stevenagl12 (2022-01-22 13:43 UTC)

<p>What I mean by that is, I have OBJ files that have RGB values for texture already in the file. How can I load this into the scene?</p>

---

## Post #12 by @pieper (2022-01-22 16:32 UTC)

<p>We don’t support textured models natively, but you can write a script to do it.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#add-a-texture-mapped-plane-to-the-scene-as-a-model" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#add-a-texture-mapped-plane-to-the-scene-as-a-model</a></p>

---

## Post #13 by @lassoan (2022-01-24 21:16 UTC)

<p>If someone does not want to copy-paste scripts then the “Texture model” module in SlicerIGT extension can be used for this:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="PeyfyCs2tJg" data-video-title="Importing of color surface scans into 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=PeyfyCs2tJg" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/PeyfyCs2tJg/hqdefault.jpg" title="Importing of color surface scans into 3D Slicer" width="" height="">
  </a>
</div>

<p>The module even has the option of assigning texture values to each mesh point, just in case you want to perform mesh processing based on texture values or want to save the textured model into a single vtk or ply file. The texture image can contain more details than what can be reconstructed from point data, so the point-sample-based color representation is not a complete replacement of texture mapping.</p>

---

## Post #14 by @stevenagl12 (2022-01-25 12:54 UTC)

<p>I am confused with how you imported the file as a volume, unless this was already a separate file to begin with that contained only the RGB values. How do you separate the RGB values from the OBJ file?</p>

---

## Post #15 by @lassoan (2022-01-25 13:50 UTC)

<p>The texture image (png file) was loaded as usual, using “Add data”.</p>
<p>The user experience could be improved by automatically loading associated texture files; and by saving in the scene the information that a texture is associated with a model (currently, the association between the model and texture image is not stored persistently in the scene).</p>

---

## Post #16 by @stevenagl12 (2022-01-25 19:09 UTC)

<p>Ah, so this goes back to my original question then. I do not have a PNG file for the texture, but rather I have a OBJ file with both the vertices and texture values (similar to the way you said you can save OBJ files with these), and faces.</p>

---

## Post #17 by @lassoan (2022-01-25 19:31 UTC)

<p>An OBJ file cannot store per-vertex color, just texture coordinates (see <a href="https://en.wikipedia.org/wiki/Wavefront_.obj_file">specification</a>). The color is determined by mapping portions of the texture image (specified by the texture coordinates) on the rendered surface.</p>
<p>If you don’t have the texture image then you won’t have colors (other than the uniform colors that are defined in the material file).</p>
<p>There might be non-standard variations of file formats, so if you are sure that you have per-vertex color information in your OBJ files then you can upload an example somewhere and post the link here so that we can have a look.</p>

---

## Post #18 by @stevenagl12 (2022-01-25 21:52 UTC)

<p>So, I can’t share the OBJ file itself because of HIPAA laws, but I can show you what I mean:</p>
<p>o Object.1<br>
v 9.140000 73.727997 416.315002 43 21 15<br>
v 1.630000 59.623001 408.157990 87 4 0<br>
v -2.048000 65.589996 382.217987 88 28 4<br>
v -2.800000 72.429001 408.101013 105 23 0<br>
v 12.335000 73.512001 408.225006 18 0 0<br>
v -1.555000 65.552002 382.286987 84 21 0<br>
v -1.957000 65.717003 382.250000 76 28 15<br>
v -1.655000 65.588997 382.240997 75 28 16<br>
v 5.374000 74.228996 408.181000 73 0 0<br>
v -1.758000 65.700996 382.296997 72 27 15<br>
v -1.955000 65.455002 382.290009 90 19 0<br>
v 9.362000 73.671997 416.255005 36 14 9<br>
v -1.623000 65.397003 382.309998 138 10 0<br>
v -1.926000 65.624001 382.136993 76 28 15<br>
v -2.633000 72.100998 407.997009 65 12 5<br>
v -1.557000 65.433998 382.281006 52 21 8<br>
v -1.742000 65.462997 382.190002 90 30 7<br>
v -1.749000 65.598999 382.195007 75 28 16<br>
v -2.008000 65.794998 382.437988 77 23 7<br>
v -1.943000 65.788002 382.437012 85 12 0<br>
v -1.846000 65.775002 382.441986 85 12 0<br>
v -2.010000 65.475998 382.471985 85 23 0<br>
v 8.897000 73.684998 416.281006 50 19 6<br>
v 9.296000 73.656998 416.371002 36 14 9<br>
v -0.800000 58.567001 408.160004 47 29 0<br>
v 15.982000 66.615997 408.125000 45 1 0<br>
v -2.085000 65.720001 382.446014 77 23 7<br>
v -1.710000 65.752998 382.471008 82 14 0<br>
v 4.327000 58.469002 408.197998 73 25 0<br>
v -1.419000 65.384003 382.468994 52 21 8<br>
v 7.911000 60.262001 408.196991 42 0 0<br>
v 6.899000 59.730000 408.048004 1 0 0<br>
v 6.653000 59.680000 408.141998 18 0 0<br>
v -4.153000 56.791000 408.169006 43 0 0<br>
v -1.371000 65.426003 382.481995 53 25 16<br>
v 14.071000 60.319000 408.161987 62 8 0<br>
v -1.426000 65.517998 382.416992 74 22 0<br>
v 9.142000 73.612000 416.453003 53 21 0<br>
v -1.588000 65.345001 382.425995 138 10 0<br>
v -1.496000 65.623001 382.450012 74 22 0</p>

---

## Post #19 by @lassoan (2022-01-26 19:46 UTC)

<p>Thanks, this snippet was useful. While vertex color cannot be stored in standard OBJ files, it seems that there is a <a href="http://www.paulbourke.net/dataformats/obj/colour.html">workaround</a> that is used in your file, too. VTK does not support this workaround, but probably you can find other software that does.</p>
<p>Therefore, I would recommend load the non-standard OBJ file using a software that supports per-vertex colors (you can try MeshLab) then save it into a standard PLY file (that supports per-vertex coloring). If you save the vertex colors in <code>uchar</code> type properties with the names <code>red</code>, <code>green</code>, and <code>blue</code> then Slicer will load the vertex colors.</p>

---

## Post #20 by @stevenagl12 (2022-01-27 16:14 UTC)

<p>ok thank you. Is there any chance that this might be something done in the future? I am collaborating with some people who would very much appreciate it, but I don’t want to get their hopes up.</p>

---

## Post #21 by @lassoan (2022-01-27 16:21 UTC)

<p>Where does the data come from? Can they save the surface in PLY format when they acquire it?</p>
<p>Adding vertex color loading to VTK OBJ reader would be quite straightforward, probably less than one week for a developer who knows VTK. But you either need to wait until a funded project needs this feature, hire someone to do it or do it yourself.</p>
<p>You could also try converting the OBJ to PLY using meshio or similar Python packages, if converting using MeshLab is too complicated or takes too much time.</p>

---

## Post #22 by @stevenagl12 (2022-01-27 16:24 UTC)

<p>Let me try to working with them to see if there system will allow that save option, and we shall see. If necessary I can try to work on it myself, but I have a fair amount on my plate as well so this will need to wait. I was moreso curious if anyone else has had these problems.</p>

---
