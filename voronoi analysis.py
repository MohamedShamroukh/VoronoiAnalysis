#
#
# ((copyrights))
# created by: Mohamed Shamroukh Under the guidance and supervision of Prof.Mohamed Alkhuzamy Aziz
# ((python libraries and modules))
# importing analysis module
import os
import arcpy
# ((workspace variables))
# Set the workspace for ListFeatureClasses
inputSERVICESworkspace = arcpy.GetParameterAsText(0)
arcpy.env.workspace = inputSERVICESworkspace
inputborder = arcpy.GetParameterAsText(1)
output = arcpy.GetParameterAsText(2)
zonename = arcpy.GetParameterAsText(3)
arcpy.env.overwriteOutput = True
arcpy.AddMessage("analysis is about to start applying geo-processing on: >>>>>.....{}>>>>>" .format(inputborder))
# ((Voronoi Analysis Algorithm))>>>>>>>>>>>>>>>>>>>
# Use the ListFeatureClasses function to return a list of shapefiles.
featureclasses = arcpy.ListFeatureClasses()
# loop through the list of shape files
for ifc in featureclasses:
    arcpy.env.extent = inputborder
    voronoi = os.path.join(output, os.path.splitext(ifc)[0] + zonename + '_voronoi')
    arcpy.CreateThiessenPolygons_analysis(ifc, voronoi, "ALL")
    voronoicl = os.path.join(output, os.path.splitext(ifc)[0] + zonename + '_voronoiclip')
    arcpy.Clip_analysis(voronoi, inputborder, voronoicl, "")
    arcpy.AddMessage("analysis has been completed: >>>>>.....{}>>>>>" .format(ifc))
arcpy.AddMessage("analysis has been completed")
arcpy.AddMessage('created by: Mohamed Shamroukh under the guidance and supervision of Prof.Mohamed Alkhuzamy Aziz')
