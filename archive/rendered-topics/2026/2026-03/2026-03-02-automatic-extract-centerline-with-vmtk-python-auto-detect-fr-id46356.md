---
topic_id: 46356
title: "Automatic Extract Centerline With Vmtk Python Auto Detect Fr"
date: 2026-03-02
url: https://discourse.slicer.org/t/46356
---

# Automatic Extract Centerline with VMTK python (auto detect) from trachea segementation

**Topic ID**: 46356
**Date**: 2026-03-02
**URL**: https://discourse.slicer.org/t/automatic-extract-centerline-with-vmtk-python-auto-detect-from-trachea-segementation/46356

---

## Post #1 by @hadrien_calmet (2026-03-02 11:09 UTC)

<p>Hi everyone.</p>
<p>Since several people seem to be working on this without a clear answer, I’m sharing my contribution in case it helps others in the community.</p>
<p>Final main script:</p>
<p>make_clean_centerlines_zmax_generic.py</p>
<p>Cleans the STL and keeps the largest connected component (*_largest.stl),</p>
<p>Detects the seed at maximum Z,</p>
<p>Automatically detects all distal targets (no longer limited to 32),</p>
<p>Computes the centerlines (vmtkcenterlines),</p>
<p>Extracts/splits branches (vmtkbranchextractor),</p>
<p>Reconnects junctions + removes duplicates → *_centerlines_clean_connected.vtp.</p>
<blockquote>
<p>#!/usr/bin/env python3<br>
import math<br>
import subprocess<br>
from collections import defaultdict, deque<br>
from pathlib import Path</p>
<p>import numpy as np<br>
import vtk</p>
<h1>=========================================================</h1>
<h1>ONLY EDIT THIS LINE</h1>
<p>INPUT_STL = Path(“Huca3006198.stl”)# the segmentation that you have</p>
<h1>=========================================================</h1>
<h1>Tuning (usually keep defaults)</h1>
<p>MERGE_TOL_MM = 0.05<br>
TARGET_CLUSTER_RADIUS_MM = 0.0<br>
MAX_TARGETS = 0  # 0 means keep all detected outlet targets</p>
<p>def run(cmd):<br>
print(“[cmd]”, " ".join(cmd))<br>
subprocess.run(cmd, check=True)</p>
<p>def read_polydata(path: Path):<br>
ext = path.suffix.lower()<br>
if ext == “.stl”:<br>
reader = vtk.vtkSTLReader()<br>
elif ext == “.vtp”:<br>
reader = vtk.vtkXMLPolyDataReader()<br>
else:<br>
raise ValueError(f"Unsupported extension: {ext}")<br>
reader.SetFileName(str(path))<br>
reader.Update()<br>
return reader.GetOutput()</p>
<p>def clean_stl_keep_largest(input_stl: Path, output_stl: Path):<br>
poly = read_polydata(input_stl)</p>
<pre><code class="lang-auto">connectivity = vtk.vtkPolyDataConnectivityFilter()
connectivity.SetInputData(poly)
connectivity.SetExtractionModeToLargestRegion()
connectivity.Update()

largest = connectivity.GetOutput()
if largest is None or largest.GetNumberOfCells() == 0:
    raise RuntimeError("Largest connected component extraction failed.")

writer = vtk.vtkSTLWriter()
writer.SetFileName(str(output_stl))
writer.SetFileTypeToBinary()
writer.SetInputData(largest)
writer.Write()

print(
    f"[info] STL cleaned: cells {poly.GetNumberOfCells()} -&gt; {largest.GetNumberOfCells()} "
    f"({output_stl.name})"
)
</code></pre>
<p>def largest_component_nodes_from_network(network_vtp: Path):<br>
pd = read_polydata(network_vtp)<br>
pts = np.array([pd.GetPoint(i) for i in range(pd.GetNumberOfPoints())], dtype=float)</p>
<pre><code class="lang-auto">adj = defaultdict(set)
for cid in range(pd.GetNumberOfCells()):
    cell = pd.GetCell(cid)
    if cell.GetCellType() not in (vtk.VTK_LINE, vtk.VTK_POLY_LINE):
        continue
    ids = [cell.GetPointId(i) for i in range(cell.GetNumberOfPoints())]
    for a, b in zip(ids[:-1], ids[1:]):
        if a == b:
            continue
        adj[a].add(b)
        adj[b].add(a)

nodes = list(adj.keys())
visited = set()
components = []
for s in nodes:
    if s in visited:
        continue
    q = deque([s])
    visited.add(s)
    comp = []
    while q:
        u = q.popleft()
        comp.append(u)
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)
    components.append(comp)

if not components:
    raise RuntimeError("No centerline graph extracted from network.")

components.sort(key=len, reverse=True)
main = set(components[0])

leaves = [u for u in main if len([v for v in adj[u] if v in main]) == 1]
if len(leaves) &lt; 2:
    raise RuntimeError("Not enough leaf nodes found to define targets.")

src = max(leaves, key=lambda i: pts[i, 2])  # z max seed
outlets = [i for i in leaves if i != src]

clustered = list(outlets)
if TARGET_CLUSTER_RADIUS_MM &gt; 0.0:
    # Optional clustering to reduce near-duplicate targets.
    reduced = []
    for idx in sorted(outlets, key=lambda i: pts[i, 2]):
        p = pts[idx]
        keep = True
        for j in reduced:
            if np.linalg.norm(pts[j] - p) &lt; TARGET_CLUSTER_RADIUS_MM:
                keep = False
                break
        if keep:
            reduced.append(idx)
    clustered = reduced

