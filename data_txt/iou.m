function IOU=iou(gt,dr)
xmin_gt = gt(1);ymin_gt=gt(2);xmax_gt=gt(3);ymax_gt=gt(4);
xmin=dr(1);ymin=dr(2);xmax=dr(3);ymax=dr(4);
start_x=max(xmin,xmin_gt);end_x=min(xmax,xmax_gt);
start_y=max(ymin,ymin_gt);end_y=min(ymax,ymax_gt);
height=xmax-xmin;width=ymax-ymin;
height_gt=xmax_gt-xmin_gt;width_gt=ymax_gt-ymin_gt;
height_iou=end_x-start_x;width_iou=end_y-start_y;
area=height*width;
area_gt=height_gt*width_gt;
area_iou=height_iou*width_iou;
if height_iou<=0 || width_iou<0
    IOU=0;
else
    IOU=area_iou/(area+area_gt-area_iou);
end
end