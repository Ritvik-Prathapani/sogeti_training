from abc import ABC,abstractmethod
class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass
    
    @abstractmethod
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def login(self):
        return "Logged in using Google"
    
    def logout(self):
        return "Logged out from Google"
    
class FacebookAuth(UserAuthentication):
    def login(self):
        return "Logged in using Facebook"
    
    def logout(self):
        return "Logged out from Facebook"
    
google_auth = GoogleAuth()
print(google_auth.login())   
print(google_auth.logout())   

facebook_auth = FacebookAuth()
print(facebook_auth.login())   
print(facebook_auth.logout())   