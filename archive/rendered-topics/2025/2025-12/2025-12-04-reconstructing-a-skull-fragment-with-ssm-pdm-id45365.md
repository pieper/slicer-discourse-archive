# Reconstructing a skull fragment with SSM/PDM

**Topic ID**: 45365
**Date**: 2025-12-04
**URL**: https://discourse.slicer.org/t/reconstructing-a-skull-fragment-with-ssm-pdm/45365

---

## Post #1 by @ThomasVanParys (2025-12-04 16:01 UTC)

<p>Hello!</p>
<p>I am seeking advice on how to practically reconstruct a skull in order to calculate cranial capacity.<br>
The skull is a fragment (missing skull base and some parietal), estimated to be a 4 year old indiviual.<br>
I have segmented complete skulls of 4 year olds from NMDID CT scans and aligned them with landmark-based alignment in Scalismo/VSC Studio.</p>
<p>What would be the next steps? Do I need to resample to a reference mesh to get point-to-point correspondence? Do I need to create a mean shape and warp it to fit the shape of the skull fragment? I believe the SSM approach is reliable for skull reconstruction/estimation?<br>
How much of this can be done in slicer. I am strugging with the coding side of VSC studio, but this is what I have so far:</p>
<pre><code class="lang-auto">//&gt; using scala "3.3.7"
//&gt; using repository "https://scalismo.org/repo/"
//&gt; using dep "ch.unibas.cs.gravis::scalismo:0.92.0"
//&gt; using dep "ch.unibas.cs.gravis::scalismo-ui:0.92.0"

import scalismo.geometry._
import scalismo.common._
import scalismo.mesh._
import scalismo.transformations._
import scalismo.io.MeshIO
import scalismo.ui.api._
import scalismo.registration._
import java.io.File

object SkullRigidAlignmentApp {

  def main(args: Array[String]): Unit = {

    // Initialize Scalismo and the UI
    scalismo.initialize()
    val ui = ScalismoUI()

    // Load skull meshes
    val skullFiles = Seq(
      new File("G:\\Kikopey_project\\skull-ssm\\data\\case-119553_skull.ply"),
      new File("G:\\Kikopey_project\\skull-ssm\\data\\case-137263_skull.ply"),
      new File("G:\\Kikopey_project\\skull-ssm\\data\\case-119851_skull.ply")
    )

    val skullMeshes: Seq[TriangleMesh[_3D]] =
      skullFiles.map(file =&gt; MeshIO.readMesh(file).get)

    // Display original skulls
    val skullGroup = ui.createGroup("OriginalSkulls")
    skullMeshes.zipWithIndex.foreach { case (mesh, idx) =&gt;
      ui.show(skullGroup, mesh, s"Skull${idx + 1}")
    }

    // Pick the first skull as reference
    val referenceMesh = skullMeshes.head

    // Define landmarks (replace with actual PointIds from your meshes)
    val landmarkIds = Seq(PointId(1000), PointId(5000), PointId(10000))
    val referenceLandmarks = landmarkIds.map(pid =&gt;
      Landmark(s"ref-${pid.id}", referenceMesh.pointSet.point(pid))
    )

    // Align other skulls rigidly to the reference
    val alignedSkullsGroup = ui.createGroup("AlignedSkulls")
    skullMeshes.zipWithIndex.tail.foreach { case (mesh, idx) =&gt;

      val targetLandmarks = landmarkIds.map(pid =&gt;
        Landmark(s"tgt-${pid.id}", mesh.pointSet.point(pid))
      )

      // Compute best rigid transform using landmarks
      val bestTransform: RigidTransformation[_3D] =
        LandmarkRegistration.rigid3DLandmarkRegistration(referenceLandmarks, targetLandmarks, center = Point(0, 0, 0))

      // Apply transformation
      val alignedMesh = mesh.transform(bestTransform)

      // Show aligned mesh in UI
      val view = ui.show(alignedSkullsGroup, alignedMesh, s"AlignedSkull${idx + 2}")
      view.color = java.awt.Color.RED
    }

    println("Rigid alignment done. Check the UI for original and aligned skulls.")
  }
}
</code></pre>
<p>The skull fragment mesh looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26f8bc03e562517746080a9abcfe21336a3aeff8.jpeg" data-download-href="/uploads/short-url/5yL3pcXq4OKWK8HsazEgET1JO9W.jpeg?dl=1" title="Screenshot 2025-12-04 155954" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26f8bc03e562517746080a9abcfe21336a3aeff8_2_602x499.jpeg" alt="Screenshot 2025-12-04 155954" data-base62-sha1="5yL3pcXq4OKWK8HsazEgET1JO9W" width="602" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26f8bc03e562517746080a9abcfe21336a3aeff8_2_602x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26f8bc03e562517746080a9abcfe21336a3aeff8.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26f8bc03e562517746080a9abcfe21336a3aeff8.jpeg 2x" data-dominant-color="7C7D9C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-12-04 155954</span><span class="informations">708×588 96.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84015a101428d5baffe0adfe337b2ea2932e2da2.jpeg" data-download-href="/uploads/short-url/iPLVbs4kHv5JGsG5PtulD99N4To.jpeg?dl=1" title="Screenshot 2025-12-04 155946" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84015a101428d5baffe0adfe337b2ea2932e2da2_2_559x500.jpeg" alt="Screenshot 2025-12-04 155946" data-base62-sha1="iPLVbs4kHv5JGsG5PtulD99N4To" width="559" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84015a101428d5baffe0adfe337b2ea2932e2da2_2_559x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84015a101428d5baffe0adfe337b2ea2932e2da2.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84015a101428d5baffe0adfe337b2ea2932e2da2.jpeg 2x" data-dominant-color="737397"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-12-04 155946</span><span class="informations">701×626 81.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you!</p>

