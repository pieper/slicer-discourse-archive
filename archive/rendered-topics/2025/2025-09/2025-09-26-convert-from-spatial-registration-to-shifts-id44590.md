---
topic_id: 44590
title: "Convert From Spatial Registration To Shifts"
date: 2025-09-26
url: https://discourse.slicer.org/t/44590
---

# Convert from spatial registration to shifts

**Topic ID**: 44590
**Date**: 2025-09-26
**URL**: https://discourse.slicer.org/t/convert-from-spatial-registration-to-shifts/44590

---

## Post #1 by @G_Tom (2025-09-26 05:12 UTC)

<p>Hello,</p>
<p>This is for the the experts in image registration, particularly CT to CBCT registration to obtain table shifts,</p>
<p>Typically the CBCT is acquired on the day of treatment with the patient on the bed and registered with the planning CT. This registration yields bed shifts (Online Match) that should move the patient to the correct planned position before treatment.</p>
<p>In my planning system software, I register a CT and a CBCT and I get a Dicom Spatial Registration object <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1da5908188076d3410559c2270a7ea38cde48806.png" data-download-href="/uploads/short-url/4egz99EDUEy9Z9wF8weQ7r77zsq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1da5908188076d3410559c2270a7ea38cde48806.png" alt="image" data-base62-sha1="4egz99EDUEy9Z9wF8weQ7r77zsq" width="556" height="437"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">556×437 68.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The planning system also reports the match computed from the Registration above as:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9cc7af38745d56dd52efe6db4676abafd977775.png" data-download-href="/uploads/short-url/oe6MWLF4jKRt8dgHP11bH6KB90p.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9cc7af38745d56dd52efe6db4676abafd977775.png" alt="image" data-base62-sha1="oe6MWLF4jKRt8dgHP11bH6KB90p" width="343" height="174"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">343×174 22.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now, In Slicer, I want to recreate these table shifts. When I export the registration object into slicer the transformation matrix is:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11cb7935fdeba758eb7088823c2278d359fd89d0.png" data-download-href="/uploads/short-url/2xq3wNcGCYBJ3xb6E7z5XsIliQo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11cb7935fdeba758eb7088823c2278d359fd89d0.png" alt="image" data-base62-sha1="2xq3wNcGCYBJ3xb6E7z5XsIliQo" width="437" height="115"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">437×115 1.74 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For anyone who has done this before, how can you compute these Online Match values from the transformation matrix read from the Dicom Registration object ?</p>
<p>Any pointers on how to compute this will be greatly appreciated.</p>
<p>Thanks</p>

---

## Post #2 by @cpinter (2025-09-26 08:58 UTC)

<p>The transformation matrix looks like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ec94a957f80bf0ab88c9f204e65bdd78e615c46.png" data-download-href="/uploads/short-url/dww96PcV206tgME9It7xMCtUlSe.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ec94a957f80bf0ab88c9f204e65bdd78e615c46.png" alt="image" data-base62-sha1="dww96PcV206tgME9It7xMCtUlSe" width="469" height="203"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">469×203 5.96 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The last column of the matrix (excluding the bottom element) gives the translation vector (represents the shift in <strong>X, Y, Z</strong> directions in mm)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca95f06994a532597f9ec3fcde06815acf525e1f.png" alt="image" data-base62-sha1="sU9GUpvslcefiIEcf6DKoNIRRX9" width="90" height="88"></p>
<p>The upper-left 3×3 part of the matrix is the rotation matrix.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb488d6dd27d9cc6155b35124e61261212298c85.png" data-download-href="/uploads/short-url/xzpEcKpklEQ1LNnzD3WJcuPfVhb.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb488d6dd27d9cc6155b35124e61261212298c85.png" alt="image" data-base62-sha1="xzpEcKpklEQ1LNnzD3WJcuPfVhb" width="690" height="470" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">742×506 23.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>FYI here is the IGRT tutorial, in case you want to also compare DVH or gamma: <a href="https://github.com/SlicerRt/SlicerRtDoc/blob/master/tutorials/SlicerRT_Tutorial_IGRT_4.11.pptx" class="inline-onebox">SlicerRtDoc/tutorials/SlicerRT_Tutorial_IGRT_4.11.pptx at master · SlicerRt/SlicerRtDoc · GitHub</a></p>

---

