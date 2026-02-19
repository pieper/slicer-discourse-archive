---
topic_id: 37410
title: "Adding Shadow Function Throws Error"
date: 2024-07-16
url: https://discourse.slicer.org/t/37410
---

# Adding Shadow function throws error

**Topic ID**: 37410
**Date**: 2024-07-16
**URL**: https://discourse.slicer.org/t/adding-shadow-function-throws-error/37410

---

## Post #1 by @Marleen_Sinsel (2024-07-16 20:47 UTC)

<p>We have created an extension with Total Segmentator for Slicer (5.6.1), in which there is a function to draw the silhouette around objects and in another function a shadow should be added. We get the error below, which only occurs after the function that adds the shadow.<br>
When you press the button to draw the silhouette, the silhouette is drawn around the 3D cube in the slicer and no longer around the selected objects. Even if you activate the silhouette first and then the shadow, the same thing happens. Without the shadow function the silhouette function works perfectly. We do not understand how the shadow and silhouette functions are related and what is going wrong.<br>
The error message also says something about vtkTransformPolyData which we do not use, we use vtkPolyDataSilhouette() in the silhouette function and our shadow function looks like this:</p>
<p>the error message we get:</p>
<pre><code class="lang-auto">[VTK] Input port 0 of algorithm vtkTransformPolyDataFilter (000001AE289620D0) has 0 connections but is not optional.
[VTK] Input port 0 of algorithm vtkTransformPolyDataFilter (000001AE289620D0) has 0 connections but is not optional.
[VTK] Input port 0 of algorithm vtkTransformPolyDataFilter (000001AE28961EF0) has 0 connections but is not optional.
[VTK] Input port 0 of algorithm vtkTransformPolyDataFilter (000001AE28961EF0) has 0 connections but is not optional.
[VTK] 1: #version 150
[VTK] 2: #ifdef GL_ES
[VTK] 3: #ifdef GL_FRAGMENT_PRECISION_HIGH
[VTK] 4: precision highp float;
[VTK] 5: precision highp sampler2D;
[VTK] 6: precision highp sampler3D;
[VTK] 7: #else
[VTK] 8: precision mediump float;
[VTK] 9: precision mediump sampler2D;
[VTK] 10: precision mediump sampler3D;
[VTK] 11: #endif
[VTK] 12: #define texelFetchBuffer texelFetch
[VTK] 13: #define texture1D texture
[VTK] 14: #define texture2D texture
[VTK] 15: #define texture3D texture
[VTK] 16: #else // GL_ES
[VTK] 17: #define highp
[VTK] 18: #define mediump
[VTK] 19: #define lowp
[VTK] 20: #if __VERSION__ == 150
[VTK] 21: #define texelFetchBuffer texelFetch
[VTK] 22: #define texture1D texture
[VTK] 23: #define texture2D texture
[VTK] 24: #define texture3D texture
[VTK] 25: #endif
[VTK] 26: #endif // GL_ES
[VTK] 27: #define varying in
[VTK] 28: 
[VTK] 29: 
[VTK] 30: /*=========================================================================
[VTK] 31: 
[VTK] 32:   Program:   Visualization Toolkit
[VTK] 33:   Module:    vtkPolyDataFS.glsl
[VTK] 34: 
[VTK] 35:   Copyright (c) Ken Martin, Will Schroeder, Bill Lorensen
[VTK] 36:   All rights reserved.
[VTK] 37:   See Copyright.txt or http://www.kitware.com/Copyright.htm for details.
[VTK] 38: 
[VTK] 39:      This software is distributed WITHOUT ANY WARRANTY; without even
[VTK] 40:      the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
[VTK] 41:      PURPOSE.  See the above copyright notice for more information.
[VTK] 42: 
[VTK] 43: =========================================================================*/
[VTK] 44: // Template for the polydata mappers fragment shader
[VTK] 45: 
[VTK] 46: uniform int PrimitiveIDOffset;
[VTK] 47: 
[VTK] 48: 
[VTK] 49: 
[VTK] 50: // VC position of this fragment
[VTK] 51: //VTK::PositionVC::Dec
[VTK] 52: 
[VTK] 53: // Camera prop
[VTK] 54: uniform int cameraParallel;
[VTK] 55: 
[VTK] 56: 
[VTK] 57: // optional color passed in from the vertex shader, vertexColor
[VTK] 58: uniform float ambientIntensity; // the material ambient
[VTK] 59: uniform float diffuseIntensity; // the material diffuse
[VTK] 60: uniform float opacityUniform; // the fragment opacity
[VTK] 61: uniform vec3 ambientColorUniform; // ambient color
[VTK] 62: uniform vec3 diffuseColorUniform; // diffuse color
[VTK] 63: 
[VTK] 64: 
[VTK] 65: // optional surface normal declaration
[VTK] 66: //VTK::Normal::Dec
[VTK] 67: 
[VTK] 68: // extra lighting parameters
[VTK] 69: uniform vec3 lightColor0;
[VTK] 70:   uniform vec3 lightDirectionVC0; // normalized
[VTK] 71: uniform vec3 lightColor1;
[VTK] 72:   uniform vec3 lightDirectionVC1; // normalized
[VTK] 73: 
[VTK] 74: uniform float depthC;
[VTK] 75: vec2 calcShadow(in vec4 vert,
[VTK] 76:                   in sampler2D shadowMap,
[VTK] 77:                   in mat4 shadowTransform,
[VTK] 78:                   in float attenuation,
[VTK] 79:                   in int shadowParallel,
[VTK] 80:                   in float sNearZ, in float sFarZ)
[VTK] 81: {
[VTK] 82:   vec4 shadowCoord = shadowTransform*vert;
[VTK] 83:   float expFactor = 8.0;
[VTK] 84:   float thickness = 0.0;
[VTK] 85:   if(shadowCoord.w &gt; 0.0)
[VTK] 86:     {
[VTK] 87:     vec2 projected = shadowCoord.xy/shadowCoord.w;
[VTK] 88:     if(projected.x &gt;= 0.0 &amp;&amp; projected.x &lt;= 1.0
[VTK] 89:        &amp;&amp; projected.y &gt;= 0.0 &amp;&amp; projected.y &lt;= 1.0)
[VTK] 90:       {
[VTK] 91:       float ldepth = shadowCoord.z;
[VTK] 92:       if (shadowParallel == 0) { ldepth =  (shadowCoord.w - sNearZ)/(sFarZ - sNearZ); }
[VTK] 93:       float depthCExpActual = exp(- depthC*ldepth);
[VTK] 94:       float depthCExpBlured = texture2D(shadowMap,projected).r;
[VTK] 95:       expFactor = depthCExpBlured * depthCExpActual;
[VTK] 96:       float depth = log(depthCExpBlured)/depthC;
[VTK] 97:       thickness = clamp(ldepth - depth, 0.0, 1.0)*(sFarZ - sNearZ);
[VTK] 98:       if (expFactor &gt; 1.0) { expFactor = 1.0; }
[VTK] 99:       }
[VTK] 100:     }
[VTK] 101:   return vec2(1.0 - attenuation + attenuation*expFactor, thickness);
[VTK] 102: }
[VTK] 103: uniform int shadowParallel0;
[VTK] 104: uniform float shadowNearZ0;
[VTK] 105: uniform float shadowFarZ0;
[VTK] 106: uniform float shadowAttenuation0;
[VTK] 107: uniform sampler2D shadowMap0;
[VTK] 108: uniform mat4 shadowTransform0;
[VTK] 109: 
[VTK] 110: 
[VTK] 111: // Texture maps
[VTK] 112: //VTK::TMap::Dec
[VTK] 113: 
[VTK] 114: // Texture coordinates
[VTK] 115: //VTK::TCoord::Dec
[VTK] 116: 
[VTK] 117: // picking support
[VTK] 118: //VTK::Picking::Dec
[VTK] 119: 
[VTK] 120: // Depth Peeling Support
[VTK] 121: //VTK::DepthPeeling::Dec
[VTK] 122: 
[VTK] 123: // clipping plane vars
[VTK] 124: //VTK::Clip::Dec
[VTK] 125: 
[VTK] 126: // the output of this shader
[VTK] 127: out vec4 fragOutput0;
[VTK] 128: 
[VTK] 129: 
[VTK] 130: // Apple Bug
[VTK] 131: //VTK::PrimID::Dec
[VTK] 132: 
[VTK] 133: // handle coincident offsets
[VTK] 134: //VTK::Coincident::Dec
[VTK] 135: 
[VTK] 136: // Value raster
[VTK] 137: //VTK::ValuePass::Dec
[VTK] 138: 
[VTK] 139: // surface with edges
[VTK] 140: //VTK::Edges::Dec
[VTK] 141: 
[VTK] 142: void main()
[VTK] 143: {
[VTK] 144:   // VC position of this fragment. This should not branch/return/discard.
[VTK] 145:   //VTK::PositionVC::Impl
[VTK] 146: 
[VTK] 147:   // Place any calls that require uniform flow (e.g. dFdx) here.
[VTK] 148:   //VTK::UniformFlow::Impl
[VTK] 149: 
[VTK] 150:   // Set gl_FragDepth here (gl_FragCoord.z by default)
[VTK] 151:   //VTK::Depth::Impl
[VTK] 152: 
[VTK] 153:   // Early depth peeling abort:
[VTK] 154:   //VTK::DepthPeeling::PreColor
[VTK] 155: 
[VTK] 156:   // Apple Bug
[VTK] 157:   //VTK::PrimID::Impl
[VTK] 158: 
[VTK] 159:   //VTK::Clip::Impl
[VTK] 160: 
[VTK] 161:   //VTK::ValuePass::Impl
[VTK] 162: 
[VTK] 163:     vec3 ambientColor = ambientIntensity * ambientColorUniform;
[VTK] 164:   vec3 diffuseColor = diffuseIntensity * diffuseColorUniform;
[VTK] 165:   float opacity = opacityUniform;
[VTK] 166: 
[VTK] 167: 
[VTK] 168:   //VTK::Edges::Impl
[VTK] 169: 
[VTK] 170:   // Generate the normal if we are not passed in one
[VTK] 171:   //VTK::Normal::Impl
[VTK] 172: 
[VTK] 173:   vec2 factor0 = vec2(1.0);
[VTK] 174: vec2 factor1 = calcShadow(vertexVC, shadowMap0, shadowTransform0, shadowAttenuation0, shadowParallel0, shadowNearZ0, shadowFarZ0);
[VTK] 175:   fragOutput0 = vec4(ambientColor + diffuseColor, opacity);
[VTK] 176:   //VTK::Light::Impl
[VTK] 177: 
[VTK] 178: 
[VTK] 179: 
[VTK] 180:   //VTK::TCoord::Impl
[VTK] 181: 
[VTK] 182:   if (fragOutput0.a &lt;= 0.0)
[VTK] 183:     {
[VTK] 184:     discard;
[VTK] 185:     }
[VTK] 186: 
[VTK] 187:   //VTK::DepthPeeling::Impl
[VTK] 188: 
[VTK] 189:   //VTK::Picking::Impl
[VTK] 190: 
[VTK] 191:   // handle coincident offsets
[VTK] 192:   //VTK::Coincident::Impl
[VTK] 193: }
[VTK] ERROR: 0:175: 'vertexVC' : undeclared identifier 
[VTK] ERROR: 0:175: '' : compilation terminated 
[VTK] ERROR: 2 compilation errors.  No code generated.
[VTK] Could not set shader program
[VTK] attempt to add attribute without a bound program for attribute vertexMC
[VTK] Error setting 'vertexMC' in shader VAO.
[VTK] Input port 0 of algorithm vtkTransformPolyDataFilter (000001AE289620D0) has 0 connections but is not optional.
[VTK] Input port 0 of algorithm vtkTransformPolyDataFilter (000001AE289620D0) has 0 connections but is not optional.
[VTK] Input port 0 of algorithm vtkTransformPolyDataFilter (000001AE28961EF0) has 0 connections but is not optional.
[VTK] Input port 0 of algorithm vtkTransformPolyDataFilter (000001AE28961EF0) has 0 connections but is not optional.
</code></pre>

---

## Post #2 by @lassoan (2024-07-16 20:52 UTC)

<p>There are two probably unrelated issues.</p>
<ol>
<li><code>Input port 0 of algorithm vtkTransformPolyDataFilter (000001AE289620D0) has 0 connections but is not optional</code></li>
</ol>
<p>This means that some model is empty. Make sure to check if a model is empty before processing it.</p>
<ol start="2">
<li><code>[VTK] ERROR: 0:175: 'vertexVC' : undeclared identifier </code></li>
</ol>
<p>This is a shader compilation error. VTK is extremely good in allowing mixing and matching various custom rendering steps, but it is not perfect. There are certainly combinations that are incompatible. You can probably fix it by reviewing the error message and VTK shader generation code.</p>
<p>Note that <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> has already implemented a very similar feature that you described - see details <a href="https://projectweek.na-mic.org/PW41_2024_MIT/Projects/NodeFocus/">here</a>.</p>
<p>You may want to check out what he has done and maybe work together to get the feature finalized and integrated sooner.</p>

---
