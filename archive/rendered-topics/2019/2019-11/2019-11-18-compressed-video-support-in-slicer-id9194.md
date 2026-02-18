# Compressed video support in Slicer

**Topic ID**: 9194
**Date**: 2019-11-18
**URL**: https://discourse.slicer.org/t/compressed-video-support-in-slicer/9194

---

## Post #1 by @Sunderlandkyl (2019-11-18 15:57 UTC)

<p>Compressed video support for 3D Slicer is available in both the 4.10.2 and 4.11.0 releases.</p>
<div class="lazyYT" data-youtube-id="V0Oqk7DjQp4" data-youtube-title="Compressed video transfer in Plus" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>For users:</p>
<ul>
<li>Requires Sequences, SlicerOpenIGTLink and SlicerIGSIO extensions</li>
<li>Video recording and playback</li>
<li>Save and load MKV files encoded with VP9</li>
<li>Stream compressed video through OpenIGTLink</li>
<li>Storage space for 60 sec, 10 fps, 640x480 video:
<ul>
<li>Before: ~222.6 MB, 30s</li>
<li>Now: ~37.1 MB, &lt;1s</li>
</ul>
</li>
<li>Video sequences can be re-encoded with different settings/compression levels</li>
</ul>
<p>For developers:</p>
<ul>
<li>Compressed video frames are stored using vtkMRMLStreamingVolumeNode, which handles decoding and encoding of video frames.</li>
<li>Frame data is represented using vtkStreamingVolumeFrame, which contains frame metadata, as well as  pointer to the previous frame in the decoding sequence.</li>
<li>New codecs can be added to Slicer by subclassing vtkStreamingVolumeCodec and registering  it with vtkStreamingVolumeCodecFactory.</li>
<li>Documentation for compressed video is here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/CompressedVideo" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/CompressedVideo</a>
</li>
</ul>
<p>Suggestions and feedback are welcome.</p>
<p>This work was made possible through collaboration with Longquan Chen and Harvard SNRL.<br>
Development was funded in part by CANARIE’s Research Software Program.</p>

---
