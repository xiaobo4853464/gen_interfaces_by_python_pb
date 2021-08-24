import importlib
import os

from jinja2 import PackageLoader, Environment
from utils import proto_to_dict


def gen_service_cls(pb, data):
    svc = pb.call_service_name()
    values = data
    v = list(values.values())
    clz_name = "".join([word.capitalize() for word in svc.split(".")])
    interfaces = []
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
        interface = {"path": i['full_name'], "method_name": i['name'], "args": args}
        interfaces.append(interface)

    data = {"cls_name": clz_name, "service_name": svc, "interfaces": interfaces}
    env = Environment(
        loader=PackageLoader("data", "templates"),
        keep_trailing_newline=True,
        line_statement_prefix="##",
        line_comment_prefix="###",
        trim_blocks=True,
        lstrip_blocks=True,
    )
    t = env.get_template("cls_demo")
    content = t.render(data=data)
    print(content)

    with open(f"services/{clz_name.lower()}.py", "w") as f:
        f.write(content)


if __name__ == '__main__':
    # 拿data下的所有proto
    pb2_list = os.popen("find bapis_python -name *_pb2.py").readlines()
    # 过滤不需要解析的proto

    pb2s = [p.replace(".py", "").replace("/", ".").strip("\n") for p in pb2_list if "gogo_pb2" not in p]

    for pb2 in pb2s:
        pb = importlib.import_module(pb2)
        pp = proto_to_dict.ServiceCaller(pb)
        _data = pp.call_all_services()

        # 生成service class
        try:
            gen_service_cls(pp, _data)
        except TypeError as e:
            print(repr(e))
            continue
