---
topic_id: 32323
title: "Screen Space Ambient Occlusion For Volume Rendering"
date: 2023-10-19
url: https://discourse.slicer.org/t/32323
---

# Screen-space ambient occlusion for volume rendering

**Topic ID**: 32323
**Date**: 2023-10-19
**URL**: https://discourse.slicer.org/t/screen-space-ambient-occlusion-for-volume-rendering/32323

---

## Post #1 by @LucasGandel (2023-10-19 09:16 UTC)

<p>The goal of this topic is to track the feasibility and interest for implementing SSAO for volume rendering in VTK / 3DSlicer.<br>
As highlighted by <a class="mention" href="/u/lassoan">@lassoan</a> in <a href="https://discourse.slicer.org/t/vtk-multivolume-cinematic-volume-rendering/31981/12">this post</a>, SSAO for volumes could be a game-changer especially for the recent (and outstanding) colorized volume visualization presented <a href="https://discourse.slicer.org/t/new-colorize-volume-module/32254">here</a>.</p>
<p>First tries look promising with a very simple opacity function resulting in a fully opaque representation of the volume (left: SSAO disabled; right: SSAO enabled):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0cf73e8fc1583b57721e91f4c7af8c332851067.png" alt="image" data-base62-sha1="rvG8FyNOlWduGe9TrAEK5OEfN6D" width="512" height="197"></p>
<p>More details will follow in the posts below.</p>

---

## Post #2 by @LucasGandel (2023-10-19 09:53 UTC)

<p>Quick comparison of SSAO for surface and volume.<br>
The iso surface value used for extraction corresponds to the half of the volume’s scalar range.<br>
The opacity function used for volume rendering is a ramp with value 0.0 before the half of the volume’s scalar range, and 1.0 after. No gradient function was used.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/952229858fd57d3a7b94d14598bb457d0a35ecb2.jpeg" data-download-href="/uploads/short-url/lhikMJY07LfXmA625UbX1Yx0uoq.jpeg?dl=1" title="Volume-Surface-SSAO.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/952229858fd57d3a7b94d14598bb457d0a35ecb2_2_350x375.jpeg" alt="Volume-Surface-SSAO.PNG" data-base62-sha1="lhikMJY07LfXmA625UbX1Yx0uoq" width="350" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/952229858fd57d3a7b94d14598bb457d0a35ecb2_2_350x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/952229858fd57d3a7b94d14598bb457d0a35ecb2_2_525x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/952229858fd57d3a7b94d14598bb457d0a35ecb2_2_700x750.jpeg 2x" data-dominant-color="80848B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Volume-Surface-SSAO.PNG</span><span class="informations">1205×1290 232 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Inspecting the computed SSAO textures in RenderDoc shows how sensitive to normal computation the SSAO algorithm is. While the surface is perfectly smooth, voxels appear on the volume and make it appear darker. This effect should be mitigated when using a smooth transfer function and a gradient function to improve normals.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7607c4d8797325222a715d139759f8f725d8b0d.jpeg" data-download-href="/uploads/short-url/zioEA6V24bLr4lorP5cB7q5SW6h.jpeg?dl=1" title="SSAOTextures" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7607c4d8797325222a715d139759f8f725d8b0d_2_345x141.jpeg" alt="SSAOTextures" data-base62-sha1="zioEA6V24bLr4lorP5cB7q5SW6h" width="345" height="141" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7607c4d8797325222a715d139759f8f725d8b0d_2_345x141.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7607c4d8797325222a715d139759f8f725d8b0d_2_517x211.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7607c4d8797325222a715d139759f8f725d8b0d_2_690x282.jpeg 2x" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SSAOTextures</span><span class="informations">1920×788 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2023-10-19 11:35 UTC)

<p>This is very exciting, thanks a lot for working on this!</p>
<p>You can adjust SSAO parameters (see <a href="https://github.com/PerkLab/SlicerSandbox/blob/c6e3ec60d146578c25e308dd8edc2680784aff07/Lights/Lights.py#L360">here</a> or try interactively in the Lights module in Sandbox extension) to control the darkening. Small size scale will highlight small irregularities in the surface (I think this is what we see in the renderings above). By increasing the sIze scale you can simulate drop shadow (this is what we need). Further increasing the size scale the ambient occlusion becomes so blurred that it is not useful anymore. So, I would suggest to try to tune the SSAO parameters by adjusting the size scale, similarly how it is done in Sandbox extension.</p>

---

## Post #4 by @LucasGandel (2023-10-19 12:42 UTC)