---

## Post #2 by @muratmaga (2025-12-04 16:21 UTC)

<p>I am not sure if statismo would be much of use here. You can take a few age matched individuals from NIDID segment the endocranial space from the. Deformably register those to your specimen, and the use that mapping to transfer the segmented endocranial space to your fragmented skull. Doing this a few different individuals will give you a range of estimates then you can decide to average or report or as a range.</p>

---

## Post #3 by @ThomasVanParys (2025-12-04 16:43 UTC)

<p>Thank you for the advice as always!</p>
<p>How would you perform the endocranial deformations and register the deformable/mean shape to the fossil fragment? I am less versed with Python, if that is what you recommend. Can this be done within Slicer?</p>
<p>Thiss individual likely had craniosynostosis (via fusion of sagittal and parietal sutures) with a congenital syndrome. I think a range for CC would be best.</p>

---

## Post #4 by @muratmaga (2025-12-04 16:52 UTC)

<p>You can use python but don’t need to.</p>
<p>You can use ANTs registration to do that in Slicer. It is available through SlicerANTs and SlicerANTsPy extension (the former is only registration, the latter has more functionality but the parameters you can control for registration is not as comprehensive as the other).</p>
<p>In either case you want to use the SyNRegistrationQuick[s] for quick results and then just use SyN for final set of results (will take some time).</p>

---

## Post #5 by @ThomasVanParys (2025-12-04 17:17 UTC)

