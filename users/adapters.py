from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user = super().save_user(request, user, form, False)
        phone= data.get('phone')
        address= data.get('address')
        if phone:
            user.phone = phone
        if address:
            user.address = address
        user.save()
        return user
    

#class CustomAccountAdapter(DefaultAccountAdapter):
 #   def save_user(self, request,user,form,commit=True):
        data = form.cleaned_data
        user= super().save_user(request,user,form,False)

        phone = data.get('phone')
        address = data.get('address')
        if phone:
            user.phone = phone
        if address:
            user.address = address
        user.save()
        return user