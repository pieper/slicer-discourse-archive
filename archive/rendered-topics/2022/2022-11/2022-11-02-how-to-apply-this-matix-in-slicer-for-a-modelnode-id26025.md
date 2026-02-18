# How to apply this matix in slicer for a modelNode

**Topic ID**: 26025
**Date**: 2022-11-02
**URL**: https://discourse.slicer.org/t/how-to-apply-this-matix-in-slicer-for-a-modelnode/26025

---

## Post #1 by @timeanddoctor (2022-11-02 09:35 UTC)

<p>np.Mtrix(Transform4*4):  K, R<br>
position(x,y,z):  X(position), Y(target)</p>
<p>(R[2,:]<em>X)<em>Y=K</em>R</em>X</p>
<p>Can I change upper equation to such format :  Y=Mat*X.  So if X is a Node , I could use it in slicer.<br>
Thanks</p>

---

## Post #2 by @timeanddoctor (2022-11-02 09:36 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5b7c81da7934c3e9f8770978953434ab62f6778.jpeg" alt="未命名_副本" data-base62-sha1="wMb5ECXBVGaX1K8dK1LqOLSnYy4" width="600" height="400"></p>
<p>Can I change the equation to such format : Y=Mat*X.</p>

---