<p>Thank you, I will look into this further.</p>
<p>I am assuming ANTs handles volumes (i.e., segmented CT scans) rather than 3D models of my endocasts? Can it batch process multiple at one time?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c574eccc66e383ad38816adc2a106881551f53e.png" data-download-href="/uploads/short-url/1LaMIv1WDqmovfViSU0ZCiqIZhI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c574eccc66e383ad38816adc2a106881551f53e_2_395x500.png" alt="image" data-base62-sha1="1LaMIv1WDqmovfViSU0ZCiqIZhI" width="395" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c574eccc66e383ad38816adc2a106881551f53e_2_395x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c574eccc66e383ad38816adc2a106881551f53e_2_592x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c574eccc66e383ad38816adc2a106881551f53e_2_790x1000.png 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1053×1330 52.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am assuming you mean the SyN function in BRAINS General Registration:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f3e9413c0f4e9bd463df123ca24e7d29d42327d.png" data-download-href="/uploads/short-url/91u9z7FdCwEVFEGVkXCoVQ5S4Fv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f3e9413c0f4e9bd463df123ca24e7d29d42327d_2_300x500.png" alt="image" data-base62-sha1="91u9z7FdCwEVFEGVkXCoVQ5S4Fv" width="300" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f3e9413c0f4e9bd463df123ca24e7d29d42327d_2_300x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f3e9413c0f4e9bd463df123ca24e7d29d42327d_2_450x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f3e9413c0f4e9bd463df123ca24e7d29d42327d_2_600x1000.png 2x" data-dominant-color="F4F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1051×1749 77.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you for answering my questions, this has been difficult to conceptualise <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @muratmaga (2025-12-04 17:23 UTC)

<p>Yes, ANTs is a volumetric registration module.  I assumed you segmented your skulls in Slicer. If you don’t have the original volumes, obviously this won’t work.</p>
<p>SyN option in the Brains Registration doesn’t work (it requires Brains to be built against ANTs, which is not done in Slicer build). You need to use the ANTsRegistration module.</p>
<p>If you are using ANTs extension, then you would choose QuickSyN, for quick results. Looks like ANTsPY extension has an issue blocking to be run in Slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5120ae69ee151f0c687d3635f1490d61ec89f452.png" data-download-href="/uploads/short-url/bzGH3zj8aA4kXlBcRImO7ltDLAC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5120ae69ee151f0c687d3635f1490d61ec89f452.png" alt="image" data-base62-sha1="bzGH3zj8aA4kXlBcRImO7ltDLAC" width="493" height="393"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">493×393 28.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @ThomasVanParys (2025-12-04 17:41 UTC)

<p>Thank you - I am currently away from my computer, but can the ANTs extension run a batch of multiple volumes at one time?</p>

---

## Post #8 by @muratmaga (2025-12-04 17:59 UTC)

<aside class="quote no-group" data-username="ThomasVanParys" data-post="7" data-topic="45365">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ThomasVanParys:</div>
<blockquote>
<p>can the ANTs extension run a batch of multiple volumes at one time?</p>
</blockquote>
</aside>
<p>No, but ANTsPy can (it is in the groupwise registration tab).</p>
<p>Also, the issue turned out to be simple. ANTs and ANTsPy apparently can’t co-exist (at the moment). If you want to use ANTspy, uninstall the ANTs extension and things should work. Again you want to start with <strong>antsRegistrationSyNQuick[s]</strong> until you know things are working.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e27c12a5efac9f9be0ad8911f1a29d9360f283ba.png" data-download-href="/uploads/short-url/wjzJshHOkugOn9kHrUR2bWZXmc2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e27c12a5efac9f9be0ad8911f1a29d9360f283ba.png" alt="image" data-base62-sha1="wjzJshHOkugOn9kHrUR2bWZXmc2" width="690" height="399" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">760×440 21.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @ThomasVanParys (2025-12-05 11:04 UTC)

<p>Thank you.<br>
I am using ANTsPy. Pair-wise QuickRigid registration was much faster than antsRegistrationSyNQuick[s] which is yet to finish (&gt;1 hour). Is this normal? I am assuming SyN is doing both Affine and Rigid registration, and full SyN parameters will take even longer.</p>
<p>Just to clarify - Would you recommend deforming the endocranial cavity volumes, or the skull volumes themselves?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/391c34eb92e3c29889008080d2e23c7b3aea57f4.jpeg" data-download-href="/uploads/short-url/89dEczSdq1saJKRT2r7YtiKtpvm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/391c34eb92e3c29889008080d2e23c7b3aea57f4_2_690x310.jpeg" alt="image" data-base62-sha1="89dEczSdq1saJKRT2r7YtiKtpvm" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/391c34eb92e3c29889008080d2e23c7b3aea57f4_2_690x310.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/391c34eb92e3c29889008080d2e23c7b3aea57f4_2_1035x465.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/391c34eb92e3c29889008080d2e23c7b3aea57f4_2_1380x620.jpeg 2x" data-dominant-color="B9BBDA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×865 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I will use Group-Wise to batch register my volumes, but how exactly do I go form this stage to transfering it to the fragmented skull? Thank you!</p>

