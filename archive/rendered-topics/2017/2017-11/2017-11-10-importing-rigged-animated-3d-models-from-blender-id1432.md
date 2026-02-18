# Importing rigged/animated 3D models from Blender

**Topic ID**: 1432
**Date**: 2017-11-10
**URL**: https://discourse.slicer.org/t/importing-rigged-animated-3d-models-from-blender/1432

---

## Post #1 by @jdx-john (2017-11-10 15:14 UTC)

<ol>
<li>I know Slicer has some built-in support to load static polygon meshes, where is it documented what formats? I think I saw mention of STL and OBJ so far</li>
<li>We have a medical device being modelled, with animations, in Blender. As I understand, multiple poses of a skeletally-rigged model. We’ve come across some VTK support from skinned animations (<a href="https://www.vtk.org/doc/nightly/html/classvtkWeightedTransformFilter.html" rel="nofollow noopener">https://www.vtk.org/doc/nightly/html/classvtkWeightedTransformFilter.html</a> seems most likely) but I don’t know what capabilities Slicer has to actually load from this file… writing a bespoke loader would be a pain. Does Slicer support any standard file formats such as FBX?</li>
</ol>

---

## Post #2 by @jcfr (2017-11-10 15:36 UTC)

<aside class="quote no-group" data-username="jdx-john" data-post="1" data-topic="1432">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a6a055/48.png" class="avatar"> jdx-john:</div>
<blockquote>
<p>where is it documented what formats? I think I saw mention of STL and OBJ so far</p>
</blockquote>
</aside>
<p><a href="https://www.slicer.org/wiki">Slicer Wiki</a> → User Manual → <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/SupportedDataFormat">Supported Data Formats</a></p>
<aside class="quote no-group quote-modified" data-username="jdx-john" data-post="1" data-topic="1432">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a6a055/48.png" class="avatar"> jdx-john:</div>
<blockquote>
<p>We have a medical device being modelled, with animations, in Blender. As I understand, multiple poses of a skeletally-rigged model. We’ve come across some VTK support from skinned animations (<a href="https://www.vtk.org/doc/nightly/html/classvtkWeightedTransformFilter.html" class="inline-onebox">VTK: vtkWeightedTransformFilter Class Reference</a> seems most likely) but I don’t know what capabilities Slicer has to actually load from this file…</p>
</blockquote>
</aside>
<p>That makes me think of <a href="https://public.kitware.com/Wiki/Bender" class="inline-onebox">Bender - KitwarePublic</a> a Slicer based project for repositioning voxelized anatomical models.</p>
<p>Note that it is named <strong>Bender</strong> and not <strong>Blender</strong></p>
<p>It applies the rigging, skinning and posing technique to volumes by providing an additional step to resample the volume. It internally uses Cleaver and SOFA.</p>
<aside class="quote no-group" data-username="jdx-john" data-post="1" data-topic="1432">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a6a055/48.png" class="avatar"> jdx-john:</div>
<blockquote>
<p>Does Slicer support any standard file formats such as FBX?</p>
</blockquote>
</aside>
<p>Part of the Bender project could probably be turn into a Slicer extension.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> What do you think ?</p>

---

## Post #3 by @lassoan (2017-11-11 15:22 UTC)

<p>Yes, I think it would be a good idea to port Bender to an extension.</p>

---

## Post #4 by @jdx-john (2017-11-13 13:19 UTC)

<p>Thanks for the replies.</p>
<p>If you’re suggesting we actually use Bender instead of Blender for creating<br>
the animations I don’t <em>think</em> this would work. We are working from<br>
supplied polygonal models I think (although it might be solidworks) and I<br>
think need to use industry-standard tools like Blender/3DSMax for modelling<br>
and rigging/animating.</p>

---

## Post #5 by @lassoan (2017-11-13 16:17 UTC)

<p>Bender = special build of Slicer with additional modules for animation and physically realistic simulation of tissue deformations.</p>
<p>Bender includes readers for BVH motion capture files and armature files. The armature file format seems to be some VTK-based format, so it would need to be modified to be able to read some other format that Blender/3DSMax can export.</p>
<p>See a couple of videos about what it can do:</p>
<ul>
<li><a href="https://vimeo.com/73247670">https://vimeo.com/73247670</a></li>
<li><a href="https://vimeo.com/63601648">https://vimeo.com/63601648</a></li>
<li><a href="https://vimeo.com/63601647">https://vimeo.com/63601647</a></li>
</ul>
<p>While you can do basic rigging and animation in Slicer (Bender), for more sophisticated animations it is probably better to work in Blender or other professional modeler software, export results to files, and import those into Slicer.</p>

---

## Post #6 by @lassoan (2017-11-13 17:08 UTC)

<p>There is also an <a href="https://public.kitware.com/gitweb?p=Bender/Bender.git;a=blob;f=Utilities/Blender/io_export_armature.py;h=f814440c1ad86f34b0efa4b91cc88d4db7b7327b;hb=HEAD">armature exporter Blender plugin</a> in Bender utilities. I think Blender can export motion capture data as .bvh and models as stl or obj. So, I think these may cover all data export/import needs.</p>

---

## Post #7 by @jdx-john (2017-11-13 19:23 UTC)

<p>I’m unsure… It appears Mo-Cap is exported via BVH but as I understand it,<br>
STL/OBJ only store raw polygon data. Isn’t there a 3rd piece missing, the<br>
actual rigging (armature as you describe it?)</p>

---

## Post #8 by @Johan_Andruejol (2017-11-13 20:08 UTC)

<p>Hey John,</p>
<p>Bender is able to directly read BVH files, so you can import the rigging<br>
(armature) with its pose.</p>
<p>When importing a BVH in Bender, you can choose the frame of the animation<br>
(as demonstrated in this video: <a href="https://vimeo.com/90788904#t=1m20s" rel="nofollow noopener">https://vimeo.com/90788904#t=1m20s</a>)<br>
or you can manually adjust it from within the Armature module in the<br>
armature pose panel (see the documentation here<br>
<a href="https://public.kitware.com/Wiki/Bender/Documentation/2.0/Modules/Armatures" rel="nofollow noopener">https://public.kitware.com/Wiki/Bender/Documentation/2.0/Modules/Armatures</a>)</p>
<p>You can also create (rig) and pose the armature directly from Bender.</p>
<p>Thanks !<br>
Johan</p>

---

## Post #9 by @jdx-john (2017-11-13 20:55 UTC)

<p>Hi, I’ve maybe misunderstood what data is stored in the BVH file? So not<br>
just the raw motion of points, but the rigging/weighting as well?<br>
We don’t have mo-cap data, can we use BVH as a generic transport for this<br>
sort of data?</p>
<p>And then - how do I get this into Slicer rather than Bender?<br>
I can’t use Bender for the rigging because we want to use the same models<br>
in realtime 3D engines, etc, and these really need to use more standard<br>
formats like PBX… plus our artists will want to stay with familiar tools.</p>
<p>Many thanks.</p>

---

## Post #10 by @lassoan (2017-11-13 21:33 UTC)

<p>I’ve checked and .bvh has both armature and motion capture data. Blender has a .bvh exporter, so I guess if you can import something to Blender then you can export it as .bvh and then Bender (=Slicer+extra modules) can use it for creating animations.</p>
<p><a class="mention" href="/u/johan_andruejol">@Johan_Andruejol</a> <a class="mention" href="/u/finetjul">@finetjul</a> Can you confirm?</p>

---

## Post #11 by @Johan_Andruejol (2017-11-14 00:08 UTC)

<p>Yes, BVH has both the rig and the animation information.)<br>
Also, I seem to recall Blender having support for exporting under the BVH<br>
format.</p>
<p>However, BVH import does NOT contain the weight information. You will have<br>
to supply/create that yourself.<br>
Since Bender is aimed toward posing/animating labelmaps,we need a weight<br>
map that is also a labelmap.<br>
That weight map can be created using a few modules:</p>
<ul>
<li>
<p>The Volume Skinning module create a 1-to-1direct mapping between a bone<br>
and a voxel. This is a very simple skinning. See<br>
<a href="https://public.kitware.com/Wiki/Bender/Documentation/2.0/Modules/VolumeSkinning" rel="nofollow noopener">https://public.kitware.com/Wiki/Bender/Documentation/2.0/Modules/VolumeSkinning</a><br>
.</p>
</li>
<li>
<p>This simple skinning can be edited using any labelmap editor. I would<br>
advise using the Segment Editor in Slicer<br>
<a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html" rel="nofollow noopener">http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a>,<br>
though Bender still uses the old Editor<br>
<a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/Editor" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.8/Modules/Editor</a></p>
</li>
</ul>
<p>-This 1-to-1 map can further refined to obtain smooth transition with the<br>
Compute Armature Weight module:<br>
<a href="https://public.kitware.com/Wiki/Bender/Documentation/2.0/Modules/ComputeArmatureWeight" class="onebox" target="_blank" rel="nofollow noopener">https://public.kitware.com/Wiki/Bender/Documentation/2.0/Modules/ComputeArmatureWeight</a></p>
<p>In any case, I encourage you to download Bender and try it yourself, it’s<br>
free <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
Bender’s Workflow module takes you through all the steps needed to create,<br>
rig and pose a labelmap. This should give you a better idea of what it can<br>
do.</p>
<p>I hope this helps,<br>
Johan</p>

---

## Post #12 by @jdx-john (2017-11-14 11:57 UTC)

<p>Thanks Johan. Since we’re talking about animating a 3D model rather than<br>
medical dataset, not being able to import the weightings sounds like a<br>
problem to me. That’s surely one of the key things an animator/modeller<br>
would do, making them do it twice seems a bad idea.</p>
<p>I think I’ll ask the animator to peruse this thread in case we’re talking<br>
at cross-purposes, though I think the terminology might be slightly<br>
different anyhow.</p>

---
