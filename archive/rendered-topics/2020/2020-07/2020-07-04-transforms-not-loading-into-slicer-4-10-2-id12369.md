# Transforms not loading into Slicer 4.10.2

**Topic ID**: 12369
**Date**: 2020-07-04
**URL**: https://discourse.slicer.org/t/transforms-not-loading-into-slicer-4-10-2/12369

---

## Post #1 by @Vinny (2020-07-04 00:51 UTC)

<p>Hi,</p>
<p>I’ve generated acpc transforms in 4.11.0-2020-06-06 that are not loading into the stable Slicer release 4.10.2.  The data module is empty and does not display the transform.</p>
<p>Any help would be appreciated.</p>
<p>Thanks,</p>
<p>Vinny</p>

---

## Post #2 by @lassoan (2020-07-04 01:34 UTC)

<p>Can you upload the transform file somewhere and post the link here?</p>

---

## Post #3 by @Vinny (2020-07-04 02:32 UTC)

<p>Hi Andras,</p>
<p>Here’s the link… <a href="https://github.com/vinkirk/public/raw/master/Xfm_acpc.h5" rel="nofollow noopener">https://github.com/vinkirk/public/raw/master/Xfm_acpc.h5</a></p>
<p>Thanks,</p>
<p>Vinny</p>

---

## Post #4 by @lassoan (2020-07-04 03:14 UTC)

<p>Thank you, I could reproduce the problem. It seems that ITK 5 .h5 transform file format is not backward compatible with ITK 4. I’ve <a href="https://discourse.itk.org/t/itk4-cannot-read-itk5-h5-transform-files/3264">asked on the ITK forum about why is this</a>.</p>
<p>In the meantime, if you need to save transforms in an ITK 4 compatible format, I would recommend to use a different format, such as tfm.</p>

---

## Post #5 by @Vinny (2020-07-04 13:05 UTC)

<p>Great thanks Andras.</p>

---