---

## Post #10 by @ThomasVanParys (2025-12-05 14:51 UTC)

<p>If anyone has further advice on this regarding a workflow I would be very grateful! <a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #11 by @muratmaga (2025-12-05 16:36 UTC)

<p>Quick or Affine are not deformable registrations. Quick simply rotates and translates the object, affine does the same with scaling and shearing allowed. You need deformable registration to warp one object to the other, and that’s computationally expensive and long.</p>
<p>So, if you want to run things fast, down sample your fixed volume by 2 using crop volume (ants will automatically resample the moving one to match that). It will go faster. Or find a computer with lots of cores.</p>

---

## Post #12 by @ThomasVanParys (2025-12-05 16:43 UTC)

<p>Thank you.<br>
This has been my procedure and parameters so far:<br>
(1) <em>Group-Wise Tab:</em></p>
<p>Template: case-109181_skull.nrrd.<br>
Output: Transformed Volume.<br>
transform Type: antsRegistrationSyNQuick[s] (~30 mins / volume).</p>
<p>(2) Then in the <em>Template</em> tab:</p>
<p>Initital Template: case-109181_skull.nrrd<br>
Transform Type: antsRegistrationSyNQuick[s], iterations: 1 (I know &gt;3 iterations would be ideal).<br>
Select Input Images: The Group-Wise registered .nii.gz’s<br>
Run Template Building and create new volume.</p>
<p>(3) <em>Pair-wise</em> tab:<br>
Fixed Image: fragmented skull fossil (photo in above conversation)<br>
Moving Image: Template .nrrd<br>
Transform Type: SyN<br>
Create Transformed Volume.</p>
<p>Would you add/change this workflow?<br>
How do I go from the labelmap volume to segmentation to compute segment statistics/endocranial capacity/volume etc?</p>

---

## Post #13 by @chz31 (2025-12-05 16:56 UTC)

<p>I recently created a module for reconstructing fractured orbit using the mirrored contralateral side built on functions from SlicerMorph.</p>
<p>I wonder if the two sides are similar enough to warrant a good registration, but it might not hurt to give it a quick try.</p>
<p>You can one-click install <a href="https://github.com/chz31/SlicerOrbitSurgerySim?tab=readme-ov-file#mirrororbitrecon-module-tutorial" rel="noopener nofollow ugc">SlicerOrbitSurgerySim</a>from the Extension Manager on 5.10. It’ll load SlicerMorph for you as well.</p>
<p>It has sample data for you to play with. See video tutorial: <a href="http://youtube.com/watch?si=wHra2VXSp__asPQt&amp;v=t951sCvk_lc&amp;feature=youtu.be" rel="noopener nofollow ugc">youtube.com/watch?si=wHra2VXSp__asPQt&amp;v=t951sCvk_lc&amp;feature=youtu.be</a></p>

---

## Post #14 by @muratmaga (2025-12-05 17:21 UTC)

<p>I don</p>
<aside class="quote no-group" data-username="ThomasVanParys" data-post="12" data-topic="45365">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ThomasVanParys:</div>
<blockquote>
<p>(2) Then in the <em>Template</em> tab:</p>
</blockquote>
</aside>
<p>If you are going to use my suggested approach, which is find 3-4 age/sex matched normal skulls, and segment the endocranial space from them, and then deformably register them to your fractured one, then you don’t need to use the template workflow. Only the groupswise.</p>
<p>Settings would be</p>
<p>Fixed is the fractured skull</p>
<p>moving would be your intact skulls (3-4 of them)</p>
<p>Transform would be initially AntsRegistrationSyNQuick[s], and the output would all of them (transformed volume, forward and inverse transforms).</p>
<p>SyN is about 10 times slower than the SyNQuick (uses cross-correlation instead mutual informaiton) and definitely results better alignment, but your goal is to get results quick to see how things work out. So I would stick with SyNQuick until you know things works and you want the best outcome.</p>