## Post #3 by @G_Tom (2025-09-26 15:49 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a> for the kind explanations. I have implemented just this :</p>
<pre><code class="lang-auto">        double[,] m = reg.TransformationMatrix;

        // Translations (in mm)
        double[] t = new double[3] { 
            m[3,0], m[3,1], m[3,2] 
        };        

        double RAD2DEG = 180.0 / Math.PI;

        double r00 = m[0,0], r01 = m[0,1], r02 = m[0,2];
        double r10 = m[1,0], r11 = m[1,1], r12 = m[1,2];
        double r20 = m[2,0], r21 = m[2,1], r22 = m[2,2];
        
        // Extract R (row-major)
        double[,] R = new double[3,3];
        // Copy row 0
        R[0, 0] = m[0, 0];
        R[0, 1] = m[0, 1];
        R[0, 2] = m[0, 2];
        // Copy row 1
        R[1, 0] = m[1, 0];
        R[1, 1] = m[1, 1];
        R[1, 2] = m[1, 2];
        // Copy row 2
        R[2, 0] = m[2, 0];
        R[2, 1] = m[2, 1];
        R[2, 2] = m[2, 2];

        // Intrinsic X-Y-Z (roll, pitch, yaw)
        double y_rad = Math.Asin(Math.Max(-1.0, Math.Min(1.0, r02)));
        double x_rad = Math.Atan2(-r12, r22);
        double z_rad = Math.Atan2(-r01, r00);

        double roll = -x_rad * RAD2DEG;  // roll
        double pitch = -y_rad * RAD2DEG;  // pitch
        double yaw = -z_rad * RAD2DEG;  // yaw
        
        // Get first frame
        var cbctframe = cbctvol.Frames.FirstOrDefault();
        var ctframe = ctvol.Frames.FirstOrDefault();
        
        //// Extract parameters from the CBCT frame
        int cbctxSize = cbctframe.XSize;
        int cbctySize = cbctframe.YSize;
        int cbctzSize = cbctframe.ZSize;

        double cbctxRes = cbctframe.XRes;
        double cbctyRes = cbctframe.YRes;
        double cbctzRes = cbctframe.ZRes;

        VVector cbctorigin = cbctframe.Origin;
        VVector cbctxDir = cbctframe.XDirection;
        VVector cbctyDir = cbctframe.YDirection;
        VVector cbctzDir = cbctframe.ZDirection;
        
        
        //// Extract parameters from the CT frame
        int ctxSize = ctframe.XSize;
        int ctySize = ctframe.YSize;
        int ctzSize = ctframe.ZSize;

        double ctxRes = ctframe.XRes;
        double ctyRes = ctframe.YRes;
        double ctzRes = ctframe.ZRes;

        VVector ctorigin = ctframe.Origin;
        VVector ctxDir = ctframe.XDirection;
        VVector ctyDir = ctframe.YDirection;
        VVector ctzDir = cbctframe.ZDirection;
        
        var ctUserOrigin = ctvol.UserOrigin;
        var cbctUserOrigin = cbctvol.UserOrigin;
        
        
        // Compute center directly from origin and half-extent
        VVector cbct_center = cbctorigin
                            + (cbctxSize * 0.5 * cbctxRes) * cbctxDir
                            + (cbctySize * 0.5 * cbctyRes) * cbctyDir
                            + (cbctzSize * 0.5 * cbctzRes) * cbctzDir;
                            
        // Compute center directly from origin and half-extent
        VVector ct_center = ctorigin
                            + (ctxSize * 0.5 * ctxRes) * ctxDir
                            + (ctySize * 0.5 * ctyRes) * ctyDir
                            + (ctzSize * 0.5 * ctzRes) * ctzDir;
</code></pre>
<p>Now the issue is actually recreating those Table shifts (Online Match) values from the screenshots. I am not sure how to recreate this from just the 4x4 matrix shown in slicer.</p>
<p>Thanks a lot for your help</p>

---

## Post #4 by @cpinter (2025-09-30 10:13 UTC)

<aside class="quote no-group" data-username="G_Tom" data-post="3" data-topic="44590">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/g_tom/48/68257_2.png" class="avatar"> G_Tom:</div>
<blockquote>
<p>I am not sure how to recreate this from just the 4x4 matrix shown in slicer</p>
</blockquote>
</aside>
<p>Maybe I misunderstand the question but I think this is just what my comment explains. It starts from the 4x4 matrix and explains how the translation/rotation values can be calculated from that.</p>

---