# Keep farthest targets from source first. If MAX_TARGETS&lt;=0, keep all.
clustered = sorted(clustered, key=lambda i: np.linalg.norm(pts[i] - pts[src]), reverse=True)
if MAX_TARGETS &gt; 0:
    clustered = clustered[:MAX_TARGETS]

if not clustered:
    raise RuntimeError("No targets selected after clustering.")

source_xyz = pts[src].tolist()
targets_xyz = []
for i in clustered:
    targets_xyz.extend(pts[i].tolist())

print(f"[info] source(zmax) point id={src} xyz={source_xyz}")
print(f"[info] outlets detected={len(outlets)} selected targets={len(clustered)}")

return source_xyz, targets_xyz
</code></pre>
<p>def post_clean_dedup(input_vtp: Path, output_vtp: Path, tol_mm: float):<br>
reader = vtk.vtkXMLPolyDataReader()<br>
reader.SetFileName(str(input_vtp))<br>
reader.Update()<br>
poly = reader.GetOutput()</p>
<pre><code class="lang-auto">clean = vtk.vtkCleanPolyData()
clean.SetInputData(poly)
clean.PointMergingOn()
clean.ToleranceIsAbsoluteOn()
clean.SetAbsoluteTolerance(tol_mm)
clean.Update()
cleaned = clean.GetOutput()

seen = set()
unique_lines = []
kept_cell_ids = []

for cid in range(cleaned.GetNumberOfCells()):
    cell = cleaned.GetCell(cid)
    if cell.GetCellType() not in (vtk.VTK_LINE, vtk.VTK_POLY_LINE):
        continue
    ids = tuple(cell.GetPointId(i) for i in range(cell.GetNumberOfPoints()))
    if len(ids) &lt; 2:
        continue
    key = min(ids, ids[::-1])
    if key in seen:
        continue
    seen.add(key)
    unique_lines.append(ids)
    kept_cell_ids.append(cid)

out = vtk.vtkPolyData()
out.SetPoints(cleaned.GetPoints())

out_lines = vtk.vtkCellArray()
for ids in unique_lines:
    pl = vtk.vtkPolyLine()
    pl.GetPointIds().SetNumberOfIds(len(ids))
    for i, pid in enumerate(ids):
        pl.GetPointIds().SetId(i, pid)
    out_lines.InsertNextCell(pl)
out.SetLines(out_lines)

in_pd = cleaned.GetPointData()
out_pd = out.GetPointData()
for i in range(in_pd.GetNumberOfArrays()):
    arr = in_pd.GetArray(i)
    if arr is not None:
        out_pd.AddArray(arr)

in_cd = cleaned.GetCellData()
out_cd = out.GetCellData()
for name in ("Blanking", "CenterlineIds", "TractIds", "GroupIds"):
    arr = in_cd.GetArray(name)
    if arr is None:
        continue
    new_arr = vtk.vtkIntArray()
    new_arr.SetName(name)
    new_arr.SetNumberOfTuples(len(kept_cell_ids))
    for i, cid in enumerate(kept_cell_ids):
        new_arr.SetValue(i, int(arr.GetTuple1(cid)))
    out_cd.AddArray(new_arr)

clean2 = vtk.vtkCleanPolyData()
clean2.SetInputData(out)
clean2.PointMergingOn()
clean2.ToleranceIsAbsoluteOn()
clean2.SetAbsoluteTolerance(0.0)
clean2.Update()

writer = vtk.vtkXMLPolyDataWriter()
writer.SetFileName(str(output_vtp))
writer.SetInputData(clean2.GetOutput())
writer.Write()
</code></pre>
<p>def main():<br>
if not INPUT_STL.exists():<br>
raise FileNotFoundError(f"STL not found: {INPUT_STL}")</p>
<pre><code class="lang-auto">stem = INPUT_STL.stem
cleaned_stl = INPUT_STL.with_name(f"{stem}_largest.stl")
rough_network = INPUT_STL.with_name(f"{stem}_rough_network.vtp")
work_centerlines = INPUT_STL.with_name(f"{stem}_centerlines_zmax_auto.vtp")
work_branches = INPUT_STL.with_name(f"{stem}_centerlines_zmax_auto_branches.vtp")
final_out = INPUT_STL.with_name(f"{stem}_centerlines_clean_connected.vtp")

# 0) Surface cleanup: keep only the largest connected STL component.
clean_stl_keep_largest(INPUT_STL, cleaned_stl)

# 1) Rough automatic network just to detect leaves/targets robustly on new geometries
run([
    "vmtkcenterlinesnetwork",
    "-ifile", str(cleaned_stl),
    "-ofile", str(rough_network),
])

source_xyz, targets_xyz = largest_component_nodes_from_network(rough_network)

# 2) Final centerlines using zmax source + auto-selected targets
run([
    "vmtkcenterlines",
    "-ifile", str(cleaned_stl),
    "-seedselector", "pointlist",
    "-sourcepoints", *[str(v) for v in source_xyz],
    "-targetpoints", *[str(v) for v in targets_xyz],
    "-endpoints", "1",
    "-ofile", str(work_centerlines),
])

# 3) Split/group and clean
run([
    "vmtkbranchextractor",
    "-ifile", str(work_centerlines),
    "-ofile", str(work_branches),
])

post_clean_dedup(work_branches, final_out, MERGE_TOL_MM)
print("[ok] wrote", final_out)
</code></pre>
<p>if <strong>name</strong> == “<strong>main</strong>”:<br>
main()</p>
</blockquote>

---
