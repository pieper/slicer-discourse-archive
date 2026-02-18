# Metal artefact reduction on CT

**Topic ID**: 12731
**Date**: 2020-07-25
**URL**: https://discourse.slicer.org/t/metal-artefact-reduction-on-ct/12731

---

## Post #1 by @kt297 (2020-07-25 20:29 UTC)

<p>Hi,</p>
<p>I am trying to segment bone with a metal prosthesis. Is there a plugin that will do this and remove the metal at the same time as segmenting the bone?</p>

---

## Post #2 by @timeanddoctor (2020-07-26 03:07 UTC)

<p>you can use the segment editor to deal with it.</p>

---

## Post #3 by @kt297 (2020-07-26 09:04 UTC)

<p>Thanks,</p>
<p>Is there a tutorial on how to do this?</p>

---

## Post #4 by @timeanddoctor (2020-07-26 10:43 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Segmentation_for_3D_printing" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Training#Segmentation_for_3D_printing</a></p>

---

## Post #5 by @lassoan (2020-07-26 15:32 UTC)

<p>I agree that for Segment Editor is a good tool for <strong>manual</strong> removal of metal artefacts. You can find some more background information and detailed description of segmentation related modules and links to tutorials here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html</a></p>
<p>In Segment Editor, you can get initial segmentation using Threshold effect (that creates a segment that contains what you need and as small artifact as possible), apply a little Smoothing to make 3D reconstruction faster, enable “Show 3D” and use Scissors tool to cut off artefacts, then apply Smoothing to make the cut surfaces smoother.</p>
<p><a class="mention" href="/u/timeanddoctor">@timeanddoctor</a> do you have a workflow that you find that usually works well for you?</p>
<p>For <strong>automatic</strong> removal/reduction of artefacts the most effective tools are implemented in the CT scanner and workstation, as they require special image acquisition protocols and 3D reconstruction techniques. If the image is already reconstructed into a 3D volume then there is no generally applicable artefact removal method, but you can still develop techniques that work for certain kind of images. If you post a few screenshots then we might be able to give more specific advice.</p>

---

## Post #6 by @philippe (2022-06-17 09:33 UTC)

<p>hello,</p>
<p>I came around this old post searching for a way to do it in slicer.<br>
Depending on your image, you can try wxdicom:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://mi.eng.cam.ac.uk/Main/GMT_wxDicom">
  <header class="source">
      <img src="https://mi.eng.cam.ac.uk/foswiki/pub/System/ProjectLogos/cuedfavicon.ico" class="site-icon" width="" height="">

      <a href="https://mi.eng.cam.ac.uk/Main/GMT_wxDicom" target="_blank" rel="noopener nofollow ugc">mi.eng.cam.ac.uk</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://mi.eng.cam.ac.uk/Main/GMT_wxDicom" target="_blank" rel="noopener nofollow ugc">Machine Intelligence Laboratory</a></h3>

  <p>The Machine Intelligence Laboratory is part of the Information Engineering Division of the Department of Engineering, University of Cambridge, UK.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It has filters specifically targetting metal artefacts. It may be better than a direct segmentation (the metal stays there but the radial artefacts are largely removed).<br>
It looks like these filters are not implemented in slicer tough ??</p>
<p>Thanks<br>
Philippe</p>

---

## Post #7 by @pieper (2022-06-17 12:01 UTC)

<p>The wxDicom filters look nice, but it’s not clear if the source code is available and if so what license it is released under.  You could experiment with the executables and if it’s promising you may want to contact the author.</p>

---

## Post #8 by @philippe (2022-06-20 06:33 UTC)

<p>Hello,</p>
<p>I don’t know about the source code either but I guess it is published algorithms.<br>
On the trials we did, it seemed to work pretty well.</p>
<p>However, the post was mainly to provide information to people that would look for the same info (what is out there, in slicer or not) and possibly trigger an updated reaction. I have no urgent need to have it implemented in slicer (it is fine for us to use it as wxdicom).</p>
<p>Thanks<br>
Philippe</p>

---
