---
topic_id: 406
title: "Superimposing Two Different Models"
date: 2017-05-31
url: https://discourse.slicer.org/t/406
---

# Superimposing two different models

**Topic ID**: 406
**Date**: 2017-05-31
**URL**: https://discourse.slicer.org/t/superimposing-two-different-models/406

---

## Post #1 by @bpaniagua (2017-05-31 12:15 UTC)

<p>Junwooram wrote on 	Tue, May 30, 2017 at 6:49 PM</p>
<blockquote>
<p>One more question please…<br>
I want to superimpose two different models, but It is not easy to find out the way.<br>
How can I do that?<br>
First, I want to orient the first model.<br>
Then, to superimpose the second model on the first model to compare and quantify the difference.<br>
Please help me.</p>
<p>Thank you.</p>
</blockquote>
<p>Hi Junwooram,</p>
<p>There are plenty of options for model registration in 3DSlicer. You can use the <a href="https://www.slicer.org/wiki/Documentation/4.6/Modules/Transforms">transforms</a> module to make manual adjustments on the alignment of models. For automatic model registration, I recommend you look at the <a href="https://www.slicer.org/wiki/Documentation/4.6/Modules/SurfaceRegistration">surface registration module</a> included in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/CMFreg">CMF reg extension</a>.</p>
<p>Please, let me know if you have further questions.<br>
Best,</p>
<p>Beatriz</p>

---
