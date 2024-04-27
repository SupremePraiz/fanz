from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type":"password"},write_only=True)
    password2 = serializers.CharField(style={"input_type":"password"},write_only=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
        # extra_kwargs ={
        #                "password":({"write_only": True}),
        #                 }
        
        def save(self):
            password = self.validated_data["password"]
            password2 = self.validated_data["password2"]
            
            if password != password2:
                raise serializers.ValidationError({"error":"Password1 and password2 must be the same"})
            if User.objects.filter(email = self.validated_data["email"]).exists():
                raise serializers.ValidationError({"error":"this email has already been used"})
            if User.objects.filter(username=self.validated_data["username"]).exists():
                raise serializers.ValidationError({"error":"this username has already been used"})
            
               
            account = User(email=self.validated_data["email"], username=self.validated_data["username"])
            account.set_password(password)
            account.save()
            
            return account