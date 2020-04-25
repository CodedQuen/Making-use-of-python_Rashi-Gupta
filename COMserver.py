class COMStringServer:
    _reg_clsid_=’{BD055A03-EC10-4919-9F65-FDE57A840D1A}’
    _reg_progid_=’COMSTRINGSERVER’
    _public_methods_=[‘letters’,’words’]
    
    def letters(self,arg1):
        #arg1=arg1.strip()
        counter=arg1.count(‘ ‘)
        l=len(arg1)
        return l-counter

    def words(self,arg1):
        arg1=arg1.strip()
        counter=arg1.count(‘ ‘)
        return counter+1

if __name__==’__main__’:
    import win32com.server.register
    win32com.server.register.UseCommandLine(COMStringServer)
