---
topic_id: 36362
title: "I Want To Calculate Mean"
date: 2024-05-24
url: https://discourse.slicer.org/t/36362
---

# I want to calculate mean

**Topic ID**: 36362
**Date**: 2024-05-24
**URL**: https://discourse.slicer.org/t/i-want-to-calculate-mean/36362

---

## Post #1 by @Vikram (2024-05-24 03:41 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4fe7e585418ae9302eebf682cffd0b00785ae40.jpeg" data-download-href="/uploads/short-url/nxBypzaQznmlxntGoiJM8kvbwaY.jpeg?dl=1" title="pet image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4fe7e585418ae9302eebf682cffd0b00785ae40_2_690x373.jpeg" alt="pet image" data-base62-sha1="nxBypzaQznmlxntGoiJM8kvbwaY" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4fe7e585418ae9302eebf682cffd0b00785ae40_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4fe7e585418ae9302eebf682cffd0b00785ae40_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4fe7e585418ae9302eebf682cffd0b00785ae40_2_1380x746.jpeg 2x" data-dominant-color="696868"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pet image</span><span class="informations">1404×760 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
i have pet dicom file of cubic , in this image there is lattice and also air i put FDG and sent for  pet , after pet scan i want to calculate the mean in air and lattice.<br>
any one can guide me how i can calculate the mean from pet image</p>

---

## Post #2 by @cpinter (2024-05-24 08:36 UTC)

<p>Define the air and lattice regions using Segment Editor. Then use the Segment Statistics module to get all kinds of statistics including the mean of the image content under these segments.</p>

---
