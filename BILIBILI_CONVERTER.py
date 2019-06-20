"""
BILIBILI 视频转换提取脚本

Author: alancheg
Date: 2019-06-19

## 目标
考虑到B站视频下载好后有统一的接口，因此写一个脚本进行批量转换

## 待办：
1. 文件名过长时无法进行转换
2. 加速转换时间，考虑直接复制或者其他方法
3. 转换结束后删除原来文件夹 保证转换顺利（即文件大小保持基本一致）
"""
import json
import os
import re
import glob

if __name__ == "__main__":

    # 目标文件夹
    src_dir = input("请输入需要操作的文件夹地址：")
    if not os.path.exists(src_dir):
        raise "directory not exist ! "

    # 遍历文件夹，并且在目标目录生成新的目录
    tar_dir = r"C:\Users\alan\Downloads\JavaVideo"

    # b站下载的视频目录结构层一般是 av号/序号/lua/视频文件 av号/序号/entry.json   
    for dir in os.listdir(src_dir):
        json_dir = os.path.join(src_dir, dir, "entry.json")
        json_file = json.load(open(json_dir, "r", encoding="utf8"))      
        title_dir = os.path.join(tar_dir, json_file["title"])
        if not os.path.exists(title_dir):
            os.mkdir(title_dir)

        # 转换成 flv 格式
        file_name = json_file['page_data']['part'] + ".flv"
        src_video_path = ""
        
        # tar_video_path = ""
        for video_dir in os.listdir(os.path.join(src_dir, dir)):
            for (dirpath, dirnames, video_files) in os.walk(os.path.join(src_dir, dir, video_dir)):
                src_video_path = glob.glob(os.path.join(src_dir, dir, video_dir,'*.blv'))[0]

        tar_video_path = os.path.join(tar_dir, title_dir, file_name)

        # print(src_video_path)
        if os.path.isfile(src_video_path): 
            print(src_video_path + " 开始转换 ！")
            open(tar_video_path, "wb").write(open(src_video_path, "rb").read())
        print(tar_video_path + " 转换完成 ！")