<blockquote>
<p>This is very exciting, thanks a lot for working on this!</p>
</blockquote>
<p>I’m on vacation for the next two days, I couldn’t resist… <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<blockquote>
<p>You can adjust SSAO parameters…</p>
</blockquote>
<p>Right, I confirm the effect can be mitigated by playing with the ssao parameters. (Results bellow from left to right with SSAO OFF, SSAO radius = 1, SSAO radius = 10, SSAO radius = 100).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e76c50a9cf92b6cdfa5266d48fe1e4eb1f50c75.jpeg" data-download-href="/uploads/short-url/bc7HKhDYQm8OvDKvyby5cORj2Pr.jpeg?dl=1" title="SSAO_off_r1_r10_r100.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e76c50a9cf92b6cdfa5266d48fe1e4eb1f50c75_2_690x157.jpeg" alt="SSAO_off_r1_r10_r100.PNG" data-base62-sha1="bc7HKhDYQm8OvDKvyby5cORj2Pr" width="690" height="157" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e76c50a9cf92b6cdfa5266d48fe1e4eb1f50c75_2_690x157.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e76c50a9cf92b6cdfa5266d48fe1e4eb1f50c75_2_1035x235.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e76c50a9cf92b6cdfa5266d48fe1e4eb1f50c75_2_1380x314.jpeg 2x" data-dominant-color="676D76"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SSAO_off_r1_r10_r100.PNG</span><span class="informations">1920×437 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
However the “grain” effect is present in the computed normals so I definitely think better results can be achieved with better opacity parameters:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/367a03ae6cccba2200f5b48084d159f4a7ff5f7b.png" data-download-href="/uploads/short-url/7LVch8VFCYZNb1VYqAIKJCjfkF5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/367a03ae6cccba2200f5b48084d159f4a7ff5f7b_2_162x250.png" alt="image" data-base62-sha1="7LVch8VFCYZNb1VYqAIKJCjfkF5" width="162" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/367a03ae6cccba2200f5b48084d159f4a7ff5f7b_2_162x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/367a03ae6cccba2200f5b48084d159f4a7ff5f7b_2_243x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/367a03ae6cccba2200f5b48084d159f4a7ff5f7b_2_324x500.png 2x" data-dominant-color="2C2A6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">747×1149 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Below are additional images using a wide ramp for the opacity function.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/950c69c78ef4ff38dff4e590b0b335b16aea58b0.png" alt="VolumeSSAO_transparent.drawio" data-base62-sha1="lgxJLRxSA6peyy9Uz1DBszFqgeI" width="262" height="121"></p>

---

## Post #5 by @lassoan (2023-10-19 13:23 UTC)

<p>This looks amazing!</p>
<p>If the scalar opacity transfer function is a step function then some edge artifacts are indeed often appear. Therefore, usually the scalar opacity function has a ramp-like shape and the user adjusts steepness and maximum of the ramp to show details with sufficient sharpness and clarity but to avoid highlighting irrelevant surface imperfections.</p>
<p>Can you make this avaialable somehow so that I can play with it?</p>

---

## Post #6 by @LucasGandel (2023-10-19 14:06 UTC)

<p>Thank you! I confirm I mean a step function in my first post, a ramp was used after that for the last screenshot.</p>
<p>I completely agree the best is that you give it a try as you are way more experienced than me at playing with such transfer function parameters.<br>
I’ll clean the current code (most of it is on the application side for now) and will explain the few changes required in VTK in a follow-up post (hopefully before tonight).</p>
<p>In the meantime, I tried playing a bit with the data from <a class="mention" href="/u/muratmaga">@muratmaga</a> and your new Colorize Volume module. It looks really promising, but again the rendering parameters should be optimized (this is plain VTK with default options):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba197a65d773a25edd72ee33030ad4e93ae7ca58.jpeg" data-download-href="/uploads/short-url/qyjoyFBZNSJ7HDuxe3mLpuS6Tyg.jpeg?dl=1" title="SSAO_mouse.drawio" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba197a65d773a25edd72ee33030ad4e93ae7ca58.jpeg" alt="SSAO_mouse.drawio" data-base62-sha1="qyjoyFBZNSJ7HDuxe3mLpuS6Tyg" width="690" height="223" data-dominant-color="3E5357"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SSAO_mouse.drawio</span><span class="informations">1142×370 25.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @LucasGandel (2023-10-19 14:27 UTC)

<p>As I probably won’t have time to go further before tonight, and can’t wait to see if this performs well on your side. Here is a quick way to try it:</p>
<ol>
<li>VTK changes required: <a href="https://gitlab.kitware.com/LucasGandelKitware/vtk/-/commit/586e173991b60aa6fa24dc261099f76d7cdfea70" rel="noopener nofollow ugc">This commit</a> from the volume-ssao branch</li>
<li>The following shader replacement on the mapper:</li>
</ol>
<pre><code class="lang-auto">  volume-&gt;GetProperty()-&gt;ShadeOn();

  volume-&gt;GetShaderProperty()-&gt;AddFragmentShaderReplacement("//VTK::ComputeLighting::Dec", true,
    "vec3 g_dataNormal; \n"\
    "//VTK::ComputeLighting::Dec\n",
    false);
  volume-&gt;GetShaderProperty()-&gt;AddFragmentShaderReplacement("//VTK::RenderToImage::Dec", true,
    "vec3 l_opaqueFragNormal;\n"
    "vec3 l_opaqueFragPos;\n"
    "bool l_updateDepth;\n",
    false);

  volume-&gt;GetShaderProperty()-&gt;AddFragmentShaderReplacement("//VTK::RenderToImage::Init", true,
    "\
    \n  l_opaqueFragPos = vec3(-1.0);\
    \n  l_updateDepth = true;",
    false);

  volume-&gt;GetShaderProperty()-&gt;AddFragmentShaderReplacement("//VTK::RenderToImage::Impl", true,
    "\
    \n    if(!g_skip &amp;&amp; g_srcColor.a &gt; 0.0 &amp;&amp; l_updateDepth)\
    \n      {\
    \n      l_opaqueFragPos = g_dataPos;\
    \n      l_opaqueFragNormal = g_dataNormal;\
    \n      l_updateDepth = false;\
    \n      }",
    false);


  volume-&gt;GetShaderProperty()-&gt;AddFragmentShaderReplacement("//VTK::RenderToImage::Exit", true,
    "\
    \n  if (l_opaqueFragPos == vec3(-1.0))\
    \n    {\
\n gl_FragDepth = 1.0; \
\n gl_FragData[1] = gl_FragData[1]; \
    \n    }\
    \n  else\
    \n    {\
    \n    vec4 depthValue = in_projectionMatrix * in_modelViewMatrix *\
    \n                      in_volumeMatrix[0] * in_textureDatasetMatrix[0] *\
    \n                      vec4(l_opaqueFragPos, 1.0);\
    \n    depthValue /= depthValue.w;\
    \n    gl_FragDepth = 0.5 * (gl_DepthRange.far - gl_DepthRange.near) * depthValue.z + 0.5 * (gl_DepthRange.far + gl_DepthRange.near);\
    \n    gl_FragData[1] = in_modelViewMatrix * in_volumeMatrix[0] * in_textureDatasetMatrix[0] * vec4(l_opaqueFragPos, 1.0);\
    \n    gl_FragData[2] = vec4(l_opaqueFragNormal, 0.0);\
    \n    }",
    false);
