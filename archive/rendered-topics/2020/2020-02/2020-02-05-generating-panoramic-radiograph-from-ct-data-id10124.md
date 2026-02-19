---
topic_id: 10124
title: "Generating Panoramic Radiograph From Ct Data"
date: 2020-02-05
url: https://discourse.slicer.org/t/10124
---

# Generating Panoramic Radiograph from Ct data

**Topic ID**: 10124
**Date**: 2020-02-05
**URL**: https://discourse.slicer.org/t/generating-panoramic-radiograph-from-ct-data/10124

---

## Post #1 by @JoeCrozier (2020-02-05 12:59 UTC)

<p>Hello,<br>
At our hospital, our craniofacial surgeons have been discussing whether it’s necessary to order both a ct scan and a panoramic xray (“panorex”) when performing certain procedures.  The current practice is to get both, but the argument is that maybe the CT scan already has all the pertinent info and we’re unnecessarily introducing the patient to extra radiation.<br>
When discussing it, one of our surgeons suggested that maybe I could figure out a way to take the data we already had from a CT, and somehow digitally “unwrap” it into something that visually looked like a panorex.<br>
Well, not knowing enough about the differences between either I googled it, and I found these three papers where they seem to have done just that:<br>
<a href="https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0156976&amp;type=printable" class="onebox" target="_blank" rel="nofollow noopener">https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0156976&amp;type=printable</a><br>
<a href="https://www.clinicalkey.com/service/content/pdf/watermarked/1-s2.0-S0169260719303384.pdf?locale=en_US&amp;searchIndex=" class="onebox" target="_blank" rel="nofollow noopener">https://www.clinicalkey.com/service/content/pdf/watermarked/1-s2.0-S0169260719303384.pdf?locale=en_US&amp;searchIndex=</a><br>
<a href="https://www.ingentaconnect.com/contentone/ist/ei/2019/00002019/00000013/art00014?crawler=true&amp;mimetype=application/pdf" class="onebox" target="_blank" rel="nofollow noopener">https://www.ingentaconnect.com/contentone/ist/ei/2019/00002019/00000013/art00014?crawler=true&amp;mimetype=application/pdf</a><br>
Hopefully the links work for you.</p>
<p>My question is:  it seems like those papers used a lot of manual c++ programming and fancy algorithms they wrote up.  Are there any extensions to Slicer that could do the same?  I’m not versed in a lot of that hardcore programming but I’d love to accomplish the same.  Thoughts?</p>

---

## Post #2 by @lassoan (2020-02-05 15:33 UTC)

<p>Yes, Slicer can generate panoramic X-ray from CT. See this post for details: <a href="https://discourse.slicer.org/t/how-to-implement-cpr-curved-plannar-reconstruction-from-centerline/9456/3" class="inline-onebox">How to implement CPR (curved plannar reconstruction) from centerline?</a></p>
<p>Let us know if you have any questions.</p>

---

## Post #3 by @JoeCrozier (2020-02-05 16:28 UTC)

<p>Looks great!  Thank you</p>

---
