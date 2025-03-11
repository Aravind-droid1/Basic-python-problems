class sol(object):
    def exception(self,a,b):
        try:
            a/b
        except Exception as e:
            print("exception:",e)
        else:
            print("success")
        finally:
            print("nothing to worry")

obj=sol()
obj.exception(2,'hi')
obj.exception(6,2)