</code></pre>
<p>Important:<br>
Shading must be turned ON otherwise the shader fails to compile. Other non-default options have not been tested.<br>
The VTK commit above works around a problem with FBOs when the SSAO pass is activated, by commenting the depth buffer blit that is required for surfaces to occlude the volume. This should be fixed later.</p>

---

## Post #8 by @lassoan (2023-10-19 14:29 UTC)

<p>Awesome, thank you, I give it a try and post the results here!</p>

---

## Post #9 by @LucasGandel (2023-10-24 19:25 UTC)

<p>The last line of the shader replacement above is wrong, normals must be normalized (which was causing the artefacts in the normal texture screenshot above). After replacing the last line with  <code>gl_FragData[2] = vec4(normalize(l_opaqueFragNormal), 0.0);\</code>, the SSAO texture for volumes looks very similar to the one for surfaces<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f008f01593472960f7c0583c34c81841cf4ba960.jpeg" data-download-href="/uploads/short-url/yfrK0HCZzfo3vJ72u9SO89NQcww.jpeg?dl=1" title="SSAO_mouse.drawio" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f008f01593472960f7c0583c34c81841cf4ba960_2_664x500.jpeg" alt="SSAO_mouse.drawio" data-base62-sha1="yfrK0HCZzfo3vJ72u9SO89NQcww" width="664" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f008f01593472960f7c0583c34c81841cf4ba960_2_664x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f008f01593472960f7c0583c34c81841cf4ba960_2_996x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f008f01593472960f7c0583c34c81841cf4ba960_2_1328x1000.jpeg 2x" data-dominant-color="A0A9B0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SSAO_mouse.drawio</span><span class="informations">1920×1444 85.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There is possibly one remaining visual artefact between the opaque voxels and the background. But I guess this is because we write the depth of any voxel that has opacity greater than 0, using a configurable threshold could address this.</p>

---

## Post #10 by @LucasGandel (2023-10-24 19:34 UTC)

