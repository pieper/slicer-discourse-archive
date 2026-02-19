---
topic_id: 11113
title: "Problem With Cip 3D Model And Exportation"
date: 2020-04-14
url: https://discourse.slicer.org/t/11113
---

# Problem with CIP 3d model and exportation

**Topic ID**: 11113
**Date**: 2020-04-14
**URL**: https://discourse.slicer.org/t/problem-with-cip-3d-model-and-exportation/11113

---

## Post #1 by @javierfuster (2020-04-14 13:35 UTC)

<p>Hi everyone,</p>
<p>I am making the lobe lung segmentation (Iteractive Lobe Segmentation) with the extension CIP. Everything works fine but at the moment that I want to make a 3D model it results imposible with the lobe segmentation done. I can’t make the 3D model with the 5 lobes segmented and then export this model.</p>
<p>I need your help, please.</p>
<p>Thanks in advance,</p>
<p>Javier</p>

---

## Post #2 by @rbumm (2021-04-27 20:17 UTC)

<p>Hi Javier,</p>
<p>You probably created a <em>labelmap</em> from the Interactive Lobe Segmentation. You need to go to the module “Model Maker”, find the labelmap that was created by CIP, and create a new model of the five lobes.<br>
These can then be found in the module “Models”.<br>
Hope that helps<br>
Rudolf</p>

---
