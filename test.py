#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Yuji Kato
#
# Created:     17/05/2013
# Copyright:   (c) Yuji Kato 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy

fc = "C:/damien/TEST_IST.shp"

rows = arcpy.UpdateCursor(fc)
for row in rows:
    activites = row.ALL_ACT_ID.split(":")
    i = 0
    conf = 0
    while i<(len(activites)-1):
        j = i+1
        a = activites[i]
        while j<len(activites):
            b = activites[j]
            if (a=="E114" and b=="E115") or (b=="E115" and a=="E114"):
                conf += 1
            j += 1
        i += 1
    row.conflit = conf
    rows.updateRow(row)