---
topic_id: 20651
title: "Parameter Settings For Levelset Segmentation In Coronary Art"
date: 2021-11-17
url: https://discourse.slicer.org/t/20651
---

# Parameter settings for Levelset segmentation in coronary artery segmentation

**Topic ID**: 20651
**Date**: 2021-11-17
**URL**: https://discourse.slicer.org/t/parameter-settings-for-levelset-segmentation-in-coronary-artery-segmentation/20651

---

## Post #1 by @biplabketan (2021-11-17 05:39 UTC)

<p>Please let me know the correct parameter settings for <strong>levelset segmentation</strong> for coronary artery segmentation. Also, how the number of iterations can be selected? What is the significance of it and what is the convergence criteria?</p>

---

## Post #2 by @kayarre (2021-11-29 23:35 UTC)

<p>hi <a class="mention" href="/u/biplabketan">@biplabketan</a> and welcome.</p>
<p>This depends on the kind of images you have. how noisy? how much contrast? Usuallly one has to play around with the values. a good place to start is using slicer and playing around with the threshold segmentation to get an idea for values that get close the vessel edges. I believe Luca Antiga’s thesis, ITK, or Slicer documentation could provide some insight.</p>

---
