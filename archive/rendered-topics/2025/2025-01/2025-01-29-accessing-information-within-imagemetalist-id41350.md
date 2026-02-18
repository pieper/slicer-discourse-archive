# Accessing information within ImageMetaList

**Topic ID**: 41350
**Date**: 2025-01-29
**URL**: https://discourse.slicer.org/t/accessing-information-within-imagemetalist/41350

---

## Post #1 by @Arber_Demi (2025-01-29 10:09 UTC)

<p>Hello!</p>
<p>I am trying to automate a data extraction process from a medical device using python, however I’m having issue extracing the data from a ImageMetaList node after receiving it as a response. Is there a way I’m supposed to be able to make an ImageMetaElement such that I can use GetImageMetaElement(), or is there another way I’m missing?</p>
<p>Any advice would be appreciated!</p>
<p>My overall goal is to not have to interact with the Widgets GUI at all, and just query data and place them into nodes for Slicer which I can then use, using python only.</p>
<p>Also wanted to mention that WriteXML is not reachable from the python object, so I can’t use that either to extract the data.</p>

---

## Post #2 by @Arber_Demi (2025-01-29 11:15 UTC)

<p>Forgot to clarify, I am using Slicer 5.6.2, and the ImageMetaList I am referring to is from SlicerOpenIGTLink <a href="https://github.com/openigtlink/SlicerOpenIGTLink/blob/master/OpenIGTLinkIF/MRML/vtkMRMLImageMetaListNode.cxx" rel="noopener nofollow ugc">here</a></p>

---