---

## Post #15 by @ThomasVanParys (2025-12-05 18:18 UTC)

<p>Great, I will try this.<br>
A potential issue, however, is that the fragmented skull is just an .obj surface mesh. Converting this to a segmentation → Export models and labelmaps → Export to new labelmap, creates anomalies and artefacts in the volume (bottom: surface mesh, top: labelmap volume in 3D rendering). This might be ok, but I will have to test it out.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c91b27f951c6bd04e42054862a0fefee68d5f1bf.jpeg" data-download-href="/uploads/short-url/sH49vr0Q3Tz8MwYOIbC3KHhQA4D.jpeg?dl=1" title="Screenshot 2025-12-05 181452" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c91b27f951c6bd04e42054862a0fefee68d5f1bf.jpeg" alt="Screenshot 2025-12-05 181452" data-base62-sha1="sH49vr0Q3Tz8MwYOIbC3KHhQA4D" width="423" height="355"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-12-05 181452</span><span class="informations">564×474 81 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cb899170af441408c4a3706ae0fbe2379387c2c.jpeg" data-download-href="/uploads/short-url/1OxectMXG9R8HLv2iZT8UJZA6VS.jpeg?dl=1" title="Screenshot 2025-12-05 181326" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cb899170af441408c4a3706ae0fbe2379387c2c.jpeg" alt="Screenshot 2025-12-05 181326" data-base62-sha1="1OxectMXG9R8HLv2iZT8UJZA6VS" width="447" height="354"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-12-05 181326</span><span class="informations">597×472 69.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(unless of course I manually clean this in the segment editor myself)<br>
Or I might have better results with the Model to LabelMap plug-in?</p>

---

## Post #16 by @chz31 (2025-12-05 18:34 UTC)

<p>Would you be able to fill it using something like SurfaceWrapSolidify?</p>
<aside class="quote quote-modified" data-post="1" data-topic="11248">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/fill-or-extract-cavities-in-segmentations-using-the-new-wrap-solidify-effect/11248">Fill or extract cavities in segmentations using the new "Wrap Solidify" effect</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Making a segment that has fractured, discontinuous boundary and holes inside to be a simple solid object is a quite common task for segmentation. For example it is needed for creating simple solid bone models from CT images, extracting skin surface, segment thin surfaces, such as orbital bone wall, measuring brain volume, or volumes of various cavities. 
Slicer now has a tool for all this: “Wrap Solidify” Segment Editor effect, provided by <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify" rel="noopener nofollow ugc">SurfaceWrapSolidify extension</a> and contributed by Sebasti…
  </blockquote>
</aside>

<aside class="onebox githubrepo" data-onebox-src="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">
  <header class="source">

      <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/556b67fda6347e85c653519d562cd332/sebastianandress/Slicer-SurfaceWrapSolidify" class="thumbnail">

  <h3><a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify" target="_blank" rel="noopener nofollow ugc">GitHub - sebastianandress/Slicer-SurfaceWrapSolidify: 3D Slicer extension which contains a Segment...</a></h3>

    <p><span class="github-repo-description">3D Slicer extension which contains a Segment Editor Effect that solidifies and extracts the surface of a segmentation</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #17 by @muratmaga (2025-12-05 18:35 UTC)

<p>How did you generate the obj? You don’t have the original scan? That’s what you will need for this to work. Even if you were to able to generate a decent labelmap by cleaning up, registration will not work, as it expects and intensity image.</p>

---

## Post #18 by @ThomasVanParys (2025-12-05 18:39 UTC)

<p>That’s a huge shame! I believe it was made via photogrammetry/Artec Spider work…</p>

---

## Post #19 by @ThomasVanParys (2025-12-05 18:46 UTC)

<p>We will have to CT scan the Crania when we are next in the field - but is there any possible method to use the .obj alone?</p>

---

## Post #20 by @muratmaga (2025-12-05 18:46 UTC)

