# Why I can't set my own transform matrix while using VolumeReconstructor?

**Topic ID**: 21244
**Date**: 2021-12-28
**URL**: https://discourse.slicer.org/t/why-i-cant-set-my-own-transform-matrix-while-using-volumereconstructor/21244

---

## Post #1 by @Junshi_Peng (2021-12-28 06:27 UTC)

<p>In my tracking case, I’ve only appied one set of tracker on ultrasound probe, and I would like to reconstruct the volume from the input ultrasound image set and the corresponding transforms data of the moving probe.</p>
<p>In this way, before using VolumeReconstructor by the command line, I should set the config xml file accordingly. But when I tried to adjust the transform matrix in the xml file into identity matrix, the volume reconstruction process failed and  didn’t return anything.</p>
<p>But according to my case, I didn’t applied any phantom trackers, and I just need the ultrasound volume, so I don’t need to consider about the transform between probe tracker and image neither. In this way, I do need to set these two matrixs into 1.</p>
<p>But why this can make the VolumeReconstructor go wrong?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1ebfbf779ddfaef281a4fad86de9dfe6716ea06.png" data-download-href="/uploads/short-url/yw8FbxcgWUl8iA8Fh6c00DZSfDo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1ebfbf779ddfaef281a4fad86de9dfe6716ea06.png" alt="image" data-base62-sha1="yw8FbxcgWUl8iA8Fh6c00DZSfDo" width="503" height="499" data-dominant-color="242527"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">812×807 20.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ungi (2021-12-29 17:45 UTC)

<p>Hi, it seems like you are trying to use PLUS, not 3D Slicer, right? In that case you are on the wrong website. But since you are here already, let me suggest just streaming tracked images from PLUS to 3D Slicer, and do volume reconstruction in 3D Slicer. So you would not need the VolumeReconstruction part in your PLUS config file. But you would need to add a PlusOpenIGTLinkServer part. Slicer has all kinds of visualization options for you to check what might be wrong with the data before or after volume reconstruction.</p>
<p>Here are a few videos using volume reconstruction in Slicer, so you see how it should work if you set it up correctly:</p><div class="youtube-onebox lazy-video-container" data-video-id="2vXeJxYFou4" data-video-title="Real-time 3D ultrasound reconstruction using 3D Slicer + SlicerIGT" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=2vXeJxYFou4" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/2vXeJxYFou4/maxresdefault.jpg" title="Real-time 3D ultrasound reconstruction using 3D Slicer + SlicerIGT" width="" height="">
  </a>
</div>
<div class="youtube-onebox lazy-video-container" data-video-id="l0BcW8c9CnI" data-video-title="Tracked ultrasound AI segmentation and 3D reconstruction tutorial" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=l0BcW8c9CnI" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/l0BcW8c9CnI/maxresdefault.jpg" title="Tracked ultrasound AI segmentation and 3D reconstruction tutorial" width="" height="">
  </a>
</div>
<div class="youtube-onebox lazy-video-container" data-video-id="WyscpAee3vw" data-video-title="Real-time ultrasound AI segmentation and volume reconstruction" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=WyscpAee3vw" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/WyscpAee3vw/maxresdefault.jpg" title="Real-time ultrasound AI segmentation and volume reconstruction" width="" height="">
  </a>
</div>


---
