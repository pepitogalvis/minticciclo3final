from rest_framework import serializers
from shsApp.models.user import User
from shsApp.models.account import Account
from shsApp.serializers.accountSerializer import AccountSerializer

class UserSerializer(serializers.ModelSerializer):

    account = AccountSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'lastname', 'address', 'city', 'phone', 'email', 'dni', 'born_date', 'account']

    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)
        return {
                    'id': user.id,
                    'username': user.username,
                    'name': user.name,
                    'lastname': user.lastname,
                    'address': user.address,
                    'city': user.city,
                    'phone': user.phone,
                    'email': user.email,
                    'dni': user.dni,
                    'born_date': user.born_date,
                    'account': {
                        'id': account.id,                        
                        'lastChangeDate': account.lastChangeDate,
                        'isActive': account.isActive
                    }
        }