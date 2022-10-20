from json.encoder import INFINITY
import cv2
import numpy as np
from tqdm import tqdm

import torch
from kornia_moons import feature
import kornia as K
import kornia.feature as KF
laf_from_opencv_SIFT_kpts = feature.laf_from_opencv_SIFT_kpts

device = "cuda" if torch.cuda.is_available() else "cpu"
descriptor = KF.HardNet8(True).eval().to(device)
SIFT = cv2.SIFT_create(contrastThreshold=-1, nfeatures=10000)

# template = img1[60:70,80:90]
# print(template.shape)
# img1 = np.zeros((6,4))
# template = np.zeros((3,2))
# print(cv2.imread("./1.png", 0))
# exit()
# img1 = cv2.imread("./1.png", 0)
# template = np.array([[255]],dtype=np.uint8)
# print(template.shape)
def template_matching(img1,template):
    edge_y = template.shape[0]
    edge_x = template.shape[1]
    template_new = template.flatten()
    res = []
    dists = []
    # new_img=np.zeros((img.shape[0]-2*edge,img.shape[1]-2*edge),dtype=np.uint8)
    for y in tqdm(range(img1.shape[0]-edge_y+1)):
        for x in range(img1.shape[1]-edge_x+1):
            a = img1[y:y+edge_y,x:x+edge_x]
            a = a.flatten()
            dist = np.abs(a-template_new).sum()
            dists.append(dist)
            # res.append((y,y+edge_y,x,x+edge_x))
            res.append(((x,y),(x+edge_x,y+edge_y)))
            # print(a.shape)
            # return
    # print(dists[np.argmin(dists)])
    # print(res[np.argmin(dists)])
    bbox = res[np.argmin(dists)]
    img1_rect = cv2.rectangle(img1.copy(), bbox[0], bbox[1], (0,0,0), 2)
    img1_rect_with_template = cv2.drawMatches(img1_rect, [], template, [], [],None)
    cv2.imwrite(f"{img1_filename[0]}_template_matching.png", img1_rect_with_template)
    # return res[np.argmin(dists)]

def get_bbox(points):
    min_y = INFINITY
    min_x = INFINITY
    max_x = -1
    max_y = -1
    for x, y in points:
        x = int(x)
        y = int(y)
        min_y = min(y,min_y)
        min_x = min(x,min_x)
        max_y = max(y,max_y)
        max_x = max(x,max_x)
    return ((min_x,min_y), (max_x,max_y))

def get_features(img):
    keypoints = SIFT.detect(img,None)
    with torch.no_grad():
            timg = K.image_to_tensor(img, False).float()/255.
            timg = timg.to(device)
            if timg.shape[1] == 3:
                timg_gray = K.rgb_to_grayscale(timg)
            else:
                timg_gray = timg
            lafs = laf_from_opencv_SIFT_kpts(keypoints, device=device)
            patches = KF.extract_patches_from_pyramid(timg_gray, lafs, 32)
            B, N, CH, H, W = patches.size()
            descs = descriptor(patches.view(B * N, CH, H, W)).view(B * N, -1).detach().cpu().numpy()   
    return (keypoints, descs)


def local_features_matching(img1,template):
    kpts1, descs1 = get_features(img1)
    kpts2, descs2 = get_features(template)
    # print(len(kpts1))
    # print(len(kpts2))
    match_threshold = 0.8
    dists, match_ids = KF.match_smnn(torch.from_numpy(descs1), torch.from_numpy(descs2), match_threshold)
    # print(len(dists))
    found_keypoints = []
    for i in match_ids[:,0]:
        found_keypoints.append(kpts1[i].pt)
    # print(match_ids[:,0])
    # print(match_ids)
    # print(found_keypoints)
    bbox = get_bbox(found_keypoints)
    # print(bbox)

    good_matches=[]
    for x in match_ids:
        good_matches.append(cv2.DMatch(int(x[0]), int(x[1]), 1.))

    print(len(good_matches))
    img1_rect = cv2.rectangle(img1.copy(), bbox[0], bbox[1], (0,0,0), 2)
    img1_rect_with_template = cv2.drawMatches(img1_rect, [], template, [], [],None)
    # cv2.imwrite("1_rectangle.png",img1_rect_with_template)
    img_matches = cv2.drawMatches(img1_rect, kpts1, template, kpts2, good_matches,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)    
    # cv2.imwrite("1_rectangle2.png",img)
    img_final = cv2.drawMatches(img1_rect_with_template, [], img_matches, [], [],None)
    # print(f"{img1_filename}_{template_filename}.png")
    cv2.imwrite(f"{img1_filename[0]}_hardnet8.png",img_final)
    # img = cv2.rectangle(img, bbox[0], bbox[1], (255,0,0), 2)
    # cv2.imshow("", img_final)
    # cv2.waitKey(0)




for i in range(8,9):
    img1_filename = f"{i}.png"
    template_filename = f"{i}_template.png"
    img1 = cv2.imread(img1_filename,0)
    template = cv2.imread(template_filename,0) #template
    # template_matching(img1, template)
    local_features_matching(img1, template)

# local_features_matching(img1, template)


