import importlib
import json
import os

from utils import proto_to_dict


def gen_service_cls(pb, data):
    svc = pb.call_service_name()
    values = data
    v = list(values.values())
    clz_name = svc.replace(".", "").capitalize()
    l = []
    for i in v:
        def get_args():
            for ii in i['input']:
                for _k, _v in ii.items():
                    arg, (_type, tag) = _k, _v
                    ori = f"{arg}:{_type}"
                    if tag != 'required':
                        "level:str=None"
                        ori += "=None"
                    yield ori

        tl = list(get_args())
        ll = sorted(tl, key=lambda x: "=None" in x)
        args = ", ".join(ll)

        interface_desc = f"""
    @grpc_proxy(path="{i['full_name']}")
    def {i['name']}(self,{args}):
        \"\"\""\"\"\n"""
        l.append(interface_desc)

    template = f"""# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class {clz_name}(BaseClient):
    SERVICE_NAME="{svc}"
            {"".join(l)}
        """
    with open(f"services/{clz_name.lower()}.py", "w") as f:
        f.write(template)


if __name__ == '__main__':
    # 拿data下的所有proto
    pb2_list = os.popen("find data/ -name *_pb2.py").readlines()
    # 过滤不需要解析的proto
    pb2s = [p.replace(".py", "").replace("//", ".").strip("\n") for p in pb2_list if "gogo_pb2" not in p]

    for pb2 in pb2s:
        pb = importlib.import_module("data.dm_pb2")
        pp = proto_to_dict.ServiceCaller(pb)
        _data = pp.call_all_services()

        with open("services/f.json", "w") as f:
            json.dump(_data, f, indent=4)
        # 生成service class
        gen_service_cls(pp, _data)