<p>ANTs is an intensity registration framework, so it does need intensity images. You can convert all your volumes labelmaps and do a labelmap registrations….</p>
<p>There might be deformable mesh registration frameworks that can do what I suggested on 3D models.</p>

---

## Post #21 by @ThomasVanParys (2025-12-05 18:51 UTC)

<p>Ok - I will try a few other methods, what do you mean by converting volumes labelmaps and do a labelmap registration? Does that mean using the .nrrd’s instead of the registered .nii’s ?</p>
<p>I wonder if Scalismo can work with meshes alone? Although I am struggling with the coding aspect</p>

---

## Post #22 by @muratmaga (2025-12-05 19:05 UTC)

<aside class="quote no-group" data-username="ThomasVanParys" data-post="21" data-topic="45365">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ThomasVanParys:</div>
<blockquote>
<p>what do you mean by converting volumes labelmaps and do a labelmap registration</p>
</blockquote>
</aside>
<p>If you threshold your volumes, and create a labelmap, you can input those as the fixed and moving volumes (I think). That’s what I meant. Format doesn’t matter both nii.gz and nrrd are fine.</p>

---

## Post #23 by @ThomasVanParys (2025-12-05 19:34 UTC)

<p>Perhaps I’m doing this in the wrong order - but I already have labelmaps of the volumes as .nrrd files - I would still, at some stage, need to input the fragmented skull as the fixed volume?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/1823375144d56cfd04c1fce507c5b275ff12aafe.png" data-download-href="/uploads/short-url/3rwUnK366refjKQSyKAEJPOp7vE.png?dl=1" title="Screenshot 2025-12-05 193250" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/1823375144d56cfd04c1fce507c5b275ff12aafe.png" alt="Screenshot 2025-12-05 193250" data-base62-sha1="3rwUnK366refjKQSyKAEJPOp7vE" width="663" height="360"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-12-05 193250</span><span class="informations">663×360 8.48 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb1e70b3a273ae1b71b1285cc17424d7f97f259d.jpeg" data-download-href="/uploads/short-url/zPv3UafQfQ7WPXScD1EOJuE83o1.jpeg?dl=1" title="Screenshot 2025-12-05 193233" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb1e70b3a273ae1b71b1285cc17424d7f97f259d_2_690x303.jpeg" alt="Screenshot 2025-12-05 193233" data-base62-sha1="zPv3UafQfQ7WPXScD1EOJuE83o1" width="690" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb1e70b3a273ae1b71b1285cc17424d7f97f259d_2_690x303.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb1e70b3a273ae1b71b1285cc17424d7f97f259d_2_1035x454.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb1e70b3a273ae1b71b1285cc17424d7f97f259d_2_1380x606.jpeg 2x" data-dominant-color="BABBCF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-12-05 193233</span><span class="informations">1663×731 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #24 by @ThomasVanParys (2025-12-06 17:57 UTC)

<p>Thank you. How do you recommend registering the two halves together? I am concerned about asymmetry in the skull, and thus oversampling the cranial capacity. It also still lacks much of the skull base, so estimating cranial capacity from a non watertight mesh could be tricky… any advice is appreciated!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84338819843dcc3b748c40409ede2b0a6b411644.png" data-download-href="/uploads/short-url/iRvqN63E9anriVcYigdzcIiv940.png?dl=1" title="Screenshot 2025-12-06 175410" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84338819843dcc3b748c40409ede2b0a6b411644_2_517x301.png" alt="Screenshot 2025-12-06 175410" data-base62-sha1="iRvqN63E9anriVcYigdzcIiv940" width="517" height="301" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84338819843dcc3b748c40409ede2b0a6b411644_2_517x301.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84338819843dcc3b748c40409ede2b0a6b411644_2_775x451.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84338819843dcc3b748c40409ede2b0a6b411644_2_1034x602.png 2x" data-dominant-color="ECD0D2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-12-06 175410</span><span class="informations">1637×955 270 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bf67a094180f3f921af4500c888c48e02083f66.jpeg" data-download-href="/uploads/short-url/3ZmXRMzogmPFqoAeobdaI787WJM.jpeg?dl=1" title="Screenshot 2025-12-06 175356" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bf67a094180f3f921af4500c888c48e02083f66_2_517x285.jpeg" alt="Screenshot 2025-12-06 175356" data-base62-sha1="3ZmXRMzogmPFqoAeobdaI787WJM" width="517" height="285" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bf67a094180f3f921af4500c888c48e02083f66_2_517x285.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bf67a094180f3f921af4500c888c48e02083f66_2_775x427.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bf67a094180f3f921af4500c888c48e02083f66_2_1034x570.jpeg 2x" data-dominant-color="E7E8D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-12-06 175356</span><span class="informations">1668×922 266 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #25 by @chz31 (2025-12-06 18:26 UTC)

