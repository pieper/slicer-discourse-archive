---
topic_id: 29105
title: "3D 2D Ct Fluoro Registration"
date: 2023-04-25
url: https://discourse.slicer.org/t/29105
---

# 3D-2D CT-Fluoro registration

**Topic ID**: 29105
**Date**: 2023-04-25
**URL**: https://discourse.slicer.org/t/3d-2d-ct-fluoro-registration/29105

---

## Post #1 by @BraveDistribution (2023-04-25 06:01 UTC)

<p>Hello community,</p>
<p>I would like to perform 3D-2D registration (CT-fluoroscopy) on pelvis data from the GitHub repository <a href="https://github.com/rg2/Regi2D3D-IPCAI2020" class="inline-onebox" rel="noopener nofollow ugc">GitHub - rg2/Regi2D3D-IPCAI2020: Code for the registration component of the IPCAI 2020 paper: "Automatic Annotation of Hip Anatomy in Fluoroscopy for Robust and Efficient 2D/3D Registration." https://arxiv.org/abs/1911.07042 or https://doi.org/10.1007/s11548-020-02162-7</a>.</p>
<p>I have some assumptions on how to perform the registration:</p>
<ol>
<li>Create DRR - I can achieve that with <a href="https://github.com/arcadelab/deepdrr" class="inline-onebox" rel="noopener nofollow ugc">GitHub - arcadelab/deepdrr: Code for "DeepDRR: A Catalyst for Machine Learning in Fluoroscopy-guided Procedures". https://arxiv.org/abs/1803.08606</a>.</li>
<li>Compare two images to obtain the NCC loss (DRR, fluoroscopy).</li>
<li>Optimize the transformation and rotation matrix to minimize loss. At the moment, I can use some nature-inspired algorithm since this is a proof of concept and real-time capability is not necessary yet.</li>
</ol>
<p>I have read <a class="mention" href="/u/lassoan">@lassoan</a>’s answers from both <a href="https://discourse.slicer.org/t/get-projection-plane-in-2d-3d-registration/26023" class="inline-onebox">Get projection plane in 2D-3D Registration</a> and <a href="https://discourse.slicer.org/t/get-projection-plane-in-2d-3d-registration/26023" class="inline-onebox">Get projection plane in 2D-3D Registration</a>.</p>
<blockquote>
<p>2D/3D registration is a challenging problem. You need to set the initial pose close to the solution, but there may be other tricks as well.</p>
</blockquote>
<p>If I want to get the initial pose close to the solution, can I perform manual registration via some fiducials in 3DSlicer? If yes, could you please tell me how?</p>
<p>Thanks</p>

---
