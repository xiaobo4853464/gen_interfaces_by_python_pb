from services.api import Api

if __name__ == '__main__':
    account_vip = Api()
    r = account_vip.GetStreamBandWidth()
    print(r)
