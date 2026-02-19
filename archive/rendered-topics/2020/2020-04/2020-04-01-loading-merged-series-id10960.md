---
topic_id: 10960
title: "Loading Merged Series"
date: 2020-04-01
url: https://discourse.slicer.org/t/10960
---

# Loading merged series

**Topic ID**: 10960
**Date**: 2020-04-01
**URL**: https://discourse.slicer.org/t/loading-merged-series/10960

---

## Post #1 by @JanWitowski (2020-04-01 16:07 UTC)

<p>Hello,</p>
<p>I’m trying to load merged series DICOM images, i.e. arterial and venous phase are saved as the same Series ID and thus read by 3D Slicer as a single serie. It’s being loaded layer by layer from each acquisition:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a4fbe39ec2e2ee0267e5994b6c5b30ebfcefa75.jpeg" data-download-href="/uploads/short-url/hs16cVujFe46l9VoQqXqYhw7uq9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a4fbe39ec2e2ee0267e5994b6c5b30ebfcefa75_2_690x201.jpeg" alt="image" data-base62-sha1="hs16cVujFe46l9VoQqXqYhw7uq9" width="690" height="201" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a4fbe39ec2e2ee0267e5994b6c5b30ebfcefa75_2_690x201.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a4fbe39ec2e2ee0267e5994b6c5b30ebfcefa75.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a4fbe39ec2e2ee0267e5994b6c5b30ebfcefa75.jpeg 2x" data-dominant-color="5D5D5D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">888×259 49.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>At loading, I get the error message:</p>
<blockquote>
<p>2: Unnamed Series [Scalar Volume]: Images are not equally spaced (a difference of -2.5 vs 5 in spacings was detected).  If loaded image appears distorted, enable ‘Acquisition geometry regularization’ in Application settings / DICOM / DICOMScalarVolumePlugin. Please use caution.</p>
</blockquote>
<p>I tried loading from both DICOM Browser and drag&amp;drop files and enabling “Allow loading subseries by time”, unfortunately with no luck.</p>
<p>This is an anonymized serie I’m having trouble loading: <a href="https://we.tl/t-1qA1eZznEF" class="inline-onebox" rel="noopener nofollow ugc">WeTransfer - Send Large Files &amp; Share Photos Online - Up to 2GB Free</a></p>
<p>Is there a way to load this as two separate series? If not, maybe you have any clues on how to process it based on some DICOM headers?</p>
<p>Thanks for your help!</p>

---

## Post #2 by @lassoan (2020-04-01 19:53 UTC)

<p>All acquisitions are lumped into a single image series. Acquisition Number tag can be used to split them but it was not added to the list of supported subseries tags in DICOM scalar volume importer.</p>
<p>I’ve submitted a <a href="https://github.com/Slicer/Slicer/pull/4801">pull request</a> that adds this tag. It works well, it allows loading this series as two separate volumes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcab32e610921f80cb86b0506ad1355f4a3ba965.gif" data-download-href="/uploads/short-url/A3d75wnMWJkNg6uKYIDaKb4EcW9.gif?dl=1" title="SlicerCapture"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fcab32e610921f80cb86b0506ad1355f4a3ba965_2_397x500.gif" alt="SlicerCapture" data-base62-sha1="A3d75wnMWJkNg6uKYIDaKb4EcW9" width="397" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fcab32e610921f80cb86b0506ad1355f4a3ba965_2_397x500.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcab32e610921f80cb86b0506ad1355f4a3ba965.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcab32e610921f80cb86b0506ad1355f4a3ba965.gif 2x" data-dominant-color="3C3C3C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerCapture</span><span class="informations">466×586 250 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @JanWitowski (2020-04-01 20:16 UTC)

<p>Thank you so much! I will be watching for the update in next builds</p>

---
