---
topic_id: 32775
title: "Extractorglcm Execute"
date: 2023-11-13
url: https://discourse.slicer.org/t/32775
---

# extractorGLCM.execute()

**Topic ID**: 32775
**Date**: 2023-11-13
**URL**: https://discourse.slicer.org/t/extractorglcm-execute/32775

---

## Post #1 by @Tomas_Korinek (2023-11-13 10:15 UTC)

<p>Hello everybody.<br>
I would love to use your genius ideas and asking for a help.<br>
This is my code for radiomics extraction:</p>
<p>Img,Mask = PyrexReader.Img_Bimask(img_path,rtstruct_path,ROI)</p>
<p>extractorFO      = radiomics.firstorder.RadiomicsFirstOrder(Img, Mask)<br>
extractorSF3D    = radiomics.shape.RadiomicsShape(Img, Mask)<br>
extractorGLCM    = radiomics.glcm.RadiomicsGLCM(Img, Mask)<br>
extractorGLSZM   = radiomics.glszm.RadiomicsGLSZM(Img, Mask)<br>
extractorGLRLM   = radiomics.glrlm.RadiomicsGLRLM(Img, Mask)<br>
extractorNGTDM   = radiomics.ngtdm.RadiomicsNGTDM(Img, Mask)<br>
extractorGLDM    = radiomics.gldm.RadiomicsGLDM(Img, Mask)</p>
<p>resultFO = extractorFO.execute()<br>
for key, val in six.iteritems(resultFO):<br>
print(“\t%s: %s” %(key, val))</p>
<p>resultSF3D = extractorSF3D.execute()<br>
for key, val in six.iteritems(resultSF3D):<br>
print(“\t%s: %s” %(key, val))</p>
<p>extractorGLCM.execute()</p>
<p>Laset row in script: extractorGLCM.execute(), writes down a error:<br>
IndexError: arrays used as indices must be of integer (or boolean) type</p>
<p>Would you know how to solve that? What to change in code? When I use it on 10 datasets (CT, RS dicom), it occurs in 5 datasets from 10.</p>
<p>Thank you for any ideas! Tomas, Czech Republic.</p>

---