<p>I am glad it helps!</p>
<p>Reconstruction can be very ad hoc due to variations left-right asymmetry and you might try a couple of different methods. Fossils also may involve distortions.</p>
<p>A few methods I could think about:</p>
<ul>
<li>Use a skull that looks similar (e.g., one species, perhaps using the strictest species definition, similar age) to fix it. You could try FastModelAlign from SlicerMorph for model registration and affine deformation. <a href="https://github.com/SlicerMorph/Tutorials/tree/main/FastModelAlign" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/FastModelAlign at main · SlicerMorph/Tutorials · GitHub</a></li>
<li>You can also manually adjust it using the new Slicer interaction transform handle. Simple go to Data module, right click the eyeball, and activate the 3D interaction transform. You’ll see a handle to play with.</li>
<li>You can also use the Fiducial Registration Wizard to use manual landmarks to align left-right or two specimens. <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/fiducialregistration.html" class="inline-onebox" rel="noopener nofollow ugc">Fiducial Registration — 3D Slicer documentation</a></li>
<li>Once it is registered, you can use the affine registration in MirrorOrbitRecon or FastModelAlign to see if slight deformation can improve the fit.</li>
<li>Another way is the thin plate spline transformation between two manual landmark sets with correspondence manually established. You can then use the generated grid transform to transform one specimen to match to another one. This may require minimal Python programming. I could send you a snippet later (the same method is used in GPA of SlicerMorph as well).</li>
</ul>
<p>My feeling is, you might want to use manual landmarks to see if it’ll perform better than model registrations since the bones could be fragmentary. Again, there is no guarantee which method would be suitable unless trying them one-by-one.</p>

---

## Post #26 by @muratmaga (2025-12-06 19:32 UTC)

<aside class="quote no-group" data-username="ThomasVanParys" data-post="24" data-topic="45365">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ThomasVanParys:</div>
<blockquote>
<p>How do you recommend registering the two halves together? I am concerned about asymmetry in the skull, and thus oversampling the cranial capacity. I</p>
</blockquote>
</aside>
<p>That’s why I suggested image registration based deformation, since you wouldn’t have to worry too much about the lack of cranial base, remaining points should still give you reliable deformation.</p>
<p>Since you can’t use that method due to lack of CT scan of the actual specimen, you might want to  consider using tools in the Dynamic modeler plane cut options. You can use mid sagittal to remove the damaged side (left), then another plane to create an artficial cranial base, and then calculate the volume inside and multiply by 2. You want to use the PlaneCut with the cap option enabled.</p>

---

## Post #27 by @ThomasVanParys (2025-12-07 08:38 UTC)

