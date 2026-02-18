# Tractography in PLY with colors to OBJ with material (MTL) conversion

**Topic ID**: 9438
**Date**: 2019-12-08
**URL**: https://discourse.slicer.org/t/tractography-in-ply-with-colors-to-obj-with-material-mtl-conversion/9438

---

## Post #1 by @Gonzalo_Rojas_Costa (2019-12-08 22:00 UTC)

<p>How can I convert tractography saved in a PLY file with colors to a OBJ/MTL file ?</p>

---

## Post #2 by @lassoan (2019-12-09 04:22 UTC)

<p>MeshLab can bake textures from point scalars, so if you need a one-off conversion then that may be the simplest. You can find instructions on the web, see for example <a href="http://www.danielgm.net/cc/forum/viewtopic.php?t=830">here</a>.</p>
<p>If you need to do this often or this is part of a time-constrained workflow then probably you can write a script that uses VTK filters to create texture coordinates and fill the texture image with colors taken from the PLY mesh.</p>
<p>Why do you need the colored model as OBJ/MTL file? For 3D printing?</p>
<p>If you have access to a suitable multimaterial Stratasys printer, then you may try voxel printing with <a href="https://github.com/SlicerFab/SlicerFab">SlicerFab</a> extension. Voxel printing is not as widely available as standard colored surface printing but it is so much nicer. See for example how fiber tracts look with this technique:</p>
<p>                    <a href="https://scx1.b-cdn.net/csz/news/800/2018/makingdatama.jpg" target="_blank" class="onebox" rel="nofollow ugc noopener">
            <img src="https://scx1.b-cdn.net/csz/news/800/2018/makingdatama.jpg" width="690" height="414">
          </a>

</p>
<p>(source: <a href="https://techxplore.com/news/2018-05-multimaterial-voxel-printing-method-imaging-datasets.html">https://techxplore.com/news/2018-05-multimaterial-voxel-printing-method-imaging-datasets.html</a>)</p>

---

## Post #4 by @Gonzalo_Rojas_Costa (2019-12-09 04:40 UTC)

<p>I need the tract (PLY mesh) in OBJ/MTL for a virtual reality software that we are creating…</p>

---

## Post #5 by @lassoan (2019-12-09 04:50 UTC)

<p>FYI, you can <a href="https://github.com/KitwareMedical/SlicerVirtualReality">show Slicer scene in virtual reality</a> with a single button click, on any OpenVR compatible headset. No need to use any third-party software or exporting or converting any data. Moreover, you are not limited to viewing some static set of fiber tracts but you can do dynamic tractography seeding, see for example this multi-user demo:</p>
<div class="lazyYT" data-youtube-id="rG9ST6xv6vg" data-youtube-title="Collaborative surgery planning in virtual reality" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque&amp;start=27"></div>
<p>Instead of redeveloping a limited variant of this feature in a different environment, it would be so much nicer to collaborate on improving the existing implementation in Slicer. Customization and optimization of tractography visualization in virtual reality would be a good project for an upcoming Project week (in Spain in January or in Boston in June), but if you cannot come to these then we are happy to help you remotely/via this forum.</p>

---
