# How to give camera position and camera focal point  as utm format in VTK 

**Topic ID**: 41238
**Date**: 2025-01-23
**URL**: https://discourse.slicer.org/t/how-to-give-camera-position-and-camera-focal-point-as-utm-format-in-vtk/41238

---

## Post #1 by @manafpv (2025-01-23 14:15 UTC)

<p>Hello Guys,</p>
<p>I am facing a issue which i want to give lat and long and distance of the camera from ground in utm format. but my camera is only considering lat, long manner , here i attaching my code… please find a solution for me</p>
<pre><code>  #include &lt;math.h&gt;
  
  #include &lt;string.h&gt;
  
  #include &lt;sys/time.h&gt;
  
  #include &lt;cuda_runtime_api.h&gt;
  
    #include &lt;tuple&gt;
    
    #include &lt;GeographicLib/UTMUPS.hpp&gt;
    
    #include &lt;opencv2/opencv.hpp&gt;
    
    #include &lt;iostream&gt;
    
    #include &lt;cmath&gt;
    
    #include &lt;vector&gt;
    
    #include &lt;random&gt;
    
    #include &lt;string&gt;
    
    #include &lt;map&gt;
    
    #include &lt;gdal.h&gt;
    
    #include &lt;gdal_priv.h&gt;
    
    #include &lt;ogrsf_frmts.h&gt;
    
    #include "ogr_spatialref.h"
    
    #include &lt;gdal_priv.h&gt; // For GDAL, used to read shapefiles and handle projections
    
    #include &lt;ogr_api.h&gt;
    
    #include &lt;ogr_geometry.h&gt;
    
    #include &lt;ogr_feature.h&gt;
    
    #include &lt;utility&gt;
    
    #include &lt;vtk-9.1/vtkActor.h&gt;
    
    #include &lt;vtk-9.1/vtkCamera.h&gt;
    
    #include &lt;vtk-9.1/vtkCylinderSource.h&gt;
    
    #include &lt;vtk-9.1/vtkNamedColors.h&gt;
    
    #include &lt;vtk-9.1/vtkNew.h&gt;
    
    #include &lt;vtk-9.1/vtkPolyDataMapper.h&gt;
    
    #include &lt;vtk-9.1/vtkProperty.h&gt;
    
    #include &lt;vtk-9.1/vtkRenderWindow.h&gt;
    
    #include &lt;vtk-9.1/vtkRenderWindowInteractor.h&gt;
    
    #include &lt;vtk-9.1/vtkRenderer.h&gt;
    
    #include &lt;vtk-9.1/vtkPolyData.h&gt; // For 3D plotting (alternative to PyVista)
    
    #include &lt;vtk-9.1/vtkSmartPointer.h&gt;
    
    #include &lt;vtk-9.1/vtkArcPlotter.h&gt; // For plotting
    
    #include &lt;vtk-9.1/vtkPoints.h&gt;
    
    #include &lt;vtk-9.1/vtkCellArray.h&gt;
    
    #include &lt;vtk-9.1/vtkCellArrayIterator.h&gt;
    
    #include &lt;vtk-9.1/vtkFloatArray.h&gt;
    
    #include &lt;vtk-9.1/vtkColor.h&gt;
    
    #include &lt;vtk-9.1/vtkPNGWriter.h&gt;
    
    #include &lt;vtk-9.1/vtkWindowToImageFilter.h&gt;
    
    #include &lt;vtk-9.1/vtkNamedColors.h&gt;
    
    #include &lt;array&gt;

