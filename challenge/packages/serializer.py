import datetime
from rest_framework import serializers
from rest_framework.response import Response
from .models import Package, Variant, Agent, Agency, Country, Date


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = "__all__"


class VariantsSerializer(serializers.ModelSerializer):
    dates = DateSerializer(many=True)

    future_dates = serializers.SerializerMethodField('get_status')

    def get_status(self, obj):
        try:

            # Create an empty list
            filter_arr = []

            for element in obj.dates.all():
                # if the element is completely divisble by 2, set the value to True, otherwise False
                if element.date > datetime.date.today():
                    print("//biger")
                    filter_arr.append(True)
                else:
                    print("//smaller")
                    # filter_arr.append(False)

            if len(filter_arr) <= 0:
                return "No Future Dates"
            else:
                return "Has Future Dates"
        except Exception as e:
            print(e)

    class Meta:
        model = Variant
        fields = "__all__"


class VariantsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ["title", "description"]


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = "__all__"


class AgentSerializer(serializers.ModelSerializer):
    agency = AgencySerializer()

    class Meta:
        model = Agent
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class PackagesSerializer(serializers.ModelSerializer):
    variants = serializers.SerializerMethodField()
    agent = AgentSerializer()
    agency = AgencySerializer()
    country = CountrySerializer()

    def get_variants(self, obj):
        variants_query = obj.variants.all()
        return VariantsSerializer(variants_query, many=True).data

    class Meta:
        model = Package
        fields = "__all__"