<p>Interesting effect with high transparency: the depth is written for any voxel that is not fully transparent, but the corresponding color is barely visible. It results in a kind of shell:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7f48dc72324918f7eb41556b24f34611e0bf6ce.jpeg" data-download-href="/uploads/short-url/swSYbBKowZYiTZ2x2DGnCVZA3Om.jpeg?dl=1" title="SSAO_mouse.drawio (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7f48dc72324918f7eb41556b24f34611e0bf6ce_2_690x223.jpeg" alt="SSAO_mouse.drawio (1)" data-base62-sha1="swSYbBKowZYiTZ2x2DGnCVZA3Om" width="690" height="223" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7f48dc72324918f7eb41556b24f34611e0bf6ce_2_690x223.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7f48dc72324918f7eb41556b24f34611e0bf6ce_2_1035x334.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7f48dc72324918f7eb41556b24f34611e0bf6ce_2_1380x446.jpeg 2x" data-dominant-color="324757"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SSAO_mouse.drawio (1)</span><span class="informations">1812×586 28 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @lassoan (2023-10-24 20:43 UTC)

<p>This looks amazing!</p>
<p>I’ve been trying to reproduce this, but I don’t see any difference when I apply the shader replacementes and your VTK fix. Activating SSAO in the renderer (as I do it for surface rendering) has an effect on surface rendering, but not on volume rendering.</p>
<p>Is there any extra step needed to activate this?</p>
<p>Is <code>gl_FragData[1] = gl_FragData[1];</code> line intentional?</p>
<p><a class="mention" href="/u/pieper">@pieper</a> could you give it a try, too?</p>
<p>I’m trying to use this code snippet to activate this in Slicer:</p>
<pre><code class="lang-python">vrDisplayNode = slicer.util.getNodesByClass('vtkMRMLGPURayCastVolumeRenderingDisplayNode')[0]
shaderPropertyNode = vrDisplayNode.GetOrCreateShaderPropertyNode(slicer.mrmlScene)
shaderProperty = shaderPropertyNode.GetShaderProperty()

shaderProperty.ClearAllFragmentShaderReplacements()

shaderProperty.AddFragmentShaderReplacement("//VTK::ComputeLighting::Dec", True,
    """
    vec3 g_dataNormal;
    //VTK::ComputeLighting::Dec
    """, False)
shaderProperty.AddFragmentShaderReplacement("//VTK::RenderToImage::Dec", True,
    """
    vec3 l_opaqueFragNormal;
    vec3 l_opaqueFragPos;
    bool l_updateDepth;
    """, False)
shaderProperty.AddFragmentShaderReplacement("//VTK::RenderToImage::Init", True,
    """
    l_opaqueFragPos = vec3(-1.0);
    l_updateDepth = true;
    """, False)
shaderProperty.AddFragmentShaderReplacement("//VTK::RenderToImage::Impl", True,
    """
    if(!g_skip &amp;&amp; g_srcColor.a &gt; 0.0 &amp;&amp; l_updateDepth)
        {
        l_opaqueFragPos = g_dataPos;
        l_opaqueFragNormal = g_dataNormal;
        l_updateDepth = false;
        }
    """, False)
shaderProperty.AddFragmentShaderReplacement("//VTK::RenderToImage::Exit", True,
    """
    if (l_opaqueFragPos == vec3(-1.0))
        {
        gl_FragDepth = 1.0;
        gl_FragData[1] = gl_FragData[1];
        }
    else
        {
        vec4 depthValue = in_projectionMatrix * in_modelViewMatrix *
            in_volumeMatrix[0] * in_textureDatasetMatrix[0] *
            vec4(l_opaqueFragPos, 1.0);
        depthValue /= depthValue.w;
        gl_FragDepth = 0.5 * (gl_DepthRange.far - gl_DepthRange.near) * depthValue.z + 0.5 * (gl_DepthRange.far + gl_DepthRange.near);
        gl_FragData[1] = in_modelViewMatrix * in_volumeMatrix[0] * in_textureDatasetMatrix[0] * vec4(l_opaqueFragPos, 1.0);
        gl_FragData[2] = vec4(normalize(l_opaqueFragNormal), 0.0);
        }
""", False)
</code></pre>

---

## Post #12 by @pieper (2023-10-24 21:15 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="32323">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> could you give it a try, too?</p>
</blockquote>
</aside>
<p>No, I’m not seeing anything either.</p>

---

## Post #13 by @LucasGandel (2023-10-25 10:01 UTC)

<p>Thank you both for trying, and sorry for the inconvenience. I just had a quick look (thank you for sharing the code to run in Slicer) and it was a bit tricky <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> The Lights module enables SSAO directly using the API of the renderer, which internally only enables the opaque pass in the SSAO pass (see <a href="https://gitlab.kitware.com/vtk/vtk/-/blob/master/Rendering/OpenGL2/vtkOpenGLRenderer.cxx#L503" rel="noopener nofollow ugc">here</a>).  The solution is to either fix VTK to use a RenderStepPass instead of an opaque pass only, or to this directly in the Lights module by managing the renderer pass instead of using the SSAO public API.<br>
<a href="https://drive.google.com/file/d/1cU-KaIJLdaVATII4GtViQ5wLgxziR28n/view?usp=sharing" rel="noopener nofollow ugc">Here</a> is a modified version of Lights.py that implements the second approach (it was faster as this is what I used in my VTK based example).</p>

---

## Post #14 by @cpinter (2023-10-25 11:12 UTC)

<p>Wow, I thought the opaque-only behavior was a limitation. <a class="mention" href="/u/lucasgandel">@LucasGandel</a> Thanks a lot for the explanation and the change in the Lights module! I think we should just update the module in SlicerSandbox as suggested. <a class="mention" href="/u/lassoan">@lassoan</a> if you agree I can do it after a bit of testing. Thank you!</p>

---

## Post #15 by @lassoan (2023-10-25 11:52 UTC)

<p>Yes, please update the list guts module and send a pull request. Could you test if there are any disadvantages of using the new method (speed, artifacts in some special cases,…) because if there are then it could make sense to have an option to use the old or the new method. Check how things work with semi-transparent models, mix of surface and volume rendering, various volume rendering settings.</p>

---

## Post #16 by @LucasGandel (2023-10-25 11:57 UTC)

<p>Wait, I agree the opaque-only behavior should be a limitation, I think without the VTK change (hack) referenced here it can’t work (the volume disappears). And as pointed by Andras, transparent actors might be impacted too.</p>
<p>In any case, the VTK hack is not an option, so while working on the true fix, we should consider testing the transparent pass too. Not sure when/if I can find time to do it, but always happy to help</p>

---

## Post #17 by @cpinter (2023-10-25 12:03 UTC)

<aside class="quote no-group" data-username="LucasGandel" data-post="16" data-topic="32323">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lucasgandel/48/18202_2.png" class="avatar"> LucasGandel:</div>
<blockquote>
<p>without the VTK change (hack) referenced here it can’t work</p>
</blockquote>
</aside>
<p>I may be overlooking something, but I don’t know what is this hack. You referenced a <a href="https://gitlab.kitware.com/vtk/vtk/-/blob/master/Rendering/OpenGL2/vtkOpenGLRenderer.cxx#L503">line in the code</a> above, that’s all I see. What is the change needed so that the modified Lights.py works with semi-transparent models with SSAO?</p>
<p>I agree a fix in VTK would be nice, but VTK changes take their time so if it’s possible I’d like to use an intermediate solution in the meantime.</p>
<p>Let me know how I can help. Thanks!</p>

---

## Post #18 by @LucasGandel (2023-10-25 12:13 UTC)

<p>Sorry for not being clear, the solution is indeed spread across every posts above, but mainly <a href="https://discourse.slicer.org/t/screen-space-ambient-occlusion-for-volume-rendering/32323/7">this post is</a> what is required. It references this <a href="https://gitlab.kitware.com/LucasGandelKitware/vtk/-/commit/586e173991b60aa6fa24dc261099f76d7cdfea70" rel="noopener nofollow ugc">VTK commit</a>  which is a huge hack. It remove support for occluding volume rendering with surface as it wipes out the depth buffer to workaround a bug caused by using the volume pass in the SSAO pass. This is why I say that changing the opaque pass with vtkRenderStepPass in the SSAO pass won’t work if you don’t use this hack.</p>
<p>(I hope this helps, I will try to post later tonight the action that must be taken to replace this VTK hack with a clean commit )</p>

---

## Post #19 by @cpinter (2023-10-25 12:26 UTC)

<p>Thanks! I saw that commit, but it is about volume rendering. And the Lights module affects surface rendering, so that commit should not be needed right? Just to be clearer on my side too, I’m interested in supporting SSAO for semi-transparent models for rendering polydata.</p>

---

## Post #20 by @lassoan (2023-10-25 12:54 UTC)

<p>Lights module is for all rendering. Only the SSAO feature was limited to surface rendering.</p>
<p>We can make changes in Slicer’s VTK very quickly and easily, but we also need to get the all the changes integrated into VTK proper, too, to prevent divergence of Slicer’s VTK from upstream VTK.</p>
<p>Until <a class="mention" href="/u/lucasgandel">@LucasGandel</a> has a chance to come up with a full fix of the VTK bug, we can only experiment with this in local developer builds. Once the proper fix is ready we can integrate it into Slicer’s VTK immediately and send a merge request to VTK upstream.</p>
<p>We can add the shader replacements and transparent SSAO rendering step to Lights module for now. When everything is confirmed to be working well, then we’ll move all the changes to their proper places:</p>
<ul>
<li>VTK: add a transparent SSAO flag to the renderer; maybe add the shader code for volume rendering SSAO</li>
<li>CTK: add SSAO options to ctkVTKAbstractView</li>
<li>Slicer core: add shader replacements to Volume Rendering displayable manager (if not added to VTK)</li>
</ul>

---

## Post #21 by @LucasGandel (2023-10-25 13:35 UTC)

<p>Thanks for the clarification, I now understand that you need SSAO for semi-transparent surface actors, not volumes. This is yet another story <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> which can be partially solved with the information in this topic.<br>
Similar to what is required for volumes, you will indeed need to change the SSAO pass in the Lights.py script (or VTK later) so that it uses vtkRenderStepPass instead of the opaque pass. As long as you don’t render volume, you don’t need/are not impacted by the VTK hack.<br>
However, similar hack/commit might be required to fully support SSAO for transparent surface actors: semi-transparent actors do not write to the depth buffer, this must be changed in a similar way as it was done for volumes <a href="https://gitlab.kitware.com/LucasGandelKitware/vtk/-/commit/586e173991b60aa6fa24dc261099f76d7cdfea70#632b3677f9257d77462fa7b0ef618b50511becae_53_52" rel="noopener nofollow ugc">here</a>.</p>
<p>For now I will focus on implementing the proper fix for volumes in VTK. I’ll see to give a try to transparent actors in the meantime</p>

---

## Post #22 by @cpinter (2023-10-25 13:39 UTC)

<p>Thank you so much <a class="mention" href="/u/lucasgandel">@LucasGandel</a> for bearing with me and answering corner case questions <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> I understand now, that it is about the depth buffer, and profound changes would be needed to do this fix. OK let’s put this aside for now, I appreciate you helping me understand the root cause!</p>

---

## Post #23 by @lassoan (2023-10-25 14:48 UTC)

<p>Yay, with the Lights module change it all works in Slicer:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7147013c78e32618150708ee4d5f3dd8ef88e493.jpeg" data-download-href="/uploads/short-url/ga652xjtS1QR3ebCCyuAClvDnaP.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7147013c78e32618150708ee4d5f3dd8ef88e493_2_418x500.jpeg" alt="image" data-base62-sha1="ga652xjtS1QR3ebCCyuAClvDnaP" width="418" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7147013c78e32618150708ee4d5f3dd8ef88e493_2_418x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7147013c78e32618150708ee4d5f3dd8ef88e493_2_627x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7147013c78e32618150708ee4d5f3dd8ef88e493_2_836x1000.jpeg 2x" data-dominant-color="7B6E7A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1372×1638 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/547b4aa84e1f8b1a0e4d877772609ad567689573.jpeg" data-download-href="/uploads/short-url/c3mg27VWlHF3lswUWyMDfVk8Jvt.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/547b4aa84e1f8b1a0e4d877772609ad567689573_2_418x500.jpeg" alt="image" data-base62-sha1="c3mg27VWlHF3lswUWyMDfVk8Jvt" width="418" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/547b4aa84e1f8b1a0e4d877772609ad567689573_2_418x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/547b4aa84e1f8b1a0e4d877772609ad567689573_2_627x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/547b4aa84e1f8b1a0e4d877772609ad567689573_2_836x1000.jpeg 2x" data-dominant-color="7D656D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1372×1638 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/lucasgandel">@LucasGandel</a> a few things about the shader:</p>
<ol>
<li>We need to make the opacity threshold (originally 0.5, here 0.25) configurable here, as &gt;0.0 makes very transparent pieces to cast shadow that is not optimal:</li>
</ol>
<pre><code class="lang-auto">if(!g_skip &amp;&amp; g_srcColor.a &gt; 0.25 &amp;&amp; l_updateDepth)
</code></pre>
<ol start="2">
<li>This line looks suspicious:</li>
</ol>
<pre><code class="lang-auto">gl_FragData[1] = gl_FragData[1];
</code></pre>

---

## Post #24 by @lassoan (2023-10-25 15:50 UTC)

<p>I’ve submitted a pull request for the Lights module that takes care of setting up everything (enable SSAO rendering pass for transparent rendering, applies shader replacements, allows customizing the opacity threshold):</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/PerkLab/SlicerSandbox/pull/23">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerSandbox/pull/23" target="_blank" rel="noopener">github.com/PerkLab/SlicerSandbox</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/PerkLab/SlicerSandbox/pull/23" target="_blank" rel="noopener">Add experimental option for SSAO for volume rendering</a>
      </h4>

    <div class="branches">
      <code>PerkLab:master</code> ← <code>PerkLab:vr-ssao</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-10-25" data-time="15:46:36" data-timezone="UTC">03:46PM - 25 Oct 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 185 additions and 34 deletions">
          <a href="https://github.com/PerkLab/SlicerSandbox/pull/23/files" target="_blank" rel="noopener">
            <span class="added">+185</span>
            <span class="removed">-34</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">requires VTK fix described here:
https://discourse.slicer.org/t/screen-space-am<span class="show-more-container"><a href="https://github.com/PerkLab/SlicerSandbox/pull/23" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">bient-occlusion-for-volume-rendering/32323/18</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I’ll wait for a proper VTK fix from <a class="mention" href="/u/lucasgandel">@LucasGandel</a> that we can merge into Slicer’s VTK and then I’ll merge the pull request and the feature will be available for everyone.</p>
<p>Until then the feature is only available for developers who apply the VTK fix locally and use this branch of the Sandbox.</p>

---

## Post #25 by @LucasGandel (2023-10-25 16:12 UTC)

<p>This is fantastic <a class="mention" href="/u/lassoan">@lassoan</a>, thank you for trying and for creating the branch.<br>
So I understand that there is interest for it, and that it should be finalized at some point. If yes, I will now focus on the fix for volume occlusion, the rest of the change can be integrated with mapper options or volume properties.<br>
I completely agree with your points:</p>
<ol>
<li>A configurable threshold makes sense as it can highlights different structures (in addition to prevent weird effect with almost fully transparent pixels when 0.0 is used as you said). I started work in this direction and I think g_fragColor.a must be used to take the opacity transfer function instead of g_srcColor.a (at least it makes a difference for RGBA columes I think)</li>
<li>Right, this line is non-sense. I just added it because the RenderDoc frame debugger needs anything to be written to the texture, but those fragments are not used in the final blending as no depth is associated to them. This needs to be fixed when mixing volumes and surface to ensure existing fragments are not overridden</li>
</ol>

---

## Post #26 by @lassoan (2023-10-25 16:17 UTC)

<p>An overview of how much improvement we achieved compared to the baseline (what was possible a few weeks ago) in Slicer’s volume rendering with introducing colorized rendering and SSAO:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f33eede8d3e6d6f913adf32a7698b598e4aa7a7f.jpeg" data-download-href="/uploads/short-url/yHQQKskeUFp4kEBvfdL6TvwK8Nh.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f33eede8d3e6d6f913adf32a7698b598e4aa7a7f_2_690x277.jpeg" alt="image" data-base62-sha1="yHQQKskeUFp4kEBvfdL6TvwK8Nh" width="690" height="277" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f33eede8d3e6d6f913adf32a7698b598e4aa7a7f_2_690x277.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f33eede8d3e6d6f913adf32a7698b598e4aa7a7f_2_1035x415.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f33eede8d3e6d6f913adf32a7698b598e4aa7a7f_2_1380x554.jpeg 2x" data-dominant-color="908299"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×772 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>With more opaque rendering:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a60ec48860e35815190ad881fb30bed42748fa4.jpeg" data-download-href="/uploads/short-url/3Lm4o0AAhi0Xxn3QdPy8Gk2cbbe.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a60ec48860e35815190ad881fb30bed42748fa4_2_690x417.jpeg" alt="image" data-base62-sha1="3Lm4o0AAhi0Xxn3QdPy8Gk2cbbe" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a60ec48860e35815190ad881fb30bed42748fa4_2_690x417.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a60ec48860e35815190ad881fb30bed42748fa4_2_1035x625.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a60ec48860e35815190ad881fb30bed42748fa4_2_1380x834.jpeg 2x" data-dominant-color="958590"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1161 217 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #27 by @LucasGandel (2023-10-25 16:22 UTC)

<p>This is amazing, thanks for sharing!</p>

---

## Post #28 by @lassoan (2023-10-25 18:25 UTC)

<p>Here is a video, that shows details of muscles:</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06563a108db41445849da7cf2fdcf7ea9266f083.mp4">
  </div><p></p>

---

## Post #29 by @jay1987 (2023-10-26 03:02 UTC)

<p>it’s amazing lassoan,can you give us a simple tutorial on how to use slicer to achieve the effect you have?</p>

---

## Post #30 by @lassoan (2023-10-26 03:06 UTC)

<p><a class="mention" href="/u/lucasgandel">@LucasGandel</a> needs to do some cleanup of a VTK fix, which may take some time (hopefully not more than a few days?) and then we can make the ambient shading available for everyone. We’ll post updates on this thread.</p>
<p>If you want to access this feature earlier then you ned to build Slicer from source code and apply the VTK fix locally.</p>

---

## Post #31 by @jay1987 (2023-10-26 03:13 UTC)

<p>thank you lassoan , I will try to hack into vtk follow <a class="mention" href="/u/lucasgandel">@LucasGandel</a> vtk’s thread commit ,the rendering looks amazing!</p>

---

## Post #32 by @LucasGandel (2023-10-27 06:30 UTC)

<p>Yesterday I could find the fix to bring back volume depth occlusion. The required change will be done in the coming days.  I have a project to handle the integration of the depth mask change in VTK so I will start with that. For this we will use the vtkOpenActor::DepthMaskOverride information key.<br>
<a class="mention" href="/u/lassoan">@lassoan</a> Is it possible to set the information key from python? like <a href="https://gitlab.kitware.com/vtk/vtk/-/blob/master/Rendering/OpenGL2/vtkDepthPeelingPass.cxx#L475" rel="noopener nofollow ugc">this</a></p>

---

## Post #33 by @lassoan (2023-10-27 22:38 UTC)

<p>You can set those information keys in Slicer in Python like this:</p>
<pre><code class="lang-python">threeDViewWidget = slicer.app.layoutManager().threeDWidget(0)
vrDisplayableManager = threeDViewWidget.threeDView().displayableManagerByClassName("vtkMRMLVolumeRenderingDisplayableManager")

volumeNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLVolumeNode')

volumeActor = vrDisplayableManager.GetVolumeActor(volumeNode)
info = volumeActor.GetPropertyKeys()
if not info:
    info = vtk.vtkInformation()
    volumeActor.SetPropertyKeys(info)
info.Set(vtk.vtkOpenGLActor.GLDepthMaskOverride(), 1)
</code></pre>
<p>Would it be possible to set enable depth mask override by default to avoid the need for such low-level manipulations? None of the other volume rendering techniques require such calls.</p>
<p>If there are some negative side-effects of enabling depth mask override in some cases then making it optional could make sense, but then there should be more convenient API, for example a method in <code>vtkVolume</code>.</p>

---

## Post #34 by @LucasGandel (2023-10-30 07:14 UTC)

<p>Perfect, thanks. Eventually it will be enabled by default by the ssao pass so it won’t be required anymore. Same for the shaders replacement and modification of the ssao pass detp texture format. But for now, all the VTK hack from my volume-ssao branch can be replaced with:</p>
<ol>
<li><a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/10642" rel="noopener nofollow ugc">VTK!10642</a> makes it possible to use the <a href="https://discourse.slicer.org/t/screen-space-ambient-occlusion-for-volume-rendering/32323/33">GLDepthMaskOverride key</a> to write to the depth buffer.</li>
<li><a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/10644" rel="noopener nofollow ugc">VTK!10644</a> allows for calling <code>ssaoPass-&gt;SetDepthFormat(vtkTextureObject::Fixed32);</code> to fix the issue with volume depth occlusion</li>
<li><a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/10645" rel="noopener nofollow ugc">VTK!10645</a> allows to add the following shader replacement to fix the previously hardcoded one:</li>
</ol>
<pre><code class="lang-auto">  volume-&gt;GetShaderProperty()-&gt;AddFragmentShaderReplacement("//VTK::ComputeLighting::Exit", false,
    "\n  //VTK::ComputeLighting::Exit\
     \n  g_dataNormal = -shading_gradient.xyz;",
    false);
</code></pre>
<p>I will follow up as soon as I can, but the change in the ssao pass to make this automatic should be ready by next week</p>

---

## Post #35 by @lassoan (2023-10-30 11:48 UTC)

<p>Thank you for working on this and for clarifying the roadmap. When I reviewed the VTK merge requests I was not sure if we’ll need all the low-level API calls to activate this feature, but it’s great to hear that it’ll be all seamlessly integrated into the existing SSAO feature! I’ll test this and let you know if it all works the same way as before.</p>

---

## Post #36 by @lassoan (2023-11-17 06:15 UTC)

<p>I’ve tried to apply all the VTK changes, enabled GLDepthMaskOverride, changed depth format, and added the shader replacement. Unfortunately, the volume disappears and this message is displayed:</p>
<pre><code class="lang-auto">[VTK] 0(350) : error C1503: undefined variable "g_dataNormal"
[VTK] Shader failed to compile
</code></pre>
<p>Where g_dataNormal is defined?</p>

---

## Post #37 by @LucasGandel (2023-11-17 17:03 UTC)

<p>Thanks a lot for following up on this. To answer your question, this is defined in the shader replacement that you must add on the application side for now. See the following code from previous comments:</p>
<pre><code class="lang-auto">vtkShaderProgram::Substitute(fragmentShader, "//VTK::ComputeLighting::Dec",
      "vec3 g_dataNormal; \n"
      "//VTK::ComputeLighting::Dec\n",
      false);
</code></pre>
<p>However, this won’t be required anymore when everything gets moved to the SSAO pass. I am almost done with that, still need to write a test and open an MR on VTK, but you can access the code on my updated <a href="https://gitlab.kitware.com/LucasGandelKitware/vtk/-/tree/volume-ssao?ref_type=heads" rel="noopener nofollow ugc">volume-ssao branch</a>.<br>
The branch has been rebased on master and only <a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/10644" rel="noopener nofollow ugc">VTK!10644</a> has been cherry-picked because it did not make it yet into VTK ( <a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/10642" rel="noopener nofollow ugc">VTK!10642</a> and <a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/10645" rel="noopener nofollow ugc">VTK!10645</a> have been merged).</p>
<p>The only thing that is still required on the application side if using my volume-ssao branch is to set the depth format on the ssao pass: <code>ssao-&gt;SetDepthFormat(vtkTextureObject::Fixed32);</code>.</p>
<p>Let me know if something is still missing after that, setting the vtkRenderStepPass as a delegate of the SSAO pass is still required on the application too as I did not change the vtkRenderer SSAO pass.</p>

---

## Post #38 by @LucasGandel (2023-11-24 12:45 UTC)

<p>All the low level pending MRs have been merged into VTK and <a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/10725" rel="noopener nofollow ugc">VTK!10725</a> handles shader replacements in the SSAO pass and is ready for reviews <img src="https://emoji.discourse-cdn.com/twitter/tada.png?v=12" title=":tada:" class="emoji" alt=":tada:" loading="lazy" width="20" height="20"></p>
<p>I plan to write a post on the Kitware blog to present the approach. If anyone wants to provide data or screenshots, that would be much appreciated. Maybe a second blog post presenting the same at an higher level, with the colorized volume approach, also makes sense, if anyone wants to co-author that. I really think we should communicate more on this now that it is kind of ready. <a class="mention" href="/u/lassoan">@lassoan</a> WDYT?</p>

---

## Post #39 by @lassoan (2023-11-24 14:33 UTC)

<p>Great, thank you very much for all your work on this. I’ll test this and provide data and screenshots. I would also be happy to help with a blog post and probably write a short paper that can be cited, because I think this (along with colorizing volume using segmentation) may be a breakthrough in utilizing data that all the new “AI” segmentation tools provide.</p>

---

## Post #40 by @rbumm (2023-11-24 16:07 UTC)

<p>This is fascinating. Is there a way to test this feature ?</p>

---

## Post #41 by @lassoan (2023-11-24 19:16 UTC)

<p>We’ll need a week or so to integrate and test all the VTK updates and then add GUI to Slicer to configure it.</p>

---

## Post #42 by @muratmaga (2023-11-25 06:01 UTC)

<p>I assume this is not going to get into the current release being cut (5.6)?</p>

---

## Post #43 by @jcfr (2023-11-25 06:12 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="42" data-topic="32323" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I assume this is not going to get into the current release being cut (5.6)?</p>
</blockquote>
</aside>
<p>Earlier today, <a class="mention" href="/u/lucasgandel">@LucasGandel</a>  and I reviewed the list of VTK changes that we would need to backport to our <code>Slicer/VTK</code> fork, I am currently assessing if integrating these into the release is sensible.</p>

---

## Post #44 by @LucasGandel (2023-12-01 07:13 UTC)

<p>The final change (<a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/10725" rel="noopener nofollow ugc">VTK!10725</a>) has been merged! <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=12" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"><br>
This makes SSAO available for volumes, but not with the vtkRenderer::UseSSAOOn() function, you must explicitly set the render passes like this:</p>
<pre><code class="lang-auto"> // Render passes setup
  vtkNew&lt;vtkRenderStepsPass&gt; basicPasses;
  vtkNew&lt;vtkSSAOPass&gt; ssao;
  ssao-&gt;SetRadius(40);
  ssao-&gt;SetKernelSize(128);
  ssao-&gt;SetBias(0.01);
  ssao-&gt;BlurOn();
  // The depth format must be Fixed32 for the volume mapper to successfully copy the depth texture
  ssao-&gt;SetDepthFormat(vtkTextureObject::Fixed32);
  ssao-&gt;SetVolumeOpacityThreshold(0.95);
  ssao-&gt;SetDelegatePass(basicPasses);

  renderer-&gt;SetPass(ssao);
</code></pre>
<p>I’ll start working on screenshots and will try to kick off a doc for technical writing.</p>

---

## Post #45 by @muratmaga (2023-12-09 02:30 UTC)

<p>Is this available for preview versions?</p>

---

## Post #46 by @LucasGandel (2023-12-11 15:52 UTC)

<p>I don’t think so. <a class="mention" href="/u/jcfr">@jcfr</a> can you make sure to backport the <a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/10725/commits" rel="noopener nofollow ugc">commits from VTK!10725</a> ? Then <a class="mention" href="/u/lassoan">@lassoan</a>’s MR on the sandbox module needs modifications to only include the setup of the render passes as done in my last comment.</p>

---

## Post #47 by @lassoan (2023-12-11 16:22 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> let me know when all the required VTK commits are in. Then I’ll update the Sandbox module according to <a class="mention" href="/u/lucasgandel">@LucasGandel</a> latest comment (<a href="https://discourse.slicer.org/t/screen-space-ambient-occlusion-for-volume-rendering/32323/44" class="inline-onebox">Screen-space ambient occlusion for volume rendering - #44 by LucasGandel</a>).</p>

---

## Post #48 by @muratmaga (2023-12-13 06:11 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="43" data-topic="32323">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Earlier today, <a class="mention" href="/u/lucasgandel">@LucasGandel</a> and I reviewed the list of VTK changes that we would need to backport to our <code>Slicer/VTK</code> fork, I am currently assessing if integrating these into the release is sensible.</p>
</blockquote>
</aside>
<p>Did this make into the patch? I am not seeing it listed under the 5.6.1 release notes.</p>

---

## Post #49 by @jcfr (2023-12-13 06:31 UTC)

<blockquote>
<p>Did this make into the patch? I am not seeing it listed under the 5.6.1 release notes.</p>
</blockquote>
<p>These will be integrated when we update the version of VTK used in Slicer Preview.</p>

---

## Post #50 by @LucasGandel (2023-12-19 16:34 UTC)

<p>A first post is now available: <a href="https://www.kitware.com/screen-space-ambient-occlusion-for-volumes/" rel="noopener nofollow ugc">https://www.kitware.com/screen-space-ambient-occlusion-for-volumes/</a></p>
<p>I’m happy to help writing, reviewing, or providing screenshot if you want to communicate further once this is in Slicer.</p>
<p>I’m also considering revisiting the approach for almost fully transparent volume, as I think the ambient occlusion contribution should be multiplied with the fragment opacity</p>

---

## Post #51 by @lassoan (2024-01-02 18:10 UTC)

<p>A post was split to a new topic: <a href="/t/improve-ambient-occlusion-in-volume-rendering/33590">Improve ambient occlusion in volume rendering</a></p>

---