OGRLayer* shapefile(const char* shapefilePath) {
    // Step 1: Open the shapefile
    GDALDataset* dataset = (GDALDataset*)GDALOpenEx(shapefilePath, GDAL_OF_VECTOR, nullptr, nullptr, nullptr);
    if (dataset == nullptr) {
        std::cerr &lt;&lt; "Failed to open shapefile: " &lt;&lt; shapefilePath &lt;&lt; std::endl;
        return nullptr;
    }

    std::cout &lt;&lt; "Shapefile opened successfully!" &lt;&lt; std::endl;

    // Step 2: Get the layer from the shapefile
    OGRLayer* layer = dataset-&gt;GetLayer(0);
    if (layer == nullptr) {
        std::cerr &lt;&lt; "Failed to get layer from shapefile." &lt;&lt; std::endl;
        GDALClose(dataset);
        return nullptr;
    }

    // Step 3: Get the current spatial reference system of the layer
    OGRSpatialReference* sourceSRS = layer-&gt;GetSpatialRef();
    if (sourceSRS == nullptr) {
        std::cerr &lt;&lt; "Shapefile does not have a spatial reference system." &lt;&lt; std::endl;
        GDALClose(dataset);
        return nullptr;
    }

    char* sourceWKT = nullptr;
    sourceSRS-&gt;exportToWkt(&amp;sourceWKT);
    std::cout &lt;&lt; "Source CRS: " &lt;&lt; sourceWKT &lt;&lt; std::endl;
    CPLFree(sourceWKT);

    // Step 4: Define the target spatial reference system (EPSG:32617)
    OGRSpatialReference targetSRS;
    targetSRS.importFromEPSG(32617);

    // Step 5: Create a coordinate transformation
    OGRCoordinateTransformation* coordTransform = OGRCreateCoordinateTransformation(sourceSRS, &amp;targetSRS);
    if (coordTransform == nullptr) {
        std::cerr &lt;&lt; "Failed to create coordinate transformation." &lt;&lt; std::endl;
        GDALClose(dataset);
        return nullptr;
    }

    std::cout &lt;&lt; "Coordinate transformation created successfully to EPSG:32617." &lt;&lt; std::endl;

    // Step 6: Iterate through the features and transform their geometries
    OGRFeature* feature;
    layer-&gt;ResetReading();
    while ((feature = layer-&gt;GetNextFeature()) != nullptr) {
        OGRGeometry* geometry = feature-&gt;GetGeometryRef();
        if (geometry == nullptr) {
            std::cerr &lt;&lt; "Feature has no geometry." &lt;&lt; std::endl;
            OGRFeature::DestroyFeature(feature);
            continue;
        }

        if (geometry-&gt;transform(coordTransform) != OGRERR_NONE) {
            std::cerr &lt;&lt; "Failed to transform geometry." &lt;&lt; std::endl;
        }

        // Optionally, do something with the transformed geometry

        OGRFeature::DestroyFeature(feature);
    }

    // Clean up
    OCTDestroyCoordinateTransformation(coordTransform);

    std::cout &lt;&lt; "Shapefile reprojected to EPSG:32617." &lt;&lt; std::endl;

    // Return the reprojected layer
    return layer;
}

