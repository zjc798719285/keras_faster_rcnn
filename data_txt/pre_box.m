clc
clear
f=importdata('train.txt');
thresh_iou=0.7;
num_pos=0;
img_width=399;
img_height=866;
map_width=25;
map_height=60;
stride=16;
scale=[320, 350, 380,400];
ratio=[2.5,3,3.2];
for i=1:10
    i
    s_cell = regexp(f{1},';','split');lab_path = s_cell{2};
    rect_cell = load(lab_path);rect = rect_cell.label;
    xmin_gt=round(rect(1)*img_height);
    ymin_gt=round(rect(2)*img_width);
    xmax_gt=round(rect(4)*img_height)+xmin_gt;
    ymax_gt=round(rect(3)*img_width)+ymin_gt;
    GroundTruth=[xmin_gt,ymin_gt,xmax_gt,ymax_gt];
    for scale_i=1:length(scale)
        for ratio_i=1:length(ratio)
            box_width=scale(scale_i)/ratio(ratio_i)^0.5;
            box_height=scale(scale_i)*ratio(ratio_i)^0.5;
            for cx=1:map_height
                for cy =1:map_width
                    xmin = round(stride*(0.5+cx)-box_height/2);
                    ymin = round(stride*(0.5+cy)-box_width/2);
                    xmax = round(stride*(0.5+cx)+box_height/2);
                    ymax = round(stride*(0.5+cy)+box_width/2);
                    anchor=[xmin,ymin,xmax,ymax];
                    IOU=iou(GroundTruth,anchor);
                    if IOU>thresh_iou
                        num_pos = num_pos+1;
                    end
                end
            end
        end
    end
end
num_pos