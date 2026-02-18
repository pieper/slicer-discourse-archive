# 3D volume appears distorted - jaw looks elongated

**Topic ID**: 9072
**Date**: 2019-11-07
**URL**: https://discourse.slicer.org/t/3d-volume-appears-distorted-jaw-looks-elongated/9072

---

## Post #1 by @talalzahid (2019-11-07 20:36 UTC)

<p>Hi,</p>
<p>I am trying to convert the dental CBCT scan into a 3d model to be printed. however when I do that the end result does not look realistic and the jaw looks elongated and the compressed.</p>
<p>I have uploaded a picture for the result <a href="https://imgur.com/a/NlA2vUm" rel="nofollow noopener">https://imgur.com/a/NlA2vUm</a></p>
<p>When I upload the cbct it show a warning " multi-frame image. If slice orientation or spacing is non-uniform, then the image may be displayed incorrectly" however, I do not think this is possible. Is there is a way to fix this?</p>
<p>I have the Dicom files uploaded if anyone is interested in checking it.</p>
<p>Thank you in advance</p>

---

## Post #2 by @lassoan (2019-11-07 20:38 UTC)

<p>Most likely you have run into a known problem with Dolphin CBCT scanners. See the solution here: <a href="https://discourse.slicer.org/t/dvt-import-with-wrong-dimensions/4284/4" class="inline-onebox">DVT import with wrong dimensions</a></p>

---

## Post #3 by @talalzahid (2019-11-11 22:42 UTC)

<p>Thank you so much worked like a charm.</p>
<p>I encountered another problem when I try to using dicom files from medical ct scans. The render is not smooth and look like layers as seen in the picture on the following link</p>
<p>            </p><div class="onebox imgur-album">
              <a href="https://imgur.com/a/I4INAgM" target="_blank" rel="nofollow noopener">
                <span class="outer-box" style="width:600px">
                  <span class="inner-box">
                    <span class="album-title">[Album] Imgur</span>
                  </span>
                </span>
                <img src="https://i.imgur.com/KljyAY5.jpg?fb" title="Imgur" height="315" width="600">
              </a>
            </div>

<p>any idea ?</p>
<p>Thank you in advance</p>

---

## Post #4 by @lassoan (2019-11-12 00:31 UTC)

<p>It seems that the volume has spacing between slices that is about 10x larger than pixel spacing within a slice. Use <code>Crop Volume</code> module to resample the volume with isotropic voxel size by checking  <code>Isotropic spacing</code>  checkbox and selecting  <code>B-spline</code> interpolation. After this segment the cropped/resample volume using Segment Editor module.</p>

---