std::vector&lt;vtkSmartPointer&lt;vtkPolyData&gt;&gt; processGeometries(OGRLayer* transformedLayer, vtkRenderer* renderer, vtkRenderWindow* renderWindow) {
    // Check if the layer is valid
    if (transformedLayer == nullptr) {
        std::cerr &lt;&lt; "Layer is empty." &lt;&lt; std::endl;
        return {}; // Return empty vector if the layer is invalid
    }

    // Create a vector to store poly meshes
    std::vector&lt;vtkSmartPointer&lt;vtkPolyData&gt;&gt; polyMeshes;

    OGRFeature* poFeature;
    OGRGeometry* poGeometry;

    // Create a coordinate transformation for EPSG:4326 -&gt; EPSG:32617
    OGRSpatialReference oSRS1, oSRS2;
    oSRS1.SetWellKnownGeogCS("EPSG:4326");  // Input CRS (WGS 84)
    oSRS2.SetProjCS("EPSG:32617");          // Target CRS (UTM Zone 17N)
    OGRCoordinateTransformation* poTransform = OGRCreateCoordinateTransformation(&amp;oSRS1, &amp;oSRS2);

    if (poTransform == nullptr) {
        std::cerr &lt;&lt; "Failed to create coordinate transformation." &lt;&lt; std::endl;
        return {};
    }

    // Iterate through each feature in the layer
    transformedLayer-&gt;ResetReading();
    int featureCount = 0;

    while ((poFeature = transformedLayer-&gt;GetNextFeature()) != nullptr) {
        featureCount++;
        poGeometry = poFeature-&gt;GetGeometryRef();

        if (poGeometry) {
            // Print geometry type name
            OGRwkbGeometryType geomType = poGeometry-&gt;getGeometryType();
            std::cout &lt;&lt; "Processing Geometry Type: " &lt;&lt; OGRGeometryTypeToName(geomType) &lt;&lt; std::endl;

            // Apply CRS transformation to the geometry
            if (geomType == wkbPolygon || geomType == wkbMultiPolygon) {
                // Handle Polygon and MultiPolygon geometries separately
                OGRGeometry* transformedGeometry = poGeometry-&gt;clone(); // Clone to transform

                // Transform each point in the geometry
                OGRPolygon* poPolygon = nullptr;
                if (geomType == wkbPolygon) {
                    poPolygon = (OGRPolygon*)transformedGeometry;
                } else if (geomType == wkbMultiPolygon) {
                    OGRMultiPolygon* poMultiPolygon = (OGRMultiPolygon*)transformedGeometry;
                    for (int i = 0; i &lt; poMultiPolygon-&gt;getNumGeometries(); i++) {
                        poPolygon = (OGRPolygon*)poMultiPolygon-&gt;getGeometryRef(i);
                    }
                }

                if (poPolygon) {
                    OGRLinearRing* poRing = poPolygon-&gt;getExteriorRing();
                    for (int i = 0; i &lt; poRing-&gt;getNumPoints(); i++) {
                        OGRPoint point;
                        poRing-&gt;getPoint(i, &amp;point);

                        double x = point.getX();
                        double y = point.getY();
                        double z = point.getZ();

                        // Transform the point coordinates
                        if (poTransform-&gt;Transform(1, &amp;x, &amp;y, &amp;z)) {
                            poRing-&gt;setPoint(i, x, y);
                        } else {
                            std::cerr &lt;&lt; "Coordinate transformation failed for point " &lt;&lt; i &lt;&lt; "." &lt;&lt; std::endl;
                        }
                    }
                }

                // Proceed to handle transformed geometries after transformation
                vtkSmartPointer&lt;vtkPoints&gt; points = vtkSmartPointer&lt;vtkPoints&gt;::New();
                for (int i = 0; i &lt; poPolygon-&gt;getExteriorRing()-&gt;getNumPoints(); i++) {
                    OGRPoint point;
                    poPolygon-&gt;getExteriorRing()-&gt;getPoint(i, &amp;point);
                    points-&gt;InsertNextPoint(point.getX(), point.getY(), 0.0);
                }

                vtkSmartPointer&lt;vtkCellArray&gt; cells = vtkSmartPointer&lt;vtkCellArray&gt;::New();
                vtkSmartPointer&lt;vtkPolyData&gt; polyMesh = vtkSmartPointer&lt;vtkPolyData&gt;::New();

                vtkIdType numPoints = points-&gt;GetNumberOfPoints();
                vtkIdType* ids = new vtkIdType[numPoints];
                for (vtkIdType i = 0; i &lt; numPoints; i++) {
                    ids[i] = i;
                }
                cells-&gt;InsertNextCell(numPoints, ids);
                delete[] ids;

                polyMesh-&gt;SetPoints(points);
                polyMesh-&gt;SetPolys(cells);

                std::cout &lt;&lt; "Polygon geometry with " &lt;&lt; numPoints &lt;&lt; " points." &lt;&lt; std::endl;
                polyMeshes.push_back(polyMesh);
            }
            // Handle other geometry types (LineString, Point, etc.)
            else if (geomType == wkbLineString) {
                // Handle LineString geometry
                OGRLineString* poLineString = (OGRLineString*)poGeometry;
                vtkSmartPointer&lt;vtkPoints&gt; points = vtkSmartPointer&lt;vtkPoints&gt;::New();
                for (int i = 0; i &lt; poLineString-&gt;getNumPoints(); i++) {
                    OGRPoint point;
                    poLineString-&gt;getPoint(i, &amp;point);
                    points-&gt;InsertNextPoint(point.getX(), point.getY(), 0.0);
                }

                vtkSmartPointer&lt;vtkCellArray&gt; cells = vtkSmartPointer&lt;vtkCellArray&gt;::New();
                vtkSmartPointer&lt;vtkPolyData&gt; polyMesh = vtkSmartPointer&lt;vtkPolyData&gt;::New();

                vtkIdType numPoints = points-&gt;GetNumberOfPoints();
                vtkIdType* ids = new vtkIdType[numPoints];
                for (vtkIdType i = 0; i &lt; numPoints; i++) {
                    ids[i] = i;
                }
                cells-&gt;InsertNextCell(numPoints, ids);
                delete[] ids;

                polyMesh-&gt;SetPoints(points);
                polyMesh-&gt;SetLines(cells);

                std::cout &lt;&lt; "LineString geometry with " &lt;&lt; numPoints &lt;&lt; " points." &lt;&lt; std::endl;
                polyMeshes.push_back(polyMesh);
            }
            else if (geomType == wkbPoint) {
                // Handle Point geometry
                OGRPoint* poPoint = (OGRPoint*)poGeometry;
                vtkSmartPointer&lt;vtkPoints&gt; points = vtkSmartPointer&lt;vtkPoints&gt;::New();
                points-&gt;InsertNextPoint(poPoint-&gt;getX(), poPoint-&gt;getY(), 0.0);

                vtkSmartPointer&lt;vtkCellArray&gt; cells = vtkSmartPointer&lt;vtkCellArray&gt;::New();
                vtkSmartPointer&lt;vtkPolyData&gt; polyMesh = vtkSmartPointer&lt;vtkPolyData&gt;::New();

                vtkIdType ids[1] = {0};
                cells-&gt;InsertNextCell(1, ids);

                polyMesh-&gt;SetPoints(points);
                polyMesh-&gt;SetVerts(cells);

                std::cout &lt;&lt; "Point geometry." &lt;&lt; std::endl;
                polyMeshes.push_back(polyMesh);
            }
        } else {
            std::cerr &lt;&lt; "No geometry found for feature." &lt;&lt; std::endl;
        }

        OGRFeature::DestroyFeature(poFeature);
    }

    std::cout &lt;&lt; "Processed " &lt;&lt; polyMeshes.size() &lt;&lt; " geometries from " &lt;&lt; featureCount &lt;&lt; " features." &lt;&lt; std::endl;

    // Debugging: Render and print information about the meshes
    vtkSmartPointer&lt;vtkNamedColors&gt; colors = vtkSmartPointer&lt;vtkNamedColors&gt;::New();
    for (auto&amp; polyMesh : polyMeshes) {
        std::cout &lt;&lt; "Processing mesh with number of points: " &lt;&lt; polyMesh-&gt;GetPoints()-&gt;GetNumberOfPoints() &lt;&lt; std::endl;

        if (polyMesh-&gt;GetPoints()-&gt;GetNumberOfPoints() == 0) {
            std::cerr &lt;&lt; "Empty mesh found!" &lt;&lt; std::endl;
            continue;
        }

        // Create mapper and actor for rendering
        vtkSmartPointer&lt;vtkPolyDataMapper&gt; mapper = vtkSmartPointer&lt;vtkPolyDataMapper&gt;::New();
        mapper-&gt;SetInputData(polyMesh);

        vtkSmartPointer&lt;vtkActor&gt; actor = vtkSmartPointer&lt;vtkActor&gt;::New();
        actor-&gt;SetMapper(mapper);
        actor-&gt;GetProperty()-&gt;SetColor(colors-&gt;GetColor4d("Red").GetData()); // Set color to red
        actor-&gt;GetProperty()-&gt;SetLineWidth(5.0); // Increase line thickness
        actor-&gt;GetProperty()-&gt;SetPointSize(8.0); // Increase point size for points
        actor-&gt;GetProperty()-&gt;SetOpacity(1.0); // Set opacity

        // Add the actor to the renderer
        renderer-&gt;AddActor(actor);
        std::cout &lt;&lt; "Added actor for mesh with " &lt;&lt; polyMesh-&gt;GetPoints()-&gt;GetNumberOfPoints() &lt;&lt; " points." &lt;&lt; std::endl;
    }

    // Set camera with azimuth and elevation
    vtkSmartPointer&lt;vtkCamera&gt; camera = renderer-&gt;GetActiveCamera();
    camera-&gt;SetPosition(594132.5056322503, 4493767.354823077, 150.01129150390625);
    camera-&gt;SetFocalPoint( 594132.5056322503, 4493767.354823077, 0); 
    camera-&gt;SetViewUp(0.0, 1.0, 0.0); 
    camera-&gt;Azimuth(0);  // Set azimuth

    camera-&gt;Elevation(60);  // Set elevation
   

    camera-&gt;SetViewAngle(89.9);
    renderer-&gt;ResetCamera();
    std::cout &lt;&lt; "Camera Position: "
          &lt;&lt; camera-&gt;GetPosition()[0] &lt;&lt; ", "
          &lt;&lt; camera-&gt;GetPosition()[1] &lt;&lt; ", "
          &lt;&lt; camera-&gt;GetPosition()[2] &lt;&lt; std::endl;

    std::cout &lt;&lt; "Camera Focal Point: "
          &lt;&lt; camera-&gt;GetFocalPoint()[0] &lt;&lt; ", "
          &lt;&lt; camera-&gt;GetFocalPoint()[1] &lt;&lt; ", "
          &lt;&lt; camera-&gt;GetFocalPoint()[2] &lt;&lt; std::endl;

    std::cout &lt;&lt; "Camera View Up: "
          &lt;&lt; camera-&gt;GetViewUp()[0] &lt;&lt; ", "
          &lt;&lt; camera-&gt;GetViewUp()[1] &lt;&lt; ", "
          &lt;&lt; camera-&gt;GetViewUp()[2] &lt;&lt; std::endl;

    std::cout &lt;&lt; "Camera Distance second: "
          &lt;&lt; camera-&gt;GetDistance() &lt;&lt; std::endl;

    renderWindow-&gt;Render();
    return polyMeshes;
}

