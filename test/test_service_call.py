from services.livelivedm import Livelivedm
if __name__ == '__main__':
    livedm=Livelivedm()
    r=livedm.SendMsg(uid=110000233, roomid=460460, msg="hello", rnd="hjhjkhkj")
    r2=livedm.GetHistory(roomid=460460)
    print(r)
    print(r2)
