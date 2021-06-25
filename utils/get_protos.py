import importlib
import os
from shutil import copy

branch = 'master'


def get_proj_path(proj_name):
    p = os.path.abspath(os.path.dirname(__file__))
    return p[:p.find(proj_name) + len(proj_name)]


# cur_p = os.getcwd()
go_proj_path = f"{os.environ['HOME']}/go-live"
# os.chdir(go_proj_path)
# os.system('git reset --hard')  # 彻底回退到某个版本，本地的源码也会变为上一个版本的内容
# os.system('git clean -d -f')  # git clean -d -f删除未跟踪的目录和文件
# os.system('git pull -p')
# result = os.system('git checkout ' + branch)
# os.system('git pull -p')  # 本地删除远程已经删除的分支

# 把proto文件cp到本地，并且替换gogo.proto
for root, dirs, files in os.walk(f"{go_proj_path}/api"):
    for f in files:
        if f.endswith(".proto"):
            file_path = root + "/" + f
            target_path = get_proj_path("kunnka") + "/data/" + root[root.rfind("go-live"):]
            if os.path.exists(file_path):
                if not os.path.isdir(target_path):
                    os.makedirs(target_path)
                with open(file_path, "r") as f1:
                    content = f1.read()
                    if content:
                        c = content.replace('import "github.com/gogo/protobuf/gogoproto/gogo.proto";',
                                            'import "data/gogo.proto";')
                        with open(target_path + "/" + f, "w") as f2:
                            f2.write(c)

# os.chdir(cur_p)


# os.environ['PATH']+="/Users/boxiao/go/pkg/mod/"
# print(os.environ['PATH'])
# proto_path = "/Users/boxiao/PycharmProjects/kunnka/go-live/api/lottery/liverpc/v2/Lottery.proto"
# cmd=f"python3 -m grpc_tools.protoc --python_out=. Lottery.proto -I {go_proj_path}/api/lottery/liverpc/v2/"
# print(cmd)
