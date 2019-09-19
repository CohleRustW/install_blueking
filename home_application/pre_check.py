import re
class Sync(object):
    def __init__(self,ip):
        self.ip = ip
    def test(self):
        print(self.ip)
    def check_contrl_ip(self,outter_ip_list,contrl_ip):
        p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
        if not p.match(contrl_ip):
            return TypeError
        if contrl_ip in outter_ip_list:
            print('ip  in ')
            return True
        else:
            print('not  in')
            return False         
    def check_is_domain(self,domain):
        domain_regex = re.compile(
            r'(?:[A-Z0-9_](?:[A-Z0-9-_]{0,247}[A-Z0-9])?\.)+(?:[A-Z]{2,6}|[A-Z0-9-]{2,}(?<!-))\Z', 
            re.IGNORECASE)
        return True if domain_regex.match(domain) else False
    
    import re

    def passwd_check(self,passwd):

        lowerRegex = re.compile('[a-z]')
        upperRegex = re.compile('[A-Z]')
        digitRegex = re.compile('[0-9]')
        wrongRegex = re.compile('[^a-zA-Z0-9]')

        while True:
            password = input('请输入大于8位的包含大小写字母和数字的密码：')
            if len(password) < 8:
                return('输入的密码小于8位')
            elif wrongRegex.search(password) != None:
                return('包含无效字符')
            else:
                if lowerRegex.search(password) == None:
                    return('未包含小写字母')
                elif upperRegex.search(password) == None:
                    return('未包含大写字母')
                elif digitRegex.search(password) == None:
                    return('未包含数字')
                else:
                    return('输入成功')
                    break
        
