# My Plug-in load failed

**Topic ID**: 1110
**Date**: 2017-09-24
**URL**: https://discourse.slicer.org/t/my-plug-in-load-failed/1110

---

## Post #1 by @francis (2017-09-24 15:03 UTC)

<p>Hello everyone,I have completed my own plug-in named breastImage,and compiled the package regarding to release version,but it dose not work.its solution is based on S4R(slicer 4.5.0-1).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f27d72d950f45711657b49bde97a76cb2086148.png" data-download-href="/uploads/short-url/90HrbYFqQSJ5YoXfaiptVrEA4He.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f27d72d950f45711657b49bde97a76cb2086148_2_690x33.png" alt="image" data-base62-sha1="90HrbYFqQSJ5YoXfaiptVrEA4He" width="690" height="33" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f27d72d950f45711657b49bde97a76cb2086148_2_690x33.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f27d72d950f45711657b49bde97a76cb2086148_2_1035x49.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f27d72d950f45711657b49bde97a76cb2086148_2_1380x66.png 2x" data-dominant-color="F5F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1671×80 9.59 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/880295c4cc629ff24f3a5519bec8e2b6bd3ffafe.png" alt="image" data-base62-sha1="jpctpyHQpOr2p4t44EPmKU7BW5o" width="415" height="18"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f436c43270030b269ca222f7129d795112e3a6a.png" data-download-href="/uploads/short-url/krmJkCptYlYDSdrwSTMsz9dz1cC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f436c43270030b269ca222f7129d795112e3a6a.png" alt="image" data-base62-sha1="krmJkCptYlYDSdrwSTMsz9dz1cC" width="690" height="22" data-dominant-color="8AA8C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1199×39 1.21 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I have also compiled the package regarding to debug version,and it work well.its solution is based on S4D(slicer 4.5.0-1).<br>
I need your help,how can i solve this problem?</p>

---

## Post #2 by @pieper (2017-09-24 15:19 UTC)

<p>To develop your own c++ modules you need to have compiled Slicer locally.  We suggest using the current git master branch.</p>
<p>The information here should help:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Module" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Module</a></p>

---