void visualize_scene(double latitude, double longitude, double yaw, double pitch, double distance, double hfov, double vfov) {
    // Check if the latitude and longitude are valid
    if (latitude &lt; -90.0 || latitude &gt; 90.0 || longitude &lt; -180.0 || longitude &gt; 180.0) {
        std::cerr &lt;&lt; "Invalid latitude or longitude!" &lt;&lt; std::endl;
        return;
    }

    int zone;
    bool northp; // Whether the location is in the northern hemisphere or not
    double easting, northing;

    // Convert latitude and longitude to UTM
    GeographicLib::UTMUPS::Forward(latitude, longitude, zone, northp, easting, northing);
    std::cout &lt;&lt; "Using UTM zone: " &lt;&lt; zone &lt;&lt; ", Easting: " &lt;&lt; easting &lt;&lt; ", Northing: " &lt;&lt; northing &lt;&lt; std::endl;

    // Further processing: If the pitch is non-zero, calculate new coordinates
    double new_lat = latitude, new_lon = longitude;
    if (pitch != 0) {
        // Assuming calculate_new_location is defined elsewhere
        calculate_new_location(latitude, longitude, distance, yaw, pitch, hfov, vfov, new_lat, new_lon);
    }

    std::cout &lt;&lt; "New Latitude: " &lt;&lt; new_lat &lt;&lt; ", New Longitude: " &lt;&lt; new_lon &lt;&lt; std::endl;

    // Convert new latitude and longitude to UTM
    GeographicLib::UTMUPS::Forward(new_lat, new_lon, zone, northp, easting, northing);
    std::cout &lt;&lt; "New UTM - Easting: " &lt;&lt; easting &lt;&lt; ", Northing: " &lt;&lt; northing &lt;&lt; std::endl;

    // Assuming calculate_camera_position is defined elsewhere
    std::tuple&lt;double, double, double&gt; center = {easting, northing, 0.0};
    std::cout &lt;&lt; "Center - Easting: " &lt;&lt; std::get&lt;0&gt;(center) &lt;&lt; ", Northing: " &lt;&lt; std::get&lt;1&gt;(center) &lt;&lt; std::endl;

    auto cam_position = calculate_camera_position(center, distance);
    std::cout &lt;&lt; "Camera Position Calculated: (" &lt;&lt; std::get&lt;0&gt;(cam_position) &lt;&lt; ", "
              &lt;&lt; std::get&lt;1&gt;(cam_position) &lt;&lt; ", " &lt;&lt; std::get&lt;2&gt;(cam_position) &lt;&lt; ")" &lt;&lt; std::endl;

    // Initialize GDAL and OGR
    GDALAllRegister();

    OGRLayer* transformedLayer = shapefile("road_shape/road_shape.shp");
    if (transformedLayer == nullptr) {
        std::cerr &lt;&lt; "Failed to load shapefile!" &lt;&lt; std::endl;
        return;
    }

    std::cout &lt;&lt; "Successfully retrieved transformed layer." &lt;&lt; std::endl;

    // Set up VTK to render the scene
    vtkSmartPointer&lt;vtkNamedColors&gt; colors = vtkSmartPointer&lt;vtkNamedColors&gt;::New();
    vtkSmartPointer&lt;vtkRenderer&gt; renderer = vtkSmartPointer&lt;vtkRenderer&gt;::New();
    renderer-&gt;SetBackground(colors-&gt;GetColor3d("SkyBlue").GetData());

    vtkSmartPointer&lt;vtkRenderWindow&gt; renderWindow = vtkSmartPointer&lt;vtkRenderWindow&gt;::New();
    renderWindow-&gt;AddRenderer(renderer);

    vtkSmartPointer&lt;vtkRenderWindowInteractor&gt; renderWindowInteractor = vtkSmartPointer&lt;vtkRenderWindowInteractor&gt;::New();
    renderWindowInteractor-&gt;SetRenderWindow(renderWindow);

    // Process geometries from the shapefile
    //          std::vector&lt;vtkSmartPointer&lt;vtkPolyData&gt;&gt; polyMeshes = processGeometries(transformedLayer, renderer, renderWindow);
    std::string outputImagePath = "transparent_colored_polygons_test.png";
    //std::vector&lt;vtkSmartPointer&lt;vtkPolyData&gt;&gt; polyMeshes = processGeometries(
        //transformedLayer, renderer, renderWindow, cam_position, easting, northing, yaw, pitch, hfov, outputImagePath);
    //std::string outputImagePath = "transparent_colored_polygons_test.png";  
        std::vector&lt;vtkSmartPointer&lt;vtkPolyData&gt;&gt; polyMeshes = processGeometries(transformedLayer, renderer, renderWindow);

    }
</code></pre>
<p>you can only concentrated on calling this function part , this calling function  have this issue<br>
std::vector&lt;vtkSmartPointer&gt; polyMeshes =<br>
processGeometries(transformedLayer, renderer, renderWindow);</p>

---

## Post #2 by @lassoan (2025-01-23 15:45 UTC)

<p>While Slicer can be used for some geoinformatics applications, most of the community experience is around biomedical imaging. You may find more geo experts on the <a href="https://discourse.vtk.org/">VTK forum</a>.</p>

---
