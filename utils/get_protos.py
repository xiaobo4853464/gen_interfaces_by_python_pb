"""
通过proto 文件生成python pb 描述文件。需要进一步开发。
"""
import importlib
import os
from shutil import copy

branch = 'master'


def get_proj_path(proj_name):
    p = os.path.abspath(os.path.dirname(__file__))
    return p[:p.find(proj_name) + len(proj_name)]


# cur_p = os.getcwd()
# go_proj_path = f"{os.environ['HOME']}/go-live"
go_proj_path = f"{get_proj_path('kunnka')}/go-live"
# os.chdir(go_proj_path)
# os.system('git reset --hard')  # 彻底回退到某个版本，本地的源码也会变为上一个版本的内容
# os.system('git clean -d -f')  # git clean -d -f删除未跟踪的目录和文件
# os.system('git pull -p')
# result = os.system('git checkout ' + branch)
# os.system('git pull -p')  # 本地删除远程已经删除的分支

# 把proto文件cp到本地，并且替换gogo.proto

if __name__ == '__main__':

    # for root, dirs, files in os.walk(f"{go_proj_path}/app/service"):
    #     for f in files:
    #         if f.endswith(".proto"):
    #             file_path = root + "/" + f
    #             if os.path.exists(file_path):
    #                 with open(file_path, "r") as f1:
    #                     content = f1.read()
    #                     if content:
    #                         content = content.replace('import "github.com/gogo/protobuf/gogoproto/gogo.proto";',
    #                                                   'import "data/gogo.proto";')
    #                 with open(file_path, "w") as f2:
    #                     f2.write(content)

    proto_list = os.popen("find ../go-live/app/service -name *.proto").readlines()
    os.chdir("..")
    for p in proto_list:
        proto_f = p.strip("\n").replace("../", "")
        a = os.system("python3 -m grpc_tools.protoc --python_out=. -I. " + proto_f)
        print(a)