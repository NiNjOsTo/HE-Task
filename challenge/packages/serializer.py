from rest_framework import serializers
from .models import Package,Variant,Agent,Agency,Country


class VariantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = "__all__"

class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = "__all__"     

class AgentSerializer(serializers.ModelSerializer):
    agency=AgencySerializer()
    class Meta:
        model = Agent
        fields = "__all__"
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"    
class PackagesSerializer(serializers.ModelSerializer):
    variants=serializers.SerializerMethodField()
    agent = AgentSerializer()
    agency = AgencySerializer()
    country = CountrySerializer()
    def get_variants(self,obj):
        variants_query=obj.variants.all()
        return VariantsSerializer(variants_query,many=True).data
    class Meta:
        model = Package
        fields = "__all__"
