---
topic_id: 16658
title: "Build Fails Vtk9 Expected"
date: 2021-03-20
url: https://discourse.slicer.org/t/16658
---

# Build fails : VTK9 expected

**Topic ID**: 16658
**Date**: 2021-03-20
**URL**: https://discourse.slicer.org/t/build-fails-vtk9-expected/16658

---

## Post #1 by @chir.set (2021-03-20 15:22 UTC)

<p>Slicer build failed today on Arch Linux against VTK8. This trivial patch fixed the build process. I can’t know if it’s the right fix.</p>
<pre><code class="lang-diff">diff --git a/Libs/MRML/Core/vtkMRMLModelStorageNode.cxx b/Libs/MRML/Core/vtkMRMLModelStorageNode.cxx index e7e29785c7..a6851467cf 100644
--- a/Libs/MRML/Core/vtkMRMLModelStorageNode.cxx
+++ b/Libs/MRML/Core/vtkMRMLModelStorageNode.cxx
@@ -507,13 +507,17 @@ int vtkMRMLModelStorageNode::WriteDataInternal(vtkMRMLNode *refNode)
     if (modelNode-&gt;GetMeshType() == vtkMRMLModelNode::PolyDataMeshType)
       {
       writer = vtkSmartPointer&lt;vtkPolyDataWriter&gt;::New();
+#if VTK_MAJOR_VERSION &gt;= 9 || (VTK_MAJOR_VERSION &gt;= 8 &amp;&amp; VTK_MINOR_VERSION &gt;= 90)      
       writer-&gt;SetFileVersion(42);
+#endif      
       writer-&gt;SetInputData(meshToWrite);
       }
     else
       {
       writer = vtkSmartPointer&lt;vtkUnstructuredGridWriter&gt;::New();
+#if VTK_MAJOR_VERSION &gt;= 9 || (VTK_MAJOR_VERSION &gt;= 8 &amp;&amp; VTK_MINOR_VERSION &gt;= 90)
       writer-&gt;SetFileVersion(42);
+#endif
       writer-&gt;SetInputData(meshToWrite);
       }
 
diff --git a/Modules/CLI/ModelMaker/ModelMaker.cxx b/Modules/CLI/ModelMaker/ModelMaker.cxx
index 6c3b6065b1..374fad5c6c 100644
--- a/Modules/CLI/ModelMaker/ModelMaker.cxx
+++ b/Modules/CLI/ModelMaker/ModelMaker.cxx
@@ -1177,7 +1177,9 @@ int main(int argc, char * argv[])
       if (SaveIntermediateModels)
         {
         writer = vtkSmartPointer&lt;vtkPolyDataWriter&gt;::New();
+#if VTK_MAJOR_VERSION &gt;= 9 || (VTK_MAJOR_VERSION &gt;= 8 &amp;&amp; VTK_MINOR_VERSION &gt;= 90)
         writer-&gt;SetFileVersion(42);
+#endif
         std::string            commentSaveCubes = "Writing intermediate model after marching cubes " + labelName;
         vtkPluginFilterWatcher watchWriter(writer,
                                            commentSaveCubes.c_str(),
</code></pre>
<p>Regards.</p>

---

## Post #2 by @chir.set (2021-03-22 09:04 UTC)

<p>OK, Slicer nightly now ships with VTK9; this might explain why the code doesn’t check VTK version anymore. But VMTK extension is not available for VTK9. Until VMTK extension builds with VTK9, I’ll have to build Slicer with VTK8, as long as next fixes are as trivial as above. One more reason why self built Slicer may be of interest.</p>

---

## Post #3 by @jcfr (2021-03-24 04:18 UTC)

<p>To follow up, errors discussed here have been fixed by <a class="mention" href="/u/lassoan">@lassoan</a> in these commits:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/commit/7eb86ab4e4e7450c58359e30a64cc474368266be" class="inline-onebox">COMP: Fix build error with VTK8 · Slicer/Slicer@7eb86ab · GitHub</a></li>
<li><a href="https://github.com/Slicer/Slicer/commit/2f15e458f3a4af5f6c4ca33ffe6a301fdce7b820" class="inline-onebox">COMP: Fix remaining build error with VTK8 · Slicer/Slicer@2f15e45 · GitHub</a></li>
</ul>

---