<p>I will try this. How does one create an artificial cranial base? using an ROI clipping of an aligned complete skull and then merging with the sagitally clipped fragmented skull?<br>
Or is this just via:  Add another <strong>Plane Cut</strong> tool</p>
<ul>
<li>Input: the previously cut half-skull</li>
<li>Create another plane</li>
<li>Position this plane so it approximates a <strong>cranial base</strong></li>
<li>Usually an oblique plane under the orbits and occipital region</li>
<li>You can adjust in 3D using transform gizmos<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1cbec1930ed7ff058de01deb23a27bc193c7220.jpeg" data-download-href="/uploads/short-url/yv1YfC6gdy7lVkBlgyTZOtnpJ5K.jpeg?dl=1" title="Screenshot 2025-12-07 085835" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1cbec1930ed7ff058de01deb23a27bc193c7220_2_517x332.jpeg" alt="Screenshot 2025-12-07 085835" data-base62-sha1="yv1YfC6gdy7lVkBlgyTZOtnpJ5K" width="517" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1cbec1930ed7ff058de01deb23a27bc193c7220_2_517x332.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1cbec1930ed7ff058de01deb23a27bc193c7220_2_775x498.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1cbec1930ed7ff058de01deb23a27bc193c7220.jpeg 2x" data-dominant-color="CCC79A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-12-07 085835</span><span class="informations">1006×647 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ad34c81c0d079a1cbc7c242d7c91b2f58266fa1.jpeg" data-download-href="/uploads/short-url/1xLtMHUXNFSueoAd2CuZdfiHawh.jpeg?dl=1" title="Screenshot 2025-12-07 085817" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ad34c81c0d079a1cbc7c242d7c91b2f58266fa1_2_517x355.jpeg" alt="Screenshot 2025-12-07 085817" data-base62-sha1="1xLtMHUXNFSueoAd2CuZdfiHawh" width="517" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ad34c81c0d079a1cbc7c242d7c91b2f58266fa1_2_517x355.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ad34c81c0d079a1cbc7c242d7c91b2f58266fa1_2_775x532.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ad34c81c0d079a1cbc7c242d7c91b2f58266fa1_2_1034x710.jpeg 2x" data-dominant-color="E9D0C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-12-07 085817</span><span class="informations">1090×750 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
<p>I plugged the resulting .ply into Endomaker (Arothron, R Studio), with a result of 939.2671ml x 2 = ~1,878.53 ml, which for a 4 year-old skull with synostosis/macrocephaly, I think is reasonable?<br>
I can play around with the parameters further, but looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00f56c2f90f13bde5d445e73a6db55899cd1ea45.jpeg" data-download-href="/uploads/short-url/8tOyLOoB3KmkShQJ0FkDo9wG9v.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00f56c2f90f13bde5d445e73a6db55899cd1ea45_2_503x375.jpeg" alt="image" data-base62-sha1="8tOyLOoB3KmkShQJ0FkDo9wG9v" width="503" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00f56c2f90f13bde5d445e73a6db55899cd1ea45_2_503x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00f56c2f90f13bde5d445e73a6db55899cd1ea45_2_754x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00f56c2f90f13bde5d445e73a6db55899cd1ea45.jpeg 2x" data-dominant-color="EAD5EA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">927×690 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #28 by @muratmaga (2025-12-08 06:32 UTC)

<p>Sounds like you figured out. Yes, just use two planes.</p>
<p>If you need more accurate estimates, then I would suggest using deformable model (or mesh) registration and estimate it from the reference ones.</p>

---

## Post #29 by @muratmaga (2025-12-09 17:52 UTC)

<p>Also, for posterity. There is now deformable model registration in <code>FastModelAlign</code> module of SlicerMorph extension. See here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="45426">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/deformable-model-registration-prototype/45426">Deformable model registration prototype</a> <a class="badge-category__wrapper " href="/c/community/biological-morphology-slicer-extension/24"><span data-category-id="24" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #F7941D;" data-parent-category-id="12" data-drop-close="true" class="badge-category --style-square --has-parent"><span class="badge-category__name">SlicerMorph</span></span></a>
    </div>
  </div>
  <blockquote>
    I have enabled deformable model registration as fourth level of registration (scaling, rigid, affine) in FastModelAlign module of SlicerMorph extension. Like ALPACA, it uses the point cloud based registration via Coherent Point Drift (CPD) algorithm. Then pointwise deformations are interpolated for every vertex. In its default mode it works quite fast. 
You can also output an interpolated grid transform (up to 256x256x256 grid size, default is 128^3) so that you can apply the resultant transform…
  </blockquote>
</aside>


---
