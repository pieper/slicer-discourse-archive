# Extracting Implants model form CT scan

**Topic ID**: 43607
**Date**: 2025-07-04
**URL**: https://discourse.slicer.org/t/extracting-implants-model-form-ct-scan/43607

---

## Post #1 by @Naseem_Machlovi (2025-07-04 23:31 UTC)

<p>Hi,<br>
I am new to 3d Slicer and figuring things out. I am planning to extract implant models from patient CT scans and then perform some FEA analysis. Can you please guide me if this is something doable, and if so, do we have any guidelines or tutorials to follow?</p>
<p>Thank you,</p>

---

## Post #2 by @MasatoshiOBA (2025-07-06 22:57 UTC)

<p>Hello Naseem,</p>
<p>I used to specialize in FEA of THA implants.</p>
<p>To begin with the conclusion, it’s quite difficult to perform the entire process using only Slicer.</p>
<p>First, the shape of the implant is affected by artifacts caused by the metal, which also influence the surrounding bone structures. As a result, the implant often appears slightly “inflated” in the images. In addition, due to these artifacts, the CT values of the bone can become abnormally high or low.</p>
<p>Therefore, obtaining an accurate implant model solely from CT data is challenging. The implant geometry must either be reconstructed from CAD or, if possible (though not easy), obtained directly from the manufacturer.</p>
<p>As for CT imaging, it’s best to use preoperative scans.</p>
<p>The postoperative CT should be used as a “guide” for placing the implant model. By aligning the CAD model to the implant position visible in the postoperative CT, and then registering the postoperative CT to the preoperative CT, you can effectively remove the postoperative CT and place the STL model within the preoperative bone.</p>
<p>From there, you can begin your FEA workflow.</p>
<p>There are also various other registration methods you can explore.<br>
However, I do not recommend using the postoperative CT directly as the basis for FEA.</p>
<p>Wishing you all the best in your research!</p>

---

## Post #3 by @Naseem_Machlovi (2025-07-07 13:00 UTC)

<p>Hi Masatoshi,</p>
<p>Thank you for your thorough feedback, and I really appreciate your detailed insights.<br>
I have been digging a lot into this, but haven’t come across anyone who has done it yet, so I thought it might be a good idea to explore it. Maybe I will give it a try to see how challenging it will be and what the limitations will be.</p>
<p>Meanwhile, I will reach out to the manufacturer to get the CAD models. Do you think we can get the drawing details for CAD modelling from the manufacturer’s website or any other community platform, which I haven’t come across yet?</p>
<p>Thank you</p>

---

## Post #4 by @MasatoshiOBA (2025-07-07 22:47 UTC)

<p>Hi Naseem,</p>
<p>Getting STL model data directly from the manufacturer can be quite difficult.</p>
<p>In many cases, you need a strong personal connection — for example, the name of a well-known professor or orthopedic surgeon who has a close relationship with the company — in order to even initiate the conversation. This is because the implant geometry itself is considered intellectual property, and manufacturers must trust that the data will be used strictly for research purposes.</p>
<p>If you’re only looking for approximate models, you can try searching for terms like “STL THA free.” You’ll find several websites offering STL files. However, please note that these are merely <strong>look-alike</strong> models. They might appear realistic, especially with surface textures applied, but in FEA, visual realism is less important than accurate <strong>contact conditions</strong>.</p>
<p>If you’re familiar with CAD software, you might be able to reconstruct a 3D model based on 2D templates. These are sometimes provided to surgeons by manufacturers and printed on transparent sheets as part of standard surgical planning materials. But again, such reconstructions are also only <strong>approximate</strong>.</p>
<p>One thing to keep in mind is that THA implant sizes often do not follow a simple scale-up or scale-down pattern. For example, smaller sizes may have steeper or shallower taper angles. So, the more effort you put into modeling, the better your reconstruction might be — but it will still be an approximation.</p>
<p>Ultimately, which of these approaches you take depends on <strong>what exactly you want to validate or explore through your FEA</strong>.</p>
<p>By the way, while some manufacturers have product search pages on their websites where you can look up implant model numbers, accessing detailed templates — even just 2D ones — is usually quite difficult due to intellectual property restrictions.<br>
Even for licensed surgeons, obtaining such data typically requires formal requests and trust-based relationships. For non-clinicians, especially graduate students, it can be even more challenging.<br>
So unfortunately, these resources are not generally available to the public.</p>
<p>It seems that you’re facing exactly the same challenges I encountered a few years ago — and you’re now trying to go even further beyond them.<br>
I’m sure there will be many difficulties along the way, but I truly hope your research goes well and leads to meaningful results.</p>
<p>Best of luck with your work!</p>

---

## Post #5 by @Naseem_Machlovi (2025-07-08 21:00 UTC)

<p>You are right that getting their details seems impossible until I get involved with a renowned institution or surgeon. All the research papers at the moment discussed different settings for more or less similar implants, which are mostly the Zimmer Z1. As per my research, there have been a lot of changes made in recent THA implants, and none of the studies have compiled them yet, which is probably evident due to their proprietary nature.</p>
<p>I did give it a try to extract the implant from the CT scan and exported a STL file, though. Still, as you mentioned, it seems inflated, and I’m unsure if performing any analysis after smoothing or cleaning will be beneficial.</p>
<p>Thank you for your overview and guidance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd25691a2d0eae8ed1e289bb676f2523886984ac.png" data-download-href="/uploads/short-url/qZgopen9koxHB0K2ZIkTav0SVT6.png?dl=1" title="SceneView_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd25691a2d0eae8ed1e289bb676f2523886984ac.png" alt="SceneView_1" data-base62-sha1="qZgopen9koxHB0K2ZIkTav0SVT6" width="568" height="477"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SceneView_1</span><span class="informations">568×477 16.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
